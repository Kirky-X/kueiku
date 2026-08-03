# Database Schema Design

## Core Concept
Data modeling + index strategy + safe migration + normalization/denormalization tradeoffs. Design schemas that are correct, performant, and evolvable.

## Applicable Scenarios
✅ **Best for**
- New project data model
- Schema restructuring
- Query optimization

## Key Steps
1. Identify entities and relationships (ERD)
2. Normalize to 3NF by default; denormalize only for proven performance needs
3. Design indexes based on query patterns (not in advance)
4. Plan migrations: always backward-compatible, use expand-and-contract pattern
5. Add constraints: NOT NULL, UNIQUE, FOREIGN KEY where appropriate
6. Test with realistic data volumes; optimize slow queries

## Source
Database design best practices; Martin Fowler's evolution database patterns.
