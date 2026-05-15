# Extraction: COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating State Space Models
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: COMBA
- Type: GNN

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4620 | 0.0080 | Yes | this paper | Table 1 |
| Gated-GCN | 0.4810 | 0.0071 | Yes | this paper | Table 1 |
| Nagphormer | 0.5040 | 0.0070 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.4760 | 0.0047 | Yes | this paper | Table 1 |
| Graph Mamba-1 | 0.4150 | 0.0016 | Yes | this paper | Table 1 |
| Graph Mamba-2 | 0.4900 | 0.0036 | Yes | this paper | Table 1 |
| COMBA | 0.5070 | 0.0025 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8840 | 0.0046 | Yes | this paper | Table 1 |
| Gated-GCN | 0.9050 | 0.0016 | Yes | this paper | Table 1 |
| Nagphormer | 0.9030 | 0.0006 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.8860 | 0.0024 | Yes | this paper | Table 1 |
| Graph Mamba-1 | 0.8060 | 0.0059 | Yes | this paper | Table 1 |
| Graph Mamba-2 | 0.9270 | 0.0021 | Yes | this paper | Table 1 |
| COMBA | 0.9420 | 0.0039 | No | this paper | Table 1 |

### Ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6800 | 0.0044 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7010 | 0.0065 | Yes | this paper | Table 1 |
| Nagphormer | 0.6960 | 0.0023 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.6780 | 0.0076 | Yes | this paper | Table 1 |
| Graph Mamba-1 | 0.6040 | 0.0020 | Yes | this paper | Table 1 |
| Graph Mamba-2 | 0.6860 | 0.0089 | Yes | this paper | Table 1 |
| COMBA | 0.7160 | 0.0037 | No | this paper | Table 1 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7950 | 0.0088 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8330 | 0.0079 | Yes | this paper | Table 1 |
| Nagphormer | 0.8000 | 0.0043 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.8150 | 0.0042 | Yes | this paper | Table 1 |
| Graph Mamba-1 | 0.6770 | 0.0009 | Yes | this paper | Table 1 |
| Graph Mamba-2 | 0.8690 | 0.0092 | Yes | this paper | Table 1 |
| COMBA | 0.8950 | 0.0038 | No | this paper | Table 1 |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8380 | 0.0034 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8320 | 0.0090 | Yes | this paper | Table 1 |
| Nagphormer | 0.8340 | 0.0045 | Yes | this paper | Table 1 |
| Cluster-GCN | 0.7580 | 0.0056 | Yes | this paper | Table 1 |
| Graph Mamba-1 | 0.7340 | 0.0113 | Yes | this paper | Table 1 |
| Graph Mamba-2 | 0.8030 | 0.0199 | Yes | this paper | Table 1 |
| COMBA | 0.8450 | 0.0009 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling)
- **Gated-GCN**
- **Nagphormer**
- **Cluster-GCN** (from: Chiang et al.)
- **Graph Mamba-1**
- **Graph Mamba-2**

## Extraction Notes

[Roman-empire] Extracted only the Roman-empire Accuracy column from Table 1 as requested. All values
include standard deviation. The proposed model COMBA is bolded in the table. [Amazon-ratings]
Extracted only Amazon-ratings Accuracy results from Table 1. All values parsed from the format
'value_{std}'. Bold values indicate best performance but were extracted normally as per
instructions. [Ogbn-arxiv] Extracted only the Ogbn-arxiv Accuracy column from Table 1. All values
are test-set results as implied by the context of benchmark comparison tables. Standard deviations
were parsed from the format 'value_{±std}'. Bold values indicate best performance but were extracted
normally. [Ogbn-products] failed: 5 validation errors for ExtractionOutput results.0.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Minesweeper] Extracted only the Minesweeper dataset
results as requested. The table caption explicitly states that ROC AUC scores are reported for
Minesweeper. All values include standard deviations. The proposed model is COMBA. [Tolokers]
Extracted only the 'Tolokers' dataset results as requested. The table caption confirms ROC AUC is
the metric for Tolokers. All values and standard deviations were parsed from the 'Tolokers' column.
The proposed model is COMBA.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*