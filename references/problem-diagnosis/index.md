# Problem Diagnosis

**When to use**: A problem is known to exist, and you need to find the root cause or redefine the problem

| Method | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **5 Whys** | Ask "why" 5 times consecutively to penetrate the surface and find the root cause | Production incidents, business metric decline, process errors | `five-whys.md` |
| **Fishbone / Ishikawa** | Fishbone diagram: systematically list multi-dimensional causes | Quality issues, multi-factor influences, team collaborative analysis | `fishbone.md` |
| **First Principles** | Break analogies, reason up from fundamental axioms | Innovative design, disrupting existing solutions, breaking mental models | `first-principles.md` |
| **Pareto Analysis** | Identify the 20% of factors causing 80% of results, focus on the vital few | Resource allocation, problem prioritization, key driver identification | `pareto.md` |

## Minimum Information Requirements per Method

- **5 Whys / Fishbone**: A quantifiable or observable specific problem statement
- **First Principles**: Clear assumptions or analogies to challenge
- **Pareto Analysis**: Quantifiable impact metrics + candidate item list

## Routing Trigger Signals

- "Find root cause" / "Why did this fail" → 5 Whys (primary)
- "Disruptive thinking" / "Break assumptions" → First Principles (primary)
- "80/20 key identification" / "Focus resources" → Pareto Analysis (primary)
- "Multi-factor cause analysis" / "Fishbone diagram" → Fishbone / Ishikawa (primary)
