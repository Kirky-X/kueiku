# Ideal Customer Profile (ICP)

## Core Concept
4-dimension ICP definition: Demographics (who they are), Behaviors (what they do), JTBD (what job they hire your product for), Needs (what outcomes they need). Used for sales lead scoring and targeted advertising.

## Applicable Scenarios
✅ **Best for**
- Sales lead scoring
- Targeted advertising
- Product-market fit validation

⚠️ **When NOT to use**
- No customers exist yet (0→1) — an ICP reverse-engineered from nothing is fiction; use Beachhead Segment hypotheses + interviews instead
- Product-led motion with self-serve signup — ICP gating at the door strangles volume; score for expansion propensity instead
- Founder-led sales with fewer than ~20 closed deals — there is no contrast data to score against; talk to every prospect instead of gating

## Key Steps
1. Analyze your best customers (highest LTV, lowest churn)
2. Define Demographics: company size, industry, role, location
3. Define Behaviors: usage patterns, buying signals, engagement
4. Define JTBD: what job do they hire your product to do?
5. Define Needs: what outcomes matter most?
6. Score leads against ICP; focus resources on highest-fit prospects

## Output Template

```
ICP (reverse-engineered from [N] best customers):
  Demographics: [size, industry, role, geo]
  Behaviors: [usage/buying signals that predict success]
  JTBD: [the job they hire the product for]
  Needs: [outcomes that matter most]

Anti-ICP (worst customers, and why): [disqualifying traits]
Lead scoring: [dimensions + weights, sales-follow-up threshold]
Refresh trigger: [e.g. quarterly, or a churn-pattern shift]
```

## Failure Modes
- ICP by vanity traits: "companies like Stripe" — resemblance without outcome data → derive every dimension from best/worst customer contrast, not aspiration
- Frozen ICP: the profile outlives the market → re-fit quarterly against fresh win/churn data
- Over-gating: disqualifying leads that would have expanded → score in tiers; review disqualified-but-won losses each quarter

## Evidence Strength
Practitioner consensus in B2B sales/marketing; outcome-linked ICPs reliably improve lead quality in case practice, but published effect sizes are mostly vendor-reported. The 4-dimension decomposition is a framework choice, not a validated model.

## Source
Standard B2B sales/marketing practice (ICP scoring is a convention of ABM and sales-development playbooks); the JTBD dimension references Clayton Christensen's jobs framework.
