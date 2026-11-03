# Factor Investing

## Core Concept
Systematically capture risk premiums using multi-factor models (Fama-French etc.). Factors include Value, Momentum, Size, Quality, Low Volatility. Evaluate factors using IC, IC_IR, and group return monotonicity.

## Applicable Scenarios
✅ **Best for**
- Factor stock selection
- Portfolio construction
- Attribution analysis

⚠️ **When NOT to use**
- Sizing on raw historical premia — factor returns shrink after publication as capital crowds in; in-sample estimates overstate what remains, so haircut them or treat factors as risk exposures, not guaranteed alpha
- Single-company questions — factor models rank stocks across a universe; for one company's profitability or valuation use **DuPont Analysis**, **DCF**, or **Comparable Company**
- Thin or costly universes — small expected spreads are consumed by turnover and shorting costs; test net of costs or the "premium" is a cost machine
- Short holding horizons — factor premia arrive unevenly and multi-year drawdowns are normal; users who cannot sit through that will capitulate at the worst time

## Key Steps
1. Select factors based on theory and empirical evidence
2. Calculate factor exposures for each asset
3. Evaluate factor performance: IC (Information Coefficient), IC_IR (IC Information Ratio)
4. Test monotonicity: do 5-group returns increase/decrease monotonically?
5. Combine factors into multi-factor model
6. Construct portfolio based on factor scores

## Output Template

```
Universe: [index, point-in-time membership] — period: [x to x]
Factor definitions: [how value / momentum / quality / size / low-vol are computed, data source]

Per-factor evaluation:
  [Value]: IC [x], IC_IR [x], top-minus-bottom annual [x%], 5-group monotonic? [yes/no]
  [Momentum]: IC [x], IC_IR [x], top-minus-bottom annual [x%], 5-group monotonic? [yes/no]
Net-of-cost long-short: [x%] annualized, after turnover [x] × cost [x bps]
Multi-factor: weights [..] — factor correlation matrix [..] — combined IC_IR [x]
Portfolio: top-quintile [weights], turnover [x], expected tracking error [x]
Caveat: [which factors look crowded or decayed; minimum holding discipline]
```

## Failure Modes
- Data mining: test enough factors and some "work" by chance → demand an economic rationale before any test, and count the trials run
- Non-point-in-time data: restated fundamentals or today's constituents leak the future → use as-reported data and delisting-inclusive universes
- Gross-of-cost evaluation: high-turnover signals die after costs → report IC and long-short spreads net of realistic costs
- Crowding risk: everyone holds the same factors and unwinds are correlated (momentum-crash style) → monitor factor valuation spreads and size modestly

## Evidence Strength
Contested — factor premia were strong in the samples that discovered them, but post-publication decay, multiple-testing concerns, and crowding are documented in general terms, so today's net premia are smaller and less certain than the classic estimates; the strongest defensible use is as a risk-exposure and diversification lens, with any alpha claim sized conservatively.

## Source
Eugene Fama & Kenneth French, Fama-French 3-factor model (1992); factor investing literature.
