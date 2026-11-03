# Team Topologies

## Core Concept
Organizational architecture constrains system architecture (Conway's Law), so design team boundaries deliberately instead of inheriting them. Four team types — stream-aligned, platform, enabling, complicated-subsystem — and three interaction modes — collaboration, X-as-a-Service, facilitating — make the structure explicit; cognitive load is the binding constraint that limits what any team can own.

## Applicable Scenarios
✅ **Best for**
- Structuring or restructuring delivery organizations around domain boundaries
- Deciding platform-vs-product team splits and what "platform" actually owes its users
- Diagnosing dependency hell: too many teams waiting on too many other teams
- Aligning team boundaries with software boundaries (pairs with Domain-Driven Design (Engineering))

⚠️ **When NOT to use**
- One team is the whole org — applying four team types to five people is taxonomy cosplay; grow first
- The real problem is individual capability or hiring → A-Player Density
- Reorganizing as a reflex response to friction, without a flow diagnosis → diagnose with flow metrics first
- Strategy is the actual problem; structure cannot fix direction → Strategy Red Team (Execution) first

## Key Steps
1. Map current state: every team's type, scope, self-assessed cognitive load, and actual interaction modes
2. Define intended domain boundaries (with bounded contexts where software is involved)
3. Assign each team a type; flag scope that overloads any team (load is the constraint, not headcount)
4. Choose the interaction mode per team pair; convert chaotic collaboration into X-as-a-Service where the service is stable
5. Set team lifespan expectations: stream-aligned teams are long-lived; their scope changes, the team persists
6. Evolve on a cadence: re-assess when scale, ownership, or load shifts; measure flow (dependency count, wait time, cross-team tickets)

## Output Template

```
Current team map: [team | type | scope | load (low/medium/high) | actual interactions]
Target topology: [team | type | scope | interactions (mode per pair)]
Cognitive load findings: [overloaded teams + what moves off]
Transition steps: [sequence, what changes per step, who is affected]
Flow metrics baseline + target: [cross-team dependencies, wait time, rework signals]
Re-assessment trigger: [scale/ownership threshold]
```

## Failure Modes
- Relabeling: renaming teams with four new type words while interactions stay unchanged → the interaction modes are the mechanism, not the type labels
- Ignored cognitive load: the "platform" team absorbs every request and becomes a ticket queue → enforce scope by load, convert to X-as-a-Service with a real product surface
- Boundary churn: re-org after every friction — teams never gain the trust and rhythm long lifespans create → change scope within stable teams before changing teams
- Structure without Conway awareness: communication patterns mirror the org chart whether designed or not → place the boundaries where you want the system boundaries
- premature topologies (single-team orgs): ceremony replaces work → defer until multiple teams genuinely exist

## Evidence Strength
Practitioner consensus with a growing case-study base (Skelton & Pais, industry adoption since 2019); causal evidence is thin — treat it as a design vocabulary with sensible defaults and explicit trade-offs, not a tested theory of organizational performance.

## Source
Matthew Skelton & Manuel Pais, *Team Topologies* (2019); Melvin Conway, "How Do Committees Invent?" (1968). Admission verdict: **Build** (v0.1.12) — leadership held hiring, motivation, and change entries but no org-structure design method; engineering held system-boundary design but not team-boundary design.
