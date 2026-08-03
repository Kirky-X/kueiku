# Code Review Checklist

## Core Concept
4-dimension checklist-driven review: Security / Architecture / Performance / Maintainability. Structured review process that catches issues systematically rather than relying on reviewer intuition.

## Applicable Scenarios
✅ **Best for**
- Pre-merge quality gate
- Refactoring impact assessment
- Team code quality standards

## Key Steps
1. **Security**: hardcoded secrets? SQL injection? XSS? Auth/authz bypass? Input validation?
2. **Architecture**: correct layer? Dependency direction? Interface contract? Error handling?
3. **Performance**: N+1 queries? Unnecessary allocations? Missing indexes? Blocking calls?
4. **Maintainability**: clear naming? Appropriate abstraction? Test coverage? Documentation?
5. Score each dimension; block merge on critical issues

## Source
Code review best practices; Google engineering practices.
