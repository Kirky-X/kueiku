# Problem Diagnosis

**When to use**: A known problem exists; need to find the root cause or redefine the problem

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **5 Whys** | Ask "why" 5 times consecutively to pierce through symptoms to root cause | Production incidents, business metric decline, process errors | `five-whys.md` |
| **Fishbone / Ishikawa** | Fishbone diagram: systematically listing multi-dimensional causes | Quality issues, multi-factor influence, team collaboration analysis | `fishbone.md` |
| **Issue Tree** | MECE decomposition into sub-questions + hypothesis-driven evidence hunt from a Day-1 answer | Large vague problems, team-split workstreams, constrained analysis budget | `issue-tree.md` |
| **Why Tree** | Multi-branch causal tree; every node tagged with evidence kind + confidence + citation, then adversarially refuted | High-stakes root-cause analysis, auditable diagnoses, merged evidence of unequal reliability | `why-tree.md` |
| **IS/IS-NOT Difference Analysis (Kepner-Tregoe)** | Contrast where the problem occurs vs where it plausibly could but doesn't; boundary discriminates causes; MUST/WANT weighting for the fix choice | Selective defects with comparable non-cases, option choice with non-negotiables | `kepner-tregoe.md` |
| **First Principles** | Break analogies, re-derive from foundational axioms | Innovative design, disrupting existing solutions, breaking mental models | `first-principles.md` |
| **Pareto Analysis** | Identify the 20% key factors causing 80% of results, focus on priorities | Resource allocation, problem prioritization, key driver identification | `pareto.md` |

## Minimum Information Requirements per Methodology

- **5 Whys / Fishbone**: Requires a quantifiable or observable specific problem statement
- **Issue Tree**: Requires a problem expressible as a decomposable question + enough domain knowledge to attempt a Day-1 answer
- **Why Tree**: Requires a measurable deviation statement + citable evidence sources (data queries, stakeholders, documents)
- **IS/IS-NOT Difference Analysis (Kepner-Tregoe)**: Requires a deviation with comparable non-cases (where it doesn't occur); Decision Analysis mode additionally requires alternatives + explicit non-negotiables
- **First Principles**: Clear assumption or analogy to disrupt
- **Pareto Analysis**: Requires quantifiable impact metrics + candidate list

## Routing Trigger Signals

- "Find root cause" / "why did this happen" → 5 Whys (primary)
- "Disruptive thinking" / "break assumptions" → First Principles (primary)
- "80/20 focus identification" / "resource focus" → Pareto Analysis (primary)
- "Multi-factor causation analysis" / "fishbone diagram" → Fishbone / Ishikawa (primary)
- "Decompose complex problem" / "problem tree" / "hypothesis-driven analysis" / "Day-1 answer" → Issue Tree (primary)
- "Evidence-graded diagnosis" / "stress-test the diagnosis" / "which claims can we trust" → Why Tree (primary)
- "Only some users/instances affected" / "where does it NOT occur" / "IS vs IS-NOT" / "MUST-WANT screening" → IS/IS-NOT Difference Analysis (primary)

## Triage — before picking a framework

The keyword routing above assumes the problem type is already known. When it is not, triage first — three questions whose answers pick the branch. Answer them from evidence the user provides; do not guess:

| # | Question | Yes → | No → |
| --- | --- | --- | --- |
| 1 | Do multiple independent cause families look plausible from the start (people / machine / method / measurement all candidates)? | Multi-factor branch: Fishbone → Pareto | next question |
| 2 | Is there a comparable non-case (a similar unit without the problem)? | Selective-defect branch: IS/IS-NOT Difference Analysis | next question |
| 3 | Is the causal chain short and directly observable end-to-end? | Chain-traceable branch: 5 Whys | Chain not directly observable: recurring/oscillating behavior → Systems Thinking (Structured Thinking); deep-but-gradable evidence → Why Tree |

Triage typically yields a working root-cause label — pricing misalignment, churn spike, weak PMF, broken GTM activation, process decay — to carry into whichever branch or combination fits. The label names the problem family; the rows above name the method chains.

**First-response contract**: until comparable component-level evidence is in hand, every conclusion is labeled **"cause not established"** — name the candidate causes, then name the evidence that would discriminate between them. Report it with stop_reason `degraded(L2)` so a paused diagnosis is never structurally indistinguishable from a finished one. Premature attribution is the failure this contract exists to prevent. (This specializes the SKILL.md L3 degradation — "ask 1-3 critical questions" — to diagnosis tasks.)

## Common Combinations

- **Structured takedown of a big vague problem**: Issue Tree (decompose into sub-questions) → Why Tree (evidence-grade the live branches) → 5 Whys (chain-trace the confirmed branch to its actionable root)
  - Step outputs: Issue Tree → MECE sub-question list with Day-1 hypotheses; Why Tree → evidence-tagged branch verdicts (supports / refutes / unknown); 5 Whys → causal chain ending in an actionable root cause
  - Branch: a branch surviving evidence grading goes straight to 5 Whys; branches still "unknown" get a data-collection task, not more analysis
  - Final deliverable: root-cause statement + discriminating-evidence log + fix options ranked by impact — synthesized, not stapled
- **Selective defect diagnosis**: Fishbone (diverge candidate causes) → IS/IS-NOT (keep only candidates explaining both sides of the boundary) → Pareto Analysis (rank fixes by measured impact)
  - Step outputs: Fishbone → cause-family map; IS/IS-NOT → shortlist of boundary-consistent causes with the discriminating observation; Pareto → ranked fix list with measured impact shares
  - Branch: a cause surviving the boundary test but unmeasurable → treat as "cause not established" and instrument first, do not rank on guesses
  - Final deliverable: verified cause + ranked corrective actions with expected impact
- **Diagnose then fix**: IS/IS-NOT (verify the cause) → RICE (prioritize corrective actions) — run sequentially; do not mix causal evidence with option scores
