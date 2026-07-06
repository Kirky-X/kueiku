# Intended vs Implemented

## Core idea
Code drift is the most insidious risk in the AI collaboration era—docs say do A, code actually does B, and nobody notices until an incident. This framework requires every critical decision point to have "documented intent ↔ cited code evidence" bidirectional referencing, and explicit mismatch marking for cross-module/cross-boundary deviations.

## Use cases
- AI agents make extensive code changes that humans can't review line-by-line
- Docs and code are out of sync for extended periods; new team members get misled by reading docs
- Cross-team interfaces frequently have "I thought you implemented that" discrepancies

## Key steps
1. In every Design Doc / Spec, annotate intent: explicitly state "we decided this because..."
2. In code comments, back-reference the doc: `// implements: design.md#section-3.2`
3. CI auto-checks: every referenced code segment must exist and match the interface signature described in the doc
4. Explicit mismatch marking for cross-module/cross-service boundaries:
   - Doc says synchronous call, code switched to async—must be explicitly annotated and dependent parties notified
   - Doc says returns Result, code panics—CI alerts
5. Periodic (monthly) intent↔code bidirectional audit, output mismatch list
6. Mismatch is not necessarily a bug, but must be explicitly decided: revise doc / revise code / mark as known deviation

## Source
Product Compass (Intended vs Implemented framework)
