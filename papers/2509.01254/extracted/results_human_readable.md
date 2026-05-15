# Extraction: What Expressivity Theory Misses:\\ Message Passing Complexity for GNNs
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: CIN
- Type: GNN

## Results

### ZINC-subset — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5300 | — | Yes | this paper | Table 1 |
| GraphSage | 0.4000 | — | Yes | this paper | Table 1 |
| GCN | 0.3700 | — | Yes | this paper | Table 1 |
| GSN | 0.1200 | — | Yes | this paper | Table 1 |
| FragNet | 0.0780 | — | Yes | this paper | Table 1 |
| CIN | 0.0770 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **GIN** (from: Xu et al. 2019)
- **GraphSage** (from: Hamilton et al. 2017)
- **GCN** (from: Kipf & Welling 2017)
- **GSN** (from: Maron et al. 2019)
- **FragNet** (from: null)

## Extraction Notes

[ZINC-subset] Extracted MAE results for ZINC-subset from Table 1. The table caption refers to
'prediction penalized logP' but the metric is labeled 'MAE (ZINC)'. All values are standard MAE
scores. No standard deviations are reported in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*