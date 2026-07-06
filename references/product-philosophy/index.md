# Product Philosophy

**Applicable Scenarios**: When making foundational judgments on product direction, architecture, and craft standards — not execution-level scheduling

| Methodology | One-Line Description | Best Scenario | Reference |
| --- | --- | --- | --- |
| **Focus as No** | Focus is not about saying "yes" but "no" — radical subtraction to lock in the minimal set | Product scope decisions, feature trade-offs, preventing product bloat | `focus-as-no.md` |
| **Whole Widget** | End-to-end responsibility, key decisions not outsourced — vertical integration architecture | Product architecture decisions, vertical integration vs. horizontal specialization | `whole-widget.md` |
| **Technology Meets Humanities** | Technology × Humanities × Business three-dimensional assessment — a single perspective is insufficient for great products | Product evaluation, design decisions, team composition | `technology-meets-humanities.md` |
| **Invisible Perfection** | Internal craft quality determines external experience — polish even the unseen areas | Code quality, internal tools, craft standard setting | `invisible-perfection.md` |

## Minimum Information Requirements per Methodology

- **Focus as No**: Current feature/requirement list + business goal priorities
- **Whole Widget**: Product key decision point inventory + outsourcing cost/benefit data for each component
- **Technology Meets Humanities**: Product technical metrics + user humanities sensitivity data + business model
- **Invisible Perfection**: Internal craft point inventory + existing quality standards + automation check capabilities

## Routing Trigger Signals

- "Too many features / product bloat / wanting to do everything" → Focus as No (primary)
- "Should this component be built in-house or outsourced/purchased?" → Whole Widget (primary)
- "Product evaluation only looking at technical metrics is insufficient / missing humanities perspective" → Technology Meets Humanities (primary)
- "Code quality / internal tools — should we spend time polishing?" → Invisible Perfection (primary)

## Common Combinations

- **Product scope decision**: Focus as No (lock in minimal set) → RICE (execution prioritization) → Invisible Perfection (craft standards)
- **Architecture decision**: Whole Widget (identify key decision points) → Technology Meets Humanities (three-dimensional assessment)
- **New product evaluation**: Technology Meets Humanities (three-dimensional assessment) → Focus as No (eliminate temptations)
