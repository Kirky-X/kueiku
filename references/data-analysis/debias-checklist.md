# Cognitive & Statistical Bias Checklist

## Core Concept
A pre-flight checklist for any data analysis, organized by the analysis lifecycle: **Design** (what to measure, on whom) → **Collection** (how reality got recorded) → **Interpretation** (what the numbers mean) → **Reporting** (what gets decided). Each entry names one bias, the signal that it may be active, and one concrete check action. The unit of value is not knowing the name — it is catching, at a specific stage, the flaw that would most cheaply invalidate the conclusion if caught now and most expensively if caught after the decision.

## Applicable Scenarios
✅ **Best for**
- Reviewing an analysis (yours or someone else's) before acting on it
- Designing metrics, dashboards, or experiments — choosing what to measure and how
- Post-mortems on a wrong decision: locating which lifecycle stage let the flaw through

⚠️ **When NOT to use**
- As rhetoric to dismiss inconvenient findings — name the specific bias and run its check, or the checklist itself becomes a confirmation-bias instrument
- Exhaustively on trivial reads — full checklist for consequential decisions; on quick reads, check the one stage you are least sure of

## Key Steps

### Stage 1 — Design (what to measure, on whom)

1. **Survivorship bias** — signal: the dataset contains only winners (current customers, surviving funds, live products); the churned, exited, and failed are structurally missing → check: state which population is invisible in this data; if failed units cannot appear, restate conclusions as conditional on survival, and in retention reads confirm cohorts include churned users (`cohort-analysis.md`).
2. **Selection bias** — signal: the sample arrived through a channel correlated with the outcome (opt-in surveys, one platform's users, volunteers) → check: write down the sampling mechanism; if it plausibly correlates with the outcome, treat between-group comparisons as confounded by unmeasured differences.
3. **Perverse incentive (Cobra Effect)** — signal: the metric doubles as someone's target, bonus, or OKR → check: ask how a rational agent maximizes this metric while defeating its purpose; if a gaming path exists, pair the metric with a counter-metric that the gaming would hurt.

### Stage 2 — Collection (how reality got recorded)

4. **Observer effect** — signal: subjects know they are measured, or measurement requires intervention (surveys, instrumented builds, shadowed support queues) → check: compare measured behavior against an unobserved baseline or a pre-announcement trend; assume reported behavior ≠ natural behavior until shown otherwise.

### Stage 3 — Interpretation (what the numbers mean)

5. **Data dredging (p-hacking)** — signal: many metrics, subsets, or cutoffs were tried and only the "significant" one is reported; the hypothesis was stated after seeing the result → check: count the tests actually run and apply multiplicity correction (`ab-test-analysis.md`); require out-of-sample or pre-registered confirmation for findings nobody predicted.
6. **Simpson's paradox** — signal: an aggregate trend reverses inside subgroups, or the groups differ both in size and in base rates → check: recompute the comparison within natural segments; if aggregate and segmented answers disagree, report both and name the weighting that produces the difference.
7. **Base-rate neglect** — signal: a result is judged by its hit rate alone ("the test is 90% accurate", "the signal fired") without asking how rare the target event is → check: start from the prior probability and update via the likelihood ratio (`decision-making/probabilistic-reasoning.md`); for rare events a 90%-accurate indicator is usually wrong when it fires.
8. **Gambler's fallacy** — signal: short-run history is expected to "correct" itself ("failed three times, so it's due", "the streak must end") → check: ask whether the trials are actually dependent; for independent trials the past changes nothing — recompute from base rates, not from the recent sequence.

### Stage 4 — Reporting (what gets decided)

9. **Confirmation bias** — signal: the write-up contains only evidence for the favored conclusion; null results and disconfirming cuts are absent → check: require a "What would change my mind" section carrying the strongest counter-evidence found; a report without one is advocacy, not analysis.

## Output Template
```
Bias review: [analysis / metric / decision]
Per bias: [pass | flagged → check run + what it showed]
Blocked by: [failed checks that must be fixed before acting]
Verdict: proceed | fix first (which stage) | redesign measurement
```

## Failure Modes
- Checklist theater: boxes ticked without running the checks → a "pass" requires written evidence per flagged item, not a Yes column
- Bias name-calling: "that's just survivorship bias" as a debate move → checks, not labels, decide; no check run, no finding
- Uniform depth: running all nine checks on a dashboard tweak → match review depth to decision stakes, not to checklist length

## Evidence Strength
Mixed — the individual biases are well documented in the judgment-and-decision-making literature (selection and survivorship effects empirically robust; Simpson's paradox mathematically demonstrable; multiplicity correction standard statistics), while the lifecycle grouping and the specific check actions are kueiku's practitioner synthesis, not a validated instrument.

## Source
Heuristics-and-biases research program (Tversky & Kahneman); Geckoboard's statistical fallacies collection.
Provenance: bias coverage absorbed from [awesome-concepts](https://github.com/lukasz-madon/awesome-concepts) README Fallacies section (CC0 1.0 license) and [knowledge-skills](https://github.com/deciqAI/knowledge-skills) `logical-fallacies` / `sunk-cost-fallacy` / `narrative-fallacy` (MIT license); lifecycle structure, trigger signals, and check actions authored for kueiku, absorbed 2026-09.
Admission: Build (new entry) — owns stage-by-stage bias checking across the analysis lifecycle; existing data-analysis entries assume unbiased measurement.
