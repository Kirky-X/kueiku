# Agent DX / CLI Scale

## Core Concept
7-axis 0-3 scoring system for CLI/SDK agent friendliness: Machine-Readable output, Raw Payload access, Schema availability, Context richness, Hardening (error handling), Safety (idempotency), Knowledge (documentation). Higher scores mean better AI agent integration.

## Applicable Scenarios
✅ **Best for**
- CLI/SDK agent friendliness assessment
- API design for AI integration
- Developer experience improvement

⚠️ **When NOT to use**
- A CLI that humans are the only consumers of — the rubric rewards machine-readability, so a well-designed human tool scores low and the team optimizes against a nonexistent agent → **Agent DX / CLI Scale** only pays off once a named agent or script actually calls the surface
- Network interface contract work — this scores the output shape of a command, not the service contract behind it → **API Design** / **Typed Service Contracts**
- Ranking two toolchains by the 0-21 total — the sum treats seven axes as interchangeable, but a zero on Safety (unsafe writes) outweighs a three on Schema → score per axis against the agent's actual failure, never rank on the total
- Internal tooling with a handful of invocations — there is no repeated agent interaction to amortize the hardening work

## Key Steps
1. For each of the 7 axes, score the CLI/SDK 0-3:
   - **Machine-Readable**: Does it output JSON/structured data? (0=human only, 3=full JSON)
   - **Raw Payload**: Can agents access raw data? (0=formatted only, 3=raw+formatted)
   - **Schema**: Is output schema documented? (0=none, 3=JSON Schema + examples)
   - **Context**: Does output include enough context for agents? (0=minimal, 3=self-describing)
   - **Hardening**: Error handling quality (0=crash, 3=structured errors with recovery hints)
   - **Safety**: Idempotency and side-effect management (0=unsafe, 3=fully idempotent)
   - **Knowledge**: Documentation quality for agents (0=none, 3=agent-optimized docs)
2. Calculate total score (0-21)
3. Identify lowest-scoring axes for improvement
4. Prioritize improvements by agent impact

## Output Template

```
Tool: [name / version]      Consumer: [which agent or script calls it]

Axis scores (0-3):
  Machine-Readable: [0-3 — JSON on stdout, human text on stderr]
  Raw Payload:      [0-3 — raw access via --format=json / --output=file]
  Schema:           [0-3 — JSON Schema published at [url], with examples]
  Context:          [0-3 — self-describing: ids, units, timestamps, pagination]
  Hardening:        [0-3 — structured errors, distinct exit codes, recovery hints]
  Safety:           [0-3 — idempotency key on write commands / N-A for read-only]
  Knowledge:        [0-3 — usage doc written for agents, copy-paste examples]
Total: [n/21]   Weakest axis: [axis]   Evidence: [failed agent run that exposed it]

Priority fix: [axis] → [concrete change] → [agent behavior improves: fewer retries / no ad-hoc parsing]
```

## Failure Modes
- Self-assessment inflation: the team scores its own CLI after building it, and every axis reads 2 or 3 → have an agent, or a reviewer outside the team, score it from the published docs and the raw output only
- Machine path built for no consumer: a JSON mode nobody invokes gets added to raise the score → ship the machine path only after naming the agent that will call it and the command it will run
- Safety scored on read-only commands → a read-only CLI is docked for lacking idempotency, which is not a real defect → score Safety only where the command has side effects, and mark the rest N-A
- Fixing the lowest-scoring axis because it is lowest → effort goes to a missing schema while the axis that actually broke the agent run is ignored → pick the axis from the recorded failed run, not from the scoreboard

## Evidence Strength
Practitioner consensus — the underlying interface practice (machine-readable output, raw payload access, idempotency on writes) is long-established and widely endorsed, but this particular rubric is a recent popularization with little independent validation; the 0-3 scale and the implicit comparability of its axes are conventions, not measured properties, so a total score should be read as a conversation starter rather than a measurement.

## Source
Agent-first design methodology; CLI/SDK agent experience framework.
