# Database Schema Design

## Core Concept
Data modeling + index strategy + safe migration + normalization/denormalization tradeoffs. Design schemas that are correct, performant, and evolvable.

## Applicable Scenarios
✅ **Best for**
- New project data model
- Schema restructuring
- Query optimization

⚠️ **When NOT to use**
- The slowdown is in query code or application logic rather than in the schema → **Performance Optimization** (measure, locate, optimize, verify) finds the real hotspot; reshuffling tables under an unprofiled system moves the cost without removing it
- Ownership and boundaries of the data — which service owns these tables and how they stay in sync → **Microservices Patterns** (Saga, CQRS) decides that, and the schema follows the boundary
- Business entity identity and rules → **Domain-Driven Design** owns the model; an ERD drawn before the domain is settled encodes the wrong nouns and needs redoing
- Greenfield with no real query patterns yet — indexes chosen on guesses add write cost and migration time → instrument first and let **Observability** supply the actual access paths

## Key Steps
1. Identify entities and relationships (ERD)
2. Normalize to 3NF by default; denormalize only for proven performance needs
3. Design indexes based on query patterns (not in advance)
4. Plan migrations: always backward-compatible, use expand-and-contract pattern
5. Add constraints: NOT NULL, UNIQUE, FOREIGN KEY where appropriate
6. Test with realistic data volumes; optimize slow queries

## Output Template

```
Model: [domain area]   Engine: [postgres / mysql]   Volume: [rows today → 12 months]

Entities:
  [entity]  pk [id]  fields [name type null?, ...]  relations [1-N → other.entity]
  [entity]  pk [id]  fields [name type null?, ...]  relations [N-1 → other.entity]
Constraints: NOT NULL [list]   UNIQUE [list]   FK [child.parent_id → parent.id]   CHECK [rule]
Soft delete / history / tenancy: [how rows expire, which columns carry scope]

Normalization: [3NF] — deliberate exceptions: [table, reason]
Indexes (from observed query patterns only):
  [table].[col] — supports [query shape] — plan at prod volume: [index scan | seq scan]
Access paths to protect: [query → expected latency]

Migration (expand-and-contract):
  1 expand  : add [column] nullable; backfill in batches of [n]
  2 migrate : switch [reads/writes] to [new shape]; dual-write window [x days]
  3 contract: drop [old column] after [date]
Rollback per phase: [how to revert at step 1 / step 2]
```

## Failure Modes
- Normalize first and denormalize later without a measured trigger, leaving two copies of the truth → denormalize only against a measured read path, and write down how the copy stays consistent
- One blocking DDL on a large table, taking a lock or a long transaction → use expand-and-contract: add nullable, backfill in batches, switch reads, then drop the old column after a dated dual-write window
- Indexes created for queries that do not exist, costing write throughput and slowing every later migration → derive indexes from observed access paths and check the plan on production-sized data before creating them
- Foreign keys dropped for convenience and never reinstated, allowing orphaned rows nobody notices → keep the constraint; if it must go, replace it with an application check plus a periodic orphan audit
- Schema applied by hand in one environment, so production drifts from the repository → migrations live in the repo and are applied by the pipeline, with the schema version checked at deploy time

## Evidence Strength
Practitioner consensus — normalization, index selection driven by query patterns, and expand-and-contract migration are long-standing, widely taught database practice with strong operational backing; the evidence for any specific normalization target or universal indexing rule is weak and workload-dependent, and modern analytical and distributed stores deliberately violate both, so the default 3NF posture is a starting position rather than a law.

## Source
Database design best practices; Martin Fowler's evolution database patterns.
