# Extraction: arXiv:2407.02758
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Ours
- Type: GNN

## Results

### CIFAR10-SP — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | Kipf 2016 | Table 1 |
| MoNet | 0.5465 | 0.0052 | Yes | Monti 2017 | Table 1 |
| GraphSAGE | 0.6577 | 0.0031 | Yes | Hamilton 2017 | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | Xu 2019 | Table 1 |
| GCNII | 0.5608 | 0.0020 | Yes | Chen 2020 | Table 1 |
| PNA | 0.7035 | 0.0063 | Yes | Corso 2020 | Table 1 |
| DGN | 0.7284 | 0.0042 | Yes | Beaini 2021 | Table 1 |
| Cy2C-GNNs | 0.6429 | 0.0001 | Yes | Choi 2022 | Table 1 |
| ARGNP | 0.7390 | 0.0015 | Yes | Cai 2022 | Table 1 |
| CRaWl | 0.6901 | 0.0026 | Yes | Toenshoff 2021 | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | Zhao 2021 | Table 1 |
| 3WLGNN | 0.5917 | 0.0159 | Yes | Maron 2019 | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | Hussain 2022 | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + SSFG | 0.7194 | 0.0019 | Yes | Zhang 2022 | Table 1 |
| EdgeGCN | 0.7613 | 0.0040 | Yes | Zhang 2023 | Table 1 |
| Exphormer | 0.7475 | 0.0019 | Yes | Shirzad 2023 | Table 1 |
| TIGT | 0.7396 | 0.0036 | Yes | Choi 2024 | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | Ma 2023 | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | Rampásek 2022 | Table 1 |
| Ours | 0.7907 | 0.0027 | No | this paper | Table 1 |
| GCN + differential enc. | 0.6202 | 0.0036 | Yes | this paper | Table 3 |
| GAT + differential enc. | 0.6737 | 0.0042 | Yes | this paper | Table 3 |
| MPNN only | 0.7682 | 0.0022 | Yes | this paper | Table 2 |
| MPNN + differential encoding | 0.7782 | 0.0009 | Yes | this paper | Table 2 |
| Global attention only | 0.4524 | 0.0135 | Yes | this paper | Table 2 |
| Global attention + differential encoding | 0.6447 | 0.0054 | Yes | this paper | Table 2 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.1339 | 0.0044 | Yes | this paper | Table 1 |
| GCNII | 0.1404 | 0.0011 | Yes | this paper | Table 1 |
| GatedGCN | 0.2641 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN + RWSE | 0.2574 | 0.0034 | Yes | this paper | Table 1 |
| Transformer + LapPE | 0.2618 | 0.0031 | Yes | this paper | Table 1 |
| SAN + LapPE | 0.2592 | 0.0158 | Yes | this paper | Table 1 |
| SAN + RWSE | 0.2434 | 0.0156 | Yes | this paper | Table 1 |
| Exphormer | 0.3455 | 0.0009 | Yes | this paper | Table 1 |
| GPS | 0.3412 | 0.0044 | Yes | this paper | Table 1 |
| Ours | 0.3567 | 0.0026 | No | this paper | Table 1 |

### MNIST-SP — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | Kipf 2016 | Table 1 |
| MoNet | 0.9081 | 0.0003 | Yes | Monti 2017 | Table 1 |
| GraphSAGE | 0.9731 | 0.0010 | Yes | Hamilton 2017 | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | Xu 2019 | Table 1 |
| GCNII | 0.9067 | 0.0014 | Yes | Chen 2020 | Table 1 |
| PNA | 0.9794 | 0.0012 | Yes | Corso 2020 | Table 1 |
| Cy2C-GNNs | 0.9777 | 0.0000 | Yes | Choi 2022 | Table 1 |
| CRaWl | 0.9794 | 0.0005 | Yes | Toenshoff 2021 | Table 1 |
| 3WLGNN | 0.9507 | 0.0096 | Yes | Maron 2019 | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | Hussain 2022 | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + SSFG | 0.9798 | 0.0003 | Yes | Zhang 2022 | Table 1 |
| EdgeGCN | 0.9843 | 0.0006 | Yes | Zhang 2023 | Table 1 |
| Exphormer | 0.9855 | 0.0004 | Yes | Shirzad 2023 | Table 1 |
| TIGT | 0.9823 | 0.0013 | Yes | Choi 2024 | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | Ma 2023 | Table 1 |
| GPS (base model) | 0.9805 | 0.0013 | Yes | Rampásek 2022 | Table 1 |
| Ours | 0.9856 | 0.0006 | No | this paper | Table 1 |
| MPNN only | 0.9799 | 0.0012 | Yes | this paper | Table 2 |
| MPNN + differential encoding | 0.9829 | 0.0008 | Yes | this paper | Table 2 |
| Global attention only | 0.9756 | 0.0015 | Yes | this paper | Table 2 |
| Global attention + differential encoding | 0.9791 | 0.0006 | Yes | this paper | Table 2 |
| Full Model | 0.9853 | 0.0006 | Yes | this paper | Table 2 |
| GCN + differential enc. | 0.9473 | 0.0014 | Yes | this paper | Table 3 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 3 |
| GAT + differential enc. | 0.9716 | 0.0015 | Yes | this paper | Table 3 |

### OGBG-PPA — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6839 | 0.0084 | Yes | Kipf 2016 | Table 1 |
| GCN + virtual node | 0.6857 | 0.0061 | Yes | this paper | Table 1 |
| GIN | 0.6892 | 0.0100 | Yes | Xu 2019 | Table 1 |
| GIN + virtual node | 0.7037 | 0.0107 | Yes | this paper | Table 1 |
| DeeperGCN | 0.7712 | 0.0071 | Yes | this paper | Table 1 |
| ExpC | 0.7976 | 0.0072 | Yes | Yang 2022 | Table 1 |
| K-Subtree SAT | 0.7522 | 0.0056 | Yes | this paper | Table 1 |
| GPS | 0.8015 | 0.0033 | Yes | Rampavsek 2022 | Table 1 |
| Ours | 0.8096 | 0.0029 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 1 |
| GCNII | 0.3161 | 0.0004 | Yes | this paper | Table 1 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 1 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3242 | 0.0008 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.3341 | 0.0006 | Yes | this paper | Table 1 |
| Graph Diffuser | 0.3388 | 0.0011 | Yes | Glickman 2023 | Table 1 |
| GPS | 0.3337 | 0.0006 | Yes | Rampásek 2022 | Table 1 |
| Ours | 0.3459 | 0.0005 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | Kipf 2016 | Table 1 |
| GINE | 0.1265 | 0.0076 | Yes | Hu 2019 | Table 1 |
| GCNII | 0.1698 | 0.0080 | Yes | Chen 2020 | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + RWSE | 0.2860 | 0.0085 | Yes | Rampásek 2022 | Table 1 |
| Transformer + LapPE | 0.2694 | 0.0098 | Yes | Dwivedi 2022 | Table 1 |
| SAN + LapPE | 0.3230 | 0.0039 | Yes | Dwivedi 2022 | Table 1 |
| SAN + RWSE | 0.3216 | 0.0027 | Yes | Dwivedi 2022 | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | Shirzad 2023 | Table 1 |
| GPS | 0.3748 | 0.0109 | Yes | Rampásek 2022 | Table 1 |
| Ours | 0.4242 | 0.0011 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| Gated + RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Ours | 0.6608 | 0.0046 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **MoNet** (from: Monti 2017)
- **GraphSAGE** (from: Hamilton 2017)
- **GIN** (from: Xu 2019)
- **GCNII** (from: Chen 2020)
- **PNA** (from: Corso 2020)
- **DGN** (from: Beaini 2021)
- **Cy2C-GNNs** (from: Choi 2022)
- **ARGNP** (from: Cai 2022)
- **CRaWl** (from: Toenshoff 2021)
- **GIN-AK+** (from: Zhao 2021)
- **3WLGNN** (from: Maron 2019)
- **EGT** (from: Hussain 2022)
- **GatedGCN** (from: Bresson 2017)
- **GatedGCN + SSFG** (from: Zhang 2022)
- **EdgeGCN** (from: Zhang 2023)
- **Exphormer** (from: Shirzad 2023)
- **TIGT** (from: Choi 2024)
- **GRIT** (from: Ma 2023)
- **GPS** (from: Rampásek 2022)
- **MPNN only** (from: this paper)
- **MPNN + differential encoding** (from: this paper)
- **Global attention only** (from: this paper)
- **Global attention + differential encoding** (from: this paper)
- **GCN + differential enc.** (from: this paper)
- **GAT** (from: this paper)
- **GAT + differential enc.** (from: this paper)
- **GINE** (from: Hu 2019)
- **GatedGCN + RWSE** (from: Rampásek 2022)
- **Transformer + LapPE** (from: Dwivedi 2022)
- **SAN + LapPE** (from: Dwivedi 2022)
- **SAN + RWSE** (from: Dwivedi 2022)
- **GatedGCN+RWSE**
- **Transformer+LapPE**
- **SAN+LapPE**
- **SAN+RWSE**
- **Graph Diffuser** (from: Glickman 2023)
- **GCN + virtual node** (from: this paper)
- **GIN + virtual node** (from: this paper)
- **DeeperGCN** (from: this paper)
- **ExpC** (from: Yang 2022)
- **K-Subtree SAT** (from: this paper)
- **Gated + RWSE**

## Extraction Notes

[MNIST-SP] Extracted all rows from Table 1, Table 2, and Table 3 that correspond to the MNIST-SP
dataset. Values were converted from percentages to [0,1] range. Standard deviations were parsed from
the '±' notation. The 'Full Model' in Table 2 appears to be a variant of the proposed method but is
listed separately from 'Ours' in Table 1; both are included as they represent distinct experimental
configurations reported in the paper. Table 3 reports ablation on GCN and GAT with differential
encoding, which are also included. [CIFAR10-SP] Extracted all CIFAR10-SP Accuracy results from Table
1, Table 2, and Table 3. Values were converted from percentages to [0,1] range. Standard deviations
were parsed from the 'mean ± std' format. All rows corresponding to CIFAR10-SP were included.
[PascalVOC-SP] Extracted only PascalVOC-SP results as requested. The primary metric F1 was used. All
baseline and proposed model rows from Table 1 were included. Values were normalized to [0,1] range.
Standard deviations were parsed from the ± notation. [COCO-SP] Extracted all rows from Table 1 for
the COCO-SP dataset. The primary metric F1 was used. Values are normalized to [0,1]. Standard
deviations were parsed from the '±' notation. The proposed model is labeled as 'Ours' in the table.
[PCQM-Contact] Extracted MRR results for PCQM-Contact from Table 1. All values are normalized to
[0,1]. The proposed model is labeled 'Ours'. Baselines include GNNs and Transformers. Source hints
provided for Graph Diffuser and GPS based on citations in the table. [OGBG-PPA] Extracted all rows
from Table 1 for OGBG-PPA. Values were converted from percentages to [0,1] range as per
instructions. Standard deviations were parsed from the '±' notation. The proposed model is referred
to as 'Ours' in the table. [Peptides-func] Extracted all rows from Table 1 (labeled tab:peptifunc)
for the Peptides-func dataset. The metric is AP (Average Precision). Values were converted from
percentages in the text description to decimals in the table (e.g., 65.35% -> 0.6535). The table
explicitly lists AP values as decimals. Standard deviations are included where provided.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*