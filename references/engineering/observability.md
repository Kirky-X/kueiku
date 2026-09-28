# Observability

## Core Concept
Three pillars working together: Logs (discrete events), Metrics (aggregated measurements), Traces (request flow across services). SLO-driven alerting ensures you're alerted on user-impacting issues, not noise.

## Applicable Scenarios
✅ **Best for**
- Production incident investigation
- Distributed system tracing
- Capacity planning

⚠️ **When NOT to use**
- A single service with trivial traffic — structured logs plus one uptime check may be the honest ceiling; a tracing stack is overhead
- Debugging you can do locally with a debugger — production observability is for production behavior
- Collecting everything "just in case" — unbounded telemetry costs money and buries signal; instrument questions you actually need answered

## Key Steps
1. **Define SLOs**: what level of service do users expect? (e.g. 99.9% success rate, p99 < 200ms)
2. **Instrument**: add structured logging, metrics collection, distributed tracing
3. **Alert on SLOs**: alert when error budgets are being consumed, not on raw metrics
4. **Correlate**: link logs, metrics, and traces for fast incident investigation
5. **Review**: regular observability reviews to improve coverage

## Output Template

```
Service: [checkout-api]

SLOs: availability 99.9% (30d) | p99 latency < 300ms | — error budget: [x% remaining]
Alerts (SLO burn only): fast-burn [2%/1h → page], slow-burn [5%/24h → ticket]
  Explicitly NOT alerting: [CPU > 80% — no direct user impact proven]

Instrumentation:
  Metrics: [RED — rate/errors/duration per endpoint; saturation for queues]
  Logs: structured JSON, [trace_id on every line], sampled [x]
  Traces: [ propagated across services, tail-sampled for errors]

Incident drill: given [p99 spike alert], can an on-call reach the failing dependency in <5 min via trace → logs? [test it quarterly]
```

## Failure Modes
- Alert spam → numbness: raw-threshold alerts (CPU, memory) page on non-problems → alert only on SLO burn; if a page has no user impact, it's a dashboard, not an alert
- Pillars in silos: logs in one tool, metrics in another, traces nowhere — correlation by human memory → enforce trace IDs across all three; uncorrelated telemetry is three times the cost for a third of the value
- Dashboard sprawl: 40 dashboards nobody opens outside incidents → prune to the SLO view plus per-service RED; coverage reviews decide what earns its place

## Evidence Strength
Practitioner consensus — SRE practice with strong industrial adoption; the SLO/error-budget mechanism is operationally well proven at scale, while "three pillars" itself is contested in practice (tracing-centric approaches increasingly subsume logs/metrics). The alert-fatigue failure mode is extensively documented.

## Source
Google SRE methodology; Charity Majors et al., *Observability Engineering*.
