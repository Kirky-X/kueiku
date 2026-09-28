# Why Tree — Evidence-Graded Causal Tree

## Core Concept
A multi-branch causal tree where **every node carries three tags: evidence kind, confidence (Strong/Mod/Weak), and citation** — the kind says *what you are trusting* before how much. Unlike 5 Whys (one chain), it maps the causal web and grades each link's support.

## Evidence Kinds (seven)
**Measured** (hard number, n + window) · **Instance** (n=1-few, not a rate) · **External** (named third-party fact) · **Claim** (said, not verified) · **Inference** (logic on measured premises) · **Hypothesis** (untested; settling test nameable) · **Framing** (a lens — the apex is always one).

A number is not yet a fact. Measured carries a validation state: `raw` (pipeline unchecked — caps at Mod, cannot support the conclusion) → `validated` (denominator, definition, window, attribution, survivorship checked) → `triangulated` (two independent pipelines agree). `contested` = both values stay visible; the node cannot act as fact.

## Applicable Scenarios
✅ High-stakes "why" questions · auditable diagnoses · merged unequal-reliability evidence
⚠️ **When NOT to use**: quick single-chain incidents (5 Whys) · low-stakes questions with no audit need — the tag ledger costs more than the answer · lightweight contexts — degrade to the calling protocol's **fact / inference / assumption** tagging

## Key Steps
1. **Frame the apex**: one observed gap, stated measurably.
2. **Fan branches backward**; tag every node.
3. **Validate Measured sources** once each; record the state.
4. **Adversarial pass**: try to kill each load-bearing branch (data-otherwise / broken mechanism / mis-attribution / dirty pipeline); refuted stay visible with killing evidence.
5. **Converge**: load-bearing nodes still Hypothesis → headline is "where to look"; ship the cheapest test.

## Output Template

```
Apex: [observed gap]
├─ [cause] — Inference/Mod — [cite]
│   ├─ [support] — Measured/Strong, validated — "42% (n=310, Mar)"
│   └─ [support] — Hypothesis — test: [...]
├─ [cause] — REFUTED — killed by: [evidence]
└─ Contested: [A/src] vs [B/src] → reconcile: [check]
Census: [x% measured · y% hypothesis] → cheapest test: [...]
```

## Failure Modes
- **Green-chip fiction**: unchecked-pipeline numbers as facts.
- **Ritual tags**: every node labeled, none load-bearing checked — the ledger becomes decoration → tag only what the conclusion leans on, and validate those.
- **Skipped adversarial pass**: load-bearing branches never attacked (data-otherwise / broken mechanism / mis-attribution) → run step 4 before converging; refuted branches stay visible with their killing evidence.
- **Measurable-in-hand blindness**: one query would settle it — run it now.
- **Pruning the corpse**: deleting refuted branches and their lesson.

## Evidence Strength
Practitioner consensus on the discipline (grade evidence before trusting it; `raw → validated → triangulated` mirrors standard data-quality practice), but the seven-kind taxonomy is an authored framework, not a validated instrument — node grades are only as honest as whoever tags them, and the tree makes no causal claim its citations don't carry.

## Source
Goldratt CRT lineage; the evidence-grading discipline extends it.
Provenance: evidence grading absorbed from [systems-thinking-skills](https://github.com/BayramAnnakov/systems-thinking-skills) (MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns evidence-graded multi-branch causal mapping; 5 Whys is a single ungraded chain.
