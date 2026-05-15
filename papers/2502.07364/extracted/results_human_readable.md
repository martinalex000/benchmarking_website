# Extraction: arXiv:2502.07364
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: DropSens
- Type: GNN

## Results

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| None | 0.8189 | — | Yes | topping2022understanding | Table 1(a) |
| +FA | 0.8165 | — | Yes | topping2022understanding | Table 1(a) |
| DIGL (PPR) | 0.8321 | — | Yes | topping2022understanding | Table 1(a) |
| SDRF | 0.8276 | — | Yes | topping2022understanding | Table 1(a) |
| DropSens | 0.8498 | — | No | this paper | Table 1(a) |

## Baseline Models Identified

- **None**
- **Last FA**
- **Every FA**
- **DIGL**
- **SDRF**
- **FoSR** (from: karhadkar2023fosr)
- **GTR** (from: black2023resistance)
- **+FA** (from: topping2022understanding)
- **DIGL (PPR)** (from: topping2022understanding)

## Extraction Notes

[SyntheticZINC] The provided table contains results for Mutag, Proteins, Enzymes, Reddit, IMDb, and
Collab. No results for the requested dataset 'SyntheticZINC' were present in the provided text.
[Cora] Extracted results for Cora from Table 1(a). Values were converted from percentages to
decimals. Baselines were sourced from topping2022understanding as indicated in the table caption.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*