# Decision Matrix

## Core Concept
Multi-option, multi-criteria weighted scoring that quantifies choices. Each option is scored against each criterion, weights reflect relative importance, and the highest total score wins.

## Applicable Scenarios
✅ **Best for**
- Technology selection with custom criteria
- Strategy comparison
- Candidate evaluation

⚠️ **When NOT to use**
- Options have probabilistic, quantifiable payoffs — weighted preference scoring ignores expectation; use **Decision Tree & Expected Value**
- One uncertain quantity to estimate, no multi-option comparison — scoring answers the wrong question; use **Probabilistic Reasoning**
- The cause-effect structure of the situation is still unclear — criteria chosen before understanding encode the confusion; classify with **Cynefin** first
- Criteria and weights are genuinely contested among stakeholders — the matrix launders politics into arithmetic; negotiate the criteria openly first or the total is theater

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

## Failure Modes
- Weights chosen to crown the preferred option: the winner was implicitly picked before scoring started → elicit and freeze weights before any option is scored, then sensitivity-check whether the ranking survives weight swings
- Double-counted criteria: "cost" scored directly and again inside "risk" → each factor belongs in exactly one criterion; merge or drop duplicates before weighting
- Unanchored scales: 1-5 scores on undefined levels read as measurements → publish anchors per score level before scoring
- Straw-man option set: only weak variants of one alternative listed → include the honest rival and a do-nothing baseline
- Arithmetic laundering: the total implies an objectivity the inputs never had → report the result as weighted judgment and flag near-ties as effectively tied

## Evidence Strength
Mixed — the arithmetic is exact but every input is judgment: weighted scoring has a long operational record (Pugh, AHP, SMART lineage), yet outputs are highly sensitive to weight elicitation, scale anchoring, and criterion framing, and no evidence shows the top total outperforms a well-argued ranking. The matrix's real product is the explicit criteria-and-weights conversation; treat the winner as a structured opinion and lean on the sensitivity step for the verdict.

## Source
Standard decision analysis methodology; Pugh matrix variant.
