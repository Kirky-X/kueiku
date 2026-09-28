# Fishbone / Ishikawa Diagram

## Core Concept
A fishbone (cause-and-effect) diagram systematically categorizes potential causes of a problem across multiple dimensions, helping teams visualize the full landscape of contributing factors rather than fixating on the first plausible cause.

## Applicable Scenarios
- Quality issues with multiple potential contributing factors
- Team brainstorming sessions for root cause identification
- When 5 Whys alone is insufficient due to multi-factor causation

⚠️ **When NOT to use**
- A single dominant cause chain — 5 Whys drills faster; a fishbone spends structure on breadth you don't need
- No domain knowledge in the room — the diagram organizes candidate causes but can't invent them; expertise is the input
- Data-driven prioritization is the actual task — the fishbone generates hypotheses; Pareto or measurement ranks them

## Key Steps
1. Write the problem statement at the "head" of the fish
2. Define major cause categories (common: 6M for manufacturing — Man/Machine/Material/Method/Measurement/Mother Nature; or 4P for services — Policies/Procedures/People/Plant)
3. Brainstorm potential causes within each category
4. For each potential cause, ask "why" to drill deeper (combine with 5 Whys)
5. Validate causes with data; prioritize the most likely root causes

## Output Template

```
Problem (head): [specific, measurable effect]

  Man        — [operator skip]        → why: [no checklist]
  Machine    — [calibration drift]    → why: [schedule not enforced]
  Method     — [manual data entry]    → why: [no barcode integration]
  Material   — [supplier lot variance]→ why: [no incoming inspection]
  Measurement— [gauge worn]           → why: [no calibration log]
  Environment— [humidity swings]      → why: [HVAC fault]

Prioritized causes (validated with data): 1. [gauge worn — measured] 2. [...]
Actions per confirmed cause: [owner + fix + verification]
```

## Failure Modes
- Brainstorm-only fishbone: a full diagram of opinions where every bone has three sticky notes and nothing is measured → every candidate cause gets a validation plan before the session ends; the output is hypotheses, not conclusions
- Category bias: the 6M template imports causes from manufacturing into software (or wherever it doesn't fit) → pick categories that match the domain (people/process/technology/external) rather than forcing 6M
- Fish freeze: an elaborate diagram from last year still hanging on the wall → date it and re-draw per incident; stale bones hide new causes

## Evidence Strength
Practitioner consensus — a core quality-management tool since the 1960s; its value is exhaustive hypothesis generation (documented failure mode of narrower methods is early fixation), while the diagram itself makes no causal claim — validation is always external.

## Source
Kaoru Ishikawa (1960s); quality management tool.
