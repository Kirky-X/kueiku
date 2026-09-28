# MECE + Pyramid Principle

## Core Concept
MECE (Mutually Exclusive, Collectively Exhaustive) for structuring analysis; Pyramid Principle for structuring communication — lead with the conclusion, then support with arguments and data.

## Applicable Scenarios
✅ **Best for**
- Consulting reports
- Complex problem decomposition
- Executive reporting

⚠️ **When NOT to use**
- Genuinely overlapping systems — forcing MECE on interdependent causes creates false separation; use systems thinking when boundaries don't exist
- Chronological/narrative communication (incident timelines, user stories) — conclusion-first works for decisions, not for stories that build understanding
- Exploratory analysis before the structure is known — MECE is for organizing findings; premature structure pre-decides what you'll find

## Key Steps
1. Start with the answer/conclusion (Pyramid top)
2. Support with 3-5 key arguments (Pyramid middle)
3. Support each argument with data/evidence (Pyramid base)
4. Validate MECE: are the arguments mutually exclusive? Collectively exhaustive?
5. Iterate: if not MECE, restructure until clean

## Output Template

```
Conclusion (the answer, first sentence): [we should do X because of Y]

Key arguments (MECE check on this layer):
  1. [Market: demand is shifting — data: ...]
  2. [Capability: we can execute — data: ...]
  3. [Economics: returns clear the bar — data: ...]
  MECE check: any overlap between arguments? [no — state why] any missing dimension that could overturn the conclusion? [no — state why]

Support layer: each argument carries [evidence + source], not assertions
Counterweight (the strongest counterargument, answered): [...]
One-sentence test: can a listener repeat the conclusion + 3 arguments after one pass? [test it]
```

## Failure Modes
- Fake MECE: "people / process / technology" buckets where the same root cause sits in all three → test overlap with a real case: if one fact lands in two buckets, the cut is wrong; re-cut by the question you're answering
- Pyramid built top-down from a preferred answer: conclusion first becomes conclusion only, evidence reverse-engineered → write the evidence layer and check it still supports the top before communicating; if it doesn't, the top changes
- Over-branched pyramids: 7 arguments, 5 sub-arguments each — nobody retains it → 3-5 arguments max per layer; the discipline is cutting, not enumerating

## Evidence Strength
Practitioner consensus — the communication benefits of conclusion-first structure are consistently supported by practitioner experience and by cognitive-load reasoning (audiences retain hierarchies better than lists); MECE as an analysis-standard is more contested (real-world causation is often non-exclusive), and its rigidity is a known failure mode.

## Source
Barbara Minto, *The Minto Pyramid Principle* (1987); McKinsey consulting methodology.
