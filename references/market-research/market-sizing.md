# Market Sizing

## Core Concept
Calculate TAM (Total Addressable Market), SAM (Serviceable Addressable Market), SOM (Serviceable Obtainable Market) using top-down and bottom-up approaches with triangulation for validation.

## Applicable Scenarios
✅ **Best for**
- Funding decks
- New market assessment
- Strategic planning

⚠️ **When NOT to use**
- Headline arithmetic — "$X B market × 1% share" is not sizing; a top-down number only counts once bottom-up triangulation gates it
- Deciding whether to build a feature — sizing is a strategy input, not product evidence; use **Kano Model** or **JTBD** research for that
- Markets where competitive share is the real question — incumbent strength matters more than market size; reach for **Porter's Five Forces**
- Demands for false precision — a single confident number invites over-trust; present ranges with named assumptions

## Key Steps
1. Define the market boundary (what product/service in what geography?)
2. Top-down: start with industry reports, macro data; estimate TAM
3. Bottom-up: start with unit economics (customers × ARPU); build up
4. Triangulate: compare top-down and bottom-up; reconcile differences
5. Narrow TAM → SAM (your segment) → SOM (realistic capture)
6. Document assumptions and data sources

## Output Template

```
Market definition: [product/service] for [customer] in [geography]
Top-down: industry total [$] × applicable slice [%] → TAM [$]
Bottom-up: [# target customers] × [ARPU $] × [achievable penetration %] → [$]
Triangulation: top-down vs bottom-up gap = [×n] — reconciled by [which assumption moves]
SAM: [segment/geography/channel filter] → [$]
SOM: [realistic capture, 3-5 yrs, evidence] → [$]
Key assumptions: [each with source]
Sensitivity: TAM range [$low–$high] when [variable] swings ±[n%]
```

## Failure Modes
- Top-down fantasy: industry totals multiplied into a number with no causal path to your customers → gate every figure against a bottom-up build; the two must reconcile within an order of magnitude
- Boundary creep: defining the market as "everyone with a phone" → fix the boundary first (who pays, for what, where); a market without a refusal criterion is not a market
- Unrecorded assumptions: the model can't be audited or falsified → log every assumption with its source and publish a sensitivity band, not a point estimate
- TAM as the goal: SAM/SOM skipped so the headline flatters the deck → show the full TAM→SAM→SOM funnel; the obtainable number is the only decision-grade one

## Evidence Strength
Practitioner consensus — triangulating bottom-up builds against top-down anchors is the standard taught method and the only one that yields defensible numbers, but absolute precision is unattainable: market boundaries and adoption rates are estimates, and top-down inputs come from analyst reports whose definitions rarely match yours. Report ranges with assumptions, never point estimates alone.

## Source
Standard market research methodology; widely used in startup fundraising.
