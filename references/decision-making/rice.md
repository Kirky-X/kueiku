# RICE Scoring

## Core Concept
Quantify priority using Reach × Impact × Confidence ÷ Effort. Each dimension is scored on a defined scale, producing a comparable priority number for ranking features, projects, or initiatives.

## Applicable Scenarios
✅ **Best for**
- Product roadmap prioritization
- Requirement ranking across teams
- Resource allocation decisions

⚠️ **When NOT to use**
- Effort is the binding constraint and the question is sequencing, not value density — RICE says "value per person-month", not "what ships first"; pair with delivery capacity and **Reversibility Grading** for quick-win ordering
- Strategic bets and platform infrastructure — low Reach today, compounding payoff later; RICE structurally starves them, so keep a strategic reserve outside the scoring
- Confidence has no evidence behind it — the 50/80/100% knob launders vibes into a number; if no data or user input exists, run discovery first
- Compliance or executive-mandated items — they don't compete for score; exempt them from the ranking before it starts

## Key Steps
1. List all candidate items (features, projects, initiatives)
2. Score Reach: how many users/customers will this affect per period?
3. Score Impact: how much will this move the metric? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
4. Score Confidence: how sure are we? (100%=high, 80%=medium, 50%=low)
5. Score Effort: person-months required
6. Calculate RICE = (Reach × Impact × Confidence) / Effort
7. Sort by RICE score descending

## Output Template
```
RICE Prioritization:
| Item | Reach | Impact | Confidence | Effort | RICE Score |
|------|-------|--------|------------|--------|------------|
| A    | 1000  | 3      | 80%        | 2      | 1200       |
| B    | 500   | 2      | 100%       | 1      | 1000       |

Tier Recommendations:
  High priority (top 30%): [...]
  Medium priority: [...]
  Low priority (defer): [...]
```

## Failure Modes
- Effort estimated by the proposer is systematically optimistic: the denominator drives the score as hard as Reach → take Effort from an independent estimate or cap it in calendar time
- Impact numbers without a metric: "3 = massive" of what? → bind each Impact score to a named metric with a directional estimate before scoring
- Reach inflated to the whole user base for features only a segment touches → define Reach as the users who actually encounter the change per period
- Confidence as comfort: the percentage expresses stakeholder mood, not evidence → attach an evidence tag (data / user input / opinion) to every Confidence score
- Score worship: RICE becomes the roadmap instead of an input → treat the ranking as a proposal; strategy, dependencies, and commitments can override it with stated reasons

## Evidence Strength
Practitioner consensus — Intercom's published prioritization scheme, widely adopted in product management; it disciplines prioritization conversations by forcing explicit Reach, metric-bound Impact, and evidence-tagged Confidence. The arithmetic is exact only on judgment inputs: no research validates the specific scales or shows RICE rankings outperform other prioritization schemes on delivered outcomes.

## Source
Intercom product team; widely adopted in product management.
