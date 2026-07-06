# Design Thinking · 设计思维

## Core Concept

A **human-centered** innovation methodology that drives solution design through deep understanding of user needs. Systematized by IDEO and Stanford d.school, it consists of five iterative phases.

```
Empathize → Define → Ideate → Prototype → Test
```

**Difference from Traditional Design:**
- Traditional: What technology/resources do we have → What product can we build → Will users like it?
- Design Thinking: What do users truly need → What is the ideal solution → How can we implement it?

---

## Applicable Scenarios

✅ **Best For**
- Designing entirely new products/services from 0 to 1
- Solving pain points in user experience (qualitative problems)
- Service design and process reengineering
- Innovation workshops and team alignment

⚠️ **Use with Caution**
- Rapid decisions under extreme time pressure
- When technical constraints are already very clear (just do the engineering)
- Pure data-driven optimization (A/B testing is more effective)

---

## Five Phases Explained

### Phase 1 · Empathize

**Goal**: Deeply understand users, rather than assuming what they need.

Methods:
- **User Interviews**: Open-ended questions exploring behavior and motivation
- **Contextual Shadowing**: Observe user behavior in real environments
- **Experience Diaries**: Have users record daily product usage experiences
- **Extreme User Interviews**: Interview power users and users who dislike the product most (insights are more extreme and obvious)

Outputs:
- User stories, quote collections
- Behavioral observation notes
- Empathy map (see `empathy-map.md`)

Key principle: **Set aside assumptions, observe like an anthropologist**

---

### Phase 2 · Define

**Goal**: Focus the divergent information from Empathize into a **clear, meaningful problem definition**.

Core tool: **How Might We (HMW) Statement**

```
Format: How might we help [user] achieve [goal], while/although [constraint/tension]?

Example: How might we help elderly people living alone maintain connection with family,
    while not making them feel "monitored"?
```

**HMW Scope Control**:
- Too broad: "How might we improve elderly life?" → Not actionable
- Too narrow: "How might we teach elderly to use video calls?" → Limits innovation space
- Just right: "How might we help elderly naturally share daily life with family?" ✅

Outputs:
- User persona
- Core problem statement (Point of View)
- HMW question list

---

### Phase 3 · Ideate

**Goal**: Generate as many ideas as possible for the HMW question, deferring judgment.

Main methods:
- **Brainstorm**: Quantity first, 50+ ideas in 20 minutes
- **SCAMPER**: Substitute/Combine/Adapt/Modify/Put-to-other-uses/Eliminate/Rearrange
- **Reverse thinking**: How could we make the problem worse? → Invert to get solutions
- **Analogous borrowing**: How do other industries solve similar problems?

Focusing methods (after divergence):
- Voting stickers (limited votes per person, select most promising ideas)
- 2×2 matrix (feasibility vs impact)
- RICE scoring (see `rice.md`)

Outputs:
- Idea inventory (organized by category)
- Top 3-5 concept directions

---

### Phase 4 · Prototype

**Goal**: Quickly build **low-cost, testable** prototypes to turn abstract ideas into visible, tangible forms.

Prototype types (by fidelity):

| Type | Materials | Purpose |
|------|------|------|
| Paper prototype | Paper, pen, scissors | Test process and concept |
| Wireframe / Mockup | Figma/Sketch | Test interaction and layout |
| Functional prototype | Real code (partial) | Test technical feasibility |
| Service role-play | Manual simulation | Test service process |
| Video prototype | Short video | Test value proposition understanding |

**Key principle: Start low-fidelity, iterate quickly. Prototypes are not final products — they are learning tools.**

---

### Phase 5 · Test

**Goal**: Put prototypes in front of real users, collect feedback, learn and iterate.

Testing principles:
- **Let users operate, you just observe**: Don't explain how to use it
- **Ask "why" not "do you like it"**: Avoid polite positive feedback
- **Focus on behavior, not words**: A user saying "good" but getting stuck is more informative
- **Fail fast**: The purpose of testing is to discover problems, not to prove yourself right

Iteration judgment:
- After testing, return to which phase? (Could be Define, could be Ideate, could be tweaking Prototype)
- When is it ready to move to development? (Core hypotheses validated, key pain points resolved)

---

## Output Template (Workshop Version)

```
Project: [Product/Service]

Phase 1 · Empathize:
  Users interviewed: [N people, characteristics]
  Key observations: [...]
  Surprising discoveries: [...]

Phase 2 · Define:
  User persona: [...]
  Core POV: [User] needs [need] because [insight/reason]
  HMW statement: [Final selected HMW]

Phase 3 · Ideate:
  Number of ideas generated: [N]
  Top concepts:
    1. [Name] — [One-line description]
    2. [...]
    3. [...]

Phase 4 · Prototype:
  Prototype type: [Paper/Wireframe/Functional]
  Prototype description: [...]
  Key hypotheses to test: [...]

Phase 5 · Test:
  Test users: [N people]
  Key findings: [...]
  Points needing modification: [...]
  Next step: [Return to which phase for iteration / Ready for development]
```

---

## Relationships with Other Methodologies

- **Preceded by JTBD**: JTBD uncovers real user Jobs as input for Empathize + Define phases
- **Followed by Lean BML**: Design thinking produces prototype concepts; BML loops execute product iteration
- **Combined with Customer Journey Map**: Journey map is a core tool for the Empathize phase
- **Combined with RICE**: When focusing in the Ideate phase, use RICE to prioritize creative ideas
