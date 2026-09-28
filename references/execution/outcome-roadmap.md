# Outcome Roadmap

## Core Concept
Transform a feature-focused roadmap into an outcome-focused one using the format: Enable [segment] to [customer outcome] so that [business impact]. Shifts from "what we'll build" to "what we'll achieve."

## Applicable Scenarios
- Roadmap currently lists features/outputs instead of outcomes
- Need to align roadmap with business objectives
- Stakeholders question roadmap priorities

⚠️ **When NOT to use**
- Compliance and platform work where the deliverable is the point ("ship SOC2 evidence") — forcing outcomes produces padded language, not clarity
- Discovery-stage planning where you don't yet know which outcome is achievable — commit to a learning outcome, not a business outcome
- Pure communication theater: renaming features into outcome sentences while prioritization still happens by effort → the roadmap must re-rank or nothing changed

## Key Steps
1. Audit current roadmap items — are they outputs (features) or outcomes?
2. For each output, rewrite using: Enable [segment] to [customer outcome] so that [business impact]
3. Validate each item has a measurable business impact
4. Prioritize by business impact, not by feature effort
5. Review with stakeholders — does each item clearly connect to business value?

## Output Template

```
| Now / Next / Later | Outcome statement                                                        | Measure (business impact) | Current baseline → target | Leading indicator       |
| ------------------ | ------------------------------------------------------------------------ | ------------------------- | ------------------------- | ----------------------- |
| Now                | Enable [new teams] to [self-serve onboarding] so that [CAC drops]         | CAC                       | $420 → $350               | [activation rate]       |
| Next               | Enable [admins] to [audit access in one view] so that [enterprise deals unblock] | [deal cycle days]  | 45 → 30                   | [security review pass]  |
| Later              | Enable [mobile users] to [track orders] so that [support cost drops]      | [tickets/order]           | 0.4 → 0.2                 | —                       |

Dropped in rewrite: [feature X — no one could name its outcome] — explicit decision to defer/kill
Review rhythm: [quarterly outcome review — did shipped work move the measure?]
```

## Failure Modes
- Outcome cosplay: "ship dark mode" becomes "enable users to delight in personalization" — a feature in a costume → the business-impact clause must name a metric someone owns
- Unowned measures: outcome stated, no baseline, no target, no owner → every row carries baseline → target and an accountable name
- Later-land purgatory: vague outcomes parked in Later forever — fine, but say why (uncertain impact vs dependent on Now items)

## Evidence Strength
Practitioner consensus — consistent with outcome-driven product practice (OKR lineage); adopters report better prioritization conversations, but there is no controlled evidence outcome-framed roadmaps outperform output roadmaps on delivery efficiency — the claimed gains are in focus and stakeholder alignment.

## Source
Joshua Seiden & Jeff Patton; popularized in outcome-driven product management.
