# Dependency Management

## Core Concept
Introduction assessment + version strategy + security monitoring + health audit. Systematic approach to managing third-party dependencies throughout their lifecycle.

## Applicable Scenarios
✅ **Best for**
- Dependency selection decisions
- Vulnerability response
- Dependency health audits

⚠️ **When NOT to use**
- A known-vulnerable dependency with a published fix — this framework decides policy; an emergency upgrade doesn't wait for an audit cycle
- Vendored/internal-only code — external-dependency hygiene (registry trust, license checks) applies differently
- Standard-library available — the best dependency assessment for a small utility is often "don't add it"

## Key Steps
1. **Evaluate before adding**: necessity, maintenance status, license, security track record
2. **Version strategy**: pin to major.minor; use lock files; automate updates
3. **Security monitoring**: integrate dependency vulnerability scanning in CI
4. **Health audit**: quarterly review of dependency health (outdated, unmaintained, vulnerable)
5. **Removal plan**: for each dependency, know how to replace it if needed

## Output Template

```
Add/drop decision record:
  Candidate: [lib v2.3] — need: [what it does that we can't cheaply build]
  Health: last release [date], open issues [n/age], maintainers [n], downloads trend [↗]
  License: [MIT/Apache — compatible? y] — transitive deps: [n, any red flags]
  Security: [known CVEs: none/advisories]
  Exit plan: [how we'd replace it — wrapper layer? y/n]

Policy in force: pin [major.minor], lockfile committed, updates via [renovate/dependabot] with [test gate]
Quarterly audit: [n outdated / n unmaintained >12mo / n with CVEs] → actions: [upgrade / wrap / plan exit]
```

## Failure Modes
- Addition-by-convenience without exit thinking: six months later the un-wrapped library owns your data layer → wrap heavyweight dependencies behind your own interface where swap risk is real
- Pin-and-forget: versions frozen "for stability", security updates never land → automated updates with test gates; pinning is for reproducibility, not for freezing
- Audit as spreadsheet: the quarterly review finds issues and records them without actions → every red health flag gets an owner and a date, or the audit is inventory, not management

## Evidence Strength
Practitioner consensus — the practices (lockfiles, automated updates, CI scanning, license checks) are industry-standard and align with OWASP guidance; quantitative claims about optimal cadences are thinner, and the deep dependency-graph problem (transitive risk) remains only partially addressable by any policy.

## Source
Dependency management best practices; OWASP dependency check guidelines.
