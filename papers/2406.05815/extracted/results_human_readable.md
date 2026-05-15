# Extraction: arXiv:2406.05815
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GSSC
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 2 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 2 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 2 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 2 |
| GraphGPS | 0.7230 | 0.0036 | Yes | this paper | Table 2 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 2 |
| Grit | 0.7647 | 0.0088 | Yes | this paper | Table 2 |
| GRED | 0.7685 | 0.0019 | Yes | this paper | Table 2 |
| Graph-Mamba-I | 0.7370 | 0.0034 | Yes | this paper | Table 2 |
| Graph-Mamba-II | 0.7576 | 0.0042 | Yes | this paper | Table 3 |
| GSSC | 0.7764 | 0.0046 | No | this paper | Table 2 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 2 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 2 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 2 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 2 |
| GraphGPS | 0.9805 | 0.0013 | Yes | this paper | Table 2 |
| Exphormer | 0.9855 | 0.0004 | Yes | this paper | Table 2 |
| Grit | 0.9811 | 0.0011 | Yes | this paper | Table 2 |
| GRED | 0.9838 | 0.0001 | Yes | this paper | Table 2 |
| Graph-Mamba-I | 0.9842 | 0.0008 | Yes | this paper | Table 2 |
| Graph-Mamba-II | 0.9839 | 0.0018 | Yes | this paper | Table 2 |
| GSSC | 0.9849 | 0.0005 | No | this paper | Table 2 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8100 | — | Yes | this paper | Table 2 |
| GIN | 0.8898 | 0.0056 | Yes | this paper | Table 2 |
| GAT | 0.9210 | 0.0024 | Yes | this paper | Table 2 |
| GatedGCN | 0.9223 | 0.0065 | Yes | this paper | Table 2 |
| GraphGPS | 0.9350 | 0.0041 | Yes | this paper | Table 2 |
| Exphormer | 0.9402 | 0.0021 | Yes | this paper | Table 2 |
| Graph-Mamba-I | 0.9340 | 0.0027 | Yes | this paper | Table 2 |
| GSSC | 0.9406 | 0.0064 | No | this paper | Table 2 |

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
| Graph-Mamba-I | 0.8671 | 0.0005 | Yes | this paper | Table 1 |
| GSSC | 0.8751 | 0.0008 | No | this paper | Table 1 |
| Graph-Mamba-II | 0.8714 | 0.0012 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GIN** (from: Xu et al. 2019)
- **GAT** (from: Veličković et al. 2018)
- **GatedGCN** (from: Corso et al. 2020)
- **SAN** (from: Ying et al. 2021)
- **GraphGPS** (from: Rampásek et al. 2022)
- **Exphormer** (from: Terzi et al. 2022)
- **Grit** (from: This paper (Table 1))
- **GRED** (from: This paper (Table 1))
- **Graph-Mamba-I** (from: This paper (Table 2))
- **Graph-Mamba-II** (from: This paper (Table 2))

## Extraction Notes

[MNIST] Extracted only MNIST results as requested. The paper reports Accuracy as a percentage (e.g.,
98.492), which was divided by 100 to fit the [0,1] range rule for Accuracy metrics. Table 1 does not
contain MNIST results. Table 2 and Table 3 (supplementary) contain overlapping MNIST results; Table
2 was used as the primary source as it contains the full set of baselines including the proposed
model GSSC. Graph-Mamba-II appears only in Table 3, so it was included based on that table.
[CIFAR10] Extracted only CIFAR10 results from Table 2 and Table 3. Values were converted from
percentages (e.g., 77.642) to decimals (0.77642) as per instructions for Accuracy metrics. Standard
deviations were parsed from the 'mean_std' format. [PATTERN] Extracted results for the PATTERN
dataset from Table 1 and Table 2. Both tables report the same values for GSSC and Graph-Mamba-I.
Graph-Mamba-II is only present in Table 2. All values are percentages, so they were divided by 100
to fit the [0,1] range for Accuracy. Standard deviations were parsed from the 'mean_std' format.
[CLUSTER] failed: 1 validation error for ExtractionOutput results.12.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [MalNet-Tiny] Extracted only MalNet-Tiny results from
Table 2. Note that GCN's result for MalNet-Tiny is reported as '81.0' without a standard deviation
in the table, so std is null. All other values include standard deviations. The metric is Accuracy,
which is normalized to [0,1] by dividing by 100. [PascalVOC-SP] failed: 3 validation errors for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] failed: 1 validation error for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-struct] failed: 1 validation error for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*