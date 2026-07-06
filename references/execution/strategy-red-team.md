# Strategy Red Team

## Core Idea
Teams tend to fall into "self-persuasion" after formulating strategy. Red Team exercises force a steelman first (articulate the opponent's strongest argument better than they can) before attacking, avoiding straw-man fallacies. Then rank by impact × likelihood × cheapness-to-test, prioritizing the most worthwhile rebuttals to validate.

## Use Cases
- Strategy is about to be finalized and needs a final round of stress-testing
- Team is overconfident about the strategy, lacking dissenting views
- Potential challenges from investors or the board need to be anticipated

## Key Steps
1. Write down the strategic proposition to challenge (clear, one-sentence statement)
2. Steelman: Find a genuine opponent's perspective, articulate the counter-argument stronger than the opponent would (no weak phrasing like "the opponent might say...")
3. Attack: Based on the steelman, identify weak assumptions and failure conditions in the strategy
4. Evaluate each rebuttal on 3 dimensions:
   - Impact: Degree of damage to the strategy if valid (high/medium/low)
   - Likelihood: Probability of it being valid (high/medium/low)
   - Cheapness-to-test: Cost of validation (low/medium/high)
5. Prioritize: High Impact + High Likelihood + Low cost = validate first
6. Design validation experiments (see experiment-design-library.md), feed results back into strategy revision

## Source
Product Compass (Strategy Red Team framework); red team concept originated from military and cybersecurity domains
