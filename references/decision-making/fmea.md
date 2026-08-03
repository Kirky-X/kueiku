# FMEA — Failure Mode and Effects Analysis

## Core Concept
Systematic identification and ranking of potential failure modes using Severity × Occurrence × Detection = Risk Priority Number (RPN). Higher RPN = higher priority for mitigation.

## Applicable Scenarios
✅ **Best for**
- Product/process risk identification
- Quality engineering
- Safety-critical systems

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

## Source
Military standard MIL-P-1629 (1949); adopted by automotive (AIAG) and aerospace industries.
