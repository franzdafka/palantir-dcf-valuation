# Palantir Technologies (NASDAQ: PLTR) — DCF Valuation

A bottom-up, 10-year discounted cash flow model, built as a portfolio piece for investment banking / markets internship applications. Palantir is one of the more genuinely contested valuations in public markets right now — a ~55x trailing EV/Sales, high-conviction AI-platform story trading on execution that has, so far, kept beating even raised guidance. The goal of this project is not to prove PLTR is cheap or expensive, but to show a disciplined, defensible process for valuing a company like this, and to engage honestly with why reasonable people land in very different places on it.

**Data as of:** August 3–4, 2026, refreshed to include Palantir's Q2 2026 earnings release (reported August 3, 2026, after market close), with a follow-up verification pass against primary SEC filings on August 4, 2026 — see "Updates Since Original Build" at the bottom of this file.

---

## Executive Summary

| Scenario | Estimated intrinsic value per share (blended) |
|---|---|
| Bear | $43.22 |
| Base | $68.32 |
| Bull | $115.75 |

**vs. current market price: $144.45** (Aug 3, 2026 after-hours, immediately following the Q2 print) / **$125.65** (last regular-session close, pre-earnings).

The headline finding is uncomfortable for a bull, and that discomfort is the point of the exercise: under every scenario built here — including the Bull case, which assumes Palantir sustains 85%+ commercial growth into next year, fades more slowly than Base, and reaches a 47% terminal GAAP operating margin — the model's blended intrinsic value comes in **below** both the pre- and post-earnings market price. Even isolating the single most optimistic component in the model — the Bull scenario's "still-growth" 15.5x EV/Sales exit-multiple method on its own, before blending with the more conservative Gordon Growth method — produces $191.56/share undiscounted-equivalent terminal value per share; once the full 10-year explicit period is built out and everything is discounted at the model's ~11.3% WACC, the *blended* Bull output is $115.75/share, still roughly 20% below the post-earnings market price.

This is not a verdict that the stock is overvalued — a rigorous DCF on a 10-year-out, still-unprofitable-by-normal-standards-adjusted-for-multiple business is inherently a blunt instrument, and the gap here is informative about *what has to be true* for today's price to be fair, not proof that it isn't. Section 4 below ("Why This Is a Hard Valuation") works through that reconciliation directly: to justify ~$144/share, the market is implicitly underwriting some combination of (a) a materially lower cost of capital than this model's CAPM build supports, (b) sustained hyper-growth well past what a 10-year fade to 6–12% terminal growth captures, or (c) an exit multiple meaningfully above even this model's "still-growth" 15.5x case. None of those are unreasonable bets on Palantir specifically — its recent execution has been genuinely exceptional — but they are bets, not base-rate assumptions, and a defensible valuation model should say so plainly rather than reverse-engineering assumptions to hit the market price.

---

## 1. Methodology

### 1.1 Structure

- **10-year explicit forecast** (FY2027E–FY2036E), not the more conventional 5-year window. Palantir's current growth (56% FY2025, 93% actual Q2 2026 YoY) is too far from a plausible mature terminal rate (mid-to-high single digits for Government, low double digits for Commercial) to fade credibly in 5 years without either understating near-term momentum or wildly overstating Year-5 scale.
- **Two segments modeled and faded independently — Government and Commercial** — rather than a single blended growth rate. This is one of the judgment calls that matters most in this model (the others are SBC treatment and the FY2026E margin anchor, both below), because the two segments have genuinely different economics, competitive dynamics, and ceilings:
  - **Government**: durable multi-year relationships, high switching costs, but growth is inherently capped by federal/allied procurement cycles and budget authorization timing. Modeled fading from an estimated ~32–48% Year-1 (FY2027E) growth rate (scenario-dependent) down toward a 5–7% terminal rate by Year 10.
  - **Commercial**: the current growth engine (Q2 2026 global commercial revenue +110% YoY; US commercial +149% YoY), reflecting genuine AI-platform differentiation and land-and-expand economics, but not treated as sustaining hyper-growth indefinitely. Modeled fading from an estimated ~55–85% Year-1 growth rate down toward an 8–12% terminal rate by Year 10.
  - Each segment's fade path is built as an exponential decay toward its terminal rate — `growth(t) = terminal + (Year1 − terminal) × e^(−k×(t−1))` — with the decay speed **k** set independently per segment *and* per scenario (Bear fades fastest, Bull slowest), so the three scenarios differ in shape, not just in a single multiplier applied to one output.

- **Unlevered FCF build**: Revenue → EBIT → NOPAT → (+) D&A → (−) Capex → (−) increase in NWC → Unlevered FCF, run separately for Bear / Base / Bull on dedicated model tabs (not a single toggled sheet), so all three cases are visible and auditable simultaneously.

- **Terminal value, both methods, side by side**: Gordon Growth (2.5–4.0% perpetuity growth, scenario-dependent) and Exit Multiple (7.5x EV/Sales "matured-to-market" vs. 15.5x EV/Sales "still-growth," sourced from current peer multiples — see §1.3).

- **WACC via bottom-up CAPM**, not a screener number — see §2.

### 1.2 SBC treatment — the judgment call that matters most

This model **fully expenses stock-based compensation**: Unlevered FCF is built on GAAP EBIT, which already reflects SBC as a real cost, and SBC is **not** added back as a non-cash item. This is a deliberate and, in my view, the more defensible choice for a company where SBC has historically run 15–30% of revenue — treating it as a "non-cash" add-back the way many bullish sell-side notes and retail commentary do systematically overstates free cash flow, because it ignores the real dilution that cost imposes on existing shareholders.

Separately, and **without double-counting**, the model tracks a diluted share count roll-forward — growing from the recent ~3.2%/year net issuance trend down toward 0–1%/year by Year 10 as buybacks scale with FCF (scenario-dependent: Bear stays more dilutive, Bull assumes buybacks roughly offset new issuance by Year 10). This schedule is shown for transparency on the dilution trend but is **not** used as the per-share divisor for the DCF output — doing so on top of fully-expensed SBC would double-count the same economic cost twice (once through lower EBIT, again through a larger share count). The per-share value in this model divides today's equity value by today's diluted share count, which is the standard, non-double-counting convention once SBC is fully expensed.

The **`SBC Addback Comparison`** tab in the workbook shows exactly what the alternative, non-GAAP-addback convention would produce, side by side with this model's basis: **$45.73/share (GAAP-expensed, this model's Base-case Gordon Growth output) vs. $56.06/share (non-GAAP, SBC added back)** — a **+22.6% uplift** from switching conventions alone, with every other input held identical. That gap is the "bull-case shortcut" this project was asked to address head-on: it's a real, mechanical inflation of intrinsic value that comes purely from an accounting convention choice, not from any difference in the underlying business.

### 1.3 FY2026E margin anchor — updated with actual H1 2026 results

The forecast's Year-0 (FY2026E) GAAP operating margin anchor is **45.5%**, built up from Palantir's *actual* H1 2026 results rather than a pre-earnings estimate: H1 2026 GAAP operating margin came in at 46.70% ($1,666.0mm on $3,568.0mm revenue, per the Q2 2026 8-K). Blending that actual with an H2 2026E estimate implied from the raised FY2026 guidance (revenue $8.150–8.158B; adjusted operating income $4.889–4.897B, ≈60% adjusted margin; less an estimated ~14.4% of revenue for SBC and related payroll tax, consistent with the H1 actual ratio) gives a full-year GAAP margin of approximately 45.7%, rounded to 45.5% here. Terminal (Year 10) margins by scenario are **held at their original, externally-benchmarked levels** (31% Bear / 42% Base / 47% Bull — see §3) rather than shifted up in lockstep with the anchor, since those represent absolute mature-SaaS-peer reference points, not a fixed offset from wherever the company happens to be today. One consequence worth being explicit about: with a higher starting point, the **Base case now models modest margin *normalization* from an elevated H1 base**, not further expansion — a more conservative and, I'd argue, more honest read of the current print than assuming today's unusually strong margin simply keeps compounding.

### 1.4 Terminal value inputs

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
| Pre-tax cost of debt | 5.5% | Estimate (PLTR's debt-like obligations are immaterial and don't carry a quoted market yield) |
| Tax rate | 25% | Normalized marginal rate |
| **WACC** | **~11.28%** | Within ~5bps of cost of equity, given PLTR's minimal debt weight |

**Beta is genuinely disputed.** Five-year raw beta runs from ~1.56 (stockanalysis.com, used here as the primary case) to as high as ~2.02 on other data providers, reflecting differences in return-interval, benchmark, and lookback-window choices for a stock with PLTR's volatility and comparatively short trading history. At a 4.23% ERP, that range alone moves cost of equity from ~11.3% to ~13.2% — a swing that materially changes the per-share output through the Gordon Growth formula, since PV of terminal value is highly convex in the WACC-minus-growth spread. **This is why the WACC × terminal-growth sensitivity grid should be weighed at least as heavily as the single base-case headline number** — for a stock like PLTR, the "right" WACC is itself a live debate, not a settled input.

PLTR carries no funded debt — the ~$183–212mm figure used in the capital-structure build across periods is noncurrent operating lease liabilities, not financial debt — against a large net cash position (~$9.0–9.2B as of Q2 2026), so WACC sits within basis points of cost of equity.

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
| Anchor GAAP EBIT margin (FY2026E, all scenarios) | 45.5% | 45.5% | 45.5% | Built up from actual H1 2026 GAAP margin (46.7%) blended with H2 2026E implied from raised guidance — see §1.3. Updated from an original pre-earnings estimate of 41%. |
| Terminal GAAP EBIT margin (Yr-10) | 31% | 42% | 47% | Bear: competitive pricing pressure and heavier S&M spend to defend share. Base: modest margin *normalization* from the elevated FY2026E anchor, not further expansion (see §1.3). Bull: best-in-class mature-SaaS operating leverage. Held at original, externally-benchmarked absolute levels, not shifted with the anchor. |
| Gordon terminal growth (g) | 2.5% | 3.0% | 3.5% | Within the specified 2.5–4% range; below each segment's own Year-10 fade rate. |
| Net share issuance, Yr-1 → Yr-10 | 3.2% → 1.5% | 3.2% → 0.5% | 3.2% → 0.0% | Recent trailing dilution (~3.2%/yr) held as the common starting point; fade speed reflects how much buyback capacity each scenario's FCF generates. Shown for transparency only — not used as the per-share divisor (see §1.2). |

Tax rate (25%), D&A (2.0% of revenue), capex (2.0% of revenue), and incremental-NWC use (3.0% of incremental revenue) are held constant across scenarios; the FY2026E anchor revenue split between segments ($3,555mm Government / $4,599mm Commercial, summing to the ~$8,154mm midpoint of the twice-raised FY2026 guidance) is likewise a shared estimate, since Palantir does not guide segment-level revenue for the full year.

---

## 4. Why This Is a Hard Valuation

**The bull case, briefly stated:** Palantir has built genuinely durable government relationships (some dating back to the Gotham era) that are hard for a startup competitor to replicate, and it is now converting that platform and trust into a rapidly expanding commercial AI business — US commercial revenue growth accelerated to 149% YoY in Q2 2026, and the Rule-of-40 score climbed to 155%, suggesting the growth is not being bought with margin. Operating leverage is real and visible in the numbers: GAAP operating margin has expanded from -8.5% (FY2022) to 46.7% (H1 2026 actual) to 47.1% in Q2 2026 alone, and management continues to raise guidance rather than merely meet it. If Palantir is actually building the "operating system" for enterprise AI deployment — not just another point-solution vendor — a 10-year fade to single-digit-to-low-double-digit terminal growth may understate the durability of the moat, and a premium exit multiple in the high teens is not unreasonable for a company still compounding at that pace a decade out.

**The bear case, just as briefly:** PLTR trades at roughly 55x trailing EV/Sales and a 77x forward P/E — multiples that price in near-flawless execution for years, leaving very little margin for a growth disappointment, a large customer loss, or a macro-driven pullback in enterprise software spending. SBC dilution, even fully expensed in this model's UFCF build, is a real and ongoing transfer of value away from existing shareholders (~14% of revenue in H1 2026). Government revenue — still roughly half the business — carries real concentration risk around a relatively small number of large contracts and is exposed to US federal budget and procurement politics in a way most software companies are not. And competition is intensifying from both directions: hyperscalers (Microsoft, Google, Amazon) are bundling AI orchestration into their existing enterprise relationships, while a wave of cheaper, more focused point solutions is emerging to attack specific pieces of Palantir's commercial workflow.

**The reconciliation this model surfaces:** even this model's Bull case — 85% Commercial Year-1 growth, a slow 0.50 fade constant, a 47% terminal margin, and a 15.5x exit multiple applied to a Year-10 revenue base compounded at that pace — produces a blended value of $115.75/share, still roughly 20% below the post-earnings market price. Closing that gap requires pushing at least one input to its outer edge relative to what this model treats as defensible: a WACC near the low end of the beta-dispersion range (using β≈1.2–1.3 rather than 1.56–2.02), an exit multiple materially above 15.5x (i.e., PLTR trading like the market's single best-in-class software franchise a decade from now, not merely a strong one), or sustained growth that doesn't fade as fast as even the Bull case assumes. None of these are crazy bets on Palantir specifically given its recent track record — but they are the bets an investor buying at $144+ is implicitly making, and this model's job was to make that explicit rather than to quietly assume it.

---

## 5. Limitations — what could make this valuation wrong

- **Beta dispersion (1.56–2.02)** is the single largest source of uncertainty in the WACC, and WACC is the single largest lever on the output given the 10-year discounting horizon. See the WACC × g sensitivity grid.
- **FY2026E segment revenue split is an estimate.** Palantir guides total revenue only; the $3,555mm Government / $4,599mm Commercial anchor split is derived from the FY2026 guidance midpoint and Q2 2026 YTD segment growth proportions, not a company-disclosed figure.
- **The FY2026E margin anchor (45.5%) blends an H1 2026 actual with an H2 2026E estimate** derived from guidance and an assumed constant SBC-and-payroll-tax ratio (see §1.3) — it is a reasoned build-up, not itself a company-disclosed full-year figure, and the actual H2 print could land meaningfully above or below this estimate.
- **Tax rate is a normalized 25% marginal rate**, not PLTR's actual near-term cash tax rate, which is currently lower due to NOL carryforwards from its unprofitable years. This makes the model's near-term NOPAT somewhat conservative relative to actual near-term cash taxes, and somewhat aggressive relative to the eventual rate once NOLs are exhausted — the two effects partially offset but don't exactly cancel.
- **The two-segment fade curves are a modeling simplification**, not a forecast Palantir would sign off on. Real-world growth doesn't decay smoothly along an exponential curve — it moves in lumps tied to specific large contract wins/losses, particularly on the Government side.
- **D&A, capex, and NWC assumptions are estimates** (2.0% / 2.0% / 3.0% of incremental revenue respectively) based on PLTR's historically asset-light model, not detailed line-item forecasts; a shift toward heavier AI-infrastructure capex (a real possibility given the compute intensity of the products PLTR sells) would pressure UFCF below what's modeled here.
- **The Sensitivity tab's second grid (long-term growth × terminal margin) uses a simplified flat-CAGR proxy** for Year-10 revenue rather than re-running the full two-segment fade curve for every cell — it isolates terminal-value sensitivity cleanly but will not exactly reproduce the Base case's own Year-10 output. This is disclosed on the tab itself.
- **Remaining historical data gaps**: FY2023 US-segment revenue split and the FY2023 cash+securities balance are still sourced via financial-data aggregators rather than independently pulled from the primary 10-K text. Everything else in the historical table (FY2022–2025 GAAP margins, SBC, FCF, diluted share counts, and Q2 2026 actuals) was independently verified against primary SEC filings during the August 4, 2026 verification pass — see the changelog below and `/data/historical_financials.csv` for the full sourcing trail.
- **This is a snapshot valuation as of Aug 3–4, 2026**, immediately after a strong Q2 print and a 15% after-hours stock move. Both the "current market price" used for comparison and some Q2-specific inputs will look stale quickly for a stock this volatile.

---

## Updates Since Original Build (Aug 4, 2026 verification pass)

The model was originally built on the evening of Aug 3–4, 2026, immediately after Palantir's Q2 2026 earnings release, using the Q2 8-K's headline bullet points plus Q1 2026 figures as interim proxies for anything not in those bullets. A follow-up verification pass against primary SEC filings (the FY2024 8-K Ex-99.1, the FY2025 8-K Ex-99.1, and the full Q2 2026 8-K Ex-99.1 financial tables, not just the highlights section) found and corrected the following:

- **Font-color convention** — the workbook's stated blue/black/green convention (hardcode / formula / cross-sheet link) was only partially applied; all cross-sheet-referencing formula cells across every tab have been corrected to green.
- **FY2026E anchor GAAP operating margin** updated from a pre-earnings estimate (41%) to a build-up from actual H1 2026 results (45.5%) — see §1.3. This is the one change that moves the headline output: Base blended value rose from $67.39 to $68.32, Bull from $114.48 to $115.75, Bear from $42.50 to $43.22. The modest size of that shift, despite a meaningful margin re-estimate, is itself informative: it shows this 10-year DCF is terminal-value-dominated, and near-term margin assumptions matter far less than the terminal growth, terminal margin, and WACC assumptions already stress-tested in the Sensitivity tab.
- **Q2 2026 SBC and diluted share count** replaced with actual verified figures ($265.2mm and 2,568.7mm) from the Q2 2026 8-K's full financial statements, rather than the Q1 2026 interim proxies used in the original build.
- **Q2 2026 GAAP operating margin (47.1%) and gross margin (84.7%)** added — these were in the Q2 8-K's full income statement but not its headline bullet list, so the original build had flagged them "not available."
- **FY2023 and FY2024 GAAP operating income, GAAP operating margin, SBC, free cash flow, and diluted share counts** replaced with figures verified directly against the primary Q4 2024 8-K Ex-99.1 comparative statements, resolving several original "approximate, aggregator-sourced" flags. The FY2023/2024 free cash flow figures in particular were corrected upward (FY2023: $656.9mm → $697.1mm; FY2024: $1,101.5mm → $1,141.2mm).
- **FY2025 cash + marketable securities and net cash** corrected from $8,030mm (which had been mistakenly copied from the Q1 2026 balance sheet) to the actual Dec 31, 2025 figure of $7,177.0mm, verified against the FY2025 8-K balance sheet.
- **FY2025 net income** corrected from a derived estimate ($1,633.5mm, backed out from a rounded margin) to the actual reported figure ($1,625.0mm).
- Added a simple Bear/Base/Bull-vs-market-price chart to the Summary Output tab.

Full detail and exact source citations for every correction are in `/data/historical_financials.csv`.

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
