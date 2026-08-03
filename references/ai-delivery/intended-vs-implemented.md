# Intended vs Implemented

## Core Concept
A framework for detecting drift between documented intent and cited code implementation. Tracks bidirectional references: does the design doc reference the right code? Does the code cite the right design doc? Identifies boundary mismatches where scope has shifted.

## Applicable Scenarios
- Detecting doc-code drift in AI-era projects
- Ensuring design documents stay aligned with implementation
- Auditing specification coverage

## Key Steps
1. Extract documented intents from design docs (features, behaviors, constraints)
2. Map each intent to its corresponding code implementation (cited code)
3. Check bidirectional references: does code reference back to the intent?
4. Identify boundary mismatches: scope changes, missing implementations, orphaned docs
5. Create a drift report with severity and recommended actions

## Source
AI delivery best practices; doc-code alignment frameworks.
