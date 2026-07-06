# Decision Matrix (Pugh Matrix)

## Core Concept

When facing **multiple alternatives** with non-uniform evaluation criteria, transform subjective judgments into comparable quantitative conclusions through weighted scoring. Suitable for option selection scenarios with "many criteria and large weight differences."

> RICE is a formula for product requirement prioritization; the decision matrix is a general-purpose selection tool for any multiple options and criteria — they complement each other.

---

## Applicable Scenarios

✅ **Best suited for**
- Technology selection (framework/vendor/architecture solution)
- Strategy option selection (multiple strategic alternatives)
- Hiring candidate evaluation
- Any decision with "3+ options + 3+ evaluation criteria"

⚠️ **Use with caution**
- Only 2 options with clear criteria (direct comparison suffices)
- Product requirement prioritization (use RICE instead, lighter weight)
- Decision heavily dependent on emotional/values factors (matrix numbers may mask true judgment)

---

## Execution Steps

### Step 1: List Alternative Options

```
Option A: [...]
Option B: [...]
Option C: [...]
(Recommended 3-7 options; too few doesn't need matrix, too many hard to evaluate)
```

### Step 2: Determine Evaluation Criteria

Exhaustively list all relevant criteria, then merge overlapping items, keeping 5-8 core criteria:

```
Candidate criteria: [...]
Final criteria: [Criterion 1, Criterion 2, Criterion 3, ...]
```

**Example criteria**: Cost, implementation difficulty, scalability, user experience, risk, delivery speed, team familiarity

### Step 3: Assign Weights

Sum of all criteria weights = 100% (or 1.0):

```
Criterion 1: [x%]
Criterion 2: [x%]
...
```

Weight setting principles:
- Criteria most directly related to core goals get highest weights
- All decision participants reach consensus on weights (weight disagreements themselves are important information)

### Step 4: Score Each Option

Score each option on each criterion (1-5 or 1-10 scale, consistent):

```
| Criterion         | Weight | Option A | Option B | Option C |
|--------------|------|-------|-------|-------|
| [Criterion 1]      | 30%  |   4   |   3   |   5   |
| [Criterion 2]      | 25%  |   5   |   4   |   3   |
| [Criterion 3]      | 20%  |   3   |   5   |   4   |
| [Criterion 4]      | 15%  |   4   |   4   |   3   |
| [Criterion 5]      | 10%  |   5   |   3   |   4   |
```

Scoring rules:
- Relative scoring (comparing options) is more accurate than absolute scoring
- Under same criterion, first determine which option gets highest score, then score others

### Step 5: Calculate Weighted Total Score

```
Option A total score = Σ (each score × weight)
```

Example:
```
Option A = 4×30% + 5×25% + 3×20% + 4×15% + 5×10% = 4.10
Option B = 3×30% + 4×25% + 5×20% + 4×15% + 3×10% = 3.80
Option C = 5×30% + 3×25% + 4×20% + 3×15% + 4×10% = 3.90
```

### Step 6: Sensitivity Analysis (Optional but Important)

Change 1-2 key weights to see if conclusion changes:

```
If [Criterion 1] weight is reduced from 30% to 15%, does the conclusion change?
```

Conclusion stable → Decision reliability high
Conclusion changes with weights → Weight setting itself is key to decision, needs re-discussion

### Step 7: Interpretation and Decision

```
Option with highest score: [...]
But need to verify:
  ✓ Does conclusion align with intuition? (If not, check scoring or weights)
  ✓ Does any option score extremely low on a key criterion (veto item)?
  ✓ How large is the gap between first and second place? (Small gap indicates two options are evenly matched)
```

---

## Output Template

```
Decision problem: [...]

Alternative options: [A] / [B] / [C]

Evaluation matrix:
| Criterion       | Weight | Option A | Option B | Option C |
|------------|------|-------|-------|-------|
| [Criterion 1]    | xx%  |       |       |       |
| [Criterion 2]    | xx%  |       |       |       |
| ...        |      |       |       |       |
| **Total Score**   |      | x.xx  | x.xx  | x.xx  |

Sensitivity test: After adjusting [key criterion] weight, conclusion [unchanged/changed to Option X]

Recommended option: [...] — Main advantage: [...] — Main risk: [...]
Alternative option: [...] — Applicable conditions: [...] (If [certain condition changes], switch to this option)
```

---

## Execution Example

**Scenario**: Selecting backend framework (Node.js vs Go vs Rust) for new service

```
Criteria and weights:
  Development efficiency      30% (current team bottleneck)
  Runtime performance    25% (new service is high-frequency interface)
  Team familiarity    20% (learning cost affects delivery)
  Ecosystem completeness    15%
  Long-term maintainability    10%

Scoring (1-5):
| Criterion       | Weight | Node.js | Go | Rust |
|------------|------|---------|----|------|
| Development efficiency   | 30%  |    5    |  4 |  2   |
| Performance       | 25%  |    3    |  5 |  5   |
| Familiarity     | 20%  |    5    |  3 |  1   |
| Ecosystem       | 15%  |    5    |  4 |  3   |
| Maintainability     | 10%  |    3    |  5 |  4   |

Total score: Node.js = 4.30 | Go = 4.15 | Rust = 2.90

Sensitivity: If performance weight increased to 40%, Go surpasses Node.js (4.45 vs 4.10)

Recommendation: Node.js (under current constraints)
Alternative: Go (switch when performance becomes primary constraint)
```

---

## Common Pitfalls

| Pitfall | Description | How to Avoid |
|------|------|---------|
| Backward scoring from weights | Knowing which option you want first, then adjusting weights | Set weights first, then score; order cannot be reversed |
| Ignoring veto items | An option scores 1 on a key criterion but total score still high | Set "minimum score threshold," items below threshold are directly eliminated |
| False precision | Calculating 4.32 vs 4.28 and assuming former is better | Gaps < 0.3 considered evenly matched, do sensitivity analysis |
| Overlapping criteria | "Speed" and "response time" are essentially the same | Merge similar items before establishing criteria |

---

## Relationship with Other Methodologies

- **Precedes MECE**: Ensure evaluation criteria are non-overlapping and exhaustive
- **Combined with Pre-mortem**: After decision, use Pre-mortem to verify risks of selected option
- **Boundary with RICE**: Product requirement prioritization uses RICE; option selection uses decision matrix
- **Combined with Six Thinking Hats**: Before scoring, use six hats to ensure multi-angle evaluation, avoiding single-perspective bias