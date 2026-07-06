# Value Proposition Canvas · 价值主张画布

## Core Concept

Systematically validate the fit between **product features** and **user needs** (a micro version of Product-Market Fit). Proposed by Osterwalder, it is a deep-dive tool for the "Value Proposition" module in the Business Model Canvas.

> JTBD uncovers user tasks; VPC checks whether your product truly responds to those tasks.

**Two Half-Circles:**
- **Right Half (Customer Profile)**: Customer Jobs / Pains / Gain Expectations
- **Left Half (Value Map)**: Products & Services / Pain Relievers / Gain Creators

Fit = the degree to which the left half systematically responds to the right half.

---

## Applicable Scenarios

✅ **Best For**
- Product feature priority decisions (which features truly address user pains)
- Validating fit before launching new products/features
- Discovering misalignment between existing products and user needs
- Differentiation positioning analysis against competitors

⚠️ **Use with Caution**
- No prior contact with real users yet (do JTBD interviews first)
- Overall business model evaluation (use Business Model Canvas instead)

---

## Execution Steps

### Right Half: Customer Profile

#### Step 1: Customer Jobs

What is the user trying to accomplish with your product/service? Three categories:

```
Functional job: [What they actually need to do, e.g., "manage team's work progress"]
Emotional job: [How they want to feel during the process, e.g., "feel in control"]
Social job: [How they want to be perceived by others, e.g., "be seen as an efficient manager"]
```

Prioritize: which jobs matter most to the user?

#### Step 2: Pains

Obstacles, risks, and negative experiences encountered when completing jobs:

```
Obstacles: [Factors that make the job harder]
Risks: [Potential negative outcomes]
Friction: [Annoyances, hassles, time-wasters]
```

Rank by severity (extreme pain → mild inconvenience).

#### Step 3: Gain Expectations

Benefits the user expects to receive (beyond basic needs — "delighters"):

```
Required gains: [Minimum expectations; won't use if not met]
Expected gains: [Desired but not mandatory]
Unexpected gains: [Surprises beyond expectations]
```

---

### Left Half: Value Map

#### Step 4: Products & Services

List all features/services you provide (factual inventory, not marketing copy):

```
Feature list: [...]
```

#### Step 5: Pain Relievers

How does your product specifically eliminate pains from the right half?

```
Pain [X] → Addressed through [Feature Y], method: [...]
```

Map one-to-one; mark unmatched pains as "Not covered."

#### Step 6: Gain Creators

How does your product meet or exceed user gain expectations?

```
Gain expectation [X] → Delivered through [Feature Y], method: [...]
```

---

### Fit Analysis

#### Step 7: Assess Fit Gaps

```
Covered core pains: [...]
Uncovered core pains: [...] (← most important insight)
Key gains created: [...]
Ignored important gain expectations: [...]
```

**Fit Assessment:**
- Are the core pains (top 3 most severe) all covered?
- Are all required gains met?
- Are there "features with no pain correspondence" (useless features)?

---

## Output Template

```
Target Customer Segment: [...]

【Customer Profile】
Core Jobs: [Top 1-3 jobs]
Severe Pains: [Ranked by severity]
Key Gain Expectations: [Required gains + highest-priority expected gains]

【Value Map】
Core Features: [...]
Pain Coverage:
  ✅ [Pain] → [Feature] → Resolution method
  ❌ [Pain] → Not covered
Gain Creation:
  ✅ [Gain expectation] → [Feature] → Delivery method
  ❌ [Gain expectation] → Not met

【Fit Assessment】
Fit strength: [Strong/Medium/Weak]
Biggest gap: [...]
Recommended priority features/improvements: [...]
```

---

## Common Pitfalls

| Pitfall | Description | How to Avoid |
|------|------|---------|
| Using assumptions instead of user data | Filling right half subjectively | Right half inputs must come from real user interviews or data |
| Working on left and right halves separately | Building value map first, then "fitting" the customer profile | Always start from the right half (user); left half is the response |
| Feature list = Value Map | Treating features as value propositions | Every feature must correspond to a specific pain or gain expectation |
| Ignoring uncovered pains | Focusing only on covered areas | Gap analysis is the most valuable output |

---

## Relationships with Other Methodologies

- **Preceded by JTBD**: Use JTBD to deeply uncover customer jobs, directly feeding the right half
- **Combined with Business Model Canvas**: VPC is the expansion of the BMC value proposition module
- **Output feeds RICE**: Fit gaps (uncovered pains) become features to develop, prioritized via RICE
- **Output feeds Lean BML**: The largest gap becomes the hypothesis validation target for the next Build-Measure-Learn cycle

---

## Comparison with 6-Part JTBD Value Proposition

VPC and [6-Part JTBD Value Proposition](jdb-value-proposition.md) both clarify value propositions, but differ in perspective and output format:

| Dimension | Value Proposition Canvas | 6-Part JTBD Value Proposition |
|------|--------------------------|-------------------------------|
| Perspective | Descriptive (what pains/gains users have, how we respond) | Action-oriented (what Job the customer needs done, differentiation vs alternatives) |
| Structure | Left/right half-circles with 6 fields (Customer Jobs/Pains/Gains × Products/Pain Relievers/Gain Creators) | 6-section template (Who/Why/What before/How/What after/Alternatives) |
| Focus | Fit between product and user needs | Differentiation vs alternatives |
| Output | Gap list (which pains are uncovered) | A externally communicable value proposition statement |
| Best stage | PMF validation (product still being refined) | GTM stage (writing sales materials/website) |

**Combined usage**: Use VPC first for internal gap analysis; once fit is confirmed, use 6-Part JTBD to craft external value proposition messaging.

---

## 4 Structural Weaknesses of VPC

VPC reveals 4 structural weaknesses in practice that require proactive compensation:

1. **Static perspective**: VPC is a snapshot, not showing how value evolves across the user journey/product stages — pair with [Customer Journey Map](customer-journey.md) to add the time dimension
2. **No prioritization mechanism**: All Pains/Gains have equal weight on the canvas, but "severe pain" and "mild inconvenience" differ vastly in actual weight — enforce Top 3 ranking
3. **No competitor comparison**: VPC only compares "user's current state vs your product," not competitors — pair with [Positioning Strategy](positioning-strategy.md) to add competitive dimension
4. **Solution bias**: The left half (your product) canin turn influence how you fill the right half (customer profile) — fill and freeze the right half first, then fill the left half to mitigate
