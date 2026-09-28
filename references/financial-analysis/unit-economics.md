# Unit Economics

## Core Concept
Does one customer make or lose money, and how fast does the cash come back? Four numbers answer it: **CAC** (fully-loaded cost to acquire a customer), **contribution margin** (per-customer revenue minus variable costs of serving them), **LTV** (the margin a customer contributes over their lifetime), and **payback period** (months to recover CAC). Growth amplifies whatever the unit economics already are — scaling a negative unit economy buys losses faster, not success.

## Applicable Scenarios
✅ **Best for**
- Deciding whether to increase sales/marketing spend or scale a channel
- Startup viability checks and fundraising readiness
- Comparing channels and segments: which customers are worth acquiring

⚠️ **When NOT to use**
- Pre-revenue with no cost data — estimate ranges explicitly and revisit; do not fake precision
- Company-level P&L questions (whole-firm profitability drivers) — use DuPont Analysis for firm-level decomposition
- Fixed-cost-dominant businesses where per-customer framing misleads — contribution margin still applies; LTV framing may not

## Key Steps
1. Compute **CAC fully loaded**: all sales & marketing spend (ads + salaries + tools + agency fees) ÷ new customers acquired in the period — ads-only CAC is fiction
2. Compute **contribution margin** per customer: revenue − variable costs (COGS, support, payment fees, variable infrastructure)
3. Compute **LTV on margin, not revenue**: ARPU × gross margin × average lifetime (equivalently ARPU × gross margin ÷ churn rate); revenue-based LTV overstates health by the entire cost structure
4. Compute **payback period**: CAC ÷ monthly contribution margin per customer
5. Check health heuristics — these are inherited rules of thumb, **not laws**; state your own threshold and why:
   - LTV:CAC ≥ 3:1 (below ~1:1 you lose money per customer; just above, margin is too thin to fund growth)
   - Payback ≤ 12–18 months — for cash-constrained businesses payback is the binding constraint, not the ratio
   - Contribution margin positive and growing; SaaS extension: Rule of 40 (revenue growth % + profit margin % ≥ 40)
6. **Segment before deciding**: blended figures hide winner and loser channels — compute CAC/LTV/payback per channel and per cohort (cohort-level tracking: `data-analysis/cohort-analysis.md`)
7. Decide: scale segments that pay back inside runway; fix the inputs (price, margin, CAC, churn) or cut the rest
8. **Consistency with market sizing**: when feeding a bottom-up TAM/SOM estimate (`market-research/market-sizing.md`, customers × ARPU), reuse the same customer definition and ARPU computed here, so the market model and the unit economics reconcile instead of contradicting each other

## Output Template
```
Unit economics: [product / segment / channel]
CAC (fully loaded): [$] per customer  | blended $[x] vs [channel] $[y]
Contribution margin: [$ or %] per customer per month
LTV (margin-based): [$]  → LTV:CAC = [x.x]:1   [heuristic ≥ 3:1]
Payback: [n] months                                  [heuristic ≤ 12–18]
Blended-vs-segment note: [what the blended figure hides]
Decision: scale | fix inputs first | cut — and why
```

## Failure Modes
- Revenue-based LTV: drops the cost structure from the lifetime value → always margin-based
- Under-loaded CAC: excluding salaries and tools → fully loaded, or the ratio is fiction
- Blended CAC lies: one great channel subsidizes three broken ones inside the average → segment by channel and cohort
- Payback longer than runway: a "healthy" 3:1 with 24-month payback still bankrupts a cash-tight company → compare payback against runway months before scaling spend
- Treating 3:1 as a law: industry and margin-structure variance is wide → use it to trigger a conversation, not to end one

## Evidence Strength
Practitioner consensus — CAC, contribution margin, LTV, and payback are standard accounting identities, but the health thresholds (3:1, 12–18 months, Rule of 40) are venture-practitioner heuristics with wide industry variance, not empirical constants; they degrade outside subscription and e-commerce contexts.

## Source
David Skok, "SaaS Metrics 2.0" (unit economics canon); standard venture finance practice.
Provenance: metric set and benchmark structure absorbed from [claude-skill-management-consultant-B1](https://github.com/DogInfantry/claude-skill-management-consultant-B1) FRAMEWORKS.md §Unit Economics (Apache-2.0 license) and [knowledge-skills](https://github.com/deciqAI/knowledge-skills) `unit-economics-cac-ltv-payback` (MIT license); definitions, pitfalls, and thresholds-are-heuristics framing written for kueiku, absorbed 2026-09.
Admission: Build (new entry) — owns per-customer viability math (CAC / LTV / payback); existing financial-analysis entries value companies, not customers.
