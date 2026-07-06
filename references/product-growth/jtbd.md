# JTBD · Jobs to Be Done（用户任务框架）

## Core Concept

Users buy/use products to **complete a specific Job**, not because they like the product itself. Competitors are not just similar products, but any solution that can complete the same Job.

> Classic example: People don't buy a 1/4-inch drill bit — they buy a 1/4-inch hole. The deeper Job is: hanging a picture on the wall to make the home more beautiful.

**Three Dimensions of a Job:**
- **Functional**: The goal the task itself aims to achieve
- **Emotional**: How the user wants to feel when completing the task
- **Social**: How the user wants to be perceived by others

---

## Applicable Scenarios

✅ **Best For**
- Understanding users' **real needs** vs surface needs
- Discovering competitive replacement opportunities (what old solution did users "hire" us from?)
- Product positioning and value proposition design
- Exploring new feature directions (unmet Jobs)
- Competitive analysis (who are the real competitors?)

⚠️ **Use with Caution**
- Scenarios requiring large-scale quantitative data (JTBD is a qualitative framework)
- When sufficient user research data already exists and only execution is needed

---

## Core Concepts

### Job Statement Format

```
When [situation/context],
I want to [motivation/goal],
So that [expected outcome/deeper need].
```

Example:
```
When I get home late from work (situation),
I want to quickly prepare a decent dinner (motivation),
So that I take care of myself without feeling guilty (deeper need).
```

### Hiring and Firing

- **Hire**: User chooses a product/solution to complete a Job
- **Fire**: User abandons one solution in favor of another
- Studying "why users fire the old solution" is often more insightful than "why they chose us"

### Redefining Competitors

From a Job perspective, competitors ≠ feature-similar products.

Example: The milkshake case (Clayton Christensen)
- Surface competitors: cola, juice, water
- Real Job: keep hands busy and pass time during morning commute without getting hungry too quickly
- Real competitors: bananas, cereal bars, coffee

---

## Execution Steps

### Step 1: Contextual Interviews

Conduct deep interviews with real users, focusing on:
1. **Purchase/selection context**: "What situation led you to start looking for this type of product/solution?"
2. **Previous solution**: "Before us, what method did you use to accomplish this?"
3. **Firing trigger**: "What made you decide to switch from the previous solution?"
4. **Progress friction**: "What felt frustrating or cumbersome during the process?"
5. **Success criteria**: "What outcome would make you feel this Job is 'done'?"

Key interview principles:
- Ask about **specific behaviors**, not abstract preferences ("What did you do last time?" not "What do you like?")
- Focus on the **timeline** (trigger → search → evaluate → choose → use → outcome)
- Explore **emotional and social dimensions**, not just functional

### Step 2: Write Job Statements

Synthesize interview insights and write core Job Statements in standard format. A product typically corresponds to 2-5 different Jobs.

### Step 3: Quantify Job Importance vs Satisfaction

Through survey (ODI method, Outcome-Driven Innovation):
- For each Job, users rate: **Importance (1-10)** and **Current Satisfaction (1-10)**
- Opportunity score = Importance + Max(Importance - Satisfaction, 0)
- Opportunity score > 10 indicates a **high-value unmet Job**

### Step 4: Competitive Mapping

For each high-value Job, identify:
- What solution are users currently using to complete this Job?
- What are the satisfaction weaknesses of those solutions?
- Where can our solution do better?

### Step 5: Translate to Product Decisions

Convert high-opportunity + low-satisfaction Jobs into:
- Core feature direction
- Value proposition wording
- Marketing/positioning strategy

---

## Output Template

```
Research context: [Product/feature, research method, sample size]

Core Job Statements:

Job 1:
  Context: [...]
  Motivation: [...]
  Deeper need: [...]
  Functional dimension: [...]
  Emotional dimension: [...]
  Social dimension: [...]

Job 2: [...]

Job Importance vs Satisfaction Matrix:
  Job        | Importance | Satisfaction | Opportunity Score | Priority
  -----------|------------|--------------|-------------------|---------
  Job 1      |    [N]     |     [N]      |       [N]         |  High
  Job 2      |    [N]     |     [N]      |       [N]         |  Medium

Competitive Analysis (Job perspective):
  Job 1 current primary solution: [...] Weakness: [...]
  Job 2 current primary solution: [...] Weakness: [...]

Product Insights:
  Highest opportunity Job: [...]
  Recommended product direction: [...]
  Value proposition recommendation: [...]
```

---

## Common Pitfalls

| Pitfall | Description |
|------|------|
| Writing Jobs as feature descriptions | "I want a search function" ≠ Job; keep asking "To do what?" |
| Ignoring emotional/social dimensions | Purely functional Jobs are rarely the real purchase driver |
| Only looking at current users | Research "non-customers" and "churned customers" for deeper insights |
| Inconsistent Job granularity | "I want to live better" is too macro; "I want to bold text in Word" is too micro |

---

## Relationships with Other Methodologies

- **Preceded by Design Thinking**: JTBD defines the real user Job; Design Thinking designs the solution
- **Input to AARRR**: Use JTBD to explain drop-off reasons at each funnel layer
- **Combined with Customer Journey Map**: JTBD is the "why"; the journey map is the "how the Job gets done"
- **Combined with RICE**: High-opportunity Jobs become features, prioritized via RICE
