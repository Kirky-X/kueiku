# Lean Build-Measure-Learn · 精益创业循环

## Core Concept

Proposed by Eric Ries in *The Lean Startup*. Core thesis: **entrepreneurship (or product development) is fundamentally a process of learning under extreme uncertainty**.

Minimize the cycle time for "turning hypotheses into knowledge," not maximize "feature delivery volume."

```
      Build
    ↗      ↘
Ideas          Product
    ↖      ↙
      Measure  ← Data
           ↓
          Learn
```

> Not "build the product as fast as possible," but "validate or invalidate hypotheses as fast as possible."

---

## Core Concepts

### MVP (Minimum Viable Product)

A version that uses **minimum resources** to validate the **most critical hypothesis**.

MVP is NOT: an incomplete product, a beta version, "start small and grow later"

MVP IS: an **experiment designed to validate a single most critical hypothesis**

MVP Types:
| Type | Description | Suitable for Validating |
|------|------|---------|
| Smoke Test | Launch landing page to collect signups, but product doesn't exist yet | Whether demand exists |
| Wizard of Oz | Backend is manual; user thinks it's automated | Validate process before automation |
| Concierge MVP | Fully manual service, validating service value | Concierge MVP |
| Video MVP | An explanatory product video (e.g., Dropbox) | Demand validation |
| Landing Page + Payment MVP | Require user payment, observe conversion | Willingness to pay |
| Feature MVP | Core path only; everything else stripped | Core value validation |

### Key Hypothesis Identification

Before Build, clarify:
- **What is the highest-risk hypothesis** (if this hypothesis is wrong, the entire product collapses)?
- How to design an experiment to quickly validate/invalidate it?

Hypothesis types:
- **Value Hypothesis**: Does the user find the product valuable?
- **Growth Hypothesis**: Will the product grow in the expected way?
- **Feasibility Hypothesis**: Can we technically implement it?

---

## Applicable Scenarios

✅ **Best For**
- Early-stage product validation (0→1)
- New feature direction exploration (is it worth full development?)
- Validation before major product direction pivots
- Growth hypothesis testing (improvement plans for a layer in AARRR)

⚠️ **Use with Caution**
- Engineering execution for already-validated products (should optimize efficiency, not run hypothesis tests)
- Highly regulated industries (finance/healthcare — MVPs may have compliance risks)

---

## Execution Steps

### Step 1: Clarify the Current Most Critical Hypothesis

```
We believe: [User/Market/Technology hypothesis]
We will validate this through: [What metric]
If [metric] reaches [target] within the validation period, the hypothesis holds.
```

### Step 2: Design the MVP

Choose the MVP type that **minimizes effort** while **effectively validating the hypothesis**:
- Don't "prepare extra, just in case"
- Each MVP validates only one core hypothesis

### Step 3: Build

Execute with minimum necessary scope, with a clear time limit (typically 1-2 weeks).

### Step 4: Measure

Define **leading indicators**, not just lagging metrics:

| Metric Type | Description | Examples |
|---------|------|------|
| Leading indicators | Behavioral metrics that predict future outcomes | Feature click rate, content creation rate |
| Lagging indicators | Outcome metrics, slow to respond | MAU, revenue |

Avoid vanity metrics:
- 🚫 Download count (doesn't reflect whether it's used)
- 🚫 Registered users (doesn't reflect retention)
- ✅ 7-day active rate, core feature usage rate, NPS

### Step 5: Learn

Answer three questions:
1. Does the hypothesis hold? (Based on data, not feelings)
2. If yes → **Persevere**: what is the next most critical hypothesis?
3. If no → **Pivot**: which dimension to adjust?

**Common Pivot Types:**
- Customer Segment Pivot: Same product, different target audience
- Problem Pivot: Solve a different problem for the same users
- Business Model Pivot: Same product, different monetization method
- Channel Pivot: Same product, different acquisition channel
- Platform Pivot: From application to platform (or vice versa)

---

## Output Template

```
Current Loop #[N]

Hypothesis:
  We believe: [Specific hypothesis statement]
  Validation metric: [Metric name] reaching [target]
  Validation deadline: [Date]
  Failure condition: [What outcome indicates the hypothesis is wrong]

Build:
  MVP type: [Type]
  Build scope: [...]
  Time limit: [N days/weeks]

Measure:
  Core metric: [Metric] = [Actual value] vs Target [target]
  Supporting data: [...]
  Qualitative feedback: [...]

Learn:
  Hypothesis validated? Yes / No / Partially
  Key insight: [...]
  Decision:
    □ Persevere — Next hypothesis: [...]
    □ Pivot — Adjust direction: [...]
    □ Stop — Reason: [...]
```

---

## Relationships with Other Methodologies

- **Preceded by Design Thinking**: Design thinking produces conceptual direction; BML loops validate and iterate on concepts
- **Combined with AARRR**: AARRR locates bottleneck layers; BML loops test improvement plans
- **Combined with RICE**: Before running BML loops, use RICE to decide which hypothesis to test
- **Uses 5 Whys**: After BML loop tests fail, use 5 Whys to analyze failure causes
