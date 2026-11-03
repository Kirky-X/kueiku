# Backtesting Framework

## Core Concept
Systematic backtesting pipeline: Data → Signal → Execution → Evaluation. Key metrics: Sharpe Ratio, Sortino Ratio, Calmar Ratio, Maximum Drawdown, VaR, Win Rate, Distribution analysis.

## Applicable Scenarios
✅ **Best for**
- Strategy validation
- Parameter optimization
- Overfitting detection

⚠️ **When NOT to use**
- Fewer than ~30 historical trades — no statistical power; the Sharpe ratio is noise and any "edge" is indistinguishable from luck
- Survivorship-biased data — a universe built from today's constituents silently inflates every result; delisted failures must be in the sample or the backtest is fiction (audit the data with **Cognitive & Statistical Bias Checklist**)
- In-sample parameter sweeps presented as validation — optimizing on the full history is curve-fitting, not testing; if you cannot hold out data, say so instead of quoting the in-sample Sharpe
- One-off, non-repeatable decisions — backtesting validates rule-based strategies only; for single uncertain calls use **Probabilistic Reasoning** or **Decision Tree & Expected Value**

## Key Steps
1. **Data**: clean historical data (survivorship-bias-free, point-in-time)
2. **Signal**: define strategy rules; generate trading signals
3. **Execution**: simulate realistic execution (transaction costs, slippage, market impact)
4. **Evaluation**: calculate performance metrics (Sharpe, Sortino, Calmar, Max DD, VaR, Win Rate)
5. **Robustness**: out-of-sample testing, walk-forward analysis, parameter sensitivity
6. **Overfitting check**: if results look too good, they probably are

## Output Template

```
Strategy: [rules, universe, rebalance frequency] — decision price: [close / next open]
Data: [source, period, point-in-time? delistings included?]
Costs modeled: [commission bps] + [slippage bps] + [impact model?]

In-sample [period]: Sharpe [x] — Max DD [x%] — Win rate [x%] — trades [n]
Out-of-sample [period]: Sharpe [x] — Max DD [x%] — trades [n]
Walk-forward: parameters [stable / drifting across folds]

Robustness: perturb each parameter ±[20%] → Sharpe range [x to y]
Too-good check: [Sharpe > 2 on liquid instruments → hunt for the bug first]
Verdict: [deploy / paper trade / discard] — reason: [the evidence cited]
```

## Failure Modes
- Lookahead bias: the signal uses data not available at decision time (restated financials, same-bar fills) → time-stamp every input; execute on the bar after the signal
- Survivorship bias: the universe excludes dead assets → rebuild point-in-time membership including delistings before trusting any metric
- Cost omission: gross Sharpe evaporates after commissions, slippage, and impact, especially at high turnover → model costs before evaluating results
- Multiple-testing overfitting: the best of many tried configurations wins by chance → count the trials, penalize the search, hold out data it never touched
- Too-good-to-be-true acceptance: exceptional results read as skill → treat a spectacular backtest as a bug report first; a green backtest still needs **Pre-mortem & Counterfactual** and paper trading before capital

## Evidence Strength
Practitioner consensus — the pipeline itself (point-in-time data, realistic costs, out-of-sample and walk-forward validation) is the standard discipline of systematic trading, with wide agreement on the major biases; the caveat cuts the other way: the headline metrics of any single backtest are weak evidence, because overfitting and cost underestimation reliably shrink live performance.

## Source
Systematic trading methodology; Robert Pardo, *The Evaluation and Optimization of Trading Strategies*.
