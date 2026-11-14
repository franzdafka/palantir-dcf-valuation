"""Reverse DCF: what does the market price imply?

Rebuilds the Base case from the inputs in model/Palantir_DCF_Model.xlsx
(checked against the workbook's own output), then solves, one lever at a
time and holding everything else at Base, for the value of each assumption
that makes the Gordon Growth DCF equal the market price.

    python analysis/reverse_dcf.py

Writes analysis/reverse_dcf.json and docs/sensitivity_wacc_g.png.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
import openpyxl
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "model" / "Palantir_DCF_Model.xlsx"
DOCS = ROOT / "docs"


@dataclass(frozen=True)
class Inputs:
    gov0: float
    com0: float
    gov_y1: float
    gov_term: float
    gov_k: float
    com_y1: float
    com_term: float
    com_k: float
    margin0: float
    margin_term: float
    tax: float
    da: float
    capex: float
    nwc: float
    g: float
    wacc: float
    exit_low: float
    exit_high: float
    net_cash: float
    shares: float
    price: float
    extra_growth: float = 0.0  # added to every year's growth in both segments (reverse-DCF lever)


def load_base_inputs() -> tuple[Inputs, dict[str, float]]:
    wb = openpyxl.load_workbook(MODEL, data_only=True)
    a, w, m = wb["Assumptions"], wb["WACC"], wb["Model - Base"]
    inputs = Inputs(
        gov0=a["C45"].value, com0=a["C46"].value,
        gov_y1=a["D7"].value, gov_term=a["D8"].value, gov_k=a["D9"].value,
        com_y1=a["D13"].value, com_term=a["D14"].value, com_k=a["D15"].value,
        margin0=a["D19"].value, margin_term=a["D20"].value,
        tax=a["C23"].value, da=a["C24"].value, capex=a["C25"].value, nwc=a["C26"].value,
        g=a["D40"].value, wacc=w["C29"].value,
        exit_low=a["C41"].value, exit_high=a["C42"].value,
        net_cash=a["C50"].value, shares=a["C51"].value, price=a["C52"].value,
    )
    workbook_values = {}
    for row in m.iter_rows(min_col=2, max_col=3):
        label, value = row[0].value, row[1].value
        if label == "Value per Share — Gordon Growth":
            workbook_values["gordon"] = value
        elif label == "Value per Share — Exit Multiple, low":
            workbook_values["exit_low"] = value
        elif label == "Value per Share — Exit Multiple, high":
            workbook_values["exit_high"] = value
    return inputs, workbook_values


def fade(y1: float, term: float, k: float, extra: float) -> np.ndarray:
    t = np.arange(1, 11)
    return term + (y1 - term) * np.exp(-k * (t - 1)) + extra


def build(p: Inputs) -> dict[str, float | np.ndarray]:
    gov = p.gov0 * np.cumprod(1 + fade(p.gov_y1, p.gov_term, p.gov_k, p.extra_growth))
    com = p.com0 * np.cumprod(1 + fade(p.com_y1, p.com_term, p.com_k, p.extra_growth))
    revenue = gov + com
    prev = np.r_[p.gov0 + p.com0, revenue[:-1]]
    margin = p.margin0 + (p.margin_term - p.margin0) * np.arange(1, 11) / 10
    nopat = revenue * margin * (1 - p.tax)
    ufcf = nopat + p.da * revenue - p.capex * revenue - p.nwc * (revenue - prev)
    disc = (1 + p.wacc) ** -np.arange(1, 11)
    pv_explicit = float(ufcf @ disc)
    tv_gordon = ufcf[-1] * (1 + p.g) / (p.wacc - p.g)
    per_share = lambda tv: (pv_explicit + tv * disc[-1] + p.net_cash) / p.shares
    return {
        "revenue": revenue,
        "ufcf": ufcf,
        "pv_explicit": pv_explicit,
        "gordon": per_share(tv_gordon),
        "exit_low": per_share(p.exit_low * revenue[-1]),
        "exit_high": per_share(p.exit_high * revenue[-1]),
        "disc10": disc[-1],
    }


def solve(p: Inputs, field: str, lo: float, hi: float) -> float:
    f = lambda x: build(replace(p, **{field: x}))["gordon"] - p.price
    return brentq(f, lo, hi)


def main() -> None:
    base, workbook = load_base_inputs()
    b = build(base)
    for key in ("gordon", "exit_low", "exit_high"):
        assert abs(b[key] - workbook[key]) < 0.05, (key, b[key], workbook[key])

    rev_cagr = (b["revenue"][-1] / (base.gov0 + base.com0)) ** 0.1 - 1
    implied_wacc = solve(base, "wacc", base.g + 0.005, base.wacc)
    implied_g = solve(base, "g", base.g, base.wacc - 0.001)
    implied_extra = solve(base, "extra_growth", 0.0, 0.3)
    implied_rev = build(replace(base, extra_growth=implied_extra))["revenue"][-1]
    implied_cagr = (implied_rev / (base.gov0 + base.com0)) ** 0.1 - 1
    implied_margin = solve(base, "margin_term", base.margin_term, 3.0)
    # Exit-multiple method: EV/Sales on Year-10 revenue that gives the market price.
    needed_tv_pv = base.price * base.shares - base.net_cash - b["pv_explicit"]
    implied_exit = needed_tv_pv / b["disc10"] / b["revenue"][-1]

    out = {
        "market_price": base.price,
        "base_gordon_value": round(b["gordon"], 2),
        "checks_vs_workbook": {k: [round(b[k], 3), round(workbook[k], 3)] for k in workbook},
        "levers": [
            {"lever": "WACC", "base": base.wacc, "implied": implied_wacc},
            {"lever": "Terminal growth g", "base": base.g, "implied": implied_g},
            {"lever": "Revenue CAGR FY26-FY36", "base": rev_cagr, "implied": implied_cagr},
            {"lever": "Year-10 revenue ($bn)", "base": b["revenue"][-1] / 1e3, "implied": implied_rev / 1e3},
            {"lever": "Terminal EBIT margin", "base": base.margin_term, "implied": implied_margin},
            {"lever": "Exit EV/Sales on Year-10 revenue", "base": None, "implied": implied_exit},
        ],
    }
    (ROOT / "analysis" / "reverse_dcf.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))
    plot_sensitivity(base)


def plot_sensitivity(base: Inputs) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    waccs = np.arange(0.073, 0.1431, 0.01)
    gs = np.arange(0.02, 0.0451, 0.005)
    grid = np.array([[build(replace(base, wacc=w, g=g))["gordon"] for g in gs] for w in waccs])
    DOCS.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    im = ax.imshow(grid, cmap="Blues", aspect="auto", vmin=0, vmax=base.price)
    for i in range(len(waccs)):
        for j in range(len(gs)):
            v = grid[i, j]
            ax.text(j, i, f"${v:.0f}", ha="center", va="center", fontsize=9,
                    color="white" if v > base.price * 0.55 else "black",
                    fontweight="bold" if abs(waccs[i] - 0.113) < 1e-3 and abs(gs[j] - 0.03) < 1e-3 else None)
    ax.set_xticks(range(len(gs)), [f"{g:.1%}" for g in gs])
    ax.set_yticks(range(len(waccs)), [f"{w:.1%}" for w in waccs])
    ax.set_xlabel("Terminal growth g")
    ax.set_ylabel("WACC")
    ax.set_title(f"Base case value per share (Gordon Growth) vs market price ${base.price:.2f}",
                 loc="left", fontsize=10, fontweight="bold")
    fig.colorbar(im, ax=ax, label="$ per share (scale ends at market price)")
    fig.tight_layout()
    fig.savefig(DOCS / "sensitivity_wacc_g.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
