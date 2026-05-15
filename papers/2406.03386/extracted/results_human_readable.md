# Extraction: arXiv:2406.03386
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: NeuralWalker
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| CRaWL | 0.6901 | 0.0026 | Yes | this paper | Table 1 |
| NeuralWalker | 0.7690 | 0.0046 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | Xu 2019 | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | Veličković 2018 | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | Bresson 2017 | Table 1 |
| SAT | 0.7786 | 0.0010 | Yes | Chen 2022 | Table 1 |
| GPS | 0.7802 | 0.0018 | Yes | Rampásek 2022 | Table 1 |
| Exphormer | 0.7807 | 0.0004 | Yes | Shirzad 2023 | Table 1 |
| GRIT | 0.8003 | 0.0028 | Yes | Ma 2023 | Table 1 |
| NeuralWalker | 0.7819 | 0.0019 | No | this paper | Table 1 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1338 | 0.0007 | Yes | this paper | Table 1 |
| GIN | 0.2125 | 0.0009 | Yes | this paper | Table 1 |
| GatedGCN | 0.2922 | 0.0018 | Yes | this paper | Table 1 |
| GPS | 0.3412 | 0.0044 | Yes | this paper | Table 1 |
| Exphormer | 0.3455 | 0.0009 | Yes | this paper | Table 1 |
| NeuralWalker | 0.4398 | 0.0033 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | kipf2016semi | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | xu2019powerful | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | velivckovic2018graph | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | bresson2017residual | Table 1 |
| GPS | 0.9805 | 0.0013 | Yes | rampavsek2022recipe | Table 1 |
| Exphormer | 0.9855 | 0.0003 | Yes | shirzad2023exphormer | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | ma2023graph | Table 1 |
| CRaWL | 0.9794 | 0.0005 | Yes | tonshoff2023walking | Table 1 |
| NeuralWalker | 0.9869 | 0.0008 | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | kipf2016semi | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | xu2019powerful | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | velivckovic2018graph | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | bresson2017residual | Table 1 |
| SAT | 0.8685 | 0.0004 | Yes | chen2022structure | Table 1 |
| GPS | 0.8669 | 0.0006 | Yes | rampavsek2022recipe | Table 1 |
| Exphormer | 0.8670 | 0.0003 | Yes | shirzad2023exphormer | Table 1 |
| GRIT | 0.8720 | 0.0008 | Yes | ma2023graph | Table 1 |
| NeuralWalker | 0.8698 | 0.0001 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4526 | 0.0006 | Yes | this paper | Table 1 |
| GIN | 0.4617 | 0.0005 | Yes | this paper | Table 1 |
| GatedGCN | 0.4670 | 0.0004 | Yes | this paper | Table 1 |
| GPS | 0.4703 | 0.0014 | Yes | tonshoff2023did | Table 1 |
| NeuralWalker | 0.4707 | 0.0007 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | Yes | this paper | Table 1 |
| GIN | 0.2718 | 0.0054 | Yes | this paper | Table 1 |
| GatedGCN | 0.3880 | 0.0040 | Yes | this paper | Table 1 |
| GPS | 0.3748 | 0.0109 | Yes | this paper | Table 1 |
| Exphormer | 0.3975 | 0.0037 | Yes | this paper | Table 1 |
| NeuralWalker | 0.4912 | 0.0042 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6860 | 0.0050 | Yes | this paper | Table 1 |
| GIN | 0.6621 | 0.0067 | Yes | this paper | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| CRawL | 0.7074 | 0.0032 | Yes | Tonshoff 2023 | Table 1 |
| NeuralWalker | 0.7096 | 0.0078 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | Yes | this paper | Table 1 |
| GIN | 0.2473 | 0.0017 | Yes | this paper | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 1 |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| CRawL | 0.2506 | 0.0022 | Yes | this paper | Table 1 |
| NeuralWalker | 0.2463 | 0.0005 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | Kipf & Welling 2017 | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | Xu et al. 2019 | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | Veličković et al. 2018 | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | Bresson & Laurent 2017 | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | Ying et al. 2021 | Table 1 |
| SAT | 0.0890 | 0.0020 | Yes | Chen et al. 2022 | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | Rampásek et al. 2022 | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | Ma et al. 2023 | Table 1 |
| CRaWL | 0.0850 | 0.0040 | Yes | Tonshoff et al. 2023 | Table 1 |
| NeuralWalker | 0.0530 | 0.0020 | No | this paper | Table 1 |

### amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.5270 | 0.0062 | Yes | this paper | Table 1 |
| GPS | 0.5310 | 0.0042 | Yes | this paper | Table 1 |
| NAGphormer | 0.5126 | 0.0072 | Yes | this paper | Table 1 |
| Exphormer | 0.5351 | 0.0046 | Yes | this paper | Table 1 |
| Polynormer | 0.5481 | 0.0049 | Yes | this paper | Table 1 |
| NeuralWalker | 0.5458 | 0.0036 | No | this paper | Table 1 |

### minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.9391 | 0.0035 | Yes | this paper | Table 1 |
| GPS | 0.9063 | 0.0067 | Yes | this paper | Table 1 |
| NAGphormer | 0.8419 | 0.0066 | Yes | this paper | Table 1 |
| Exphormer | 0.9074 | 0.0053 | Yes | this paper | Table 1 |
| Polynormer | 0.9746 | 0.0036 | Yes | this paper | Table 1 |
| NeuralWalker | 0.9782 | 0.0040 | No | this paper | Table 1 |

### ogbg-code2 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1595 | 0.0018 | Yes | this paper | Table 1 |
| GIN | 0.1581 | 0.0026 | Yes | this paper | Table 1 |
| GraphTrans | 0.1830 | 0.0024 | Yes | this paper | Table 1 |
| SAT | 0.1937 | 0.0028 | Yes | this paper | Table 1 |
| GPS | 0.1894 | 0.0024 | Yes | this paper | Table 1 |
| NeuralWalker | 0.1957 | 0.0025 | No | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2424 | 0.0034 | Yes | this paper | Table 1 |
| GIN | 0.2703 | 0.0023 | Yes | this paper | Table 1 |
| GraphTrans | 0.2761 | 0.0029 | Yes | this paper | Table 1 |
| GPS | 0.2907 | 0.0028 | Yes | this paper | Table 1 |
| CRaWL | 0.2986 | 0.0025 | Yes | this paper | Table 1 |
| NeuralWalker | 0.3086 | 0.0031 | No | this paper | Table 1 |

### ogbg-ppa — ACC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6857 | 0.0061 | Yes | this paper | Table 1 |
| GIN | 0.7037 | 0.0107 | Yes | this paper | Table 1 |
| SAT | 0.7522 | 0.0056 | Yes | this paper | Table 1 |
| GPS | 0.8015 | 0.0033 | Yes | this paper | Table 1 |
| NeuralWalker | 0.7888 | 0.0059 | No | this paper | Table 1 |

### pokec — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7545 | 0.0017 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.7223 | 0.0018 | Yes | this paper | Table 1 |
| NAGphormer | 0.7659 | 0.0025 | Yes | this paper | Table 1 |
| Polynormer | 0.8610 | 0.0005 | Yes | this paper | Table 1 |
| NeuralWalker | 0.8646 | 0.0009 | No | this paper | Table 1 |

### questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7609 | 0.0127 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.7679 | 0.0071 | Yes | this paper | Table 1 |
| GPS | 0.7173 | 0.0147 | Yes | this paper | Table 1 |
| NAGphormer | 0.6817 | 0.0153 | Yes | this paper | Table 1 |
| Exphormer | 0.7394 | 0.0106 | Yes | this paper | Table 1 |
| Polynormer | 0.7892 | 0.0089 | Yes | this paper | Table 1 |
| NeuralWalker | 0.7852 | 0.0113 | No | this paper | Table 1 |

### roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.8875 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.8200 | 0.0061 | Yes | this paper | Table 1 |
| NAGphormer | 0.7434 | 0.0077 | Yes | this paper | Table 1 |
| Exphormer | 0.8903 | 0.0037 | Yes | this paper | Table 1 |
| Polynormer | 0.9255 | 0.0037 | Yes | this paper | Table 1 |
| NeuralWalker | 0.9292 | 0.0036 | No | this paper | Table 1 |

### tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 1 |
| GAT(-sep) | 0.8378 | 0.0043 | Yes | this paper | Table 1 |
| GPS | 0.8371 | 0.0048 | Yes | this paper | Table 1 |
| NAGphormer | 0.7832 | 0.0095 | Yes | this paper | Table 1 |
| Exphormer | 0.8377 | 0.0078 | Yes | this paper | Table 1 |
| Polynormer | 0.8591 | 0.0074 | Yes | this paper | Table 1 |
| NeuralWalker | 0.8556 | 0.0074 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: kipf2016semi)
- **GIN** (from: xu2019powerful)
- **GAT** (from: velivckovic2018graph)
- **GatedGCN** (from: bresson2017residual)
- **Graphormer** (from: ying2021transformers)
- **SAT** (from: chen2022structure)
- **GPS** (from: rampavsek2022recipe)
- **Exphormer** (from: shirzad2023exphormer)
- **GRIT** (from: ma2023graph)
- **CRaWL** (from: tonshoff2023walking)
- **GraphTrans** (from: You et al. 2020)
- **GAT(-sep)** (from: Veličković et al. 2018)
- **NAGphormer** (from: Beaini et al. 2022)
- **Polynormer** (from: Bouritsas et al. 2023)

## Extraction Notes

[ZINC] Extracted only ZINC results from Table 1. NeuralWalker uses a pretraining strategy (indicated
by star symbol in table), so uses_external_data is set to true. All other models are standard
baselines without external pretraining mentioned for this specific benchmark context. Values are
normalized to [0,1] range where applicable (MAE is not normalized but is small here). Standard
deviation parsed from 'mean ± std' format. [MNIST] Extracted only MNIST results as requested. The
table reports Accuracy (ACC) for MNIST. Values were converted from percentages to [0,1] range.
NeuralWalker uses a pretraining strategy (indicated by star), so uses_external_data is set to true.
All other models are standard GNNs without external pretraining mentioned for this specific
benchmark context. [CIFAR10] Extracted only CIFAR10 results from Table 1. Values were converted from
percentages to [0,1] range. Standard deviations were parsed from 'mean ± std' format. Graphormer and
SAT did not report CIFAR10 results, so they are excluded from the results list for this dataset.
[PATTERN] Extracted only PATTERN dataset results as requested. Values are percentages from the
table, converted to [0,1] range. NeuralWalker uses pretraining strategy (indicated by star), so
uses_external_data is true. All other models are standard benchmarks without external pretraining
mentioned for this specific task context. [CLUSTER] Extracted only the CLUSTER dataset results from
Table 1. The metric is Accuracy (ACC). Values were converted from percentages to [0,1] range.
Standard deviations were parsed from the 'mean ± std' format. All rows for CLUSTER were included.
[PascalVOC-SP] Extracted only test-set results for PascalVOC-SP from Table 1. Excluded ablation
tables (Table 2 and Appendix Table) as they report validation performance, not test performance.
Note: GRIT and CRawL do not have results reported for PascalVOC-SP in Table 1, so they are excluded
from the results list for this specific dataset. [COCO-SP] Extracted only COCO-SP results as
requested. All values are F1 scores. Baselines GRIT and CRawL do not have results for COCO-SP in the
table, so they are excluded from the results list for this specific dataset. [Peptides-func]
Extracted only the 'Peptides-func' column from Table 1 as requested. The metric is AP (Average
Precision), which is higher-is-better. All values were normalized to [0,1] range (they were already
in that format). Standard deviations were parsed from the 'mean ± std' format. Note that there are
two entries for GPS; both are included as they represent different configurations/citations in the
table. [Peptides-struct] Extracted only Peptides-struct MAE results from Table 1. Note that GCN and
GRIT share the same best baseline value (0.2460), but GCN is bolded in the table, indicating it is
the specific best baseline referenced by the caption. NeuralWalker (0.2463) is slightly worse than
GCN/GRIT in this specific metric, despite the caption claiming improvement (likely referring to
other metrics or a different comparison context, but we extract the raw numbers as presented).
[PCQM-Contact] Extracted only PCQM-Contact results as requested. Note that GPS, Exphormer, GRIT, and
CRawL have '--' for PCQM-Contact, indicating no results were reported for this dataset in the table.
The metric is MRR (Mean Reciprocal Rank), which is higher-is-better. Values are normalized to [0,1]
range. [ogbg-molpcba] Extracted only the 'ogbg-molpcba' dataset results from Table 1. The metric is
AP (Average Precision), which is higher-is-better. SAT and CRaWL do not report results for this
dataset in the table, so they are excluded from the results list for this specific dataset. All
values are normalized to [0,1] range as they are AP scores. [ogbg-ppa] Extracted only the 'ogbg-ppa'
dataset results as requested. GraphTrans and CRaWL have '--' for ogbg-ppa, so they are excluded. All
other models have reported ACC values with standard deviations. The metric is Accuracy (ACC), higher
is better. Values are normalized to [0,1]. [ogbg-code2] Extracted only the 'ogbg-code2' column from
Table 1 as requested. The metric is F1. All values are normalized to [0,1]. Standard deviations are
included. NeuralWalker is identified as the proposed model based on the bolding of its result and
the context of the paper. [roman-empire] Extracted only the 'roman-empire' column from Table 1. The
metric reported in the table header is 'ACC', which corresponds to Accuracy. Values were converted
from percentages to [0,1] range. Standard deviations were parsed from the 'mean ± std' format.
[amazon-ratings] Extracted only the 'amazon-ratings' column from Table 1. The metric reported in the
table header is 'ACC', which corresponds to Accuracy. Values were divided by 100 to normalize to
[0,1] range. Standard deviations were parsed from the 'mean ± std' format. [minesweeper] Extracted
only the 'minesweeper' column from Table 1. The metric is ROC AUC. Values were converted from
percentages (e.g., 89.75) to decimals (0.8975) as per standard ROC-AUC reporting conventions in the
schema instructions, although the table header says 'ROC AUC' and values are >1, implying
percentage. The schema rule states 'Accuracy, F1, AP, AUC, ROC-AUC... are always in the range [0,
1]'. Therefore, 89.75 becomes 0.8975. [tolokers] Extracted only the 'tolokers' column from Table 1.
The metric for this dataset is ROC AUC. Values were converted from percentages (e.g., 83.64) to
decimals (0.8364) as per standard ROC-AUC reporting conventions in the schema rules. All models
listed in the table were included. [questions] Extracted only the 'questions' dataset column from
Table 1. The metric for 'questions' is ROC AUC. Values were converted from percentages (e.g., 76.09)
to decimals (0.7609) as per standard ROC-AUC reporting conventions in the schema instructions,
although the table header says 'ROC AUC' and values are >1, implying percentage. The schema rule
states 'Accuracy, F1, AP, AUC, ROC-AUC... are always in the range [0, 1]'. Therefore, 76.09 becomes
0.7609. [pokec] Extracted only the 'pokec' column from Table 1. GPS and Exphormer are marked as
'OOM' (Out of Memory) and thus excluded as no numerical result is provided. All other models have
valid Accuracy values with standard deviations. Values were converted from percentages to [0,1]
range.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*