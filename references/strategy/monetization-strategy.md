# Monetization Strategy

## Core Concept
7 monetization models: Freemium, Subscription, Usage-based, Per-seat, One-time, Marketplace, Advertising.

## Applicable Scenarios
✅ **Best for**
- Business model selection, monetization efficiency optimization

⚠️ **When NOT to use**
- Willingness to pay is unknown — model selection before price validation picks a container for an unvalidated guess
- Unit economics are underwater — no monetization model fixes a product that costs more to serve than any price users accept
- Marketplace dynamics absent for the "Marketplace" option — take rate monetization requires liquidity you may never reach

## Key Steps
1. List all 7 monetization models
2. Assess fit for each: your product type, user willingness to pay, market norms
3. Select primary model + backup
4. Design pricing tiers
5. Validate with market data

## Output Template

```
| Model        | Fit with product type | WTP evidence | Market norm | Conflict risk | Verdict |
| ------------ | --------------------- | ------------ | ----------- | ------------- | ------- |
| Freemium     | [why fits/doesn't]    | [data or none]| [norm]     | [cannibalization?] | [keep/cut] |
| Subscription | ...                   | ...          | ...         | ...           | ...     |
| Usage-based  | ...                   | ...          | ...         | ...           | ...     |
| (… all 7)    |                       |              |             |               |         |

Primary: [model] — because [decisive reason]
Backup: [model] — trigger to switch: [metric/threshold]
Tier draft: [Free: x / Pro: $y — value metric: z]
Validation next step: [pricing survey / A/B / sales test] by [date]
```

## Failure Modes
- Model by imitation: copying a famous company's model without their cost structure → every row needs your economics, not theirs
- Value metric mismatch: charging per seat when value scales with usage (or vice versa) → derive the metric from what drives customer value, not from billing convenience
- Primary without backup: market norms shift (seat-based → usage-based across SaaS) → name the trigger that flips you before you need it

## Evidence Strength
Practitioner consensus — the taxonomy is descriptive and the fit logic is sound, but model-to-success claims are anecdotal; pricing research (e.g. Van Westendorp, A/B) supplies the actual evidence, so treat this as the structuring layer on top.

## Source
Standard monetization strategy methodology.
