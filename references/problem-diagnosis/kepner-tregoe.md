# IS/IS-NOT Difference Analysis (Kepner-Tregoe)

## Core Concept
Diagnose a *selective* deviation by asking not only "where does it occur?" but "**where does it NOT occur, though it plausibly could?**" The IS vs IS-NOT boundary is a discriminator: a valid cause must explain *both* sides. Flipped to choices it becomes Decision Analysis: screen on pass/fail MUSTs, rank survivors on weighted WANTs, expose what could reverse the ranking. Boundary discrimination is its unique mechanism among the diagnosis cards (positioning table below).

## Applicable Scenarios
✅ A defect hits some objects, locations, times, or cohorts but not comparable others ("only EU, only since Tuesday") · several candidate causes the boundary can discriminate · a consequential choice with explicit non-negotiables
⚠️ **When NOT to use**: uniform, non-selective failure — with no meaningful contrast, IS/IS-NOT has no discriminating power (use 5 Whys) · no comparable non-cases exist to fill the IS-NOT side · cause already confirmed or one cheap observation settles it · forward failure discovery for a planned change (premortem territory)

## Key Steps

**Mode 1 — Problem Analysis**
1. Frame the deviation: object, defect, location, time, extent.
2. For WHAT / WHERE / WHEN / EXTENT record IS, the closest comparable IS-NOT, and the distinction unique to the IS side; list changes near first occurrence.
3. Generate candidates from distinctions + changes; a candidate **survives only if it explains both IS and IS-NOT** — reject causes fitting only the IS side.
4. Run the cheapest discriminating check; stop when one verified cause explains the full boundary.

**Mode 2 — Decision Analysis**
1. Define MUSTs (pass/fail) and WANTs (weight 1–10) **before** scoring — post-hoc weights invite reverse-engineering.
2. Eliminate options failing any MUST; never rescue them with high WANT totals.
3. Score survivors per WANT; for leaders, list adverse consequences (probability × impact) and the assumption or weight change that would flip the ranking.
4. Decide — or return "none passes the MUSTs" rather than force a winner.

## Output Template

```
Problem Analysis — deviation: [object + defect + where/when/extent]
| Dimension | IS | IS-NOT (closest) | Distinction |   ← WHAT/WHERE/WHEN/EXTENT
Nearby changes: [...] · Candidates: [cause → explains both sides? y/n]
Verified cause: [...] or next check: [...]

Decision Analysis — decision: [...] · alternatives: [A, B, C]
MUST screen: [...] → eliminated: [...]
WANT matrix (weight × score) → totals: [...]
Leader risks: [risk → p × impact] · flips if: [...]
Choice: [...] or "none passes — reopen criteria"
```

## Four-Way Positioning (diagnosis cards)

| Card | Motion | Reach for it when |
|------|--------|-------------------|
| 5 Whys | Single chain, backward | One obvious causal thread |
| Fishbone | Divergent, all cause families | Team brainstorm, unknown factors |
| Issue Tree | Forward decomposition + evidence hunt | Big vague problem, workstreams |
| IS/IS-NOT | Boundary discrimination | The failure is *selective* — contrasts discriminate causes |

## Failure Modes
- **Contrast-free matrix**: IS-NOT rows filled with non-comparable cases — the distinction column turns to noise → pick the *closest comparable* non-case, not any non-case.
- **Score theater**: WANT weights tuned until the preferred option wins → fix weights and scale before scoring; report the flip condition.
- **Forced winner**: no cause explains both sides, no option passes the MUSTs, yet the template demands an answer → return open/none; that is a finding.

## Evidence Strength
Practitioner consensus — taught and deployed in industry since 1965, and the boundary/both-sides test is sound logic; but there is no rigorous comparative evidence it beats other diagnosis methods, and its ranking steps inherit whatever weights and distinctions humans feed them.

## Source
Charles Kepner & Benjamin Tregoe, *The Rational Manager* (1965); Kepner-Tregoe methodology.
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) (MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns IS/IS-NOT boundary discrimination for selective deviations; 5 Whys traces causal chains but does not scope the deviation.
