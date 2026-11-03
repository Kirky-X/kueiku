# Agent Autonomy & Runtime Design

## Core Concept
The workflow-vs-agent decision: a **workflow** orchestrates LLM steps through predetermined code paths (predictable, cheap, testable); an **agent** lets the LLM direct its own tool-use loop (flexible, costly, harder to verify). Choose the **least autonomous design that works** — autonomy is a cost you pay in reliability and verifiability, not a feature. Between the two sit composable patterns of increasing autonomy: prompt chaining → routing → parallelization → orchestrator-workers → evaluator-optimizer. Autonomy is granted per action, not per agent: read-only actions run free, irreversible actions get a human checkpoint.

## Applicable Scenarios
✅ **Best for**
- Deciding whether a task needs an agent at all, or a fixed pipeline suffices
- Choosing the orchestration pattern and where human checkpoints sit
- Setting the autonomy dial per action (read / mutate / irreversible)
- Structuring tool surfaces and injection defenses before the first deploy

⚠️ **When NOT to use**
- Choosing between agent frameworks (langgraph / crewai / autogen vs roll-your-own) → **diting** owns framework selection (recorded no-route in this repo's trigger queries); this entry decides *whether and how autonomous*, which precedes framework choice
- Reviewing the code of an already-built agent → **diting** (Engine A, code quality)
- Authoring ZCode multi-subagent workflow scripts → **dynamic-workflows** skill
- Scoring a single tool's output shape (CLI readability) → **Agent DX / CLI Scale**
- Threat modeling the surrounding system → **Security by Design**; this entry covers runtime injection defense for the agent loop itself
- One LLM call with no tools and no branching → there is no runtime to design

## Key Steps
1. Decompose the task: can it be expressed as fixed steps with known inputs? If yes, build the workflow and stop — the agent question is answered
2. If the path genuinely cannot be predetermined (open-ended inputs, unknown step count), select the composable pattern of least autonomy that covers it: chaining → routing → parallelization → orchestrator-workers → evaluator-optimizer
3. Set the autonomy dial per action: **read-only** (run free), **mutable-but-reversible** (run with logging), **irreversible** (send, pay, delete, publish — human checkpoint before execution)
4. Define the tool surface: each tool is one clear action with typed parameters and a documented failure mode; no kitchen-sink tools
5. Ground every observation: tool output, web content, and file contents are **untrusted data**, never instructions (prompt-injection defense; OWASP LLM Top 10) — quote, delimit, and never let retrieved text issue commands
6. Set stop conditions and budgets: max iterations, max tool calls, max spend, and a "return partial result with what blocked you" exit — an agent without an exit is a loop with a personality
7. Instrument for evals from day one: log every trajectory; route failures into the golden set (**LLM Output Evals**)

## Output Template

```
Task: [one sentence] → Verdict: [workflow | agent + pattern] — because [the path is / is not predetermined]
Autonomy table:
  [action] — [read-only | reversible | irreversible] — checkpoint: [none | log | human-approve]
Tools: [name — one action — typed params — failure mode]
Injection defense: [retrieved content delimiting rule | confirmation gate on tool output]
Limits: max iterations [n], max tool calls [n], budget [cost], stop condition [predicate]
Eval plan: [golden set source, gate criterion → LLM Output Evals]
Deferred to diting: [framework choice | built-code review]
```

## Failure Modes
- Agent for everything: the default answer to "could this be an agent?" is almost always "no, it's a pipeline" → run step 1 honestly; the workflow you didn't build is test coverage you didn't lose
- Autonomy creep: a read-only tool grows a write side, and the old dial silently grants it → re-run the autonomy table on every tool change; the dial attaches to actions, not agents
- Missing human checkpoint on irreversible actions: the agent emails the customer / merges the branch / charges the card → anything irreversible or outbound gets a gate, no exceptions for "it usually gets it right"
- Injection through observations: web content or command output containing instructions that the loop obeys → delimit retrieved text as data; instructions arrive only from the operator
- No exit: max iterations unset, the agent wanders or cycles → budgets and stop conditions are part of the design, not runtime hopes
- Kitchen-sink tools: one tool that does five things defeats the autonomy dial (which action is being approved?) → split until each tool is one auditable action
- Framework-first design: picking langgraph before deciding the task needs an agent → the decision precedes the framework; record both in the design record
- Evals bolted on later: no trajectory logging until the first incident → instrument at build time; every failure should feed the eval set

## Evidence Strength
**Mixed, strengthening.** The workflow-vs-agent decision and the composable patterns are practitioner consensus from high-scale agent builders (Anthropic 2024) and align with the ReAct loop literature (Yao et al., ICLR 2023); the injection-threat taxonomy is codified (OWASP Top 10 for LLM Applications). The field moves fast: specific defense techniques and pattern names evolve, while the underlying decision discipline — least autonomy that works, per-action checkpoints, untrusted observations — is stable. Grade the decision framework strong, specific defenses evolving.

## Source
Anthropic, "Building Effective Agents" (2024); Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (ICLR 2023); OWASP Top 10 for LLM Applications (2025). Admission verdict: **Build** (v0.1.16) — ranked second by the independent necessity audit: `agent-dx-cli-scale.md` scores tool output surfaces ("this scores the output shape of a command, not the service contract behind it"), not runtime design; diting owns review of built agents and framework selection (recorded no-route); dynamic-workflows owns ZCode workflow scripts. The design-time "whether and how autonomous" question was unowned.
