# Agent DX / CLI Scale · Agent Developer Experience Scoring Axis

## Core Idea
Traditional DX (developer experience) targets humans. The agent era needs a new scoring axis. Use 7 dimensions scored 0–3 to quantify tool/CLI/SDK friendliness for agents, turning "can an agent use this efficiently" from subjective judgment into an auditable checklist.

## Use Cases
- Designing CLI/SDK for AI agent use
- Evaluating existing tools for agent friendliness
- Tool documentation quality varies, causing frequent agent invocation errors

## Key Steps
Score each dimension 0–3 (0=terrible, 3=excellent):

1. **Machine-Readable**: Does the output have structured format (JSON/JSON Lines)? Or is it only human-readable text?
2. **Raw Payload**: Can it output raw data (without formatting/color/box-drawing characters)?
3. **Schema Introspection**: Can the agent query input/output schema (is `--help` machine-readable, is there a schema endpoint)?
4. **Context Window**: Can output be trimmed to necessary fields (`--fields`/`--filter`) to avoid blowing up agent context?
5. **Input Hardening**: Does input tolerate common agent mistakes (extra spaces, field order, quote style)?
6. **Safety Rails**: Do dangerous operations require explicit `--confirm` to prevent agents from accidentally executing destructive commands?
7. **Knowledge Packaging**: Does it provide concise knowledge packs loadable by agents (SKILL.md / structured docs) instead of making agents crawl full documentation?

Total score = sum of 7 dimensions (0–21):
- 0–7: Difficult for agents to use, requires extensive wrappers
- 8–14: Usable but inefficient
- 15–21: Agent-native friendly

## Source
design.md (Agent DX / CLI Scale scoring axis)
