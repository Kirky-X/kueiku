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
| **Reversibility Grading** | Type 2/1.5/1 undo-cost classification matching analysis depth to how reversible a decision is | Deciding how much process a choice deserves; high-lock-in vs low-blast-radius calls | `reversibility.md` |
| **OODA Loop** | Observe→Orient→Decide→Act cycling on ~70% confidence for reversible moves | In-flight incidents, moving-target debugging, decisions under a still-moving situation | `ooda-loop.md` |
| **Probabilistic Reasoning** | Base-rate priors, ranges, likelihood-ratio updates for uncertain quantities | Forecasts, risk sizing, any confident single number you cannot actually know | `probabilistic-reasoning.md` |
| **Principled Negotiation** | Interests-not-positions bargaining with BATNA-derived walk-away power and objective criteria | Salary/vendor/partnership deals, resource disputes, multi-round agreements where the relationship survives | `principled-negotiation.md` |
| **Decision Tree & Expected Value** | Roll back probability-weighted payoffs across branches; max EV then risk + sensitivity check | Discrete options with probabilistic outcomes: build vs buy, settle vs litigate, pivot vs persevere | `decision-tree.md` |

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
- **Reversibility Grading**: Requires a named decision + concrete undo path (rollback, revoke, re-negotiate)
- **OODA Loop**: Requires a still-moving situation + at least one reversible next action
- **Probabilistic Reasoning**: Requires a checkable claim (outcome + timeframe + unit) + a reference class or prior anchor
- **Principled Negotiation**: Requires a live counterpart + your own alternatives inventoried and valued (a BATNA you could actually exercise)
- **Decision Tree & Expected Value**: Requires discrete alternatives + base-rate-anchored probabilities + quantifiable payoffs (ordinal utility acceptable)

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
- "How much analysis does this decision deserve / is it reversible / one-way vs two-way door" → Reversibility Grading (primary) ⚡ If the question is values-level "should I do this at all" (life/career/startup direction) → use Death Filter
- "Situation still moving, must act under time pressure (incident, outage, moving-target debugging)" → OODA Loop (primary) ⚡ If already stabilized → use Incident Response & Postmortem (Engineering); if rehearsing before action → use Pre-mortem & Counterfactual
- "Forecast / estimate an uncertain number / how likely is X / update a belief with evidence" → Probabilistic Reasoning (primary) ⚡ If only qualitative ranking of known risks → use Risk Matrix; if weighing options against criteria → use Decision Matrix
- "Negotiate a deal / salary / vendor terms / reach agreement with another party / deadlock over positions" → Principled Negotiation (primary) ⚡ If no real alternative to walk away to → build the BATNA first (Decision Matrix + Reversibility Grading); if mapping who influences the outcome without a live counterpart → use Stakeholder Mapping (Strategic Analysis)
- "Build vs buy / settle vs litigate / what's the expected value of this gamble / weight the option by what could happen" → Decision Tree & Expected Value (primary) ⚡ If estimating one uncertain quantity (no choice among branches) → use Probabilistic Reasoning; if scoring options on criteria without probability structure → use Decision Matrix

## Common Combinations

- **Major decision**: Socratic questioning (clarify assumptions) → Decision Matrix → Pre-mortem (risk review)
- **Requirement full lifecycle**: Kano (classify nature) → MoSCoW (scope) → RICE (prioritize)
- **Comprehensive risk assessment**: FMEA (systematic identification) → Pre-mortem (imaginative supplement) → Second-Order Thinking (chain effects)
- **Major life/startup decision**: Death Filter (filter true inclination) → Pre-mortem (rehearse selected direction risks) → Second-Order Thinking (long-term effects)
- **Project kickoff risk assessment**: Pre-mortem (identify risks) → Risk Matrix (quantify and rank) → FMEA (deep analysis of high-risk items)
- **Technology selection risk**: Decision Matrix (option comparison) → Risk Matrix (risk ranking) → Second-Order Thinking (chain effects)
- **Uncertain reversible decision**: Reversibility Grading (classify undo cost) → Probabilistic Reasoning (bound the estimate) → OODA Loop (cycle if the situation keeps moving)
- **In-flight incident**: OODA Loop (cycle reversible moves while degraded) → Incident Response & Postmortem (extract learning after stabilization)

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

"How much process does this decision deserve?"
  ├─ Values-level "should I do this at all" (life, career, startup direction)?
  │   └─ Yes → Death Filter
  ├─ Undo cost is the open question (tech, product, process, org call)?
  │   └─ Yes → Reversibility Grading
  └─ Situation moving + time pressure + reversible moves available?
      └─ Yes → OODA Loop

"Estimating an uncertain quantity"
  ├─ Qualitative screening of an identified risk list?
  │   └─ Yes → Risk Matrix
  ├─ Estimating / forecasting a number that updates with evidence?
  │   └─ Yes → Probabilistic Reasoning
  └─ Situation still moving and action cannot wait for the estimate?
      └─ Yes → OODA Loop (act on ~70% confidence for reversible moves)

"Reaching agreement with another party"
  ├─ Live counterpart, terms on the table (price, salary, scope, partnership)?
  │   └─ Yes → Principled Negotiation
  ├─ No live counterpart — deciding whether/how much to commit to a path?
  │   └─ Yes → Reversibility Grading (or Death Filter for values-level calls)
  └─ Multiple parties with veto power, no single negotiation table?
      └─ Yes → Stakeholder Mapping (Strategic Analysis)

"Choosing among probabilistic outcomes"
  ├─ Discrete options, outcomes with probabilities and quantifiable payoffs?
  │   └─ Yes → Decision Tree & Expected Value
  ├─ One uncertain quantity to estimate (no branch choice)?
  │   └─ Yes → Probabilistic Reasoning
  └─ Fixed evaluation criteria, no probability structure?
      └─ Yes → Decision Matrix
```

## Methodology Mutual Exclusion and Ordering Constraints

| Constraint pair | Rule | Reason |
| --- | --- | --- |
| RICE ↔ ICE | **ICE for rough screening → RICE for fine ranking**, don't use in parallel | ICE is a simplified version of RICE; parallel use produces redundant output |
| RICE vs Decision Matrix | **Choose by evaluation dimensions**: fixed R/I/C/E→RICE; custom dimensions→Decision Matrix | Core difference is whether dimensions are fixed; input structure is similar but purposes differ |
| FMEA → Pre-mortem | **FMEA before Pre-mortem** (comprehensive risk assessment scenario) | FMEA systematically identifies; Pre-mortem supplements imaginatively |
| Reversibility Grading vs Death Filter | **Choose by question level**: values-level "whether at all"→Death Filter; process depth "how much analysis"→Reversibility Grading | Different questions about the same decision; they compose on big calls (filter first, then grade) rather than run in parallel |
| OODA Loop → Incident Response & Postmortem | **Same event, by phase**: in-flight → OODA Loop; stabilized → Incident Response & Postmortem (`engineering/`) | Both on the same live event split attention from the loop; postmortem needs the stabilized outcome as input |
| Probabilistic Reasoning vs Risk Matrix | **Choose by treatment**: calibrated estimate that updates with evidence→Probabilistic Reasoning; qualitative P×I screening of a risk list→Risk Matrix | Same input (uncertainty), different output: a number to revise vs a zone to rank |
| Principled Negotiation vs Stakeholder Mapping | **Choose by state**: live counterpart with terms→Principled Negotiation; mapping all parties' influence before/without a table→Stakeholder Mapping (Strategic Analysis) | Negotiation works one counterpart's interests; stakeholder mapping works the whole influence field — feeding it into your BATNA estimate |
| Decision Tree vs Decision Matrix vs Probabilistic Reasoning | **Choose by question type**: choosing among probabilistic gambles→Decision Tree; scoring options on criteria→Decision Matrix; estimating one uncertain quantity→Probabilistic Reasoning | Same inputs recur (options, uncertainty) but the outputs differ: a choice, a ranking, a number |
