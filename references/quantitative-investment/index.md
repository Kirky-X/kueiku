# Quantitative Investment

**When to use**: Need to make investment decisions based on data and models, build portfolios, evaluate strategy returns and risks

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Factor Investing** | Systematically capturing risk premiums based on Fama-French multi-factor models | Factor stock selection, portfolio construction, attribution analysis | `factor-investing.md` |
| **Portfolio Optimization** | Markowitz mean-variance + Black-Litterman Bayesian equilibrium | Optimal weight allocation, risk-return tradeoff | `portfolio-optimization.md` |
| **Risk Parity** | Allocate weights by equal risk contribution, not by capital proportion | Risk budgeting, asset allocation, reducing concentration | `risk-parity.md` |
| **Momentum Strategy** | Capturing excess returns from asset price trend continuation | Trend following, timing, rotation strategies | `momentum-strategy.md` |
| **Statistical Arbitrage** | Mean-reversion pairs/basket trading based on statistical relationships | Market-neutral strategies, pairs trading, cointegration | `statistical-arbitrage.md` |
| **Backtesting Framework** | Systematic backtesting pipeline: Data→Signal→Execution→Evaluation | Strategy validation, parameter optimization, overfitting detection | `backtesting-framework.md` |
| **ML Stock Selection** | Using machine learning models to predict returns / classify up-down for stock selection | Factor nonlinear combination, high-dimensional feature stock selection | `ml-stock-selection.md` |

## Minimum Information Requirements per Methodology

- **Factor Investing**: Asset historical return data + factor exposure data + factor return data
- **Portfolio Optimization**: Asset expected returns + covariance matrix + constraints (short-selling restrictions, etc.)
- **Risk Parity**: Asset class/strategy historical return series + covariance matrix
- **Momentum Strategy**: Asset historical price series + lookback/holding period parameters
- **Statistical Arbitrage**: Pair/basket asset historical prices + cointegration test data
- **Backtesting Framework**: Strategy signal definition + historical market data + transaction cost assumptions
- **ML Stock Selection**: Feature engineering data (fundamental/technical/alternative data) + label definition (returns/up-down)

## Routing Trigger Signals

- "Factor stock selection / multi-factor model / alpha factor / factor exposure / attribution analysis" → Factor Investing (primary)
- "Optimal portfolio / asset allocation / weight optimization / efficient frontier / risk-return tradeoff" → Portfolio Optimization (primary)
- "Risk budget / risk contribution / risk equalization / all-weather / reducing concentration" → Risk Parity (primary)
- "Momentum / trend following / rotation / chase-rising-sell-falling / price trend" → Momentum Strategy (primary)
- "Pairs trading / statistical arbitrage / cointegration / mean reversion / market neutral" → Statistical Arbitrage (primary)
- "Strategy backtesting / historical validation / overfitting / Sharpe ratio / maximum drawdown" → Backtesting Framework (primary)
- "Machine learning stock selection / AI stock selection / feature engineering / prediction model / nonlinear factor" → ML Stock Selection (primary)

## Common Combinations

- **Systematic quantitative strategy**: Factor Investing (factor selection) → Portfolio Optimization (weight optimization) → Backtesting Framework (strategy validation)
- **Risk-oriented allocation**: Risk Parity (risk budget) → Momentum Strategy (tactical enhancement) → Backtesting Framework (effectiveness validation)
- **Alpha strategy development**: Statistical Arbitrage (signal generation) → Backtesting Framework (backtest validation) → ML Stock Selection (signal enhancement)
- **Fundamental quantitative**: Factor Investing (factor construction) → ML Stock Selection (nonlinear combination) → Portfolio Optimization (portfolio construction)
