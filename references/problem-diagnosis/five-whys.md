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

⚠️ **When NOT to use**
- Multiple independent root causes are plausible from the start — a single forced chain hides the branches; map with Fishbone first
- The system behaves as a feedback loop (causes and effects reinforce each other) — linear why-chains mislead on entangled systems; use Systems Thinking
- No evidence exists to check any "why" step (no logs, no data, no observations) — the output would be plausible fiction, not diagnosis; gather data first (see Red Flags in SKILL.md)
- The root cause is structural or political — 5 Whys can identify it but cannot resolve it; pair the finding with organizational tools

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

## Failure Modes

- **Stopping at symptoms**: the chain ends at Why 1-2 with a restated symptom → force the question until the level found is actionable (system/process/design), never a person
- **Evidence-free steps**: each "why" answered from plausibility instead of observation → every step carries its evidence; a step that cannot be verified ends the chain honestly ("cause not established" at that level)
- **Single-chain bias**: one tidy causal chain reported for a multi-cause problem → when a second chain surfaces mid-analysis, switch to Fishbone and branch
- **"Human error" terminal**: the chain stops at "someone made a mistake" — a non-actionable end → keep asking what made the error likely (system, process, training)

---

## Evidence Strength

Practitioner consensus for simple, chain-traceable causation — decades of Toyota Production System use. The specific "five" is convention, not calibration: stop at the actionable level, whether that takes three whys or seven. Contested for complex systems, where linear root-cause narratives can false-compress multi-factor failures (see When NOT to use).

---

## Relationship with Other Methodologies

- **Pair with Fishbone**: When there are multiple independent root causes, use Fishbone to map the full picture first, then apply 5 Whys to each branch
- **Output to RICE**: After root cause is confirmed, use RICE to prioritize fix solutions
- **Output to OKR**: Long-term prevention measures can be converted to OKR Key Results
