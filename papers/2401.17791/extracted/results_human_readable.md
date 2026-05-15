# Extraction: arXiv:2401.17791
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Eigenformer (0.5M params)
- Type: GraphTransformer

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
| CRaW1 | 0.6901 | 0.0026 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| EXPHORMER | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| Eigenformer | 0.6732 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.7019 | — | No | this paper | Table 1 |

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
| GRIT | 0.8003 | 0.0028 | Yes | this paper | Table 1 |
| EXPHORMER | 0.7807 | 0.0004 | Yes | this paper | Table 1 |
| Eigenformer | 0.7726 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.7746 | — | No | this paper | Table 1 |

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
| GPS | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| EXPHORMER | 0.9855 | 0.0004 | Yes | this paper | Table 1 |
| Eigenformer | 0.9714 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.9836 | — | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| DGN | 0.8668 | 0.0003 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | this paper | Table 1 |
| SAN | 0.8658 | 0.0004 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.8685 | 0.0004 | Yes | this paper | Table 1 |
| EGT | 0.8682 | 0.0002 | Yes | this paper | Table 1 |
| GPS | 0.8669 | 0.0006 | Yes | this paper | Table 1 |
| GRIT | 0.8720 | 0.0008 | Yes | this paper | Table 1 |
| EXPHORMER | 0.8674 | 0.0001 | Yes | this paper | Table 1 |
| Eigenformer | 0.8668 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.8674 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0035 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| EXPHORMER | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| Eigenformer | 0.6414 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.6317 | — | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GPS | 0.2500 | 0.0012 | Yes | this paper | Table 1 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| EXPHORMER | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| Eigenformer | 0.2599 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.2687 | — | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| GatedGCN-LSPE | 0.0900 | 0.0010 | Yes | this paper | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table 1 |
| DGN | 0.1680 | 0.0030 | Yes | this paper | Table 1 |
| GSN | 0.1010 | 0.0100 | Yes | this paper | Table 1 |
| CIN | 0.0790 | 0.0060 | Yes | this paper | Table 1 |
| CRaW1 | 0.0850 | 0.0040 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.0940 | 0.0080 | Yes | this paper | Table 1 |
| EGT | 0.1080 | 0.0090 | Yes | this paper | Table 1 |
| Graphormer-URPE | 0.0860 | 0.0070 | Yes | this paper | Table 1 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | this paper | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | this paper | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| Eigenformer | 0.0770 | — | No | this paper | Table 1 |
| Eigenformer (feat.) | 0.0890 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling)
- **GIN** (from: Xu et al.)
- **GAT** (from: Veličković et al.)
- **GatedGCN** (from: Bresson & Laurent)
- **GatedGCN-LSPE** (from: Bresson & Laurent)
- **PNA** (from: Corso et al.)
- **DGN** (from: Bouritsas et al.)
- **GSN** (from: Maron et al.)
- **CIN** (from: Maron et al.)
- **CRaW1** (from: Bouritsas et al.)
- **GIN-AK+** (from: Xu et al.)
- **SAN** (from: Ying et al.)
- **Graphormer** (from: Bian et al.)
- **K-Subgraph SAT** (from: Cun et al.)
- **EGT** (from: Chen et al.)
- **Graphormer-URPE** (from: Bian et al.)
- **Graphormer-GD** (from: Bian et al.)
- **GPS** (from: Fey et al.)
- **GRIT** (from: Chen et al.)
- **EXPHORMER** (from: Chen et al.)
- **GINE** (from: Xu et al.)
- **GatedGCN+RWSE** (from: LRGB)
- **Transformer+LapPE** (from: LRGB)
- **SAN+LapPE** (from: Ying et al.)
- **SAN+RWSE** (from: Ying et al.)

## Extraction Notes

[ZINC] Extracted only ZINC results from Table 1. The table caption indicates results are from a
single training run for Eigenformer, while baselines report mean +/- std of 4 runs. Eigenformer
values do not have standard deviations reported in the table, so std is null. The 'Eigenformer
(feat.)' row is treated as a variant of the proposed model. All other rows are baselines. [MNIST]
Extracted only MNIST results as requested. Note that Eigenformer results are reported as single runs
without standard deviation, while baselines report mean +/- std. The values for Eigenformer are
taken directly from the table. The 'Eigenformer (feat.)' variant is also included as it is a
distinct row in the table. [CIFAR10] Extracted only CIFAR10 results from Table 1. Note that
Eigenformer results are single runs without standard deviation reported in the table, while
baselines report mean +/- std. The proposed model name is 'Eigenformer' and its variant 'Eigenformer
(feat.)'. All values converted from percentages to [0,1] range. [PATTERN] Extracted only PATTERN
dataset results from Table 1. Note that the table header says 'Wt. Acc.' (Weighted Accuracy) for
PATTERN, but the prompt requested 'Accuracy'. In the context of the Benchmarking GNNs paper, PATTERN
is a graph classification task where 'Accuracy' is the standard metric reported in the main text and
often used interchangeably with Weighted Accuracy in summary tables if classes are imbalanced.
However, looking at the values (e.g., 87.196 for GRIT), these are clearly percentages. The prompt
asks to normalize Accuracy to [0,1]. The values in the table are like 87.196, which implies 87.196%.
I have divided by 100. The metric name in the table is 'Wt. Acc.', but the prompt asks to focus on
'Accuracy'. Given the ambiguity, I will use 'Accuracy' as the metric name as per the prompt's focus
instruction, assuming Wt. Acc. is the specific implementation of accuracy for this dataset in this
benchmark. The values are normalized to [0,1]. Standard deviations are extracted where available.
Eigenformer results are single runs, so std is null. [CLUSTER] Extracted only CLUSTER dataset
results as requested. The table reports Accuracy for CLUSTER. Eigenformer results are single runs
(no std reported), while baselines report mean +/- std. Values are normalized to [0,1] range.
[Peptides-func] Extracted only Peptides-func AP results as requested. Note that Eigenformer results
are single runs (no std reported) while baselines report mean +/- std of 4 runs. The 'Eigenformer
(feat.)' variant is included as it is a distinct row in the table for the same dataset/metric.
[Peptides-struct] Extracted all rows from Table 1 for the 'Peptides-struct' dataset. The table
caption notes that Eigenformer results are from a single run, hence std is null. Baselines report
mean +/- std of 4 runs. Values are normalized to [0,1] range where applicable (MAE is not normalized
but is < 1 here). Metric is MAE, lower is better.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*