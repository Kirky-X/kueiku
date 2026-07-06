# Consumer Decision Journey · 消费者决策旅程

## Core Concept

McKinsey proposed that the process from a consumer's need arising to forming loyalty is **non-linear**, not a traditional funnel-style linear progression. The decision journey includes: **Consider → Evaluate → Purchase → Experience → Advocate (Loyalty)**, where the **Experience stage** is the key to whether a brand enters the loyalty loop.

> The traditional funnel assumes consumers passively narrow down choices. In reality, consumers actively add/remove brands during their journey, and post-purchase experience determines whether they enter the loyalty loop — this is the engine of repeat purchases and word-of-mouth.

```
        ┌──────────────── Loyalty Loop ──────────────┐
        ↓                                            │
  Consider → Evaluate → Purchase → Experience → Advocate ──────────┘
                                    │
                                    └→ Exit loop if dissatisfied
```

---

## Applicable Scenarios

✅ **Best Suited For**
- User journey optimization and touchpoint design
- Marketing resource allocation across decision stages
- Churn analysis and re-engagement design
- Omnichannel experience consistency diagnosis

⚠️ **Use with Caution**
- Low-involvement impulse purchases (decision journey is too short; model has low value)
- Complex B2B procurement (multiple decision-makers; use B2B procurement journey model instead)
- Lack of touchpoint data (cannot pinpoint experience bottlenecks)
- Treating the journey as a linear funnel (losing non-linear insights)

---

## Execution Steps

### Step 1: Map the Journey

List the full process from need emergence to loyalty:

```
Decision journey stages:
  1. Consider: Consumer develops a need and initially thinks of candidate brands
  2. Evaluate: Actively gathers information, adds/removes brands
  3. Buy: Completes the transaction at a channel
  4. Experience: Uses the product/service, forms perceptions
  5. Advocate: If satisfied, recommends/repeats purchase, entering the loyalty loop
```

For each stage, identify what consumers are doing, thinking, and feeling.

### Step 2: Identify Touchpoints

List all touchpoints between consumers and the brand / channel at each stage:

```
Touchpoint inventory (examples):
  Consider: Ads / word-of-mouth / search results / social media / friend recommendations
  Evaluate: Official website / reviews / comparison sites / customer service inquiries / offline experiences
  Buy: E-commerce platforms / stores / apps / sales staff
  Experience: Unboxing / usage / customer service / community / content
  Advocate: Reviews / sharing / referrals / repeat purchases / UGC
```

> Not all touchpoints are brand-controllable (e.g., word-of-mouth, reviews), but they all influence decisions and must be included in the analysis.

### Step 3: Evaluate Experience

Assess consumer experience at each stage and touchpoint:

```
Experience evaluation table:
  Stage     Touchpoint       Experience Score  Pain Point           Churn Risk
  Consider  Search results   [Low]             Brand terms hijacked by competitors  High
  Evaluate  Official website [Medium]          Confused information architecture    Medium
  Buy       Payment process  [High]            Too many steps                         Low
  Experience Unboxing        [High]            None                                   Low
  Experience Customer service[Low]             Slow response                          High
  Advocate   Reorder prompt  [Medium]          No re-engagement mechanism             Medium
```

Focus on the **Experience stage**: this is the key to entering the loyalty loop. Poor post-purchase experience zeroes out all prior touchpoint efforts.

### Step 4: Optimize Key Touchpoints

Prioritize by "Impact × Pain Severity":

```
Optimization priority matrix:
  High impact + High pain → Optimize immediately (e.g., customer service response)
  High impact + Low pain  → Monitor and maintain
  Low impact + High pain  → Secondary optimization
  Low impact + Low pain   → No investment for now

Optimization action examples:
  - Consider stage: Strengthen brand term SEO/SEM, intercept competitors
  - Evaluate stage: Restructure website information architecture, provide decision tools
  - Experience stage: Improve customer service response SLA, establish proactive care
  - Advocate stage: Design reorder incentives + referral rewards
```

> The goal of journey optimization is not single-touchpoint excellence, but **whole-journey smoothness**. Single-point optimization with broken touchpoints elsewhere still leads to churn.

---

## Output Template

```
Consumer Decision Journey Analysis

I. Journey Overview
  Category: [...] / Target audience: [...]
  Journey stages: Consider → Evaluate → Purchase → Experience → Advocate

II. Touchpoint Inventory
  [List all touchpoints by stage, marking brand-controllable / uncontrollable]

III. Experience Assessment
  [Table: Stage / Touchpoint / Experience Score / Pain Point / Churn Risk]
  Key churn points: [...] — Root cause: [...]

IV. Optimization Priorities
  Priority 1: [Touchpoint] — Action [...] — Expected churn reduction [X%]
  Priority 2: [Touchpoint] — Action [...] — ...

V. Loyalty Loop Design
  Experience key actions: [...]
  Advocate incentive mechanisms: [...]
  Repeat purchase triggers: [...]

VI. Effect Tracking
  Key metrics: [Stage conversion rates / repeat purchase rate / NPS]
  Re-measurement frequency: [Quarterly]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|------|---------|
| Treating the journey as a linear funnel | Must capture non-linear add/remove brand behaviors |
| Only focusing on pre-purchase touchpoints | The Experience stage is critical for the loyalty loop and cannot be ignored |
| Ignoring uncontrollable touchpoints | Word-of-mouth / reviews are uncontrollable but influence decisions; must be included |
| Single-touchpoint optimization ignoring the whole journey | Whole-journey smoothness takes priority over single-point excellence |
| Journey remains static | Journey evolves with channels / categories; re-measure regularly |
| Using average experience to mask segment differences | Different audience segments may have different journeys; analyze by segment |

---

## Relationship with Other Methodologies

- **Pair with Customer Journey Map**: CJM is a finer-grained service design tool; CDJ is a strategic-level framework
- **Pair with RFM Model**: RFM identifies high-value / churn-risk users; CDJ designs engagement actions
- **Pair with STP Analysis**: Different target segments may have different decision journeys; map separately
- **Pair with Empathy Map**: Empathy Map supplements what consumers think and feel during the journey
- **Pair with A/B Test**: Touchpoint optimization validated through A/B testing
