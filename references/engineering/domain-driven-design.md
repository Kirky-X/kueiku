# Domain-Driven Design

## Core Concept
Model complex business systems using: Bounded Contexts (clear boundaries), Aggregate Roots (consistency boundaries), Ubiquitous Language (shared terminology), and Event Storming (collaborative discovery).

## Applicable Scenarios
✅ **Best for**
- Complex business system modeling
- Microservice boundary definition
- Aligning technical and business domains

⚠️ **When NOT to use**
- Simple domain, simple rules — DDD patterns on a CRUD app bury logic in ceremony
- The business experts can't be engaged (no access to domain owners) — the language work is the method; without it you're doing guesswork with extra patterns
- Teams new to the domain AND to DDD simultaneously — learning two unknowns at once fails for both

## Key Steps
1. **Event Storming**: gather domain experts; map domain events on a timeline
2. Identify Bounded Contexts: group related events and entities
3. Define Aggregate Roots: entities that ensure consistency within a context
4. Establish Ubiquitous Language: same terms in code, docs, and conversation
5. Define Context Maps: how bounded contexts interact

## Output Template

```
Domain: [e-commerce fulfillment]

Bounded contexts: [Ordering] [Inventory] [Shipping]
  Ordering: aggregate root [Order] — invariants: [total = Σ lines; cannot ship while unpaid]
    Ubiquitous terms: [Order, LineItem, PaymentConfirmed — one meaning, code+talk]
  Inventory: aggregate [StockItem] — invariant: [never negative]
Context map: Ordering →(OrderPlaced event)→ Inventory; Shipping ←(PaymentConfirmed)← Ordering

Event log (from storming): [OrderPlaced → PaymentConfirmed → StockReserved → Shipped]
Integration style per boundary: [events / shared kernel (avoid) / ACL]
Term-drift watchlist: ["customer" means X in Ordering, Y in Shipping → rename to distinct terms]
```

## Failure Modes
- DDD as class diagram: applying entities/repositories while skipping language and boundaries — the parts that carry the value → if no domain expert was in the room, it isn't DDD yet
- Wrong aggregate lines: aggregates too large (one root for the whole order+customer+inventory world) cause lock storms and transactional pain → draw aggregates around invariants, not around nouns
- Shared kernel creep: contexts drift back into one database/one model "temporarily" → integration only through published events or explicit contracts; model drift is the smell to surface, not hide

## Evidence Strength
Practitioner consensus with case-based support — strategic patterns (bounded contexts, ubiquitous language) are widely credited in complex-domain success stories, but controlled evidence is scarce and failures from over-application are common; best supported as a complexity-matching tool, weakest when applied to simple domains.

## Source
Eric Evans, *Domain-Driven Design* (2003).
