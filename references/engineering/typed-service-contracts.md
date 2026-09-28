# Typed Service Contracts

## Core Concept
Design service boundaries using: Spec & Handler pattern + Design by Contract (pre/post conditions) + Result Monad (no exceptions) + Parse don't validate (type-safe data). Creates compile-time guarantees at service boundaries.

## Applicable Scenarios
✅ **Best for**
- Service boundary contract design
- Boundary error defense
- API design between services

⚠️ **When NOT to use**
- Rapid prototyping where shapes change daily — type ceremony slows the exploration it should serve; introduce contracts when shapes stabilize
- Scripts and glue code inside one trust boundary — internal helpers with known-good inputs don't need boundary parsing
- As a substitute for runtime contract tests — types prove shape, not behavior; cross-service compatibility still needs tests

## Key Steps
1. Define the service interface as a typed Spec (input/output types)
2. Add pre-conditions (what must be true before calling) and post-conditions (what is guaranteed after)
3. Use Result types instead of exceptions for error handling
4. Parse input data into typed structures at the boundary (Parse don't validate)
5. Implement the Handler that satisfies the Spec

## Output Template

```
Spec: CreateOrder
  Input  (parsed once at boundary): { user_id: UserId (validated), items: NonEmptyVec<LineItem>, coupon?: CouponCode }
  Output (Result): Ok(OrderConfirmed) | Err(OutOfStock(sku)) | Err(PaymentDeclined(reason)) | Err(InvalidCoupon(code))

Pre-conditions: [caller authenticated; idempotency key provided]
Post-conditions: [order persisted exactly once; event OrderPlaced published]

Parse don't validate:
  raw JSON → parse into typed structs at the edge (fail fast with field-level errors)
  inside the handler: no re-checking, types guarantee shape — business checks return typed Err only

Handler satisfies Spec — compiler enforces: all Err variants handled by caller; no silent exceptions
Contract test: [spec examples covering each Err variant, run against both sides of the boundary]
```

## Failure Modes
- Boolean blindness: validate() returning bool then re-parsing downstream — the check and the use live in different worlds → parse into types that make invalid states unrepresentable; validation without construction is theater
- Exception leaks across the boundary: "typed contract" that still throws deep inside — every throw is an untyped error path → map all internal errors to the Result at the edge
- Contract rot: Spec updated, handler drifts, callers crash at runtime → Spec and Handler in one compiled unit, plus contract tests in CI; a stale contract is worse than none

## Evidence Strength
Practitioner consensus — the underlying ideas (Design by Contract, algebraic error types, parse-don't-validate) are well argued and widely adopted in type-rich ecosystems; evidence of defect reduction comes mostly from practitioner experience and language-level studies, not controlled trials, and payoff shrinks for small or rapidly churning boundaries.

## Source
Functional programming patterns; Design by Contract (Bertrand Meyer); Parse don't validate (Alexis King).
