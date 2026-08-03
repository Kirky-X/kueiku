# Assumption Mapping

## Core Concept
Make implicit assumptions behind a product/project explicit, ranked on an Impact × Risk 2D matrix, prioritizing validation of high-impact + high-risk assumptions. The basic version uses 4 risk categories: Desirability (do users want it) / Viability (does the business work) / Feasibility (can we build it) / Usability (can users use it); the extended version adds 8 categories, supplementing with Ethics, Legal, Brand, Strategic Fit, etc.

## Applicable Scenarios
- Before launching a new feature/product, identify "what are we actually betting on"
- When multiple assumptions coexist, decide which to validate first
- Cross-team alignment on "what must be true for this to work"

## Key Steps
1. List all assumptions the proposal depends on, categorize by 4 (or 8) risk types
2. For each assumption assess: if false, impact on business (High/Medium/Low) + current risk (High/Medium/Low)
3. Plot on Impact × Risk matrix, prioritize the "high impact + high risk" quadrant
4. Design minimum experiments for each priority assumption (see experiment-design-library.md)
5. After experiments, return to matrix, update risk scores, and decide GO / Pivot / Kill

## Source
Popularized by Teresa Torres in *Continuous Discovery Habits*; 4-risk model originates from IDEO; 8-risk extension from Product Compass.
