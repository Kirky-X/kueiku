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

## Common Combinations

- **Structured takedown of a big vague problem**: Issue Tree (decompose into sub-questions) → Why Tree (evidence-grade the live branches) → 5 Whys (chain-trace the confirmed branch to its actionable root)
- **Selective defect diagnosis**: Fishbone (diverge candidate causes) → IS/IS-NOT (keep only candidates explaining both sides of the boundary) → Pareto Analysis (rank fixes by measured impact)
- **Diagnose then fix**: IS/IS-NOT (verify the cause) → RICE (prioritize corrective actions) — run sequentially; do not mix causal evidence with option scores
