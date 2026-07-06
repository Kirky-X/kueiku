# Fishbone Diagram

## Core Concept

Systematically visualize all potential causes of a problem in **multiple dimensions** to avoid missing cause categories. Shaped like a fishbone: fish head = problem, main bones = major cause categories, small bones = specific causes.

Invented by Japanese quality management expert Kaoru Ishikawa in the 1960s.

> 5 Whys digs vertically deep; Fishbone spreads horizontally wide — they complement each other.

---

## When to Use

✅ **Best suited for**
- Problems with **multiple independent causes** (5 Whys can only handle a single causal chain)
- **Team collaboration** brainstorming causes (Fishbone's visual structure facilitates discussion)
- Quality problem analysis in manufacturing/engineering
- Full-picture mapping of complex business problems

⚠️ **Use with caution**
- Problems with a single clear root cause (5 Whys is more direct)
- Scenarios requiring quantitative analysis (Fishbone is a qualitative tool)

---

## Common Classification Frameworks

### 6M Framework (Manufacturing/Engineering)

| Category | English | Description |
|----------|---------|-------------|
| Man / People | Man / People | Human operation, skills, fatigue, negligence |
| Machine | Machine | Equipment failure, tool wear, calibration issues |
| Material | Material | Raw material quality, supplier issues |
| Method | Method | Processes, operating procedures, standards |
| Measurement | Measurement | Measurement bias, instrument precision |
| Milieu/Environment | Milieu/Environment | Temperature, humidity, noise, work environment |

### 4P Framework (Service/Marketing)

| Category | Description |
|----------|-------------|
| Policies | Policy rules, approval processes, SOPs |
| Procedures | Operating steps, execution methods |
| People | Team capabilities, training, collaboration |
| Plant | Systems, tools, physical space |

### 8P Framework (Internet/Product, Custom)

Customize categories based on product characteristics, for example:
- **Product**: Feature defects, design issues
- **Platform**: System stability, performance
- **Process**: R&D process, collaboration methods
- **People**: Skills, resources
- **Data**: Data quality, monitoring coverage
- **External**: Third-party dependencies, policies

---

## Execution Steps

### Step 1: Define the Problem (Fish Head)

Write a **clear, specific** problem statement on the right side of the diagram (same requirements as 5 Whys).

### Step 2: Choose a Classification Framework

Select 6M / 4P / custom framework based on the problem domain, and draw the main bones.

### Step 3: Brainstorm Causes

For each category, **brainstorm** all possible causes and write them on the corresponding small bones:
- Don't evaluate, diverge first
- Encourage asking "what causes this cause?" (can branch further into sub-bones)
- Describe each cause using **noun phrases**, not solutions

### Step 4: Organize and Verify

- Mark **high-probability** causes (supported by data/observations)
- Identify **cause cluster areas** (which category has the most issues)
- Determine which causes need **further verification**

### Step 5: Prioritize

Select the top 3-5 most likely root causes for deep investigation (you can apply 5 Whys to each one).

---

## Output Template (Text Version)

```
Problem (Fish Head): [Specific problem statement]

Analysis Framework: [6M / 4P / Custom]

Cause Mapping:

【People】
  - [Cause A]
  - [Cause B]
  - [Cause B.1] (sub-cause of Cause B)

【Method】
  - [Cause C]
  - [Cause D]

【Machine / Platform】
  - [Cause E]

【Material / Data】
  - [Cause F]

【Environment / External】
  - [Cause G]

High-priority causes (need further investigation):
  1. [Cause X] — Evidence/rationale: [...]
  2. [Cause Y] — Evidence/rationale: [...]
  3. [Cause Z] — Evidence/rationale: [...]
```

---

## Worked Example

**Problem**: After the new app version launch, 7-day retention dropped from 42% to 28%

```
【Product/Features】
  - Core feature entry point buried, users can't find it
  - New tab bar design unfamiliar to users
  - Homepage information density too high, increased cognitive load

【Technology/Performance】
  - New package size increased, crash rate on low-end devices rose
  - Image lazy loading delays causing blank screens

【Process/Testing】
  - A/B test coverage insufficient, only tested 5% of users
  - Retention metrics not monitored during testing, only DAU was checked

【Data/Tracking】
  - New version tracking gaps, user behavior paths not traceable

【External/Competitive】
  - Competitors launched similar features simultaneously (diverting traffic)

High priority:
  1. Core feature entry point buried — Heatmap data shows 60% drop in core path clicks
  2. Low-end device crash rate increase — Crash reports show rate rose from 0.3% to 2.1%
  3. A/B test process deficiency — This test confirmed retention metrics were not included
```

---

## Relationship with Other Methodologies

- **Combined with 5 Whys**: Fishbone spreads the full picture, 5 Whys digs deep into key causes
- **Feeds into RICE**: Solutions for high-priority causes can be prioritized using RICE
- **Combined with data analysis**: Fishbone generates hypotheses, data analysis validates them
