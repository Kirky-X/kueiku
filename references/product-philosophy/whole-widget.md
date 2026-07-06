# Whole Widget

## Core Philosophy

End-to-end responsibility (hardware + software + services), with key decisions kept in-house.

Vertical integration means that key decision points along the product chain must be under your own control — not "build everything yourself," but "build the key components that determine product experience yourself." The cost of outsourcing is not money, but loss of control over key decisions: when you hand over the component that determines user experience to a third party, you lose iteration speed and differentiation capability.

> **Key Distinction**: Whole Widget ≠ building everything in-house.
> - **In-house**: Key components that determine product experience differentiation (e.g., OS, chips, core algorithms)
> - **Outsource**: Standardized components that don't affect experience differentiation (e.g., power supplies, standard parts, general-purpose tools)

---

## Applicable Scenarios

✅ **Best For**
- Product architecture decisions: which components to build in-house vs. outsource/purchase
- Strategic choice between vertical integration and horizontal specialization
- When an outsourced component becomes an experience bottleneck or iteration blocker
- "Build vs. buy" decisions when entering a new domain

⚠️ **Use With Caution**
- Early-stage teams with severely limited resources (validate first, then integrate)
- Highly standardized components with no differentiation space (purchasing is more efficient)
- Short-term projects (integration is a long-term investment)

---

## Execution Steps

### Step 1: Identify Key Decision Points

List the complete product chain from input to delivery, and annotate each component:
- Does this component affect key differentiation in user experience?
- Is this component's capability a core moat of the product?
- If outsourced, can iteration remain rapid?

**Decision Criteria**: Affects differentiation + is a core moat + requires rapid iteration = key decision point, should be built in-house.

### Step 2: Evaluate Outsourcing Costs

For each candidate outsourced component, conduct a quantitative assessment:
- **Direct cost**: Purchase price vs. in-house cost (including labor/time)
- **Hidden cost**: Communication and coordination costs, iteration delays, information asymmetry
- **Opportunity cost**: Loss of capability accumulation and moat building after outsourcing
- **Exit cost**: Difficulty of switching suppliers or bringing development in-house

> Hidden costs and exit costs are often underestimated, and are the main cause of outsourcing decision failures.

### Step 3: Choose an Integration Strategy

Based on the distribution of key decision points, select an integration strategy:
- **Full vertical integration**: Key decision points are numerous and distributed (e.g., Apple hardware + OS + chips + services)
- **Key component integration**: Key decision points are concentrated (e.g., most SaaS products build core algorithms in-house + purchase cloud services)
- **Platform-based integration**: Build a platform layer, with ecosystem collaboration above (e.g., iOS + App Store)

### Step 4: Assess Integration Level

Regularly evaluate integration effectiveness:
- Is the iteration speed of key decision points meeting targets?
- Are outsourced components becoming experience bottlenecks?
- Are the marginal benefits of integration still greater than the marginal costs?

> Integration is not a one-time decision — it needs to be dynamically adjusted as the product matures.

---

## Output Template

```
Analysis Target: [Product/Business]
Analysis Date: [Date]

Product Chain Component Inventory:
  1. [Component Name] | Affects Differentiation: High/Medium/Low | Core Moat: Yes/No | Iteration Frequency: High/Low
  2. [...]

Key Decision Points (should be in-house):
  1. [Component Name] — Rationale: [...]
  2. [...]

Outsourcing Cost Assessment Table:
  | Component | Direct Cost | Hidden Cost | Opportunity Cost | Exit Cost | Decision |
  |-----------|------------|-------------|-----------------|-----------|----------|
  | ...       | ...        | ...         | ...             | ...       | In-house/Outsource |

Integration Strategy: [Full vertical / Key component / Platform-based]
Rationale: [...]

Integration Level Assessment Metrics:
  - Key decision point iteration speed: [Target value]
  - Outsourced component experience bottlenecks: [Monitoring items]
  - Marginal benefit/cost ratio: [Evaluation period]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Equating "build everything yourself" with vertical integration | Only build in-house the key decision points; standardizing components for purchase is more efficient |
| Only calculating direct costs, ignoring hidden/exit costs | All four types of costs must be fully assessed |
| Making a one-time decision without revisiting | Integration level needs regular assessment and adjustment as the product matures |
| Building non-key components in-house for "sense of control" | Sense of control ≠ differentiation; avoid NIH syndrome |
| Losing capability accumulation after outsourcing | Even when outsourcing, maintain technical judgment capability |

---

## Relationship with Other Methodologies

- **Preceded by Focus as No**: After focusing on "what to do," then decide "how to do it"
- **Complementary to Technology Meets Humanities**: Integration decisions must consider both technical feasibility and human experience
- **Followed by Invisible Perfection**: In-house components need craft standards to ensure quality
- **Contrasted with VRIO Framework**: Use VRIO to assess whether in-house components constitute a sustainable competitive advantage
