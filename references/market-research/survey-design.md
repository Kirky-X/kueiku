# Survey Design

## Core Concept
A survey is an instrument: wording, order, and sample shape the answers as much as respondents' opinions do. Design it before fielding — decision → hypotheses → constructs → questions → scales → pilot → field → clean — and prefer behavior questions over stated intent, because what people say they would do and what they did diverge systematically.

## Applicable Scenarios
✅ **Best for**
- Quantifying known hypotheses across many users (validate interview findings at scale)
- Satisfaction/usage baselines and tracking
- Segmentation inputs (feeds User Segmentation and User Personas)
- Pricing research with an established instrument (Van Westendorp PSM)

⚠️ **When NOT to use**
- Discovering unknown needs — questions only confirm what you thought to ask; interview first → The Mom Test (Product Discovery), then survey to size what interviews surfaced
- Predicting behavior from stated intent ("would you pay for X?") — inflated several-fold; ask about last actual behavior
- Very small samples (n < ~30 per segment) — an interview study answers more per hour
- Fuzzy constructs — pretest or the numbers will be precise and meaningless

## Key Steps
1. Write the decision the survey informs and the hypotheses it tests (else the data has no consumer)
2. Operationalize each construct into concrete questions
3. Wording rules: one question at a time (no double-barreled), behavior over prediction ("last time" not "would you"), no loaded/leading phrasing, mutually exclusive exhaustive options
4. Order: easy engaging questions first, sensitive ones later, demographics last; randomize option order where viable
5. Choose scales deliberately (5/7-point Likert; NPS only where a benchmark exists)
6. Pilot with ~10-20 respondents; fix every comprehension break before fielding
7. Field to a defined sampling frame; monitor straight-lining and speeders
8. Analyze against the hypotheses; report response rate and sample composition with the findings

## Output Template

```
Decision informed: [what changes based on results]
Hypotheses: [H1..Hn with the question that tests each]
Question list: [text | type (behavior/attitude/screen) | construct | notes]
Scales: [per construct]
Sample frame + target n: [who, how reached, expected response rate]
Pilot findings: [comprehension breaks fixed]
Analysis plan: [cross-tabs per hypothesis, nonresponse caveats]
```

## Failure Modes
- Stated-intent questions: "would you use/pay for X" returns inflated enthusiasm → ask about the last real occurrence; treat intent answers as weak evidence, labeled as such
- Double-barreled and leading questions: "How much do you enjoy our fast, reliable app?" measures nothing identifiable → one construct per question, neutral wording
- Convenience sample read as market truth → weight, restrict claims, or label the bias in the output
- Survey-first discovery: fielding before interviews bakes your blind spots into the data → interviews generate the hypotheses, surveys quantify them
- No pilot: comprehension breaks discovered after 1,000 responses → pilot is not optional
- Nonresponse ignored: the 12% who answered differ from the 88% who didn't → report response rate and who is missing

## Evidence Strength
Practitioner consensus — wording, order, and mode effects are among the most replicated findings in survey methodology (Schuman & Presser's experiments); NPS's causal claims are contested; stated-intent inflation is well replicated across domains.

## Source
Howard Schuman & Stanley Presser, *Questions and Answers in Attitude Surveys* (1981); Floyd Fowler, *Survey Research Methods*; Fred Reichheld, "The One Number You Need to Grow" (2003, NPS). Admission verdict: **Build** (v0.1.12) — the category's methodologies consume research data but none designed the instrument that produces it.
