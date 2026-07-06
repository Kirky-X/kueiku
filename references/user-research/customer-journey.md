# Customer Journey Map · 客户旅程地图

## Core Concept

Visualize the user's **end-to-end interaction** with a product / service, capturing user behavior, emotions, pain points, and opportunities at each touchpoint, helping teams understand the product experience from the **user's perspective** rather than a feature perspective.

Dimensions of the journey map:

```
Stage: Division of the user's journey phases
Actions: What the user does at each stage
Thoughts: What the user is thinking
Emotions: The user's emotional curve (high / flat / low)
Pain Points: Experiences that cause friction or frustration
Opportunities: Design improvements that can be made
Touchpoints: Channels through which the user interacts with the product / service
```

---

## Applicable Scenarios

✅ **Best Suited For**
- Comprehensive product experience diagnosis ("Where are users dropping off or dissatisfied?")
- Experience planning before designing new products / services
- Cross-department alignment (helping product, operations, and customer service jointly understand the full user experience)
- Discovering overlooked experience breakpoints

⚠️ **Use with Caution**
- When no user research data is available (a journey map drawn from imagination has limited value)
- When quantitative analysis is needed (complement with AARRR)

---

## Execution Steps

### Step 1: Define the Scope

- **User perspective**: Choose a specific user role (Persona)
- **Journey boundaries**: Start point (user first learns about the product) and end point (user churns or becomes a loyal user)
- **Scenario**: A specific task / goal (e.g., "complete first purchase" or "from sign-up to finishing the first project")

### Step 2: Break Down Journey Stages

Divide the journey into 4-7 stages, named from the **user's perspective** (not feature names):

Common stage patterns:
```
Consumer product: Awareness → Interest → Consideration → Purchase → Usage → Renewal / Churn
SaaS product: Discovery → Sign-up → Activation → Daily usage → Payment → Renewal / Referral
Offline service: Need emergence → Search → Arrival → Service process → Departure → Repeat purchase
```

### Step 3: Fill in Dimensions for Each Stage

For each stage, fill in one by one:

**Actions (What are they doing?)**
- The user's specific operational steps at this stage

**Thoughts (What are they thinking?)**
- The user's inner monologue, concerns, doubts
- Sources: User interview quotes, customer service records, user reviews

**Emotions (How do they feel?)**
- Emotional curve: Use a +5 to -5 scale to represent emotional highs and lows
- Emotional peaks and valleys are the most important design opportunities

**Touchpoints**
- Which channels the user uses to interact with the product / service at this stage
- E.g., App, official website, email, customer service, social media

**Pain Points**
- Specific moments that cause friction, confusion, or frustration for the user

**Opportunities**
- Based on pain points and emotional valleys, what improvement measures can be designed

### Step 4: Draw the Emotional Curve

Plot the emotional changes across the entire journey as a curve, highlighting:
- **Emotional valleys**: High-risk points for churn and dissatisfaction (primary improvement targets)
- **Emotional peaks**: "Wow Moments" that can be reinforced
- **Emotional plateaus**: Low-stimulation areas where optimization may be possible

### Step 5: Extract Opportunities and Prioritize

Extract all opportunity points from the journey map and rank them using RICE or Eisenhower matrix.

---

## Output Template (Text Version)

```
Journey subject: [User role / Persona description]
Journey scenario: [Specific goal, e.g., "New user completes first project creation"]
Journey scope: [Start point] → [End point]

---

Stage 1: [Stage name, user perspective]

  Touchpoints: [App homepage / Official website / Email invitation]
  
  Actions:
    - [User action 1]
    - [User action 2]
  
  Thoughts:
    "[User inner monologue, preferably interview quotes]"
    "[...]"
  
  Emotions: [+3 / Curious, Anticipation]
  
  Pain Points:
    - [Specific pain point description]
    - [...]
  
  Opportunities:
    - [Improvement direction 1]
    - [...]

---

Stage 2: [...] (Same format as above)

---

Emotional curve summary:
  Stages: [1]  [2]  [3]  [4]  [5]
  Emotions: [+3] [+1] [-2] [-4] [+2]
  Key: Stage 4 is the lowest emotional valley, reason: [...]

Opportunity point priorities:
  P0 (Must fix): [Stage 4 pain point, emotion -4]
  P1: [...]
  P2: [...]
```

---

## Execution Example (Excerpt)

**Scenario**: SaaS project management tool, new user first-use journey

```
Stage 3: Activation (within 24 hours after sign-up)

  Touchpoints: Web App, onboarding emails

  Actions:
    - Log in to the product
    - View Onboarding Checklist
    - Attempt to create the first project
    - Invite team members (get stuck)

  Thoughts:
    "There's so much on the interface, I don't know where to start"
    "I just want to create a project and try it — why do I have to fill in so much?"
    "Why is inviting members so complicated?"

  Emotions: +1 → -3 (Anxiety starts when creating a project)

  Pain Points:
    - Information density too high, large cognitive load
    - Invite flow requires 5 steps, user can't find the entry point
    - Cannot skip non-core configuration to directly experience core features

  Opportunities:
    - Redesign onboarding to keep only the 3 most essential steps
    - Simplify member invitation to a one-click copy link
    - Provide example project templates so users can "see a success state"
```

---

## Relationship with Other Methodologies

- **Preceded by JTBD**: JTBD defines the user's core Job; the Journey Map describes the process of completing that Job
- **Pairs with AARRR**: AARRR provides the quantitative funnel (which stage numbers drop); Journey Map provides qualitative explanation (why they drop)
- **Feeds into RICE**: Opportunity points prioritized
- **Feeds into Design Thinking**: Journey Map is a core tool of the Empathize phase; outputs are used in the Define phase
