# Experiment Design Library

## Core Concept
A menu of 7 experiment types for validating hypotheses at minimum cost before committing to full development. Each experiment type tests a specific assumption with a specific fidelity level.

## Applicable Scenarios
- Need to validate product hypotheses before building
- Choosing the right experiment type for each assumption
- Building a culture of experimentation

⚠️ **When NOT to use**
- Unnamed assumptions — picking an experiment type before stating the hypothesis guarantees a vague result; write the falsifiable hypothesis and threshold first
- Core UX validation via fake door or landing page — those measure willingness to click, not whether the product works
- Demand magnitude from interviews alone — conversations reveal problems, not quantified demand; pair with **Survey Design** or a landing-page test
- Cost-mismatched experiments — running a concierge MVP to validate copy wording is waste; match experiment cost to assumption risk

## Key Steps
1. Identify the riskiest assumption to validate
2. Select the cheapest experiment type that can test it (see types below)
3. Define success criteria in advance (minimum threshold)
4. Run the experiment with minimum investment
5. Measure results against success criteria; decide Pivot / Persevere / Kill

## Experiment Types
1. **Customer Interview** — Test problem existence (lowest fidelity)
2. **Survey** — Test demand magnitude
3. **Landing Page Test** — Test interest/click-through
4. **Fake Door Test** — Test willingness to engage
5. **Concierge MVP** — Test full solution manually
6. **Wizard of Oz** — Test with manual backend, automated frontend
7. **Prototype Test** — Test usability and desirability (highest fidelity)

## Output Template

```
Hypothesis: [we believe X; if true, Y follows]
Riskiest assumption: [the one that kills the project if wrong]
Experiment type: [interview / survey / landing page / fake door / concierge / wizard of oz / prototype]
Cost: [time, effort]  Fidelity: [low → high]
Success criteria (set BEFORE running): [metric ≥ threshold]
Run window: [duration, sample]
Result: [measured value vs threshold]
Decision: [Pivot / Persevere / Kill] — based on [evidence]
Next assumption: [what gets tested next]
```

## Failure Modes
- Criteria after the fact: defining "success" once results are in turns every outcome into a win → write the threshold and sample size before launch; pre-registration is the whole discipline
- Wrong fidelity: a fake door can't answer usability questions and a prototype can't answer demand magnitude → match experiment type to the assumption class, not to what's easiest to build
- Testing the safe assumption: validating what's easy instead of what's fatal → rank assumptions by "if wrong, the project dies" and test the top one
- Experiment theater: running tests whose results change no decision → pre-commit to the Pivot/Persevere/Kill mapping; if no outcome would change the decision, don't run it

## Evidence Strength
Practitioner consensus — the experiment menu is standard lean-startup practice synthesized from Ries, Torres and practitioner canvases; there is no comparative research ranking the experiment types against each other, and validity depends on honest pre-registered success criteria rather than on the menu itself.

## Source
Adapted from Eric Ries *The Lean Startup*, Dave lands Experiment Canvas, and Teresa Torres *Continuous Discovery Habits*.
