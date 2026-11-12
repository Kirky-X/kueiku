# Adversarial Review Panel

## Core Concept
Review a high-stakes artifact (analysis memo, plan, postmortem, methodology doc) with dedicated opposing roles instead of one generalist reader: an **Attacker** mandated to find faults across categories (instructed to over-report), a **Fact-Checker** mandated to recompute every number and verify every claim, a **Risk Reviewer** mandated to hunt omissions, gameability, and second-order effects — then a **Judge** merges, dedupes, and rules each finding confirmed or rejected against the artifact. The mechanism is role specialization: a generalist scans "what is written"; specialized mandates also scan "what is missing and how this can be gamed" — the blind spots a solo pass systematically drops (local experiment: both solo misses were omission-type defects; the risk-reviewer role caught them all three times).

## Applicable Scenarios
✅ **Best for**
- Irreversible or high-stakes artifacts before commitment: strategy memos, investment theses, public claims, published methodologies
- After a solo review already ran and the stakes justify a deeper sweep
- Reviewing decision methods themselves — a method's failure modes are second-order (gameability, institutional side-effects) and rarely surface to a single reader

⚠️ **When NOT to use**
- Small, reversible artifacts — solo review at ~1/4 the cost is the right default
- Claims mechanically checkable — compute them (python), a panel adds nothing
- When the solo baseline is unknown — run a solo pass first; it is also the control that tells you whether the panel added anything

## Key Steps
1. Freeze the artifact; write three non-overlapping mandates (attacker: fault-finding, over-report on purpose; fact-checker: recompute + verify every claim; risk reviewer: omissions, gameability, second-order effects)
2. Run the three reviews independently — no cross-visibility before the judge stage (interaction before independent judgment correlates errors and manufactures false consensus)
3. Judge: dedupe, then rule each finding confirmed/rejected with a one-line reason checked against the artifact; the rejected count is the honesty signal
4. Triage: every confirmed finding ends in a fix, a mitigation with owner, or a documented accepted-risk — no "further study" exits
5. Re-review any patch: the fix is a new artifact with its own attack surface

## Output Template

```
Artifact: [one line] — result: [n] findings confirmed, [m] rejected

| # | Role          | Finding (position + substance)                          | Ruling                    | Action (fix / owner / accepted-risk) |
| --- | ----------- | ------------------------------------------------------- | ------------------------- | ------------------------------------ |
| 1 | Attacker      | [TAM arithmetic: 3000万×$600=180亿, memo says 210亿]     | Confirmed                 | [fix §1]                             |
| 2 | Fact-checker  | [claim X contradicts source Y]                          | Rejected: [one-line why]  | —                                    |
| 3 | Risk reviewer | [no risk section; free-alternative threat undiscussed]  | Confirmed                 | [owner + mitigation]                 |

Cost gate: solo review first; escalate to the panel only for irreversible/high-stakes artifacts (~4-5× solo cost)
```

## Failure Modes
- Role drift: mandates bleed into each other until you have three copies of the same generalist → keep mandates non-overlapping and one-directed (attacker over-reports, checker recomputes, risk reviewer hunts the absent)
- Judge rubber-stamp: merging without rulings launders false positives into the final list → one-line ruling per finding; a judge that rejects nothing is not judging
- Correlated independence theater: same model + near-identical prompts agree because they share blind spots, not because they are right → make mandates structurally different; treat unanimous confirmation of ambiguous items as "unverified", not "validated"
- Cost creep on trivia: panel on a low-stakes doc spends 4-5× for no recall gain when solo is already ceiling → gate on irreversibility, not on availability
- Compute confound: attributing panel gains to "adversarial structure" when they partly come from 4× compute + specialization → before escalating, compare against a solo reviewer holding an explicit omission-hunting mandate; adopt the panel only if it still wins

## Evidence Strength
Mixed-to-promising. Local controlled experiment (2026-11-12, defect-injection artifact with 10 seeded defects × 3 runs per arm): panel recall 10/10/10 (zero variance) vs solo generalist 10/9/9 (median 9/10, both misses omission-type); real-artifact round (a methodology entry): solo 13 findings vs panel 79, with second-order defects (score gaming, Goodhart-vulnerable metrics, institutional side-effects) almost exclusively from specialized roles. Known limitations: recall judged by a single human; judge step skipped in one of three panel runs; panel = 3 specialized roles + ~4× compute vs 1 generalist, so role specialization and compute are confounded; real-artifact round run once. Literature: devil's advocacy and dialectical inquiry show controlled-experiment gains in decision quality (Schwenk 1990; Schweiger, Sandberg & Ragan 1986); multi-agent debate improves factuality on reasoning tasks (Du et al. 2023); cheap-talk results (Crawford–Sobel) warn that unanimous agreement without independence carries no information.

## Source
Mason (1969) dialectical inquiry; Cosier & Schwenk devil's advocacy; Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate" (2023); local experiment log 2026-11-12/13 (defect-injection + real-artifact rounds). Admission verdict: **Build** (2026-11-13) — adversarial review of artifacts via specialized roles + judge was absent: Strategy Red Team stress-tests a strategy thesis before commitment, not a document's factual and structural integrity; this entry covers the artifact-review layer and defers strategy stress-testing to Strategy Red Team.
