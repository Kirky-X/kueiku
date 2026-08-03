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

## Source
Lean Analytics (Croll & Yoskovitz); standard product analytics methodology.
