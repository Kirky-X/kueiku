# User Stories

## Core Concept
Agile requirements in the format: As a [role], I want [goal], so that [benefit]. Governed by the 3 C's (Card/Conversation/Confirmation) and INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).

## Applicable Scenarios
- Agile backlog management
- Cross-functional team communication about requirements
- Iterative development planning

⚠️ **When NOT to use**
- The benefit differs from the goal in no meaningful way ("so that I can log in") — the third clause is decoration; write a plain requirement
- Precise contractual specifications (integrations, compliance) — stories negotiate; contracts specify
- Situations matter more than roles — Job Stories carry context better; personas here would be invented

## Key Steps
1. Write the story: As a [role], I want [goal], so that [benefit]
2. Card: keep the written description brief — it's a placeholder for conversation
3. Conversation: discuss the story with the team to flesh out details
4. Confirmation: define acceptance criteria (testable conditions of satisfaction)
5. Validate against INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable

## Output Template

```
Story: As a [support agent], I want [to bulk-reassign tickets], so that [reassignments don't eat my morning]

Acceptance criteria (Confirmation):
  Given [50 open tickets filtered by tag], when [I select all + reassign], then [all move in one action and audit log records it]
  Given [ticket in status Closed], when [bulk reassign includes it], then [it is skipped and reported]
  Edge: [0 tickets selected] → [button disabled]

INVEST check: Independent [n/a deps?] Negotiable [open on how] Valuable [why] Estimable [team confirms] Small [fits a sprint?] Testable [criteria above]

Split if too big: [vertical slice 1: single reassign; slice 2: bulk] — never split by architecture layer
Conversation notes: [decisions from discussion, dated]
```

## Failure Modes
- Role inflation: "As a user" — a role with no perspective → name the specific role with the specific need, or switch to a job story
- Story as spec: acceptance criteria grow into a requirements document taped to a story format → keep the card thin; move detail to tests or the conversation notes
- INVEST as trivia: criteria recited but "Small" never enforced and "Independent" never examined → run the check at refinement, and split on INVEST failures before estimation

## Evidence Strength
Practitioner consensus — the de facto standard for backlog expression in agile teams; evidence for specific format benefits (stories vs task lists) is anecdotal, and the known failure mode is cargo-cult formatting without the conversation the 3 C's actually govern.

## Source
Mike Cohn, *User Stories Applied* (2004); Ron Jeffries' 3 C's (2001).
