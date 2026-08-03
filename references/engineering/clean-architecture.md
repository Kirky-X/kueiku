# Clean Architecture

## Core Concept
Dependency inversion layering + Port & Adapter pattern + domain layer with zero external dependencies. The core business logic depends on nothing; everything else depends on the core.

## Applicable Scenarios
✅ **Best for**
- New project architecture design
- Framework/database replacement
- Long-term maintainability

## Key Steps
1. Identify the domain entities and business rules (core)
2. Define ports (interfaces) for external interactions
3. Implement adapters that connect external systems to ports
4. Enforce dependency rule: dependencies point inward (toward domain)
5. The domain layer must not import any framework, database, or UI code

## Source
Robert C. Martin, *Clean Architecture* (2017).
