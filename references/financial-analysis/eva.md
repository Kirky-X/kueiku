# EVA — Economic Value Added

## Core Concept
EVA = NOPAT − (WACC × Invested Capital). Measures true value creation: a company creates value only when returns exceed the cost of capital.

## Applicable Scenarios
✅ **Best for**
- Performance evaluation
- Investment decisions
- Value-based management

⚠️ **When NOT to use**
- WACC noise — EVA inherits the discount-rate problem: a small WACC error flips the sign; report sensitivity before declaring "creates / destroys value"
- Early-stage or heavy-investment phases — negative EVA during build-out is by design, not destruction; judge the trajectory and returns on incremental capital, not the single-year sign
- Cross-firm comparison without normalization — invested-capital definitions and accounting choices (leases, R&D capitalization, goodwill) differ across companies; raw EVA rankings mislead
- Standalone valuation — EVA is a single-period, accounting-derived metric; for what the business is worth use **DCF**, and for market-relative pricing **Comparable Company**

## Key Steps
1. Calculate NOPAT = EBIT × (1 − Tax Rate)
2. Determine Invested Capital = Total Equity + Total Debt − Cash
3. Estimate WACC
4. Calculate EVA = NOPAT − (WACC × Invested Capital)
5. Positive EVA = value creation; Negative EVA = value destruction
6. Track EVA trends over time; diagnose drivers

## Output Template

```
Company: [x] — period: [FY]
NOPAT: EBIT [x] × (1 − tax [x%]) = [x]
Invested Capital: equity [x] + debt [x] − cash [x] = [x]
  Adjustments stated: [leases / R&D capitalization / goodwill / other: x]
WACC: [x%] — build-up: [..]
EVA = [x] − ([x%] × [x]) = [x]
Trend: EVA over [3-5y]: [x, x, x] — improving or deteriorating?
Driver diagnosis: [margin / capital efficiency / cost of capital — with numbers]
Sensitivity: EVA at WACC ±1pp: [x to x] — does the sign flip? [yes/no]
```

## Failure Modes
- Binary sign reading: one year's EVA sign treated as a verdict → read the trend and the WACC sensitivity; the sign is an estimate, not a fact
- Inconsistent invested capital: lease, R&D, and goodwill treatment differing across firms or years → fix one definition and apply it across the whole comparison
- Punishing growth investment: expansion-period EVA is negative by design → separate maintenance returns from investment-phase dilution
- WACC anchoring: choosing the rate to make the conclusion land → build it bottom-up, freeze it, then compute
- Accrual inheritance: NOPAT inherits the distortions of reported earnings → cross-check against cash-flow-based measures

## Evidence Strength
Practitioner consensus — residual income logic is coherent and EVA-based management spread widely through the 1990s corporate world; the metric reliably reframes profit against capital cost, but it inherits WACC and accounting-definition sensitivity, and claims that EVA adoption itself improves firm performance are weaker than the accounting logic behind the formula.

## Source
Stern Stewart & Co. (1990s); based on residual income theory.
