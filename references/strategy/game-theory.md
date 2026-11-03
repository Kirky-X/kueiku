# Game Theory & Nash Equilibrium

## Core Concept
Model multi-party decisions as games — players, strategies, payoffs — and predict outcomes that are stable because no player gains by unilateral deviation (Nash equilibrium). The discipline it imposes: stop analyzing your move in isolation; derive the other side's best response first, then your best response to that. It also classifies the game type — prisoners' dilemma (individually rational, collectively bad), coordination, zero-sum, repeated — because the escape from a bad structure is changing the game (commitment, communication, repetition), not playing it better.

## Applicable Scenarios
✅ **Best for**
- Competitive moves where rivals visibly react: pricing against a responder, feature races, bidding/auctions
- Multi-party platform/standard contests and coalition building
- Designing cooperation: contracts, alliances, retaliation rules in repeated relationships
- Any plan silently assuming "the competitor will do nothing"

⚠️ **When NOT to use**
- Single-agent decisions with no strategic interaction (capacity, portfolio, prioritization) — the game frame adds nothing
- 3+ players with unknown payoffs: assumptions collapse and you are decorating opinions with equilibrium language
- Behavioral or emotional conflicts — use Stakeholder Mapping; people are not payoff functions. One counterpart with terms on the table → Principled Negotiation (Decision Making)
- Payoffs not estimable even ordinally — garbage-in equilibria: the matrix looks rigorous and is fiction

## Key Steps
1. Name the players — include the absent ones your move affects (regulators, customers, rivals' rivals)
2. List each player's realistic strategies (including "do nothing")
3. Estimate the payoff matrix per combination; ordinal (win/lose/draw) is enough
4. Mark each player's best response in every column/row
5. Locate the Nash equilibrium or equilibria — where no unilateral deviation pays
6. Classify the game: dilemma / coordination / zero-sum / repeated — a dilemma verdict points to changing payoffs (commitment devices, repetition, side-payments), not to playing harder
7. Derive the move: play the equilibrium, commit visibly (burn the option), signal credibly, or restructure payoffs

## Output Template

```
Players: [each with what they actually control]
Strategies per player: [2-4 realistic options each, "do nothing" included]
Payoff matrix: [ordinal outcome per combination — who gains, who bleeds]
Best responses: [marked per cell]
Equilibrium(a): [stable outcomes + whether multiple]
Game type verdict: [dilemma / coordination / zero-sum / repeated]
Move: [play it / commit / signal / change the payoffs — and the concrete device]
Confidence: [what the verdict survives: payoffs wrong by how much?]
```

## Failure Modes
- Equilibrium worship: multiple equilibria or none in pure strategies → report the set; the real question becomes which one coordination selects
- Rationality overreach: assuming a counterpart optimizes when they satisfice or spite → bound the analysis with best-response ranges instead of point predictions
- Payoff numbers invented to complete the matrix → ordinal and honest beats cardinal and fake; state what would change the verdict
- One-shot analysis of a repeated game: repetition flips incentives (cooperation via tit-for-tat becomes stable); check the shadow of the future before concluding defection
- Decorative matrix: if the completed matrix does not change the move you would have made anyway, the tool misfit — say so and stop

## Evidence Strength
Strong formal core — equilibrium existence results, auction design, and mechanism design are in live industrial use (spectrum auctions, ad auctions); informal strategic sketches have a mixed transfer record, and applied equilibrium claims routinely overstate their precision. Nobel-recognized lineage (Nash, Schelling, auction design).

## Source
John von Neumann & Oskar Morgenstern, *Theory of Games and Economic Behavior* (1944); John Nash, "Equilibrium Points in N-Person Games" (1950); Thomas Schelling, *The Strategy of Conflict* (1960). Admission verdict: **Build** (v0.1.11) — interdependent-decision modeling was absent from the strategy corpus: Porter's Five Forces is static industry structure, not move-and-countermove.
