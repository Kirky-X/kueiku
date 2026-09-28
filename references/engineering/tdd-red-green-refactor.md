# TDD Red-Green-Refactor

## Core Concept
Test-Driven Development cycle: Red (write a failing test) → Green (write minimal code to pass) → Refactor (clean up while keeping tests green). Ensures every line of code has a test and the codebase stays clean.

## Applicable Scenarios
✅ **Best for**
- Frequent regression bugs
- Refactoring without safety nets
- Building confidence in code changes

⚠️ **When NOT to use**
- Exploratory spikes and throwaway prototypes — the tests would fossilize code you intend to rewrite; write tests when the spike graduates
- UI layout and visual work — pixel-level assertions are brittle; use visual regression or human review instead
- Legacy code with no test infrastructure — build the smallest testing seam first; strict TDD from an untestable start fails on contact

## Key Steps
1. **Red**: Write a test that describes the next behavior you want. Run it — it should fail.
2. **Green**: Write the minimum code to make the test pass. No more.
3. **Refactor**: Clean up the code. Remove duplication. Improve naming. All while keeping tests green.
4. Repeat the cycle for the next behavior.
5. Run the full test suite after each cycle to catch regressions.

## Output Template

```
Behavior: [calc_discount applies 5% over 50 items]

RED  — test_order.py::test_discount_over_fifty   → FAILED (no discount logic) ✓ expected failure
GREEN — Order.calc_discount: minimum implementation → test PASSES (1/1)
REFactor — extract DISCOUNT_THRESHOLD constant, drop duplication → all tests still green

Cycle log: [n cycles this session, each red→green verified — never green-first]
Suite: full run after cycle [n] — 42 passed
Deferred behaviors: [list, each will get its own red test]
```

## Failure Modes
- Green-first: writing the implementation then a test that passes immediately — the test never proved it can fail → assert the red step every cycle; a test that never failed proves nothing
- Test-after drift: "tests coming later" — later never comes under deadline → the cycle log makes skipped reds visible; count them honestly
- Mocking the subject: over-mocked tests that verify the mock, not behavior → test observable outputs of real units; if everything must be mocked to test one thing, the design is the smell

## Evidence Strength
Mixed — controlled and quasi-experiments on TDD show consistently higher test coverage and often better external quality, with mixed or neutral results on development speed (and noticeable setup cost for teams new to it); the discipline's clearest support is for regression safety during refactoring, its stated strength here.

## Source
Kent Beck, *Test-Driven Development: By Example* (2002).
