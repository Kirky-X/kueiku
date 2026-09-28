# Assumption Mapping

## Core Concept
Make implicit assumptions behind a product/project explicit, ranked on an Impact × Risk 2D matrix, prioritizing validation of high-impact + high-risk assumptions. The basic version uses 4 risk categories: Desirability (do users want it) / Viability (does the business work) / Feasibility (can we build it) / Usability (can users use it); the extended version adds 8 categories, supplementing with Ethics, Legal, Brand, Strategic Fit, etc.

## Applicable Scenarios
- Before launching a new feature/product, identify "what are we actually betting on"
- When multiple assumptions coexist, decide which to validate first
- Cross-team alignment on "what must be true for this to work"

⚠️ **When NOT to use**
- The proposal has one dominant bet — skip the matrix, design that one experiment
- Assumptions can be settled by reading data you already have — mapping exercise before a 10-minute log query is ceremony
- Regulated launches where the gate sequence is fixed by compliance — the ordering is prescribed, not discovered

## Key Steps
1. List all assumptions the proposal depends on, categorize by 4 (or 8) risk types
2. For each assumption assess: if false, impact on business (High/Medium/Low) + current risk (High/Medium/Low)
3. Plot on Impact × Risk matrix, prioritize the "high impact + high risk" quadrant
4. Design minimum experiments for each priority assumption (see experiment-design-library.md)
5. After experiments, return to matrix, update risk scores, and decide GO / Pivot / Kill

## Output Template

```
Proposal: [one line]

| Assumption (falsifiable form)                       | Type        | Impact | Risk | Priority | Experiment            |
| --------------------------------------------------- | ----------- | ------ | ---- | -------- | --------------------- |
| [Segment X will pay $Y for Z]                        | Viability   | High   | High | P0       | [pricing page A/B]    |
| [Users can complete flow W without help]             | Usability   | High   | Med  | P1       | [5-user prototype test]|
| [We can source data D under budget B]                | Feasibility | Med    | Low  | P3       | [vendor quotes]       |

Test order: P0 → P1 (P0 failing kills the bet regardless of P1)
Decision after tests: GO / Pivot / Kill — revisit date: [date]
```

## Failure Modes
- Unfalsifiable assumptions: "users will love it" can't be tested → rewrite each assumption so an experiment could prove it false
- Mapping meeting without re-mapping: risks scored once at kickoff, never updated after experiments → the matrix is a living artifact; re-plot after each result
- Comfortable quadrant: team validates low-risk assumptions first because they're easy → test order is set by the quadrant, not by convenience

## Evidence Strength
Practitioner consensus — an application of established decision logic (spend evidence where the bet is biggest); no controlled studies compare assumption-mapped vs unmapped launches, and impact/risk scores are judgment calls whose quality decides everything.

## Source
Popularized by Teresa Torres in *Continuous Discovery Habits*; 4-risk model originates from IDEO; 8-risk extension from Product Compass.
