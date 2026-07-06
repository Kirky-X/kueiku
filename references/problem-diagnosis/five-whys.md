# 5 Whys · Root Cause Analysis

## Core Philosophy

By asking "Why" consecutively, we penetrate through surface symptoms to find the **actionable root cause**. Created by Sakichi Toyoda, it is a core tool of the Toyota Production System (TPS).

> Symptoms are manifestations; the root cause is the true source. Treating symptoms only leads to recurrence; resolving the root cause ensures lasting resolution.

---

## Applicable Scenarios

✅ **Best Suited For**
- Production incident post-mortems
- Significant business metric declines
- Process errors or quality issues
- Persistent results deviating from expectations

⚠️ **Use with Caution**
- When the problem has multiple independent root causes (use Fishbone instead)
- When root causes are structural/political (5 Whys can identify but may be difficult to resolve)
- When insufficient data supports each step of questioning

---

## Execution Steps

### Step 1: Clearly Define the Problem Statement

Write a clear problem statement that includes: **What went wrong + When + Scope of impact**

```
❌ Vague: "System is slow"
✅ Clear: "Starting from 2024-06-01 14:00, payment API response time increased from 200ms to 3000ms, affecting approximately 30% of users"
```

### Step 2: First Round of Why

For the problem statement, ask: **"Why did this happen?"**

Write the direct cause, supported by factual evidence (logs, data, observations). Unverified guesses are not permitted.

### Step 3-5: Continue Questioning

For each answer from the previous step, continue asking "Why" until:
- An actionable root cause is reached (a level where action can be taken to resolve)
- Or questioning cannot continue further (reached the system/human nature/resource constraint level)

**Each step must be verified:** Is this cause supported by data or evidence?

### Step 6: Define Remediation Actions

For **the final root cause** (typically at levels 4-6), develop:
- Immediate fix (treat symptoms)
- Long-term prevention (address root cause)

---

## Output Template

```
Problem Statement: [Specific, quantifiable problem description]

Why 1: [Direct cause] — Evidence: [...]
  Why 2: [Deeper cause] — Evidence: [...]
    Why 3: [Deeper cause] — Evidence: [...]
      Why 4: [Deeper cause] — Evidence: [...]
        Why 5: [Root Cause] — Evidence: [...]

Root Cause: [One-sentence summary]

Remediation Actions:
  - Immediate (symptom treatment): [...]
  - Long-term (root cause treatment): [...]
  - Owner / Deadline: [...]
```

---

## Execution Example

**Problem**: User complaints increased by 40%, customer service tickets rose from 200 to 280/day

```
Why 1: Why did ticket volume increase?
→ The onboarding flow after the APP update confused users, many were unable to complete their first actions

Why 2: Why did the onboarding flow confuse users?
→ The new flow was directly migrated from the B-end product without redesign for C-end users

Why 3: Why wasn't it redesigned for C-end users?
→ Product iteration schedule was tight, and onboarding optimization was considered low priority and skipped

Why 4: Why was onboarding optimization considered low priority?
→ Priority ranking lacked data to support the impact of onboarding, relying entirely on subjective judgment

Root Cause: Lack of user behavior data tracking prevented product decisions from quantifying the value of user onboarding experience

Remediation Actions:
  Immediate: Temporarily add video guide popups (handled by customer service)
  Long-term: ① Implement event tracking ② Establish onboarding funnel monitoring ③ Standardize onboarding priority evaluation
```

---

## Common Pitfalls

| Pitfall | Description | Avoidance Method |
|---------|-------------|------------------|
| Stopping at symptoms | Stopping at Why 1-2, only identifying symptoms | Force questioning until an actionable systemic root cause is reached |
| Leaping inference | Lack of rigorous logic between steps, jumping based on intuition | Each step must be supported by evidence |
| Single root cause bias | Attributing complex problems to a single cause | When multiple Why chains are discovered, supplement with Fishbone |
| Stopping at people | Root cause is "someone's mistake" — this is not actionable | Continue questioning: Why did this person make a mistake? Where did the system/process/training fail? |

---

## Relationship with Other Methodologies

- **Combine with Fishbone**: When there are multiple independent root causes, use Fishbone to first map the full picture, then use 5 Whys to deeply explore each branch
- **Output feeds RICE**: Once root cause is confirmed, prioritize remediation solutions using RICE
- **Output feeds OKR**: Long-term prevention measures can be converted into OKR Key Results
