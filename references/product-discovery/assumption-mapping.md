# Assumption Mapping

## Core Idea
Make implicit assumptions behind a product/project explicit, rank them by "impact × risk," and prioritize validating high-impact + high-risk assumptions first. The basic version uses 4 risk categories: Desirability (do users want it) / Viability (is it commercially viable) / Feasibility (can it be built) / Usability (can it be used effectively); the extended version adds 8 categories including Ethics, Legal, Brand, Strategic Fit, etc.

## Use Cases
- Before launching a new feature/product, identify "what are we actually betting on"
- When multiple assumptions coexist, decide which to validate first
- Cross-team alignment on "what must be true for this to work"

## Key Steps
1. List all assumptions the solution depends on, categorized by 4 (or 8) risk types
2. Assess each assumption: Impact on business if false (high/medium/low) + Current risk level (high/medium/low)
3. Plot on an Impact × Risk matrix, prioritize the "high impact + high risk" quadrant
4. Design minimal experiments for each prioritized assumption (refer to experiment-design-library.md)
5. After experiments, return to the matrix, update risk scores and decide GO / Pivot / Kill

## Source
Promoted by Teresa Torres in *Continuous Discovery Habits*; the 4-risk model originated from IDEO, 8-risk extension see Product Compass.
