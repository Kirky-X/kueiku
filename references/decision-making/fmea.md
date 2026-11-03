# FMEA — Failure Mode and Effects Analysis

## Core Concept
Systematic identification and ranking of potential failure modes using Severity × Occurrence × Detection = Risk Priority Number (RPN). Higher RPN = higher priority for mitigation.

## Applicable Scenarios
✅ **Best for**
- Product/process risk identification
- Quality engineering
- Safety-critical systems

⚠️ **When NOT to use**
- The question is top-down deductive ("what could cause THIS top event?") → Fault-Tree Recipe below; FMEA is bottom-up inductive per component
- Conceptual design with no component decomposition yet → Pre-mortem is faster and catches design-level blind spots
- Failure modes dominated by human/organizational factors, where S×O×D becomes false numerics → qualitative scan (Risk Matrix)
- Fast-moving software failure surfaces: a static RPN ages in weeks → incident-response data (observability) supersedes the worksheet

## Key Steps
1. Decompose the system/process into components/steps
2. For each component, identify potential failure modes
3. For each failure mode, score: Severity (1-10), Occurrence (1-10), Detection (1-10)
4. Calculate RPN = S × O × D
5. Sort by RPN descending
6. Develop mitigation actions for top RPNs
7. Re-score after mitigation to verify risk reduction

## Output Template
```
FMEA Results:
| Component | Failure Mode | S | O | D | RPN | Action |
|-----------|-------------|---|---|---|-----|--------|
| Auth      | Token leak   | 9 | 4 | 6 | 216 | Encrypt + rotate |
| API       | Timeout      | 6 | 5 | 3 | 90  | Circuit breaker |

Risk Classification:
  Critical (RPN ≥ 200): [...]
  High (100-199): [...]
  Medium (50-99): [...]
  Low (< 50): [...]
```

## Failure Modes
- RPN theater: multiplying three invented numbers and sorting the product → treat RPN as an ordering heuristic; severity ≥ 9 goes to the top regardless of the product
- Decomposing by code structure instead of function → failure modes live in functions; a component map without functions misses them
- Detection scored on hope ("tests will catch it") → score by current evidence of what detection actually catches
- One-and-done worksheet: no re-score after mitigation → the loop closes nothing; schedule the re-score with the action

## Fault-Tree Recipe (cross-reference)

Top-down deductive twin: start from a named top event and enumerate the AND/OR combinations that reach it — **Fault Tree Analysis** (IEC 61025). Use FTA when one specific failure demands causal decomposition; use FMEA to sweep components for what could fail. This entry holds the pointer, not a duplicate method.

**Admission verdict** (v0.1.13, corrected v0.1.15): Fault Tree Analysis reviewed → Recipe, because it complements rather than duplicates FMEA's question, and a separate card would split one bottom-up/top-down pairing across two files. **Corrected**: the Recipe verdict assumed another entry held FTA — none did, so this pointer was a dead route. FTA is now its own entry (`fault-tree-analysis.md`); the pointer stays, and the bottom-up/top-down pairing is documented in one place.

## Evidence Strength
**Practitioner consensus in its industries, heuristic arithmetic.** FMEA is standard in automotive (AIAG-VDA), aerospace, and medical devices with decades of institutional use; the RPN product itself is criticized (ordinal scales multiplied as if cardinal) — use rankings, not the absolute number.

## Source
Military standard MIL-P-1629 (1949); adopted by automotive (AIAG) and aerospace industries. Fault-Tree Recipe pointer added v0.1.13.
