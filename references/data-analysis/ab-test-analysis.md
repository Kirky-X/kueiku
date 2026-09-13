# A/B Test Analysis

## Core Concept
Statistical comparison of two or more variants to determine if observed differences are statistically significant. Includes sample size calculation, significance testing, decision framework (Ship/Extend/Stop/Investigate), and SRM (Sample Ratio Mismatch) detection.

The `abtest` script analyzes 3+ variant inputs as follows: the first two variants get the primary analysis (z-test, SRM, decision); every additional variant is explicitly summarized and compared against the control in a separate "Additional Variants" section — never silently dropped. For 3+ variant decisions, correct for multiplicity (e.g. Bonferroni α = 0.05 / number of comparisons).

## Applicable Scenarios
✅ **Best for**
- A/B test design and decision-making
- Determining if a change has a real effect
- Comparing multiple treatment variants

⚠️ **Use with caution**
- Very small sample sizes (underpowered tests)
- Multiple metrics without correction (multiple comparisons problem)

## Key Steps
1. Define hypothesis: H0 (no difference) and H1 (expected difference)
2. Calculate required sample size (power analysis)
3. Run test, collect data per variant
4. Check SRM: actual vs expected sample ratios (chi-squared test, χ² > 3.841 at α = 0.05, df = 1)
5. Run statistical test (z-test for proportions, t-test for continuous)
6. Apply decision framework: Ship / Extend / Stop / Investigate

## Output Template
```
A/B Test Results:
Variant A: [users] [conversions] [rate]
Variant B: [users] [conversions] [rate]

Statistical Test:
  p-value: [...]
  Confidence interval: [...]
  SRM check: [PASS/FAIL]

Decision: [Ship/Extend/Stop/Investigate]
Reason: [...]
```

## Source
Standard statistical methodology; Ron Kohavi et al., *Trustworthy Online Controlled Experiments*.
