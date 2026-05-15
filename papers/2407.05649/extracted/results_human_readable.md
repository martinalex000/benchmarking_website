# Extraction: arXiv:2407.05649
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: GRASS (0.5M params)
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| DGN | 0.7284 | 0.0042 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| NeuralWalker | 0.8003 | 0.0019 | Yes | this paper | Table 1 |
| GRASS (ours) | 0.8375 | 0.0014 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 1 |
| SAN | 0.7669 | 0.0065 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.7786 | 0.0010 | Yes | this paper | Table 1 |
| EGT | 0.7923 | 0.0035 | Yes | this paper | Table 1 |
| GPS | 0.7802 | 0.0018 | Yes | this paper | Table 1 |
| Exphormer | 0.7807 | 0.0004 | Yes | this paper | Table 1 |
| GRIT | 0.8003 | 0.0028 | Yes | this paper | Table 1 |
| NeuralWalker | 0.7819 | 0.0019 | Yes | this paper | Table 1 |
| GRASS (ours) | 0.7954 | 0.0017 | No | this paper | Table 1 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1338 | 0.0007 | Yes | Gutteridge et al. 2023; Tonshoff et al. 2023 | Table 2 |
| GINE | 0.2125 | 0.0009 | Yes | Gutteridge et al. 2023; Tonshoff et al. 2023 | Table 2 |
| GatedGCN | 0.2922 | 0.0018 | Yes | Gutteridge et al. 2023; Tonshoff et al. 2023 | Table 2 |
| Transformer+LapPE | 0.2618 | 0.0031 | Yes | Gutteridge et al. 2023 | Table 2 |
| SAN+LapPE | 0.2592 | 0.0158 | Yes | Gutteridge et al. 2023 | Table 2 |
| GPS+LapPE | 0.3884 | 0.0055 | Yes | Tonshoff et al. 2023 | Table 2 |
| Exphormer | 0.3455 | 0.0009 | Yes | Shirzad et al. 2023 | Table 2 |
| NeuralWalker | 0.4398 | 0.0033 | Yes | Chen et al. 2024 | Table 2 |
| GRASS | 0.4752 | 0.0032 | No | this paper | Table 2 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| PNA | 0.9794 | 0.0012 | Yes | this paper | Table 1 |
| CRaW1 | 0.9794 | 0.0005 | Yes | this paper | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 1 |
| Exphormer | 0.9855 | 0.0004 | Yes | this paper | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | ma2023graph | Table 1 |
| NeuralWalker | 0.9876 | 0.0008 | Yes | this paper | Table 1 |
| GRASS (ours) | 0.9893 | 0.0008 | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| DGN | 0.8668 | 0.0003 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.8685 | 0.0004 | Yes | this paper | Table 1 |
| EGT | 0.8682 | 0.0002 | Yes | this paper | Table 1 |
| GPS | 0.8669 | 0.0006 | Yes | this paper | Table 1 |
| Exphormer | 0.8674 | 0.0001 | Yes | this paper | Table 1 |
| GRIT | 0.8720 | 0.0008 | Yes | this paper | Table 1 |
| NeuralWalker | 0.8698 | 0.0001 | Yes | this paper | Table 1 |
| GRASS (ours) | 0.8918 | 0.0031 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | Yes | tonshoff2023did | Table 1 |
| GINE | 0.2718 | 0.0054 | Yes | tonshoff2023did | Table 1 |
| GatedGCN | 0.3880 | 0.0040 | Yes | tonshoff2023did | Table 1 |
| DIGL+MPNN | 0.2824 | 0.0039 | Yes | gutteridge2023drew | Table 1 |
| DIGL+MPNN+LapPE | 0.2921 | 0.0038 | Yes | gutteridge2023drew | Table 1 |
| MixHop-GCN | 0.2506 | 0.0133 | Yes | gutteridge2023drew | Table 1 |
| MixHop-GCN+LapPE | 0.2218 | 0.0174 | Yes | gutteridge2023drew | Table 1 |
| DRew-GCN | 0.1848 | 0.0107 | Yes | tonshoff2023did | Table 1 |
| DRew-GCN+LapPE | 0.1851 | 0.0092 | Yes | tonshoff2023did | Table 1 |
| DRew-GIN | 0.2719 | 0.0043 | Yes | tonshoff2023did | Table 1 |
| DRew-GIN+LapPE | 0.2692 | 0.0059 | Yes | tonshoff2023did | Table 1 |
| DRew-GatedGCN | 0.3214 | 0.0021 | Yes | tonshoff2023did | Table 1 |
| DRew-GatedGCN+LapPE | 0.3314 | 0.0024 | Yes | tonshoff2023did | Table 1 |
| Transformer+LapPE | 0.2694 | 0.0098 | Yes | ma2023graph | Table 1 |
| SAN+LapPE | 0.3230 | 0.0039 | Yes | ma2023graph | Table 1 |
| GPS+LapPE | 0.4440 | 0.0065 | Yes | tonshoff2023did | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | shirzad2023exphormer | Table 1 |
| NeuralWalker | 0.4912 | 0.0042 | Yes | chen2024learning | Table 1 |
| GRASS | 0.5670 | 0.0049 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN* | 0.6860 | 0.0050 | Yes | Gutteridge et al. 2023 | Table 1 |
| GINE* | 0.6621 | 0.0067 | Yes | Gutteridge et al. 2023 | Table 1 |
| GatedGCN* | 0.6765 | 0.0047 | Yes | Gutteridge et al. 2023 | Table 1 |
| DIGL+MPNN | 0.6469 | 0.0019 | Yes | Gutteridge et al. 2023 | Table 1 |
| DIGL+MPNN+LapPE | 0.6830 | 0.0026 | Yes | Gutteridge et al. 2023 | Table 1 |
| MixHop-GCN | 0.6592 | 0.0036 | Yes | Gutteridge et al. 2023 | Table 1 |
| MixHop-GCN+LapPE | 0.6843 | 0.0049 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GCN | 0.6996 | 0.0076 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GCN+LapPE | 0.7150 | 0.0044 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GIN | 0.6940 | 0.0074 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GIN+LapPE | 0.7126 | 0.0045 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GatedGCN | 0.6733 | 0.0094 | Yes | Gutteridge et al. 2023 | Table 1 |
| DRew-GatedGCN+LapPE | 0.6977 | 0.0026 | Yes | Gutteridge et al. 2023 | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | Gutteridge et al. 2023 | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | Gutteridge et al. 2023 | Table 1 |
| GPS+LapPE* | 0.6534 | 0.0091 | Yes | Tonshoff et al. 2023 | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | Shirzad et al. 2023 | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | Ma et al. 2023 | Table 1 |
| NeuralWalker | 0.7096 | 0.0078 | Yes | Chen et al. 2024 | Table 1 |
| GRASS (ours) | 0.6737 | 0.0064 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN* | 0.2460 | 0.0007 | Yes | Gutteridge et al. 2023 | Table 2 |
| GINE* | 0.2473 | 0.0017 | Yes | Gutteridge et al. 2023 | Table 2 |
| GatedGCN* | 0.2477 | 0.0009 | Yes | Gutteridge et al. 2023 | Table 2 |
| DIGL+MPNN | 0.3173 | 0.0007 | Yes | Gutteridge et al. 2023 | Table 2 |
| DIGL+MPNN+LapPE | 0.2616 | 0.0018 | Yes | Gutteridge et al. 2023 | Table 2 |
| MixHop-GCN | 0.2921 | 0.0023 | Yes | Gutteridge et al. 2023 | Table 2 |
| MixHop-GCN+LapPE | 0.2614 | 0.0023 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GCN | 0.2781 | 0.0028 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GCN+LapPE | 0.2536 | 0.0015 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GIN | 0.2799 | 0.0016 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GIN+LapPE | 0.2606 | 0.0014 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GatedGCN | 0.2699 | 0.0018 | Yes | Gutteridge et al. 2023 | Table 2 |
| DRew-GatedGCN+LapPE | 0.2539 | 0.0007 | Yes | Gutteridge et al. 2023 | Table 2 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | Tonshoff et al. 2023 | Table 2 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | Tonshoff et al. 2023 | Table 2 |
| GPS+LapPE* | 0.2509 | 0.0014 | Yes | Tonshoff et al. 2023 | Table 2 |
| Exphormer | 0.2481 | 0.0007 | Yes | Shirzad et al. 2023 | Table 2 |
| GRIT | 0.2460 | 0.0012 | Yes | Ma et al. 2023 | Table 2 |
| NeuralWalker | 0.2463 | 0.0005 | Yes | Chen et al. 2024 | Table 2 |
| GRASS (ours) | 0.2459 | 0.0007 | No | this paper | Table 2 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| GatedGCN-LSPE | 0.0900 | 0.0010 | Yes | ma2023graph | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | ma2023graph | Table 1 |
| DGN | 0.1680 | 0.0030 | Yes | ma2023graph | Table 1 |
| GSN | 0.1010 | 0.0100 | Yes | ma2023graph | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | ma2023graph | Table 1 |
| CRaW1 | 0.0850 | 0.0040 | Yes | ma2023graph | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | ma2023graph | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | ma2023graph | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | ma2023graph | Table 1 |
| K-Subgraph SAT | 0.0940 | 0.0080 | Yes | ma2023graph | Table 1 |
| EGT | 0.1080 | 0.0090 | Yes | ma2023graph | Table 1 |
| Graphormer-URPE | 0.0860 | 0.0070 | Yes | ma2023graph | Table 1 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | ma2023graph | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | ma2023graph | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | ma2023graph | Table 1 |
| NeuralWalker | 0.0650 | 0.0010 | Yes | ma2023graph | Table 1 |
| GRASS | 0.0470 | 0.0010 | No | this paper | Table 1 |

### roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 2 |
| GAT (-sep) | 0.8875 | 0.0041 | Yes | this paper | Table 2 |
| GPS | 0.8200 | 0.0061 | Yes | this paper | Table 2 |
| NAGphormer | 0.7434 | 0.0077 | Yes | this paper | Table 2 |
| Exphormer | 0.8903 | 0.0037 | Yes | this paper | Table 2 |
| Polynormer | 0.9255 | 0.0037 | Yes | this paper | Table 2 |
| NeuralWalker | 0.9292 | 0.0036 | Yes | this paper | Table 2 |
| GRASS (ours) | 0.9134 | 0.0022 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling)
- **GIN** (from: Xu et al.)
- **GAT** (from: Velickovic et al.)
- **GatedGCN** (from: Bresson et al.)
- **GatedGCN-LSPE** (from: ma2023graph)
- **PNA** (from: Corso et al.)
- **DGN** (from: ma2023graph)
- **GSN** (from: ma2023graph)
- **CIN** (from: ma2023graph)
- **CRaW1** (from: ma2023graph)
- **GIN-AK+** (from: ma2023graph)
- **SAN** (from: Ying et al.)
- **Graphormer** (from: You et al.)
- **K-Subgraph SAT** (from: ma2023graph)
- **EGT** (from: ma2023graph)
- **Graphormer-URPE** (from: ma2023graph)
- **Graphormer-GD** (from: ma2023graph)
- **GPS** (from: dwivedi2022long)
- **Exphormer** (from: shirzad2023exphormer)
- **GRIT** (from: ma2023graph)
- **NeuralWalker** (from: ma2023graph)
- **GCN*** (from: Gutteridge et al. 2023 (adapted))
- **GINE*** (from: Gutteridge et al. 2023 (adapted))
- **GatedGCN*** (from: Gutteridge et al. 2023 (adapted))
- **DIGL+MPNN** (from: Gutteridge et al. 2023 (adapted))
- **DIGL+MPNN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **MixHop-GCN** (from: Gutteridge et al. 2023 (adapted))
- **MixHop-GCN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GCN** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GCN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GIN** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GIN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GatedGCN** (from: Gutteridge et al. 2023 (adapted))
- **DRew-GatedGCN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **Transformer+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **SAN+LapPE** (from: Gutteridge et al. 2023 (adapted))
- **GPS+LapPE*** (from: Tonshoff et al. 2023 (adapted))
- **GINE** (from: re-tuned by tonshoff2023did)
- **GPS+LapPE** (from: re-tuned by tonshoff2023did)
- **GAT (-sep)**
- **NAGphormer**
- **Polynormer**

## Extraction Notes

[ZINC] Extracted only the main benchmark results for ZINC from Table 1. Excluded ablation tables
(Table 2 and Table 3) as they represent variations/variants of the proposed model rather than
standard baseline comparisons. Note: Exphormer has a dash '-' for ZINC MAE in Table 1, so it was
excluded from results as no value was reported. [MNIST] Extracted only MNIST results as requested.
All values were converted from percentages to [0,1] range. Standard deviations were parsed from the
'mean ± s.d.' format. The table caption indicates that performance numbers other than GRASS are
adapted from other papers, but the table itself contains the values, so they are included with
appropriate source_ref. [CIFAR10] Extracted only CIFAR10 results from Table 1. All values were
percentages in the table, so they were divided by 100 to fit the [0,1] range for Accuracy. Standard
deviations were parsed from the 'mean ± std' format. The proposed model is GRASS. [CLUSTER]
Extracted all rows for the CLUSTER dataset from Table 1. Values were converted from percentages to
[0,1] range. Standard deviations were parsed from the 'mean ± s.d.' format. The proposed model is
GRASS. [PATTERN] Extracted only PATTERN dataset results from Table 1. All values are Accuracy
(higher is better). Standard deviations were parsed from the 'mean ± s.d.' format. Values were
divided by 100 to normalize percentages to [0,1] range. Baseline models are adapted from cited
papers as noted in the table caption. [Peptides-func] Extracted all rows from Table 1 for the
Peptides-func dataset. The metric is AP (Average Precision). All values are normalized to [0,1].
Standard deviations are included where reported. Baseline models are adapted from other papers as
noted in the table caption. [Peptides-struct] Extracted only Peptides-struct MAE results from Table
2. All values are normalized to [0,1] range where applicable (MAE is not percentage-based but small
values < 1). Standard deviations are parsed from 'mean ± std' format. Baseline sources inferred from
table caption citations. [PascalVOC-SP] Extracted only PascalVOC-SP results from Table 1 (LRGB
datasets). Excluded ablation tables (Table 2 and Table 3) as they represent variants/ablations
rather than the standard benchmark comparison against baselines. All values are Macro F1 scores
normalized to [0,1]. Standard deviations are included where reported. [COCO-SP] Extracted only COCO-
SP results as requested. The table caption indicates results are mean ± s.d. of 8 runs. All other
datasets (Peptides-func, Peptides-struct, PascalVOC-SP) were ignored. Baseline models for COCO-SP
are limited to those explicitly listed in the table with values for that column. [roman-empire]
Extracted results from Table 2 (labeled table:results_roman_empire in text). All values were
percentages in the table (e.g., 73.69) and were divided by 100 to fit the [0,1] range for Accuracy.
The table caption indicates these are mean ± s.d. of 8 runs. No other datasets were included as per
instructions.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*