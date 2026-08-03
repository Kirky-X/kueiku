# Agent DX / CLI Scale

## Core Concept
7-axis 0-3 scoring system for CLI/SDK agent friendliness: Machine-Readable output, Raw Payload access, Schema availability, Context richness, Hardening (error handling), Safety (idempotency), Knowledge (documentation). Higher scores mean better AI agent integration.

## Applicable Scenarios
✅ **Best for**
- CLI/SDK agent friendliness assessment
- API design for AI integration
- Developer experience improvement

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

## Source
Agent-first design methodology; CLI/SDK agent experience framework.
