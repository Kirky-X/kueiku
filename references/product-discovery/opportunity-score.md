# Opportunity Score

## Core Concept
Quantify the opportunity size for a given need using Importance × (1 − Satisfaction). Needs that are important but currently underserved score high, indicating the biggest product opportunity. Derived from Kano thinking but normalized to 0–1 for easy cross-comparison.

## Applicable Scenarios
- Have user survey data (importance + satisfaction), need to prioritize requirements
- Find "low satisfaction, high importance" quick-win opportunities
- Validate product-market fit gaps

⚠️ **When NOT to use**
- No survey data yet — scores from guessed ratings are decoration; collect importance/satisfaction first
- Needs wording is ambiguous across respondents — inconsistent stimuli produce garbage averages
- Choosing between strategic bets where satisfaction isn't the lever (new market creation) — the score presumes an existing served need

## Key Steps
1. For each candidate need/feature, ask target users to rate: Importance (1–5 or 1–10) + Current Satisfaction (1–5)
2. Normalize: map both importance and satisfaction to 0–1 (e.g. on a 5-point scale, score = (rating−1)/4)
3. Calculate Opportunity Score: Opportunity = Importance × (1 − Satisfaction)
4. Sort by Opportunity descending, focus on high scores (high importance + low satisfaction = blue ocean)
5. High-score items with already-high satisfaction are met needs; low-importance items with low satisfaction still aren't worth investing in

## Output Template

```
Survey: n=[respondents], profile [who], needs phrased as [outcomes, not features]

| Need (outcome wording)              | Imp 1-5 | Sat 1-5 | Importance norm | (1−Sat) norm | Opportunity | Read             |
| ----------------------------------- | ------- | ------- | --------------- | ------------ | ----------- | ---------------- |
| [find reusable code quickly]        | 4.6     | 2.1     | 0.90            | 0.78         | 0.70        | attack           |
| [export to any format]              | 3.9     | 4.4     | 0.73            | 0.15         | 0.11        | met need         |
| [AI-written changelogs]             | 2.0     | 1.8     | 0.25            | 0.80         | 0.20        | unimportant      |

Priorities: top [2] by opportunity — cross-check segment splits before committing (averages hide divergent segments)
```

## Failure Modes
- Feature-worded needs: "dark mode" rated, not the underlying outcome → rate outcomes; features carry solution bias
- Average masking: one segment 1-satisfied, another 5-satisfied averages to a meaningless 3 → segment the data before ranking
- Treating 0.70 vs 0.65 as decisive: rating-scale noise swamps gaps that small → separate clear tiers; below that, tie-break with evidence outside the survey

## Evidence Strength
Mixed — the importance × (1 − satisfaction) form is a sensible, widely used heuristic for spotting underserved needs, but it inherits all rating-scale weaknesses (scale-use variance, stated preference bias); Olsen presents it as a prioritization aid, not a validated instrument, and it works best when followed by behavioral confirmation.

## Source
Dan Olsen, *The Lean Product Playbook* (2015)
