# TDD: Red-Green-Refactor · Test-Driven Development

## Core Idea
Enforce "think clearly about what you want, then write code, then clean up" through a three-phase cycle — Red (write a test, it must fail) → Green (write the simplest code to make the test pass) → Refactor (clean up structure, stay green). Each step is under 5 minutes, making design intent explicit in tests.

## Use Cases
- Frequent regression bugs after code changes
- Refactoring lacks a safety net, afraid to touch code
- Requirements are vague, leading to rework from "write first, think later"

## Key Steps
1. Red: Write a test describing behavior that doesn't exist yet; run it, confirm it fails (and fails for the right reason — assertion failure, not compilation failure)
2. Green: Write the **simplest** implementation to make the test pass (ugly is okay, hardcoding is okay); don't write code not covered by tests
3. Refactor: Clean up code structure (naming/extract functions/eliminate duplication); after each small change, immediately re-run tests, stay green
4. Cycle: One Red-Green-Refactor cycle every 2–5 minutes
5. Never skip Red: Writing implementation first and adding tests later is not TDD
6. Test quality check: Can you make the test fail by deleting production code? If not, the test is ineffective

## Source
Kent Beck, *Test-Driven Development: By Example* (2002); TDD concept traceable to Kent Beck's 1990s Smalltalk practice
