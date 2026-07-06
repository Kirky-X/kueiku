# First Principles Thinking

## Core Concept

Decompose a problem down to **indivisible basic facts (axioms)**, then reconstruct solutions from these fundamentals — rather than reasoning by analogy, convention, or "how the industry usually does it."

> Reasoning by analogy: Others do it this way, so we should too.
> First principles: Starting from physics/fundamental facts, how **should** this be done?

Elon Musk's articulation: *"I think it's important to reason from first principles. You boil things down to the most fundamental truths and then reason up from there, instead of reasoning by analogy."*

---

## When to Use

✅ **Best suited for**
- Existing solutions are too expensive, requiring disruptive redesign
- Constrained by industry "conventions" or "best practices," needing to break assumptions
- Innovative product/service design, building from scratch
- Evaluating whether something "impossible" is truly impossible

⚠️ **Use with caution**
- Time-sensitive everyday decisions (reasoning by analogy is more efficient)
- Mature solutions exist and no innovation is needed
- Team lacks deep understanding of foundational knowledge (reasoning will be ungrounded)

---

## Execution Steps

### Step 1: Clarify the Problem

Write the problem statement, making sure **not to embed a solution in the problem**.

```
❌ Solution-embedded: "We need to build a better battery factory"
✅ Neutral statement: "We need to store and use electrical energy at lower cost"
```

### Step 2: Identify and Challenge All Assumptions

List all assumptions behind the current solution, questioning each one:
- **Is this assumption a real physical/chemical/mathematical constraint, or a historical convention?**
- If this assumption didn't exist, how would the solution change?

| Assumption | Fact or Convention? | What is the real constraint? |
|------------|-------------------|------------------------------|
| EV batteries are expensive | Industry convention pricing | What is the actual market price of raw materials? |
| ... | ... | ... |

### Step 3: Find the Fundamental Facts

Dig down to truly indisputable **physical/chemical/mathematical/economic fundamentals**:

- What is the **atomic structure** of this material?
- What is the **physical limit** of this process?
- Stripping away all intermediaries, what is the **direct cost**?

### Step 4: Reconstruct from Fundamentals

Starting from the verified fundamentals in the previous step, **unconstrained by existing solutions**, derive new solutions:

- "Starting from fundamental facts, what is the theoretically optimal solution?"
- "Where is the gap between the current solution and the theoretical optimum?"
- "How can we design an approach to approach the theoretical optimum?"

### Step 5: Verify and Iterate

Does the new solution still hold up against fundamental facts? Has it introduced new implicit assumptions?

---

## Output Template

```
Problem statement: [Neutral description without embedded solution]

Assumption inventory:
  - Assumption A: [Description] → Nature: fact / convention / to be verified
  - Assumption B: [Description] → Nature: ...
  - ...

Fundamental facts:
  - Fact 1: [Indisputable constraint or data]
  - Fact 2: [...]
  - ...

Reconstruction from fundamentals:
  Theoretical optimum: [...]
  Gap with current solution: [...]
  New solution direction: [...]

Conclusions needing verification: [Which deduction steps still need experimental/data validation]
```

---

## Worked Example

**Problem**: How did SpaceX reduce rocket launch costs from $500M to $60M?

```
Traditional assumptions:
  - Rockets are highly complex precision devices, single-use is industry standard
  - Government-grade procurement processes determine cost structure
  - Aerospace supply chain prices are fixed

Digging to fundamental facts:
  - What is the market price of rocket materials (aluminum alloy, titanium alloy, carbon fiber)? → ~$2M
  - What is the physical cost of propellant (kerosene + liquid oxygen)? → ~$200K
  - Does reusability violate physical laws? → No

Reconstruction:
  - If material cost is only $2M, where does $500M come from? → Complex supply chain, certification processes, single-use design
  - Break the "single-use" assumption: Rockets can be reused like airplanes
  - Re-internalize supply chain: Vertical integration, build in-house rather than outsource

Conclusion: Reusability + vertically integrated supply chain → 10x cost reduction
```

---

## Common Pitfalls

| Pitfall | Description |
|---------|-------------|
| Pretending first principles while still reasoning by analogy | "Google does it this way, so from first principles this is correct" |
| Insufficient decomposition at the fundamental level | Stopping at "industry data" instead of "physical constraints" |
| Lack of feasibility verification in reconstruction | Purely theoretical derivation of perfect solutions, ignoring implementation constraints |
| Using it where no innovation is needed | Applying first principles to everyday operations is over-engineering |

---

## Relationship with Other Methodologies

- **Complements 5 Whys**: After 5 Whys identifies root causes, use first principles to design disruptive solutions
- **Precedes Design Thinking**: Introduce at the "ideate" stage of Design Thinking to break through conventional solutions
- **Opposes SWOT**: SWOT evaluates current constraints; first principles questions whether those constraints are real
