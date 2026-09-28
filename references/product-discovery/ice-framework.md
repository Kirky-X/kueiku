# ICE Framework

## Core Concept
Quick prioritization using Impact × Confidence × Ease, scoring each idea 1-10 on three dimensions. A lightweight alternative to RICE when you need to screen many ideas fast (under 30 minutes) without precise metrics.

## Applicable Scenarios
- Large backlog of ideas needing quick initial screening
- Early-stage teams without reliable Reach data for RICE
- Time-constrained prioritization workshops

⚠️ **When NOT to use**
- Committing a quarter's roadmap on ICE scores — screening output feeds RICE or experimentation, not direct commitments
- One scorer with private context — unexplained individual scores produce one person's ranking wearing a formula
- Items with wildly different effort scales (a 1-hour fix vs a quarter build) — Ease compresses that into one number; split the backlog first

## Key Steps
1. List all candidate ideas/features
2. Score each on Impact (1-10): how much will this move the metric if it works?
3. Score each on Confidence (1-10): how sure are we it will work?
4. Score each on Ease (1-10): how easy is it to implement?
5. Calculate ICE = Impact × Confidence × Ease, sort descending
6. Top items go forward; discuss scoring disagreements as a team

## Output Template

```
Scoring session: [date], scorers: [names], metric focus: [activation]

| Idea | Impact | Confidence | Ease | ICE | Notes on the lowest dim                |
| ---- | ------ | ---------- | ---- | --- | -------------------------------------- |
| [A]  | 8      | 4          | 7    | 224 | confidence low — no prior data          |
| [B]  | 5      | 8          | 9    | 360 | —                                       |
| [C]  | 9      | 3          | 2    | 54  | ease low — needs legal review           |

Disagreements logged: [idea X: scorer 1 said 7, scorer 2 said 4 — resolved by evidence Y]
Next: top items → [RICE scoring / experiment design]; bottom: parked with revisit date
```

## Failure Modes
- Impact scored 10 by default: enthusiasm leaks into the dimension with no ceiling anchor → anchor scales in writing (what does a 3 vs 7 vs 10 impact look like?) before scoring
- Confidence never interrogated: everyone scores their own idea confidently → the Confidence dimension exists to discount unsupported bets; require evidence for ≥7
- Precision cosplay: two-decimal ICE averages implying measurement that doesn't exist → the output is a screening order, not a valuation

## Evidence Strength
Practitioner consensus — a folk heuristic from growth practice; deliberately unvalidated and rough (multiplicative scales with subjective anchors), it trades statistical meaning for speed. Use as a screen, then let RICE or experiments supply the actual evidence.

## Source
Sean Ellis, *Hacking Growth* (2017)
