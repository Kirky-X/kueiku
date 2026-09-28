# The Mom Test

## Core Concept
Even your mom will say your idea is great — so don't ask "what do you think of my idea", ask about her **past** real behaviors. Rob Fitzpatrick proposes 10 rules, the core being: avoid collecting false positive feedback.

## Applicable Scenarios
- Early-stage startup/new feature, need user interviews to validate demand
- You find yourself pitching ideas instead of listening
- Interview conclusions are always "users say they like it" but conversion data is poor

⚠️ **When NOT to use**
- Testing usability of a concrete design — you need task-based usability testing, not life-history interviews
- Expert/beta users giving technical feedback on a working build — specific critique here is genuine signal, not social politeness
- You need market sizing — interviews explain why, not how many; pair with Opportunity Score or market research

## Key Steps
1. Ask about the past, not the future — "last time you encountered problem X, what did you do?" not "would you use feature X?"
2. Don't pitch your idea — once you pitch, the other person will socially agree
3. 80/20 listening — you talk 20%, let the user talk 80%
4. Capture strong emotional signals — "I hate that process", "I spent three hours" — these are 10x more important than "it's fine"
5. Validate commitment, not opinions — "have you paid for this?", "what alternatives have you tried?"

## Output Template

```
Interview: [who, role, when] — script adherence: [pitched or not]

Signals (past behavior only):
  Problem: [specific episode — last time, what happened, cost in time/money]
  Emotion: [verbatim quotes with heat: "I nearly missed the deadline because ..."]
  Workarounds: [spreadsheet/VA/manual process — strongest demand evidence]
  Commitment: [paid: y/n + what for / tried: which alternatives / invested time: ...]

Verdict on the problem: validated / not yet / invalid — based on: [n episodes of real spending or heavy workaround]
Feature reactions collected (LOW trust): [what they said about our idea — note, don't conclude]
Next: [who else to interview / what behavior to observe in-product]
```

## Failure Modes
- Compliment collection: "that's great!" logged as validation → only past behavior and sunk costs count as evidence; opinions are recorded and discarded
- Leading questions smuggled in: "don't you hate how X takes forever?" — the answer was installed by the question → script questions around episodes, not evaluations
- Over-generalizing from 3 interviews: three anecdotes become a roadmap → interviews set hypotheses; in-product behavior or experiments must confirm at scale

## Evidence Strength
Practitioner consensus — grounded in well-documented survey/interview biases (social desirability, stated vs revealed preference); the method is a bias-avoidance discipline, not a statistical technique, and small-n anecdote risk remains its known limit.

## Source
Rob Fitzpatrick, *The Mom Test* (2013)
