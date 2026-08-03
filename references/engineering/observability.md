# Observability

## Core Concept
Three pillars working together: Logs (discrete events), Metrics (aggregated measurements), Traces (request flow across services). SLO-driven alerting ensures you're alerted on user-impacting issues, not noise.

## Applicable Scenarios
✅ **Best for**
- Production incident investigation
- Distributed system tracing
- Capacity planning

## Key Steps
1. **Define SLOs**: what level of service do users expect? (e.g. 99.9% success rate, p99 < 200ms)
2. **Instrument**: add structured logging, metrics collection, distributed tracing
3. **Alert on SLOs**: alert when error budgets are being consumed, not on raw metrics
4. **Correlate**: link logs, metrics, and traces for fast incident investigation
5. **Review**: regular observability reviews to improve coverage

## Source
Google SRE methodology; Charity Majors et al., *Observability Engineering*.
