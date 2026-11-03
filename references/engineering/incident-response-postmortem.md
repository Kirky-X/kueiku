# Incident Response & Postmortem

## Core Concept
Detection → Response → Mitigation → Resolution + blameless postmortem + Action Item closure. Structured incident management that learns from failures without blaming individuals.

## Applicable Scenarios
✅ **Best for**
- Production incident emergency response
- On-Call process building
- Experience capture and learning

⚠️ **When NOT to use**
- No production impact yet — a failing build, a staging-only bug, a customer-reported annoyance with no outage → this is ordinary work, and running the incident process on it dilutes the signal and trains people to dismiss the process
- A slowdown with no user-visible impact yet → **Performance Optimization** (measure, locate, optimize, verify) is the right cycle; an incident process around a known, contained problem adds overhead
- A security incident with disclosure, legal, and forensic obligations → this entry covers learning, not breach handling; run the security response process alongside it
- Deciding what to alert on and who to page → **Observability** owns SLOs and burn-rate alerting, which is what determines whether anyone is woken up at all

## Key Steps
1. **Detect**: alert fires; on-call is paged
2. **Respond**: acknowledge; assemble incident team; start incident channel
3. **Mitigate**: take action to reduce user impact (rollback, failover, etc.)
4. **Resolve**: fix the root cause; verify recovery
5. **Postmortem**: within 48h, write blameless postmortem (timeline, impact, root cause, action items)
6. **Action Items**: assign owners and deadlines; track to completion

## Output Template

```
Incident: [id]   Severity: [SEV1-4]   Started: [time]   Detected by: [alert | customer | human]
Resolved: [time]   User impact window: [x min]   Commander: [role]

Timeline (written during the incident, not reconstructed later):
  [hh:mm] [alert fired: ...]  [hh:mm] [mitigation applied: ...]  [hh:mm] [recovery verified: ...]
Impact: [users affected / requests failed / SLO budget consumed]

Root cause: [one technical cause, one layer below the symptom]
Trigger: [what changed]

Action items (owner + date + verification, all three required):
  1. [action] — owner [name] — due [date] — verified by [check]
  2. [action] — owner [name] — due [date] — verified by [check]
Blameless scope: [system and behavior only — no individual named as cause]
Closure: next review [date]; overdue items escalated to [role]
```

## Failure Modes
- Action-item theater: the postmortem ends with a list of good intentions nobody owns → every action needs one owner, a date, and a verification check; unowned items are deleted, not assigned to a team, and the tracker is the only closure mechanism
- Blame assigned, so the next incident is reported late or not at all → scope blameless to actions and systems, and treat leadership's public commitment to that scope as a precondition, not a courtesy
- The postmortem is written weeks later, so the timeline is reconstructed from memory and the root cause is a plausible story → capture the timeline in the incident channel while it happens; a delayed postmortem is a hypothesis, not a record
- Mitigation and root cause are argued in the same conversation while users stay broken → split the work explicitly: fix forward and restore first, then analyze after service is back
- Action items tracked in a spreadsheet nobody opens → review open items at the start of every postmortem and escalate overdue ones to the leadership that owns them, or the same causes recur

## Evidence Strength
Strong — blameless postmortems, structured incident roles, and postmortem-driven action items are among the most consistently documented and widely adopted reliability practices, drawn from long-running SRE and incident-management programs; the supporting evidence is experiential and organizational rather than controlled, and the claim that postmortems prevent recurrence holds only when action-item closure is rigorous, which many organizations fail to sustain.

## Source
Google SRE methodology; PagerDuty incident response best practices.
