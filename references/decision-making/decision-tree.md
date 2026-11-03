# Decision Tree & Expected Value

## Core Concept
Structure a one-shot choice under uncertainty as a tree: decision nodes (your options) branch into chance nodes (outcomes with probabilities) ending in payoffs; roll expected values back from the leaves and pick the maximum-EV branch. EV is the starting point, not the verdict — a decision survives only after a risk check (variance, ruin, reversibility) and a sensitivity read (which input actually swings the choice).

## Applicable Scenarios
✅ **Best for**
- Discrete options with probabilistic, quantifiable outcomes: build vs buy, settle vs litigate, pivot vs persevere
- Making explicit the probabilities a plan was silently assuming
- Pricing an information purchase (what is another month of research worth?)

⚠️ **When NOT to use**
- Estimating one uncertain quantity (no choice among gambles) → Probabilistic Reasoning — different question: a number vs a branch
- Scoring options on criteria without probability structure → Decision Matrix — different question: preference vs expectation
- Outcomes that cannot be assigned even rough monetary/utility values → Decision Matrix or qualitative frameworks
- Probabilities pure invention with no base rate → garbage EV; get a reference class first
- A strictly dominant option exists → skip the tree, state the dominance

## Key Steps
1. Frame the decision, time horizon, and alternatives — include "do nothing" as a branch
2. Identify the key uncertainties per branch (prune to decision-relevant ones)
3. Assign probabilities: base rates first, adjust by evidence (likelihood-ratio discipline)
4. Assign payoffs: full consequence per leaf (costs, second-order effects), not revenue alone
5. Roll back: EV at chance nodes, max-EV choice at decision nodes
6. Sensitivity: one-at-a-time swings — which probability or payoff flips the choice, and how far
7. Risk check: ruin/downside survival, variance tolerance, reversibility grading of the leading branch
8. Decide; record assumptions and the sensitivity verdict with the output

## Output Template

```
Decision: [question + horizon]
Branches: [option → chance node → outcomes (probability, payoff)]
EV per branch: [rolled-back values]
Sensitivity: [the input that flips the choice + flip threshold]
Risk check: [worst case per branch | survivable? | reversible?]
Verdict: [max-EV choice, risk-adjusted if needed, confidence + assumptions recorded]
```

## Failure Modes
- Invented probabilities laundered as math: the tree looks rigorous, the priors are vibes → base-rate anchoring mandatory; state confidence per probability
- Payoffs missing second-order effects: competitor response, precedent, morale → feed branches from Second-Order Thinking
- EV worship under ruin risk: maximizing expected value while risking non-survival is wrong for the decision-maker — risk-adjust or constrain the downside first
- Tree explosion: every contingency mapped → prune to branches that could change the choice
- Sunk-cost branches: only future payoffs belong in the tree; what was spent is spent

## Evidence Strength
Strong normative core — decision analysis is axiomatically grounded (Savage, Howard) and standard in energy, pharma, and litigation strategy; applied transfer is mixed because outputs are dominated by input quality, and sensitivity analysis is the part with the best practice record.

## Source
Howard Raiffa, *Decision Analysis* (1968); Ronald A. Howard, "Decision Analysis: Applied Decision Theory" (1966). Admission verdict: **Build** (v0.1.12) — choice-among-gambles is a third question type in this category, distinct from estimation (Probabilistic Reasoning) and preference scoring (Decision Matrix); folding it into either would blur all three.
