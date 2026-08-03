# Portfolio Optimization

## Core Concept
Markowitz mean-variance optimization + Black-Litterman Bayesian equilibrium. Find the optimal weight allocation that maximizes expected return for a given risk level (or minimizes risk for a given return).

## Applicable Scenarios
✅ **Best for**
- Optimal weight allocation
- Risk-return tradeoff
- Asset allocation

## Key Steps
1. Estimate expected returns and covariance matrix
2. Define constraints (no short-selling, max weight, sector limits)
3. Run mean-variance optimization (MVO)
4. For MVO sensitivity, apply Black-Litterman: combine market equilibrium with investor views
5. Validate: check concentration, turnover, and out-of-sample performance
6. Rebalance periodically

## Source
Harry Markowitz, *Portfolio Selection* (1952); Black & Litterman (1992).
