# Extraction: arXiv:2310.01618
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PIGN (0.5M params)
- Type: GNN

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7130 | 0.0060 | Yes | this paper | Table 1 |
| GAT | 0.6990 | 0.0100 | Yes | this paper | Table 1 |
| IterGNN with GCN | 0.4533 | 0.1006 | Yes | this paper | Table 1 |
| IterGNN with GAT | 0.4991 | 0.0494 | Yes | this paper | Table 1 |
| PIGN with GCN (Ours) | 0.6840 | 0.0150 | No | this paper | Table 1 |
| PIGN with GAT (Ours) | 0.6610 | 0.0170 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8090 | 0.0060 | Yes | this paper | Table 1 |
| GAT | 0.8040 | 0.0110 | Yes | this paper | Table 1 |
| IterGNN with GCN | 0.6090 | 0.1740 | Yes | this paper | Table 1 |
| IterGNN with GAT | 0.6050 | 0.1750 | Yes | this paper | Table 1 |
| PIGN with GCN (Ours) | 0.7670 | 0.0140 | No | this paper | Table 1 |
| PIGN with GAT (Ours) | 0.7920 | 0.0090 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (w/o iterations) | 0.1510 | 0.0029 | Yes | Kipf 2017 | Table 1 |
| GAT (w/o iterations) | 0.1204 | 0.0127 | Yes | Veličković 2018 | Table 1 |
| GraphSAGE (w/o iterations) | 0.3015 | 0.0032 | Yes | Hamilton 2017 | Table 1 |
| IterGNN + GCN | 0.1736 | 0.0311 | Yes | this paper | Table 1 |
| IterGNN + GAT | 0.1099 | 0.0459 | Yes | this paper | Table 1 |
| IterGNN + GraphSAGE | 0.1816 | 0.0014 | Yes | this paper | Table 1 |
| PIGN + GCN | 0.1831 | 0.0038 | No | this paper | Table 1 |
| PIGN + GAT | 0.1706 | 0.0046 | No | this paper | Table 1 |
| PIGN + GraphSAGE | 0.3560 | 0.0037 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2017)
- **GAT** (from: Veličković 2018)
- **GraphSAGE** (from: Hamilton 2017)
- **IterGNN** (from: this paper)

## Extraction Notes

[PascalVOC-SP] Extracted all 9 rows from Table 1 for the PascalVOC-SP dataset. The table presents F1
scores for three backbone architectures (GCN, GAT, GraphSAGE) across three model frameworks (w/o
iterations, IterGNN, PIGN). The proposed model is PIGN. All values are normalized to [0,1] as they
are F1 scores. Standard deviations are included where reported. [Cora] Extracted only Cora results
as requested. Values are percentages from the table, converted to [0,1] range. Standard deviations
are also converted. Note: The proposed model PIGN does not achieve the highest accuracy on the
standard Cora dataset (GCN is higher), but it is the proposed method. [CiteSeer] Extracted only
CiteSeer results from Table 1. Values were converted from percentages to [0,1] range. Standard
deviations were parsed from the ± notation. The table caption indicates these are accuracy scores on
the standard test split. [CIFAR-10] failed: JSON parse error from 'qwen3.6-35b-a3b': could not
extract valid JSON

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*