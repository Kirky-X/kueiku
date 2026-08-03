# Domain-Driven Design

## Core Concept
Model complex business systems using: Bounded Contexts (clear boundaries), Aggregate Roots (consistency boundaries), Ubiquitous Language (shared terminology), and Event Storming (collaborative discovery).

## Applicable Scenarios
✅ **Best for**
- Complex business system modeling
- Microservice boundary definition
- Aligning technical and business domains

## Key Steps
1. **Event Storming**: gather domain experts; map domain events on a timeline
2. Identify Bounded Contexts: group related events and entities
3. Define Aggregate Roots: entities that ensure consistency within a context
4. Establish Ubiquitous Language: same terms in code, docs, and conversation
5. Define Context Maps: how bounded contexts interact

## Source
Eric Evans, *Domain-Driven Design* (2003).
