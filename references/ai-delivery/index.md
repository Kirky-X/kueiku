# AI Delivery

**When to use**: AI-era shipping artifacts standards, doc-code drift detection

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Shipping Artifacts** | Core 5 + Conditional 4 documents + Anti-PRD rule | AI project delivery standards | `shipping-artifacts.md` |
| **Intended vs Implemented** | Documented intent ↔ cited code cross-reference + boundary mismatch | Doc-code drift detection | `intended-vs-implemented.md` |
| **LLM Output Evaluation** | Golden set + rubric scorers + judge-bias controls + regression gate | Did my prompt/model change make output better; AI-feature regression gating | `llm-output-evals.md` |

## Minimum Information Requirements per Methodology

- **Shipping Artifacts**: Requires project scope + documentation version management
- **Intended vs Implemented**: Requires Design Doc + code reference relationships
- **LLM Output Evaluation**: Requires a defined task + output contract + a golden set of 20-50 real cases (composition over size)

## Routing Trigger Signals

- "AI project delivery standards" → Shipping Artifacts (primary)
- "Doc-code drift detection" → Intended vs Implemented (primary)
- "Did my prompt change make it better / compare two models on my task / stop AI regressions / build an eval set / LLM-as-a-judge" → LLM Output Evaluation (primary) ⚡ If measuring business metrics with real users → use A/B Test Analysis (Data Analysis); if reviewing the agent's code → diting; if the output is code and the question is security → use Security by Design (Engineering)

## Common Combinations

- **AI project delivery**: Shipping Artifacts (define the artifact set) → Intended vs Implemented (keep docs and cited code aligned as the project evolves)
- **Prompt/model change lifecycle**: LLM Output Evaluation (fixed-set gate before shipping) → Intended vs Implemented (update the docs the change invalidates)
