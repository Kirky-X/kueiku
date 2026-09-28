# Security by Design

## Core Concept
STRIDE threat modeling + secure coding patterns + CI continuous verification. Security is built in from the start, not bolted on later.

## Applicable Scenarios
✅ **Best for**
- Security architecture design
- Compliance requirements
- Security hardening

⚠️ **When NOT to use**
- As the only security activity — threat models complement, not replace, penetration testing and incident response readiness
- One-shot compliance theater: a threat model written for the audit and never updated as the system changes → security by design is a cadence, not a document
- Rebuilding everything for imagined attackers before knowing your assets — start from what's valuable and reachable, not from paranoia

## Key Steps
1. **Threat Model**: use STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)
2. **Secure Coding**: apply language-specific secure coding patterns
3. **CI Verification**: integrate SAST, dependency scanning, secret detection into CI
4. **Defense in Depth**: multiple layers of security controls
5. **Regular Audits**: periodic security reviews and penetration testing

## Output Template

```
System: [scope + trust boundaries + assets ranked by value]

STRIDE per boundary: [user → API]
  Spoofing:            [threat → mitigation: authN mechanism]
  Tampering:           [threat → mitigation: signatures/input validation]
  Repudiation:         [threat → mitigation: audit logging]
  Information Disclosure: [threat → mitigation: encryption/ACLs]
  Denial of Service:   [threat → mitigation: rate limits]
  Elevation of Privilege: [threat → mitigation: authz least-privilege]

CI gates: SAST [tool] / dependency scan [tool] / secret detection [tool] — blocking severity: [level]
Review cadence: threat model revisited on [every new trust boundary / quarterly]
Known accepted risks (documented, signed off): [list + expiry date]
```

## Failure Modes
- STRIDE-by-rote: each cell filled with "N/A" or a generic control — the model proves nothing → every mitigation names the specific mechanism and where it's enforced in code
- Scanner = security: green CI mistaken for safety — SAST misses design flaws and logic abuse → scanners cover known patterns; the threat model covers what's unique to your system
- Accepted risks without expiry: "we'll fix it later" entries living for years → every accepted risk carries a sign-off and a re-review date

## Evidence Strength
Practitioner consensus — building security in earlier is well supported by the cost asymmetry of fixing defects late, and STRIDE/OWASP practice is industry standard; quantitative evidence on specific process elements (how much threat modeling reduces incidents) is limited, and effectiveness depends heavily on actually maintaining the artifacts.

## Source
Microsoft STRIDE model; OWASP secure coding guidelines.
