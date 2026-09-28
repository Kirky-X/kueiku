# Code Review Checklist

## Core Concept
4-dimension checklist-driven review: Security / Architecture / Performance / Maintainability. Structured review process that catches issues systematically rather than relying on reviewer intuition.

## Applicable Scenarios
✅ **Best for**
- Pre-merge quality gate
- Refactoring impact assessment
- Team code quality standards

⚠️ **When NOT to use**
- Automated checks already cover an item (linters, SAST) — the checklist re-runs what the pipeline proves; reserve human attention for what tools can't see
- Trivial PRs (docs, comment fixes) — full 4-dimension review on a typo PR trains reviewers to skim
- As a substitute for design review — a checklist reads diffs; it cannot judge whether the design should exist

## Key Steps
1. **Security**: hardcoded secrets? SQL injection? XSS? Auth/authz bypass? Input validation?
2. **Architecture**: correct layer? Dependency direction? Interface contract? Error handling?
3. **Performance**: N+1 queries? Unnecessary allocations? Missing indexes? Blocking calls?
4. **Maintainability**: clear naming? Appropriate abstraction? Test coverage? Documentation?
5. Score each dimension; block merge on critical issues

## Output Template

```
PR: [title] — size [n LOC] — risk [low/med/high]

| Dimension      | Findings                                    | Severity    |
| -------------- | ------------------------------------------- | ----------- |
| Security       | [new endpoint missing authz check L88]      | blocking    |
| Architecture   | [helper placed in wrong layer]              | fix now     |
| Performance    | [N+1 in list endpoint — pre-existing]       | note        |
| Maintainability| [test covers happy path only]               | fix now     |

Verdict: [block / approve-with-nits / approve]
Scope check: did the review cover what tools can't (intent, boundary cases, contract drift)? [answer]
```

## Failure Modes
- Checklist fatigue: 30 items ticked "ok" in 90 seconds — box-ticking reads nothing → for large PRs, assign dimensions across reviewers; for small PRs, only the touched dimensions
- Nit avalanche: style comments bury the one blocking finding → findings must carry severity; blocking findings lead the review, style goes to automation
- Review as gatekeeper vs teacher: everything returned as "wrong" → classify findings: must-fix vs should-fix vs taste; taste items default to the author

## Evidence Strength
Practitioner consensus — code review itself has decent practitioner evidence for defect detection (and for knowledge transfer), while checklists demonstrably help reviewers cover systematically (aviation-derived principle); but over-long checklists degrade attention, and no specific 4-dimension weighting is validated — keep the list short and let machines carry what they can.

## Source
Code review best practices; Google engineering practices.
