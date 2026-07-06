# Invisible Perfection

## Core Philosophy

Internal craft quality determines external experience. Even the unseen areas must be polished.

Users only see the product's surface, but surface experience is supported by countless unseen internal components: code structure, data pipelines, error handling, logging standards, build processes. Once these "unseen" parts degrade, external experience inevitably deteriorates — more bugs, slower performance, slower iteration, difficulty adding new features.

> **Key Judgment**: Internal craft is not "icing on the cake" but "the foundation."
> A rotten foundation cannot support a tall building. But foundation polishing requires standards, automation, and sustained investment — it cannot rely on individual initiative.

---

## Applicable Scenarios

✅ **Best For**
- Code quality standard setting and enforcement
- Craft improvement of internal tools and infrastructure
- Building team craft culture
- Systematic technical debt management

⚠️ **Use With Caution**
- Urgent features before a delivery deadline (deliver first, polish later)
- One-off scripts/prototypes (not worth the craft investment)
- Early stages with severely limited resources (focus on core craft, don't pursue perfection everywhere)

---

## Execution Steps

### Step 1: Identify Internal Craft Points

Inventory internal craft points along the product chain:
- **Code layer**: Architecture clarity, module boundaries, naming conventions, test coverage
- **Data layer**: Data quality, pipeline stability, schema standards
- **Process layer**: CI/CD, code review, release process, monitoring and alerting
- **Documentation layer**: API documentation, architecture documentation, decision records

> Not all craft points are equally important. Prioritize by "impact on external experience."

### Step 2: Define Standards

Define quantifiable standards for each key craft point:
- **Code**: Cyclomatic complexity thresholds, minimum test coverage, lint rules
- **Data**: Latency upper bounds, error rate thresholds, schema compatibility
- **Process**: Required CI checks, code review requirements
- **Documentation**: Mandatory documentation for key APIs, mandatory recording of major decisions

> Standards must be machine-checkable. Standards relying on manual diligence will gradually fail.

### Step 3: Automate Checks

Convert standards into automated checks:
- CI integration: lint, tests, coverage checks
- Pre-commit hooks to intercept low-quality commits
- Monitoring dashboards displaying craft metric trends
- Regular reports on craft debt changes

> Standards without automation are the same as no standards.

### Step 4: Continuous Polishing

Establish a continuous polishing mechanism:
- Reserve craft debt repayment time each iteration (e.g., 20%)
- Craft debt visualization (tech debt kanban)
- ROI evaluation of craft improvements (avoid over-polishing)
- Craft culture continuity (onboarding training, code review culture)

> Continuous polishing ≠ infinite polishing. Each craft point has a "good enough" threshold — beyond that, diminishing returns set in.

---

## Output Template

```
Analysis Target: [Product/System]
Analysis Date: [Date]

Internal Craft Points Inventory:
  | Craft Point | Category | Impact on External Experience | Current Status | Priority |
  |-------------|----------|------------------------------|----------------|----------|
  | ...         | Code/Data/Process/Doc | High/Medium/Low | Good/Medium/Poor | P0/P1/P2 |

Craft Standard Definitions:
  1. [Craft Point] — Standard: [Quantifiable Metric] — Check Method: [Automation Tool]
  2. [...]

Automated Check Checklist:
  - [ ] CI Integration: [lint/test/coverage specific config]
  - [ ] Pre-commit Hook: [interception rules]
  - [ ] Monitoring Dashboard: [metrics and alert thresholds]
  - [ ] Regular Reports: [frequency and content]

Continuous Polishing Plan:
  - Per-iteration craft debt repayment time ratio: [X%]
  - Top 3 current craft debts: [...]
  - Next phase polishing focus: [...]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Polishing for the sake of polishing, not knowing when to stop amid diminishing returns | Set a "good enough" threshold for each craft point; stop when exceeded |
| Standards relying on manual diligence | Standards must be machine-checkable and CI-enforced |
| Only focusing on code, ignoring data/process/documentation | Inventory all four categories of craft points |
| Completely abandoning craft during urgent deliveries | Distinguish core craft (non-negotiable) from deferrable craft |
| Craft debt is unseen so it doesn't get repaid | Visualize craft debt; incorporate into iteration planning |
| New team members don't know the craft standards | Document standards + pass them on through code review |

---

## Relationship with Other Methodologies

- **Preceded by Focus as No**: After focusing, polish the retained features' craft
- **Preceded by Whole Widget**: In-house components need craft standards to ensure quality
- **Contrasted with Technology Meets Humanities**: Internal craft supports high scores in the humanities dimension
- **Followed by Engineering methodologies**: Specific craft practices can be found in the engineering category
