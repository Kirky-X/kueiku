# ML Stock Selection

## Core Concept
Use machine learning models to predict returns or classify up/down for stock selection. Features from fundamental, technical, and alternative data. Handles nonlinear factor combinations.

## Applicable Scenarios
✅ **Best for**
- Factor nonlinear combination
- High-dimensional feature stock selection
- Alpha signal discovery

⚠️ **When NOT to use**
- Small or short datasets — markets offer few independent regimes; complex models memorize noise and in-sample accuracy means nothing; start from the interpretable baseline in **Factor Investing** before reaching for ML
- No retraining and monitoring infrastructure — relationships drift (concept decay); a deployed model degrades silently while its predictions stay confident
- Non-reproducible features — if features cannot be recomputed point-in-time (restated fundamentals, revised alt-data), every backtest is lookahead-biased no matter how careful the validation
- Explaining a single pick — ML ranks, it does not explain; for why-this-company questions use **DuPont Analysis** or **DCF**

## Key Steps
1. **Feature Engineering**: build features from fundamental (DuPont ratios, etc.), technical (momentum, volatility), and alternative data
2. **Label Definition**: define prediction target (forward return, up/down classification)
3. **Model Selection**: try multiple models (Linear, Tree-based, Neural Network)
4. **Training**: cross-validation, avoid look-ahead bias, use rolling windows
5. **Evaluation**: IC, rank IC, long-short portfolio performance, turnover
6. **Deployment**: ensemble models, monitor for concept drift

## Output Template

```
Task: predict [forward x-month return / up-down] on [universe] — label: [exact definition]
Features: [n] from [fundamental / technical / alt-data] — point-in-time verified: [yes/no]

Validation: purged, embargoed rolling CV — train [period], test [period], folds [k]
Models tried: [linear / GBDT / NN] — chosen: [x] — in-sample vs OOS gap: [metric]
OOS metrics: Rank IC [x], IC_IR [x], top-decile spread [x%], turnover [x]
Net of costs: [x%] annualized — capacity estimate: [x]
Drift monitor: rolling IC decay trigger [threshold] → retrain or retire
Caveat: [regimes the training window never saw]
```

## Failure Modes
- Lookahead bias: features built from restated data, or labels overlapping training windows → point-in-time features plus purged/embargoed cross-validation
- Search-count overfitting: many model and feature combinations, best OOS result picked → lock the model before the test window and penalize the number of trials
- Concept drift: regime change invalidates learned patterns → rolling retraining, live IC monitoring, and a kill-switch on decay
- Cost blindness: high-turnover signals die after transaction costs → evaluate long-short spreads net of costs and capacity
- Over-trusted feature importance: correlated features split importance and narratives shift across seeds → check stability across seeds and models before believing any story

## Evidence Strength
Mixed — large-sample research shows ML genuinely captures nonlinear structure in returns, but the exploitable edge is thin, decays, and the default failure mode is overfitting that survives standard validation; treat any out-of-sample result as fragile until it survives live deployment.

## Source
Machine learning in finance literature; Gu, Kelly & Xiu (2020).
