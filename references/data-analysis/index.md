# Data Analysis

**When to use**: Retention analysis, A/B testing, metrics framework

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Cohort Analysis** | Cohort retention curves + drop-off patterns + engagement trends | Is retention improving, PMF assessment | `cohort-analysis.md` |
| **A/B Test Analysis** | Sample size + statistical significance + Ship/Extend/Stop/Investigate + SRM detection | A/B test design and decision | `ab-test-analysis.md` |
| **Lean Analytics Metrics** | 4 criteria + 8 metric types + NSM 4 layers | Metrics framework selection, good metric criteria | `lean-analytics-metrics.md` |
| **RFM Model** | Recency/Frequency/Monetary 3-dimension user segmentation | User tiering, precision marketing, churn early warning, user value assessment | `rfm-model.md` |
| **Cognitive & Statistical Bias Checklist** | Lifecycle bias checklist (design → collection → interpretation → reporting), each bias with trigger signal + check action | Reviewing an analysis before acting on it; metric/experiment design quality | `debias-checklist.md` |

## Minimum Information Requirements per Methodology

- **Cohort Analysis**: Requires user retention data grouped by time
- **A/B Test Analysis**: Requires A/B testing platform + statistics foundation
- **Lean Analytics Metrics**: Requires dashboard data + NSM candidates
- **RFM Model**: Requires user transaction data (last purchase date / purchase frequency / spend amount)
- **Cognitive & Statistical Bias Checklist**: Requires the analysis or metric design under review (question, data source, sampling mechanism, conclusions)

## Routing Trigger Signals

- "Cohort retention analysis" → Cohort Analysis (primary)
- "A/B test design and decision" → A/B Test Analysis (primary)
- "Metrics framework selection / good metric criteria" → Lean Analytics Metrics (primary)
- "User tiering / precision marketing / churn early warning / user value assessment" → RFM Model (primary)
- "Is this analysis trustworthy / bias check on findings / review before acting on data" → Cognitive & Statistical Bias Checklist (primary)

## Common Combinations

- **User value operations**: RFM Model (tiering) → Cohort Analysis (retention evolution) → A/B Test (strategy validation)
- **Growth analysis**: Lean Analytics Metrics (select metrics) → Cohort Analysis (check retention) → RFM Model (tiered operations)
- **Findings trust gate**: Cognitive & Statistical Bias Checklist (catch threats to validity) → A/B Test Analysis (verify the causal claim)
- **Retention audit**: Cohort Analysis (retention curves) → Cognitive & Statistical Bias Checklist (check survivorship in who is counted)
