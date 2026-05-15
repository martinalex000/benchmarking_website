# Extraction: Density-aware Walks for Coordinated Campaign Detection
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: DECODE
- Type: GNN

## Results

### LEN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (NF) | 0.7020 | 0.0180 | Yes | this paper | Table 1 |
| GCN (RWW, Degree, mid) | 0.8100 | 0.0130 | No | this paper | Table 1 |
| GCN (RWW, Core, 0.5) | 0.7870 | 0.0100 | No | this paper | Table 1 |
| GCN (RWW, Truss, median) | 0.8000 | 0.0190 | No | this paper | Table 1 |
| GCN (NF+RWW, Degree, mid) | 0.7840 | 0.0060 | No | this paper | Table 1 |
| GCN (NF+RWW, Core, median) | 0.8050 | 0.0180 | No | this paper | Table 1 |
| GCN (NF+RWW, Truss, 0.5) | 0.8030 | 0.0190 | No | this paper | Table 1 |
| GAT (NF) | 0.7350 | 0.0150 | Yes | this paper | Table 1 |
| GAT (RWW, Degree, median) | 0.7950 | 0.0150 | No | this paper | Table 1 |
| GAT (RWW, Core, mid) | 0.8080 | 0.0220 | No | this paper | Table 1 |
| GAT (RWW, Truss, median) | 0.8360 | 0.0160 | No | this paper | Table 1 |
| GAT (NF+RWW, Degree, median) | 0.7920 | 0.0220 | No | this paper | Table 1 |
| GAT (NF+RWW, Core, 0.5) | 0.7850 | 0.0100 | No | this paper | Table 1 |
| GAT (NF+RWW, Truss, median) | 0.7920 | 0.0300 | No | this paper | Table 1 |
| GIN (NF) | 0.6330 | 0.0650 | Yes | this paper | Table 1 |
| GIN (RWW, Degree, 0.5) | 0.7560 | 0.0050 | No | this paper | Table 1 |
| GIN (RWW, Core, median) | 0.7660 | 0.0140 | No | this paper | Table 1 |
| GIN (RWW, Truss, 0.5) | 0.7710 | 0.0060 | No | this paper | Table 1 |
| GIN (NF+RWW, Degree, 0.5) | 0.7510 | 0.0050 | No | this paper | Table 1 |
| GIN (NF+RWW, Core, mid) | 0.7920 | 0.0140 | No | this paper | Table 1 |
| GIN (NF+RWW, Truss, mid) | 0.7820 | 0.0190 | No | this paper | Table 1 |
| SAGE (NF) | 0.7290 | 0.0060 | Yes | this paper | Table 1 |
| SAGE (RWW, Degree, 0.5) | 0.8520 | 0.0100 | No | this paper | Table 1 |
| SAGE (RWW, Core, mid) | 0.7740 | 0.0250 | No | this paper | Table 1 |
| SAGE (RWW, Truss, 0.5) | 0.8340 | 0.0520 | No | this paper | Table 1 |
| SAGE (NF+RWW, Degree, median) | 0.7580 | 0.0100 | No | this paper | Table 1 |
| SAGE (NF+RWW, Core, 0.5) | 0.7900 | 0.0170 | No | this paper | Table 1 |
| SAGE (NF+RWW, Truss, 0.5) | 0.8130 | 0.0180 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GIN** (from: Xu et al. 2019)
- **GraphSAGE** (from: Hamilton et al. 2017)

## Extraction Notes

[LEN] Extracted only binary classification accuracy results for the LEN dataset as per FOCUS
instructions. The paper presents multiple configurations (Degree/Core/Truss, different tau values,
NF/RWW/NF+RWW inputs). Since the prompt asks for 'STANDARD / DEFAULT configuration' but the paper
does not define a single standard configuration for the baselines (they are all trained on NF) and
the proposed method (DECODE) is evaluated across many configurations, I extracted all rows from the
binary classification accuracy table. The text highlights SAGE (RWW, Degree, 0.5) as the best
performing configuration for the proposed method. I did not extract multiclass results or F1 scores
as the primary metric specified was Accuracy for the standard task (binary classification is the
primary task described first and has the highest accuracy values). Note: The table structure is
complex with merged cells; I expanded them into individual rows for each model/input/feature
combination.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*