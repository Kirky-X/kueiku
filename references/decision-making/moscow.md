# MoSCoW Method

## Core Concept
Requirement scoping using 4 categories: Must have (non-negotiable), Should have (important but not vital), Could have (nice to have), Won't have (explicitly out of scope this time). Creates clear boundaries for delivery.

## Applicable Scenarios
✅ **Best for**
- Scope management
- Requirement classification
- Sprint planning

⚠️ **When NOT to use**
- Solo decision-maker, small scope — four buckets add ceremony a simple ordered list doesn't; the method's value is stakeholder negotiation, not classification
- No shared delivery deadline — Must/Should only bites against a fixed release; without one, everything drifts into "eventually"
- The real question is sizing or value-per-effort — MoSCoW orders requirements but never measures them; use **RICE Scoring** when ranking needs numbers
- Backlog as long-lived wishlist archive — buckets decay as Musts ship and Shoulds fossilize; re-classify per release, not once forever

## Key Steps
1. List all requirements/features
2. Classify each into M/S/C/W with stakeholder agreement
3. Must have: if removed, the deliverable is useless
4. Should have: important but the deliverable still works without it
5. Could have: desirable but not necessary
6. Won't have: explicitly excluded from this delivery (may be future)
7. Validate: Must haves should be ≤ 60% of total effort

## Output Template

```
Delivery: [release / sprint + date]
Must have (≤60% of effort):
  - [requirement] — the deliverable is useless without it
Should have:
  - [requirement] — deliverable works without it, degraded
Could have:
  - [requirement] — nice to have, first to drop under pressure
Won't have (this round):
  - [requirement] — explicitly out; revisit on [trigger]
Check: Must effort [n% of total] — [under cap / rebalance needed]
Stakeholders agreeing: [names]
```

## Failure Modes
- Everything lands in Should: nobody will kill a requirement, so the buckets fill with S → force a Won't list every round; an empty W means the classification didn't happen
- Must inflation: every stakeholder's pet feature is declared critical → apply the test in writing ("if removed, the deliverable is useless") and enforce the ≤60% effort cap
- Could as consolation prize: disagreements get parked in C instead of resolved → a C item must be droppable with no follow-up promise; otherwise it is an S or a W
- Buckets without negotiation: one person silently bucket-lists the backlog → MoSCoW is a stakeholder agreement ritual; classifying without the disagreement on the table produces fiction

## Evidence Strength
Practitioner consensus — standard scope vocabulary since DSDM, kept alive by the one thing it forces: an explicit Won't list and a visible scope cut. Evidence on delivery outcomes is anecdotal, and its known failure (bucket inflation without a facilitator) is documented in agile practice rather than controlled studies.

## Source
Dai Clegg, *MoSCoW Method* (1994); used in DSDM agile methodology.
