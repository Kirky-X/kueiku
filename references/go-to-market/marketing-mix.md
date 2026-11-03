# Marketing Mix (4Ps / 7Ps)

## Core Concept
The four decision levers — **Product, Price, Place, Promotion** (McCarthy 1960), extended to seven for services by adding **People, Process, Physical evidence** (Booms & Bitner 1981) — that must hang together as one coherent offer. The mix is not a strategy generator; it is the **assembly and coherence check**: each P is delegated to the entry that owns it, then the Ps are verified against each other, because the classic failure is not a bad P but contradictory Ps (premium price sold through a discount channel, features advertised that do not exist).

## Applicable Scenarios
✅ **Best for**
- Assembling a launch plan after STP decisions exist (its intended downstream, per STP's own template)
- Auditing an existing offer for internal contradiction across the Ps
- Service businesses needing the 7Ps extension (where people/process/physical evidence are the actual failure points)

⚠️ **When NOT to use**
- STP not yet decided — the mix follows segment/target/positioning; a mix without them is four independent guesses → **STP Analysis**
- Deciding a single P in depth → each P has an owner: Price → **Pricing Strategy**; Place/Promotion channel-type → **GTM Motions**; Product value → **Value Proposition Canvas** / **Business Model Canvas**
- Writing ad copy or campaign content → owned messaging/copy territory (**GTM Strategy** frame; copy craft is content work)
- Pure-digital SaaS forced through 7Ps — Place is trivial there; run the 4Ps coherence check and skip the service extension honestly

## Key Steps
1. Take the STP outputs as fixed inputs: segment, target, positioning statement
2. Populate each P with its current decision, delegating depth to the owning entry (one line per P at this level)
3. Run the pairwise coherence check on the loaded Ps: Price × Place (premium price in a bargain channel?), Product × Promotion (promised features that don't exist?), Price × Product (value metric mismatched with what is built?), Place × Promotion (promoting where the buyer cannot purchase?)
4. Fix contradictions by changing the P that is least strategically committed — the mix reveals which commitment is cheapest to move
5. For services, extend to 7Ps and re-check: People (who delivers), Process (how it is delivered), Physical evidence (what the customer sees)
6. Re-run the coherence check after any single-P change — the mix is a loop, not a document

## Output Template

```
Inputs from STP: segment [..] · target [..] · positioning [..]
Mix:
  Product   : [one line — what is offered]        owner: [Value Prop Canvas / BMC]
  Price     : [one line — metric + range]          owner: [Pricing Strategy]
  Place     : [one line — channels]                owner: [GTM Motions / GTM Strategy]
  Promotion : [one line — motion + message frame]  owner: [GTM Motions]
  (services) People/Process/Physical: [one line each]
Coherence check:
  Price×Place: [consistent? contradiction named if not]
  Product×Promotion: [...]
  Price×Product: [...]
  Place×Promotion: [...]
Fixes: [contradiction → the P changed → why that P]
Re-check trigger: [any single-P change re-runs the matrix]
```

## Failure Modes
- Four independent decisions pasted into one grid: the coherence check is the mechanism; a grid without it is decoration
- Mix before STP: the levers get pulled with no target defined, then every P fights the others → STP first, always
- Treating the mix as the strategy: 4Ps organizes decisions, it does not make them — an empty grid filled with generic words ("high quality, competitive price") signals the strategy step was skipped
- Service business running only 4Ps: the failure lives in People/Process/Physical evidence, the three Ps the framework without its extension cannot see
- Promotion treated as "make ads": the P is a budget and a measurement commitment → delegate to the channel entries and record what success reads
- One-P optimization loops: Price changed without re-checking Place and Promotion → the matrix is a loop; any change re-runs it

## Evidence Strength
**Practitioner consensus as an organizing scaffold.** 4Ps (McCarthy 1960) has organized marketing planning for over sixty years, and 7Ps (Booms & Bitner 1981) is the standard service extension; the 4Cs critique (Lauterborn 1990) correctly observes it is seller-side — buyer-side framing is carried in this corpus by JTBD and the Value Proposition Canvas. As a checklist the mix is durable; as a strategy generator it is empty — its value here is strictly the cross-P coherence discipline.

## Source
E. Jerome McCarthy, *Product and Market: A Basis for Marketing Planning* (1960, 4Ps); Booms & Bitner, "Marketing Organizations and Services Marketing" (1981, 7Ps); Lauterborn, "New Marketing Litany: Four Ps Passé: C-Words Take Over" (1990, 4Cs critique). Admission verdict: **Build** (v0.1.16) — `stp-analysis.md` step 4 and its output template point at a mix method held nowhere (live dead pointer, the v0.1.15 defect class); the cross-P coherence check is the mechanism no other entry owns, and the Ps delegate to their existing owners rather than duplicating them.
