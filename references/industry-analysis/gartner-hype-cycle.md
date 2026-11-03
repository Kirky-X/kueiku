# Gartner Hype Cycle

## Core Concept
5-stage technology maturity model: Technology Trigger → Peak of Inflated Expectations → Trough of Disillusionment → Slope of Enlightenment → Plateau of Productivity. Helps time technology investments and adoption decisions.

## Applicable Scenarios
✅ **Best for**
- Technology investment timing
- New technology adoption decisions
- Technology roadmap planning

⚠️ **When NOT to use**
- Timing an individual product bet — stage labels describe technology categories, not your one product; a product built on a "trough" technology can still fail on its own merits → validate the bet with **A/B Test Analysis** and unit economics
- Technology maturity is not the decision variable — when the real question is distribution, pricing, or regulation, the cycle stage changes nothing → **Industry Value Chain**
- No credible published stage exists for the technology — for genuinely new technology there is no assessment to cite, and assigning a stage from a blog post manufactures false precision
- Using a stage label to describe your own company — the cycle is descriptive, so "we are early on a hype-cycle technology" is an unfalsifiable claim that reframes any outcome as success

## Key Steps
1. Identify the target technology
2. Determine current Hype Cycle stage using Gartner reports or equivalent assessment
3. Assess: is the technology past the Trough (approaching productivity) or still inflated?
4. For early-stage tech: plan for experimentation, not production
5. For maturing tech: plan pilots and proof-of-concepts
6. For mature tech: plan production adoption and optimization

## Output Template

```
Technology: [name + the category it belongs to]
Cycle position: [stage name] — basis: [analyst report or equivalent assessment + date]
Signal evidence: [what supports the placement — deployments, standards, funding, adoption numbers]
Decision mode: [experiment | pilot | production adoption | hold]
Budget + horizon: [spend | date to revisit]
If wrong: [the assumption that breaks first | the trigger that pivots the decision]
```

## Failure Modes
- Stage label as the decision: "it is in the trough, so adopt" — the label carries no cost, timeline, or integration requirement → name the actual investment and the trigger that starts it
- False precision on unknown technology: a stage is assigned to a technology no analyst has covered → mark the position "unassessed" and run a small pilot to generate your own evidence
- Vendor narrative capture: the publisher of the cycle also sells research and advisory into the same technology space → triangulate with deployment counts and standards progress, not analyst commentary alone
- Hype as strategy: pairing a cycle position with a marketing claim ("we are at the innovation trigger") → the label lends credibility that the underlying facts have to earn
- Plateau misread as safety: the plateau phase is where incumbents with distribution attack → compare against incumbent incentives, not against the curve position

## Evidence Strength
Contested — the Gartner Hype Cycle is a descriptive communication device, not a measurement instrument. Stage placement is an analyst judgment published as a narrative rather than derived from a repeatable method, and its predictive validity is contested: published placements are frequently disputed or revised as technologies develop, and the framework's survival is better explained by its value as shared vocabulary than by its forecasting accuracy. It works well as a forcing function — it makes the team state a decision mode and a timing horizon — and it should be treated as a prompt to think about adoption, never as evidence for the answer.

## Source
Gartner Group (1995); annual Hype Cycle reports across 30+ technology domains.
