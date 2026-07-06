# A/B Test Analysis · A/B Test Analysis

## Core Idea
A/B testing is not "just pick the version with higher numbers" — you need to calculate sample size beforehand, test statistical significance afterward, follow a standard decision matrix, and detect SRM (Sample Ratio Mismatch), a subtle but fatal error.

## Applicable Scenarios
- Product iterations require data‑driven rather than intuition‑based decisions
- A/B test results are "close" and you don’t know whether to ship
- Test results are counter‑intuitive and you need to check if the method was wrong

## Key Steps
1. Calculate sample size beforehand: based on MDE (Minimum Detectable Effect) + baseline conversion rate + significance level (α=0.05) + Power (β=0.8) using lookup tables
2. Run the test until sample size is met, **do not stop early** (this invalidates statistical validity)
3. Detect SRM (Sample Ratio Mismatch): if actual sample ratio deviates from the designed ratio by >1%, SRM exists and results are unreliable — investigate first
4. Test statistical significance: p < 0.05 and effect size ≥ MDE to be considered valid
5. Decision matrix:
   - Significant positive + sufficient business value → **Ship**
   - Significant positive but small effect → **Extend** (expand test scope or find amplification scenarios)
   - Significant negative → **Stop**
   - Not significant → **Investigate** (split by segment to see if any sub‑group is significant)
6. Record test hypothesis/results/decision in the experiment repository

## Source
Statistics (Neyman‑Pearson hypothesis testing framework); A/B testing practice see Ronny Kohavi "Trustworthy Online Controlled Experiments"