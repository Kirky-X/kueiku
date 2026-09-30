# Lean BML Loop (Lean Build-Measure-Learn Loop)

## Core Concept
Minimize assumptions → Build the minimum thing to test → Measure results → Learn and decide (pivot or persevere). The fastest loop wins.

## Applicable Scenarios
✅ **Best for**
- Product validation
- MVP design
- Hypothesis testing

## Key Steps
1. State the riskiest assumption clearly
2. Design the minimum build to test it (not a full product — the smallest experiment)
3. Define success metrics and threshold in advance
4. Build and run the experiment
5. Measure: did it meet the threshold?
6. Learn: Pivot (change assumption) or Persevere (continue)

## When NOT to use

- The riskiest assumption is already verified — the loop re-tests a settled question and burns a cycle for nothing
- Safety-critical or irreversible domains (medical dosing, structural load, security controls): "minimum build to test" and "pivot" are the wrong vocabulary
- Regulated processes where the experiment itself must be protocol-compliant (clinical trials, financial model validation)
- A team with one committed direction and no capacity for parallel experiments — the loop optimizes iteration speed, not delivery speed

## Output Template

```
Riskiest assumption: [the one whose falsity kills the plan]
Minimum build to test it: [smallest artifact + what it deliberately omits]
Success metric + threshold: [number, fixed BEFORE the run]
Result: [metric measured] vs [threshold] → met / missed
Decision: Pivot (assumption was wrong because…) | Persevere (assumption held; next riskiest assumption is…)
```

## Failure Modes

- **Threshold set after seeing results** — the loop quietly becomes "keep building what works"; write the number before the run or it is not a test
- **The minimum build grows into a product** — scope creep between steps 2 and 4; anything not required to falsify the assumption is out
- **Measuring activity instead of the assumption** — shipping is not learning; the metric must move if the assumption is false
- **Pivoting without naming the next riskiest assumption** — the loop restarts at "build" and skips the diagnostic

## Evidence Strength

**Practitioner consensus on the loop, weaker on "fastest loop wins."** The build-measure-learn framing is the most widely adopted loop in product practice. The speed claim is weaker: a fast loop only helps when the assumption under test is genuinely the riskiest, which is a judgment the framework cannot verify for you.

## Source
Eric Ries, *The Lean Startup* (2011).
