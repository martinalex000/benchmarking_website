# Extraction: SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: Graph Coarsening (Proposed Method)
- Type: Other

## Results

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Original Graph | 0.7520 | — | Yes | this paper | Table 2 |
| Coarsened Graph | 0.7390 | — | No | this paper | Table 2 |

### DD — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Original Graph | 0.7490 | — | Yes | this paper | Table 2 |
| Coarsened Graph | 0.7400 | — | No | this paper | Table 2 |

### OGBG-MolHIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Original Graph | 0.7940 | — | Yes | this paper | Table 2 |
| Coarsened Graph | 0.7870 | — | No | this paper | Table 2 |

### OGBG-MolPPA — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Original Graph GNN | 0.7670 | — | Yes | this paper | Table 2 |
| Coarsened Graph GNN | 0.7440 | — | No | this paper | Table 2 |

### REDDIT-MULTI-12K — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Original Graph | 0.4920 | — | Yes | this paper | Table 2 |
| Coarsened Graph | 0.4810 | — | No | this paper | Table 2 |

## Baseline Models Identified

- **Original Graph (Baseline)**
- **Original Graph GNN**
- **Original Graph**

## Extraction Notes

[OGBG-MolHIV] Extracted results for OGBG-MolHIV from Table 2. The table compares 'Original' vs
'Coarsened' graphs. The 'Original' column represents the baseline performance on the standard graph,
and 'Coarsened' represents the proposed method's performance. No standard deviation is reported in
the table. The metric is ROC-AUC (implied by context of MolHIV benchmark and value range 0-1, though
column header just says 'Evaluation', the values match typical ROC-AUC scores for this dataset). The
percentage in parentheses (e.g., 99.11%) indicates the ratio of coarsened to original performance,
not a separate metric. [OGBG-MolPPA] Extracted results for OGBG-MolPPA from Table 2. The table
compares 'Original' vs 'Coarsened' graph configurations. The 'Original' column represents the
baseline performance on the standard dataset, and 'Coarsened' represents the proposed method's
performance. No standard deviation is reported in the table. The metric is ROC-AUC (implied by the
context of MolPPA and typical GNN benchmarks, and the values are between 0 and 1). The values 0.767
and 0.744 correspond to the 'Evaluation' columns for Original and Coarsened respectively. [COLLAB]
Extracted results for COLLAB from Table 2. The table compares 'Original' vs 'Coarsened' graphs. The
'Coarsened' result corresponds to the proposed method's evaluation on the coarsened graph structure,
while 'Original' serves as the baseline using the original graph structure with the same GNN
architecture (implied by the context of comparing training time and evaluation performance). No
standard deviation is reported in the table. [DD] Extracted results for dataset 'DD' from Table 2.
The table reports 'Evaluation' performance for 'Original' and 'Coarsened' graphs. The values 0.749
and 0.740 are interpreted as Accuracy based on the context of graph classification benchmarks and
the focus instruction. The 'Coarsened' column represents the proposed method's performance, while
'Original' represents the baseline. No standard deviation is reported in the table. [REDDIT-
MULTI-12K] Extracted results for REDDIT-MULTI-12K from Table 2. The table compares 'Original' vs
'Coarsened' graphs. The 'Evaluation' column for Original is 0.492 and for Coarsened is 0.481. Given
the context of graph classification benchmarks like REDDIT-MULTI-12K, these values represent
Accuracy (or similar classification score), as they are between 0 and 1 and consistent with typical
performance levels for this dataset. The paper does not explicitly label the column 'Accuracy', but
'Evaluation' in this context with these values implies Accuracy. No standard deviation is reported
in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*