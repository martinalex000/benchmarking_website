# Extraction: arXiv:2505.15405
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: HOPSE
- Type: GNN

## Results

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6979 | 0.0680 | Yes | this paper | Table 1, Table 2 |
| GAT | 0.7277 | 0.0277 | Yes | this paper | Table 1, Table 2 |
| GIN | 0.7957 | 0.0613 | Yes | this paper | Table 2 |
| SCN | 0.7362 | 0.0613 | Yes | this paper | Table 2 |
| SCCNN | 0.7617 | 0.0663 | Yes | this paper | Table 1, Table 2 |
| SaNN | 0.7957 | 0.0356 | Yes | this paper | Table 2 |
| GCCN | 0.8596 | 0.0466 | Yes | this paper | Table 1, Table 2 |
| HOPSE-M | 0.8638 | 0.0631 | No | this paper | Table 1, Table 2 |
| HOPSE-G | 0.8553 | 0.0277 | No | this paper | Table 1, Table 2 |
| CCCN | 0.7702 | 0.0932 | Yes | this paper | Table 2 |
| CWN | 0.8043 | 0.0178 | Yes | this paper | Table 2 |
| GCN+PSEs | 0.8426 | 0.0356 | Yes | this paper | Table 1 |
| GAT+PSEs | 0.8043 | 0.0508 | Yes | this paper | Table 1 |

### NAME — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4214 | 0.0272 | Yes | this paper | Table 2 |
| GAT | 0.1809 | 0.0065 | Yes | this paper | Table 2 |
| GIN | 0.7614 | 0.0014 | Yes | this paper | Table 2 |
| SCN | 0.7948 | 0.0136 | Yes | this paper | Table 2 |
| SCCNN | 0.9508 | 0.0056 | Yes | this paper | Table 2 |
| SaNN | 0.8176 | 0.0137 | Yes | this paper | Table 2 |
| GCCN | 0.8676 | 0.0127 | Yes | this paper | Table 2 |
| HOPSE-M | 0.9150 | 0.0145 | No | this paper | Table 2 |
| HOPSE-G | 0.8175 | 0.0126 | No | this paper | Table 2 |
| GIN+PSEs | 0.9405 | 0.0015 | Yes | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7286 | 0.0069 | Yes | this paper | Table 1 |
| GCN+PSEs | 0.7488 | 0.0054 | Yes | this paper | Table 1 |
| GAT | 0.7500 | 0.0100 | Yes | this paper | Table 1 |
| GAT+PSEs | 0.7786 | 0.0102 | Yes | this paper | Table 1 |
| SCCNN | 0.7660 | 0.0175 | Yes | this paper | Table 1 |
| GCCN | 0.7685 | 0.0150 | Yes | this paper | Table 1 |
| HOPSE-M | 0.7735 | 0.0081 | No | this paper | Table 1 |
| HOPSE-G | 0.7770 | 0.0140 | No | this paper | Table 1 |
| GIN | 0.7426 | 0.0096 | Yes | this paper | Table 2 |
| SCN | 0.7449 | 0.0103 | Yes | this paper | Table 2 |
| SaNN | 0.6875 | 0.0164 | Yes | this paper | Table 2 |
| CCCN | 0.7667 | 0.0148 | Yes | this paper | Table 2 |
| CWN | 0.7393 | 0.0187 | Yes | this paper | Table 2 |

### NCI109 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7220 | 0.0122 | Yes | this paper | Table 1 |
| GCN+PSEs | 0.7470 | 0.0079 | Yes | this paper | Table 1 |
| GAT | 0.7380 | 0.0073 | Yes | this paper | Table 1 |
| GAT+PSEs | 0.7557 | 0.0060 | Yes | this paper | Table 1 |
| SCCNN | 0.7712 | 0.0107 | Yes | this paper | Table 1 |
| GCCN | 0.7576 | 0.0128 | Yes | this paper | Table 1 |
| HOPSE-M | 0.7634 | 0.0140 | No | this paper | Table 1 |
| HOPSE-G | 0.7636 | 0.0175 | No | this paper | Table 1 |
| GIN | 0.7442 | 0.0070 | Yes | this paper | Table 2 |
| SCN | 0.7570 | 0.0104 | Yes | this paper | Table 2 |
| SaNN | 0.6817 | 0.0088 | Yes | this paper | Table 2 |
| CCCN | 0.7535 | 0.0150 | Yes | this paper | Table 2 |
| CWN | 0.7380 | 0.0206 | Yes | this paper | Table 2 |

### ORIENT — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5628 | 0.0045 | Yes | this paper | Table 1 |
| GIN+PSEs | 0.8253 | 0.0078 | Yes | this paper | Table 1 |
| SCCNN | 0.8629 | 0.0123 | Yes | this paper | Table 1 |
| GCCN | 0.7660 | 0.0167 | Yes | this paper | Table 1 |
| HOPSE-M | 0.8924 | 0.0022 | No | this paper | Table 1 |
| HOPSE-G | 0.6217 | 0.0098 | Yes | this paper | Table 1 |
| GCN | 0.4794 | 0.0000 | Yes | this paper | Table 2 |
| GAT | 0.4794 | 0.0000 | Yes | this paper | Table 2 |
| SCN | 0.6955 | 0.0097 | Yes | this paper | Table 2 |
| SaNN | 0.6165 | 0.0055 | Yes | this paper | Table 2 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7570 | 0.0214 | Yes | this paper | Table 1 |
| GCN+PSEs | 0.7577 | 0.0298 | Yes | this paper | Table 1 |
| GAT | 0.7634 | 0.0166 | Yes | this paper | Table 1 |
| GAT+PSEs | 0.7548 | 0.0344 | Yes | this paper | Table 1 |
| SCCNN | 0.7419 | 0.0286 | Yes | this paper | Table 1 |
| GCCN | 0.7491 | 0.0251 | Yes | this paper | Table 1 |
| HOPSE-M | 0.7513 | 0.0366 | No | this paper | Table 1 |
| HOPSE-G | 0.7627 | 0.0210 | No | this paper | Table 1 |
| GIN | 0.7520 | 0.0330 | Yes | this paper | Table 2 |
| SCN | 0.7527 | 0.0214 | Yes | this paper | Table 2 |
| SaNN | 0.7505 | 0.0352 | Yes | this paper | Table 2 |
| CCCN | 0.7333 | 0.0230 | Yes | this paper | Table 2 |
| CWN | 0.7613 | 0.0270 | Yes | this paper | Table 2 |

### ZINC-12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6200 | 0.0100 | Yes | this paper | Table 1 |
| GAT | 0.6100 | 0.0100 | Yes | this paper | Table 1 |
| GIN | 0.5700 | 0.0400 | Yes | this paper | Table 1 |
| SCN | 0.5300 | 0.0400 | Yes | this paper | Table 1 |
| SCCNN | 0.3600 | 0.0200 | Yes | this paper | Table 1 |
| SaNN | 0.5500 | 0.0100 | Yes | this paper | Table 1 |
| GCCN | 0.3500 | 0.0100 | Yes | this paper | Table 1 |
| HOPSE-M | 0.3900 | 0.0200 | No | this paper | Table 1 |
| HOPSE-G | 0.4300 | 0.0100 | No | this paper | Table 1 |
| CCCN | 0.3400 | 0.0200 | Yes | this paper | Table 1 |
| CWN | 0.3400 | 0.0100 | Yes | this paper | Table 1 |
| GCN+PSEs | 0.4300 | 0.0300 | Yes | this paper | Table main_table_TDL |
| GAT+PSEs | 0.3900 | 0.0200 | Yes | this paper | Table main_table_TDL |

### β1 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.8813 | 0.0000 | Yes | this paper | Table 1 |
| GIN+PSEs | 0.9028 | 0.0005 | Yes | this paper | Table 1 |
| SCCNN | 0.9020 | 0.0020 | Yes | this paper | Table 1 |
| GCCN | 0.8420 | 0.0480 | Yes | this paper | Table 1 |
| HOPSE-M | 0.9102 | 0.0143 | No | this paper | Table 1 |
| HOPSE-G | 0.8828 | 0.0008 | Yes | this paper | Table 1 |
| GCN | 0.4686 | 0.0450 | Yes | this paper | Table 2 |
| GAT | 0.0745 | 0.0005 | Yes | this paper | Table 2 |
| SCN | 0.7645 | 0.0306 | Yes | this paper | Table 2 |
| SaNN | 0.8846 | 0.0009 | Yes | this paper | Table 2 |

### β2 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0093 | 0.0121 | Yes | this paper | Table 1 |
| GIN+PSEs | 0.6843 | 0.0059 | Yes | this paper | Table 1 |
| SCCNN | 0.6582 | 0.0270 | Yes | this paper | Table 1 |
| GCCN | 0.4182 | 0.2019 | Yes | this paper | Table 1 |
| HOPSE-M | 0.8229 | 0.0046 | No | this paper | Table 1 |
| HOPSE-G | 0.3537 | 0.0225 | Yes | this paper | Table 1 |
| GCN | 0.0000 | 0.0000 | Yes | this paper | Table 2 |
| GAT | 0.0000 | 0.0000 | Yes | this paper | Table 2 |
| SCN | 0.0545 | 0.0231 | Yes | this paper | Table 2 |
| SaNN | 0.3922 | 0.0280 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **GCN**
- **GAT**
- **GIN**
- **SCN**
- **SCCNN**
- **SaNN**
- **GCCN**
- **CCCN**
- **CWN**
- **GCN+PSEs**
- **GAT+PSEs**
- **GIN+PSEs**
- **HOPSE-G**

## Extraction Notes

[MUTAG] Extracted results from both Table 1 (which separates models by Graph, Simplicial, and Cell
categories) and Table 2. Note that GCCN and HOPSE variants appear in multiple categories (Simplicial
and Cell) with slightly different results; all were extracted as they represent different
configurations/categories in the paper. [PROTEINS] Extracted results for PROTEINS from both Table 1
(main_table_TDL) and Table 2 (main_table). Table 1 contains results categorized by Graph,
Simplicial, and Cell types, while Table 2 provides a broader benchmark comparison. All values were
normalized from percentages to [0, 1]. [NCI1] Extracted results for NCI1 from both Table 1 (which
separates models by Graph, Simplicial, and Cell categories) and Table 2. Values were normalized from
percentages to [0, 1] range. [NCI109] Extracted results for NCI109 from both Table 1
(main_table_TDL) and Table 2 (main_table). Table 1 contains results categorized by Graph,
Simplicial, and Cell configurations. Table 2 provides a consolidated view including additional
baselines like GIN, SCN, SaNN, CCCN, and CWN. [ZINC-12K] Extracted results from both Table 1
(benchmark datasets) and Table main_table_TDL. Note that GCCN appears twice in the benchmark table
under different categories (Simplicial and Cell) with different results; both are included. The
'Cell' category results for ZINC-12K are significantly lower (better) than the 'Simplicial' category
results. [NAME] Extracted results from Table 1 (main topological tasks) and Table 2 (benchmark
datasets). Note that HOPSE-M has different values in Table 1 vs Table 2; both are included as they
represent different reporting contexts in the paper. Ablation table results were skipped as per the
'STANDARD / DEFAULT configuration' rule. [ORIENT] Extracted results for ORIENT from Table 1 and
Table 2. Note that HOPSE-M has slightly different values between Table 1 (0.8924) and Table 2
(0.8068), likely due to different experimental settings or reporting versions in the paper; both are
included. Ablation table was partially provided but only the main model results were prioritized as
per standard configuration rules. [β1] Extracted results for dataset β1 from Table 1 and Table 2.
Table 3 was partially provided but contained ablation variants (Adj-1, Adj-2) which were skipped per
instructions to use only standard/default configurations. Values were normalized from percentages to
[0, 1]. [β2] Extracted results for β2 from Table 1 and Table 2. Note that Table 1 and Table 2 report
slightly different values for the same models on β2 (e.g., HOPSE-M is 82.29 in Table 1 and 71.69 in
Table 2), likely due to different experimental settings or reporting versions in the paper.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*