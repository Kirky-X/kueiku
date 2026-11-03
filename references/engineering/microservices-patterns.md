# Microservices Patterns

## Core Concept
Distributed system patterns: Saga (distributed transactions), CQRS (command-query separation), Event Sourcing (state as event log), plus service governance and resilience patterns.

## Applicable Scenarios
✅ **Best for**
- Monolith decomposition
- Distributed data consistency
- Service governance

⚠️ **When NOT to use**
- One team, one deployable, modest traffic → splitting adds network failure modes, distributed data, and coordination cost with no scaling payoff; keep the monolith until a measured constraint forces the split
- Boundaries are not understood yet → **Domain-Driven Design** (bounded contexts, event storming) has to come first, because patterns applied to arbitrary seams encode the wrong decomposition
- The problem is structure inside a single service — layers, coupling, big functions → **Clean Architecture** or **Refactoring Patterns** address that without adding a network hop
- The real constraint is throughput at one stage → **Theory of Constraints** locates the binding stage first, because distributing a flow does not raise its total throughput

## Key Steps
1. Identify service boundaries (use DDD bounded contexts)
2. Choose data consistency pattern: Saga (choreography or orchestration) for distributed transactions
3. Apply CQRS: separate read and write models where query patterns differ from write patterns
4. Consider Event Sourcing: store state changes as events for full audit trail
5. Implement resilience patterns: circuit breaker, retry, bulkhead, fallback
6. Set up service governance: service discovery, API gateway, health checks

## Output Template

```
Decomposition:
  Service: [name] — bounded context: [context] — owner team: [team] — data owned: [store/tables]
  Depends on: [service] via [sync call | event]
  Why this is a separate service: [scale | ownership | release independence]

Consistency pattern: [Saga (orchestration) | Saga (choreography) | CQRS | Event Sourcing | none]
  Why: [the specific failure it prevents]
  Steps: [S1 → S2 → S3]   compensation per step: [undo S1]   timeout per step: [x s]
  Event contract: [name, version, schema owner, compatibility rule]
  Projection: [read model, rebuild procedure, tolerated lag]

Resilience per remote hop:
  timeout [x s] | retry [max n, backoff] | circuit breaker [opens after n failures] | bulkhead [pool size] | fallback [behavior]
  Retry safety: [idempotent | not idempotent — how duplicates are handled]

Governance:
  discovery: [mechanism]   gateway: [routing, auth, rate limit]   health: [liveness / readiness endpoints]
  Contract enforcement: [schema validation | consumer-driven tests] — CI gate
  Cross-cutting: [tracing, correlation ids, audit log] — owned by [platform]
```

## Failure Modes
- Pattern shopping: Saga, CQRS, and Event Sourcing adopted together for a simple CRUD domain → each pattern adds operational surface (saga state, projection rebuilds, event versioning) with no payback; adopt one pattern against a named pain or none
- No owning team per service → nobody owns a service's on-call, lifecycle, or schema, so it decays → assign an owning team at decomposition time; an unowned service is a liability
- Event Sourcing without versioning discipline → every producer change breaks consumers → version events, keep readers backward-compatible, and rehearse projection rebuilds before you need them
- Distributed transactions reimplemented as ad-hoc compensations scattered through application code → partial failures leave unrecoverable states → use an orchestrated Saga where each step's compensation is written next to the step itself
- Remote calls treated as local calls inside a request path → latency multiplies and failures cascade → give every hop a timeout, a retry budget, a circuit breaker, and a bulkhead; a remote call without a failure budget is an outage waiting for traffic

## Evidence Strength
Mixed — the individual patterns are precisely specified in practitioner literature and their failure modes are well documented, but comparative evidence that microservice adoption improves delivery speed, reliability, or cost is mixed and frequently points the other way for small systems; the organizational premises behind the pattern set remain contested, and the claimed benefits are usually realized only where service ownership, platform capability, and operational maturity already exist.

## Source
Chris Richardson, *Microservices Patterns* (2018).
