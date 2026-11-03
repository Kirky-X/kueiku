# Critical Path Method

## Core Concept
A plan's minimum duration equals its longest dependency chain, not its total work. Decompose into tasks with durations and dependencies, compute each task's float (slack), and the zero-float chain is the critical path: delay there moves the end date, delay elsewhere does not. Management effort follows the math — protect, monitor, and compress the path; flex everything else.

## Applicable Scenarios
✅ **Best for**
- Projects with a hard deadline and many dependent tasks
- Deciding which slip actually endangers the date (and which doesn't)
- Choosing where adding resources (crashing) or overlapping phases (fast-tracking) buys real time

⚠️ **When NOT to use**
- Discovery/agent work where tasks emerge step by step → Bite-Sized Plan (Engineering) — you cannot chain durations you cannot see yet
- Single-person task juggling without dependencies → Eisenhower Matrix (Decision Making)
- Portfolio-level what-to-do-first prioritization → RICE (Decision Making)
- No task-level duration estimates exist — estimate first (ranges, per Probabilistic Reasoning (Decision Making)); CPM on invented single numbers is false precision

## Key Steps
1. Work breakdown to leaf tasks small enough to estimate honestly
2. Estimate durations — ranges where uncertain (PERT: weighted optimistic/likely/pessimistic)
3. Draw the dependency graph (finish-to-start default; note overrides)
4. Forward pass → earliest start/finish; backward pass → latest start/finish
5. Float = latest − earliest start; the zero-float chain is the critical path; also record near-critical chains
6. Manage the path: daily attention on path tasks, buffers behind high-variance path segments, crash/fast-track only on the path (with cost per day saved)
7. Re-run on every duration or scope change — the path migrates

## Output Template

```
Task table: [id | duration (range) | depends on]
Dependency graph: [chain notation]
Critical path: [task chain], minimum duration [n]
Float table: [task | float | near-critical?]
Crash options: [task | cost per day saved | days purchasable]
Buffers: [where placed, size rationale]
Merge-bias note: [count of near-critical chains → aggregate delay risk]
Re-plan trigger: [any path-task slip > X]
```

## Failure Modes
- Single-number estimates: CPM's exactness launders guesswork → ranges + PERT weighting, and say the confidence
- Ignoring resource contention: classic CPM assumes infinite resources → check who actually does each path task; leveled schedules may create a second, resource-driven critical chain
- Path drift: scope or durations change but the old path is still managed → re-run the passes on every change; the path migrates silently
- Crashing off-path tasks: money spent where float absorbs it → buy days only on zero-float tasks
- Near-critical blindness: a chain one day short of critical multiplies merge risk across branches → track the top near-critical chains, not just the one path

## Evidence Strength
Strong practitioner consensus — CPM/PERT have run construction, aerospace, and software programs since 1957-58 and the network math is exact; the dominant error source is estimate quality, so output reliability tracks input discipline, not the method.

## Source
Kelley & Walker (1957, CPM, DuPont/Remington Rand); PERT, US Navy Polaris program (1958); Goldratt, *Critical Chain* (1997) for the buffer variant. Admission verdict: **Build** (v0.1.12) — execution held roadmap and requirements perspectives only; dependency-chain scheduling math was absent.
