# Data Analysis · Data Analysis

**Applicable Scenarios**: Retention analysis, A/B testing, metric systems

| Methodology | One‑sentence description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Cohort Analysis** | Cohort retention curves + drop‑off patterns + engagement trends | Whether retention is improving, PMF judgment | `cohort-analysis.md` |
| **A/B Test Analysis** | Sample size + statistical significance + Ship/Extend/Stop/Investigate + SRM detection | A/B test design and decision‑making | `ab-test-analysis.md` |
| **Lean Analytics Metrics** | 4 criteria + 8 metric types + NSM four‑level framework | Metric system selection, good‑metric criteria | `lean-analytics-metrics.md` |
| **RFM Model** | Recency/Frequency/Monetary three‑dimension user segmentation | User stratification, precision marketing, churn prediction, user value assessment | `rfm-model.md` |

## Minimum Information Requirements for Each Methodology

- **Cohort Analysis**: Requires time‑grouped user retention data
- **A/B Test Analysis**: Requires an A/B testing platform + statistical fundamentals
- **Lean Analytics Metrics**: Requires dashboard data + NSM candidates
- **RFM Model**: Requires user transaction data (last purchase date / purchase count / spending amount)

## Routing Trigger Signals

- "Cohort retention analysis" → Cohort Analysis (primary)
- "A/B test design and decision‑making" → A/B Test Analysis (primary)
- "Metric system selection / good‑metric criteria" → Lean Analytics Metrics (primary)
- "User stratification / precision marketing / churn prediction / user value assessment" → RFM Model (primary)

## Common Combinations

- **User value operations**: RFM Model (stratification) → Cohort Analysis (retention evolution) → A/B Test (strategy validation)
- **Growth analysis**: Lean Analytics Metrics (select metrics) → Cohort Analysis (observe retention) → RFM Model (stratified operations)