# Extraction: arXiv:2311.05964
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: BSMS
- Type: GNN

## Results

### Darcy Flow — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| U-Net | 0.0064 | — | Yes | Takamoto 2022 | Table 2 |
| FNO | 0.0120 | — | Yes | Takamoto 2022 | Table 2 |
| MGN | 0.0641 | 0.0005 | Yes | Pfaff 2020 | Table 2 |
| MGN + Tree | 0.0413 | 0.0147 | Yes | this paper | Table 2 |
| BSMS | 0.0098 | 0.0008 | No | Gao 2019 | Table 2 |
| Perceiver IO | 0.0141 | 0.0012 | Yes | Jaegle 2021 | Table 2 |
| Perceiver IO + GNN | 0.0131 | 0.0002 | Yes | this paper | Table 2 |

### Magnetostatics Shape — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ChebConv | 0.0000 | — | Yes | Lotzsch et al. 2022 | Table 1 |
| OFormer | 0.0000 | — | Yes | Li et al. 2023 | Table 1 |
| MGN | 0.0000 | 0.0000 | Yes | Pfaff et al. 2020 | Table 1 |
| MGN + Tree | 0.0000 | 0.0000 | No | this paper | Table 1 |
| BSMS | 0.0000 | 0.0000 | Yes | Gao et al. 2019 | Table 1 |
| Perceiver IO | 0.0001 | 0.0000 | Yes | Jaegle et al. 2021 | Table 1 |
| Perceiver IO + GNN | 0.0000 | 0.0000 | Yes | this paper | Table 1 |

### Magnetostatics Superpositions — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ChebConv | 0.0002 | — | Yes | Lotzsch et al. 2022 | Table 1 |
| MGN | 0.0009 | 0.0004 | Yes | Pfaff et al. 2020 | Table 1 |
| MGN + Tree | 0.0003 | 0.0000 | No | this paper | Table 1 |
| BSMS | 0.0002 | 0.0000 | Yes | Gao et al. 2019 | Table 1 |
| Perceiver IO | 0.0011 | 0.0008 | Yes | Jaegle et al. 2021 | Table 1 |
| Perceiver IO + GNN | 0.0003 | 0.0001 | Yes | this paper | Table 1 |

### Motor — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MGN | 0.0936 | 0.0132 | Yes | Pfaff 2020 | Table 2 |
| MGN + Tree | 0.0755 | 0.0050 | Yes | this paper | Table 2 |
| BSMS | 0.0691 | 0.0028 | No | this paper | Table 2 |
| Perceiver IO | 0.1670 | 0.0218 | Yes | Jaegle 2021 | Table 2 |
| Perceiver IO + GNN | 0.0922 | 0.0080 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **U-Net** (from: Ronneberger 2015)
- **FNO** (from: Li 2020)
- **MGN** (from: Pfaff 2020)
- **MGN + Tree** (from: this paper)
- **Perceiver IO** (from: Jaegle 2021)
- **Perceiver IO + GNN** (from: this paper)
- **ChebConv** (from: Defferrard et al. 2016)
- **OFormer** (from: Li et al. 2023)
- **BSMS** (from: Gao et al. 2019)

## Extraction Notes

[Darcy Flow] Extracted all rows from Table 2 for the 'Darcy Flow' column. Values are in scientific
notation (e.g., 6.4 x 10^-03) and converted to decimal. Standard deviations are provided in
parentheses in the table. U-Net and FNO results are cited from Takamoto 2022 as per the table
caption. BSMS is treated as the proposed model based on the paper's focus and comparison structure,
although it cites Gao 2019. [Motor] Extracted only the 'Motor' column results from Table 2. U-Net
and FNO have no results for Motor (marked with '-'), so they are excluded from the results list. The
proposed model is identified as BSMS based on the text describing it as the main method and the
table caption highlighting it for arbitrary grids. All values are RMSE, so lower is better. Standard
deviations are provided in parentheses. [Magnetostatics] Extracted results for Magnetostatics
dataset from Table 1. The table lists two sub-datasets/tasks: 'Mag. Shape' and 'Magn. Sup.'
(Superpositions). Both are standard configurations for the Magnetostatics benchmark in this context.
OFormer has no result for Superpositions (marked as '-'), so it is excluded from that subset. All
values are MSE (lower is better). Standard deviations are provided in parentheses.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*