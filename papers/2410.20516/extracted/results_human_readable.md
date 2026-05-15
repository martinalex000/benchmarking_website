# Extraction: arXiv:2410.20516
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: SEGNN
- Type: GNN

## Results

### Galaxy Clustering Dataset — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 2PCF | 2.0300 | 0.0200 | Yes | this paper | Table 1 |
| GNN | 2.7700 | 0.4100 | Yes | this paper | Table 1 |
| EGNN | 13.3300 | 0.0000 | Yes | this paper | Table 1 |
| NequIP (l_max = 1) | 2.8800 | 0.1500 | Yes | this paper | Table 1 |
| NequIP (l_max = 2) | 3.0700 | 0.1800 | Yes | this paper | Table 1 |
| SEGNN (l_max = 1) | 2.3100 | 0.0300 | No | this paper | Table 1 |
| SEGNN (l_max = 2) | 2.3700 | 0.0600 | No | this paper | Table 1 |
| PointNet++ | 2.8700 | 0.0700 | Yes | this paper | Table 1 |
| GNN (mean agg.) | 2.7700 | 0.4100 | Yes | this paper | Table 4 |
| GNN (global attn. agg.) | 2.6000 | 0.0600 | Yes | this paper | Table 4 |
| GNN (local + global attn. agg.) | 3.0000 | 0.1400 | Yes | this paper | Table 4 |
| GNN (invariant attn.) | 3.6200 | 0.0100 | Yes | this paper | Table 4 |

## Baseline Models Identified

- **2PCF**
- **GNN**
- **EGNN**
- **NequIP**
- **PointNet++**

## Extraction Notes

[Galaxy Clustering Dataset] Extracted MSE for Omega_m, sigma_8, and v. Note that the paper specifies
these values are in units of 10^-3. I have extracted the raw numbers as presented in the table. I
skipped the 'x, v' and 'x, 2PCF' input variants as per the instruction to use the standard/default
configuration (which corresponds to the 'x' input section in Table 1).

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*