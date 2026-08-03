# Product Philosophy

**When to use**: Need foundational judgment on product direction, architecture, and craft standards — not execution-level scheduling

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Focus as No** | Focus is not saying "yes", it's saying "no"; radical subtraction to lock the minimum set | Product scope decisions, feature trade-offs, preventing product bloat | `focus-as-no.md` |
| **Whole Widget** | End-to-end ownership; vertical integration for critical decisions not outsourced | Product architecture decisions, vertical integration vs horizontal division of labor | `whole-widget.md` |
| **Technology Meets Humanities** | Technology × Humanities × Business 3-dimension assessment; a single perspective is insufficient for good products | Product evaluation, design decisions, team building | `technology-meets-humanities.md` |
| **Invisible Perfection** | Internal craft quality determines external experience; polish even the unseen parts | Code quality, internal tools, craft standard setting | `invisible-perfection.md` |

## Minimum Information Requirements per Methodology

- **Focus as No**: Current feature/requirement list + business priority objectives
- **Whole Widget**: Product critical decision point list + outsourcing cost/benefit data per stage
- **Technology Meets Humanities**: Product technical metrics + user humanities perception data + business model
- **Invisible Perfection**: Internal craft point list + existing quality standards + automated checking capability

## Routing Trigger Signals

- "Too many features / product bloat / trying to do everything" → Focus as No (primary)
- "Should this be built in-house or outsourced / buy a solution" → Whole Widget (primary)
- "Product evaluation: technical metrics alone are insufficient / missing humanities perspective" → Technology Meets Humanities (primary)
- "Code quality / internal tools: should we invest in polishing" → Invisible Perfection (primary)

## Common Combinations

- **Product scope decision**: Focus as No (lock minimum set) → RICE (execution ranking) → Invisible Perfection (craft standards)
- **Architecture decision**: Whole Widget (identify critical decision points) → Technology Meets Humanities (3-dimension assessment)
- **New product evaluation**: Technology Meets Humanities (3-dimension assessment) → Focus as No (eliminate temptation items)
