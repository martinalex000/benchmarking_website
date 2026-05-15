# Extraction: arXiv:2501.03113
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: HyMN
- Type: GNN

## Results

### MOLBACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7915 | 0.0144 | Yes | this paper | Table 1 |
| GIN | 0.7297 | 0.0400 | Yes | this paper | Table 1 |
| FULL | 0.7841 | 0.0194 | Yes | this paper | Table 1 |
| OSAN (T = 10) | 0.7630 | 0.0300 | Yes | this paper | Table 1 |
| RANDOM (T = 2) | 0.7536 | 0.0428 | Yes | this paper | Table 1 |
| CS-GNN (T = 2) | 0.8058 | 0.0104 | Yes | this paper | Table 1 |
| POLICY-LEARN (T = 2) | 0.7840 | 0.0285 | Yes | this paper | Table 1 |
| HyMN (GIN, T=2) no CSE | 0.7822 | 0.0402 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.8116 | 0.0121 | No | this paper | Table 1 |
| RANDOM (T=5) | 0.7814 | 0.0236 | Yes | this paper | Table 1 |
| CS-GNN (T = 5) | 0.7964 | 0.0143 | Yes | this paper | Table 1 |
| POLICY-LEARN (T=5) | 0.7839 | 0.0228 | Yes | this paper | Table 1 |
| HyMN (GIN, T=5) no CSE | 0.7857 | 0.0131 | No | this paper | Table 1 |
| HyMN (GIN, T=5) | 0.8064 | 0.0048 | No | this paper | Table 1 |
| HyMN (GCN, T=2) | 0.8321 | 0.0051 | No | this paper | Table 2 |

### MOLHIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7606 | 0.0097 | Yes | this paper | Table 1 |
| GIN | 0.7558 | 0.0140 | Yes | this paper | Table 1 |
| FULL | 0.7654 | 0.0137 | Yes | this paper | Table 1 |
| MAG-GNN (T = 2) | 0.7712 | 0.0113 | Yes | this paper | Table 1 |
| RANDOM (T = 2) | 0.7755 | 0.0124 | Yes | this paper | Table 1 |
| CS-GNN (T = 2) | 0.7772 | 0.0076 | Yes | this paper | Table 1 |
| POLICY-LEARN (T = 2) | 0.7913 | 0.0060 | Yes | this paper | Table 1 |
| HyMN (GIN, T=2) no CSE | 0.7977 | 0.0070 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.8101 | 0.0117 | No | this paper | Table 1 |
| RANDOM (T=5) | 0.7730 | 0.0256 | Yes | this paper | Table 1 |
| CS-GNN (T = 5) | 0.7909 | 0.0090 | Yes | this paper | Table 1 |
| POLICY-LEARN (T=5) | 0.7849 | 0.0101 | Yes | this paper | Table 1 |
| HyMN (GIN, T=5) no CSE | 0.7962 | 0.0114 | No | this paper | Table 1 |
| HyMN (GIN, T=5) | 0.8017 | 0.0140 | No | this paper | Table 1 |
| HyMN (GCN, T=2) | 0.7682 | 0.0120 | No | this paper | Table 2 |
| GatedGCN | 0.7827 | 0.0065 | Yes | this paper | Table 3 |
| GatedGCN + CSE | 0.8033 | 0.0056 | Yes | this paper | Table 3 |
| HyMN (GatedGCN, T=2) w/out CSE | 0.7902 | 0.0091 | No | this paper | Table 3 |
| HyMN (GatedGCN, T=2) | 0.8107 | 0.0021 | No | this paper | Table 3 |
| Reconstr. GNN | 0.7632 | 0.0140 | Yes | this paper | Table 4 |
| DSS-GNN | 0.7678 | 0.0166 | Yes | this paper | Table 4 |
| GSN | 0.8039 | 0.0090 | Yes | this paper | Table 4 |
| CIN | 0.8094 | 0.0057 | Yes | this paper | Table 4 |
| GPS | 0.7880 | 0.0101 | Yes | this paper | Table 4 |
| GINE-MLP-Mixer | 0.7997 | 0.0102 | Yes | this paper | Table 4 |
| GINE-ViT | 0.7792 | 0.0142 | Yes | this paper | Table 4 |
| Nested-GNN | 0.7834 | 0.0186 | Yes | this paper | Table 4 |
| GNN-AK+ | 0.7961 | 0.0119 | Yes | this paper | Table 4 |
| SUN | 0.8003 | 0.0055 | Yes | this paper | Table 4 |
| GIN+CSE | 0.7744 | 0.0187 | Yes | this paper | Table 4 |
| HyMN (GIN, T=1) | 0.8036 | 0.0123 | No | this paper | Table 4 |

### MOLTOX21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7529 | 0.0069 | Yes | this paper | Table 1 |
| GIN | 0.7491 | 0.0051 | Yes | this paper | Table 1 |
| FULL | 0.7625 | 0.0112 | Yes | this paper | Table 1 |
| RANDOM (T = 2) | 0.7665 | 0.0089 | Yes | this paper | Table 1 |
| POLICY-LEARN (T = 2) | 0.7747 | 0.0082 | Yes | this paper | Table 1 |
| HyMN (GIN, T=2) no CSE | 0.7768 | 0.0071 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.7730 | 0.0035 | No | this paper | Table 1 |
| RANDOM (T=5) | 0.7662 | 0.0089 | Yes | this paper | Table 1 |
| POLICY-LEARN (T=5) | 0.7736 | 0.0060 | Yes | this paper | Table 1 |
| HyMN (GIN, T=5) no CSE | 0.7782 | 0.0059 | No | this paper | Table 1 |
| HyMN (GIN, T=5) | 0.7699 | 0.0045 | No | this paper | Table 1 |
| HyMN (GCN, T=2) | 0.7607 | 0.0050 | No | this paper | Table 2 |

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.6555 | 0.0088 | Yes | this paper | Table 1 |
| GIN + CSE | 0.6619 | 0.0077 | Yes | this paper | Table 1 |
| HyMN (GIN, T=1) | 0.6857 | 0.0055 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.6863 | 0.0050 | No | this paper | Table 1 |
| GCN | 0.6739 | 0.0024 | Yes | this paper | Table 1 |
| GCN + CSE | 0.6812 | 0.0037 | Yes | this paper | Table 1 |
| HyMN (GCN, T=1) | 0.6912 | 0.0170 | No | this paper | Table 1 |
| HyMN (GCN, T=2) | 0.6948 | 0.0052 | No | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Graph-ViT | 0.6942 | 0.0075 | Yes | this paper | Table 1 |
| G-MLP-Mixer | 0.6921 | 0.0054 | Yes | this paper | Table 1 |
| GatedGCN | 0.6558 | 0.0068 | Yes | this paper | Table 2 |
| GatedGCN + CSE | 0.6611 | 0.0058 | Yes | this paper | Table 2 |
| HyMN (GatedGCN, T=2) w/out CSE | 0.6723 | 0.0079 | No | this paper | Table 2 |
| HyMN (GatedGCN, T=2) | 0.6788 | 0.0052 | No | this paper | Table 2 |
| GIN + RWSE | 0.6621 | 0.0067 | Yes | this paper | Table 3 |
| GCN + RWSE | 0.6860 | 0.0050 | Yes | this paper | Table 3 |
| HyMN (GIN, T=1) w/out CSE | 0.6758 | 0.0050 | No | this paper | Table 4 |

### Peptides-Struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.2497 | 0.0012 | Yes | this paper | Table 1 |
| GIN + CSE | 0.2479 | 0.0011 | Yes | this paper | Table 1 |
| HyMN (GIN, T=1) | 0.2464 | 0.0013 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.2457 | 0.0012 | No | this paper | Table 1 |
| GCN | 0.2505 | 0.0023 | Yes | this paper | Table 1 |
| GCN + CSE | 0.2499 | 0.0010 | Yes | this paper | Table 1 |
| HyMN (GCN, T=1) | 0.2481 | 0.0013 | No | this paper | Table 1 |
| HyMN (GCN, T=2) | 0.2477 | 0.0010 | No | this paper | Table 1 |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Graph-ViT | 0.2449 | 0.0016 | Yes | this paper | Table 1 |
| G-MLP-Mixer | 0.2475 | 0.0015 | Yes | this paper | Table 1 |
| GatedGCN | 0.2497 | 0.0007 | Yes | this paper | Table 2 |
| GatedGCN + CSE | 0.2482 | 0.0010 | Yes | this paper | Table 2 |
| HyMN (GatedGCN, T=2) w/out CSE | 0.2473 | 0.0013 | No | this paper | Table 2 |
| HyMN (GatedGCN, T=2) | 0.2471 | 0.0007 | No | this paper | Table 2 |
| GIN + RWSE | 0.2478 | 0.0017 | Yes | this paper | Table 3 |
| GCN + RWSE | 0.2498 | 0.0015 | Yes | this paper | Table 3 |
| HyMN (GIN, T=1) w/out CSE | 0.2466 | 0.0010 | No | this paper | Table 4 |

### RDT-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9240 | 0.0250 | Yes | this paper | Table ef{tab:rdtb_accuracy} |
| SIN | 0.9220 | 0.0100 | Yes | bodnar2021cellular | Table ef{tab:rdtb_accuracy} |
| CIN | 0.9240 | 0.0210 | Yes | bodnar2021weisfeiler | Table ef{tab:rdtb_accuracy} |
| RANDOM (T=20) | 0.9260 | 0.0150 | Yes | this paper | Table ef{tab:rdtb_accuracy} |
| RANDOM (T=2) | 0.9240 | 0.0100 | Yes | this paper | Table ef{tab:rdtb_accuracy} |
| POLICY-LEARN (T=2) | 0.9300 | 0.0090 | Yes | bevilacqua2023efficient | Table ef{tab:rdtb_accuracy} |
| HyMN (T=2) | 0.9320 | 0.0220 | No | this paper | Table ef{tab:rdtb_accuracy} |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3210 | 0.0090 | Yes | this paper | Table 1 |
| GIN | 0.1630 | 0.0040 | Yes | xu2019powerful | Table 1 |
| GSN | 0.1010 | 0.0100 | Yes | bouritsas2022improving | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | bodnar2021cellular | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | rampášek2023recipe | Table 1 |
| GINE-MLP-Mixer | 0.0730 | 0.0010 | Yes | he2023generalization | Table 1 |
| GINE-ViT | 0.0850 | 0.0040 | Yes | he2023generalization | Table 1 |
| FULL | 0.0870 | 0.0030 | Yes | this paper | Table 1 |
| OSAN | 0.1770 | 0.0160 | Yes | qian2022ordered | Table 1 |
| POLICY-LEARN (T = 2) | 0.1200 | 0.0030 | Yes | bevilacqua2023efficient | Table 1 |
| RANDOM (T = 2) | 0.1360 | 0.0050 | Yes | this paper | Table 1 |
| GIN+CSE | 0.0920 | 0.0020 | Yes | this paper | Table 1 |
| HyMN (GIN, T=1) | 0.0800 | 0.0030 | No | this paper | Table 1 |
| HyMN (GIN, T=2) | 0.0830 | 0.0020 | No | this paper | Table 1 |
| HyMN (GIN, T=1) w/out CSE | 0.1250 | 0.0040 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN**
- **GIN**
- **FULL**
- **OSAN**
- **MAG-GNN**
- **RANDOM**
- **CS-GNN**
- **POLICY-LEARN** (from: bevilacqua2023efficient)
- **GatedGCN** (from: bresson2017residual)
- **Reconstr. GNN** (from: cotta2021reconstruction)
- **DSS-GNN**
- **GSN** (from: bouritsas2022improving)
- **CIN** (from: bodnar2021cellular)
- **GPS** (from: rampášek2023recipe)
- **GINE-MLP-Mixer** (from: he2023generalization)
- **GINE-ViT** (from: he2023generalization)
- **Nested-GNN** (from: zhang2021nested)
- **GNN-AK+**
- **SUN**
- **Graph-ViT**
- **G-MLP-Mixer** (from: he2023generalization)
- **SIN** (from: bodnar2021cellular)
- **GIN+CSE** (from: this paper)

## Extraction Notes

[MOLHIV] Extracted all results for MOLHIV from four different tables. Values were reported as
percentages (e.g., 81.01) and normalized to [0, 1] as per instructions. [MOLBACE] Extracted results
for MOLBACE from both Table 1 (subgraph GNNs with GIN backbone) and Table 2 (GCN backbone). Values
were normalized from percentages to [0, 1] range. [MOLTOX21] Extracted results for MOLTOX21 from
both Table 1 and Table 2. Table 2 refers to the dataset as 'MolTox', which is mapped to 'MOLTOX21'
per instructions. Values were normalized from percentages to [0, 1] range. [Peptides-Func] Extracted
all results for Peptides-Func across multiple tables. Table 1 provided the main comparison, Table 2
focused on GatedGCN backbone, Table 3 compared CSE vs RWSE, and Table 4 showed the effect of CSE on
HyMN. [Peptides-Struct] Extracted all MAE results for Peptides-Struct across four tables. Normalized
metric name to MAE as per caption instructions. [RDT-B] Excluded 'FULL' row as it reported 'OOM'
(Out of Memory) and provided no quantitative value. [ZINC] Extracted results from Table 1 and Table
2. Table 3 was a timing table that repeated values already present in Table 1. Parameter budget of
500k mentioned in text was used for proposed_model. [MUTAG] The paper mentions the MUTAG dataset in
the text (specifically regarding perturbation analysis and centrality measures), but no quantitative
benchmark results (such as Accuracy) for MUTAG are provided in any of the tables. The tables
provided cover OGB datasets, Peptides, MalNet-Tiny, RDT-B, and ZINC. [NCI1] The paper mentions the
NCI1 dataset in the text and figures for perturbation analysis (measuring distance between
representations of an untrained GIN model), but it does not report any quantitative benchmark
results (such as Accuracy) for NCI1 in any of the provided tables. All tables contain results for
other datasets (OGB, Peptides, MalNet, RDT-B, ZINC).

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*