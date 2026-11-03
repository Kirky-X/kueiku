# CI/CD Pipeline Design

## Core Concept
7-stage pipeline: Trigger → Build → Test → Security → Quality → Deploy → Post-Deploy. Each stage has gates that must pass before proceeding. Includes rollback strategies.

## Applicable Scenarios
✅ **Best for**
- Pipeline setup
- Release strategy design
- Quality gates

⚠️ **When NOT to use**
- The pipeline exists but the real constraint is one slow or flaky stage — adding stages to a flow that already queues adds wait time without raising throughput → **Theory of Constraints** locates the binding stage first
- A project that ships a handful of times a year with a small team — a seven-stage gated pipeline costs more waiting than it saves; a release checklist with one smoke test is the honest shape
- Choosing the branch and release model that the pipeline will promote through → **Git Workflow Strategies** owns branching; this entry owns what runs and what gates it
- Defining which security checks to run and what threat they cover → **Security by Design** owns threat modeling; this entry only decides where the gate sits and what blocks the merge

## Key Steps
1. **Trigger**: define what starts the pipeline (push, PR, schedule)
2. **Build**: compile, package, containerize
3. **Test**: unit → integration → e2e (fast to slow)
4. **Security**: SAST, dependency scanning, secret detection
5. **Quality**: coverage gates, lint, static analysis
6. **Deploy**: blue-green / canary / rolling; environment promotion
7. **Post-Deploy**: smoke tests, monitoring, rollback triggers

## Output Template

```
Pipeline: [service]   Trigger: [push | PR | schedule]   Cadence: [per commit | nightly]
Target: [deploy to prod]   Promotion path: [dev → staging → prod]

Stages (run in parallel where independent):
  Build    : [command], cache key [x], artifact [type/id]        gate: [exit 0]
  Test     : unit [x s] → integration [x s] → e2e [x s]          gate: [all green]
  Security : SAST [tool], deps [tool], secrets [tool]            gate: [0 critical]
  Quality  : coverage [x%] (ratchet from [baseline]), lint [ruleset]   gate: [threshold]
  Deploy   : [blue-green | canary | rolling], canary traffic [x%] for [x min]
  Post     : smoke [check], soak [x min], auto-rollback trigger [metric > threshold]

Rollback: artifact [id] → [previous id]; RTO [x min]; decision owner [role]; drill date [date]
Budget: pipeline p50 [x min], slowest stage [x s] — required checks must finish under [n] min
```

## Failure Modes
- Gates so slow that people route around them, pushing straight to production → keep the blocking path fast enough to wait for, move slow checks to a nightly job, and treat required-check duration as a metric you own
- The seven stages treated as a fixed serial chain → Security and Quality do not depend on each other, so running them in sequence adds pure wait → draw the actual dependency graph and parallelize independent stages
- Thresholds copied from a baseline instead of an intent, so a 20% coverage gate protects nothing → set the gate at a level the team can defend, then ratchet it; a gate nobody believes in is a speed bump, not a safety net
- Rollback written down but never exercised, so the first real rollback is the first execution → run a rollback drill on a schedule against a real artifact, not a doc
- The pipeline is green while the deploy is wrong, because nothing verifies production behavior → define the smoke check and the automated rollback trigger before the first release and wire both to **Observability** metrics

## Evidence Strength
Practitioner consensus — staged pipelines, gated promotion, blue-green and canary deployment, and rehearsed rollback are long-established industrial practice with broad adoption; evidence that any particular pipeline shape or gate count outperforms another is thin, and pipeline effectiveness is dominated by test-suite speed and team discipline rather than by the stage topology this entry prescribes.

## Source
Jez Humble & David Farley, *Continuous Delivery* (2010); modern CI/CD practices.
