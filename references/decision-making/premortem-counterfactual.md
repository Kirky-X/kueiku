# Pre-mortem & Counterfactual

## Core Concept

**Pre-mortem**: Before taking action*, imagine it has already failed, reverse-engineer the causes of failure — thus avoiding them in advance.
**Counterfactual thinking**: Change a condition in the past/future, speculate "what if X were different, what would the result be" — thus identifying key variables.

> Forward planning asks "how to succeed"; reverse planning asks "if it fails, what caused it." The latter often finds blind spots the former overlooks.

---

## Applicable Scenarios

✅ **Best suited for**
- Risk identification before major decisions (investment, product launch, strategic transformation)
- Exposing team's hidden concerns before project initiation
- Retrospective: Understanding "why we ended up here"
- Identifying over-reliance on single-point assumptions in plans

⚠️ **Use with caution**
- Execution-level detail optimization (too heavyweight a tool for this)
- Decisions that cannot be changed (counterfactual speculation only produces regret, no practical value)

---

## Execution Steps

### Mode A: Pre-mortem (Failure Autopsy)

#### Step 1: Clearly Describe the Plan

Write out the core elements of the plan:
```
Goal: [...]
Key assumptions: [...]
Timeline: [...]
```

#### Step 2: Imagine Failure

**Mandatory setup**: "Now is [target time point], the plan has already failed. Not minor failure, but total failure."

Fully immerse yourself in this scenario, then ask: **"How did the failure happen?"**

#### Step 3: Brainstorm Causes of Failure

List all possible failure paths without judgment — the more, the better:

```
Candidate list of failure causes:
  - [Cause 1]
  - [Cause 2]
  - ...
```

Tip: Each cause should be specific to "who, did what, led to what" — avoid vague descriptions like "poor execution."

#### Step 4: Assess Probability and Impact

Score each cause:

```
Cause | Probability (High/Medium/Low) | Impact (High/Medium/Low) | Current preventive measures in place
```

Prioritize causes with "high probability + high impact + no preventive measures."

#### Step 5: Develop Preventive Actions

For high-priority risks, design preventive mechanisms:

```
Risk: [...]
Preventive action: [...]
Trigger signal (early warning): [...]
Responsible person/Deadline: [...]
```

---

### Mode B: Counterfactual Thinking (Key Variable Identification)

#### Step 1: Define Reference Event

```
What actually happened: [...]
```

#### Step 2: Change Single Variable

Each time change only **one** condition, ask "what if X were different, what would the result be?"

```
Counterfactual 1: If [Variable A] were different (specifically: ...), the result would be [...]
Counterfactual 2: If [Variable B] were different (specifically: ...), the result would be [...]
```

#### Step 3: Identify Key Variables

Which variable change has the greatest impact on the result? This variable is the **key leverage point**.

#### Step 4: Translate into Action

```
Key variable: [...]
How to influence/control this variable in the future: [...]
```

---

## Output Templates

### Pre-mortem Output

```
Plan overview: [...]

【Failure Scenario】(Assumed time point: [...], plan has completely failed)

High-risk failure paths:
  ① [Cause] — Probability: High — Impact: High — Preventive measures: [None/Yes (description)]
  ② [Cause] — Probability: Medium — Impact: High — Preventive measures: [...]

Priority preventive actions:
  1. [Action] — Addresses risk ① — Trigger signal: [...] — Responsible person: [...]
  2. [Action] — Addresses risk ② — Trigger signal: [...] — Responsible person: [...]

Parts of the plan that need modification: [...]
Confidence level change: Before optimization [x%] → After optimization [y%]
```

### Counterfactual Output

```
Reference event: [...]

Key counterfactual analysis:
  Variable A change → Result change: [...]  Impact: High/Medium/Low
  Variable B change → Result change: [...]  Impact: High/Medium/Low

Most critical variable: [...]
Future action: [...]
```

---

## Execution Example

**Pre-mortem scenario**: Preparing to complete product MVP and launch within three months

```
【Failure Scenario】Three months later, MVP launch is severely delayed, or no one uses it after launch.

Failure path brainstorm:
  - Core feature technical difficulty underestimated, R&D delayed 6 weeks
  - Team's understanding of target user needs is off, built something no one wants
  - Competitor launches similar feature two weeks before our launch
  - Key engineer resignation causes progress interruption
  - User test feedback is terrible but no time to iterate

Priority risks:
  ① Requirement understanding deviation — Probability: High — Impact: High — No preventive measures
  ② Technical underestimation — Probability: Medium — Impact: High — No preventive measures

Preventive actions:
  ① 4 weeks before launch, conduct 5 in-depth interviews with target users, validate core scenarios — Trigger signal: User test satisfaction <70%
  ② Complete technical assessment in Week 1, identify high-risk modules — Trigger signal: Any module assessment exceeds 2x estimated work hours
```

---

## Common Pitfalls

| Pitfall | Description | How to Avoid |
|------|------|---------|
| Failure causes too vague | "Insufficient resources," "poor execution" cannot be translated into actions | Drill down to specific people, events, time points |
| Only listing risks without preventive measures | Pre-mortem becomes a complaint session | Each high risk must have a corresponding preventive action |
| Counterfactual becomes a regret list | Doing counterfactual on unchangeable past | Only do counterfactual on "future controllable variables"; retrospective only extracts patterns |
| Overly pessimistic | Team morale damaged after Pre-mortem | Clearly state: Identifying risks is for success, not predicting failure |

---

## Relationship with Other Methodologies

- **Precedes major decisions**: After RICE/OKR determines direction, use Pre-mortem for final risk review
- **Combined with Six Thinking Hats**: Pre-mortem is a deepened version of Black Hat thinking
- **Combined with Socratic Questioning**: After questioning assumptions, use counterfactual thinking to test the impact if assumptions fail
- **Output feeds Eisenhower Matrix**: Preventive actions classified by urgency/importance, scheduled into execution priority

---

## Tigers / Paper Tigers / Elephants Three-Category Method

Pre-mortem brainstorming produces many risk items; directly scoring by "probability × impact" easily leads teams into a "everything is important" dilemma. The three-category method groups risks by nature into three types, each with different response strategies:

| Risk Type | Probability | Impact | Nature | Response Strategy |
|---------|------|------|------|---------|
| **Tiger (Real Tiger)** | High | High | Real and serious threat, highly likely to occur and cause significant damage | **Must act immediately**: Assign dedicated personnel/budget for prevention, set early warnings, incorporate into OKR |
| **Paper Tiger** | Low | High | Looks scary but actual probability is low | **Do not over-invest**: Write a contingency plan only, avoid consuming main resources; regularly reassess probability |
| **Elephant** | High | Low | Almost certain to occur but single impact is limited | **Monitor rather than eliminate**: Establish routine monitoring and rapid response processes; handle in batches rather than individually |

**Usage method**:
1. For each risk produced by Pre-mortem, first determine if it's Tiger / Paper Tiger / Elephant
2. Tigers go into the preventive action list (reference Step 5)
3. Paper Tigers go into the "observation list," reassess probability changes quarterly
4. Elephants go into the "operations list," handled daily by operations/CS team

**Anti-patterns**:
- Treating all Paper Tigers as Tigers → Resources diluted, real Tigers overlooked
- Treating Elephants as Tigers → Investing heavily in prevention with limited returns
- Treating Tigers as Paper Tigers → Root cause of "black swan" incidents