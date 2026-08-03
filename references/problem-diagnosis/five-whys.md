# 5 Whys — Root Cause Analysis

## Core Concept
By repeatedly asking "why" (typically 5 times), pierce through the symptoms of a problem to find the **actionable root cause**. Created by Sakichi Toyoda, it is a core tool of the Toyota Production System (TPS).

> Symptoms are just symptoms; root causes are the disease. Treating symptoms leads to recurrence; solving root causes leads to cure.

---

## Applicable Scenarios

✅ **Best for**
- Production incident post-mortems
- Business metric anomaly decline
- Process errors or quality issues
- Results consistently below expectations

⚠️ **Use with caution**
- Problem has multiple independent root causes (use Fishbone instead)
- Root cause is structural/political (5 Whys can identify but not resolve)
- Insufficient data to support each why step

---

## Execution Steps

### Step 1: Clearly define the problem statement

Write a clear problem statement including: **what went wrong + when + impact scope**

```
❌ Vague: "System is slow"
✅ Clear: "Since 2024-06-01 14:00, payment API response time increased from 200ms to 3000ms, affecting ~30% of users"
```

### Step 2: First Why

For the problem statement, ask: **"Why did this happen?"**

Write the direct cause, supported by facts (logs, data, observations). No guessing without verification.

### Step 3-5: Continue asking

For each previous answer, ask "why" until:
- You reach an actionable root cause (a level where action can be taken)
- Or the question can no longer be asked (reached system/human/resource constraint level)

**Each step requires validation:** Is this cause supported by data or evidence?

### Step 6: Define corrective actions

For the **final root cause** (usually at the 4th-6th level), define:
- Immediate fix (treat the symptom)
- Long-term prevention (treat the disease)

---

## Output Template

```
Problem Statement: [specific, quantifiable problem description]

Why 1: [direct cause] — Evidence: [...]
  Why 2: [deeper cause] — Evidence: [...]
    Why 3: [deeper cause] — Evidence: [...]
      Why 4: [deeper cause] — Evidence: [...]
        Why 5: [root cause] — Evidence: [...]

Root Cause: [one-sentence summary]

Corrective Actions:
  - Immediate (symptom): [...]
  - Long-term (disease): [...]
  - Owner / timeline: [...]
```

---

## Execution Example

**Problem**: User complaints up 40%, support tickets from 200 to 280/day

```
Why 1: Why did tickets increase?
→ App update made onboarding confusing; many users don't know how to complete first-time setup

Why 2: Why is onboarding confusing?
→ New onboarding was ported directly from B2B product, not redesigned for end consumers

Why 3: Why wasn't it redesigned for consumers?
→ Tight iteration schedule; onboarding optimization was deprioritized as low priority

Why 4: Why was onboarding deprioritized?
→ No user behavior data to support onboarding's impact; prioritization was purely subjective

Root Cause: Lack of user behavior data tracking prevents quantifying new user experience value in product decisions

Corrective Actions:
  Immediate: Add temporary video tutorial popup (handled by support)
  Long-term: ① Add analytics tracking ② Build onboarding funnel monitoring ③ Standardize onboarding priority assessment
```

---

## Common Pitfalls

| Pitfall | Description | How to avoid |
|---------|-------------|-------------|
| Stopping at symptoms | Stopping at Why 1-2, only finding symptoms | Force asking until reaching actionable systemic root cause |
| Jumping to conclusions | Logic between steps is not rigorous, skipping based on gut feeling | Each step must have evidence support |
| Single root cause bias | Attributing complex problems to just one cause | When multiple Why chains emerge, supplement with Fishbone |
| Stopping at "human error" | Root cause is "someone made a mistake" — this is not actionable | Keep asking: why did this person make a mistake? What went wrong in system/process/training? |

---

## Relationship with Other Methodologies

- **Pair with Fishbone**: When there are multiple independent root causes, use Fishbone to map the full picture first, then apply 5 Whys to each branch
- **Output to RICE**: After root cause is confirmed, use RICE to prioritize fix solutions
- **Output to OKR**: Long-term prevention measures can be converted to OKR Key Results
