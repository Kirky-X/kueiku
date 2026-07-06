# AARRR Funnel · 海盗指标 / 增长漏斗

## Core Concept

A growth framework proposed by Dave McClure that decomposes the user lifecycle into five stages to systematically locate growth bottlenecks. The five letters spell out like a pirate's "AARRR," hence the name "Pirate Metrics."

```
Acquisition   — How do users find us?
Activation    — Do new users experience value on first use?
Retention     — Do users keep coming back?
Revenue       — How do we generate revenue from users?
Referral      — Do users actively recommend us to others?
```

> **Core Insight**: Most products' problems are not in acquisition, but in activation and retention. First identify the weakest funnel layer, then concentrate resources to fix it.

---

## Applicable Scenarios

✅ **Best For**
- Growth bottleneck identification ("Our growth has stalled — where's the problem?")
- First health diagnostic after product launch
- Baseline assessment before formulating quarterly growth strategy
- Team consensus alignment (unified language for discussing growth)

⚠️ **Use with Caution**
- Complex B2B sales processes (funnel needs extensive customization)
- Cold-start stage of new products (too little data for effective analysis)

---

## Five Layers Explained

### A1 · Acquisition

**Core Question**: Where do users come from? Which channel has the best acquisition cost and quality?

Key Metrics:
- Traffic volume by channel (SEO/Paid/Word-of-Mouth/Social/Content)
- CAC (Customer Acquisition Cost)
- Channel conversion rate (visitor → sign up)

Diagnostic Signals:
- 🔴 Very low traffic → Brand awareness / channel problem
- 🔴 High traffic but low signups → Landing page / value proposition problem

---

### A2 · Activation

**Core Question**: Do new users truly experience product value during their first use ("Aha Moment")?

Key Metrics:
- Sign-up to core action completion rate (e.g., sign up → send first message)
- New user D1/D3/D7 retention
- Onboarding completion rate

Diagnostic Signals:
- 🔴 Many signups but rapid drop-off → Activation failure, users didn't feel the value
- Find and quantify the product's **Aha Moment** (the specific action where users experience value)

---

### R1 · Retention

**Core Question**: Do users keep coming back? At which stage does churn occur?

Key Metrics:
- D1 / D7 / D30 retention
- MAU / DAU
- User return interval distribution
- Last behavior path of churned users

Diagnostic Signals:
- 🔴 Retention curve doesn't stabilize → Core product value insufficient, habit not formed
- 🔴 Significant drop-off at a specific time point → Product experience break at that milestone

---

### R2 · Revenue

**Core Question**: How efficient is our monetization?

Key Metrics:
- Conversion rate (free → paid)
- ARPU (Average Revenue Per User)
- LTV (Lifetime Value)
- LTV / CAC ratio (>3 is healthy, <1 is burning cash)

Diagnostic Signals:
- 🔴 LTV/CAC < 1 → Acquisition cost exceeds user value, business model unsustainable
- 🔴 Low paid conversion rate → Pricing / value communication / payment flow problem

---

### R3 · Referral

**Core Question**: Do users actively bring in new users?

Key Metrics:
- NPS (Net Promoter Score)
- K-factor (K = invite rate × invite acceptance rate; K>1 = viral growth)
- Referral channel share of total signups

Diagnostic Signals:
- 🔴 K-factor near 0 → Core product value not strong enough, or no referral mechanism
- 🟡 Low NPS → Overall product satisfaction low; improve product quality before pursuing referrals

---

## Execution Steps

### Step 1: Fill in Current Data

For all five layers, collect existing data or best estimates to build a baseline table.

### Step 2: Identify the Weakest Layer

Calculate conversion rate per layer to find where the **biggest funnel gap** is.

### Step 3: Deep-Dive into the Weakest Layer

For the weakest layer, further decompose:
- User segmentation (new vs returning? Channel A vs Channel B?)
- Behavioral path analysis (where in the flow do users drop off?)
- Qualitative research (use JTBD/user interviews to understand drop-off reasons)

### Step 4: Formulate Improvement Hypotheses

Propose 3-5 improvement hypotheses for the weak layer, prioritized using RICE scoring.

### Step 5: A/B Test → Iterate

---

## Output Template

```
Product: [Name]
Analysis time period: [Month]

AARRR Funnel Data:

Acquisition:
  Primary channel: [Channel name] — Share [%], CAC: [$]
  Total monthly new visitors: [N]
  Visitor → Signup conversion rate: [%]

Activation:
  Signup → Aha Moment completion rate: [%]
  Aha Moment definition: [Specific action]
  D1 retention: [%]

Retention:
  D7 retention: [%], D30 retention: [%]
  Peak churn milestone: [Day X]
  MAU: [N]

Revenue:
  Free → Paid conversion rate: [%]
  ARPU: [$]
  LTV: [$], CAC: [$], LTV/CAC: [x]

Referral:
  NPS: [Score]
  K-factor: [Value]
  Referral channel share of signups: [%]

Funnel Diagnosis:
  Weakest layer: [Layer name]
  Core problem: [...]
  Top 3 improvement hypotheses:
    1. [Hypothesis] — RICE score: [N]
    2. [...]
    3. [...]
```

---

## Relationships with Other Methodologies

- **Preceded by JTBD**: AARRR locates which layer the problem is in; JTBD explains why users drop off at that layer
- **Output feeds RICE**: Improvement hypothesis prioritization uses RICE
- **Combined with Customer Journey Map**: AARRR is the quantitative funnel; the journey map is the qualitative path — complementary usage
- **Combined with Lean BML**: AARRR discovers problems; BML loops validate solutions
