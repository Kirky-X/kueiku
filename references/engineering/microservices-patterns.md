# Microservices Patterns

## Core Concept
Distributed system patterns: Saga (distributed transactions), CQRS (command-query separation), Event Sourcing (state as event log), plus service governance and resilience patterns.

## Applicable Scenarios
✅ **Best for**
- Monolith decomposition
- Distributed data consistency
- Service governance

## Key Steps
1. Identify service boundaries (use DDD bounded contexts)
2. Choose data consistency pattern: Saga (choreography or orchestration) for distributed transactions
3. Apply CQRS: separate read and write models where query patterns differ from write patterns
4. Consider Event Sourcing: store state changes as events for full audit trail
5. Implement resilience patterns: circuit breaker, retry, bulkhead, fallback
6. Set up service governance: service discovery, API gateway, health checks

## Source
Chris Richardson, *Microservices Patterns* (2018).
