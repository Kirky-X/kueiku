# LLM Output Evaluation (Evals)

## Core Concept
A prompt or model change is a change to a stochastic system, and the only way to know whether it improved is a **fixed evaluation set scored identically before and after**. The mechanism has four parts: a golden set (curated input → expected-behavior pairs), scorers (deterministic checks first, LLM-as-a-judge with bias controls where judgment is needed), failure-first error analysis (read what broke before admiring the score), and a regression gate (a change that loses on the fixed set does not ship). It converts "the new prompt feels better" into a decidable comparison.

## Applicable Scenarios
✅ **Best for**
- Deciding whether a prompt, model, or retrieval-parameter change ships
- Building a regression gate so AI features stop silently degrading
- Comparing model vendors on your task (not on a leaderboard)
- Turning production failures into permanent test cases

⚠️ **When NOT to use**
- One-off generation read once by a human — just read it; an eval set for output nobody will compare is ceremony
- No fixed task definition yet — build the task and its output contract first; evals measure a defined job, not a vibe
- Product-level "did the feature move business metrics" → **A/B Test Analysis** (human users, online traffic)
- "Is this code secure / does this pass lint" → static analysis (**Security by Design**); evals judge model output quality, not code properties
- Sub-agent workflow scripts in ZCode → dynamic-workflows owns that authoring surface

## Key Steps
1. Define the task and output contract: what a good output must contain, forbid, and reference — if you cannot state it, you cannot score it
2. Build the golden set: 20-50 real cases spanning the happy path, known hard cases, adversarial inputs, and past production failures — composition matters more than size
3. Choose scorers in order: deterministic assertions (schema, exact substring, refusal check) → LLM-as-a-judge with a written rubric for the rest
4. Control judge bias: randomize answer order (position bias), pin output length or report it (verbosity bias), and use a judge model different from the tested one (self-preference)
5. Run baseline and candidate on the identical set, same temperature, same scorers — any difference outside the set invalidates the comparison
6. Do failure-first error analysis: read the losing cases before the aggregate score; the score says "worse", the failures say "what to fix"
7. Gate: block ship on regression of a fixed-set criterion; record the verdict with the score delta and the failing cases
8. Grow the set: every production failure becomes a golden-set case — the eval grows where the product actually breaks

## Output Template

```
Eval report — task: [one sentence + output contract]
Golden set: [n] cases — composition: [happy x, hard x, adversarial x, from-prod x]
Scorers: [deterministic: ... | judge: model X, rubric summary, bias controls applied]
Baseline: [score / case]   Candidate: [score / case]   Δ [±x]
Failure analysis: [case → what broke → suspected cause] (top 3)
Verdict: [ship | hold] — gate criterion [met | regressed on: ...]
Set updates: [production failures added as cases]
```

## Failure Modes
- Judging with the generator: the model grading its own output prefers it → use a different judge model, and spot-check judge verdicts against human labels
- Vibes-based comparison: two prompts tried on three ad-hoc inputs and a winner declared → no fixed set, no comparison; build the set before tuning anything
- Happy-path-only golden set: regressions live in the weird cases → the set must contain the adversarial and the previously-broken
- Score without error analysis: an aggregate number cannot tell you what to change → failures first, score second
- Set too small: n < ~20 makes every delta noise → 20-50 well-chosen cases beat 500 sloppy ones
- Contamination: eval cases leaked into the prompt (few-shot examples copied from the set) → the eval then measures memorization; keep the set out of all prompts
- Ignoring cost and latency: a 5% quality gain at 10× token cost is a loss → record tokens and latency per run alongside quality
- Frozen eval: the set never grows after launch → production failures are the highest-value cases; wire them in

## Evidence Strength
**Strong mechanism, crafted instrument.** Regression testing is standard engineering, and LLM-as-a-judge agreement with human preferences is documented (MT-Bench, Zheng et al. 2023) — but judge biases (position, verbosity, self-preference) are real and must be actively controlled, and eval-set design remains craft: a bad set certifies nothing. Treat judge scores as a relative signal between two runs on one set, not an absolute quality number.

## Source
Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023); Liu et al., "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment" (EMNLP 2023); Hamel Husain, "Your AI Product Needs Evals" (2024). Admission verdict: **Build** (v0.1.16) — ranked first by the independent necessity audit: highest frequency, zero sibling collision (diting reviews agent code, tiangang scans security; neither judges model output), and `shipping-artifacts.md`'s currency check ("documents older than the last model/prompt change → block ship") implies an eval gate this entry now owns. The stable residue of prompt/context design (its one durable rule: gate every prompt change on a fixed eval set) is folded in here; the unstable remainder is deferred.
