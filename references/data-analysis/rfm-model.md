# RFM Model

## Core Concept
Segment users along 3 transaction-based dimensions: Recency (how recently they purchased), Frequency (how often), Monetary (how much they spend). Users are scored on each dimension and classified into 8 segments for targeted marketing.

## Applicable Scenarios
✅ **Best for**
- User tiering and segmentation
- Precision marketing strategies
- Churn early warning
- User value assessment

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

## Source
Direct marketing analytics; standard CRM methodology.
