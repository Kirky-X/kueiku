# Clean Architecture

## Core Concept
Dependency inversion layering + Port & Adapter pattern + domain layer with zero external dependencies. The core business logic depends on nothing; everything else depends on the core.

## Applicable Scenarios
✅ **Best for**
- New project architecture design
- Framework/database replacement
- Long-term maintainability

⚠️ **When NOT to use**
- CRUD apps with logic too thin to justify a domain layer — the indirection cost exceeds the replaceability benefit
- Small teams/short-lived services — the structure tax is paid every day; the swap benefit may never arrive
- When the "domain" is actually a thin skin over someone else's API — there are no business rules to protect

## Key Steps
1. Identify the domain entities and business rules (core)
2. Define ports (interfaces) for external interactions
3. Implement adapters that connect external systems to ports
4. Enforce dependency rule: dependencies point inward (toward domain)
5. The domain layer must not import any framework, database, or UI code

## Output Template

```
layers/
  domain/        # entities, business rules — zero external imports (enforce in CI: import-linter)
    order.py     # Order, PriceCalculator
  ports/         # interfaces the domain needs, owned by the domain side
    order_repo.py      # OrderRepo (abstract)
    payment_gateway.py # PaymentGateway (abstract)
  adapters/      # implementations of ports, pointing inward
    postgres_order_repo.py
    stripe_gateway.py
  app/           # composition root + framework glue

Dependency check: domain imports nothing from adapters/app/frameworks — violation fails build
Business rule example (lives in domain): [an order with >50 items gets 5% discount] — testable with zero mocks of frameworks
```

## Failure Modes
- Anemic domain, fat use-cases: the "domain" holds data classes while all logic sits in application services — inversion without benefit → push actual business rules into the core or admit the app doesn't need this architecture
- Ports sprawl: an interface per repository per future swap that never happens → add ports where change is plausible (payments), skip them for stable infrastructure
- Mock cascade in tests: every test mocks six adapters to reach one rule → tests for domain rules should construct domain objects directly; if they can't, logic has leaked outward

## Evidence Strength
Practitioner consensus — dependency inversion itself is a well-established design principle with strong practitioner adoption; comparative evidence that layered architectures outperform simpler ones on delivery speed is actually mixed (some studies associate extra indirection with slower early delivery), so the payoff claim rests on lifecycle length and change patterns, not on universal superiority.

## Source
Robert C. Martin, *Clean Architecture* (2017).
