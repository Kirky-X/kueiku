# Qualitative Synthesis

## Core Concept
Turn a pile of qualitative data — interview transcripts, field notes, support tickets — into a small set of themes, each backed by verbatim evidence and an honest confidence label. Five phases: Familiarize → Code → Theme → Synthesize → Report. Division of labor: Systematic Research Process runs the full research loop (question → search → output); this card owns the analysis half — what happens after data is already in hand. For study design before fieldwork, see Qualitative Research Plan (User Research).

## Applicable Scenarios
✅ **Best for**
- Data already collected: interview series, usability debriefs, open survey comments, support logs
- "We did 10 interviews — now what?"
- Producing findings someone can act on without re-reading every transcript

⚠️ **When NOT to use**
- Fewer than ~5 sources — patterns from 2 sources are anecdotes; write a memo or use Empathy Map instead
- Data is numeric or event logs — thematic coding adds subjectivity, not insight; analyze quantitatively
- The research question isn't framed yet — clarify it first (Systematic Research Process, step 1)

## Key Steps
1. **Familiarize**: read everything once before labeling anything. Per source, write a short memo: their story, 3-5 verbatim quotes, what they DO vs what they SAY, emotional intensity, what surprised you. Grade data quality — transcripts are richest; notes are pre-filtered by the note-taker; summaries are an interpretation layer (lowest trust).
2. **Code**: label meaningful excerpts. Start from interview questions and known frameworks (deductive), but let participants' own words become codes too (in-vivo) — the start list is a scaffold, not a cage. Maintain a tag table: code / one-line definition / example quote / frequency. Split codes that blur; merge codes only you can tell apart.
3. **Theme**: aggregate codes across participants. A theme is not a renamed code — apply the touch test: if you can physically touch it ("login screen", "pricing page"), it's a topic; keep abstracting until you can't ("users build private workarounds before ever asking for help"). Target 5-10 themes, each grounded in ≥2 independent sources.
4. **Synthesize**: map relations between themes — what conditions what, what leads to what, where themes contradict. Actively hunt negative cases and outliers: each one either sharpens a theme with a boundary condition or exposes it as overreach. Note absences — expected topics nobody raised are findings too.
5. **Report**: pearls, not oysters — the body explains; raw evidence goes to the appendix. Every theme ships with a claim, one luminous quote plus 2-3 echoes, prevalence (x of n), and a confidence label (High/Medium/Low) with its basis: source count, behavior vs stated, triangulation.

## Output Template

```
Theme 1: [untouchable insight phrase] — prevalence x/n — confidence H/M/L (basis: ...)
  Claim: [2-3 sentences, ties back to the research question]
  Evidence: > "[verbatim quote]" — [source ID, location]
             > "[echo]" — [ID]   > "[echo]" — [ID]
  Negative case: [who doesn't fit + why] | Absence: [expected, never heard]

Contradictions: [theme A vs theme B — who holds each side]
Open questions: [what this dataset cannot answer]
```

## Failure Modes
- Topic parade: "themes" that are touchable topics ("pricing", "onboarding") — labels, not insights → run the touch test on every theme
- Cherry-picked quotes: one vivid quote carrying a theme → every theme needs ≥2 independent sources and stated prevalence
- Premature coding: tagging during the first read → first pass is reading, memos precede codes; otherwise you code your expectations, not the data
- Buried disconfirmation: counter-evidence dropped to keep the story clean → negative cases go in the report, not the trash

## Evidence Strength
Practitioner consensus — thematic analysis is the standard qualitative method across UX and social science; its known limits are analyst subjectivity and small-n generalization, which evidence-linkage and confidence-labeling mitigate but cannot remove.

## Source
Thematic analysis tradition (Braun & Clarke).
Provenance: five-phase workflow absorbed from [cookiy-ai/user-research-skill](https://github.com/cookiy-ai/user-research-skill) (MIT license); sub-agent orchestration and platform bindings stripped, rewritten as a single-analyst method, absorbed 2026-09.
Admission: Build (new entry) — owns post-fieldwork qualitative analysis (code → theme → report); Systematic Research Process runs the research loop, not the analysis half.
