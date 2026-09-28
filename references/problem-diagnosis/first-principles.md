# First Principles Thinking

## Core Concept
Break down a problem to its most fundamental truths (axioms), then reason up from there — rather than reasoning by analogy or convention. Forces you to question every assumption and rebuild from the ground up.

## Applicable Scenarios
- Innovative design where existing solutions are inadequate
- Disrupting conventional approaches
- Breaking through mental models and industry assumptions

⚠️ **When NOT to use**
- The conventional solution is actually near-optimal — rebuilding from axioms to rediscover the standard answer is expensive theater
- Safety-critical domains with codified practice — conventions encode failures you haven't lived; deviate deliberately, not casually
- Time-boxed execution work — reserve this for design and diagnosis, not for sprint tasks

## Key Steps
1. State the current assumption or conventional approach clearly
2. Ask: "What are the fundamental truths we know with certainty?"
3. Challenge every other assumption: "Is this a law of physics, or just a convention?"
4. Reconstruct the solution from the fundamental truths upward
5. Compare the first-principles solution with the analogy-based solution; identify the delta

## Output Template

```
Problem: [goal + current cost/constraint]

Assumption inventory:
  | Conventional belief                     | Fundamental truth or convention? | Evidence if fundamental |
  | [batteries cost $600/kWh, always have]  | convention — spot prices were $[x]  | [materials breakdown: ...] |
  | [launch needs a full rocket]            | partially convention            | [physics: propellant mass ratios] |

Fundamental truths (only what survives): 1. [...] 2. [...] 3. [...]

Rebuild from truths: [how would we solve it if only the truths applied]
Delta vs analogy-based solution: [what changes, what it's worth in cost/time/feasibility]
Cheapest test of the rebuilt approach: [experiment by date]
```

## Failure Modes
- "First principles" as rhetoric: calling any fresh-thinking session first-principles while every assumption survives unchallenged → the assumption inventory with explicit convention/truth verdicts is the method; skip it and you did nothing
- Wrong floor: stopping at "industry best practice" instead of physics, math, or verified data → keep asking "why is this true?" until you hit evidence or a law
- Rebuild abandoned at friction: the from-truths design meets its first hard problem and quietly becomes the conventional design again → write the delta explicitly before comparing costs

## Evidence Strength
Practitioner consensus — a reasoning discipline with philosophical roots and famous applied cases (cost rebottoming in manufacturing); its value is assumption surfacing, and its cost is time — there is no systematic evidence on when it beats analogy-based reasoning, which in most situations remains the efficient default.

## Source
Aristotle; popularized in modern business by Elon Musk.
