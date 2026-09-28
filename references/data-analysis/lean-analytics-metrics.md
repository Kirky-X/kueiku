# Lean Analytics Metrics

## Core Concept
Framework for selecting the right metrics using 4 criteria + 8 metric types + North Star Metric (NSM) 4 layers. Helps teams avoid vanity metrics and focus on actionable, leading indicators.

## Applicable Scenarios
✅ **Best for**
- Metrics framework selection
- Defining what "good" looks like for your product
- Aligning team around actionable metrics

⚠️ **When NOT to use**
- Instrumentation doesn't exist — metric design without data plumbing produces aspirational dashboards
- Pre-product/market fit — the book's whole point is the metric changes per stage; installing a growth-stage NSM early misleads
- One-off analysis questions — use the analysis tool directly; this framework is for choosing standing metrics

## Key Steps
1. Apply the 4 criteria: Is it actionable? Accessible? Auditable? (4th: is it relevant?)
2. Identify which of the 8 metric types applies: Trending, Ranked, Ratio, Percentage, Average, Median, NPS, etc.
3. Define your NSM across 4 layers: Input metrics → Throughput metrics → Output metrics → Outcome metrics
4. Validate: does the metric drive decisions? Is it leading or lagging?
5. Build a metrics dashboard aligned to the NSM hierarchy

## Output Template

```
Stage: [empathy / stickiness / virality / revenue / scale] — business model: [type]
North Star Metric: [one metric, outcome-flavored] — why it's the best proxy for delivered value: [reason]

NSM hierarchy:
  Input metrics    → [signups started, content created]      (team moves these weekly)
  Throughput       → [activation rate, funnel conversion]    (process health)
  Output metrics   → [WAU, paid conversions]                 (product results)
  Outcome metrics  → [revenue, retention-adjusted growth]    (business results)

Vanity purge: [pageviews / total downloads / registered users] — why excluded: [only goes up, no decision attached]
4-criteria check on NSM: actionable [how a decision changes] / accessible [who can query it] / auditable [can we verify] / relevant [to this stage: y/n]
Review cadence: [weekly inputs / monthly outputs]
```

## Failure Modes
- NSM by committee averaging: a "blended" metric nobody can move → one metric, owned by one team, with a stated causal story to outcomes
- Input-output confusion: celebrating input spikes (ship count) as outcome progress → dashboards must label layers; inputs are levers, not wins
- Metric ossification: the stage changed, the metric didn't → re-derive NSM at every stage transition (and after major pivots)

## Evidence Strength
Practitioner consensus — the good-metric criteria (actionable, accessible, auditable) are standard measurement hygiene and the stage-model is a useful heuristic from lean practice; the specific 8-type taxonomy and NSM layering are organizing devices without independent empirical validation — metric quality is ultimately judged by whether decisions improve.

## Source
Alistair Croll & Benjamin Yoskovitz, *Lean Analytics* (2013).
