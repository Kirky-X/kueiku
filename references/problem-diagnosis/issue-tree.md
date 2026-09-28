# Issue Tree — Hypothesis-Driven Decomposition

## Core Concept
Split a fuzzy problem into a MECE tree of answerable sub-questions, then resolve it hypothesis-first. **Boundary**: MECE + Pyramid (`structured-thinking/mece-pyramid.md`) structures *communication*; the issue tree structures *analysis*. 5 Whys traces one chain backward; Fishbone fans out by fixed dimensions; the issue tree decomposes forward and drives the evidence hunt.

## Applicable Scenarios
✅ Large vague problems ("why is margin declining?") needing parallelizable workstreams · team investigations, where each branch is a work package · limited analysis budget — the tree tells you which analyses to skip
⚠️ **When NOT to use**: single-chain causation (5 Whys is faster) · pure reporting — the answer is settled and only needs expression (use MECE + Pyramid directly) · zero domain knowledge (orient before attempting a Day-1 answer)

## Key Steps
1. **State the problem as a question** ("Why is X below Y?"), not a solution in disguise.
2. **Write the Day-1 answer**: "If I had to recommend right now, what would I say?" A disposable lead hypothesis — the thing to disprove, not defend.
3. **Decompose MECE**, 2–4 levels: each layer mutually exclusive, collectively exhaustive. Overlap double-counts causes; gaps let causes escape.
4. **Turn leaves into killer analyses**: name the one check that settles each leaf ("if raw-material inflation drives this, COGS/unit rose faster than price"); run cheapest first.
5. **Mark each node validated / refuted / open**, prune dead branches, deepen live ones, converge: restate the Day-1 answer as confirmed, revised, or overturned — all three are legitimate outcomes.

## Output Template

```
Problem question: [single question] · Day-1 answer: [disposable hypothesis]

? Why is [metric] off target?
├─ Branch A: [sub-question] — validated/refuted/open — evidence: [...]
│   └─ A.1 [leaf question] — [status] — check: [...]
└─ Branch B: [sub-question] — [status] — evidence: [...]

Converged answer: [surviving branches → revised or overturned Day-1 answer]
Open nodes: [leaf → cheapest discriminating check]
```

## Failure Modes
- **Fake MECE**: overlapping or omitting branches — per layer, can any two items merge? does any cause fit nowhere?
- **Boiling the ocean**: equal depth everywhere — deepen only branches the Day-1 answer and early evidence mark as live.
- **Anchoring**: evidence slots filled by the Day-1 assumption instead of checks — log node statuses honestly; an overturned answer is a result.
- **Tree that never converges**: endless expansion, every validated branch sprouting two more — cap depth at 2–4 levels and force the converge step; "where to look next" is a legitimate landing.

## Evidence Strength
Practitioner consensus — hypothesis-driven decomposition is the standard consulting/ROOT-cause playbook for large vague problems; MECE is a communication discipline, not an empirical law, and tree quality is bounded by the domain expertise of whoever cuts the branches.

## Source
McKinsey-style problem structuring; hypothesis-driven consulting practice (MECE lineage of Barbara Minto).
Provenance: framework ideas absorbed from [claude-skill-management-consultant-B1](https://github.com/DogInfantry/claude-skill-management-consultant-B1) FRAMEWORKS.md (Apache-2.0 license), absorbed 2026-09.
Admission: Build (new entry) — owns hypothesis-driven forward decomposition of an unsolved problem; MECE + Pyramid Principle structures the communication of an already-formed answer.
