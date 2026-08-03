# RICE Scoring

## Core Concept
Quantify priority using Reach × Impact × Confidence ÷ Effort. Each dimension is scored on a defined scale, producing a comparable priority number for ranking features, projects, or initiatives.

## Applicable Scenarios
✅ **Best for**
- Product roadmap prioritization
- Requirement ranking across teams
- Resource allocation decisions

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

## Source
Intercom product team; widely adopted in product management.
