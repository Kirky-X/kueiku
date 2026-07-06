# GE-McKinsey Matrix

## Core Concept

Uses **Industry Attractiveness** (High/Medium/Low) × **Business Strength** (Strong/Medium/Weak) to form a 3×3 nine-cell matrix for evaluating diversified business portfolios and allocating resources. It's an upgraded version of the BCG Matrix: BCG uses only two dimensions (growth rate/share), while GE allows each dimension to be derived from multiple weighted factors for finer granularity.

> The nine cells are divided into three zones: **Invest/Grow** (upper-left three cells), **Selectivity** (diagonal three cells), and **Harvest/Divest** (lower-right three cells).

```
              Business Strength
         Strong   Medium   Weak
Industry Attractiveness High [Invest] [Invest] [Select]
                      Medium [Invest] [Select] [Harvest]
                      Low [Select] [Harvest] [Divest]
```

---

## Use Cases

✅ **Best for**
- Diversified enterprise business portfolio management
- Strategic Business Unit (SBU) resource allocation
- Investment priority ranking and exit decisions
- Cross-business-line budget allocation

⚠️ **Use with caution**
- Single-business companies (no portfolio to speak of)
- Severely missing evaluation dimension data (weighted scoring will be distorted)
- Highly coupled businesses (independent evaluation ignores synergies)

---

## Execution Steps

### Step 1: Evaluate Industry Attractiveness

Select factors influencing industry attractiveness and weight them (typically 5-7 factors):

```
Industry Attractiveness Factors (examples, adjust per project):
  - Market size             Weight [0.20]  Score [1-5]
  - Market growth rate      Weight [0.25]  Score [1-5]
  - Industry profit margin  Weight [0.20]  Score [1-5]
  - Competitive intensity   Weight [0.15]  Score [1-5] (inverse)
  - Technology stability    Weight [0.10]  Score [1-5]
  - Regulatory/Policy environment Weight [0.10] Score [1-5]
  ----------------------------------------
  Weighted total = Σ(Weight × Score) → Map to High/Medium/Low
```

### Step 2: Evaluate Business Strength

Similarly use weighted factors to evaluate each SBU's relative strength in the industry:

```
Business Strength Factors (examples):
  - Relative market share     Weight [0.25]  Score [1-5]
  - Brand strength            Weight [0.15]  Score [1-5]
  - Technology/Product capability Weight [0.20] Score [1-5]
  - Cost competitiveness      Weight [0.15]  Score [1-5]
  - Channel/Customer relationships Weight [0.15] Score [1-5]
  - Management team           Weight [0.10]  Score [1-5]
  ----------------------------------------
  Weighted total → Map to Strong/Medium/Weak
```

### Step 3: Position Each Business in the Nine Cells

```
GE Matrix Positioning:
              Business Strength
         Strong      Medium      Weak
Industry Attractiveness High [SBU-A] [SBU-B] [SBU-C]
                      Medium [SBU-D] [SBU-E] [SBU-F]
                      Low [SBU-G] [SBU-H] [SBU-I]
```

Circle size is proportional to business revenue/profit; arrows indicate expected attractiveness/strength change direction.

### Step 4: Formulate Investment Strategy

Provide strategy direction based on the zone:

| Zone | Strategy | Resource Action |
|------|------|---------|
| Invest/Grow (upper-left three cells) | Build and grow | Prioritize investment, expand share |
| Selectivity (diagonal three cells) | Selective investment | Focus on niche advantages, invest cautiously |
| Harvest/Divest (lower-right three cells) | Harvest or divest | Reduce investment, recoup cash or exit |

> Businesses near the diagonal need individual assessment: upward potential → invest; downward trend → harvest.

---

## Output Template

```
GE-McKinsey Matrix Analysis

I. Industry Attractiveness Scoring
  [List factors/weights/scores] → Total [X] → [High/Medium/Low]

II. SBU Business Strength Scoring
  SBU-A: [Factor scores] → Total [X] → [Strong/Medium/Weak]
  SBU-B: ...

III. Nine-Cell Positioning
  [Matrix chart, marking each SBU's position and circle size]

IV. Investment Strategy
  SBU-A (Invest zone): Build — [Specific actions]
  SBU-B (Selectivity zone): Focus — [Judgment basis]
  SBU-C (Harvest zone): Harvest/Exit — [Timeline]

V. Resource Reallocation
  Release [X] resources from [Harvest zone businesses] → Invest in [Invest zone businesses]
```

---

## Common Pitfalls

| Pitfall | How to Avoid |
|------|---------|
| Weighting factors by gut feel | Use team alignment + historical data to calibrate weights, document weighting rationale |
| Scores clustered in the middle (all 3s) | Force distribution or require specific evidence for each score |
| Ignoring trends, only looking at current state | Add a "3-year expected direction" column, mark with arrows |
| Not considering inter-business synergies | Separately note synergy value, avoid exit decisions for coupled businesses |
| Conflicting conclusions from mixing with BCG | Choose one as the primary framework, use the other for cross-validation |

---

## Relationship with Other Methodologies

- **Upgraded version of BCG Matrix**: BCG is a simplified GE matrix (two dimensions vs multi-factor weighted); use GE for complex portfolios
- **Combined with Ansoff Matrix**: GE evaluates existing portfolio; Ansoff determines new growth directions
- **Combined with Value Chain Analysis**: GE positions business strength sources; value chain deeply analyzes advantageous links
- **Followed by OKR/RICE**: Investment zone business targets convert to OKRs; execution tasks use RICE for prioritization
