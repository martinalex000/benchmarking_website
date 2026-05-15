# Extraction: arXiv:2407.00494
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Energy GNN (edge-wise)
- Type: GNN

## Results

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Energy GNN (edge-wise) | 0.8760 | 0.0340 | No | this paper | Table 1 |
| Energy GNN + attention | 0.7950 | 0.0180 | Yes | this paper | Table 1 |
| IGNN (1 layer) | 0.7300 | 0.0060 | Yes | this paper | Table 1 |
| GSD GNN | 0.7840 | 0.0220 | Yes | this paper | Table 1 |
| GCN (5 layer) | 0.7800 | 0.0140 | Yes | this paper | Table 1 |
| GAT (5 layer) | 0.7610 | 0.0150 | Yes | this paper | Table 1 |
| GCN* (5 layer, embedding dimension=64) | 0.8560 | 0.0580 | Yes | Gin | Table 1 |
| IGNN* (3 layer, embedding dimension=32) | 0.8930 | 0.0670 | Yes | ignn | Table 1 |
| GIN* (5 layer, embedding dimension=64) | 0.8940 | 0.0560 | Yes | gin | Table 1 |

### PPI — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Energy GNN (edge-wise) | 0.7620 | — | No | this paper | Table 1 |
| Energy GNN + attention | 0.7600 | — | Yes | this paper | Table 1 |
| IGNN (1 layer) | 0.7550 | — | Yes | this paper | Table 1 |
| GSD GNN | 0.7600 | — | Yes | this paper | Table 1 |
| GAT (5 layer) | 0.7430 | — | Yes | this paper | Table 1 |
| GCN (5 layer) | 0.7620 | — | Yes | this paper | Table 1 |
| MLP* | 0.4620 | — | Yes | IGNN | Table 1 |
| GCN* | 0.5920 | — | Yes | IGNN | Table 1 |
| GraphSAGE* | 0.7680 | — | Yes | GAT | Table 1 |
| GAT* | 0.9730 | — | Yes | GAT | Table 1 |
| IGNN* | 0.9760 | — | Yes | IGNN | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Energy GNN (edge-wise) | 0.7250 | 0.0030 | No | this paper | Table 1 |
| Energy GNN + attention | 0.7250 | 0.0050 | No | this paper | Table 1 |
| IGNN (1 layer) | 0.7180 | 0.0130 | Yes | this paper | Table 1 |
| GSD GNN | 0.7280 | 0.0080 | Yes | this paper | Table 1 |
| GCN (5 layer) | 0.7370 | 0.0050 | Yes | this paper | Table 1 |
| GAT (5 layer) | 0.7170 | 0.0320 | Yes | this paper | Table 1 |
| GCN* (5 layer, embedding dimension=64) | 0.7600 | 0.0320 | Yes | GIN | Table 1 |
| IGNN* (3 layer, embedding dimension=32) | 0.7770 | 0.0340 | Yes | IGNN | Table 1 |
| GIN* (5 layer, embedding dimension=64) | 0.7620 | 0.0190 | Yes | GIN | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Energy GNN + attention | 0.3810 | — | No | this paper | Table 1 |
| Energy GNN (edge-wise) | 0.3480 | — | Yes | this paper | Table 1 |
| IGNN (1 layer) | 0.2110 | — | Yes | this paper | Table 1 |
| GSD GNN | 0.3430 | — | Yes | this paper | Table 1 |
| GCN (5 layer) | 0.3620 | — | Yes | this paper | Table 1 |
| GAT (5 layer) | 0.3550 | — | Yes | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Energy GNN (edge-wise) | 0.3670 | — | No | this paper | Table 1 |
| Energy GNN + attention | 0.4020 | — | No | this paper | Table 1 |
| IGNN (1 layer) | 0.4260 | — | Yes | this paper | Table 1 |
| GSD GNN | 0.3750 | — | Yes | this paper | Table 1 |
| GCN (5 layer) | 0.3660 | — | Yes | this paper | Table 1 |
| GAT (5 layer) | 0.3350 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **Energy GNN + attention**
- **IGNN (1 layer)**
- **GSD GNN**
- **GCN (5 layer)**
- **GAT (5 layer)**
- **GCN* (5 layer, embedding dimension=64)** (from: Gin)
- **IGNN* (3 layer, embedding dimension=32)** (from: ignn)
- **GIN* (5 layer, embedding dimension=64)** (from: gin)
- **MLP*** (from: IGNN)
- **GCN*** (from: IGNN)
- **GraphSAGE*** (from: GAT)
- **GAT*** (from: GAT)
- **IGNN*** (from: IGNN)
- **Energy GNN (edge-wise)**
- **IGNN** (from: Ignatov et al.)
- **GCN** (from: Kipf & Welling)
- **GAT** (from: Veličković et al.)

## Extraction Notes

[MUTAG] Extracted only MUTAG results from Table 1. Values are percentages in the table, converted to
[0,1] range as per rules. Standard deviations are parsed from 'mean ± std' format. Asterisked models
are baselines from cited papers. [PROTEINS] Extracted all rows from Table 1 for the PROTEINS
dataset. Values are percentages from the table, converted to [0,1] range as per instructions.
Standard deviations are also converted to [0,1]. The asterisked models are baselines from cited
papers (GIN, IGNN) but included in the same table for comparison under equal parameter constraints
or specific configurations. [PPI] Extracted all rows from Table 1 (labeled as Table \ref{ppi} in
text) for the PPI dataset. The table reports mean micro-F1 scores as percentages. Values were
divided by 100 to normalize to [0, 1]. Standard deviations are not reported in this specific table
for the PPI results, so std is null. The asterisked models are baselines from other papers (IGNN,
GAT) as indicated by citations and the caption. [Peptides-func] Extracted only the 'Peptides-func'
(AP) column from Table 1. The second table (Table 2) reports performance *decreases* under
asynchronous inference, not absolute benchmark scores, so it was excluded. The values in Table 1 are
synchronous benchmark results. No standard deviations are reported in Table 1 for these specific
values. [Peptides-struct] Extracted MAE results for Peptides-struct from Table 1. The table caption
confirms these are from the LRGB benchmark. The second table (Table 2 in context, labeled
benchmark_decreases) reports performance *decreases* under asynchronous inference, not absolute MAE
values, so it was excluded as per instructions to extract benchmark results. Standard deviations are
not reported in Table 1 for these specific values.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*