# Refactoring Patterns

## Core Concept
Code smells → refactoring techniques mapping + small-step improvement under test protection. Systematic approach to improving code quality without breaking functionality.

## Applicable Scenarios
✅ **Best for**
- Legacy code improvement
- Large function/class decomposition
- Code quality maintenance

⚠️ **When NOT to use**
- Code with no tests and no seams — writing characterization tests is step zero; refactoring without them is gambling with production
- The module is scheduled for deletion or rewrite — polish invested in dead code is waste
- Rewrites disguised as refactoring: if behavior is changing, that's redesign — scope and review it differently

## Key Steps
1. Identify code smells (long method, god class, feature envy, data clumps, etc.)
2. Map each smell to the appropriate refactoring technique
3. Ensure test coverage exists before refactoring
4. Apply refactoring in small steps; run tests after each step
5. Verify: behavior unchanged? Complexity reduced? Readability improved?

## Output Template

```
Target: [module/function] — smell inventory:
  | Smell                | Where            | Technique                 |
  | Long method          | process() L40-220| Extract Function          |
  | Data clumps          | (user, email, …) | Introduce Parameter Object|
  | Duplicated condition | 4 sites          | Extract + polymorphism    |

Safety: tests present [y — n cases, incl. characterization tests for untested paths]
Step plan: extract helper (tests green) → move query logic (green) → rename (green) — commit per green step
Done check: behavior identical (tests untouched and passing) / complexity [metric: length, nesting depth, coupling] down / reviewable in [n] small commits
Explicitly deferred: [smells needing design decisions — not smuggled into this pass]
```

## Failure Modes
- Refactoring without a behavior net: "tests after" — every intermediate step is unverifiable → characterization tests first; if the code is untestable, start there
- Smell-hunting as aesthetics: renaming and reshaping by personal taste, calling it cleanup → every refactor must name the smell and the measurable outcome; taste-only changes stay out
- Big-bang "refactor" branches: weeks long, merge conflicts, behavior drift → small steps, each green, each committed; a refactor branch older than days is a rewrite in disguise

## Evidence Strength
Practitioner consensus — the smell/technique catalog is the standard reference in the field, and small-steps-under-tests is core discipline across method schools; empirical claims that refactoring improves maintainability are supported in studies but modest, and the catalog itself is descriptive craft knowledge, not a validated taxonomy.

## Source
Martin Fowler, *Refactoring* (1999, 2nd ed. 2018).
