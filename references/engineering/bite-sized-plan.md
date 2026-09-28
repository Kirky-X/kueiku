# Bite-Sized Plan

## Core Concept
Every step should be 2-5 minutes, with no placeholders, exact file paths, and a Self-Review 3-check. Plans so small that both agents and humans can execute them without ambiguity.

## Applicable Scenarios
✅ **Best for**
- Agent-executable plans
- Complex task decomposition
- Reducing implementation errors

⚠️ **When NOT to use**
- Exploratory work where the next step depends on what you learn — decomposition beyond the known horizon invents fiction; plan the spike, not the whole journey
- One-line changes — writing the plan costs more than doing the work
- Steps that are inherently long (training runs, installs) — 2-5 minutes is about verifiable units of change, not wall-clock; wrap long operations with their own verification step

## Key Steps
1. Break the task into steps of 2-5 minutes each
2. Each step must have: exact file path, exact code change, no placeholders
3. Self-Review 3-checks: Does it compile? Does it pass existing tests? Does it match the intent?
4. If a step needs more than 5 minutes, break it further
5. Execute steps sequentially; verify after each step

## Output Template

```
Goal: [one sentence]

Step 1 — [verb + target]
  File: src/services/order.py (function calc_total, lines 42-58)
  Change: [exact change described, no "..." placeholders]
  Verify: pytest tests/test_order.py::test_calc_total passes

Step 2 — [next verifiable unit]
  File: ...
  Change: ...
  Verify: [command] exits 0

Self-Review 3-check after each step: ① compiles ② existing tests green ③ still matches intent
Abort rule: any step that cannot be verified → stop, don't improvise past the plan
```

## Failure Modes
- Placeholder rot: steps like "refactor the handler as needed" — the executor invents the details → every step names files and the exact change; if you can't write it, you haven't finished decomposing
- Verification skipped under momentum: three steps executed before the first check → a failed step 1 poisons steps 2-3; verify after every step, no exceptions
- Over-decomposition: 40 micro-steps for a 30-minute task — plan maintenance exceeds execution → right-size at the verifiable-unit level; merge steps that share one verification

## Evidence Strength
Practitioner consensus — aligned with widely observed agent-failure modes (ambiguity compounds across steps; unverifiable steps get hand-waved); no controlled studies quantify error reduction, and the 2-5 minute constant is a practical convention rather than a calibrated optimum.

## Source
Agent workflow optimization methodology; bite-sized execution patterns.
