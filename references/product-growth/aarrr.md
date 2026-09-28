# AARRR Funnel

## Core Concept
5-stage growth funnel: Acquisition → Activation → Retention → Referral → Revenue. Identify which stage is the bottleneck to focus growth efforts.

## Applicable Scenarios
✅ **Best for**
- Growth bottleneck identification
- User lifecycle analysis
- Growth team prioritization

⚠️ **When NOT to use**
- Retention is broken: pouring users into a leaking funnel wastes everything upstream — fix retention first; the funnel's stage order isn't a work order
- Metrics for stages undefined or gameable — a funnel of vanity metrics points experiments in wrong directions
- Products with multi-loop value paths (marketplaces, UGC) — single linear funnel misses loops; consider growth loops alongside

## Key Steps
1. Define metrics for each stage: Acquisition (signups), Activation (first key action), Retention (return usage), Referral (invites), Revenue (payment)
2. Measure conversion rates between stages
3. Identify the stage with the lowest conversion (the bottleneck)
4. Focus growth experiments on the bottleneck stage
5. Re-measure after experiments; iterate

## Output Template

```
Stage metrics (defined before measuring):
  Acquisition: [visits → signups]        [8%]
  Activation:  [signup → first key action: created 1st project] [35%]
  Retention:   [week-4 return rate]      [22%]   ← health check first
  Referral:    [users sending ≥1 invite] [4%]
  Revenue:     [trial → paid]            [9%]

Bottleneck: [Activation 35% vs benchmark x] — why here and not a vanity-low stage: [highest leverage × fixable]
Experiment queue for bottleneck: [3 hypotheses with owners and dates]
Re-measure: [after each experiment — did the stage rate move? did it hold?]
```

## Failure Modes
- Funnel-wide ping-pong: experiments scattered across all five stages each week — motion without leverage → one bottleneck at a time, and re-evaluate only after its rate moves
- Activation defined as login: "activated" users who never touched core value → the activation event must be the first moment of real value, not a technical step
- Referral measured as invites sent, not invites converted: k-factor theater → measure new users acquired through referral, not invitation buttons clicked

## Evidence Strength
Practitioner consensus — the canonical startup metrics funnel; the stage decomposition and bottleneck logic are sensible and near-universally taught, while benchmark conversion rates float around as folklore — treat external benchmarks as rough context and your own trend as the real signal.

## Source
Dave McClure, 500 Startups (2007); *Startup Metrics for Pirates*.
