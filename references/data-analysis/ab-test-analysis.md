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

⚠️ **When NOT to use**
- Many simultaneous changes that may interact — a two-arm test cannot separate their effects; use factorial or sequential designs, and read the result as a bundle-level answer rather than a per-change one
- Individual-level assignment impossible (campaigns spanning regions, stores, or time periods) → randomize at the **geo/cluster level** and analyze cluster-level outcomes; for time-varying treatments use switchback designs — the power, SRM, and decision machinery below apply unchanged, only the unit of randomization changes
- Reading results before the pre-registered decision point — peeking converts a pre-registered test into a search for a lucky read; fix the sample size and the stopping rule first, then look
- Outcomes that cannot be observed soon enough to decide — if the metric takes a season to move, the experiment buys delay instead of an answer; ship and monitor instead
- Instrument changes or other measurement artifacts riding along with the treatment — novelty, notification, or instrumentation effects can dominate the signal → audit the data path with **Cognitive & Statistical Bias Checklist** before trusting the read

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

## Failure Modes
- Peeking and early stopping: the result is read daily and the test is stopped at the first favorable p-value → set the sample size and the duration in advance, or use a sequential design built for repeated looks
- Unplanned multiple comparisons: several metrics or several segments are tested and only the winner is reported → count the comparisons actually run, correct the alpha, and pre-register the primary metric
- Metric gaming: a proxy that can be moved without moving value → pair the primary metric with a guardrail metric that cannot be moved cheaply, and read both
- Sample ratio mismatch ignored: the assignment path is broken, so the arms are not comparable no matter how small the p-value → treat any SRM as fatal; stop, debug the allocation and logging, then rerun
- Underpowered test read as a null result: "not significant" is reported as "no effect" → report the confidence interval and the power; a wide interval is an unknown, not a zero

## Evidence Strength
Strong — the randomization core is the most rigorously validated method in this corpus: random assignment with pre-registration genuinely identifies causal effect, the estimators are standard statistics, and the failure conditions are documented and fixable. The caveat is that validity is lost in practice far more often than in theory: peeking, unplanned multiple comparisons, metric gaming, and an ignored sample-ratio mismatch routinely convert a well-designed test into a confident wrong answer, which is why pre-registration, multiplicity correction, and the SRM check have to be treated as binding rather than optional.

## Source
Standard statistical methodology; Ron Kohavi et al., *Trustworthy Online Controlled Experiments*.
