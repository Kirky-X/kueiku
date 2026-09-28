# Kano Model

## Core Concept
Classify features into 5 categories based on how they affect satisfaction: Must-be (dissatisfiers if absent), Performance (linear satisfaction), Excitement (delighters), Indifferent (don't matter), Reverse (some users dislike). Prevents over-investing in features that don't move satisfaction.

## Applicable Scenarios
✅ **Best for**
- Requirement nature classification
- Satisfaction strategy
- Feature type judgment

⚠️ **When NOT to use**
- Fewer than ~50 credible respondents per feature set — the classification matrix is statistical; small samples produce noise labeled as insight
- Features users can't meaningfully imagine (novel technology) — both Kano questions assume the respondent can picture presence and absence
- As the sole prioritization input — Kano reads satisfaction impact, not effort, revenue, or strategy; pair with RICE/ICE

## Key Steps
1. List candidate features
2. Design Kano questionnaire: for each feature, ask functional (if present) and dysfunctional (if absent) questions
3. Classify each feature: Must-be / Performance / Excitement / Indifferent / Reverse
4. Prioritize: Must-be first, then Performance, then selective Excitement
5. Monitor: features migrate from Excitement → Performance → Must-be over time

## Output Template

```
Survey: n=[respondents], segment [who], features [list]

| Feature        | Functional Q: "if you had X" | Dysfunctional Q: "if you didn't" | Classification | Strength |
| -------------- | ---------------------------- | -------------------------------- | -------------- | -------- |
| [offline mode] | like / must-have             | normal / don't care              | Must-be        | strong   |
| [AI summaries] | love it                      | neutral                          | Excitement     | medium   |
| [skins]        | neutral                      | neutral                          | Indifferent    | —        |
| [forced tour]  | dislike                      | like it                          | Reverse        | —        |

Priority: 1. Must-be gaps [list] 2. Performance investments [list] 3. selective delighters [1 max, cheap ones]
Migration watch: [which features crossed from delighter to expected since last survey]
```

## Failure Modes
- Self-reported delight: users claiming features they'd never use as "must-haves" — stated importance inflates → cross-check with behavior data where available; weight Must-be only when both agree
- Category from one answer pair: classification needs the full answer matrix with strength (mixed answers mean ambiguity, not a category) → use the standard evaluation table, report ambiguous separately
- Kano rerun never: delighters from 2020 are today's table stakes → re-classify annually or at major version points; the model describes a moving target

## Evidence Strength
Practitioner consensus — the satisfaction asymmetry it captures (absence hurts more than presence helps, for basics) is consistent with well-known satisfaction research; the questionnaire method is straightforward but sensitive to sample quality and question wording, and feature classifications should be treated as segment-specific snapshots rather than stable truths.

## Source
Noriaki Kano (1980s); customer satisfaction model.
