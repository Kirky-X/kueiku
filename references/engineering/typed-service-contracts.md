# Typed Service Contracts · Typed Service Contracts

## Core Idea
Don't rely on "conventions + documentation" at service boundaries — use the Spec & Handler pattern to make contracts executable code; use Design by Contract to express preconditions/postconditions; use Result Monad instead of throwing exceptions; use Parse don't validate to make illegal states unrepresentable at compile time. Move error defense from runtime to the type layer.

## Use Cases
- Microservices/module interfaces frequently fail because "the other side changed a field and I wasn't notified"
- Excessive runtime `if (data == null)` defensive code
- Exceptions abused as control flow, with callers unable to statically know when failures occur

## Key Steps
1. Spec & Handler pattern: Split each service call into Spec (type describing input/output/constraints) + Handler (function implementing the Spec). Spec is the single source of truth for the contract.
2. Design by Contract: Explicitly declare preconditions (pre) / postconditions (post) / invariants (inv) in the Spec; CI checks whether the handler satisfies them.
3. Result Monad: Use `Result<T, E>` instead of throw, making "may fail" explicit in the type signature, forcing callers to handle it.
4. Parse don't validate: Parse input into strong types once at the boundary; internal code no longer does null/format checks — illegal data is rejected at the boundary.
5. Contract versioning: Spec changes require a version bump; old versions are retained for N release cycles.
6. Auto-generated documentation and client SDK: Derived from Spec, eliminating documentation-code drift.

## Source
design.md (typed-service-contracts design pattern summary); theoretical foundation in Bertrand Meyer's *Object-Oriented Software Construction* (Design by Contract) and Alexis King's "Parse, don't validate"
