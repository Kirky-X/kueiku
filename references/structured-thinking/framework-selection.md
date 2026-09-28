# Framework Selection

## Core Concept
Meta-methodology for choosing the right framework — and the gate that keeps frameworks from becoming goals. 5 principles + a weighted fitness scorecard with an explicit NONE default: a framework is used only when it clears the bar; otherwise answer directly without one.

## Applicable Scenarios
✅ **Best for**
- Meta-decision when choosing frameworks
- Avoiding framework misuse
- Team framework alignment

⚠️ **When NOT to use**
- The choice is obvious and uncontroversial — scoring adds ceremony, not insight
- The user explicitly named the framework they want; honor it and note risks instead of re-scoring
- Only one realistic candidate exists — apply the 5 principles as a one-sentence check instead of a full scorecard

## Key Steps
1. State the core question clearly
2. List candidate frameworks
3. For each, apply the 5 principles:
   - Can it directly answer the core question?
   - Do we have enough information to use it?
   - Will its output be actionable?
   - Is the effort proportional to the decision's importance?
   - Can it be combined with other frameworks?
4. Score every surviving candidate on the fitness scorecard below
5. Use the top framework only if it clears the bar; otherwise return NONE and answer directly

## Fitness Scorecard — the gate

Score each candidate 1–5 per criterion, then compute the weighted total:

| Criterion | Weight | 1 looks like | 5 looks like |
| --- | --- | --- | --- |
| Task alignment | 30% | Answers an adjacent question | Directly answers the core question |
| Input readiness | 20% | Core data missing | All required inputs at hand or cheap to get |
| Execution competence | 20% | Needs expertise or data nobody here has | Agent and user can execute it faithfully |
| Time cost | 15% | Effort outstrips the decision's stakes | Proportional effort |
| Audience fit | 15% | Output unusable for its audience | Output immediately usable by them |

**The bar**: task alignment ≥ 4 AND weighted total ≥ 3.5. If the top candidate's weighted total falls below 3.5, the answer is NONE — answer the user's question directly and state why no framework was used. Failing the bar never means "run it anyway with caveats"; a marginal framework produces confident-looking but unfounded output.

**Tie-break**: when the top two candidates sit within 0.25 points, prefer the one that needs fewer inputs and less execution time; if still tied, prefer NONE (or the user's explicit pick) over an arbitrary winner.

**Routing output format**: a prioritized decision, not a single pick — state the selected framework, the backup, and explicitly which candidates to skip and why (near-synonyms, missing inputs, no complementary role).

## Abandonment Signals — stop and re-route mid-execution

- Forcing inputs into slots just to keep the framework alive
- The framework steers attention away from factors you know matter
- No incremental insight after honest effort (~15 minutes for a quick scan)
- You picked it by habit ("this kind of task always gets SWOT") — discard the habitual pick and re-score openly

On any signal: stop, explain what was completed and why the framework fails, re-select once per task (the replacement must clear the scorecard); if the replacement fails too, return NONE and answer from the evidence gathered so far.

## Failure Modes
- Scoring theater: inventing justifying scores for an already-made choice → write the evidence next to each score before totalling
- Bar-lowering under momentum: rounding a 3.4 up to 3.5 → the gate only works if NONE is a real, cost-free option
- Gate-skipping for familiar frameworks: habit picks skip scoring entirely → habitual picks get scored like any other candidate

## Evidence Strength
Mechanism-level, not empirical: no controlled studies show that this specific weighted bar improves decision quality. Its value is decision hygiene — it makes "no framework" a legitimate, explicit outcome instead of a failure state. The weights are defaults, not calibrated constants; adjust them per task and disclose the adjustment.

## Output Template

```
Core question: [one sentence]

Candidates (1-5 per criterion; weights: alignment 30% / readiness 20% / competence 20% / cost 15% / audience 15%):
  [Framework A]  alignment 5  readiness 4  competence 4  cost 4  audience 4  → weighted 4.30 ✅ clears bar
  [Framework B]  alignment 3  readiness 4  competence 3  cost 3  audience 4  → weighted 3.35 ❌ below bar

Decision: use [Framework A] (primary), [backup if any]; skip [B, C] — [near-synonym of A / missing inputs / no complementary role]
If NONE: answer directly. Why no framework: [top candidate + its failing criterion]
```

## Source
Kueiku skill methodology; meta-framework design.
