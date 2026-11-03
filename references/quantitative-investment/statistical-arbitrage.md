# Statistical Arbitrage

## Core Concept
Mean-reversion trading based on statistical relationships between assets. Pairs trading (2 assets) or basket trading (multiple assets). Uses cointegration tests to identify stable relationships.

## Applicable Scenarios
✅ **Best for**
- Market-neutral strategies
- Pairs trading
- Cointegration-based trading

⚠️ **When NOT to use**
- Pairs found by scanning, not economics — cointegration discovered by testing thousands of candidate pairs is mostly coincidence (multiple testing); demand a one-sentence economic reason the spread must revert
- Structural-change environments — mergers, regulation, or business-model shifts permanently break relationships; a passed test says nothing about tomorrow
- Thin spreads with heavy turnover — entries and exits are frequent; borrow costs, dividends, and slippage can consume the entire edge; net-of-cost test or skip
- Risk-averse capital seeking "market-neutral" safety — neutrality is statistical, not absolute; spreads blow up and both legs lose together, so size the worst case with **Probabilistic Reasoning**

## Key Steps
1. Identify candidate pairs/baskets with economic relationship
2. Test for cointegration (Engle-Granger or Johansen test)
3. Model the spread: z-score = (spread - mean) / std
4. Define entry/exit rules: enter when z > threshold, exit when z reverts
5. Backtest: check Sharpe ratio, maximum drawdown, turnover
6. Monitor: cointegration can break down; set stop-losses

## Output Template

```
Pair/basket: [A, B] — economic link: [one sentence on why the spread must mean-revert]
Cointegration: [Engle-Granger / Johansen, p-value, test period] — half-life: [x days]
Spread model: z = (spread − mean) / std — current z: [x]
Entry: [|z| > x] — exit: [z → 0] — stop: [|z| > x or structural event]
Backtest net of costs: Sharpe [x] — Max DD [x%] — trades [n] — avg holding [x days]
Borrow/funding: [available? cost bps] — dividends treatment: [x]
Breakdown plan: [stop-loss, max holding period, monitoring trigger]
Caveat: [what regime change would kill this pair]
```

## Failure Modes
- Data-mined pairs: scanning thousands of candidates finds fake cointegration → select the pair on economic grounds first, then test, and disclose the search
- Regime change: cointegration is an in-sample property and breaks without warning → live monitoring, hard stop-loss, exit on structural events
- Cost omission: small spreads, high turnover, borrow costs → only net-of-cost Sharpe counts
- Tail blindness: spreads can diverge far beyond historical std before reverting, or never → size for spread blowup, not for the historical distribution
- Factor overlap across the book: many "neutral" pairs share common exposures and the aggregate book carries concentrated factor bets → check factor exposures of the whole portfolio; pair-by-pair neutrality is not enough

## Evidence Strength
Mixed — the statistical machinery (cointegration testing, spread z-scores) is sound and the methodology is well established among practitioners, but documented profitability is era- and market-dependent, decays with crowding, and lives or dies on cost discipline; any specific pair's historical Sharpe should be treated as fragile evidence.

## Source
Statistical arbitrage literature; pairs trading methodology.
