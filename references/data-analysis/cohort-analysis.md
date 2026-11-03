# Cohort Analysis

## Core Concept
Track user retention by grouping users into cohorts (typically by signup date) and measuring how many remain active over time. Reveals whether retention is improving, stable, or declining — a key PMF signal.

## Applicable Scenarios
✅ **Best for**
- Is retention improving over time?
- PMF (Product-Market Fit) assessment
- Identifying drop-off patterns and engagement trends

⚠️ **Use with caution**
- Very new products without enough cohort history
- Highly seasonal products where cohort timing biases results

⚠️ **When NOT to use**
- The question is causal, not descriptive — cohort curves show what happened to a group, never why; a change in the curve needs a controlled comparison → **A/B Test Analysis**
- The behavior is not recurring — a one-off purchase, a single event, or a lifetime-value read has no retention curve to trace → **RFM Model** for value segmentation
- Cohort cells are too thin to compare — small groups turn a retention difference into sampling noise; set a minimum cell size before reading the matrix
- Seasonality dominates the comparison — a holiday cohort is being compared against a normal one; align periods before concluding anything about the trend

## Key Steps
1. Define cohort grouping (typically by signup week/month)
2. For each cohort, track active users at each subsequent period (Week 1, Week 2, etc.)
3. Calculate retention rate = active users in period N / initial cohort size
4. Build a cohort retention matrix (cohorts as rows, periods as columns)
5. Look for patterns: are newer cohorts retaining better? Is there a drop-off cliff?

## Output Template
```
Cohort Retention Matrix:
           Period 1   Period 2   Period 3   ...
Cohort A:   100%       60%        45%
Cohort B:   100%       65%        52%
Cohort C:   100%       70%        ??

PMF Signal: [improving/stable/declining] retention trend
Key Insight: [notable pattern or anomaly]
```

## Failure Modes
- Undefined "active": the retention curve measures whatever the event definition happens to be → define the active event once, in measurable terms, and keep it stable across cohorts
- Definition changed mid-flight: a definitional change looks exactly like a retention improvement → freeze the definition per reporting period and flag any change next to the matrix
- Counts compared instead of rates: the largest cohort looks like the best-retaining one → normalize by initial cohort size and always show both the rate and the denominator
- Newest cohort read as a failure: a row observed for one week is not a decline, it is an unfinished row → compare only the periods that every cohort has reached

## Evidence Strength
Mixed — cohort retention is descriptive accounting over observed data with no randomization, so it can show whether retention is changing but never why; the matrix itself is reliable arithmetic given a stable definition and adequate cell sizes. Its main weaknesses are definitional drift (what counts as active) and the standing temptation to read a descriptive trend as a causal one, and its predictive reach is limited because it describes the cohorts that have already arrived rather than the ones yet to come — use it for trend and PMF signals and pair it with a controlled design for any causal claim.

## Source
Lean Analytics (Croll & Yoskovitz); standard product analytics methodology.
