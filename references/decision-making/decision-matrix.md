# Decision Matrix

## Core Concept
Multi-option, multi-criteria weighted scoring that quantifies choices. Each option is scored against each criterion, weights reflect relative importance, and the highest total score wins.

## Applicable Scenarios
✅ **Best for**
- Technology selection with custom criteria
- Strategy comparison
- Candidate evaluation

## Key Steps
1. Define the decision to be made
2. List all options (at least 3 alternatives)
3. Define evaluation criteria (5-7 recommended)
4. Assign weights to each criterion (must sum to 1.0 or 100%)
5. Score each option per criterion (1-5 or 1-10 scale)
6. Calculate weighted score = score × weight for each cell
7. Sum weighted scores per option; highest total wins
8. Conduct sensitivity analysis: vary weights to test robustness

## Output Template
```
Decision Matrix:
| Criterion (weight) | Option A | Option B | Option C |
|--------------------|----------|----------|----------|
| Cost (0.3)         | 4 (1.2)  | 3 (0.9)  | 5 (1.5)  |
| Performance (0.4)  | 3 (1.2)  | 5 (2.0)  | 4 (1.6)  |
| Risk (0.3)         | 4 (1.2)  | 2 (0.6)  | 3 (0.9)  |
| **Total**          | **3.6**  | **3.5**  | **4.0**  |

Winner: Option C (4.0)
Sensitivity: [robust / sensitive to criterion X]
```

## Source
Standard decision analysis methodology; Pugh matrix variant.
