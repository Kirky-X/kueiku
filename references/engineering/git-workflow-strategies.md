# Git Workflow Strategies

## Core Concept
Strategy selection matrix: Trunk-Based Development (fast, CI-dependent), GitHub Flow (simple, PR-based), Git Flow (release branches, complex), GitLab Flow (environment branches). Choose based on team size, release cadence, and CI maturity.

## Applicable Scenarios
✅ **Best for**
- Team branching strategy selection
- Multi-environment release processes
- CI/CD maturity alignment

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

## Source
Git workflow comparison; Atlassian Git tutorials; GitHub Flow documentation.
