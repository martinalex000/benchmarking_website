# Extraction: arXiv:2502.09365
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: SPSE
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GraphViT | 0.7396 | 0.0033 | Yes | this paper | Table 1 |
| Exphormer | 0.7470 | 0.0013 | Yes | this paper | Table 1 |
| GPS + GPSE | 0.7231 | 0.0025 | Yes | this paper | Table 1 |
| GPS | 0.7210 | 0.0047 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.7211 | 0.0046 | No | this paper | Table 1 |
| CSA-RWSE | 0.7389 | 0.0035 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.7390 | 0.0052 | No | this paper | Table 1 |
| GRIT-RWSE | 0.7625 | 0.0095 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.7702 | 0.0043 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 1 |
| SAN (+RWSE) | 0.7669 | 0.0065 | Yes | this paper | Table 1 |
| EGT | 0.7923 | 0.0035 | Yes | this paper | Table 1 |
| Exphormer | 0.7807 | 0.0004 | Yes | this paper | Table 1 |
| GPS | 0.7797 | 0.0016 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.7844 | 0.0018 | No | this paper | Table 1 |
| CSA-RWSE | 0.7907 | 0.0012 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.7894 | 0.0013 | No | this paper | Table 1 |
| GRIT-RWSE | 0.7973 | 0.0019 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.7957 | 0.0012 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 1 |
| GraphViT | 0.9742 | 0.0011 | Yes | this paper | Table 1 |
| Exphormer | 0.9855 | 0.0004 | Yes | this paper | Table 1 |
| GPS + GPSE | 0.9808 | 0.0013 | Yes | this paper | Table 1 |
| GPS | 0.9806 | 0.0016 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.9810 | 0.0016 | No | this paper | Table 1 |
| CSA-RWSE | 0.9813 | 0.0012 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.9827 | 0.0008 | No | this paper | Table 1 |
| GRIT-RWSE | 0.9823 | 0.0020 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.9829 | 0.0015 | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | this paper | Table 1 |
| SAN (+RWSE) | 0.8658 | 0.0004 | Yes | this paper | Table 1 |
| EGT | 0.8682 | 0.0002 | Yes | this paper | Table 1 |
| Exphormer | 0.8674 | 0.0001 | Yes | this paper | Table 1 |
| GPS | 0.8669 | 0.0007 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.8683 | 0.0003 | Yes | this paper | Table 1 |
| CSA-RWSE | 0.8701 | 0.0006 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.8706 | 0.0005 | Yes | this paper | Table 1 |
| GRIT-RWSE | 0.8723 | 0.0006 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.8723 | 0.0004 | No | this paper | Table 1 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1379 | — | Yes | this paper | Table 1 |
| GIN | 0.1195 | — | Yes | this paper | Table 1 |
| Graphormer | 0.0864 | — | Yes | this paper | Table 1 |
| GPS | 0.0942 | — | Yes | this paper | Table 1 |
| GPS + SPSE | 0.0934 | — | No | this paper | Table 1 |
| CSA-RWSE | 0.0918 | — | Yes | this paper | Table 1 |
| CSA-SPSE | 0.0911 | — | No | this paper | Table 1 |
| GRIT-RWSE | 0.0838 | — | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.0831 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| SAN (+RWSE) | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GraphViT | 0.6970 | 0.0080 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| Drew | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| GPS + GPSE | 0.6688 | 0.0151 | Yes | this paper | Table 1 |
| GPS | 0.6601 | 0.0061 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.6608 | 0.0063 | No | this paper | Table 1 |
| CSA-RWSE | 0.6513 | 0.0061 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.6605 | 0.0096 | No | this paper | Table 1 |
| GRIT-RWSE | 0.6803 | 0.0085 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.6945 | 0.0113 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| SAN (+RWSE) | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GraphViT | 0.2475 | 0.0015 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| Drew | 0.2536 | 0.0015 | Yes | this paper | Table 1 |
| GPS + GPSE | 0.2464 | 0.0025 | Yes | this paper | Table 1 |
| GPS | 0.2509 | 0.0017 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.2506 | 0.0010 | No | this paper | Table 1 |
| CSA-RWSE | 0.2486 | 0.0012 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.2482 | 0.0019 | No | this paper | Table 1 |
| GRIT-RWSE | 0.2480 | 0.0025 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.2449 | 0.0018 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 1 |
| SAN (+RWSE) | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table 1 |
| EGT | 0.1080 | 0.0090 | Yes | this paper | Table 1 |
| GraphViT | 0.0730 | 0.0010 | Yes | this paper | Table 1 |
| GPS + GPSE | 0.0650 | 0.0030 | Yes | this paper | Table 1 |
| GPS | 0.0700 | 0.0030 | Yes | this paper | Table 1 |
| GPS + SPSE | 0.0680 | 0.0030 | No | this paper | Table 1 |
| CSA-RWSE | 0.0690 | 0.0030 | Yes | this paper | Table 1 |
| CSA-SPSE | 0.0610 | 0.0030 | No | this paper | Table 1 |
| GRIT-RWSE | 0.0650 | 0.0050 | Yes | this paper | Table 1 |
| GRIT-SPSE | 0.0590 | 0.0010 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **GIN**
- **GAT**
- **GatedGCN**
- **GIN-AK+**
- **SAN (+RWSE)**
- **Graphormer**
- **EGT**
- **GraphViT**
- **GPS + GPSE**
- **GPS** (from: rampavsek2022recipe)
- **CSA-RWSE**
- **GRIT-RWSE**
- **GINE**
- **Exphormer**
- **Drew**
- **GPS + SPSE**
- **CSA-SPSE**

## Extraction Notes

[ZINC] Extracted all models for ZINC dataset from Table 1. Proposed models are those explicitly
marked as '(ours)' or containing 'SPSE' in the context of the proposed method. [Peptides-func]
Extracted only Peptides-func results as requested. Models with '-' for this dataset were omitted.
[Peptides-struct] Extracted only Peptides-struct MAE results as requested. Proposed models include
GPS+SPSE, CSA-SPSE, and GRIT-SPSE. [PCQM4Mv2] Extracted only PCQM4Mv2 results as requested. Standard
deviation was not provided for this specific dataset in the table (only one run performed).
[PATTERN] Extracted only the PATTERN dataset column from Table 1. Normalized Accuracy values from
percentages to [0, 1] range. [CLUSTER] Extracted only the CLUSTER dataset column from Table 1.
Normalised Accuracy percentages by dividing by 100. [MNIST] Extracted all models for the MNIST
dataset from Table 1. Values were converted from percentages to decimals. [CIFAR10] Extracted only
CIFAR10 results from Table 1. Normalized percentages to [0, 1] range.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*