# Pre-mortem & Counterfactual

## Core Concept
Before committing to a decision, imagine it has failed spectacularly. Work backward to identify what went wrong. Then develop counterfactuals: "if X had been different, would the outcome change?" This surfaces hidden risks and critical variables.

## Applicable Scenarios
✅ **Best for**
- Major decisions before commitment
- Project kickoff risk identification
- Investment evaluation

## Key Steps
1. Assume the plan has failed catastrophically (set the scene)
2. Each team member writes down reasons for failure independently
3. Share and cluster failure reasons
4. For each failure reason, assess: probability + impact + preventability
5. Develop mitigation plans for top risks
6. Create counterfactuals: "If we had [done differently], would [failure] still occur?"
7. Adjust the plan based on findings

## Inversion (folded entry)

The failure-rehearsal mechanism run in reverse: pre-mortem imagines the failure and works backward to its causes; inversion starts from the present and asks **"what would guarantee failure?"** — then avoids that list.

- Use when the plan has no precedent to premortem against (genuinely novel): imagined failure modes are speculative, but the guarantee-failure list is derivable from hard constraints (no users, no distribution, no cash, no retention)
- Use as the opening move of a Pre-mortem: the inversion list seeds step 2's independent failure reasons
- When NOT to invert alone: regulatory/safety domains where failure modes are already catalogued by others — start from the catalogue, not from imagination

**Admission verdict** (v0.1.6): standalone Inversion entries reviewed in external mental-model collections — folded here rather than built as a separate entry, because both are failure-rehearsal mechanisms and SKILL.md's combination rules bar near-synonym stacking. Escalate to a Build verdict only if a task appears that needs inversion without any premortem framing.

## Source
Gary Klein, *Performing a Project Premortem* (2007); Harvard Business Review.
Inversion absorbed with Fold verdict, 2026-10-01 — sources: cyperx84/claude-skills-mental-models (inversion.md), mattnowdev/thinking-partner (MIT).
