# Extraction: arXiv:2311.07966
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GIN + RM (Summation-MLP)
- Type: GNN

## Results

### ogbg-code2 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Plain GIN | 0.1495 | 0.0023 | Yes | Hu et al. 2020 | Table 1 |
| EGP | 0.1497 | 0.0015 | Yes | Deac et al. 2022 | Table 1 |
| GIN + 3-Regular Bipartite Expander + Learned Features | 0.1519 | 0.0020 | No | this paper | Table 1 |
| GIN + 3-Regular Bipartite Expander + Summation | 0.1254 | 0.0029 | Yes | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Plain GIN | 0.7558 | 0.0140 | Yes | Hu et al. 2020 | Table 2 |
| EGP | 0.7934 | 0.0035 | Yes | Deac et al. 2022 | Table 2 |
| GIN + PM (Learnt) | 0.7456 | 0.0149 | Yes | this paper | Table 2 |
| GIN + PM (Summation) | 0.7538 | 0.0150 | Yes | this paper | Table 2 |
| GIN + RM (Learnt) | 0.7503 | 0.0201 | Yes | this paper | Table 2 |
| GIN + RM (Summation) | 0.7730 | 0.0154 | Yes | this paper | Table 2 |
| GIN + RM (Masking) | 0.7439 | 0.0219 | Yes | this paper | Table 1 |
| GIN + RM (Learn-Features) | 0.7503 | 0.0201 | Yes | this paper | Table 1 |
| GIN + RM (Summation-MLP) | 0.7730 | 0.0154 | Yes | this paper | Table 1 |
| GIN + PM (Learn-Features) | 0.7456 | 0.0149 | Yes | this paper | Table 3 |
| GIN + PM (Summation-MLP) | 0.7538 | 0.0150 | Yes | this paper | Table 3 |
| GIN + PM_sp (Learn-Features) | 0.7518 | 0.0158 | Yes | this paper | Table 3 |
| GIN + PM_sp (Summation-MLP) | 0.7524 | 0.0206 | Yes | this paper | Table 3 |
| GIN + PM_at (Learn-Features) | 0.7511 | 0.0133 | Yes | this paper | Table 3 |
| GIN + PM_at (Summation-MLP) | 0.7614 | 0.0056 | Yes | this paper | Table 3 |
| k=3 Ramanujan Expander | 0.7688 | 0.0077 | Yes | this paper | Table 4 |
| k=5 Ramanujan Expander | 0.7774 | 0.0047 | Yes | this paper | Table 4 |
| k=7 Ramanujan Expander | 0.7848 | 0.0135 | Yes | this paper | Table 4 |

## Baseline Models Identified

- **Plain GIN** (from: Hu et al. 2020 (OGB))
- **EGP** (from: Deac et al. 2022)

## Extraction Notes

[ogbg-molhiv] Extracted all rows from Tables 1, 2, 3, and 4 which report ROC-AUC on ogbg-molhiv.
Note that Table 2 and Table 3 contain overlapping models (GIN+RM Summation-MLP appears in both).
Table 4 reports ablation on k-regular Ramanujan expanders. The 'proposed model' is identified as the
best performing variant in the main comparison (GIN+RM Summation-MLP), though the paper presents
multiple variants. All values are normalized to [0,1]. [ogbg-code2] Extracted all rows from the
provided table for the ogbg-code2 dataset. The table explicitly lists Test F1 scores. The proposed
model is identified as the one with the best result (colored Red). Baselines are identified by their
citations. All values are normalized to [0,1] range as they are F1 scores.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*