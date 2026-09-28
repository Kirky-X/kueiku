# Stakeholder Mapping

## Core Concept
Influence×Interest matrix to identify and manage all key stakeholders.

## Applicable Scenarios
✅ **Best for**
- Organizational change, cross-department projects, policy implementation

⚠️ **When NOT to use**
- Stakeholder set is small and obvious (a 3-person decision loop) — the map adds ceremony
- Influence is dynamic or contested (reorgs, political flux) — a static map goes stale within weeks; re-map instead
- You need deep needs analysis of one stakeholder — use User Research or JTBD for the individual level

## Key Steps
1. List all stakeholders
2. Assess Influence (High/Low) and Interest (High/Low)
3. Plot on 2×2 matrix
4. Define engagement strategy per quadrant: Manage Closely (H/H), Keep Satisfied (H-I), Keep Informed (L-H), Monitor (L/L)

## Output Template

```
| Stakeholder | Influence | Interest | Quadrant        | Engagement owner | Cadence & channel   | Current stance |
| ----------- | --------- | -------- | --------------- | ---------------- | ------------------- | -------------- |
| [CTO]       | High      | High     | Manage Closely  | [you]            | [weekly 1:1]        | [supportive]   |
| [Legal]     | High      | Low      | Keep Satisfied  | [PM]             | [milestone briefs]  | [neutral]      |
| [Support]   | Low       | High     | Keep Informed   | [PM]             | [biweekly digest]   | [champion]     |
| [Other teams]| Low      | Low      | Monitor         | —                | [changelog]         | [unaware]      |

Movement risks: [High-Interest→Low if X] / [Low-Influence→High at gate review] — plan: [note]
```

## Failure Modes
- Influence scored by org chart: the real veto lives two levels down → calibrate with people who've run similar projects before plotting
- Static map for a moving project: quadrants flip at funding gates, launches, incidents → re-plot at every phase boundary
- Managed-on-paper only: every stakeholder gets "weekly" but the map never changes engagement behavior → each row must name a channel and owner that actually exists

## Evidence Strength
Practitioner consensus — the influence/interest grid is standard project-management practice with no controlled validation; its value is coverage (surfacing the forgotten stakeholder) more than quadrant precision.

## Source
Eden & Ackerman; standard stakeholder analysis methodology.
