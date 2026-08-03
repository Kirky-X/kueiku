# Statistical Arbitrage

## Core Concept
Mean-reversion trading based on statistical relationships between assets. Pairs trading (2 assets) or basket trading (multiple assets). Uses cointegration tests to identify stable relationships.

## Applicable Scenarios
✅ **Best for**
- Market-neutral strategies
- Pairs trading
- Cointegration-based trading

## Key Steps
1. Identify candidate pairs/baskets with economic relationship
2. Test for cointegration (Engle-Granger or Johansen test)
3. Model the spread: z-score = (spread - mean) / std
4. Define entry/exit rules: enter when z > threshold, exit when z reverts
5. Backtest: check Sharpe ratio, maximum drawdown, turnover
6. Monitor: cointegration can break down; set stop-losses

## Source
Statistical arbitrage literature; pairs trading methodology.
