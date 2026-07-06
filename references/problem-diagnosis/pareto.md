# Pareto Analysis

## Core Concept

A systematic application of the 80/20 rule to decision-making — identify the **vital few** (20% of causes producing 80% of impact), and focus resources there. Visualize with a Pareto chart (bar chart + cumulative curve) sorted by impact to find the highest ROI entry point.

> Not all problems deserve equal attention. Seize the vital few, discard the trivial many, to maximize output with limited resources.

---

## When to Use

✅ **Best suited for**
- Resource allocation and prioritization (features, customers, markets)
- Root cause filtering (which causes contribute the most to the problem)
- Defect analysis in quality management
- Sales/revenue analysis (which customers/products contribute the most revenue)
- Time management (which activities produce the most value)

⚠️ **Use with caution**
- All items have similar impact, no Pareto distribution exists (forcing 80/20 will distort results)
- Root cause analysis is needed (Pareto only identifies "what has large impact," not "why")
- Data set is too small (fewer than 10 items cannot form a meaningful ranking)

---

## Execution Steps

### Step 1: List All Items

Comprehensively list the items to analyze (problems, causes, features, customers, etc.):

```
Item list:
  1. [Item A]
  2. [Item B]
  3. [Item C]
  ...
```

Ensure no important items are omitted, but don't mix in obviously irrelevant ones.

### Step 2: Measure Impact for Each Item

Choose a metric aligned with your decision objective, and assign a value to each item:

```
Metric: [e.g., Revenue / Frequency / Cost / Number of complaints]
  Item A: [value]
  Item B: [value]
  Item C: [value]
  ...
```

**Key**: The metric must align with the decision objective. Use dollar amount for revenue optimization, defect count for quality, labor hours for efficiency.

### Step 3: Sort by Impact Descending

Arrange all items from largest to smallest, calculating each item's percentage of the total:

```
Item | Impact Value | Percentage
  A  |    4000      | 40%
  B  |    2500      | 25%
  C  |    1500      | 15%
  D  |    1000      | 10%
  E  |     600      | 6%
  F  |     400      | 4%
```

### Step 4: Calculate Cumulative Percentage

Accumulate percentages item by item, marking the 80% threshold:

```
Item | Impact Value | Percentage | Cumulative %
  A  |    4000      | 40%        | 40%
  B  |    2500      | 25%        | 65%
  C  |    1500      | 15%        | 80%  ← 80% threshold
  D  |    1000      | 10%        | 90%
  E  |     600      | 6%         | 96%
  F  |     400      | 4%         | 100%
```

### Step 5: Identify the Vital Few

Items whose cumulative percentage reaches 80% are the **vital few**; the rest are the **trivial many**.

> Note: 80% is a rule of thumb; the actual threshold may fall between 70%-90%. The key is to find the "inflection point" on the curve — where impact drops sharply.

### Step 6: Focus on the Vital Few, Define Actions

```
Vital few (focus resources):
  - [Item A]: Action [...]
  - [Item B]: Action [...]
  - [Item C]: Action [...]

Trivial many (reduce investment / defer / remove):
  - [Item D/E/F]: Strategy [...]
```

---

## Output Template

```
Pareto Analysis Report

Analysis objective: [e.g., Identify core customers contributing 80% of revenue]
Metric: [e.g., Annual spending amount]
Data source: [...]
Data time range: [...]

Ranked results:
  Item | Impact Value | Percentage | Cumulative % | Category
  [A]  | [...]        | [...]      | [...]        | Vital few
  [B]  | [...]        | [...]      | [...]        | Vital few
  [C]  | [...]        | [...]      | [...]        | Vital few ← 80% threshold
  [D]  | [...]        | [...]      | [...]        | Trivial many
  [...] | [...]       | [...]      | [...]        | Trivial many

Vital few ([N] items, contributing [X]% of impact):
  1. [Item] — Action: [...]
  2. [Item] — Action: [...]

Trivial many ([N] items, contributing [X]% of impact):
  Strategy: [reduce investment / standardize handling / defer / remove]

Resource reallocation:
  Resources freed from trivial many → invest in vital few's [...]
```

---

## Worked Example

**Scenario**: Analyze customer service ticket sources to identify main problems for focused optimization

```
Analysis objective: Identify problem types generating 80% of tickets
Metric: Monthly ticket volume
Data time range: 2024-05

Ranked results:
  Problem type          | Tickets | %    | Cumulative % | Category
  Payment failure       | 420     | 35%  | 35%          | Vital few
  Account login issue   | 300     | 25%  | 60%          | Vital few
  Order status mismatch | 180     | 15%  | 75%          | Vital few
  Refund status inquiry | 120     | 10%  | 85%          | Vital few ← 80% threshold
  Address change        | 90      | 7%   | 92%          | Trivial many
  Coupon usage          | 60      | 5%   | 97%          | Trivial many
  Other                 | 30      | 3%   | 100%         | Trivial many

Vital few (4 items, contributing 85% of tickets):
  1. Payment failure — Action: Integrate payment channel monitoring + auto-retry mechanism
  2. Account login issue — Action: Optimize OAuth flow + add one-click fix entry
  3. Order status mismatch — Action: Add message queue retry + status push notifications
  4. Refund status inquiry — Action: Real-time refund status page + progress SMS notifications

Trivial many (3 items, contributing 15% of tickets):
  Strategy: Route address changes and coupon usage to self-service FAQ; auto-reply for others

Resource reallocation: Free 1 customer service rep from FAQ maintenance → Invest in dedicated payment channel optimization
```

---

## Common Pitfalls

| Pitfall | Description | How to Avoid |
|---------|-------------|-------------|
| Wrong metric selected | Ranking by wrong metric leads to misaligned focus | Metric must directly align with decision objective; first clarify "what am I optimizing" |
| Forcing 80/20 | Data itself has no Pareto distribution, items have similar impact | Check if the cumulative curve has a clear inflection point first; if no inflection, Pareto analysis is not applicable |
| Ignoring trivial many's cumulative effect | Individual items small but total is significant, ignoring completely can lead to errors | Assess the total share of trivial many; if over 30%, consider standardized batch processing |
| Static analysis | Running Pareto analysis only once, ignoring impact changes over time | Re-rank periodically, especially after business environment changes |
| Confusing correlation with causation | Large impact ≠ root cause; Pareto only ranks, doesn't explain | Apply 5 Whys to the vital few to investigate root causes |

---

## Relationship with Other Methodologies

- **Combined with 5 Whys**: Pareto identifies "which problems have the most impact"; 5 Whys investigates "why these problems occur"
- **Combined with Fishbone**: After Pareto ranking, use Fishbone to expand the full causal picture for the vital few
- **Feeds into RICE**: Vital few items have higher priority, serving as quantitative basis for Impact in RICE
- **Feeds into Eisenhower Matrix**: Pareto's "vital few" corresponds to the important dimension, then combine with urgency to place in the execution matrix
- **Combined with OKR**: Action items from the vital few can be converted into Key Results for OKR
