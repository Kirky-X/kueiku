# Engineering

**When to use**: Test-driven development, bite-sized executable plans, service contract design, Agent friendliness assessment, code review, architecture design, CI/CD, observability, domain-driven design, performance optimization, security design, API design, database design, incident response, Git workflow, dependency management, microservices, refactoring, back-of-envelope estimation, throughput constraints, design contradiction resolution

## Programming Methodologies

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **TDD Red-Green-Refactor** | Red(write test→fail)→Green(minimal implementation→pass)→Refactor(clean up→stay green) | Frequent regression bugs, refactoring without safety net | `tdd-red-green-refactor.md` |
| **Bite-Sized Plan** | Each step 2-5 min + No Placeholders + exact file paths + Self-Review 3-checks | Plans that agents and humans can both follow | `bite-sized-plan.md` |
| **Code Review Checklist** | Security/Architecture/Performance/Maintainability 4-dimension checklist-driven review | Pre-merge quality gate, refactoring impact assessment | `code-review-checklist.md` |
| **Refactoring Patterns** | Code smells → refactoring techniques comparison + small-step improvement under test protection | Legacy code improvement, large function/class decomposition | `refactoring-patterns.md` |
| **Git Workflow Strategies** | Trunk-Based / GitHub Flow / Git Flow / GitLab Flow strategy selection matrix | Team branching strategy, multi-environment release process | `git-workflow-strategies.md` |
| **Dependency Management** | Introduction assessment + version strategy + security monitoring + health audit | Dependency selection, vulnerability response, dependency health audit | `dependency-management.md` |

## Architecture Methodologies

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Typed Service Contracts** | Spec&Handler + Design by Contract + Result Monad + Parse don't validate | Service boundary contract design, boundary error defense | `typed-service-contracts.md` |
| **Agent DX / CLI Scale** | 7-axis 0-3 scoring: Machine-Readable/Raw Payload/Schema/Context/Hardening/Safety/Knowledge | CLI/SDK agent friendliness assessment | `agent-dx-cli-scale.md` |
| **Clean Architecture** | Dependency inversion layering + Port & Adapter + domain layer zero external dependencies | New project architecture design, framework/database replacement | `clean-architecture.md` |
| **Domain-Driven Design** | Bounded context + aggregate root + ubiquitous language + event storming | Complex business system modeling, microservice boundary definition | `domain-driven-design.md` |
| **Microservices Patterns** | Saga/CQRS/Event Sourcing + service governance + resilience patterns | Monolith decomposition, distributed data consistency, service governance | `microservices-patterns.md` |
| **API Design** | RESTful/GraphQL/gRPC selection + version management + idempotency + error response | Interface design, API standardization, version compatibility | `api-design.md` |
| **Database Schema Design** | Data modeling + index strategy + safe migration + normalization/denormalization | New project data model, schema restructuring, query optimization | `database-schema-design.md` |
| **TRIZ Contradiction Separation** | Template-named contradiction → IFR → separate in time/space/condition/scale → reuse existing resources → lock no-compromise or record residual trade-off | Design parameters pull in opposite directions, "can't have both" trade-offs | `triz-contradictions.md` |

## Process Methodologies

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **CI/CD Pipeline Design** | 7-stage pipeline (Trigger→Build→Test→Security→Quality→Deploy→Post-Deploy) + gates + rollback | Pipeline setup, release strategy design, quality gates | `cicd-pipeline-design.md` |
| **Security by Design** | STRIDE threat modeling + secure coding patterns + CI continuous verification | Security architecture design, compliance requirements, security hardening | `security-by-design.md` |
| **Observability** | Logs + Metrics + Traces 3-pillar collaboration + SLO-driven alerting | Production incident investigation, distributed system tracing, capacity planning | `observability.md` |
| **Performance Optimization** | Measure→Locate→Optimize→Verify cycle + bottleneck layering + anti-pattern warnings | Performance troubleshooting, baseline establishment, resource cost optimization | `performance-optimization.md` |
| **Back-of-Envelope Estimation** | Fermi decomposition + c×10^e magnitude target + unit checksum + hardware/cost constant table | Pre-build capacity/QPS/cost feasibility checks, design sanity checks | `napkin-math-estimation.md` |
| **Theory of Constraints** | Identify→Exploit→Subordinate→Elevate→Recheck on the single binding stage + resource vs policy classification | One stage queues while downstream idles, added capacity doesn't raise end-to-end output | `theory-of-constraints.md` |
| **Incident Response & Postmortem** | Detect→Respond→Mitigate→Resolve + blameless postmortem + Action Item closure | Production incident emergency, On-Call process building, experience capture | `incident-response-postmortem.md` |

## Minimum Information Requirements per Methodology

- **TDD Red-Green-Refactor**: Requires runnable test framework
- **Bite-Sized Plan**: Requires task decomposition capability + clear file paths
- **Code Review Checklist**: Requires PR/MR to review + project architecture context
- **Refactoring Patterns**: Requires code to refactor + test coverage
- **Git Workflow Strategies**: Requires team size + release cadence + CI/CD maturity
- **Dependency Management**: Requires project dependency list + security scanning tools
- **Typed Service Contracts**: Requires service boundary identification + type system support
- **Agent DX / CLI Scale**: Requires CLI/SDK to evaluate + 7-dimension scoring capability
- **Clean Architecture**: Requires business domain analysis + tech stack constraints
- **Domain-Driven Design**: Requires business expert participation + domain knowledge
- **Microservices Patterns**: Requires existing system architecture + team organizational structure
- **API Design**: Requires API usage scenarios + consumer requirements
- **Database Schema Design**: Requires business entity relationships + query patterns
- **TRIZ Contradiction Separation**: Requires two named opposing states of one parameter + the benefit each state serves
- **CI/CD Pipeline Design**: Requires project type + deployment environment + team size
- **Security by Design**: Requires system data flow diagram + compliance requirements
- **Observability**: Requires system architecture + SLA/SLO definitions
- **Performance Optimization**: Requires performance baseline data + SLO targets
- **Back-of-Envelope Estimation**: Requires workload shape (request size / rates / data volumes) + hardware or cost constants for the rows used
- **Theory of Constraints**: Requires flow stage sequence + per-stage rate or queue evidence + a throughput goal
- **Incident Response & Postmortem**: Requires incident timeline + monitoring data

## Routing Trigger Signals

- "Test-driven development" → TDD Red-Green-Refactor (primary)
- "Bite-sized executable plan" → Bite-Sized Plan (primary)
- "Code review / PR review" → Code Review Checklist (primary)
- "Refactoring / code smells / code cleanup" → Refactoring Patterns (primary)
- "Git branching strategy / workflow / release process" → Git Workflow Strategies (primary)
- "Dependency management / dependency selection / dependency vulnerabilities / dependency audit" → Dependency Management (primary)
- "Service boundary contract design" → Typed Service Contracts (primary)
- "Agent friendliness assessment" → Agent DX / CLI Scale (primary)
- "Architecture design / layering / hexagonal / onion architecture" → Clean Architecture (primary)
- "Domain-driven / DDD / bounded context / event storming / aggregate root" → Domain-Driven Design (primary)
- "Microservices / distributed systems / Saga / CQRS / service governance" → Microservices Patterns (primary)
- "API design / RESTful / GraphQL / gRPC / interface design" → API Design (primary)
- "Database design / schema / indexing / data modeling / migration" → Database Schema Design (primary)
- "CI/CD / pipeline / continuous integration / continuous deployment / release strategy" → CI/CD Pipeline Design (primary)
- "Security design / threat modeling / STRIDE / secure coding" → Security by Design (primary)
- "Observability / monitoring / logging / tracing / alerting" → Observability (primary)
- "Performance optimization / performance troubleshooting / latency / throughput" → Performance Optimization (primary)
- "Back-of-envelope / napkin math / Fermi estimation / capacity estimation / cost estimation" → Back-of-Envelope Estimation (primary)
- "Bottleneck / throughput constraint / where work piles up / system-wide limit / five focusing steps" → Theory of Constraints (primary)
- "Design contradiction / conflicting requirements / resolve trade-off / can't have both" → TRIZ Contradiction Separation (primary)
- "Incident response / On-Call / Postmortem / review" → Incident Response & Postmortem (primary)

## Common Combinations

- **Capacity & cost design**: Back-of-Envelope Estimation (design-time magnitude) → Performance Optimization (measured verification once the system runs)
- **Throughput workup**: Theory of Constraints (identify the binding stage) → Performance Optimization (profile the code inside that stage)
- **Contradiction-first design**: Microservices Patterns (check the pattern inventory first) → TRIZ Contradiction Separation (no standard pattern fits the conflict)
