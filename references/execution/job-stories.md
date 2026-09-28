# Job Stories

## Core Concept
Contextualized requirements in the format: When [situation], I want [motivation], so I can [outcome]. Unlike User Stories (which center on persona), Job Stories center on the situation/context, avoiding persona bias and focusing on the causal chain.

## Applicable Scenarios
- Requirements where context matters more than who the user is
- Avoiding persona bias in feature design
- Cross-functional teams needing a shared requirement format

⚠️ **When NOT to use**
- The situation genuinely differs by role (admin vs member see different screens) — persona-bearing User Stories are more honest here
- Regulatory or contract-driven requirements with fixed inputs/outputs — write the spec; a job story adds nothing
- You have no evidence any such situation occurs — invented situations produce invented features; validate with JTBD interviews first

## Key Steps
1. Identify the situation/context: "When [specific situation triggers the need]"
2. Define the motivation: "I want [what the user wants to do in that situation]"
3. Define the expected outcome: "so I can [what outcome they achieve]"
4. Validate: does the job story capture context + motivation + outcome without referencing a specific persona?
5. Use as input for design and development, ensuring the situation drives the solution

## Output Template

```
When    [I'm commuting with one hand free and 10 minutes]
I want  [to catch up on only the threads where I was mentioned]
so I can [arrive informed without scrolling for an hour]

Situational forces (optional, sharpens design):
  Push:    [what makes the current state painful]
  Pull:    [what attracts about the new way]
  Anxiety: [what worries about switching]
  Habit:   [what competes with the new behavior]

Acceptance test: given [situation], when [action], then [outcome] — measurable?
```

## Failure Modes
- Situation so broad it fits everyone ("when I use the app") — no design tension survives → force a trigger with time, place, or state
- Motivation written as a solution ("I want a button that...") — the story then justifies its own conclusion → write what the user wants to accomplish, not how
- Outcome unverifiable: "so I can feel confident" — nothing to test → pick an observable or drop it

## Evidence Strength
Practitioner consensus — an application of the Jobs-to-be-Done tradition; teams report fewer persona debates and better context retention, but there is no controlled comparison of job stories vs user stories on requirement quality — the format's value is in forcing context specificity.

## Source
Alan Klement, *When Coffee and Kale Compete* (2016); inspired by Clayton Christensen's JTBD theory.
