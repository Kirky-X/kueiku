# Cynefin Framework

## Core Concept
Classify problems into 4 domains: Clear (known knowns — best practice), Complicated (known unknowns — expert analysis), Complex (unknown unknowns — probe-sense-respond), Chaotic (unknowable — act first to stabilize). Each domain requires a different response strategy.

## Applicable Scenarios
✅ **Best for**
- Problem nature identification
- Pre-check before methodology selection
- Complex/uncertain situations

⚠️ **When NOT to use**
- The probe-or-analyze choice is already obvious — Cynefin is a triage aid, not a required label; classifying a settled call adds ceremony
- As difficulty language ("this problem is very complex") — the domains describe cause-effect visibility, not effort or importance; misuse degrades the categories
- Post-hoc narratives about past events — classifying history is easy and cheapens the sense-making; the framework exists to pick the next move
- A factual dispute between stakeholders — no domain classification settles a disagreement about facts; settle the facts first

## Key Steps
1. Describe the problem situation
2. Assess: can cause-effect be determined? (Clear: yes, everyone agrees; Complicated: yes, with expert analysis; Complex: only in retrospect; Chaotic: no)
3. Classify the domain
4. Apply the appropriate response:
   - **Clear**: Sense → Categorize → Respond (apply best practice)
   - **Complicated**: Sense → Analyze → Respond (apply expert analysis)
   - **Complex**: Probe → Sense → Respond (experiment, then respond)
   - **Chaotic**: Act → Sense → Respond (stabilize first, then analyze)
5. If the domain is unclear, use Framework Selection to decide

## Output Template

```
Situation: [what is happening, 2-3 sentences]
Cause-effect test: [determinable by anyone? / by experts? / only in retrospect? / not at all]
→ Domain: [Clear / Complicated / Complex / Chaotic]
Response route: [Sense-Categorize-Respond / Sense-Analyze-Respond / Probe-Sense-Respond / Act-Sense-Respond]
Concrete next move:
  - Clear → [the existing best practice applied]
  - Complicated → [which expertise, engaged with what question]
  - Complex → [safe-to-fail probe: action + observation + amplify/stop rule]
  - Chaotic → [the stabilizing act taken first]
Re-check trigger: [signal that the domain has shifted]
```

## Failure Modes
- Domain misdiagnosis: a Complex situation treated as Complicated — experts analyze forever and never probe → when expert analysis stalls or disagrees, switch to probe-sense-respond; the categories are about cause-effect visibility, not difficulty
- "Complex" as an excuse: the label becomes a reason to avoid analysis where cause-effect IS determinable → run the test honestly: can experts agree on a method, even if not on the answer?
- Chaotic overreach: ordinary turbulence treated as Chaos and diagnosis skipped → act-first is for genuine crisis; most situations allow a moment to classify
- One classification forever: domains drift as context shifts (a Clear practice decays into Complex) → re-classify when the current response stops working; drift is the normal case

## Evidence Strength
Practitioner consensus — an established sense-making framework in knowledge management and agile practice, valuable mainly for forcing the probe-vs-analyze choice before a method is picked. The domains are conceptual categories rather than measured ones: empirical validation of the four-domain taxonomy and its response prescriptions is limited, and the framework's authors position it as a sense-making device, not a predictive model.

## Source
Dave Snowden (1999); IBM Center for Systems and Cognitive Understanding.
