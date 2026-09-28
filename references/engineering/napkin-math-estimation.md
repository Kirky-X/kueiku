# Back-of-Envelope Estimation

## Core Concept
Estimate performance and cost from first principles before building: Fermi-decompose the question until each factor maps to a known hardware constant, then multiply. Work in `c × 10^e` — the target is the exponent `e` (right order of magnitude); the coefficient matters far less. Keep units through every step; they are a free checksum. This is the design-time twin of Performance Optimization, which measures the running system instead.

## Applicable Scenarios
✅ **Best for**
- Capacity / QPS / storage / cost feasibility before committing to an architecture
- Sanity-checking a design proposal or infrastructure quote in minutes

⚠️ **When NOT to use**
- A running system exists — measure it (Performance Optimization)
- The answer must be precise (billing, contracts) — estimation bounds the problem, measurement decides it

## Key Steps
1. **Fermi-decompose**: break the question into factors you can guess at (log line size, requests/sec, $/GB) until each maps to a constant below.
2. **Pin the exponent first**: compute in `c × 10^e`; refine `c` only when the decision is close.
3. **Multiply with constants**, units attached; >6 assumptions means over-decomposed — collapse and re-estimate.
4. **State the verdict as magnitude + margin**: "about 10^3, could be 3× off" — not false precision.

## Reference Constants
Rounded for memorization — magnitudes, not precision; throughput/latency pairs are intentionally smoothed for arithmetic. Rows reference commodity cloud hosts (upstream suite re-measured 2026-03-08 on a GCP `c4-standard-48-lssd`-class node). **Numbers go stale — re-measure any row a critical decision hinges on.**

| Operation | Latency | Throughput |
| --- | --- | --- |
| Sequential memory access (64 B) | 0.5 ns | ~20 GiB/s per core, ~200 GiB/s threaded |
| Random memory access (64 B) | 20 ns | ~3 GiB/s |
| Hash, non-crypto (64 B) | 10 ns | ~5 GiB/s |
| System call | ~300 ns | — |
| Sequential SSD read (8 KiB) | 1 µs | ~8 GiB/s |
| Sequential SSD write, no fsync (8 KiB) | 2 µs | ~3 GiB/s |
| Context switch | ~10 µs | — |
| Random SSD read (8 KiB) | ~100 µs | ~70 MiB/s |
| Sequential SSD write, fsync (8 KiB) | ~300 µs | ~30 MiB/s |
| Redis / Memcached-class query | ~500 µs | — |
| Network, same zone | ~100 µs | ~10 GiB/s |
| Network, cross-AZ same region | ~250 µs | ~2 GiB/s |
| Network, cross-region | 25–180 ms RTT | ~25 MiB/s |
| Blob storage GET (single stream) | ~80 ms | ~100 MiB/s |
| Random HDD read (8 KiB) | ~10 ms | <1 MiB/s |

| Cost item (cloud ballpark) | ~$ / month |
| --- | --- |
| vCPU core | $15 |
| RAM | $2 / GB |
| Blob / object storage | $0.02 / GB |
| Logs & traces (ingest-class) | $0.5 / GB |
| Internet egress | $0.1 / GB |

## Output Template

```
Q: can one 8-vCPU server handle 5,000 RPS of 8 KiB cached responses?
  egress: 5,000 × 8 KiB ≈ 39 MiB/s ≈ 0.04 GiB/s → 3 orders below ~10 GiB/s NIC
  CPU: 4 syscalls (1.2 µs) + serialize 8 KiB (~8 µs) + app logic (~20 µs) ≈ 30 µs/req
       → 5,000 × 30 µs = 0.15 core
  verdict: yes, ~2 orders of headroom (margin 3×); real limits = connections, tail latency
           → measure those live before loading (Performance Optimization)

Q: cost of 2,000 log lines/s × 1 KiB for 30 days?
  ~1.9 MiB/s → ~165 GiB/day → ~5 TiB/mo × $0.5/GB ≈ $2,500/mo
  levers: compress text 2–4× → ~$600–1,200; sample 10% → ~$60–120
  verdict: TiB-scale ingestion is a real cost lever — set sampling policy before shipping
```

## Failure Modes
- Faux precision: "1,347 RPS" from 9 stacked assumptions → keep ≤6 factors, report magnitude + margin
- Dropped units: ns × MiB landing on a nonsense exponent — units that don't cancel mean a factor is missing
- Stale constants: re-measure rows a critical decision depends on
- Estimating what you can measure: once a system exists, a 5-minute benchmark beats an hour of napkin math

## Evidence Strength
Strong for the technique — Fermi decomposition and order-of-magnitude reasoning are standard capacity-planning practice, and being 2–3× off is harmless because the exponent drives the decision. The constant table is hardware- and date-bound folklore: a prior to verify, not a law.

## Source
Fermi estimation technique; Sirupsen's napkin-math project (numbers table re-measured 2026-03-08, GCP c4-standard-48-lssd).
Provenance: framework ideas absorbed from [napkin-math](https://github.com/sirupsen/napkin-math) (MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns design-time order-of-magnitude estimation; Performance Optimization measures a running system, and no existing entry covered sizing before build.
