# Bite-Sized Plan · Bite-Sized Executable Plans

## Core Idea
Plans that both agents and human engineers can follow — each step completable in 2–5 minutes, no placeholders (No Placeholders), explicit down to file paths, with a Self-Review triple check at each step. Avoid "grand but unexecutable" plan documents.

## Use Cases
- Plans look impressive but no one can follow them
- AI agents frequently get stuck on "what do I do next" when executing plans
- Tasks span multiple files but lack execution order

## Key Steps
1. Decompose the task into atomic steps completable in 2–5 minutes
2. Each step contains 4 elements:
   - exact file path (absolute path or explicit path relative to project root)
   - specific action (create/edit/delete/run command)
   - expected result (visible verification point)
   - failure handling (what to do if this step fails — not just "retry")
3. No Placeholders rule: Prohibit placeholders like "fill in Y at X" — either provide a specific value or explicitly state "to be queried by the agent in context"
4. Self-Review triple check (after each step completes):
   - Did it produce the expected result?
   - Did it affect undeclared files/functions?
   - Are prerequisites for the next step ready?
5. Explicit serial/parallel markers between steps to prevent agent ordering errors

## Source
writing-plans practice (Anthropic Claude Code patterns, Trae writing-plans skill)
