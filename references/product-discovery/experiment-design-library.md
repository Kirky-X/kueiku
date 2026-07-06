# Experiment Design Library

## Core Idea
Turn "user validation" from a vague concept into a selectable menu — 7 standard experiment types covering different cost/fidelity combinations from hypothesis to validation. Teams can pick what they need without reinventing the wheel each time.

## Use Cases
- Teams re-discuss "which method to use" every time they validate
- Experiment cost doesn't match hypothesis risk (high-fidelity experiments testing low-risk hypotheses)
- Need standardized experiment processes for cross-comparison

## Key Steps
1. Identify the type of hypothesis to validate (desirability / usability / feasibility / viability)
2. Match experiments from the library:
   - First-click test: Tests navigation/information architecture intuition
   - Fake door test: Tests whether demand exists (tracking without code changes)
   - Wizard of Oz: Frontend real, backend manual — tests whether users are willing to use it
   - Technical spike: Tests technical feasibility
   - A/B test: Tests optimization directions for live solutions
   - Prototype: Tests interaction hypotheses (high/low fidelity optional)
   - Survey: Tests attitudes/segmentation, not behavior
3. Match by "risk × cost": Use high-fidelity experiments for high-risk hypotheses, cheap experiments for low-risk ones
4. Define success thresholds and decisions in advance (GO / Pivot / Kill)
5. Archive experiment results to the team experiment library to build learning assets

## Source
Product Compass (Experiment Design Library framework)
