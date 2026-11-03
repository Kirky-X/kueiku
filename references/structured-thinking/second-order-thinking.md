# Second-Order Thinking

## Core Concept
Ask "and then what?" to analyze the 2nd, 3rd, and further-order consequences of decisions. First-order thinking sees immediate effects; second-order thinking sees chain reactions, unintended consequences, and systemic effects.

## Applicable Scenarios
✅ **Best for**
- Policy decisions
- Pricing changes
- Ecosystem effect analysis

⚠️ **When NOT to use**
- One-shot, short-horizon, weakly coupled systems — "and then what?" terminates immediately; first-order analysis is sufficient
- Raw uncertainty already swamps the first-order effect — chaining speculations multiplies noise; firm up the base estimate with **Probabilistic Reasoning** first
- Time-critical response — mapping chain reactions is analysis; in live incidents, act first (**OODA Loop**)
- The decision is reversible and cheap to iterate — tracing full chains costs more than the experiment does; try it and observe

## Key Steps
1. State the proposed decision
2. First-order effect: what happens immediately?
3. Second-order effect: what happens as a result of the first-order effect?
4. Third-order effect: what happens as a result of the second-order effect?
5. Map the chain of effects; identify potential unintended consequences
6. Decide: do the long-term consequences outweigh the short-term benefits?

## Output Template

```
Decision: [proposed change]
1st order: [immediate effect — highest confidence]
2nd order: [reaction to the effect: competitor / customer / system response]
3rd order: [consequence of that reaction]
Unintended branch: [the chain you did not design for]
Confidence per level: [H / M / L — decaying with each order]
Verdict: the long-term chain [supports / undermines] the short-term benefit because [mechanism]
Decision: [proceed / modify / reject]
Stop rule: [order beyond which further effects cannot change the choice]
```

## Failure Modes
- Infinite regress: "and then what?" forever and the analysis never lands → stop at the level that changes the decision; write the stop rule before tracing
- Chain as narrative: one vivid doom-chain recounted as the future → generate at least one positive and one negative chain per decision; second-order effects are not uniformly adverse
- Precision theater: order-4 effects stated with the confidence of order-1 → mark confidence decaying per order; distant orders are hypotheses, not forecasts
- Paralysis by chain: every action has bad knock-on effects, so nothing is chosen → chains weigh into the decision, they don't veto it; compare chains across options, not against inaction imagined as consequence-free

## Evidence Strength
Practitioner consensus, thin direct evidence — the underlying mechanism (actions trigger reactions that reshape long-run outcomes: cobweb dynamics, policy feedback, strategic response) is well established in economics and systems research, but "second-order thinking" as a named procedure has no outcome studies; its value is as a discipline against first-order-only reasoning, and chains beyond order 2-3 are mostly structured conjecture.

## Source
Howard Marks, *Mastering the Market Cycle*; mental model popularized by Shane Parrish (Farnam Street).
