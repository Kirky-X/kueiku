# Framework Selection · Framework Selection Meta-Methodology

## Core Idea

Choosing a framework itself requires a methodology. When facing a problem, choosing the wrong framework leads to biased analysis direction, wasted resources, and invalid conclusions. This meta-methodology provides **5 principles + a decision tree** to help select the most fitting framework from among many.

> "If all you have is a hammer, everything looks like a nail." The essence of framework selection meta-methodology is: first assess the problem's nature, then choose the tool — not the other way around.

---

## Applicable Scenarios

✅ **Best suited for**
- Meta-decisions when facing complex problems and unsure which framework to use
- Alignment tool when the team disagrees on framework selection
- Preventing framework misuse (using SWOT for quantitative analysis, using BCG for single-product analysis, etc.)
- Training newcomers on framework awareness

⚠️ **Use with caution**
- When the problem clearly maps to a single framework (no meta-decision needed, just use it)
- Extremely time-sensitive situations (act first, reflect later, skip selection)
- When the team is unfamiliar with all candidate frameworks (training needed first; selecting won't help)

---

## Execution Steps

### Step 1: Determine Problem Type (Principle 1)

Classify the problem, mapping to different framework families:

```
Problem type → Framework family mapping:
  Analysis (understand current state)  → SWOT / PESTLE / Five Forces / Value Chain
  Decision (choose one from many)      → Decision Matrix / RICE / Eisenhower
  Creative (generate solutions)        → SCAMPER / Six Thinking Hats / Connecting Dots
  Diagnostic (find root cause)         → 5 Whys / FMEA / Pre-mortem
  Planning (set direction)             → OKR / Ansoff / BCG / STP
  Evaluation (score and rank)          → RICE / Decision Matrix / GE Matrix
```

### Step 2: Assess Information Sufficiency (Principle 2)

```
Information sufficiency → Framework type matching:
  Low information / uncertain   → Exploratory frameworks (Lean Canvas / Empathy Map / Cynefin)
  Moderate information          → Diagnostic frameworks (SWOT / Five Forces / Value Chain)
  Sufficient information        → Quantitative frameworks (RICE / Decision Matrix / BCG Matrix)

Signals:
  Exploratory: Assumptions unverified, data missing, problem boundaries unclear
  Diagnostic: Qualitative information available but no precise data
  Quantitative: Reliable data available for scoring
```

### Step 3: Assess Time Constraints (Principle 3)

```
Time constraints → Framework depth matching:
  Urgent (hours)    → Quick frameworks (Eisenhower / 5 Whys / MECE single-level decomposition)
  Moderate (days)   → Standard frameworks (SWOT / Decision Matrix / RICE)
  Relaxed (weeks)   → Deep frameworks (PESTLE / BCG / McKinsey 7S / Value Chain)
```

### Step 4: Assess Output Format (Principle 4)

```
Required output format → Framework format matching:
  Checklist  → MoSCoW / 5 Whys / Pre-mortem
  Matrix     → BCG / GE / Eisenhower / Decision Matrix
  Narrative  → SWOT cross-analysis / Customer Journey / Strategic Group
  Numbers    → RICE / BCG share / RFM scoring
  Canvas     → BMC / Lean Canvas / Empathy Map
```

### Step 5: Assess Team Familiarity (Principle 5)

```
Team familiarity → Selection strategy:
  Team all familiar     → Use directly
  Some familiar         → Experienced guide newcomers, add alignment time
  None familiar         → If training cost > framework benefit, switch to a familiar framework or use a simple one first
```

> An "advanced" framework that the team is unfamiliar with produces far worse results than a "simple" framework they use proficiently.

### Step 6: Synthesize Decision Tree

Chain the 5 principles into a decision flow:

```
Decision flow:
  1. Problem type? → Narrow to framework family
  2. Information sufficiency? → Exploratory / Diagnostic / Quantitative
  3. Time constraints? → Quick / Standard / Deep
  4. Output format? → Checklist / Matrix / Narrative / Numbers / Canvas
  5. Team familiarity? → Use directly / Train / Switch framework
  ↓
  Output: Selected framework + Alternative framework + Selection rationale
```

---

## Output Template

```
Framework Selection Decision

I. Problem Statement
  [One-sentence problem description]

II. 5-Principle Assessment
  Principle 1 (Problem type): [Analysis / Decision / Creative / Diagnostic / Planning / Evaluation] → Framework family: [...]
  Principle 2 (Information sufficiency): [Low / Moderate / Sufficient] → Framework type: [Exploratory / Diagnostic / Quantitative]
  Principle 3 (Time constraints): [Urgent / Moderate / Relaxed] → Framework depth: [Quick / Standard / Deep]
  Principle 4 (Output format): [Checklist / Matrix / Narrative / Numbers / Canvas] → Framework format: [...]
  Principle 5 (Team familiarity): [All familiar / Some familiar / None familiar] → Selection strategy: [...]

III. Candidate Framework Screening
  Candidate 1: [Framework] — 5-principle match: [...]
  Candidate 2: [Framework] — 5-principle match: [...]

IV. Final Selection
  Selected framework: [...]
  Alternative framework: [...] (switch when primary is not applicable)
  Selection rationale: [...]
  Known limitations: [...] (blind spots of this framework in this scenario)
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|---------|-------------|
| Choosing only because of familiarity, ignoring fit | Force the 5-principle assessment, document match rationale |
| One framework for everything | Identify problem type, match different framework families |
| Ignoring team familiarity and choosing "advanced" frameworks | When training cost > benefit, switch frameworks |
| Not documenting limitations after selection | Must record this framework's blind spots in this scenario |
| Meta-decision itself takes too long | Meta-decision should complete within 15 minutes; otherwise it's overdone |
| Choosing wrong framework and persisting stubbornly | Set checkpoints; switch to alternative when framework doesn't work |

---

## Relationship with Other Methodologies

- **This methodology is the meta-layer of all other methodologies**: Choose the framework first, then use it. This methodology governs "choosing."
- **Complements Cynefin**: Cynefin determines the problem domain (clear/complicated/complex/chaotic), deepening Principle 1
- **Complements First Principles**: When no existing framework is available, fall back to first principles
- **Complements Reframe and Elevate**: When no framework works, reframe the problem first, then select a framework
