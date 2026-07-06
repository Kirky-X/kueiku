# RICE Scoring

## Core Concept

Through quantitative evaluation across four dimensions, calculate the priority score for each requirement/project, transforming subjective ranking into a **defensible structured decision**.

```
RICE Score = (Reach × Impact × Confidence) ÷ Effort
```

| Dimension | Meaning | Unit |
|------|------|------|
| **Reach** coverage | How many users/events are affected within the evaluation period | Number of people/times (per month/quarter) |
| **Impact** impact | How much impact per affected user | 0.25 / 0.5 / 1 / 2 / 3 |
| **Confidence** confidence | Degree of certainty in R and I estimates | % (100% / 80% / 50%) |
| **Effort** effort | Person-months/weeks required to complete | Person-months |

---

## Applicable Scenarios

✅ **Best suited for**
- Priority ranking of product features/requirements (Roadmap planning)
- Comparing the value of multiple improvement proposals
- Cross-team priority alignment (quantified basis reduces subjective disputes)
- Requirement pool cleanup before quarterly planning

⚠️ **Use with caution**
- Strategic direction selection (RICE is suitable for tactical level, not strategic level)
- When insufficient information exists for reasonable estimation (creates false sense of precision)
- Completely new market exploration (Reach/Impact cannot be estimated)

---

## Dimension Evaluation Guide

### Reach (Coverage)

The **number of unique users** or **events** affected by this feature within a **specific time period** (typically monthly).

Estimation methods:
- Review existing DAU/MAU for related features
- Estimate the proportion of target user group in total users
- Review traffic data for related pages/processes

```
Example: Payment process improvement
  Monthly payment users: 50,000
  Reach = 50,000
```

---

### Impact

Degree of impact on **each affected user**. Use fixed scale to avoid subjective inflation:

| Score | Meaning |
|------|------|
| 3 | Significant improvement (substantial improvement in core conversion/retention) |
| 2 | Major improvement (clearly measurable positive impact) |
| 1 | Moderate improvement (moderate improvement, noticeable but not significant) |
| 0.5 | Minor improvement (slight improvement) |
| 0.25 | Minimal impact (marginal improvement) |

Evaluation principle: Features that directly impact core metrics (conversion/retention/revenue) score high; indirect impact scores low.

---

### Confidence

Degree of certainty in Reach and Impact estimates:

| Confidence | Meaning |
|--------|------|
| 100% | Data verified (A/B test results, user research conclusions) |
| 80% | Partially data-supported (historical data from similar features, qualitative research) |
| 50% | Primarily based on intuition or analogy, weak data support |

When confidence is 50%, RICE score automatically halves, built-in uncertainty penalty.

---

### Effort

**Total human effort** required to complete this feature (design + frontend + backend + testing + PM), in **person-months** (or person-weeks, consistent units).

Estimation suggestions:
- Don't underestimate: Add buffer coefficient (actual experience × 1.2-1.5)
- Calculate full team effort, not just engineers
- Include monitoring and fixing costs after code launch

---

## Execution Steps

### Step 1: Build Requirement Pool

List all requirements/features/projects to be evaluated.

### Step 2: Evaluate Four Dimensions Item by Item

For each requirement, fill in estimated values for R, I, C, E.

**Efficiency tips**:
- First have team members score independently, then align on discussions
- Establish reference benchmarks for similar feature types (anchor to avoid drift)

### Step 3: Calculate RICE Score

```
RICE = (R × I × C) ÷ E
```

### Step 4: Ranking + Sanity Check

Sort by RICE score from high to low, then perform sanity check:
- Strategic importance: Are there strategically required items with low scores?
- Dependencies: Are some low-score items prerequisites for high-score items?
- Diversity: All same type of features? Need to add balance?

Adjust and finalize priority.

---

## Output Template

```
Evaluation time range: [Month/Quarter]
Evaluation dimension explanation: Reach unit=[people/month], Effort unit=[person-weeks]

Requirement priority ranking table:

| Requirement Name | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|------------|--------|---------|
| Feature A  | 50000 | 2      | 80%        | 2      | 40000   |
| Feature B  | 20000 | 3      | 50%        | 1      | 30000   |
| Feature C  | 80000 | 0.5    | 100%       | 4      | 10000   |
| Feature D  | 5000  | 2      | 50%        | 0.5    | 10000   |

Evaluation notes:
  - Feature A's confidence based on: [Data source]
  - Feature B needs attention: [Dependencies/Risks]

Final priority:
  Q1 must-do: [Feature A, B]
  Q1 target: [Feature C]
  To be scheduled: [Feature D]
  Shelved: [...]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|------|---------|
| Impact scores generally inflated (all 2-3) | Force relative ranking, most features should be 1 |
| Effort consistently underestimated | Establish historical calibration data, regularly review actual/estimated ratio |
| Only looking at RICE score, ignoring strategic weight | Add "strategic importance" adjustment item |
| Confidence uniformly set to 80%, losing differentiation | Clearly define evidence requirements for each level |

---

## Relationship with Other Methodologies

- **Precedes AARRR**: AARRR identifies growth bottleneck layers, RICE prioritizes improvement proposals for that layer
- **Precedes JTBD**: JTBD identifies high-opportunity Jobs, convert to features then use RICE for ranking
- **Combined with OKR**: High RICE score items correspond to OKR Key Results
- **Alternative scenarios**: More quantitative than MoSCoW; more defensible than pure subjective discussion

---

## ICE vs RICE vs Opportunity Score Comparison

All three are priority scoring frameworks, but suitable stages and data requirements differ:

| Framework | Dimensions | Best for | Data Requirements | Main Weaknesses |
|------|------|--------|---------|---------|
| **ICE** | Impact × Confidence × Ease | Initial screening of large idea pools (within 30 minutes) | Almost no data requirements, intuition-based scoring | No Reach dimension; highly subjective; cannot compare horizontally with history |
| **RICE** | Reach × Impact × Confidence ÷ Effort | Detailed roadmap ranking | Requires Reach data + Effort estimation | Effort estimation controversial; early product Reach unreliable |
| **Opportunity Score** | Importance × (1 − Satisfaction) | Finding unmet needs (product opportunity map) | Requires user research data (importance + satisfaction) | Doesn't consider implementation cost; only looks at demand side, not execution side |

**Selection decision tree**:
- Idea pool > 20, need quick screening → **ICE** initial screening
- Shortlisted ideas need detailed ranking, data available → **RICE** detailed ranking
- Existing user research, need to identify "high importance, low satisfaction" opportunities → **Opportunity Score**
- All three can be chained: ICE screen → RICE rank → Opportunity Score validates demand side

**Key differences**:
- ICE/RICE are "supply-side" scoring (is this idea worth doing)
- Opportunity Score is "demand-side" scoring (is there an opportunity for this need)
- Complete decision should look at both sides: High Opportunity Score need + High RICE score solution = Priority investment