# Theory of Constraints (Five Focusing Steps)

## Core Concept
A flow system's end-to-end throughput is set by exactly one binding constraint; improving anything else moves nothing. The Five Focusing Steps fix the order of operations: Identify → Exploit (free) → Subordinate (discipline) → Elevate (spend, only if still short) → Recheck (the constraint moves). The constraint is usually not a machine or a person but a **policy** — a forgotten rule, metric, or assumption. This is the system-level sibling of Performance Optimization: profiling finds code hotspots inside a stage, TOC finds which stage binds the whole flow and in what order to act.

## Applicable Scenarios
✅ **Best for**
- Work piles up before one stage while downstream idles (review queue, deploy pipeline, support backlog, hiring funnel)
- Adding capacity or headcount anywhere fails to raise end-to-end output
- Deciding where limited improvement budget goes, in what order

⚠️ **When NOT to use**
- Load evenly spread, no stage dominates — there is no single constraint to exploit
- Correctness fault, not flow rate — debug it
- Bottleneck hops between stages every run — concurrency/contention design problem
- Constraint known and fix cheap — just apply it
- Demand-constrained or exploratory systems — the limit is the market or unknown knowledge; forcing a permanent bottleneck there is cargo-cult TOC

## Key Steps
1. **Define the flow and the goal**: name the unit of work and the end-to-end throughput metric — never local utilization.
2. **Identify with evidence**: follow the pile (WIP accumulates immediately upstream of the constraint) and compare stage rates; supporting signals: near-saturated utilization, longest queue, lowest stage rate, more input stops raising output. Then classify **resource** (genuinely capacity-limited) vs **policy** (a rule/metric/assumption creates the cap). Default suspicion: policy — ask "what rule created this pile?"
3. **Exploit at zero spend**: constraint never idle, never work on defects, cut its setup and wait time.
4. **Subordinate**: pace upstream release to the constraint's consumption rate, cap WIP; fast stages must accept idle. Most resisted step — resistance signals the diagnosis is right.
5. **Elevate only if still short**: buy capacity, shard, parallelize. For a policy constraint, "elevate" = change the rule — usually free, usually dominates buying capacity.
6. **Recheck**: after any fix, remeasure all stages — the constraint has moved. Kill rules written to protect the old constraint; inertia is where the next one hides.

## Output Template

```
Goal: [tickets resolved/week ≥ 200]
Flow: intake → triage → investigation → fix → verify  (rates: [...])
Constraint: [investigation] — POLICY (queue 3.2 days; stage rate 140/wk caps system)
  rule behind it: [only seniors may investigate]
Exploit: [pre-triage checklists → clean input; +15%]
Subordinate: [cap intake WIP at constraint rate; tier-2 accepts idle]
Elevate: [change the approval rule before hiring — free vs $X/mo]
Watch: [re-measure all stage rates; constraint likely moves to verify]
```

## Failure Modes
- Elevate-first: buying capacity before exploiting and subordinating — the most common, most expensive error
- Mirage optimization: an hour saved at a non-constraint raises nothing but inventory
- Resource-by-default diagnosis: calling it a staffing problem when one rule change lifts the cap free
- Activity metrics: rewarding busy stages and utilization instead of system throughput

## Evidence Strength
Strong — the five-step structure recurs independently across operations, software delivery, and systems-thinking practice, and the resource-vs-policy split matches everyday experience. The specific constraint is only as good as its queue/rate evidence: no pile, no TOC.

## Source
Eliyahu M. Goldratt & Jeff Cox, *The Goal* (1984) — Theory of Constraints and the Five Focusing Steps.
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) `thinking-theory-of-constraints`, [systems-thinking-skills](https://github.com/BayramAnnakov/systems-thinking-skills) `constraint-finder`, and [knowledge-skills](https://github.com/deciqAI/knowledge-skills) `theory-of-constraints` (all MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns system-level bottleneck ordering across stages; Performance Optimization finds code hotspots inside a stage, not which stage binds the flow.
