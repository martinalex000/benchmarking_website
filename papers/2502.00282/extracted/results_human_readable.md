# Extraction: arXiv:2502.00282
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: GraphMinNet
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| GraphGPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| Grit | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| GRED | 0.7685 | 0.0019 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.7370 | 0.0034 | Yes | this paper | Table 1 |
| GSSC | 0.7764 | 0.0046 | Yes | this paper | Table 1 |
| Ours | 0.7807 | 0.0078 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 1 |
| SAN | 0.7669 | 0.0065 | Yes | this paper | Table 1 |
| GraphGPS | 0.7802 | 0.0018 | Yes | this paper | Table 1 |
| Exphormer | 0.7807 | 0.0004 | Yes | this paper | Table 1 |
| Grit | 0.8003 | 0.0028 | Yes | this paper | Table 1 |
| GRED | 0.7850 | 0.0010 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.7680 | 0.0036 | Yes | this paper | Table 1 |
| GSSC | 0.7916 | 0.0015 | Yes | this paper | Table 1 |
| Ours | 0.7928 | 0.0012 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| GraphGPS | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| Exphormer | 0.9855 | 0.0004 | Yes | this paper | Table 1 |
| Grit | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| GRED | 0.9838 | 0.0001 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.9842 | 0.0008 | Yes | this paper | Table 1 |
| GSSC | 0.9849 | 0.0005 | Yes | this paper | Table 1 |
| Ours | 0.9860 | 0.0014 | No | this paper | Table 1 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8100 | — | Yes | this paper | Table 1 |
| GIN | 0.8898 | 0.0056 | Yes | this paper | Table 1 |
| GAT | 0.9210 | 0.0024 | Yes | this paper | Table 1 |
| GraphGPS | 0.9350 | 0.0041 | Yes | this paper | Table 1 |
| Exphormer | 0.9402 | 0.0021 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.9340 | 0.0027 | Yes | this paper | Table 1 |
| GSSC | 0.9406 | 0.0064 | Yes | this paper | Table 1 |
| Ours | 0.9372 | 0.0029 | No | this paper | Table 1 |

### Molhiv — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7599 | 0.0119 | Yes | this paper | Table 1 |
| GIN | 0.7707 | 0.0149 | Yes | this paper | Table 1 |
| SAN | 0.7785 | 0.0247 | Yes | this paper | Table 1 |
| GraphGPS | 0.7880 | 0.0101 | Yes | this paper | Table 1 |
| Exphormer | 0.7879 | 0.0131 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.7823 | 0.0121 | Yes | this paper | Table 1 |
| GSSC | 0.8035 | 0.0142 | Yes | this paper | Table 1 |
| Ours | 0.8086 | 0.0056 | No | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| SAN | 0.8658 | 0.0004 | Yes | this paper | Table 1 |
| GraphGPS | 0.8669 | 0.0006 | Yes | this paper | Table 1 |
| Exphormer | 0.8674 | 0.0001 | Yes | this paper | Table 1 |
| Grit | 0.8720 | 0.0008 | Yes | this paper | Table 1 |
| GRED | 0.8676 | 0.0002 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.8671 | 0.0005 | Yes | this paper | Table 1 |
| GSSC | 0.8751 | 0.0008 | Yes | this paper | Table 1 |
| Ours | 0.8755 | 0.0012 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GIN | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| SAN | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| GraphGPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| Grit | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| GRED | 0.2455 | 0.0013 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.2478 | 0.0016 | Yes | this paper | Table 1 |
| GSSC | 0.2459 | 0.0020 | Yes | this paper | Table 1 |
| Ours | 0.2438 | 0.0014 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| GraphGPS | 0.0700 | 0.0040 | Yes | this paper | Table 1 |
| Exphormer | 0.1110 | 0.0070 | Yes | this paper | Table 1 |
| Grit | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| GRED | 0.0770 | 0.0020 | Yes | this paper | Table 1 |
| Graph-Mamba | 0.0670 | 0.0020 | Yes | this paper | Table 1 |
| GSSC | 0.0640 | 0.0020 | Yes | this paper | Table 1 |
| Ours | 0.0630 | 0.0010 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **GIN**
- **GAT**
- **GatedGCN**
- **SAN**
- **GraphGPS**
- **Exphormer**
- **Grit**
- **GRED**
- **Graph-Mamba**
- **GSSC** (from: huang2024can)

## Extraction Notes

[MNIST] Extracted only MNIST results as requested. Normalized percentages to [0, 1] range. Proposed
model identified as GraphMinNet from text. [CIFAR10] Extracted only CIFAR10 results as requested.
Model 'Ours' is identified as GraphMinNet from the text. Accuracy values were divided by 100 to
normalize to [0, 1]. [PATTERN] Extracted only the PATTERN dataset as requested. Normalized accuracy
percentages to [0, 1] range. Proposed model identified as GraphMinNet from text. [CLUSTER] Extracted
only the CLUSTER dataset results from Table 1. Ablation tables were skipped as they represent
variants/configurations of the proposed model rather than the standard benchmark results. [Molhiv]
Extracted only Molhiv results from Table 1. Ablation tables were skipped as per instructions to
focus on the standard/default configuration. Model name 'Ours' mapped to 'GraphMinNet' based on
text. [PascalVOC-SP] failed: 3 validation errors for ExtractionOutput results.2.value   Input should
be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] failed: 1 validation error for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-struct] Extracted only Peptides-struct
results as requested. GAT had no reported value for this dataset. [ZINC] Extracted only ZINC dataset
results as requested. GatedGCN had no value for ZINC in the table. [MalNet-Tiny] Extracted only
MalNet-Tiny results as requested. Normalized percentages to [0, 1]. Models with no value for MalNet-
Tiny (GatedGCN, SAN, Grit, GRED) were omitted from the results list.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*