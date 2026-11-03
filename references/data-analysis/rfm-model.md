# RFM Model

## Core Concept
Segment users along 3 transaction-based dimensions: Recency (how recently they purchased), Frequency (how often), Monetary (how much they spend). Users are scored on each dimension and classified into 8 segments for targeted marketing.

## Applicable Scenarios
✅ **Best for**
- User tiering and segmentation
- Precision marketing strategies
- Churn early warning
- User value assessment

⚠️ **When NOT to use**
- Recency and frequency are not the axes of the business — a subscription, a daily-use app, or a marketplace buyer expresses value through something RFM never measures → **Cohort Analysis** for behavior over time
- There is no transaction history — new users, or a business whose value is not transacted, cannot be scored → fall back to engagement-based segmentation
- The scoring cutoffs are inherited from a textbook — quantiles computed on a distribution that has shifted with the business produce segments that quietly mean something different each quarter → recompute and re-label on a schedule
- Individual-level action decisions that need causal support — RFM says who bought, not what will make them act → validate the treatment with **A/B Test Analysis** before rolling it out

## Key Steps
1. Collect transaction data: customer_id, recency (days since last purchase), frequency (total purchases), monetary (total spend)
2. For each dimension, assign quantile scores (1-5 or 1-10)
3. Combine R/F/M scores into 8 user segments: Champions, Loyal, Potential Loyalist, Recent, Promising, Need Attention, At Risk, Lost
4. Design targeted strategies per segment
5. Monitor segment migration over time

## Output Template
```
RFM Segmentation:
  Champions:       [count] — strategy: [reward & refer]
  Loyal:           [count] — strategy: [upsell & cross-sell]
  Potential Loyal: [count] — strategy: [engage more]
  Recent:          [count] — strategy: [build habit]
  Promising:       [count] — strategy: [increase frequency]
  Need Attention:  [count] — strategy: [re-engage]
  At Risk:         [count] — strategy: [win-back campaign]
  Lost:            [count] — strategy: [reactivate or release]
```

## Failure Modes
- Stale cutoffs: the scores are computed once and reused as the customer base shifts → recompute on a fixed schedule and version the segmentation so old and new segments stay comparable
- Recency truncation: users with no recent purchase are folded into "Lost" even when they were the largest buyers → segment churners by historical value before treating them as one group
- Equal-weight percentile scores: one point of Frequency and one point of Recency may be worth very different amounts of money → weight or re-band the dimensions against their actual business impact
- Labels read as causes: "At Risk" describes past behavior, not the reason for it → test the win-back treatment on a holdout instead of assuming the segment responds
- Segment sizes quoted without denominators: "3,000 At Risk users" says nothing about whether that group grew → always report the segment as a share of the base alongside its count

## Evidence Strength
Practitioner consensus — RFM is a long-established direct-marketing technique with a large operational base, and the underlying logic (recent, frequent, and high-value customers respond differently to contact and to offers) is consistent with long-standing customer-value practice. The evidence is largely campaign-performance experience rather than controlled studies, and the segment boundaries are analyst-chosen quantile cutoffs rather than discovered structure, so the result depends heavily on the recency window, the scoring scheme, and whether the segments map onto treatments that were ever shown to work.

## Source
Direct marketing analytics; standard CRM methodology.
