# Performance Optimization

## Core Concept
Measure → Locate → Optimize → Verify cycle. Bottleneck layering (CPU / Memory / I/O / Network). Anti-pattern warnings: don't optimize without measuring, don't guess bottlenecks.

## Applicable Scenarios
✅ **Best for**
- Performance troubleshooting
- Baseline establishment
- Resource cost optimization

## Key Steps
1. **Measure**: establish performance baseline with realistic load
2. **Locate**: profile to find the actual bottleneck (don't guess)
3. **Optimize**: address the bottleneck (layer: CPU → Memory → I/O → Network)
4. **Verify**: re-measure to confirm improvement; check for regressions
5. **Repeat**: find the next bottleneck; iterate

## Source
Performance engineering best practices; Brendan Gregg's systems performance methodology.
