# Shipping Artifacts

## Core Concept
Core 5 + Conditional 4 document standards for AI project delivery. Defines the anti-PRD rule: traditional PRDs are insufficient; AI projects need living documents that evolve with the product.

## Applicable Scenarios
- AI project delivery standards
- Defining documentation requirements for AI products
- Ensuring deliverable quality

⚠️ **When NOT to use**
- Internal experiments and prototypes that will never face users — the artifact gate would outlive the project
- Non-AI deliveries — "model card" and "data specification" assume model behavior; classic delivery needs other standards
- As a paperwork gate bolted on after the build — documents written to pass a checklist at ship time are theater, the exact failure the anti-PRD rule exists to prevent

## Key Steps
1. Identify the Core 5 documents required for every project (problem statement, architecture decision records, data specification, model card, deployment guide)
2. Identify Conditional 4 documents based on project type (ethics review, bias audit, user privacy impact, rollback plan)
3. Apply the Anti-PRD rule: replace static PRDs with living documents that update with each iteration
4. Validate all required documents exist and are current before shipping
5. Archive shipping artifacts as reference for future projects

## Output Template

```
Project: [name] — ship target: [date]

Core 5 (required, with currency date):
  Problem statement        [exists: y/n, updated: date]
  Architecture decisions   [ADRs: list, last: date]
  Data specification       [exists, updated: date]
  Model card               [exists, updated: date]
  Deployment guide         [exists, updated: date]

Conditional 4 (required for this project type):
  Ethics review [y/n/why not]  Bias audit [y/n]  Privacy impact [y/n]  Rollback plan [y/n]

Currency check: any document older than the last model/prompt change → [block ship / justify exception]
Living-document cadence: which doc updates on each iteration: [answer]
Archive: [location] — owner: [x]
```

## Failure Modes
- Checklist compliance without currency: all five docs "exist", none updated since three model changes ago → the currency check outranks the existence check
- Conditional 4 skipped silently: "not applicable" with no reason → every skipped conditional needs a one-line justification on the record
- Anti-PRD misread as anti-documentation: dropping the PRD without adopting living replacements leaves a vacuum → name which artifact now carries each former PRD responsibility

## Evidence Strength
Practitioner consensus — a process standard encoding widely shared AI-delivery lessons (model behavior shifts make static specs stale); effectiveness depends on enforcement cadence and tooling, and there is no comparative evidence that Core 5 specifically beats other minimal sets.

## Source
AI delivery standards; shipping quality frameworks.
