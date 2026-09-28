# Pretotypes

## Core Concept
Before writing a single line of code, validate "should we build this?" (Right It) in the cheapest way possible, not "did we build it right?". Through XYZ hypotheses + lightweight pretotype experiments, filter out doomed ideas before investing in engineering.

## Applicable Scenarios
- New idea is still at "I think users would want this" stage
- High engineering cost, need to validate demand existence before development
- Multiple candidate ideas, need quick screening

⚠️ **When NOT to use**
- The cost to build the real thing is trivial — pretotyping overhead exceeds just shipping behind a flag
- The idea's risk is technical feasibility, not demand — build a spike, not a landing page
- Measurable brand/UX damage from fake-door tests on existing paying users — gate by audience

## Key Steps
1. Write XYZ hypothesis: X% of target users in Y context will Z behavior
2. Choose pretotype type: Landing Page for traffic / Video for clicks / Pre-order for payment willingness / Concierge MVP manual service for real usage
3. Add Skin-in-the-Game signals: let users invest time/email/money/data, not just say "I'd want it"
4. Set success threshold in advance (e.g. CTR ≥ 5%), abandon if not met, avoid post-hoc rationalization
5. Only proceed to real prototype/engineering after passing

## Output Template

```
XYZ hypothesis: [15]% of [solopreneurs] in [invoicing context] will [pre-order at $9/mo]

Pretotype: [pre-order page] — skin-in-the-game: [email + card hold]
Audience source: [n reachable via channel C] — sample size justification: [why n detects the threshold]
Success threshold (set BEFORE launch): [≥8% pre-order rate] — below: [abandon/pivot note]
Result: [x% at n=…] — decision: proceed / abandon / reframe
What we actually learned: [demand signal vs click-quality caveat — did converters match target segment?]
```

## Failure Modes
- Threshold written after results: "5% is actually good for this channel" — the post-hoc rationalization the method exists to kill → thresholds and sample sizes committed in writing before traffic
- Testing appetite, not demand: clickers who never convert → skin-in-the-game signals only; opinion-level signals (likes, "interesting!") don't count
- Wrong crowd: paid clicks from lookalike audiences validating demand of the real segment → check converter profile against the target before declaring victory

## Evidence Strength
Practitioner consensus — grounded in the standard logic of cheap falsification and revealed preference; Savoia's catalog is anecdote-driven, and pretotype results (especially landing-page conversion) are known to over- or under-state true demand depending on channel quality, so treat a pass as a license to build a smaller next test, not as proof.

## Source
Alberto Savoia, *The Right It* (2019)
