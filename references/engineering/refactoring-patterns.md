# Refactoring Patterns

## Core Concept
Code smells → refactoring techniques mapping + small-step improvement under test protection. Systematic approach to improving code quality without breaking functionality.

## Applicable Scenarios
✅ **Best for**
- Legacy code improvement
- Large function/class decomposition
- Code quality maintenance

## Key Steps
1. Identify code smells (long method, god class, feature envy, data clumps, etc.)
2. Map each smell to the appropriate refactoring technique
3. Ensure test coverage exists before refactoring
4. Apply refactoring in small steps; run tests after each step
5. Verify: behavior unchanged? Complexity reduced? Readability improved?

## Source
Martin Fowler, *Refactoring* (1999, 2nd ed. 2018).
