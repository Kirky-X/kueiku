# Portfolio Optimization

## Core Concept
Markowitz mean-variance optimization + Black-Litterman Bayesian equilibrium. Find the optimal weight allocation that maximizes expected return for a given risk level (or minimizes risk for a given return).

## Applicable Scenarios
✅ **Best for**
- Optimal weight allocation
- Risk-return tradeoff
- Asset allocation

⚠️ **When NOT to use**
- Expected returns are guesses — MVO amplifies input error (it loads hardest on whatever was over-estimated); with unreliable inputs the "optimal" weights are confident nonsense, and **Risk Parity** or simple vol targeting is the honest choice
- Few assets, modest goals — with 3-5 assets, equal weight or vol targeting matches MVO out of sample; the optimization machinery adds fragility, not return
- Short histories relative to asset count — covariance estimation error explodes when N approaches T; without shrinkage or a factor model the matrix is noise
- Fat-tailed, skewed assets — variance understates tail risk; mean-variance is blind to how drawdowns actually arrive

## Key Steps
1. Estimate expected returns and covariance matrix
2. Define constraints (no short-selling, max weight, sector limits)
3. Run mean-variance optimization (MVO)
4. For MVO sensitivity, apply Black-Litterman: combine market equilibrium with investor views
5. Validate: check concentration, turnover, and out-of-sample performance
6. Rebalance periodically

## Output Template

```
Assets: [list] — estimation: [window, frequency], covariance: [sample / shrinkage / factor]
Expected returns: [equilibrium-implied / forecast / historical] — source of view: [x]
Constraints: [no shorts, max weight x%, sector caps, turnover limit]

MVO output: weights [..] — expected return [x%], vol [x%]
Black-Litterman: views [asset: x% ± confidence] → posterior weights [..]
Sensitivity: perturb expected returns ±[1pp] → weight swings [..] (large swings = input problem, not optimization)
Validation: OOS Sharpe [x] vs equal-weight [x] — concentration [HHI] — turnover [x%]
Rebalance: [quarterly / drift bands of x%]
```

## Failure Modes
- Error maximization: MVO concentrates on assets with over-estimated returns and under-estimated risk → constrain weights, prefer Black-Litterman or resampled inputs, and always report weight sensitivity to input perturbation
- Corner solutions: unconstrained MVO emits extreme long-short weights → impose sensible constraints (max weight, no leverage) before optimizing
- Covariance instability: sample covariance is noisy when assets outnumber observations → use shrinkage estimators or a factor covariance model
- False precision: point inputs imply a single-point answer → run sensitivity bands; if the allocation ranking flips within plausible inputs, the honest output is "indifferent"
- Static weights in a drifting world: vols and correlations move → rebalance on drift bands, not set-and-forget

## Evidence Strength
Mixed — the optimization math is exact and the framework is foundational, but MVO's out-of-sample advantage over naive equal weights is notoriously weak because it amplifies input error; Black-Litterman and constraints mitigate rather than solve this, so treat the output as a structured starting point for judgment, not the answer.

## Source
Harry Markowitz, *Portfolio Selection* (1952); Black & Litterman (1992).
