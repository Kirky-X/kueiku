# Backtesting Framework

## Core Concept
Systematic backtesting pipeline: Data → Signal → Execution → Evaluation. Key metrics: Sharpe Ratio, Sortino Ratio, Calmar Ratio, Maximum Drawdown, VaR, Win Rate, Distribution analysis.

## Applicable Scenarios
✅ **Best for**
- Strategy validation
- Parameter optimization
- Overfitting detection

## Key Steps
1. **Data**: clean historical data (survivorship-bias-free, point-in-time)
2. **Signal**: define strategy rules; generate trading signals
3. **Execution**: simulate realistic execution (transaction costs, slippage, market impact)
4. **Evaluation**: calculate performance metrics (Sharpe, Sortino, Calmar, Max DD, VaR, Win Rate)
5. **Robustness**: out-of-sample testing, walk-forward analysis, parameter sensitivity
6. **Overfitting check**: if results look too good, they probably are

## Source
Systematic trading methodology; Robert Pardo, *The Evaluation and Optimization of Trading Strategies*.
