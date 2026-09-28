# TRIZ Contradiction Separation

## Core Concept
When two required system properties pull in opposite directions, the engineering answer is usually not a midpoint compromise but **separation**: let each state hold in a different time, place, condition, or level of the system. A trade-off you have stopped fighting is still a contradiction — this card resumes the fight with method.

## Applicable Scenarios
✅ **Best for**
- Architecture/API parameters with opposite demands: fresh vs cached, stable vs evolving, thorough vs fast
- You are about to accept a trade-off "because you can't have both"
- Every option in the list shares the same structural weakness — the conflict is in the requirements, not the options

⚠️ **When NOT to use**
- A standard pattern already resolves it (cache-aside, CQRS, feature flags, versioning) — use the pattern; it IS a separation
- One option is simply better — pick it; don't manufacture a contradiction
- A cheap measurement settles which side matters — measure, don't separate
- Real physical law (CAP under partition, bandwidth vs latency) — optimize the compromise honestly or move the goal up a level; never fake a dissolution
- People or organization conflicts — separation targets system parameters

## Key Steps
1. **Name it in template form**: "We need [PARAMETER] to be [STATE_1] for [BENEFIT_1] BUT [STATE_2] for [BENEFIT_2]." If the template won't fit, stop — this card doesn't apply.
2. **State the Ideal Final Result (IFR)**: both benefits, no new machinery, no permanent midpoint sacrifice — reframes the goal from "balance the two" to "make the cost not exist".
3. **Try the four separations in order**, keeping the first that delivers both benefits with no hidden compromise:
   - **Time** — state A at one moment, state B at another
   - **Space** — state A in this component/layer, state B in that one
   - **Condition** — state A under this load/context/risk, state B otherwise
   - **Scale** — state A at the interface/aggregate level, state B at the implementation/element level
4. **If separation alone fails, apply a light transform**: segmentation, prior action, inversion, intermediary, copying, dynamization (config/flags), or up a dimension (metadata, versioning, events) — preferring moves that reuse resources the system already has (existing data, traffic, schedulers, side effects).
5. **Test every candidate for relocation**: did the cost leave the system, or just move (to the user, to later, to tech debt)? Moved = disguised compromise — flag where it went.
6. **Lock the resolution**: state the design change, where each state lives, how each benefit survives — or record the residual trade-off explicitly. Refuse TRIZ theater: running the motions and shipping the midpoint anyway is worse than an honest compromise.

## Output Template

```
Contradiction: [cached data] must be [STALE] for [cheap fast reads]
                         BUT [FRESH] for [correct decisions]
IFR: reads fast and cheap AND decisions see current data
Separation: time ✓ — serve cached on read, refresh on write events/TTL
  (pattern check: this IS cache-aside — adopt the standard pattern)
Test: staleness cost relocated to a bounded TTL window — accepted explicitly
Resolution: [cache-aside + 30s TTL on mutable fields, none on immutable]
Residual trade-off: [≤30s staleness, documented for consumers]

Contradiction: [public API] must be [FROZEN] for [client stability]
                         BUT [FREE TO CHANGE] for [product iteration]
IFR: clients never break AND the implementation evolves daily
Separation: scale ✓ — stable versioned contract at the boundary, freedom inside
Resolution: [API versioning + deprecation policy; internals unconstrained]
Residual trade-off: [none — canonical separation]
```

## Failure Modes
- TRIZ theater: generating separations as decoration, then shipping the midpoint compromise anyway
- Relocation posing as dissolution: "just cache it" still pays the staleness cost — name who eats it before calling it solved
- Vague contradiction, fake resolution: fuzzy states or element → fuzzy separations; the template gate exists for this
- Pattern re-invention: burning an afternoon on a bespoke cache/versioning scheme the standard pattern already does better

## Evidence Strength
Strong for the separation principles — time/space/condition/scale separations demonstrably underlie the most successful system patterns (caching, CQRS, versioning, feature flags), which is why the pattern-first guard matters. The full 40-principle matrix is legacy lookup machinery; judgment over separations is the durable part.

## Source
Genrich Altshuller, TRIZ (Theory of Inventive Problem Solving) — separation principles and ideal final result.
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) `thinking-triz` and [systems-thinking-skills](https://github.com/BayramAnnakov/systems-thinking-skills) `triz-dissolve` (both MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns contradiction separation for design trade-offs; no existing entry structured the trade-off-versus-contradiction move.
