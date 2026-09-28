# OODA Loop

## Core Concept
When the situation is still moving and you must act before certainty, cycle Observe → Orient → Decide → Act faster than the situation compounds: for reversible moves, act at ~70% confidence, then immediately re-observe. A late perfect plan loses to a fast loop — but the bottleneck is usually **Orient** (synthesis), not raw speed; a team that orients badly just produces wrong decisions faster.

## Applicable Scenarios
✅ **Best for**
- Incident response, outage, or ongoing degradation where state is still moving
- Debugging a moving target (intermittent failure, live traffic shift)
- Any time-bounded decision where waiting for full certainty costs more than a reversible action
- Competitive or adversarial settings where the faster cycle time is itself the advantage

⚠️ **When NOT to use**
- The situation is static and you have time — deliberate analysis or a hypothesis differential wins
- The next action is irreversible or high blast-radius — raise the evidence bar; 70% is not enough
- A cheap localization check (failing diff, log line, one metric) would end the uncertainty — test that hypothesis directly instead of looping
- No time pressure and no changing environment — the loop adds churn without value

## Key Steps
1. **Observe (time-boxed)**: gather the cheapest high-signal state now — metrics, logs, alerts, recent deploys/config, and feedback from the last action. Cap the window; never collect forever
2. **Orient**: match observations to a pattern and form **≥2 competing explanations**. Update or discard the mental model when data contradicts it — refuse single-hypothesis lock
3. **Decide**: pick one reversible action that tests the leading hypothesis. State the confidence (~70% threshold for reversible moves), the predicted effect, the next observation to check, and a time box for that check
4. **Act**: execute once, decisively, with a known rollback or degrade path
5. **Re-observe immediately**: compare outcome to prediction within the time box; feed the result into the next Observe. If Act is never followed by re-observe, the loop is broken — fix that before another action
6. **Exit explicitly** when any of: the system is stable; the remaining work is static analysis; the next step requires irreversible commitment — then switch to the matching methodology

## Output Template

```
Cycle record (repeat per loop):
1. Observed — current signals, what changed since last cycle
2. Orientation — ≥2 hypotheses; which leads and why
3. Decision — action, confidence, predicted effect, next observation, time box
4. Act + result — what ran; what the immediate re-observe showed
5. Loop status — continue | stable | exit to another method
```

## Failure Modes
- Looping without a nameable reversible next action plus a refuting observation → stop and gather evidence or escalate instead
- Single-hypothesis Orient → confirmation spiral; force the second candidate explanation before every Decide
- Applying OODA to static design work or irreversible launches → wrong tool; use deliberation and raise the evidence bar instead
- Waiting for 100% confidence on reversible mitigations under active pressure → the 70% threshold exists for exactly this case

## Timing Trio
- **Before**: `premortem-counterfactual.md` — rehearse how the planned approach could fail
- **During**: OODA Loop — cycle reversible moves while the situation is still moving
- **After**: `engineering/incident-response-postmortem.md` — extract learning once stable

## Evidence Strength
Mixed — the loop is an enduring staple of military doctrine and operations practice, and cycle-time advantage is well-attested; the ~70% confidence threshold and "Orient is the bottleneck" diagnosis are practitioner heuristics, and the Korean War origin narrative is anecdotal rather than rigorously validated.

## Source
John Boyd's Observe–Orient–Decide–Act loop, derived from Korean War air-combat analysis (the faster-cycling pilot reacts to current information while the slower one reacts to obsolete information); the ~70% confidence threshold is a practitioner heuristic for reversible moves under pressure.
Provenance: framework ideas absorbed from [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) `thinking-ooda` and [knowledge-skills](https://github.com/deciqAI/knowledge-skills) `ooda-loop` (both MIT license), absorbed 2026-09.
Admission: Build (new entry) — owns live-incident decision cycling (act before certainty); Incident Response & Postmortem requires the event to be over.
