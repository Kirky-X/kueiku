# ML Stock Selection

## Core Concept
Use machine learning models to predict returns or classify up/down for stock selection. Features from fundamental, technical, and alternative data. Handles nonlinear factor combinations.

## Applicable Scenarios
✅ **Best for**
- Factor nonlinear combination
- High-dimensional feature stock selection
- Alpha signal discovery

## Key Steps
1. **Feature Engineering**: build features from fundamental (DuPont ratios, etc.), technical (momentum, volatility), and alternative data
2. **Label Definition**: define prediction target (forward return, up/down classification)
3. **Model Selection**: try multiple models (Linear, Tree-based, Neural Network)
4. **Training**: cross-validation, avoid look-ahead bias, use rolling windows
5. **Evaluation**: IC, rank IC, long-short portfolio performance, turnover
6. **Deployment**: ensemble models, monitor for concept drift

## Source
Machine learning in finance literature; Gu, Kelly & Xiu (2020).
