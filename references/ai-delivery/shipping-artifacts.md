# Shipping Artifacts

## Core idea
Delivery in the AI era is not just writing a thick PRD—deliverables should be split into Core 5 (mandatory) + Conditional 4 (scenario-based), with an explicit "Anti-PRD rule": don't write a traditional 50-page PRD; write minimal executable documents that both agents and humans can act on.

## Use cases
- AI project deliverable standards are inconsistent; agents and human engineers can't hand off smoothly
- PRDs keep growing longer but execution efficiency keeps declining
- Different roles repeatedly ask "which document should I look at?"

## Key steps
1. Core 5 (mandatory for every project):
   - Problem Statement (what problem to solve, no solutions)
   - Spec (interface/contract definition, directly consumable by agents)
   - Tasks (decomposed into independently executable task list, each with acceptance criteria)
   - Design Doc (key design decisions and tradeoffs, max 1 page)
   - README (how to run/test, minimal executable entry point)
2. Conditional 4 (scenario-based):
   - ADR (architecture decision records, for complex decisions)
   - Runbook (post-launch ops procedures, for production systems)
   - Migration Plan (when data migration is involved)
   - Postmortem (after incidents)
3. Anti-PRD rule: no "product requirements document" may exceed 2 pages—overflow must be split into Spec + Tasks + Design Doc
4. All documents carry explicit version and status (Draft/Review/Approved/Deprecated)
5. Documents cross-reference each other with explicit links to avoid information silos

## Source
Product Compass (Shipping Artifacts framework); Anti-PRD concept from Shape Up methodology
