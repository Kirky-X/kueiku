# Pareto Analysis

## Core Concept
The 80/20 rule: roughly 80% of effects come from 20% of causes. Identify and prioritize the vital few factors that drive the majority of results, enabling focused resource allocation.

## Applicable Scenarios
- Resource allocation decisions
- Problem prioritization
- Key driver identification

⚠️ **When NOT to use**
- Cause impacts are unmeasured and can't be estimated — the ranking becomes opinion in a chart
- Causes interact strongly (fixing A fixes B) — independent-ranking breaks down; use systems thinking
- Fairness/compliance allocation — concentrating resources on the "vital few" customers/incidents is a policy decision the tool can't make

## Key Steps
1. List all contributing factors or problems with their measured impact
2. Sort by impact descending
3. Calculate cumulative percentage for each factor
4. Identify the ~20% of factors that contribute ~80% of total impact (the "vital few")
5. Focus resources on the vital few; deprioritize or eliminate the "trivial many"

## Output Template

```
Impact unit: [revenue lost / tickets / downtime minutes] — period: [range]

| Rank | Cause                 | Impact  | % of total | Cumulative % | Action     |
| ---- | --------------------- | ------- | ---------- | ------------ | ---------- |
| 1    | [checkout timeout]    | 4,100   | 41%        | 41%          | fix now    |
| 2    | [search no-results]   | 2,300   | 23%        | 64%          | fix now    |
| 3    | [slow images]         | 1,200   | 12%        | 76%          | schedule   |
| 4-10 | [long tail]           | 2,400   | 24%        | 100%         | deprioritize |

Vital few: [2-3 causes ≈ 76% of impact] — cut line: [why there, not at exactly 80%]
Re-check: [does the tail hide a cause about to grow? name it]
```

## Failure Modes
- Uncounted causes: categories drawn before counting ("other" swallows 40%) → define mutually exclusive categories first; cap "other" or re-investigate it
- 80/20 asserted, not computed: vital few announced without the cumulative table → run the arithmetic; sometimes the distribution is flat (60/40) and focus is wrong
- Frozen priorities: last year's Pareto driving this year's budget — cause impact drifts → recompute each period, and say what changed rank

## Evidence Strength
Mixed — heavy-tailed distributions are empirically common (defects, revenue, complaints), but the exact 80/20 split is folklore: measured splits range widely. The durable value is rank-and-cumulate discipline, which is arithmetic, not theory.

## Source
Vilfredo Pareto (1896); popularized by Joseph Juran in quality management.
