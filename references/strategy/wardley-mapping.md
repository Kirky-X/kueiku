# Wardley Mapping

## Core Concept
Value chain (vertical axis) × evolution stage (horizontal axis) strategic terrain map. Genesis → Custom → Product → Commodity.

## Applicable Scenarios
✅ **Best for**
- Strategic evolution awareness, Build/Buy/Outsource decisions, competitive dynamics analysis

⚠️ **When NOT to use**
- Quick decisions on a component that is obviously commodity — just buy it; mapping adds nothing
- The user need cannot be stated plainly — evolution is meaningless without an anchor need at the top of the chain
- You want a point forecast — maps communicate position and drift, not dates; pair with scenario planning for timing

## Key Steps
1. Define the user need (anchor at top)
2. Map the value chain (components needed to fulfill the need)
3. For each component, assess evolution stage: Genesis (novel), Custom-Built (emerging), Product (standard), Commodity (ubiquitous)
4. Plot on the map
5. Identify strategic moves: build what's evolving, buy/outsource what's commoditized

## Output Template

```
User need: [one plain sentence]

  Need ──┬── [Component A]  custom-built   → build (differentiating)
         ├── [Component B]  product        → buy
         │      └── [Component B1] commodity → outsource
         └── [Component C]  genesis        → option: watch / seed experiment

Movement to expect: [A is drifting toward product within ~x years — plan the transition]
Weakness signals on map: [commodity treated as custom (legacy cost), genesis treated as product (premature standardization)]
Next action: [cheapest strategic move + date]
```

## Failure Modes
- Component soup: mapping at inconsistent granularity (a whole system beside one API call) → fix altitude: decompose until each box is independently buyable or buildable
- Evolution stage argued by opinion: "our CRM is definitely custom" → use stage proxies (certainty of specification, ubiquity of vendors, publication density) and let disagreement flag uncertainty
- Map without moves: a beautiful map that changes no decision → every map session ends with ≥1 build/buy/outsource/watch call and an owner

## Evidence Strength
Practitioner consensus — an applied practice with a growing practitioner base and useful open literature, but no controlled validation of mapping quality or outcome lift; its evolution axis is inherently judgment-based. Value lies in making evolution assumptions explicit and contestable.

## Source
Simon Wardley (2015); Wardley Mapping methodology.
