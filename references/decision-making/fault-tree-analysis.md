# Fault Tree Analysis

## Core Concept
Start from one named top event and work **downward** deductively: what must be true for the top event to occur? Each event branches through AND/OR gates until reaching basic events that need no further decomposition. The tree's value is in its **minimal cut sets** — the smallest combinations of failures whose joint occurrence alone produces the top event — which are exactly the things to fix first. Quantitative forms attach probabilities and compute the top-event probability.

## Applicable Scenarios
✅ **Best for**
- One specific, serious failure that demands causal decomposition ("the payment service failed")
- Safety-critical, reliability, and regulatory analysis (aerospace, nuclear, medical, chemical)
- Deciding which single fix breaks the most failure paths

⚠️ **When NOT to use**
- Sweeping a system for whatever might fail → FMEA is bottom-up per component; FTA starts from one event and is the wrong tool when the top event is not yet identified
- The failure is a vague sentence ("the platform failed") → FTA needs one crisp, falsifiable top event; a vague apex produces a meaningless tree
- Ranking many small risks → Risk Matrix (P×I) or FMEA (RPN) handle breadth; FTA is depth on one failure
- Symbolic gates past roughly three levels of OR → the tree stops being maintainable; switch to FMEA or Why Tree
- You cannot enumerate basic events → an unclosed tree is decoration; the leaves are where the work is

## Key Steps
1. Define the top event precisely: one sentence, falsifiable, with the boundary conditions (which system, which time window, what counts as failure)
2. Draw the tree level by level: each event decomposes through an explicit **AND gate** (all children must occur) or **OR gate** (any child suffices) — state the gate type on every branch
3. Stop at basic events: no further decomposition is possible or useful; record each one's boundary condition
4. Extract minimal cut sets: the minimal combinations of basic events that produce the top event (a cut set of size 1 is a single-point failure)
5. Rank by cut-set significance: single-point cuts first, then by expected contribution if quantified
6. Quantify (optional): assign each basic event a probability, compute the top-event probability by Boolean algebra or simulation, and state the independence assumption you relied on
7. Validate against evidence: check each basic event against logs, incident history, and tests — a tree that no incident ever matched is probably the wrong tree
8. Act on the cut sets: fix, add redundancy, or add detection, then re-derive

## Output Template

```
Top event: [one falsifiable sentence + boundary conditions]
Tree:
  [Top event]
   ├─ OR ─ [Event A] ─ AND ─ [basic] / [basic]
   └─ OR ─ [Event B]
Minimal cut sets:
  CS1: [basic A] (single-point — size 1)
  CS2: [basic C] + [basic D]
Significance: [CS1 > CS2 ...] + [what is protected by fixing each]
Quantification: P(top) ≈ [value] under [independence/correlation assumption], or qualitative only
Evidence check: [each basic event: confirmed by log/test | assumed | unknown]
Fixes: [cut set → action → residual risk]
```

## Failure Modes
- Gate confusion (AND vs OR) — the most damaging error, because it silently flips the logic: write the gate type explicitly on every branch and have someone else re-derive one level
- Vague apex event ("system unavailable") → decomposition becomes unfalsifiable; sharpen the top event before drawing anything
- Unclosed leaves: branches stop at "operator error" or "human factors" without the mechanism → drill to the specific condition, or the cut set is useless
- Probability without the independence assumption: basic events in the same subsystem are usually correlated → state the assumption, or run the simulation with correlation and compare
- Combinatorial explosion: the tree grows past what anyone can maintain → prune to the branches that change a decision, and record what you pruned
- Tree drawn but no cut-set analysis: the diagram is the deliverable, the decision never happens → cut sets and fixes are the deliverable
- Confirming bias in the evidence check: only looking for the leaves that fit the suspected cause → check the leaves you expect to be absent too

## Evidence Strength
**Mixed.** Safety-critical practice is standardized and long-established (IEC 61025 syntax, nuclear and aerospace certification), and the qualitative decomposition discipline is genuinely useful. The quantitative form is weaker than it looks: multiplying probabilities assumes independence among basic events, and in real systems basic events sharing a common cause are the rule — which is why industry practice leans on cut-set analysis and simulation over closed-form products.

## Source
IEC 61025, *Fault Tree Handbook* (1992); US NRC NUREG-0492, *Fault Tree Handbook* (1982); Edward F. Singleton, "The Essence of Fault Tree Analysis"; Edward O. Robinson, "Fault Tree Analysis" hmm — Robinson's is the standard textbook (1983). Admission verdict: **Build** (v0.1.15) — the v0.1.13 Recipe verdict (FMEA "owns" it) was factually wrong: no entry held FTA, so the pointer in `fmea.md` was a dead route; FTA complements rather than duplicates FMEA's question (one top event downward vs many components upward).
