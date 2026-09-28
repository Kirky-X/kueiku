# Risk Matrix

## Core Concept
Quick 2-dimensional risk assessment using Probability × Impact. Plot identified risks on a grid to visually classify and prioritize them into zones: Critical, High, Medium, Low.

## Applicable Scenarios
✅ **Best for**
- Project kickoff risk screening
- Strategic planning risk scan
- Technology selection risk comparison

⚠️ **When NOT to use**
- Risks need quantitative treatment (expected loss in dollars) — a 3×3 grid cannot sum exposures; use FMEA or Monte Carlo for financial decisions
- Probability estimates have no basis (novel one-shot projects) — the plot implies precision nobody has
- Safety-critical domains with mandated methods — use the prescribed standard; the matrix is a screening tool, not a compliance artifact

## Key Steps
1. List all identified risks
2. For each risk, assess Probability (1-5 scale) and Impact (1-5 scale)
3. Plot on the Probability × Impact matrix
4. Classify into zones: Critical (high P + high I), High, Medium, Low
5. Develop response strategies: Critical = avoid/transfer; High = mitigate; Medium = monitor; Low = accept

## Output Template

```
Risk register (scoring anchors declared up front: what a 2 vs 4 impact means in $/time/scope)

| # | Risk                          | P | I | Zone     | Response            | Owner | Trigger/review   |
| --- | --------------------------- | - | - | -------- | ------------------- | ----- | ---------------- |
| 1  | [key vendor folds]           | 2 | 5 | High     | [dual-source now]   | [x]   | [monthly]        |
| 2  | [migration data loss]        | 3 | 5 | Critical | [avoid: dry runs + backup restore test] | [x] | [before cutover] |
| 3  | [minor UI regression]        | 4 | 1 | Low      | [accept]            | —     | —                |

Zone summary: [n critical / n high] — criticals must carry avoid/transfer plans, not just mitigation intent
Residual risk after responses: [re-plot post-mitigation? at least for criticals]
```

## Failure Modes
- Unanchored scales: everyone's "3" means something different, zones become noise → publish concrete anchors ("impact 4 = >$100k or >2wk slip") before scoring
- Probability by vibes for novel risks: anchoring on imagination, not base rates → demand a reference class ("similar migrations failed X% of the time") or mark the estimate low-confidence
- Mitigation theater: critical risks get "monitor" — the response contradicts the zone → each zone maps to an allowed response set; criticals must show avoid/transfer/mitigate with owner and trigger

## Evidence Strength
Practitioner consensus — the standard PMBOK-era screening device; useful for shared visualization, but research on risk matrices documents systematic weaknesses (category compression, poor discrimination between risks, false precision) — treat zone boundaries as conventions and keep quantitative analysis for stakes that justify it.

## Source
Standard project risk management; PMI PMBOK methodology.
