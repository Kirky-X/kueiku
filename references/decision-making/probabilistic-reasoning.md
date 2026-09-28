# Probabilistic Reasoning

## Core Concept
State beliefs as numbers and ranges, not vibes. Anchor on a reference-class base rate, update with an explicit likelihood ratio, and bound unmeasured quantities by order of magnitude — never invent false precision. Within this category, this card owns the **estimate-and-update** step: `risk-matrix.md` grades identified risks qualitatively, `decision-matrix.md` weighs options against criteria.

## Applicable Scenarios
✅ **Best for**
- Timeline, effort, or outcome forecasts where the true value is uncertain
- Risk sizing for a change, migration, launch, or bet
- Any moment you are about to state a confident single number you cannot actually know
- New evidence has arrived and a prior estimate should move

⚠️ **When NOT to use**
- The quantity is measurable or look-up-able — measure or look it up
- The decision is invariant across the whole plausible range — skip the estimate and act
- No real reference class exists — label the number a guess, not a calibrated forecast
- A binary gate plus one decisive observation already settles it — do not pad with ceremony

## Key Steps
1. **Define a checkable claim**: outcome + timeframe + unit. "Auth p95 latency under 300 ms within 2 weeks", not "performance will likely improve"
2. **Convert vague words to numbers**: declare a fixed mapping before estimating (e.g. "likely" ≈ 65–80%) so the same word means the same probability across the analysis
3. **Anchor the prior on a reference class**: what base rate do comparable cases show? Pull the prior toward it unless you can write a concrete reason for deviating. Then state the strongest evidence-based case that your prior is wrong, and revise if that countercase survives
4. **Express a range, not a point**: give at least one confidence interval (50% and 80% preferred); assume overconfidence and widen intervals when the outside view is thin
5. **Update with a likelihood ratio** when evidence arrives: LR = P(E|H) / P(E|¬H); LR > 1 supports H, LR ≈ 1 is noise, LR < 1 undermines H. Posterior odds = prior odds × LR — multiply even when LR < 1. Yesterday's posterior is today's prior for the next piece of evidence. For rare events, start from the base rate: one vivid positive still leaves most of the mass on false alarms
6. **Bound unmeasured quantities by magnitude**: decompose into factors, bound each factor with a range, multiply, and report "~X within 3–5×" — never report precision the inputs cannot support
7. **Stop** when the decision is stable across the remaining range, or the next update would need evidence you do not have

## Output Template

```
Claim: [checkable statement + timeframe + unit]
Prior: [reference-class base rate + deviation reason] → p = …
Range: 50% CI [a, b]; 80% CI [c, d]
Updates: [evidence → LR → new p] (one row per piece of evidence)
Bounds: [unmeasured factors → "~X within N×"]
Decision implication: what changes at the low vs high end of the range
```

## Two High-Frequency Traps
- **Base-rate neglect**: treating a rare event as probable because the evidence "looks like" it. Example: 0.1% prevalence with a 99:1 likelihood ratio still yields only a ~9% posterior after a positive test — anchor the prior before reading the evidence
- **Prosecutor's fallacy**: reading P(E|H) ("the evidence matches the hypothesis") as P(H|E) ("the hypothesis is true given the evidence"). Fix: you need both P(E|H) and P(E|¬H); without the false-positive rate you have half the story

## Failure Modes
- Three significant figures on a 5×-uncertain product → report magnitudes honestly instead
- An invented reference class → the output is a guess; label it as one
- The number does not move when new evidence arrives (or moves without an LR) → recompute rather than defend

## Boundaries with Adjacent Methodologies
- `risk-matrix.md` — qualitative Probability × Impact grading of an identified risk list; no calibrated updating
- `decision-matrix.md` — weighted scoring among options once criteria are fixed
- **Probabilistic Reasoning** — produces and revises the probability estimates those tools consume
- Pairs with `data-analysis/debias-checklist.md` (base-rate neglect and confirmation bias entries)

## Script Integration Note
The quantitative core (odds conversion, LR multiplication, posterior computation) is deliberately left as card guidance here; a `scripts/` helper for prior-odds → LR → posterior arithmetic is a natural future extension.

## Evidence Strength
Strong for the arithmetic — Bayes' theorem is formal mathematics and the base-rate/prosecutor's-fallacy errors are experimentally documented; the calibration layer (word→number mappings, interval widening heuristics) rests on forecasting research and convention, and interval quality degrades for novel one-off events.

## Source
Bayes' theorem (posterior odds = prior odds × likelihood ratio) combined with forecasting-calibration practice (reference-class forecasting, stated confidence intervals, word-to-number mappings).
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) `thinking-probabilistic` and [knowledge-skills](https://github.com/deciqAI/knowledge-skills) `bayesian-reasoning` (both MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns the estimate-and-update step (numeric belief revision); risk-matrix grades identified risks only qualitatively.
