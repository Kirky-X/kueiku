# Typed Service Contracts

## Core Concept
Design service boundaries using: Spec & Handler pattern + Design by Contract (pre/post conditions) + Result Monad (no exceptions) + Parse don't validate (type-safe data). Creates compile-time guarantees at service boundaries.

## Applicable Scenarios
✅ **Best for**
- Service boundary contract design
- Boundary error defense
- API design between services

## Key Steps
1. Define the service interface as a typed Spec (input/output types)
2. Add pre-conditions (what must be true before calling) and post-conditions (what is guaranteed after)
3. Use Result types instead of exceptions for error handling
4. Parse input data into typed structures at the boundary (Parse don't validate)
5. Implement the Handler that satisfies the Spec

## Source
Functional programming patterns; Design by Contract (Bertrand Meyer); Parse don't validate (Alexis King).
