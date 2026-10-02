# Socratic Questioning

## Core Concept
Systematic questioning to clarify assumptions, test logic, expose contradictions, and arrive at deeper understanding. 6 types of Socratic questions target different aspects of thinking.

## Applicable Scenarios
✅ **Best for**
- Ill-defined problem clarification
- Strategies relying on unverified assumptions
- Requirement and specification review

## Key Steps
1. **Clarification**: "What do you mean by X?" "Can you give an example?"
2. **Probing assumptions**: "What are you assuming?" "Is this always true?"
3. **Probing evidence**: "What evidence supports this?" "How do you know?"
4. **Questioning viewpoints**: "What's an alternative perspective?" "Who benefits?"
5. **Probing implications**: "If that's true, what follows?" "What are the consequences?"
6. **Questioning the question**: "Why is this question important?" "Is this the right question?"

## Orientation Check

When the user deflects questions, answers a different question, or seeks agreement rather than insight, questioning is no longer serving inquiry — diagnose the capture before persisting:

| Capture pattern | Tell | Intervention |
| --- | --- | --- |
| Conclusion preservation | Evidence for counts; evidence against gets explained away | Decouple conclusion from identity: a wrong conclusion costs nothing personal — re-examine it as if advising someone else |
| Authority preservation | "I was already thinking that"; others' input registers only as confirmation | Frame probes as a joint stress-test, not a challenge to expertise |
| Threat reduction | Rushing to resolve; complexity reads as danger | Reduce pressure before analysis: name the safety, slow the pace |
| Completion seeking | Answer speed inversely proportional to problem complexity | Insert a deliberate hold: "One more angle before we settle this." |
| Argument drift | Ever-more-elaborate analysis that keeps landing on the same conclusion | Stop arguing content; move to external checks — a testable prediction, written down, revisited later |

**Exit condition**: under threat reduction, suspend Socratic questioning entirely — lower the exploration pressure first; questioning someone under threat deepens the threat.

**Red line**: this check exists to restore the user's truth-seeking orientation — it is never a persuasion technique.

## When NOT to use

- The user is under pressure or threatened — questioning deepens the threat; lower the pressure first (Orientation Check, threat reduction row)
- The question is factual ("does X support Y?") — Socratic questioning uncovers assumptions, it does not retrieve facts; answer it
- A one-way channel with no user present (batch review, audit log) — nobody can answer the probes
- The user asked for an answer, not an examination — if the analysis is already done and the decision is theirs to make, deliver it; questioning is opt-in, never a default stance
- Persisting past saturation — once assumptions are on the table, stop; endless probing is interrogation, not inquiry

## Output Template

```
Assumption under test: [what the plan takes for granted]
Probe type: clarification | assumption | evidence | viewpoint | implication | the-question-itself
What the evidence actually shows: [verbatim, or "none offered"]
Revised statement: [the sharper version that survives the probing]
Open question: [what the questioning did not resolve]
```

## Failure Modes

- **Probe chains read as cross-examination** — five questions in a row without engaging the answers; answer each probe before the next
- **Explanations instead of evidence** — "the users obviously wanted…" passes unchallenged; ask what observation would have shown otherwise
- **Rhetorical Socratic** — questions whose only acceptable answer is agreement; the Orientation Check red line exists for this
- **Infinite regress** — "but why do you say that?" until the conversation dies; each probe must be answerable in one step from something the user actually said

## Cognitive-Bias Quick Check (Recipe cross-reference)

Before treating probe answers as findings, run three "Ask:" checks on the answers themselves:

- **Anchoring** — Ask: was the first number offered the anchor every later estimate quietly moved from?
- **Sunk cost** — Ask: is any option defended mainly by what has already been spent, not by what it returns next?
- **Confirmation bias** — Ask: what observation would have overturned this conclusion — and did anyone actually look for it?

For the full detector table (lifecycle coverage with trigger signal + check action per bias), route to **Cognitive & Statistical Bias Checklist** (data-analysis, `debias-checklist.md`). This entry holds the pointer, not a duplicate table.

**Admission verdict** (v0.1.6): standalone cognitive-bias entries reviewed — Recipe verdict, because data-analysis already owns the checklist methodology and a second table here would create twin sources of truth.

## Evidence Strength

**Practitioner consensus on method, contested on transfer.** Socratic questioning is a standard fixture in critical-thinking education and the assumption-probing sequence is well documented. Evidence that Socratic dialogue improves decision quality in applied settings is mixed, and trained facilitation matters more than the question types themselves — treat the six types as a checklist for a facilitator, not a self-operating procedure.

## Source
Socrates (470-399 BC); formalized in critical thinking education.
Provenance: orientation-capture patterns absorbed from [thinking-partner](https://github.com/mattnowdev/thinking-partner) (MIT license), absorbed 2026-09.
Cognitive-Bias Quick Check added with **Recipe** verdict, 2026-10-01 — data-analysis owns the full checklist (`debias-checklist.md`); this entry holds a three-question pointer, not a second table.
