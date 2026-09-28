# Opportunity Solution Tree

## Core Concept
Align business outcomes with discovery work through a 4-layer structure: Outcome → Opportunities → Solutions → Experiments. Force focus on "opportunities" (user pain points/needs) at each layer rather than jumping straight to solutions, avoiding "build it and they won't come."

## Applicable Scenarios
- Continuous product discovery, need to align team work with business goals
- Prevent PMs from jumping to solutions without mining user opportunities
- When multiple solutions need parallel experiments, unify discovery planning

⚠️ **When NOT to use**
- No measurable outcome exists — a tree without a real target metric becomes an idea landfill
- One-off feature work with a settled opportunity — the full tree is overhead for a single known problem
- No interview pipeline feeding it — a tree built from internal brainstorming inherits every blind spot of the room

## Key Steps
1. Define the desired Outcome (business result, not feature output), e.g. "improve new user first-week retention by 20%"
2. Mine Opportunities through user interviews (user pain points/needs/unmet scenarios under this goal), prioritize by layer
3. Design multiple Solution candidates for each priority Opportunity (encourage divergence, at least 3)
4. Design minimum Experiments for each Solution (first-click/fake door/prototype etc.) to validate hypotheses
5. Weekly meeting traces bottom-up through the tree: experiment results → solution decisions → opportunities covered → outcome progress

## Output Template

```
OUTCOME: [first-week retention +20%] — baseline [x], owner [name]
├── Opportunity: [can't see value before setup is done] (n interviews: 7/12 mentioned)
│   ├── Solution A: [template gallery] → Experiment: [fake-door CTR, threshold ≥8%]
│   ├── Solution B: [guided first-run] → Experiment: [prototype 5-user test]
│   └── Solution C: [import from competitor] → Experiment: [concierge, 5 accounts]
├── Opportunity: [doesn't know what to do after signup] (5/12)
│   └── [solutions + experiments]
└── Deprioritized: [opportunities outside outcome scope — logged with reason]

Weekly trace: [experiment result] → [solution killed/iterated] → [opportunity still open?] → [outcome progress: +x pp]
```

## Failure Modes
- Solution layer smuggled into opportunity layer: "users want a dashboard" is a solution → opportunities are phrased as user pain/need, never as artifacts
- Interview-starved tree: opportunities invented in planning meetings → every node cites interview evidence (n mentions, recency); unfed nodes get pruned
- Tree as wall art: built once in a workshop, never traced weekly → the bottom-up weekly trace is the mechanism; a stale tree is worse than none because it lends false structure

## Evidence Strength
Practitioner consensus — a structuring practice from continuous discovery coaching; widely adopted by product orgs and coherent with evidence-based iteration norms, but there is no controlled study that OST adoption improves outcomes — its value is preventing solution-jumping, which is a process gain, not a causal claim.

## Source
Teresa Torres, *Continuous Discovery Habits* (2021)
