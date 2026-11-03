# Git Workflow Strategies

## Core Concept
Strategy selection matrix: Trunk-Based Development (fast, CI-dependent), GitHub Flow (simple, PR-based), Git Flow (release branches, complex), GitLab Flow (environment branches). Choose based on team size, release cadence, and CI maturity.

## Applicable Scenarios
✅ **Best for**
- Team branching strategy selection
- Multi-environment release processes
- CI/CD maturity alignment

⚠️ **When NOT to use**
- The real question is how builds get promoted and verified — gates, environment promotion, rollback → **CI/CD Pipeline Design** owns that; branching is one input to it, not the decision
- A team of one or two, or a project with no shared release train — every multi-branch model adds merge and coordination work nobody has time for → trunk-based with short-lived feature branches is the only realistic choice
- Review quality and coding standards are the open problem → **Code Review Checklist** addresses that directly; a new branching model will not improve what reviewers miss
- A monorepo where different teams release independently → the strategy is decided per repo scope by the release tooling, and a single team-wide convention is the wrong unit of decision

## Key Steps
1. Assess: team size, release cadence, CI/CD maturity
2. Choose strategy:
   - **Trunk-Based**: small teams, fast CI, continuous deployment
   - **GitHub Flow**: simple PR-based, good for SaaS
   - **Git Flow**: release branches, good for versioned software
   - **GitLab Flow**: environment branches (dev/staging/prod)
3. Define branch naming conventions
4. Set up branch protection rules
5. Document the workflow for the team

## Output Template

```
Team: [n devs, n reviewers, shared repo?]   Release cadence: [continuous | weekly | monthly | on-demand]
CI maturity: [required suite duration, flaky rate, required checks configured?]

Strategy: [Trunk-Based | GitHub Flow | Git Flow | GitLab Flow]
  Why: [team size + cadence + CI maturity → this model]
  Rejected alternative: [name] — because: [one line]

Branch naming: [type/short-description — e.g. feat/checkout-retry]
Lifecycle: branch from [base] → merged into [base] → deleted [when]
Protected branches: [main, release/*]
Required checks: [lint, unit, build] — must complete in under [n] minutes
Environment branches (if any): [dev → staging → prod], promoted by [role]
Release flow: [tag format] → [artifact produced] → [published where]
Hotfix path: [branch from] → [merge back to] → [how it is verified]
Enforcement: [platform rules: naming, protection, required checks — not a wiki]
```

## Failure Modes
- Process heavier than the team: the chosen model demands merge coordination, release managers, or branch ceremonies nobody has time for → pick the model whose rituals the team can actually sustain; small teams should not run Git Flow
- Git Flow on a continuously deployed product → long-lived release branches accumulate conflicts, and every hotfix must be cherry-picked back into trunk → use trunk-based or GitHub Flow unless you genuinely ship versioned, supportable artifacts
- Branch protection combined with a slow CI, so reviewers wait and start merging around the pipeline → keep required checks under a few minutes and treat check duration as a blocking metric
- The strategy documented but not enforced — no naming rules, no protection, no required checks — so it decays within weeks → configure naming, protection, and required checks mechanically in the hosting platform; a convention nobody can violate is a wish
- No emergency hotfix path, so the hotfix branch is improvised during an outage → write the hotfix procedure down in advance, together with **Incident Response & Postmortem**

## Evidence Strength
Mixed — the four models are the standard vocabulary and their trade-offs are well described in practitioner literature, but comparative evidence that any one of them produces better delivery speed or defect rates is limited and mostly observational; in practice most teams labeled as using a given model run a modified version, so the label predicts less than the documentation implies.

## Source
Git workflow comparison; Atlassian Git tutorials; GitHub Flow documentation.
