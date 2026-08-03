# Incident Response & Postmortem

## Core Concept
Detection → Response → Mitigation → Resolution + blameless postmortem + Action Item closure. Structured incident management that learns from failures without blaming individuals.

## Applicable Scenarios
✅ **Best for**
- Production incident emergency response
- On-Call process building
- Experience capture and learning

## Key Steps
1. **Detect**: alert fires; on-call is paged
2. **Respond**: acknowledge; assemble incident team; start incident channel
3. **Mitigate**: take action to reduce user impact (rollback, failover, etc.)
4. **Resolve**: fix the root cause; verify recovery
5. **Postmortem**: within 48h, write blameless postmortem (timeline, impact, root cause, action items)
6. **Action Items**: assign owners and deadlines; track to completion

## Source
Google SRE methodology; PagerDuty incident response best practices.
