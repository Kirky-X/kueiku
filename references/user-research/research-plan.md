# Qualitative Research Plan

## Core Concept
Design the whole study before talking to any user: goal → method & sample → screener → interview guide → analysis plan. Division of labor with The Mom Test: Mom Test is the interviewing *attitude* (ask about past facts, not future predictions); this card is the *full study design* — who to recruit, what to ask, how findings feed a decision. It sits upstream of analysis cards: its outputs (transcripts from well-chosen participants) are the raw material Empathy Map and Customer Journey Map consume.

## Applicable Scenarios
✅ **Best for**
- Planning generative interviews, usability tests, diary studies, contextual inquiries
- Vague research requests ("we want to talk to users about onboarding") that need structure
- Before recruiters are engaged or a discussion guide is written

⚠️ **When NOT to use**
- The decision is already made and only confirmation is wanted — research can't help; skip it
- The question is quantitative (how many / how much) — run surveys or log analysis
- Informal 1:1 chats with no recruitment, screener, or guide — a checklist suffices

## Key Steps
1. **Clarify the goal**: write the Big Q — specific enough to answer, broad enough for surprise — starting with a finite outcome verb: describe / identify / evaluate / compare / characterize ("understand" and "explore" have no finish line). Then decision mapping: name the concrete decision this research feeds ("whether to add X to the roadmap"). No decision = sideshow; fix or cancel. Draft the Little q: an experience-near opener ("tell me how you handle X day-to-day").
2. **Choose method & sample**: how people actually do it → contextual inquiry; mental models and motivations → semi-structured interviews (default); behavior over time and triggers → diary study. Sample: ~5 per segment for usability (uncovers ~80% of issues), 8-12 per segment for generative interviews (thematic saturation). Profile by behavior, not demographics — "switched tools in the last 6 months" beats "ages 25-40".
3. **Design the screener**: 2-4 questions, screen-outs first so unqualified applicants exit cheaply. No yes/no questions — people agree to win the incentive; ask for specific tools, quantities, dates instead. Clarity over cleverness: ambiguous phrasing silently screens out the qualified. If budget allows, end with one articulacy check ("tell me about a recent time you…") — a storied answer previews interview data quality.
4. **Write the interview guide**: hourglass structure (general → specific → general). Open with master/apprentice framing: the participant is the expert; "we're testing the product, not you." Excavate stories — on "I usually…", redirect: "walk me through a specific time that happened." Probe with their own words ("what were you thinking at that moment?", "what happened next?"). Ban leading questions:
   - "Is this easy to use?" → "How would you describe using it?"
   - "Don't you hate when…?" → "What happened the last time you…?"
   - "Would you use a feature that…?" → "What did you do last time you needed to…?"
5. **Pre-register the analysis plan**: before fieldwork, fix the coding approach (in-vivo: participants' words; descriptive: your labels), the dimensions you'll code, and how themes map back to the Big Q's decision. This is the contract that stops post-hoc storytelling; deviations get documented, not hidden.

## Output Template

```
Big Q: [finite-verb question] → Feeds decision: [one concrete decision]
Method: [interviews / inquiry / diary] — n=[8-12 generative / 5 usability] per segment — [60] min
Screener: Q1 [screen-out] → Q2 [target behavior] → Q3 [articulacy check]
Guide: Little q opener → topics as story prompts + probes → summary check + wrap-up
Analysis plan (pre-registered): [coding approach + dimensions] → mapped to [decision]
```

## Failure Modes
- "Understanding" as the goal: open-ended objectives never terminate → rewrite with a finite verb and a named decision
- Demographic recruiting: screening for age and title instead of the behavior under study → recruit people who actually do the thing
- Leading questions smuggled in: the answer is installed by the question → episodes and past behavior only; the ban list above is the check
- Post-hoc analysis: themes decided after seeing the data → pre-register dimensions in step 5 and treat them as a commitment device

## Evidence Strength
Practitioner consensus — grounded in documented interview biases (social desirability, incentive gaming) and widely taught research-design practice; sample-size figures are heuristic saturation estimates, not statistical guarantees.

## Source
Qualitative research methodology tradition (contextual inquiry, master-apprentice framing).
Provenance: five-phase planning flow absorbed from [cookiy-ai/user-research-skill](https://github.com/cookiy-ai/user-research-skill) (MIT license); platform bindings stripped, rewritten in kueiku style, absorbed 2026-09.
Admission: Build (new entry) — owns whole-study design before fieldwork (goal → sample → screener → guide → analysis plan); user-research entries each covered a single method, not the sequencing.
