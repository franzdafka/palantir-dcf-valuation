# Palantir Technologies (NASDAQ: PLTR) — DCF Valuation

A bottom-up, 10-year discounted cash flow model, built as a portfolio piece for investment banking / markets internship applications. Palantir is one of the more genuinely contested valuations in public markets right now — a ~55x trailing EV/Sales, high-conviction AI-platform story trading on execution that has, so far, kept beating even raised guidance. The goal of this project is not to prove PLTR is cheap or expensive, but to show a disciplined, defensible process for valuing a company like this, and to engage honestly with why reasonable people land in very different places on it.

**Data as of:** August 3–4, 2026, refreshed to include Palantir's Q2 2026 earnings release (reported August 3, 2026, after market close).

---

## Executive Summary

| Scenario | Estimated intrinsic value per share (blended) |
|---|---|
| Bear | $42.50 |
| Base | $67.39 |
| Bull | $114.48 |

**vs. current market price: $144.45** (Aug 3, 2026 after-hours, immediately following the Q2 print) / **$125.65** (last regular-session close, pre-earnings).

The headline finding is uncomfortable for a bull, and that discomfort is the point of the exercise: under every scenario built here — including the Bull case, which assumes Palantir sustains 85%+ commercial growth into next year, fades more slowly than Base, and reaches a 47% terminal GAAP operating margin — the model's blended intrinsic value comes in **below** both the pre- and post-earnings market price. Even the single most optimistic building block in the model (the "still-growth" 15.5x EV/Sales exit multiple, applied to a Bull-case Year-10 revenue base of $76.4B) produces a per-share value of roughly $148 on its own before discounting — and once that terminal value is discounted back 10 years at an ~11.3% WACC, it collapses to a fraction of that.

This is not a verdict that the stock is overvalued — a rigorous DCF on a 10-year-out, still-unprofitable-by-normal-standards-adjusted-for-multiple business is inherently a blunt instrument, and the gap here is informative about *what has to be true* for today's price to be fair, not proof that it isn't. Section 4 below ("Why This Is a Hard Valuation") works through that reconciliation directly: to justify ~$144/share, the market is implicitly underwriting some combination of (a) a materially lower cost of capital than this model's CAPM build supports, (b) sustained hyper-growth well past what a 10-year fade to 6–12% terminal growth captures, or (c) an exit multiple meaningfully above even this model's "still-growth" 15.5x case. None of those are unreasonable bets on Palantir specifically — its recent execution has been genuinely exceptional — but they are bets, not base-rate assumptions, and a defensible valuation model should say so plainly rather than reverse-engineering assumptions to hit the market price.

---

## 1. Methodology

### 1.1 Structure

- **10-year explicit forecast** (FY2027E–FY2036E), not the more conventional 5-year window. Palantir's current growth (56% FY2025, 93% actual Q2 2026 YoY) is too far from a plausible mature terminal rate (mid-to-high single digits for Government, low double digits for Commercial) to fade credibly in 5 years without either understating near-term momentum or wildly overstating Year-5 scale.
- **Two segments modeled and faded independently — Government and Commercial** — rather than a single blended growth rate. This is one of the two judgment calls that matter most in this model (the other is SBC treatment, below), because the two segments have genuinely different economics, competitive dynamics, and ceilings:
  - **Government**: durable multi-year relationships, high switching costs, but growth is inherently capped by federal/allied procurement cycles and budget authorization timing. Modeled fading from an estimated ~32–48% Year-1 (FY2027E) growth rate (scenario-dependent) down toward a 5–7% terminal rate by Year 10.
  - **Commercial**: the current growth engine (Q2 2026 global commercial revenue +110% YoY; US commercial +149% YoY), reflecting genuine AI-platform differentiation and land-and-expand economics, but not treated as sustaining hyper-growth indefinitely. Modeled fading from an estimated ~55–85% Year-1 growth rate down toward an 8–12% terminal rate by Year 10.
  - Each segment's fade path is built as an exponential decay toward its terminal rate — `growth(t) = terminal + (Year1 − terminal) × e^(−k×(t−1))` — with the decay speed **k** set independently per segment *and* per scenario (Bear fades fastest, Bull slowest), so the three scenarios differ in shape, not just in a single multiplier applied to one output.

- **Unlevered FCF build**: Revenue → EBIT → NOPAT → (+) D&A → (−) Capex → (−) increase in NWC → Unlevered FCF, run separately for Bear / Base / Bull on dedicated model tabs (not a single toggled sheet), so all three cases are visible and auditable simultaneously.

- **Terminal value, both methods, side by side**: Gordon Growth (2.5–4.0% perpetuity growth, scenario-dependent) and Exit Multiple (7.5x EV/Sales "matured-to-market" vs. 15.5x EV/Sales "still-growth," sourced from current peer multiples — see §1.3).

- **WACC via bottom-up CAPM**, not a screener number — see §1.2.

### 1.2 SBC treatment — the other judgment call that matters

This model **fully expenses stock-based compensation**: Unlevered FCF is built on GAAP EBIT, which already reflects SBC as a real cost, and SBC is **not** added back as a non-cash item. This is a deliberate and, in my view, the more defensible choice for a company where SBC has historically run 15–30% of revenue — treating it as a "non-cash" add-back the way many bullish sell-side notes and retail commentary do systematically overstates free cash flow, because it ignores the real dilution that cost imposes on existing shareholders.

Separately, and **without double-counting**, the model tracks a diluted share count roll-forward — growing from the recent ~3.2%/year net issuance trend down toward 0–1%/year by Year 10 as buybacks scale with FCF (scenario-dependent: Bear stays more dilutive, Bull assumes buybacks roughly offset new issuance by Year 10). This schedule is shown for transparency on the dilution trend but is **not** used as the per-share divisor for the DCF output — doing so on top of fully-expensed SBC would double-count the same economic cost twice (once through lower EBIT, again through a larger share count). The per-share value in this model divides today's equity value by today's diluted share count, which is the standard, non-double-counting convention once SBC is fully expensed.

The **`SBC Addback Comparison`** tab in the workbook shows exactly what the alternative, non-GAAP-addback convention would produce, side by side with this model's basis: **$44.82/share (GAAP-expensed, this model's Base-case Gordon Growth output) vs. $55.14/share (non-GAAP, SBC added back)** — a **+23% uplift** from switching conventions alone, with every other input held identical. That gap is the "bull-case shortcut" this project was asked to address head-on: it's a real, mechanical inflation of intrinsic value that comes purely from an accounting convention choice, not from any difference in the underlying business.

### 1.3 Terminal value inputs

- **Gordon Growth**: 2.5% (Bear) / 3.0% (Base) / 3.5% (Bull) perpetuity growth — deliberately kept *below* each segment's Year-10 fade-curve growth rate, reflecting further long-run convergence toward nominal-GDP-like growth beyond the explicit window.
- **Exit Multiple**: 7.5x EV/Sales (low, "matured-to-market") in line with ServiceNow (~7.4x EV/Sales, a mature enterprise-software leader), and 15.5x EV/Sales (high, "still-growth") roughly the midpoint of CrowdStrike (~18.9x NTM) and Snowflake (~13–21x depending on measure/date). Sourced from current peer data — see `/data/market_and_wacc_inputs.csv`.

---

## 2. WACC

Built bottom-up via CAPM, not pulled from a screener:

| Input | Value | Source |
|---|---|---|
| Risk-free rate (10Y UST) | 4.69% | 10Y Treasury yield, Aug 3, 2026 |
| Equity risk premium | 4.23% | Damodaran implied ERP, early-Aug 2026 update |
| Beta (5Y raw, primary case) | 1.56 | stockanalysis.com |
| Cost of equity | **11.29%** | Rf + β×ERP |
| Pre-tax cost of debt | 5.5% | Estimate (PLTR's ~$212mm of debt-like obligations are immaterial and don't carry a quoted market yield) |
| Tax rate | 25% | Normalized marginal rate |
| **WACC** | **~11.28%** | Within ~5bps of cost of equity, given PLTR's minimal debt weight |

**Beta is genuinely disputed.** Five-year raw beta runs from ~1.56 (stockanalysis.com, used here as the primary case) to as high as ~2.02 on other data providers, reflecting differences in return-interval, benchmark, and lookback-window choices for a stock with PLTR's volatility and comparatively short trading history. At a 4.23% ERP, that range alone moves cost of equity from ~11.3% to ~13.2% — a swing that materially changes the per-share output through the Gordon Growth formula, since PV of terminal value is highly convex in the WACC-minus-growth spread. **This is why the WACC × terminal-growth sensitivity grid should be weighed at least as heavily as the single base-case headline number** — for a stock like PLTR, the "right" WACC is itself a live debate, not a settled input.

PLTR carries minimal debt (~$212mm) against a large net cash position (~$9.0B as of Q2 2026), so WACC sits within basis points of cost of equity — there was no need to force an artificial capital structure to make the CAPM math interesting.

---

## 3. Key Assumptions

| Driver | Bear | Base | Bull | Why |
|---|---|---|---|---|
| Government Yr-1 (FY2027E) growth | 32% | 42% | 48% | Faded down from Q2'26 actual global government growth of +79% YoY; even Bull assumes meaningful near-term deceleration off an unusually strong print. |
| Government terminal (Yr-10) growth | 5% | 6% | 7% | Procurement-cycle-constrained, mature-vendor pace; kept below long-run nominal GDP growth. |
| Government fade speed (k) | 0.75 (fastest) | 0.60 | 0.42 (slowest) | Bear assumes budget-cycle/concentration risk bites early; Bull assumes durable multi-year contract structures sustain growth longer. |
| Commercial Yr-1 (FY2027E) growth | 55% | 70% | 85% | Faded down from Q2'26 actual global commercial growth of +110% YoY (US commercial +149%). |
| Commercial terminal (Yr-10) growth | 8% | 10% | 12% | Durable AI-platform advantage assumed, but not indefinite hyper-growth. |
| Commercial fade speed (k) | 0.80 (fastest) | 0.65 | 0.50 (slowest) | Bear assumes cheaper point-solution competitors compress growth quickly; Bull assumes platform lock-in and expansion revenue sustain growth longer. |
| Terminal GAAP EBIT margin (Yr-10) | 31% | 42% | 47% | Bear: competitive pricing pressure and heavier S&M spend to defend share. Base: modest further operating leverage on top of an already-elevated FY2026E base. Bull: best-in-class mature-SaaS operating leverage. |
| Gordon terminal growth (g) | 2.5% | 3.0% | 3.5% | Within the specified 2.5–4% range; below each segment's own Year-10 fade rate. |
| Net share issuance, Yr-1 → Yr-10 | 3.2% → 1.5% | 3.2% → 0.5% | 3.2% → 0.0% | Recent trailing dilution (~3.2%/yr) held as the common starting point; fade speed reflects how much buyback capacity each scenario's FCF generates. Shown for transparency only — not used as the per-share divisor (see §1.2). |

Tax rate (25%), D&A (2.0% of revenue), capex (2.0% of revenue), and incremental-NWC use (3.0% of incremental revenue) are held constant across scenarios; the FY2026E anchor revenue split between segments ($3,555mm Government / $4,599mm Commercial, summing to the ~$8,154mm midpoint of FY2026 guidance) is likewise a shared estimate, since Palantir does not guide segment-level revenue for the full year.

---

## 4. Why This Is a Hard Valuation

**The bull case, briefly stated:** Palantir has built genuinely durable government relationships (some dating back to the Gotham era) that are hard for a startup competitor to replicate, and it is now converting that platform and trust into a rapidly expanding commercial AI business — US commercial revenue growth accelerated to 149% YoY in Q2 2026, and Rule-of-40 scores above 150% suggest the growth is not being bought with margin. Operating leverage is real and visible in the numbers: GAAP operating margin has expanded from -8.5% (FY2022) to an estimated 38%+ (Q1 2026 TTM) to a likely 40%+ handle in Q2 2026, and management continues to raise guidance rather than merely meet it. If Palantir is actually building the "operating system" for enterprise AI deployment — not just another point-solution vendor — a 10-year fade to single-digit-to-low-double-digit terminal growth may understate the durability of the moat, and a premium exit multiple in the high teens is not unreasonable for a company still compounding at that pace a decade out.

**The bear case, just as briefly:** PLTR trades at roughly 55x trailing EV/Sales and a 77x forward P/E — multiples that price in near-flawless execution for years, leaving very little margin for a growth disappointment, a large customer loss, or a macro-driven pullback in enterprise software spending. SBC dilution, even fully expensed in this model's UFCF build, is a real and ongoing transfer of value away from existing shareholders (~15% of revenue currently). Government revenue — still nearly half the business — carries real concentration risk around a relatively small number of large contracts and is exposed to US federal budget and procurement politics in a way most software companies are not. And competition is intensifying from both directions: hyperscalers (Microsoft, Google, Amazon) are bundling AI orchestration into their existing enterprise relationships, while a wave of cheaper, more focused point solutions is emerging to attack specific pieces of Palantir's commercial workflow.

**The reconciliation this model surfaces:** even this model's Bull case — 85% Commercial Year-1 growth, a slow 0.50 fade constant, a 47% terminal margin, and a 15.5x exit multiple applied to a $76B Year-10 revenue base — produces a blended value of $114.48/share, still ~21% below the post-earnings market price. Closing that gap requires pushing at least one input to its outer edge relative to what this model treats as defensible: a WACC near the low end of the beta-dispersion range (using β≈1.2–1.3 rather than 1.56–2.02), an exit multiple materially above 15.5x (i.e., PLTR trading like the market's single best-in-class software franchise a decade from now, not merely a strong one), or sustained growth that doesn't fade as fast as even the Bull case assumes. None of these are crazy bets on Palantir specifically given its recent track record — but they are the bets an investor buying at $144+ is implicitly making, and this model's job was to make that explicit rather than to quietly assume it.

---

## 5. Limitations — what could make this valuation wrong

- **Beta dispersion (1.56–2.02)** is the single largest source of uncertainty in the WACC, and WACC is the single largest lever on the output given the 10-year discounting horizon. See the WACC × g sensitivity grid.
- **FY2026E segment revenue split is an estimate.** Palantir guides total revenue only; the $3,555mm Government / $4,599mm Commercial anchor split is derived from the FY2026 guidance midpoint and Q2 2026 YTD segment growth proportions, not a company-disclosed figure.
- **Q2 2026 SBC and diluted share count are proxied from Q1 2026 10-Q data**, because the Q2 2026 10-Q had not yet been filed with the SEC as of this run (filings typically follow ~40–45 days after quarter-end). If Q2 SBC came in meaningfully different from the Q1 run-rate, both the SBC memo schedule and (less materially) the WACC's capital-structure inputs would shift.
- **Tax rate is a normalized 25% marginal rate**, not PLTR's actual near-term cash tax rate, which is currently lower due to NOL carryforwards from its unprofitable years. This makes the model's near-term NOPAT somewhat conservative relative to actual near-term cash taxes, and somewhat aggressive relative to the eventual rate once NOLs are exhausted — the two effects partially offset but don't exactly cancel.
- **The two-segment fade curves are a modeling simplification**, not a forecast Palantir would sign off on. Real-world growth doesn't decay smoothly along an exponential curve — it moves in lumps tied to specific large contract wins/losses, particularly on the Government side.
- **D&A, capex, and NWC assumptions are estimates** (2.0% / 2.0% / 3.0% of incremental revenue respectively) based on PLTR's historically asset-light model, not detailed line-item forecasts; a shift toward heavier AI-infrastructure capex (a real possibility given the compute intensity of the products PLTR sells) would pressure UFCF below what's modeled here.
- **The Sensitivity tab's second grid (long-term growth × terminal margin) uses a simplified flat-CAGR proxy** for Year-10 revenue rather than re-running the full two-segment fade curve for every cell — it isolates terminal-value sensitivity cleanly but will not exactly reproduce the Base case's own Year-10 output. This is disclosed on the tab itself.
- **Historical data gaps**: FY2023/2024 GAAP operating margin, SBC, and free cash flow figures are sourced via financial-data aggregators (cross-checked against total-revenue figures) rather than independently re-pulled from each year's primary 10-K text this run; FY2023–2025 diluted share counts are linearly interpolated between two verified endpoints (FY2022 and Q1 2026). All flagged explicitly in `/data/historical_financials.csv`.
- **This is a snapshot valuation as of Aug 3–4, 2026**, immediately after a strong Q2 print and a 15% after-hours stock move. Both the "current market price" used for comparison and some Q2-specific inputs will look stale quickly for a stock this volatile.

---

## Files

```
/palantir-dcf-valuation
  /model
    Palantir_DCF_Model.xlsx       — full DCF (Cover, Summary Output, Data Summary, WACC,
                                     Assumptions, Model - Bear/Base/Bull, Sensitivity,
                                     SBC Addback Comparison)
  /data
    historical_financials.csv     — FY2022-Q2 2026 financials, sourced line-by-line
    market_and_wacc_inputs.csv    — market data, CAPM inputs, peer multiples, sourced
  README.md                       — this file
```

**Font color key in the workbook:** blue = hardcoded input/source figure · black = formula · green = link to another tab.
