# Cohort Analysis · Cohort Analysis

## Core Idea
Split the "average retention rate" into cohort retention curves grouped by time — group users by their first use time (e.g., "January registrants" as one group), and track each group's retention at W1/W2/W4/W8. Averages mask differences between cohorts, while a cohort view reveals "whether new user retention is improving/worsening".

## Applicable Scenarios
- Overall retention rate appears stable but is actually deteriorating
- Evaluating the impact of product changes on users from different periods
- Determining whether PMF is achieved (cohort curves should level off rather than continue declining)

## Key Steps
1. Choose cohort dimension: by registration time (most common) / by first payment time / by channel source
2. Choose time window: weekly (high‑frequency products) / monthly (B2B or low‑frequency products)
3. Calculate each cohort's retention rate at W1/W2/W4/W8/W12
4. Look horizontally at a single cohort curve: where does the drop‑off concentrate (first week? second week?)
5. Look vertically at period‑over‑period comparison: does W4 retention improve as cohorts progress (product improvements taking effect)
6. Combine with engagement trends: is the usage frequency of retained users also increasing

## Source
Standard PM analytics practices (promoted by Amplitude/Mixpanel etc.)