# Execution

**When to use**: Outcome-oriented roadmapping, strategy red teaming, agile requirements

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Outcome Roadmap** | Enable[segment] to[customer outcome] so that[business impact] | Roadmap from output to outcome | `outcome-roadmap.md` |
| **Strategy Red Team** | Steelman-then-attack + rank by impact×likelihood×cheapness | Stress-test strategy before finalizing | `strategy-red-team.md` |
| **User Stories** | 3 C's (Card/Conversation/Confirmation) + INVEST 6 criteria | Agile backlog management | `user-stories.md` |
| **Job Stories** | When[situation], I want[motivation], so I can[outcome] | Contextualized requirements, avoiding persona bias | `job-stories.md` |
| **Critical Path Method** | Longest dependency chain sets minimum duration; float separates safe delay from date-killing delay | Hard-deadline projects with dependent tasks, slip triage, crash/fast-track decisions | `critical-path.md` |

## Minimum Information Requirements per Methodology

- **Outcome Roadmap**: Requires existing roadmap items + segment/outcome thinking
- **Strategy Red Team**: Requires strategic thesis to challenge
- **User Stories**: Requires backlog + acceptance criteria definition capability
- **Job Stories**: Requires situation/motivation/outcome scenario awareness
- **Critical Path Method**: Requires task-level duration estimates + explicit dependencies (ranges acceptable, invented single numbers not)

## Routing Trigger Signals

- "Outcome-oriented roadmap" → Outcome Roadmap (primary)
- "Strategy red team / Steelman-then-attack" → Strategy Red Team (primary)
- "Agile requirements / User Story" → User Stories (primary)
- "Contextualized requirements / Job Story" → Job Stories (primary)
- "Project timeline / which delay moves the end date / where to add resources to hit the deadline / dependency chain" → Critical Path Method (primary) ⚡ If tasks emerge step by step in agent/discovery work → use Bite-Sized Plan (Engineering); if no dependencies, just task juggling → use Eisenhower Matrix (Decision Making)

## Common Combinations

- **Strategy to backlog**: Strategy Red Team (stress-test the thesis) → Outcome Roadmap (sequence outcomes per segment) → User Stories (break outcomes into INVEST items)
- **Requirements formatting**: Job Stories (situation-first draft) → User Stories (formalize where the situation genuinely differs by role)
- **Deadline recovery**: Critical Path Method (locate the real path + float) → Strategy Red Team (challenge the scope the date serves) → crash/fast-track only on the path
