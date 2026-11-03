# Monte Carlo Simulation & Quantitative Risk

## Core Concept
Turn a model whose inputs are uncertain into an output **distribution** instead of a point answer: give every uncertain input a distribution, sample them many times, push each sample through the model, and read the resulting spread. What a point estimate hides becomes visible — the median, the P10/P90 band, and above all the tail (VaR, Expected Shortfall) where ruin lives. The arithmetic is exact given the model; the judgment sits in the input distributions and, fatally, in the correlation assumptions.

## Applicable Scenarios
✅ **Best for**
- Financial exposure: expected loss, portfolio risk, pricing, reserves, project cash flow under variable rates and volumes
- Any risk whose aggregate must be summed across uncertain, partly dependent components
- "How bad can this get, and what drives it" on a model with several interacting uncertainties
- Decisions where the downside tail (not the mean) drives the choice

⚠️ **When NOT to use**
- One uncertain quantity → Probabilistic Reasoning (base rate + likelihood ratio) is cheaper and clearer
- A handful of countable discrete outcomes → Decision Tree & Expected Value gives the exact number; simulation adds sampling noise for nothing
- You cannot state input distributions credibly → the simulation is a precision costume over invented numbers; get a reference class first or state the model qualitatively
- Deterministic compliance, safety, or legal questions → these need a defensible answer, not a distribution
- The question is simply "big or small" → the overhead is not repaid
- Inputs are known and bounded, with no interaction → interval reasoning or FMEA ranks as well

## Key Steps
1. Define the model: write the output as an explicit function of the inputs; if you cannot, you cannot simulate it
2. Specify each input's distribution with a stated basis (empirical data, reference class, or justified assumption) — mark which are assumed
3. Handle correlation explicitly: state the copula or the common-factor structure; if you assume independence, say so and test the sensitivity of the answer to it
4. Sample and converge: run enough iterations that the output statistics stop moving (report the convergence check, not just the count)
5. Read the distribution, not the mean: median, P10/P90 band, tail measures (VaR at a stated confidence, Expected Shortfall beyond it), and the probability of breaching a hard limit
6. Find the drivers: rank inputs by their contribution to output variance (tornado chart, rank correlation) — this is usually the actionable output
7. Stress-test the correlated case: model the joint shock scenario (rates, demand, regulation moving together) and read the loss there
8. Document: distributions, correlation assumptions, seed, iteration count, and what the result does *not* cover

## Output Template

```
Model: [output = f(input1, input2, ...)]
Inputs:
  [input] — distribution: [dist + basis: empirical | reference class | assumed] — [flag]
Correlation: [structure assumed + which pairs are dependent + independence test result]
Simulation: [iterations] — convergence: [stat stable at N]
Output distribution: median [x], P10/P90 [a, b], VaR95 [y], ES95 [z]
Breach probability: [P(loss > limit) = ...]
Drivers (variance contribution): [ranked inputs]
Stress case: [joint shock scenario → result]
Limitations: [what is not modeled; confidence + assumptions recorded]
```

## Failure Modes
- Invented distributions tuned to a comfortable answer → every distribution needs a stated basis; if the basis is "it felt right", the output is a mirror
- Independence assumed where inputs move together → the most damaging error, because the tail is then badly understated; model the common factor and compare the two answers
- Simulation without a convergence check → 1,000 iterations looks authoritative and is noise; report when the statistics stabilize
- Reading the mean only → ruin lives in the tail; a project with positive expected value and 20% chance of bankruptcy is not a good project
- Precision costume: 6 inputs, 2 of them guessed → the output has more decimal places than the inputs deserve; screen inputs first, then simulate
- Correlation fudged to make the answer stable → if you cannot defend the correlation, present a range of correlation assumptions instead of one number
- Presenting P95 without naming what was modeled → the number travels and loses its conditions
- Simulating a model with no causal structure: correlations baked in as coefficients, then re-simulated → you are running your assumptions, not reality

## Evidence Strength
**Strong for the method, conditional on the inputs.** Monte Carlo is a deterministic computation over sampled distributions: the technique itself is exact and verifiable, and it is standard practice in financial risk, engineering reliability, and insurance. The uncertainty lives entirely in the distributional and correlation choices — and those are judgment, not computation, so a rigorous-looking result can rest on invented inputs. The technique earns its reputation precisely by making that dependence visible; use it for the spread, not for false certainty.

## Source
David Luenberger, *Investment Science* (1998); Edward O. Thorp, *The Mathematics of Finance* (2002); McNeil, Frey & Embrechts, *Quantitative Risk Management* (2005); Rockafellar & Uryasev, "Optimization of Conditional Value-at-Risk", *Journal of Risk* (2000). Admission verdict: **Build** (v0.1.15) — `risk-matrix.md` routed quantitative exposure to "FMEA or Monte Carlo", but no entry held Monte Carlo; the missing target was a genuine gap, not a duplicate of FMEA (continuous unbounded distributions vs ranked discrete failure modes).
