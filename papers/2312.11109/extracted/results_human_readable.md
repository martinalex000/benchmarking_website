# Extraction: arXiv:2312.11109
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: LargeGT
- Type: GraphTransformer

## Results

### ogbn-papers100M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GOAT-full-δ | 0.6112 | 0.0010 | Yes | this paper | Table 1 |
| LargeGT-full | 0.6473 | 0.0005 | No | this paper | Table 1 |

### ogbn-products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphSAGE-δ | 0.7662 | 0.0093 | Yes | this paper | Table 1 |
| GAT-δ | 0.7738 | 0.0059 | Yes | this paper | Table 1 |
| GT-sparse-δ | 0.6076 | 0.0000 | Yes | this paper | Table 1 |
| NAGphormer-δ | 0.7528 | 0.0004 | Yes | this paper | Table 1 |
| GOAT-local-δ | 0.8117 | 0.0012 | Yes | this paper | Table 1 |
| GOAT-global-δ | 0.7028 | 0.0195 | Yes | this paper | Table 1 |
| GOAT-full-δ | 0.7988 | 0.0020 | Yes | this paper | Table 1 |
| LargeGT-local | 0.7895 | 0.0080 | No | this paper | Table 1 |
| LargeGT-full | 0.7981 | 0.0025 | No | this paper | Table 1 |

### snap-patents — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphSAGE-δ | 0.4843 | 0.0021 | Yes | this paper | Table 1 |
| GAT-δ | 0.4592 | 0.0022 | Yes | this paper | Table 1 |
| GT-sparse-δ | 0.4781 | 0.0000 | Yes | this paper | Table 1 |
| NAGphormer-δ | 0.6011 | 0.0005 | Yes | this paper | Table 1 |
| GOAT-local-δ | 0.4095 | 0.0016 | Yes | this paper | Table 1 |
| GOAT-global-δ | 0.4265 | 0.0007 | Yes | this paper | Table 1 |
| GOAT-full-δ | 0.5028 | 0.0014 | Yes | this paper | Table 1 |
| LargeGT-local | 0.6819 | 0.0311 | No | this paper | Table 1 |
| LargeGT-full | 0.7021 | 0.0012 | No | this paper | Table 1 |

## Baseline Models Identified

- **GraphSAGE** (from: Hamilton et al.)
- **GAT** (from: Veličković et al.)
- **GT-sparse**
- **NAGphormer** (from: Ying et al.)
- **GOAT** (from: Kong et al. 2023)

## Extraction Notes

[ogbn-products] Extracted only the 'ogbn-products' dataset results from Table 1. The table caption
indicates results are on 4 runs. Values are normalized to [0,1]. Standard deviations are parsed from
the ± notation. The proposed model is LargeGT. Baselines include GraphSAGE, GAT, GT-sparse,
NAGphormer, and GOAT variants. All baselines use the '-δ' suffix version which restricts computation
to 2-hop, as specified in the table caption and text. The 'Extended results' table (Table 2 in
appendix) was ignored as it contains epoch times and original baseline results without the δ
constraint, which are not the primary benchmark results for the scalable comparison requested.
[snap-patents] Extracted only the 'snap-patents' sub-table from Table 1. All values were converted
from percentages to [0,1] range. Standard deviations were parsed from the '±' notation. The 'δ'
suffix indicates a specific variant (2-hop computation) used for all models in this comparison,
treated as part of the model name for clarity. [ogbn-papers100M] Extracted only the 'ogbn-
papers100M' sub-table from Table 1 as requested. The table caption indicates results are on 4 runs.
The values are reported as percentages (e.g., 61.12), so they were divided by 100 to fit the [0,1]
range for Accuracy. The standard deviation is derived from the '±' notation (e.g., 61.12±0.10 ->
std=0.001). The proposed model is LargeGT-full, and the baseline is GOAT-full-δ.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*