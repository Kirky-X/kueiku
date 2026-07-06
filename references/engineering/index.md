# Engineering · Programming & Architecture

**Use cases**: Test-driven development, bite-sized executable plans, service contract design, agent friendliness evaluation

## Programming Methodologies

| Methodology | One-line Description | Best Scenario | Reference |
| --- | --- | --- | --- |
| **TDD Red-Green-Refactor** | Red(write test → fail) → Green(simplest implementation → pass) → Refactor(clean up → stay green) | Frequent regression bugs, refactoring without safety net | `tdd-red-green-refactor.md` |
| **Bite-Sized Plan** | Each step 2–5 min + No Placeholders + exact file paths + Self-Review triple check | Plans that agents/humans can both follow | `bite-sized-plan.md` |

## Architecture Methodologies

| Methodology | One-line Description | Best Scenario | Reference |
| --- | --- | --- | --- |
| **Typed Service Contracts** | Spec & Handler + Design by Contract + Result Monad + Parse don't validate | Service boundary contract design, boundary error defense | `typed-service-contracts.md` |
| **Agent DX / CLI Scale** | 7-axis 0–3 scoring: Machine-Readable/Raw Payload/Schema/Context/Hardening/Safety/Knowledge | Agent friendliness evaluation for CLI/SDK | `agent-dx-cli-scale.md` |

## Minimum Information Requirements for Each Methodology

- **TDD Red-Green-Refactor**: Requires a runnable test framework
- **Bite-Sized Plan**: Requires task decomposition ability + clear file paths
- **Typed Service Contracts**: Requires service boundary identification + type system support
- **Agent DX / CLI Scale**: Requires the CLI/SDK to be evaluated + 7-dimension scoring capability

## Routing Trigger Signals

- "test-driven development" → TDD Red-Green-Refactor (primary)
- "bite-sized executable plan" → Bite-Sized Plan (primary)
- "service boundary contract design" → Typed Service Contracts (primary)
- "agent friendliness evaluation" → Agent DX / CLI Scale (primary)
