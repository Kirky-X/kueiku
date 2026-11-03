# Pre-mortem & Counterfactual

## Core Concept
Before committing to a decision, imagine it has failed spectacularly. Work backward to identify what went wrong. Then develop counterfactuals: "if X had been different, would the outcome change?" This surfaces hidden risks and critical variables.

## Applicable Scenarios
✅ **Best for**
- Major decisions before commitment
- Project kickoff risk identification
- Investment evaluation

⚠️ **When NOT to use**
- Reversible, cheap-to-undo decisions — rehearsing failure costs more than iterating; grade with **Reversibility Grading** first
- The team has already publicly committed and morale is invested — the premortem's license to criticize works before commitment, not after
- Novel one-shot bets with no precedent and no hard constraints — imagined failures are free-floating anxiety; inversion needs constraints, counterfactuals need a causal skeleton
- Live incidents and time-critical response — you need **OODA Loop** tempo, not a structured imagination exercise

## Key Steps
1. Assume the plan has failed catastrophically (set the scene)
2. Each team member writes down reasons for failure independently
3. Share and cluster failure reasons
4. For each failure reason, assess: probability + impact + preventability
5. Develop mitigation plans for top risks
6. Create counterfactuals: "If we had [done differently], would [failure] still occur?"
7. Adjust the plan based on findings

## Output Template

```
Premortem — "It is [future date]. The plan has failed catastrophically."
Failure reasons (written independently before any discussion, then clustered):
  1. [reason, specific enough to be falsifiable] — probability [H/M/L] × impact [H/M/L] × preventability [H/M/L]
  2. [reason] — ...
Top risk cluster: [the cluster scoring high on all three]
Mitigations: [risk → concrete prevention / early-warning tripwire / owner]
Counterfactuals: "If we had [done X differently], would [failure] still occur?" → [yes — structural / no — controllable]
Plan changes adopted: [what changes because of this exercise]
```

## Failure Modes
- Premortem as ritual: everyone lists clichés ("scope creep", "poor communication") and nothing changes → require failure reasons specific enough to be falsifiable, and close with plan changes, not just a risk list
- Unranked dumping: 40 reasons, no prioritization → score each on probability × impact × preventability and work only the top cluster
- Hindsight creep in counterfactuals: "we should have known" smuggles hindsight bias into a forward-looking exercise → keep counterfactuals conditional on information available at decision time
- Facilitator speaks first: the leader's stated failure reasons anchor the room → independent written reasons before any discussion; that is the Klein protocol's core mechanic

## Inversion (folded entry)

The failure-rehearsal mechanism run in reverse: pre-mortem imagines the failure and works backward to its causes; inversion starts from the present and asks **"what would guarantee failure?"** — then avoids that list.

- Use when the plan has no precedent to premortem against (genuinely novel): imagined failure modes are speculative, but the guarantee-failure list is derivable from hard constraints (no users, no distribution, no cash, no retention)
- Use as the opening move of a Pre-mortem: the inversion list seeds step 2's independent failure reasons
- When NOT to invert alone: regulatory/safety domains where failure modes are already catalogued by others — start from the catalogue, not from imagination

**Admission verdict** (v0.1.6): standalone Inversion entries reviewed in external mental-model collections — folded here rather than built as a separate entry, because both are failure-rehearsal mechanisms and SKILL.md's combination rules bar near-synonym stacking. Escalate to a Build verdict only if a task appears that needs inversion without any premortem framing.

## Evidence Strength
Mixed — prospective hindsight has real experimental support: imagining an event as already having occurred reliably increases the number and specificity of risks people generate, and Klein's premortem is built on that mechanism; but the strongest results are lab-rooted single-session effects, and field evidence that premortems change real project outcomes is thinner. The counterfactual half inherits hindsight-bias research — useful for surfacing critical variables, prone to "we should have known" readings.

## Source
Gary Klein, *Performing a Project Premortem* (2007); Harvard Business Review.
Inversion absorbed with Fold verdict, 2026-10-01 — sources: cyperx84/claude-skills-mental-models (inversion.md), mattnowdev/thinking-partner (MIT).
