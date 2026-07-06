# Opportunity Score

## Core Idea
Quantifies the opportunity size for a user need through Importance × (1 − Satisfaction). Needs that are important but currently have low satisfaction score high, indicating the greatest product opportunities. Originated from Kano thinking but normalized to the 0–1 range for easy cross-comparison.

## Use Cases
- Already have user research data (importance + satisfaction) and need to prioritize requirements
- Find "low satisfaction, high importance" quick-win opportunities
- Validate product-market fit gaps

## Key Steps
1. For each candidate need/feature, have target users rate: Importance (1–5 or 1–10) + Current Satisfaction (1–5)
2. Normalize: Map both importance and satisfaction to 0–1 (e.g., on a 5-point scale: score = (rating−1)/4)
3. Calculate opportunity score: Opportunity = Importance × (1 − Satisfaction)
4. Sort by Opportunity score descending, focus on high-scoring items (high importance + low satisfaction = blue ocean)
5. High-scoring items with already-high satisfaction are satisfied needs; low-importance items aren't worth investing in even with low satisfaction

## Source
Dan Olsen, *The Lean Product Playbook* (2015)
