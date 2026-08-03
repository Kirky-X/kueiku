# Market Research

**When to use**: Market sizing, segmentation, user groups, personas

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **Market Sizing** | TAM/SAM/SOM + top-down and bottom-up triangulation | Funding decks, new market assessment | `market-sizing.md` |
| **Market Segmentation** | 3-5 non-overlapping segments, behavior+JTBD+needs | Early strategy definition of who to serve | `market-segmentation.md` |
| **User Segmentation** | Cluster by behavior/JTBD/needs from feedback data | Analyzing usage pattern differences within the same customer base | `user-segmentation.md` |
| **User Personas** | 3 personas with JTBD + Top 3 Pains/Gains + Unexpected Insight | Aligning team understanding of target users | `user-personas.md` |
| **STP Analysis** | Segmentation-Targeting-Positioning 3-step method | Market entry, product positioning, marketing strategy | `stp-analysis.md` |
| **Perceptual Mapping** | 2D coordinate chart showing consumer brand perception positioning | Brand positioning, competitive perception comparison, positioning adjustment | `perceptual-mapping.md` |
| **Technology Adoption Lifecycle** | Innovators→Early Adopters→Majority→Laggards 5 stages + the chasm | Technology product marketing, crossing the chasm strategy, target customer segment selection | `technology-adoption-lifecycle.md` |

## Minimum Information Requirements per Methodology

- **Market Sizing**: Requires industry volume data + per-customer ARPU data
- **Market Segmentation**: Requires customer behavior/JTBD/needs data
- **User Segmentation**: Requires product analysis + surveys + ticket data
- **User Personas**: Requires interview/survey data clustering
- **STP Analysis**: Requires segmentation dimension data + per-segment scale/competition/fit assessment
- **Perceptual Mapping**: Requires 50+ target segment users' perception ratings for multiple brands
- **Technology Adoption Lifecycle**: Requires customer composition + acquisition channel + deal cycle data

## Routing Trigger Signals

- "Market sizing" → Market Sizing (primary)
- "Market segmentation / 3-5 non-overlapping" → Market Segmentation (primary)
- "User segmentation / usage behavior clustering" → User Segmentation (primary)
- "User personas / 3 personas / team user awareness alignment" → User Personas (primary) ⚡ If need to uncover users' "jobs" → use JTBD (Product & Growth); if need empathetic understanding of user feelings → use Empathy Map (User Research)
- "Market entry / product positioning / marketing strategy" → STP Analysis (primary)
- "Brand positioning / competitive perception comparison / positioning adjustment" → Perceptual Mapping (primary)
- "Technology product marketing / crossing the chasm / target customer segment selection" → Technology Adoption Lifecycle (primary)

## Common Combinations

- **Market entry strategy**: Market Sizing → Market Segmentation → STP Analysis → Perceptual Mapping
- **New product launch**: STP Analysis → Technology Adoption Lifecycle → Pricing Strategy
- **Brand positioning optimization**: Perceptual Mapping → STP Analysis (repositioning)

## Methodology Mutual Exclusion and Ordering Constraints

| Constraint pair | Rule | Reason |
| --- | --- | --- |
| Market Segmentation → User Personas | **Segmentation first, then Personas** | Define market segments first, then build personas per target segment; avoids personas without segmentation basis |
| User Personas vs JTBD | **Choose by goal**: describe typical user's complete profile→Personas; uncover users' "jobs"→JTBD | Input data may overlap but output purposes differ |
| User Segmentation vs RFM Model | **Choose by data foundation**: need behavior/JTBD/needs clustering→User Segmentation; need 3-dimension transaction data tiering→RFM Model | User Segmentation is broader; RFM focuses on transaction data |
