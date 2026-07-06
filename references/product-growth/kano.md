# Kano Model · 狩野模型

## Core Concept

Proposed by Noriaki Kano in 1984, it classifies product features into five categories based on their relationship with user satisfaction. Core insight: the relationship between feature implementation level and satisfaction is **non-linear**, and different feature types have completely different mechanisms affecting satisfaction.

> Note: ASCII diagram preserved. The Kano Model is a line chart with 5 curves; mermaid `xychart-beta` has limited expressiveness and cannot accurately represent multiple non-linear curves, so conversion is omitted.

```
Satisfaction
  ↑        ╱ Attractive
  │       ╱
  │      ╱    One-dimensional
  │     ╱   ╱
  │────╱──╱───────── Must-be
  │  ╱  ╱
  │╱  ╱        Indifferent
  │ ╱
  │╲               Reverse
  └──────────────────→ Feature Implementation Level
```

| Feature Type | When Implemented | When Not Implemented | Strategy |
|---------|--------|---------|------|
| **Must-be** | Expected, does not increase satisfaction | Extreme dissatisfaction | Must satisfy |
| **One-dimensional** | Satisfaction rises linearly | Satisfaction drops linearly | The more the better, main competitive battleground |
| **Attractive** | Surprise, significantly boosts satisfaction | No dissatisfaction | Differentiation weapon |
| **Indifferent** | No feeling | No feeling | Low priority |
| **Reverse** | Dissatisfaction | Satisfaction | Never do |

---

## Applicable Scenarios

✅ **Best For**
- Product feature classification and demand nature analysis
- Feature combination strategy in version planning (Must-be foundation + One-dimensional competition + Attractive differentiation)
- User satisfaction strategy formulation

⚠️ **Use with Caution**
- When execution prioritization is needed (Kano classification ≠ priority; use RICE for ranking)
- When user input cannot be obtained (Kano is fundamentally a user-driven classification method)
- When features have strong dependencies

---

## Execution Steps

### Step 1: List Candidate Features

Collect all features/requirements to be evaluated and form a feature list. Sources can include: user feedback, competitive analysis, business goal decomposition, technology-driven.

### Step 2: Design Kano Questionnaire

Design **functional** and **dysfunctional** paired questions for each feature, with a 5-point scale: Like / Expect / Neutral / Tolerate / Dislike.

```
Functional question: If this feature existed, how would you feel?
Dysfunctional question: If this feature did not exist, how would you feel?

Note:
  - The two questions must always appear in pairs
  - Wording must remain neutral, avoid leading statements
  - Questionnaire introduction should state "there are no right or wrong answers"
```

### Step 3: Collect Questionnaire and Classify

Use the Kano evaluation table to classify each questionnaire response, taking the mode as that feature's Kano type:

```
                    Dysfunctional Response
                    Like  Must  Neutral  Tolerate  Dislike
Functional  Like     Q     A      A        A         O
Response    Must     R     I      I        I         M
            Neutral  R     I      I        I         M
            Tolerate R     I      I        I         M
            Dislike  R     R      R        R         Q

M=Must-be, O=One-dimensional, A=Attractive, I=Indifferent, R=Reverse, Q=Questionable
```

### Step 4: Calculate Satisfaction Coefficients

```
Satisfaction Coefficient CS+ = (A + O) / (A + O + M + I)
  → Closer to 1, the greater the satisfaction boost from implementing this feature

Dissatisfaction Coefficient CS- = (O + M) / (A + O + M + I) × (-1)
  → Closer to -1, the more severe the dissatisfaction from not implementing
```

### Step 5: Formulate Feature Strategy

```
Must-be → Must do (not meeting = product unusable)
One-dimensional → Competitive investment (better performance = higher satisfaction)
Attractive → Selective investment (differentiation, 1-2 is sufficient)
Indifferent → Defer or skip
Reverse → Never do
Intra-type ranking: Use CS+ and CS- values to aid decision-making
```

> **Feature Type Evolution Over Time**: Attractive features gradually downgrade to One-dimensional as competitors follow, eventually becoming Must-be. Therefore, re-evaluate feature classification every 1-2 versions.

---

## Output Template

```
Product: [Name]  Evaluation Date: [Date]  Sample Size: [N]

| Feature Name | Kano Type | CS+ | CS- | Strategy |
|---------|----------|-----|-----|------|
| Feature A  | Must-be  | 0.20 | -0.85 | Must do |
| Feature B  | One-dimensional | 0.65 | -0.70 | Heavy investment |
| Feature C  | Attractive | 0.75 | -0.10 | Differentiation |
| Feature D  | Indifferent | 0.15 | -0.05 | Defer |
| Feature E  | Reverse  | 0.05 | 0.40 | Skip |

Version Planning:
  V1.0 Must-be: [Feature A, ...]
  V1.0 One-dimensional: [Feature B, ...]
  V1.1 Attractive: [Feature C, ...]
  Deferred: [Feature D, ...]  Excluded: [Feature E, ...]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|------|---------|
| Treating Kano classification as priority ranking | Kano is demand nature analysis; priority still requires RICE |
| Questionnaire design has leading statements | Functional/dysfunctional questions must be paired, wording must stay neutral |
| Ignoring dynamic feature type evolution | Attractive → One-dimensional → Must-be is a common path; re-evaluate periodically |
| Insufficient sample size or sample bias | At least 50 valid questionnaires, covering core and edge user groups |
| Categorizing all features as One-dimensional | Distinguish "what users say they want" (One-dimensional) from "what users didn't mention but would delight them" (Attractive) |

---

## Relationships with Other Methodologies

- **Preceded by JTBD**: JTBD identifies core Jobs; Kano classifies the features that implement those Jobs
- **Followed by RICE**: Kano classification is an important input for the Impact dimension in RICE
- **Combined with MoSCoW**: Kano Must-be ≈ MoSCoW Must have, but Kano is based on user data while MoSCoW is based on stakeholder judgment
- **Combined with OKR**: Attractive features can serve as differentiation objectives in OKR
- **Combined with AARRR**: AARRR locates funnel bottlenecks; Kano determines what type of feature is needed to break through at that layer
