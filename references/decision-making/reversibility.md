# Reversibility Grading

## Core Concept
Size the process to the cost of un-deciding. Most commitments prove easier to unwind than they feel — ceremony on a days-reversible call steals time from the few that truly lock in. Grade undo cost first; deliberate only as deeply as the grade demands.

## Applicable Scenarios
✅ **Best for**
- No shared answer for how much analysis a choice deserves (tech, product, process, org)
- Low-blast-radius calls drifting toward committee review; high-lock-in ones toward snap decisions
- Wrong moves and waiting recover very differently
- Room to reshape the move (pilot, flag, abstraction, time-box) into something cheaper to undo

⚠️ **When NOT to use**
- Choices so small grading outlasts deciding — just make the call (names, local cleanups)
- Optionality never yours (mandate, signed obligation, date fixed elsewhere) — nothing left to grade
- Gates valued for being right, not fast (security review, data integrity)
- Already graded this session — execute at that depth; re-grade only on new undo-cost evidence

## Key Steps
1. **Name the decision and its reverse route**: what gets committed, concretely how to walk it back — re-deploy the previous build, restore the prior schema. No nameable reverse route → treat as more binding until one is demonstrated
2. **Grade the undo cost**: reversal effort, clock time, cash, reputation, who depends on the status quo, learning discarded:
   - **Type 2** — walk back within days, cheap → decide now
   - **Type 1.5** — weeks away, moderate cost → light structure with active monitoring
   - **Type 1** — months or effectively final → deliberate, then stage commitment
3. **Weigh the downside asymmetrically** (Type 1/1.5): wrong move — how bad, recoverable at what price? No move — what closes for good (window, exclusivity, forked-away path)? Recoverable damage + closing window → staged commitment, not indefinite delay; unrecoverable or third-party harm → refuse or reshape first
4. **Reversibilize before deliberating**: pilots, feature flags, interface abstractions, versioned rollouts, time-boxed vendor terms — each turns a would-be Type 1 commitment into a cheap Type 2 probe; deliberate only the irreducible core
5. **Commit at the graded depth**: Type 2 — pick a sound option, ship, watch it. Type 1 — record load-bearing assumptions, argue the strongest opposing case, escalate if stakes demand. Grade and depth set → stop; reopen only on new undo-cost evidence

## Output Template

```
Decision: …
Reverse route: …
Grade: Type 2 | Type 1.5 | Type 1 (weighed on: …)
Wrong-move damage / recovery: …
What waiting closes for good: …
Reversibilizing move: pilot | flag | abstraction | time-box | none
Depth of process: decide now | pilot first | deliberate fully
Commitment: …
```

## Failure Modes
- "We can always change later" with no named reverse route or cost → reversibility asserted, not demonstrated; raise the grade until produced
- Two-way-door vocabulary used to skip verification on data, security, or public commitments — verification effort tracks blast radius, not the metaphor
- Deliberation machinery on routine Type 2 work — the grading exists to buy speed where it is safe, not a ritual on every choice

## Boundaries with Adjacent Methodologies
- `death-filter.md` answers **whether** — a values-level existential filter for major life/career/startup calls; Reversibility Grading answers **how deep a process the decision deserves**. On big calls they compose: filter first, then grade
- `premortem-counterfactual.md` rehearses the risks of a chosen plan before commitment; Reversibility Grading decides how much rehearsal the plan deserves in the first place

## Evidence Strength
Practitioner consensus — the two-way/one-way door distinction is widely credited for speeding reversible calls and slowing irreversible ones; the intermediate grade and staging moves are practitioner refinements, undo-cost estimates remain prone to optimism bias, and no formal research validates the specific thresholds.

## Source
Practitioner decision-speed heuristics; the Type 1 / Type 2 door framing was popularized by Jeff Bezos's shareholder letters, extended here with an intermediate grade and option-preserving redesign moves.
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) `thinking-reversibility` (MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns execution-level process grading by undo cost; Death Filter covers the values-level should-we-do-it question at a different layer.
