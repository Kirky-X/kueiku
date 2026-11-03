# North Star Framework

## Core Concept
Define one North Star Metric (NSM) that best captures the core value your product delivers to customers, plus 3-5 input metrics that drive it. Aligns the entire organization around a single growth direction.

## Applicable Scenarios
✅ **Best for**
- Metrics framework design
- Company-wide growth alignment
- Cross-functional coordination

⚠️ **When NOT to use**
- Pre-PMF products — core value is still being discovered; locking a metric entrenches a wrong hypothesis
- Multi-sided or heavily multi-segment products — a single blended NSM can hide one side's decline; define per-side metrics alongside
- Gameable metrics — signups, sessions, raw counts rise while value falls; any NSM needs counter-metrics from day one
- Metric diagnosis — the framework aligns direction but doesn't explain why a number moved; use **Cohort Analysis** or **RFM Model** to dissect changes

## Key Steps
1. Define your product's core value proposition
2. Identify the metric that best captures that value delivery (NSM)
3. Good NSM criteria: reflects customer value, is a leading indicator, is actionable, is measurable
4. Identify 3-5 input metrics that drive the NSM
5. Build a metrics hierarchy: Input Metrics → NSM → Business Outcomes
6. Align teams around input metrics they can influence

## Output Template

```
Core value proposition: [what value, for whom]
North Star Metric: [precise, auditable definition]
  Why it captures customer value: [reasoning]
  Checks: leading? actionable? measurable? game-resistant? [assessment]
Input metrics (3-5): [each with owning team + baseline + target]
Counter-metrics: [what catches gaming / quality erosion]
Hierarchy: [input] → [NSM] → [business outcome]
Review cadence: [who reviews what, how often]
Re-validation trigger: [strategy shift that forces an NSM rethink]
```

## Failure Modes
- Gamed metric: the NSM climbs while customer value falls (signups, sessions, low-intent actions) → pair the NSM with counter-metrics and quality thresholds that can veto growth
- Proxy drift: the metric stops tracking value as the product evolves → treat the NSM as a hypothesis and re-validate it on strategy shifts
- Input sprawl: 15 input metrics nobody owns → cap at 3-5, each with a named owning team and a baseline
- One-metric tyranny: optimizing a blended NSM by sacrificing a segment or marketplace side → segment the NSM or add per-side metrics; averages hide collapsing cohorts

## Evidence Strength
Practitioner consensus — the framework is standard growth practice and reliably aligns organizations around value delivery, but metric choice is judgment rather than science: a wrong NSM efficiently aligns the whole company in the wrong direction, which is why counter-metrics and periodic re-validation are mandatory companions rather than optional extras.

## Source
Sean Ellis & Morgan Brown, *Hacking Growth* (2017); Amplitude's North Star framework.
