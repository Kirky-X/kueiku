# DCF — Discounted Cash Flow

## Core Concept
Enterprise value equals the sum of all future free cash flows discounted to present value. The most fundamental intrinsic valuation method.

## Applicable Scenarios
✅ **Best for**
- Enterprise valuation
- Investment decisions
- M&A pricing

⚠️ **When NOT to use**
- Unforecastable cash flows — early-stage, commodity-cyclical, or fast-disrupted businesses make the 10-year projection fiction; use scenario bounds (**Probabilistic Reasoning**, **Scenario Planning**) instead of a point-estimate DCF
- Terminal-value domination — when the terminal value carries most of the enterprise value, the "analysis" is one far-future assumption in present-value clothing; test that assumption directly rather than polishing the FCF table
- Indefensible WACC — a one-point change in the discount rate swings value enormously; if the rate is a guess, the output is a range at best
- Pricing-to-market questions — DCF answers intrinsic value for a long-term owner; for what the market will pay today (IPO windows, trading ranges) **Comparable Company** is the more direct tool

## Key Steps
1. Project free cash flows (FCF) for 5-10 years
2. Estimate WACC (Weighted Average Cost of Capital)
3. Calculate terminal value (Gordon Growth or Exit Multiple)
4. Discount all cash flows to present value using WACC
5. Sum PV of FCFs + PV of terminal value = Enterprise Value
6. Conduct sensitivity analysis on key assumptions (growth rate, WACC, terminal multiple)

## Output Template

```
Company: [x] — FCF definition: [state SBC / capex / working-capital treatment]
Projection [5-10y]: revenue CAGR [x%] — margin path [x% → x%] — reinvestment [x%]
WACC: [x%] — build-up: risk-free [x] + ERP [x] × beta [x] + size/other premiums [x] + after-tax cost of debt [x]
Terminal: [Gordon g = x% / exit multiple x] — PV share of EV: [x%] (flag if above ~60-70%)
Sensitivity: EV range across [g × WACC] grid: [low – high]
Verdict: value per share [x] vs price [x] — margin of safety [x%]
Assumption register: [the 2-3 assumptions the answer actually hinges on]
```

## Failure Modes
- Assumption laundering: growth and margin guesses dressed up as analysis → keep an assumption register and report the value range, not a point estimate
- Terminal-value tyranny: terminal value above ~70% of EV means the explicit forecast is decoration → shorten the horizon with an exit multiple, or state and stress the far-future assumption explicitly
- WACC arbitrage: picking the discount rate after seeing the desired valuation → build the WACC bottom-up and freeze it before computing value
- FCF definition drift: inconsistent treatment of SBC, capex, or working capital across years or companies → fix one definition, document it, apply it everywhere
- False precision: "worth $47.32" — the model's decimal places exceed its information content → present the sensitivity band as the answer

## Evidence Strength
Mixed — DCF is the theoretically correct intrinsic-value framework and the reference point of corporate finance, but its outputs are extremely assumption-sensitive: terminal value typically dominates the result and WACC shifts move value enormously, so two honest analysts applying the same method get different numbers; the honest deliverable is a defensible range plus the assumptions that drive it.

## Source
Standard finance methodology; Irving Fisher (1907), modernized by McKinsey.
