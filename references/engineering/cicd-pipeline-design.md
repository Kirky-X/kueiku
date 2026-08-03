# CI/CD Pipeline Design

## Core Concept
7-stage pipeline: Trigger → Build → Test → Security → Quality → Deploy → Post-Deploy. Each stage has gates that must pass before proceeding. Includes rollback strategies.

## Applicable Scenarios
✅ **Best for**
- Pipeline setup
- Release strategy design
- Quality gates

## Key Steps
1. **Trigger**: define what starts the pipeline (push, PR, schedule)
2. **Build**: compile, package, containerize
3. **Test**: unit → integration → e2e (fast to slow)
4. **Security**: SAST, dependency scanning, secret detection
5. **Quality**: coverage gates, lint, static analysis
6. **Deploy**: blue-green / canary / rolling; environment promotion
7. **Post-Deploy**: smoke tests, monitoring, rollback triggers

## Source
Jez Humble & David Farley, *Continuous Delivery* (2010); modern CI/CD practices.
