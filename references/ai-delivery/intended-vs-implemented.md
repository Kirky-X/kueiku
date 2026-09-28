# Intended vs Implemented

## Core Concept
A framework for detecting drift between documented intent and cited code implementation. Tracks bidirectional references: does the design doc reference the right code? Does the code cite the right design doc? Identifies boundary mismatches where scope has shifted.

## Applicable Scenarios
- Detecting doc-code drift in AI-era projects
- Ensuring design documents stay aligned with implementation
- Auditing specification coverage

⚠️ **When NOT to use**
- Documentation debt is total (no docs to compare against) — fix documentation first; there is nothing to align
- A one-shot review before merge — a checklist catches the same drift cheaper
- Regenerated/AI-written code without stable references — citation links churn every generation and produce false drift

## Key Steps
1. Extract documented intents from design docs (features, behaviors, constraints)
2. Map each intent to its corresponding code implementation (cited code)
3. Check bidirectional references: does code reference back to the intent?
4. Identify boundary mismatches: scope changes, missing implementations, orphaned docs
5. Create a drift report with severity and recommended actions

## Output Template

```
Scope: [design docs] × [code area] — audited [date]

| Intent (doc §ref)        | Implementation (path) | Forward link | Back link | Drift type        | Severity |
| ------------------------ | --------------------- | ------------ | --------- | ----------------- | -------- |
| [rate limit 100/min]     | [src/middleware/rl.go]| ✓            | ✗         | undocumented change (now 200) | High |
| [retry with backoff]     | —                     | —            | —         | unimplemented     | High     |
| —                        | [src/cache/etag.go]   | —            | ✗         | orphaned code     | Medium   |

Drift summary: [n mismatches / n intents, worst boundary: auth scope]
Actions: [update doc / file ticket / flag orphan] — owner [x] by [date]
```

## Failure Modes
- Snapshot audits that rot immediately: drift resumes the day after the report → make bidirectional citation a template habit (doc PRs cite code, code PRs cite docs), not a periodic audit
- Severity by feeling: everything marked Medium → tie severity to user impact or contract breakage, and force a top-3 ordering
- Treating doc as truth by default: sometimes the code is right and the doc is stale → each drift row must decide which side is authoritative before assigning action

## Evidence Strength
Practitioner consensus — drift between docs and code is a well-observed failure mode and citation hygiene is a reasonable control; no controlled studies quantify drift reduction from bidirectional referencing, and tooling support (doc-to-code link checkers) determines how much of it is enforceable vs manual.

## Source
AI delivery best practices; doc-code alignment frameworks.
