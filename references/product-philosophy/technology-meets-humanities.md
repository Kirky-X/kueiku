# Technology Meets Humanities

## Core Concept
Great products require 3-dimension assessment: Technology (does it work?) × Humanities (does it resonate with humans?) × Business (is it viable?). A single perspective is insufficient for good products.

## Applicable Scenarios
✅ **Best for**
- Product evaluation
- Design decisions
- Team building

⚠️ **When NOT to use**
- One dimension already binds the decision — a hard compliance, safety, or performance constraint makes a three-way assessment ceremony; score only the binding dimension and check the others for contradiction
- Pre-PMF exploration — "does it resonate with humans" cannot be read off a product that does not exist yet; this evaluates products, it does not discover them → **Design Thinking** for the discovery phase
- Incident and defect triage — the framework assesses what to build and has no mechanism for locating a live fault → root-cause analysis instead
- Team building as the deliverable — the assessment is the output; assembling T-shaped people is one implementation choice, not the framework itself

## Key Steps
1. For any product decision, assess all 3 dimensions:
   - Technology: Is it technically feasible? Scalable? Reliable?
   - Humanities: Does it resonate emotionally? Is it accessible? Does it respect users?
   - Business: Is it economically viable? Does it serve the business model?
2. If any dimension scores poorly, the product decision is incomplete
3. Build teams with T-shaped skills covering all 3 dimensions
4. Use the 3-dimension framework in design reviews

## Output Template

```
Decision: [what is being decided]
Technology: [feasible? scalable? reliable?] — evidence: [measured value, or the named unknown]
Humanities: [resonates? accessible? respects users?] — evidence: [measured value, or the named unknown]
Business: [viable? serves the model?] — evidence: [measured value, or the named unknown]
Weakest dimension: [dimension | what it costs if it stays weak]
What changes if we fix it: [the specific product decision this score flips]
```

## Failure Modes
- Scorecard without evidence: each dimension gets a confident yes or no from memory → attach measured evidence per dimension or write "unknown"; unmeasured assessments are opinions arranged in a table
- Business used as the decider: the dimension that decides is whichever one the decision-maker already favors → declare which dimension is genuinely binding before scoring
- Humanities as decoration: taste judgments dressed as research → require user evidence and separate what was observed from what is preferred
- The multiplication misread: "one weak dimension kills the product" ignores that the dimensions trade off differently and audience varies → judge each dimension against the audience you actually serve
- Framework used to justify a settled decision: the score arrives after the choice → score the strongest alternative too; a framework that only ever confirms is a rationalizer

## Evidence Strength
Mixed — the three-dimension framing is a durable synthesis of design and product practice with no controlled evidence behind the combination, and its parts are unevenly grounded: technical feasibility and business viability have established estimation disciplines, while "resonance with humans" is measured, when it is measured at all, by qualitative research whose findings are contested and sample-dependent. Its reliable use is as a completeness check that stops a single-perspective decision — usually the engineer's — from being taken as a product decision; the cost is a false sense of balance when the three scores are not comparable in rigor.

## Source
Steve Jobs: "It is in Apple's DNA that technology alone is not enough — it's technology married with liberal arts that yields the best results."
