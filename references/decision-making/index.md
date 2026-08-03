# Decision Making

**When to use**: Need to make a defensible decision among multiple options

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **RICE Scoring** | Reach×Impact×Confidence÷Effort quantified prioritization | Product roadmap ranking, requirement prioritization | `rice.md` |
| **Eisenhower Matrix** | Importance×Urgency 4-quadrant time management | Personal/team task management, resource allocation | `eisenhower.md` |
| **OKR** | Objectives + Key Results goal decomposition system | Quarterly/annual goal setting, team alignment | `okr.md` |
| **Pre-mortem & Counterfactual** | Reverse-imagine failure scenarios, rehearse risks, identify key variables | Before major decisions, project kickoff, investment evaluation | `premortem-counterfactual.md` |
| **Decision Matrix** | Multi-option multi-criteria weighted scoring, quantifying choices | Technology selection, strategy selection, candidate evaluation | `decision-matrix.md` |
| **MoSCoW Method** | Must/Should/Could/Won't 4-level requirement scoping | Scope management, requirement classification, Sprint planning | `moscow.md` |
| **FMEA** | Severity×Occurrence×Detection ranking of failure risks | Product/process risk identification, quality engineering, safety-critical systems | `fmea.md` |
| **Death Filter** | "If this were the last decision" existential filter | Major life decisions, career choices, startup direction | `death-filter.md` |
| **Risk Matrix** | Probability×Impact 2-dimension quick risk assessment and ranking | Project kickoff risk screening, strategic planning risk scan, tech selection risk comparison | `risk-matrix.md` |

## Minimum Information Requirements per Methodology

- **RICE**: Requires option list + basic magnitude awareness
- **OKR**: Requires clear time period and responsible entity
- **Pre-mortem**: Requires an existing clear plan/decision
- **Decision Matrix**: Requires at least 3 alternatives + criteria list
- **MoSCoW**: Requires requirement list + stakeholder involvement
- **FMEA**: Requires component decomposition of system/process
- **Death Filter**: Requires major irreversible decision + candidate options (not for daily/urgent decisions)
- **Eisenhower Matrix**: Requires task list to classify (personal/team task management)
- **Risk Matrix**: Requires identified risk list + probability/impact scale definitions

## Routing Trigger Signals

- "Feature/requirement prioritization" → RICE Scoring (primary) ⚡ If evaluation dimensions need customization (not R/I/C/E) → use Decision Matrix; if need quick rough screening in 30 min → use ICE
- "Personal/team task management" → Eisenhower Matrix (primary)
- "Goal setting and tracking" → OKR (primary)
- "Risk rehearsal before major decision" → Pre-mortem & Counterfactual (primary)
- "Multi-option multi-criteria selection (custom evaluation dimensions)" → Decision Matrix (primary) ⚡ If evaluation dimensions are fixed as Reach/Impact/Confidence/Effort → use RICE
- "Requirement scoping / scope management" → MoSCoW Method (primary)
- "Systematic risk identification / failure mode analysis" → FMEA (primary)
- "Major life decision / career choice / startup direction (value-based decision)" → Death Filter (primary)
- "Quick risk assessment / risk ranking / risk panorama scan" → Risk Matrix (primary)

## Common Combinations

- **Major decision**: Socratic questioning (clarify assumptions) → Decision Matrix → Pre-mortem (risk review)
- **Requirement full lifecycle**: Kano (classify nature) → MoSCoW (scope) → RICE (prioritize)
- **Comprehensive risk assessment**: FMEA (systematic identification) → Pre-mortem (imaginative supplement) → Second-Order Thinking (chain effects)
- **Major life/startup decision**: Death Filter (filter true inclination) → Pre-mortem (rehearse selected direction risks) → Second-Order Thinking (long-term effects)
- **Project kickoff risk assessment**: Pre-mortem (identify risks) → Risk Matrix (quantify and rank) → FMEA (deep analysis of high-risk items)
- **Technology selection risk**: Decision Matrix (option comparison) → Risk Matrix (risk ranking) → Second-Order Thinking (chain effects)

## Similar Methodology Disambiguation Decision Tree

When user intent is ambiguous between these methodologies, disambiguate per the decision tree:

```
"Multi-option evaluation and ranking"
  ├─ Evaluation dimensions fixed as Reach/Impact/Confidence/Effort?
  │   └─ Yes → RICE Scoring
  ├─ Evaluation dimensions need customization? (e.g. tech selection: performance/cost/risk)
  │   └─ Yes → Decision Matrix
  └─ Need quick rough screening in 30 min, no precise quantification needed?
      └─ Yes → ICE Framework

"Task/requirement ranking"
  ├─ Personal/team daily task management?
  │   └─ Yes → Eisenhower Matrix
  ├─ Product feature/requirement prioritization?
  │   └─ Yes → RICE Scoring
  └─ Requirement scope trimming (do / don't do)?
      └─ Yes → MoSCoW Method

"Risk assessment"
  ├─ Existing clear plan, need to rehearse failure scenarios?
  │   └─ Yes → Pre-mortem
  ├─ Need systematic failure mode identification?
  │   └─ Yes → FMEA
  └─ Need quick risk panorama scan and ranking?
      └─ Yes → Risk Matrix
```

## Methodology Mutual Exclusion and Ordering Constraints

| Constraint pair | Rule | Reason |
| --- | --- | --- |
| RICE ↔ ICE | **ICE for rough screening → RICE for fine ranking**, don't use in parallel | ICE is a simplified version of RICE; parallel use produces redundant output |
| RICE vs Decision Matrix | **Choose by evaluation dimensions**: fixed R/I/C/E→RICE; custom dimensions→Decision Matrix | Core difference is whether dimensions are fixed; input structure is similar but purposes differ |
| FMEA → Pre-mortem | **FMEA before Pre-mortem** (comprehensive risk assessment scenario) | FMEA systematically identifies; Pre-mortem supplements imaginatively |
