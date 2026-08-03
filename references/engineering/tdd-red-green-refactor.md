# TDD Red-Green-Refactor

## Core Concept
Test-Driven Development cycle: Red (write a failing test) → Green (write minimal code to pass) → Refactor (clean up while keeping tests green). Ensures every line of code has a test and the codebase stays clean.

## Applicable Scenarios
✅ **Best for**
- Frequent regression bugs
- Refactoring without safety nets
- Building confidence in code changes

## Key Steps
1. **Red**: Write a test that describes the next behavior you want. Run it — it should fail.
2. **Green**: Write the minimum code to make the test pass. No more.
3. **Refactor**: Clean up the code. Remove duplication. Improve naming. All while keeping tests green.
4. Repeat the cycle for the next behavior.
5. Run the full test suite after each cycle to catch regressions.

## Source
Kent Beck, *Test-Driven Development: By Example* (2002).
