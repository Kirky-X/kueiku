# Risk Parity

## Core Concept
Allocate weights so each asset/strategy contributes equally to total portfolio risk, rather than equal capital. Results in more diversified risk exposure and better risk-adjusted returns.

## Applicable Scenarios
✅ **Best for**
- Risk budgeting
- Asset allocation
- Reducing concentration risk

⚠️ **When NOT to use**
- Unreliable covariance estimates (short histories, regime breaks) — the weights are only as good as the matrix; garbage covariances give confident-looking garbage
- Leveraged implementation without funding-cost awareness — risk parity often levers low-risk assets; the strategy's returns then hinge on borrow costs, not just allocations
- Very few assets (2-3) — the parity machinery degenerates; simple volatility targeting is equivalent and clearer

## Key Steps
1. Define asset classes/strategies
2. Calculate covariance matrix
3. Iteratively solve for risk parity weights (each asset's marginal risk contribution is equal)
4. Decompose total risk: verify equal risk contribution
5. Rebalance periodically as correlations change

## Output Template

```
Assets: [equities, duration bonds, commodities, credit]
Estimation window: [10y monthly] — covariance method: [sample/shrinkage]

Risk parity weights (solved): [equities 22% / bonds 50% / commodities 18% / credit 10%]
Risk contribution check: [25% / 25% / 25% / 25%] — total vol: [x%]
  (weights are NOT equal — capital tilts toward low-vol assets)

Leverage note: [amount, funding cost assumption, margin/liquidity stress]
Rebalance: [quarterly / on 20% contribution drift] — turnover estimate: [x%]
Stress check: [correlations → 1 shock: portfolio vol becomes y% — what's the plan?]
```

## Failure Modes
- Estimation-error blindness: covariance matrices from short windows flip weights at each re-estimation → use shrinkage/robust estimators and report weight sensitivity to the estimation window
- Leverage hidden in "low risk": the balanced-risk portfolio is levered; 2008-style deleveraging hits funding, not just assets → stress the funding channel explicitly before implementing
- Rebalance-by-calendar only: correlations drift within quarters — risk contributions already unequal → add contribution-drift bands alongside the calendar

## Evidence Strength
Mixed — the equal-risk-contribution math is exact, and the diversification motive is sound; empirical claims of superior risk-adjusted returns vs simple 60/40 depend heavily on sample period and leverage costs (strong in bond-bull decades, weaker elsewhere). Treat as a principled allocation framework, not a proven alpha source.

## Source
Edward Qian et al., Bridgewater's "All Weather" concept; risk parity literature.
