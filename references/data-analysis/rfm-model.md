# RFM Model · RFM Model

## Core Concept

Use **Recency** (last purchase time), **Frequency** (purchase frequency), and **Monetary** (spending amount) three dimensions to segment users, identify high‑value users, churn‑risk users, new users, etc., to support precision operations. RFM is a classic quantitative model for user stratification, which better captures user state than simple monetary‑based segmentation.

> RFM's advantage: can be calculated using only transaction data, no complex user profiles needed; the three dimensions together depict "user's current value + future tendency".

```
              M (Spending Amount)
              High
              │   ★ High‑value users (R high F high M high)
              │   ★ High‑retention users (R low F high M high)
              │
              │   ★ High‑growth users (R high F low M high)
              │   ★ High‑win‑back users (R low F low M high)
              ┼────────────── F (Purchase Frequency)
              │
              │   ★ General‑value users (R high F high M low)
              │   ★ General‑retention users (R low F high M low)
              │
              │   ★ General‑growth users (R high F low M low)
              │   ★ General‑win‑back users (R low F low M low)
              Low
              Low R (Recency) High
```

---

## Applicable Scenarios

✅ **Most Suitable**
- User stratification and precision marketing
- User value assessment and operational resource allocation
- Churn prediction and win‑back
- Membership/loyalty program design

⚠️ **Use with Caution**
- Low‑frequency, high‑ticket businesses (e.g., automobiles/real estate, Frequency becomes ineffective)
- Non‑repeat‑purchase businesses (e.g., wedding services, RFM degrades to single M dimension)
- Cold‑start products (insufficient transaction data for stratification)
- Non‑transactional products (use activity instead of RFM, e.g., RAF model)

---

## Execution Steps

### Step 1: Collect RFM Data

Extract the three raw metrics for each user from the transaction system:

```
Data extraction:
  User ID | Last Purchase Date | Cumulative Purchase Count | Cumulative Spending Amount
  U001    | 2026-06-15         | 12                         | ¥4,800
  U002    | 2025-03-02         | 2                          | ¥600
  ...

R conversion: R = Analysis date − Last purchase date (days, smaller is better)
```

Data cleaning key points: remove test accounts, merge multiple accounts of the same user, unify currency.

### Step 2: Assign Levels

Divide each dimension's continuous values into several levels (commonly 5 or 3 levels):

```
Leveling method (choose one):
  - Equal‑interval leveling: divide by value range (suitable for uniform distribution)
  - Quantile leveling: divide by quantiles (suitable for skewed distribution, recommended)
  - Business thresholds: set thresholds based on business experience (e.g., R ≤ 30 days = 5 points)

5‑level example (quantile):
  R: [0‑30 days] = 5 / [31‑90] = 4 / [91‑180] = 3 / [181‑365] = 2 / [>365] = 1
  F: [≥12 times] = 5 / [8‑11] = 4 / [5‑7] = 3 / [2‑4] = 2 / [1 time] = 1
  M: [≥¥5000] = 5 / [¥3000‑4999] = 4 / ... / [<¥500] = 1
```

> Quantile leveling is more robust than equal‑interval, avoiding distortion by extreme values. Each level has roughly equal user counts.

### Step 3: User Segmentation

Combine R/F/M levels into operationally meaningful groups:

```
Eight major user groups (by R high/low × F high/low × M high/low combinations):
  High‑value users      R high F high M high — just purchased, frequent, high spend → VIP maintenance
  High‑retention users  R low F high M high — previously high‑frequency high‑value, recently inactive → churn prediction/win‑back
  High‑growth users     R high F low M high — recently purchased high amount, but low frequency → increase frequency
  High‑win‑back users   R low F low M high — historically high value but recently silent → high‑priority win‑back
  General‑value users   R high F high M low — active but low spend → increase average order value
  General‑retention users R low F high M low — previously active now silent → low‑priority win‑back
  General‑growth users  R high F low M low — new or low‑frequency low‑spend → nurture
  General‑win‑back users R low F low M low — low‑value churn → abandon/low‑cost reach
```

You can also use the total R+F+M score for overall stratification (e.g., 13‑15 points = top, 9‑12 = middle, 5‑8 = tail).

### Step 4: Formulate Operation Strategies

Match operational actions to each user group:

```
Operation strategy matrix:
  User group          Operation goal   Key actions                     Expected metrics
  High‑value users    Maintain loyalty exclusive benefits/priority service/thank‑you renewal rate/retention
  High‑retention users prevent churn    win‑back offers/survey reasons/reactivate win‑back rate
  High‑growth users   increase frequency cross‑sell/subscription/repeat‑purchase incentives frequency lift
  High‑win‑back users high‑priority win‑back high‑touch/large discount/manual intervention win‑back rate/LTV
  General‑value users increase AOV     full‑amount reduction/upgrade/recommendations AOV lift
  General‑growth users nurture         onboarding tasks/education/small incentives frequency + amount
  General‑retention/win‑back low‑cost reach automated email/Push/abandon ROI control
```

> Strategies must align with ROI. The win‑back cost ceiling for high‑win‑back users = that group's historical LTV × win‑back probability.

---

## Output Template

```
RFM User Stratification Report

I. Data Overview
  Analysis date: [...]
  Total users: [N]
  Data time window: [past X months]

II. Leveling Criteria
  R: [5‑level thresholds]
  F: [5‑level thresholds]
  M: [5‑level thresholds]

III. User Segmentation Results
  High‑value users: [N people, X% share] — average LTV [¥]
  High‑retention users: [N people] — win‑back value [¥]
  High‑growth users: [N people]
  High‑win‑back users: [N people]
  General‑value/retention/growth/win‑back: [N people each]

IV. Operation Strategies
  [List each group's goal/actions/metrics as per the table above]

V. Effect Tracking
  Re‑test frequency: [monthly]
  Key metrics: [each group's retention/win‑back rate/AOV change]
```

---

## Common Pitfalls

| Pitfall | Avoidance Method |
|---------|------------------|
| Equal‑interval leveling distorted by extreme values | Prefer quantile leveling |
| Level thresholds unchanged over time | Periodically recalculate thresholds to adapt to business growth |
| Looking only at total score, not combinations | R+F+M total score masks group characteristics; must examine combinations |
| Ignoring low‑frequency business characteristics | Reduce F weight or use RAF model for low‑frequency businesses |
| Operational actions lacking ROI control | Set reach cost ceilings for each group |
| Treating RFM as static stratification | Users move between groups; need dynamic tracking of migration |

---

## Relationship with Other Methodologies

- **Combined with User Segmentation**: RFM is transaction‑based segmentation, can be overlaid with behavioral/needs segmentation
- **Combined with Cohort Analysis**: RFM shows current stratification, Cohort shows cohort retention evolution
- **Combined with Customer Journey Map**: RFM identifies key groups, journey map designs reach actions
- **Combined with Lean Analytics Metrics**: RFM is a drill‑down dimension for retention and LTV metrics
- **Followed by A/B Test**: Operation strategies validated via A/B testing