# User Segmentation

## Core Concept
Cluster existing users by behavior/JTBD/needs from feedback data. Unlike market segmentation (which targets potential customers), user segmentation analyzes current users to find usage pattern differences within the same customer base.

## Applicable Scenarios
✅ **Best for**
- Analyzing usage pattern differences within existing users
- Personalization strategies
- Feature prioritization per user group

⚠️ **When NOT to use**
- Targeting prospects who aren't users yet — there is no behavior to cluster; that's **Market Segmentation** territory
- A revenue-only cut — revenue bands are **RFM Model** / **Cohort Analysis** work; behavioral clusters answer "why", RFM answers "how much"
- Data-poor bases — clustering on sparse logs produces fiction; require enough behavior per user to be meaningful
- One-time analysis presented as segments — the base churns and migrates; without a refresh loop it's a snapshot

## Key Steps
1. Collect user data: behavior logs, survey responses, support tickets
2. Identify clustering variables (usage frequency, feature adoption, JTBD)
3. Cluster users into 3-5 groups
4. For each group, profile: behavior patterns, needs, satisfaction levels
5. Design targeted strategies per segment
6. Monitor segment migration over time

## Output Template

```
Segment: [name]
  Size: [# users, % of base]
  Defining behavior: [usage pattern, feature-adoption signature]
  Dominant job: [what they hire the product for]
  Health: [satisfaction score, churn risk]
  Strategy: [targeted action]
  Success metric: [how you'll know it worked]
Migration watch: [which segments flow in/out]
```

## Failure Modes
- Demographic labels on behavioral clusters: "power users are 25-34" explains nothing → cluster on behavior and **JTBD**; demographics only where they demonstrably track usage
- Statistical clusters without faces: an n=3 grouping nobody can act on → every cluster needs a human-readable profile and a testable strategy before it counts
- Static snapshots: segments defined at launch never revisited while the base migrates → re-run on a cadence and track migration, not just membership
- Single-source clustering: log-only clusters miss motivation; survey-only clusters miss behavior → triangulate behavioral data with interview evidence per segment

## Evidence Strength
Practitioner consensus — behavioral segmentation of an installed base is standard product analytics practice and measurably improves targeting and retention work; the caveats are that cluster stability depends on data volume and periodic re-runs, and formal cluster-validity checks are frequently skipped in practice, so treat segment boundaries as provisional.

## Source
Product analytics methodology; behavioral segmentation frameworks.
