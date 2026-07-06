# Focus as No

## Core Philosophy

Focus is not about saying "yes" — it's about saying "no." What truly defines a product's shape is not "what was added," but "what was cut."

This methodology opposes the passive response model of "ask users what they want, then comply" — user research is necessary, but users' surface-level requests are often just combinations of things they've already seen, making it difficult to produce breakthrough innovation. It advocates deeply understanding the essence of the task (job-to-be-done) and proactively eliminating all non-core temptations.

> **Boundary Annotation (Important)**
> - This methodology opposes "ask what they want, then comply." It does **not** oppose "deeply understanding the task."
> - In engineering tasks, do not misapply this as "don't listen to user requirements" — engineering requirements are contracts, not product bloat.
> - Applicable: Product feature trade-offs, scope expansion temptations.
> - Not applicable: Clear requirement contract fulfillment, bug fix scope, compliance requirements.

---

## Applicable Scenarios

✅ **Best For**
- Product feature bloat, wanting to do everything
- Early-stage products with limited resources that must make trade-offs
- Product iterations where existing feature lists need "trimming"
- Discussions about "users have raised many requests, should we do all of them?"

⚠️ **Use With Caution**
- Requirement trimming in engineering tasks (requirements are contracts, not bloat)
- Compliance/security requirements (cannot be "cut")
- Bug fix scope (fixing is an obligation)

---

## Execution Steps

### Step 1: Identify Temptations

List all features/requirements that are "wanted to be built," and annotate each:
- Source (user feedback / competitor following / internal assumptions / executive decision)
- Whether it corresponds to a real, observable task (JTBD)
- If not built, who would be affected and how severely

**Decision Criteria**: Items that cannot correspond to a real task, or "nobody would be truly affected if not built," are marked as "temptations."

### Step 2: Candidate Elimination List

Place all temptations in a candidate elimination list, specifying for each:
- Feature name
- Surface request (user says "I want X")
- Real task (what the user is actually trying to do)
- Whether existing solutions can cover this task

> If existing solutions can cover it, then the feature is redundant rather than innovative — it's a candidate for elimination.

### Step 3: Evaluate Elimination Consequences

Conduct "reverse validation" for each candidate elimination item:
- After elimination, how many users would be affected? (Quantify or estimate)
- Do affected users have alternative paths?
- What is the simplification benefit from elimination (maintenance cost / cognitive load / focus)?

Elimination is only confirmed when "simplification benefit > impact cost."

### Step 4: Lock in the Minimal Set

Clearly define the **locked set** (retained features) + **elimination set** (confirmed cuts), and set **escalation trigger conditions** for the locked set:
- What data metrics would trigger reconsidering a previously eliminated item?
- What user behavior signals indicate the judgment was wrong?

> Elimination without escalation trigger conditions is a one-time bet with no mechanism for course correction.

---

## Output Template

```
Analysis Target: [Product/Feature Module]
Analysis Date: [Date]

Candidate Temptation List:
  1. [Feature Name] | Source: [User/Competitor/Internal] | Corresponding Task: [Yes/No] | Impact Scope: [Description]
  2. [...]

Elimination Decision Table:
  | Feature | Surface Request | Real Task | Existing Solution Covers? | Elimination Consequence | Decision |
  |---------|----------------|-----------|--------------------------|------------------------|----------|
  | ...     | ...            | ...       | Yes/No                   | ...                    | Eliminate/Retain |

Locked Set (Retained Features):
  1. [Feature Name] — Retention Rationale: [...]
  2. [...]

Elimination Set (Confirmed Cuts):
  1. [Feature Name] — Elimination Rationale: [...]
  2. [...]

Escalation Trigger Conditions:
  - If [Metric X] reaches [Threshold], re-evaluate [Eliminated Item Y]
  - If [User Behavior Z] appears, re-evaluate [Eliminated Item W]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Accidentally cutting core features (cutting for the sake of cutting) | Each elimination item must pass dual validation: "real task + existing solution coverage" |
| Treating "user didn't mention it" as "user doesn't need it" | Proactively verify: is it a lack of need, or a lack of expression? |
| No correction mechanism after elimination | Must set escalation trigger conditions to avoid one-time bets |
| Misapplying this methodology in engineering tasks | Engineering requirements are contracts, not product scope trade-offs |
| Using "Jobs said no too" to justify arbitrary decisions | "Saying no" should be based on task analysis, not personal preference |

---

## Relationship with Other Methodologies

- **Preceded by JDB Value Proposition**: Use JTBD to identify real tasks and determine if features are redundant
- **Followed by RICE**: Use RICE within the locked set to prioritize execution
- **Followed by Invisible Perfection**: After focusing, polish the craft of retained features
- **Complementary to Whole Widget**: Focus as No focuses on "what to do"; Whole Widget focuses on "how to do it"
