# FMEA · Failure Mode and Effects Analysis

## Core Concept

Systematically identify potential failure modes, score each failure by **Severity (S) × Occurrence (O) × Detection (D)**, calculate **Risk Priority Number RPN = S × O × D**. Sort by RPN from high to low, design preventive measures for high-risk items, then recalculate RPN to verify improvement.

> Rather than firefighting afterward, it's better to prevent fires in advance. FMEA transforms "what could go wrong" thinking from reactive to proactive, from ad hoc to systematic.

---

## Applicable Scenarios

✅ **Best suited for**
- Risk prevention during product design (Design FMEA)
- Quality control in production/service processes (Process FMEA)
- Risk identification in safety-critical systems (medical, aviation, automotive)
- Risk assessment before new process launch
- Failure prevention at critical supply chain nodes

⚠️ **Use with caution**
- Strategic-level risks (Pre-mortem is more appropriate)
- When quick risk overview is needed (FMEA is too detailed and slow)
- Retrospective analysis of failures that have occurred (use 5 Whys + Fishbone)
- Creative ideation phase (FMEA is a convergent tool, not suitable for early divergence)

---

## Execution Steps

### Step 1: Define Analysis Object and Break Down

Clarify analysis scope, break down system/process into analyzable components or steps:

```
Analysis object: [System/Process name]
Analysis type: Design FMEA / Process FMEA

Component/Step breakdown:
  1. [Component A / Step 1]
  2. [Component B / Step 2]
  3. [Component C / Step 3]
  ...
```

### Step 2: Identify Potential Failure Modes

For each component/step, list **all possible failure modes**:

```
Component: [Component A]
  Failure mode 1: [e.g., Connection timeout]
  Failure mode 2: [e.g., Returning incorrect data]
  Failure mode 3: [e.g., Complete non-response]
```

> Key: Don't just list "broken" — specify "how it breaks" — different failure modes have completely different impacts and probabilities.

### Step 3: Describe Failure Effects and Assess Severity (S)

For each failure mode, describe its impact on system/user, and score from 1-10:

```
Severity scoring criteria:
  1  — Almost no impact, user won't notice
  2-3 — Minor impact, user can recover themselves
  4-5 — Moderate impact, degraded function but still usable
  6-7 — Serious impact, core function unavailable
  8-9 — Extremely serious, safety risk or data loss
  10 — Catastrophic, system crash or personnel injury
```

### Step 4: Assess Occurrence (O)

Evaluate the probability of this failure mode occurring, score from 1-10:

```
Occurrence scoring criteria:
  1  — Extremely unlikely (<1/100,000)
  2-3 — Rare (1/10,000 ~ 1/1,000)
  4-5 — Occasional (1/1,000 ~ 1/100)
  6-7 — Moderate (1/100 ~ 1/10)
  8-9 — Frequent (1/10 ~ 1/2)
  10 — Almost certain (>1/2)
```

### Step 5: Assess Detection (D)

Evaluate **whether the failure can be detected before impact occurs**, score from 1-10:

```
Detection scoring criteria:
  1  — Almost certainly detectable (automated monitoring + alerts)
  2-3 — Very likely detectable (regular checks + obvious symptoms)
  4-5 — Possibly detectable (detection methods exist but imperfect)
  6-7 — Difficult to detect (relies on manual inspection)
  8-9 — Very difficult to detect (no effective detection methods)
  10 — Almost impossible to detect (hidden failure)
```

> Note: Higher D is more dangerous — it means the failure has occurred and you don't know about it.

### Step 6: Calculate RPN and Sort

```
RPN = S × O × D

Component | Failure mode | S | O | D | RPN
[A]  | [Mode 1] | 8 | 4 | 6 | 192
[A]  | [Mode 2] | 5 | 3 | 3 |  45
[B]  | [Mode 1] | 9 | 3 | 8 | 216
[C]  | [Mode 1] | 6 | 5 | 4 | 120
```

### Step 7: Design Preventive Measures for High RPN Items

Prioritize items with highest RPN (typically RPN > 100 or Top 3):

```
High RPN item: [Component B-Mode 1] RPN=216
  Preventive measures (reduce O): [...]
  Detection measures (reduce D): [...]
  Responsible person/Deadline: [...]
```

### Step 8: Recalculate RPN to Verify Improvement

```
Component | Failure mode | S | O | D | RPN | S'| O'| D'| RPN'
[B]  | [Mode 1] | 9 | 3 | 8 | 216 | 9 | 2 | 3 |  54
```

Significant RPN reduction indicates measures are effective.

---

## Output Template

```
FMEA Analysis Report

Analysis object: [...]
Analysis type: Design / Process
Analysis date: [...]
Team: [...]

FMEA Worksheet:

Item | Component | Failure mode | Effect | S | Cause | O | Current controls | D | RPN
  1   | [...] | [...]   | [...] |[S]| [...] |[O]| [...]   |[D]| [RPN]
  2   | [...] | [...]   | [...] |[S]| [...] |[O]| [...]   |[D]| [RPN]
  ...

High-risk items (RPN > [threshold]):

  ① [Component-Failure mode] RPN=[...] — Preventive measures: [...] — Detection measures: [...] — Responsible person: [...]
  ② [Component-Failure mode] RPN=[...] — Preventive measures: [...] — Detection measures: [...] — Responsible person: [...]

Post-measure RPN verification:

Item | Original RPN | Measure | S'| O'| D'| New RPN | Improvement rate
  1   | [...]  | [...] |[S']|[O']|[D']| [...]  | [X]%
  2   | [...]  | [...] |[S']|[O']|[D']| [...]  | [X]%

Conclusions and recommendations: [...]
```

---

## Execution Example

**Scenario**: Process FMEA for online payment process

```
Analysis object: User online payment process
Analysis type: Process FMEA

FMEA Worksheet:

Item | Step     | Failure mode       | Effect              | S | Cause          | O | Current controls    | D | RPN
  1   | Initiate payment | Payment channel timeout   | User cannot complete payment   | 8 | High channel load    | 5 | None          | 8 | 320
  2   | Initiate payment | Duplicate deduction      | User overcharged      | 9 | Idempotency not implemented    | 2 | Reconciliation check    | 5 | 90
  3   | Verify signature | Signature verification failure   | Legitimate payment rejected    | 6 | Certificate expired      | 3 | Certificate monitoring    | 4 | 72
  4   | Callback notification | Notification lost      | Order status out of sync    | 7 | Message queue failure  | 4 | None          | 7 | 196
  5   | Callback notification | Notification delayed      | User anxiety waiting      | 5 | Processing queue backlog  | 6 | None          | 6 | 180

High-risk items (RPN > 100):

  ① Initiate payment - Channel timeout RPN=320
    Preventive measures: Connect backup payment channel, auto-switch when main channel times out
    Detection measures: Real-time monitoring of payment channel response time, alert when >2s
    Responsible person: Payment team / Within 2 weeks

  ② Callback notification - Notification lost RPN=196
    Preventive measures: Message queue persistence + at-least-once delivery + consumer-side idempotency
    Detection measures: Scheduled reconciliation between order status and payment status, 5min interval
    Responsible person: Order team / Within 1 week

  ③ Callback notification - Notification delayed RPN=180
    Preventive measures: Increase consumer instance count, set backlog alerts
    Detection measures: Queue depth monitoring, alert when >1000
    Responsible person: Infrastructure team / Within 1 week

Post-measure RPN verification:

Item | Original RPN | Measure              | S'| O'| D'| New RPN | Improvement rate
  1   | 320   | Backup channel + monitoring alerts  | 8 | 2 | 2 |  32   | 90%
  4   | 196   | Persistence + reconciliation       | 7 | 2 | 2 |  28   | 86%
  5   | 180   | Capacity expansion + depth monitoring     | 5 | 3 | 2 |  30   | 83%
```

---

## Common Pitfalls

| Pitfall | Description | How to Avoid |
|------|------|---------|
| Failure modes too vague | "System failure" is not a failure mode, "payment channel timeout" is | Each failure must be specific to observable phenomena |
| Inconsistent scoring | Different people score the same failure with large differences | Team scores together, use scoring criteria table for alignment |
| Only reducing O not D | Only focusing on prevention, ignoring detection capability improvement | Measures must consider reducing both O and D |
| RPN threshold | Different industries have different reasonable thresholds | Set thresholds based on industry conventions and risk tolerance |
| Not updating after completion | FMEA is a living document, not updated after system changes | Update corresponding FMEA items after each system/process change |
| Ignoring low S high D items | Low severity but high detection failures easily overlooked | High D means hidden risk, pay special attention |

---

## Relationship with Other Methodologies

- **Combined with 5 Whys**: FMEA identifies "what could go wrong," 5 Whys asks "why did it go wrong"
- **Combined with Fishbone**: FMEA lists failure modes, Fishbone expands each failure's causal chain
- **Combined with Pre-mortem**: Pre-mortem does strategic-level risk forecasting, FMEA does execution-level risk quantification
- **Input to RICE**: Preventive measures for high RPN items can be candidate tasks for RICE evaluation
- **Combined with Pareto Analysis**: Use Pareto to verify if a few failure modes contribute most of the risk