# Momentum Strategy

## Core Concept
Exploit the tendency of asset prices to continue trending. Buy past winners, sell past losers. Evaluate using multi-period returns, cross-sectional ranking, group returns, and rolling momentum.

## Applicable Scenarios
✅ **Best for**
- Trend following
- Market timing
- Rotation strategies

⚠️ **When NOT to use**
- Post-crash rebound regimes — momentum crashes are documented: past losers rip hardest in recoveries and the long-momentum book is on the wrong side; if you cannot size for that tail, step aside
- High-cost or illiquid universes — monthly rebalancing turnover burns a modest premium; test net of costs or the strategy is a cost machine
- Very short lookbacks — below roughly one month the documented effect reverses (short-term reversal); applying "momentum" there trades against the evidence
- Sideways, mean-reverting assets — trend following whipsaws in ranges; for uncertain directional calls, size exposure with **Probabilistic Reasoning** instead of extrapolating the trend

## Key Steps
1. Define lookback period (e.g. 12-1 month) and holding period
2. Calculate returns for each asset over the lookback
3. Rank assets cross-sectionally by past returns
4. Go long top decile, short bottom decile (or long-only top group)
5. Calculate group returns and test for statistical significance
6. Monitor rolling momentum; watch for momentum crashes

## Output Template

```
Universe: [assets] — lookback: [12-1m], skip: [1m], rebalance: [monthly]
Ranking: cross-sectional past return — long top [decile], short bottom [decile]

Group returns: quintile means [monotonic? yes/no] — long-short t-stat [x]
Net performance [period]: annualized [x%] — Sharpe [x] — Max DD [x%] — turnover [x]
Crash check: worst month [x%] — performance in down markets [x]
Current state: momentum percentile of held assets [..] — regime note: [rebound / chop / trend?]
Caveat: [what would make you exit — crash-filter trigger, threshold]
```

## Failure Modes
- Crash exposure: long-momentum implicitly shorts the best rebounders and crashes cluster right after bear markets → add a trend or volatility filter on the strategy itself, not just the assets
- Cost and turnover omission: small premia times monthly rebalancing → quote every result net of realistic costs
- Lookback data mining: the best in-sample lookback is overfit → test a neighborhood of lookbacks and report the sensitivity
- Skip-month omission: including the most recent month imports short-term reversal and distorts the signal → keep the standard skip unless your data says otherwise
- Cross-asset overgeneralization: momentum's strength differs by asset class and era → re-estimate per universe before sizing

## Evidence Strength
Mixed — momentum is one of the most replicated return patterns across asset classes and decades, so the effect itself is well evidenced; but the premium is modest, crash risk is real and concentrated in rebounds, and post-publication decay is documented in general terms — treat it as a risk premium paid for enduring crashes, not free money.

## Source
Jegadeesh & Titman (1993); momentum factor research.
