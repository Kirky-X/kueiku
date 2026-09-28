# Performance Optimization

## Core Concept
Measure → Locate → Optimize → Verify cycle. Bottleneck layering (CPU / Memory / I/O / Network). Anti-pattern warnings: don't optimize without measuring, don't guess bottlenecks.

## Applicable Scenarios
✅ **Best for**
- Performance troubleshooting
- Baseline establishment
- Resource cost optimization

⚠️ **When NOT to use**
- No measurable user or cost pain — optimizing without a symptom produces code churn and bugs, and usually optimizes cold paths
- One-shot scripts and prototype code — clarity outruns speed until the prototype proves its shape
- Premature micro-optimization during initial development — algorithm choice matters, cache-line tuning doesn't yet

## Key Steps
1. **Measure**: establish performance baseline with realistic load
2. **Locate**: profile to find the actual bottleneck (don't guess)
3. **Optimize**: address the bottleneck (layer: CPU → Memory → I/O → Network)
4. **Verify**: re-measure to confirm improvement; check for regressions
5. **Repeat**: find the next bottleneck; iterate

## Output Template

```
Symptom (user-visible): [p95 page load 2.8s, target <1s]
Baseline: [load profile: n rps, data volume, environment] — reproducible via [benchmark command]

Profile evidence: [flame chart / EXPLAIN / profiling output — the actual measurement]
Bottleneck located: [N+1 queries in order listing — 41 queries/request] — layer: I/O

Optimization applied: [batch fetch + join] — expected effect: [queries 41→2]
Verify: [p95 2.8s → 0.9s] — regression check: [full test suite + correctness spot-check on edge cases]
Guardrail added: [query-count assertion in integration test]
Next bottleneck: [or: target met, stop]
```

## Failure Modes
- Optimization by folklore: rewriting the hot function that profiling never flagged → no optimization starts without profile evidence; intuition proposes, profiler disposes
- Unverified wins: change merged on "should be faster", later found slower at real load → same benchmark, before and after, plus a regression check on correctness
- Benchmark theater: measuring a microbenchmark that doesn't represent production shape (data volume, concurrency) → baselines must match realistic load, or state clearly that they don't

## Evidence Strength
Strong for the cycle itself — measure-first optimization is foundational performance engineering practice, and the cost of guessing wrong is empirically well known (most intuitive hotspots aren't hot); specific heuristics (C10k-style rules, cache tuning folklore) age quickly, so lean on measurement over doctrine.

## Source
Performance engineering best practices; Brendan Gregg's systems performance methodology.
