# Strategy Red Team

## Core Concept
Stress-test a strategy by steelmanning it (strongest possible version), then attacking it from multiple angles, ranking attacks by impact × likelihood × cheapness of mitigation.

## Applicable Scenarios
- Before finalizing a major strategic decision
- When the team is too close to the plan to see its weaknesses
- Board/investor preparation

⚠️ **When NOT to use**
- The decision is small and reversible — run the experiment instead of the red team
- Without decision authority in the room — findings that can't change the plan are ceremony
- As retroactive justification: red-teaming a strategy already announced and resourced produces diluted attacks — hold it before commitment

## Key Steps
1. Steelman the strategy: articulate the strongest possible version
2. Attack from multiple angles: market, competitive, execution, financial, organizational
3. For each attack, estimate: Impact (if it hits) × Likelihood (probability) × Cheapness (cost to mitigate)
4. Rank attacks by the composite score
5. Address top-ranked attacks in the strategy; document accepted risks

## Output Template

```
Strategy under review: [one paragraph] — steelman: [strongest version, stated by a believer]

| # | Angle       | Attack (how this fails)                     | Impact 1-5 | Likelihood 1-5 | Mitigation cheapness 1-5 | Score | Action            |
| --- | --------- | ------------------------------------------- | ---------- | -------------- | ------------------------ | ----- | ----------------- |
| 1 | Competitive | [incumbent bundles our core feature free]   | 5          | 3              | 1 (can't match burn)     | 15    | [preempt via ...] |
| 2 | Execution   | [key-person dependency in data pipeline]    | 4          | 4              | 4 (document + hire)      | 12*   | [do first — cheap]|
| 3 | Market      | [...]                                       | ...        | ...            | ...                      | ...   | ...               |

Accepted risks (documented, with owner): [attack + why we absorb it]
Changes made to the strategy as a result: [list] — if the list is empty, the exercise was decorative
```

## Failure Modes
- Polite red team: insiders attack their own plan in front of its author — attacks arrive pre-weakened → assign attack ownership to people with no stake in the plan, or use the pre-mortem "failure already happened" framing
- Score soup: precise-looking composite scores from hand-waved inputs → show the ranges; a 15 vs 12 gap within estimation error should not decide priority (cheap mitigations may break ties)
- Attack backlog instead of decisions: every top attack spawns "further study" → each top-3 attack ends in a strategy change, a mitigation with owner, or a documented accepted risk

## Evidence Strength
Practitioner consensus — red-teaming and pre-mortems are widely adopted and the mechanism (prospective hindsight surfaces risks optimism hides) has experimental support in the judgment-and-decision-making literature; the specific impact × likelihood × cheapness scoring is a practical heuristic, not a validated instrument.

## Source
Adapted from military red teaming and Daniel Kahneman's pre-mortem technique.
