# Pricing Strategy

## Core Concept
Van Westendorp Price Sensitivity Meter + value metric identification + tier design.

## Applicable Scenarios
✅ **Best for**
- Pricing/repricing decisions, price sensitivity assessment

⚠️ **When NOT to use**
- Fewer than ~200 surveyable respondents who match the buyer — Van Westendorp curves from tiny samples mislead
- Brand-new category with no price anchors in respondents' heads — the four questions return noise
- B2B negotiated pricing where list price is a fiction — interview sales outcomes instead

## Key Steps
1. Identify your value metric (what unit of value do customers buy?)
2. Conduct Van Westendorp survey: at what price is it too cheap / cheap / expensive / too expensive?
3. Find optimal price range
4. Design tiers based on value metric
5. Validate with A/B testing

## Output Template

```
Value metric: [per user / per 1k events / per seat — why this tracks customer value]

Van Westendorp (n=[sample], respondent profile: [who]):
  Point of Marginal Cheapness (PMC): $[x]   — below: quality doubts
  Indifference Price Point (IPP):    $[y]
  Point of Marginal Expensiveness (PME): $[z] — above: rejection
  Optimal Price Range (OPP): $[a – $b]

Tier design:
  [Starter] $[x]/[metric] — for [segment], capped at [usage]
  [Pro]     $[y]/[metric] — for [segment], the intended home
  [Scale]   $[z]/[metric] — for [segment]

Validation: A/B or sales test of [$y vs $y±15%] on [segment], success criterion: [revenue per visitor / conversion floor]
```

## Failure Modes
- Asking willingness-to-pay directly ("what would you pay?") — the PSM's four questions exist precisely because direct answers are unreliable → never replace the four questions with one
- Surveying users instead of buyers: end users tolerate prices they don't pay → sample the budget holder
- Metric locked before testing: seat pricing on a product whose value is usage-shaped → A/B the metric itself when unsure, not just the number

## Evidence Strength
Mixed — Van Westendorp is a standard, cheap first pass, but stated-price methods systematically diverge from revealed willingness to pay (the gap is well documented); treat its range as a hypothesis band to be confirmed by real transactions, which the framework itself prescribes.

## Source
Peter van Westendorp (1976); pricing strategy methodology.
