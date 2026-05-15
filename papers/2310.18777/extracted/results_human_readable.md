# Extraction: arXiv:2310.18777
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: SEM-IL
- Type: GNN

## Results

### MPI3D-real — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline | 0.0454 | 0.0110 | Yes | this paper | Table 1 |
| NIL-only | 0.0434 | 0.0140 | Yes | this paper | Table 1 |
| SEM-only | 0.0429 | 0.0100 | Yes | this paper | Table 1 |
| SEM-IL | 0.0312 | 0.0081 | No | this paper | Table 1 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GCN) | 0.1250 | 0.0020 | Yes | this paper | Table 1 |
| Baseline+ (GCN) | 0.1180 | 0.0040 | Yes | this paper | Table 1 |
| SEM-only (GCN) | 0.1060 | 0.0020 | Yes | this paper | Table 1 |
| SEM-IL (GCN) | 0.1020 | 0.0050 | No | this paper | Table 1 |
| Baseline (GIN) | 0.1090 | 0.0030 | Yes | this paper | Table 1 |
| Baseline+ (GIN) | 0.1080 | 0.0030 | Yes | this paper | Table 1 |
| SEM-only (GIN) | 0.1060 | 0.0040 | Yes | this paper | Table 1 |
| SEM-IL (GIN) | 0.0980 | 0.0050 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline (GCN) | 0.7625 | 0.0038 | Yes | this paper | Table 1 |
| Baseline+ (GCN) | 0.7558 | 0.0100 | Yes | this paper | Table 1 |
| SEM-only (GCN) | 0.7840 | 0.0067 | Yes | this paper | Table 1 |
| SEM-IL (GCN) | 0.7909 | 0.0067 | No | this paper | Table 1 |
| Baseline (GIN) | 0.7699 | 0.0142 | Yes | this paper | Table 1 |
| Baseline+ (GIN) | 0.7701 | 0.0094 | Yes | this paper | Table 1 |
| SEM-only (GIN) | 0.7821 | 0.0078 | Yes | this paper | Table 1 |
| SEM-IL (GIN) | 0.7861 | 0.0073 | No | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN Baseline | 0.2213 | 0.0046 | Yes | this paper | Table 1 |
| GCN Baseline+ | 0.2268 | 0.0030 | Yes | this paper | Table 1 |
| GCN SEM-only | 0.2589 | 0.0071 | Yes | this paper | Table 1 |
| GCN SEM-IL | 0.2715 | 0.0074 | No | this paper | Table 1 |
| GIN Baseline | 0.2264 | 0.0049 | Yes | this paper | Table 1 |
| GIN Baseline+ | 0.2291 | 0.0040 | Yes | this paper | Table 1 |
| GIN SEM-only | 0.2566 | 0.0047 | Yes | this paper | Table 1 |
| GIN SEM-IL | 0.2802 | 0.0061 | No | this paper | Table 1 |

## Baseline Models Identified

- **Baseline** (from: OGB default hyperparameters)
- **Baseline+** (from: this paper (modified baseline))
- **SEM-only** (from: this paper)
- **IL-only**
- **Given-G**
- **NIL-only**

## Extraction Notes

[ogbg-molhiv] Extracted only the 'Test-full' column for 'ogbg-molhiv' as per the FOCUS instruction
to use the standard/default configuration. The table reports AUROC in percent form, so values were
divided by 100. The 'Valid-half' and 'Test-half' columns correspond to a pruned dataset variant and
were ignored. The 'Valid-full' column was ignored in favor of 'Test-full' as the latter represents
the final benchmark result. Both GCN and GIN backbones were included as they are the standard
baselines reported for this dataset in the paper. [ogbg-molpcba] Extracted only the 'Test-full'
column for 'molpcba (Avg.Precision)' from Table 1. The table caption states values are in percent
form, so values were divided by 100. The paper distinguishes between 'Valid-full/Test-full'
(standard split) and 'Valid-half/Test-half' (pruned split). The FOCUS instruction requested the
STANDARD/DEFAULT configuration, so only the 'Test-full' results were extracted. The proposed model
is identified as SEM-IL based on the bolding and text description. [PCQM4Mv2] Extracted only
PCQM4Mv2 results from Table 1. The paper reports validation performance as the test set is private.
The metric is MAE (lower is better). All values are normalized correctly. Baselines include GCN and
GIN variants with SEM-IL as the proposed method. [3dShapes] The paper mentions '3dShapes' in the
text as a dataset used for verification of the SEM-IL method. However, the provided text explicitly
states that 'The detailed experimental settings and results on additional similar datasets, dSprites
and MPI3D-real, are given in \cref{sec:app_more_experiments_toy}.' The provided tables (Table 1 and
Table 2) contain results for molhiv, molpcba, PCQM, and graph probing tasks, but do NOT contain any
results for the 3dShapes dataset. Therefore, no quantitative results could be extracted for 3dShapes
from the provided text. [dSprites] The paper mentions 'dSprites' in the text as a dataset where
results are given in the appendix ('sec:app_more_experiments_toy'). However, the provided text and
tables only contain results for 'molhiv', 'molpcba', 'PCQM', and graph probing tasks on molecular
properties. No tables or numerical results for 'dSprites' are present in the provided input.
Therefore, no results could be extracted for this dataset. [MPI3D-real] The table reports results
for 'MPI3D' which corresponds to the 'MPI3D-real' dataset mentioned in the text. The caption states
'The test MSE for different settings are the numbers multiplying 10^-3'. I have divided all
extracted values by 1000 to normalize them. The table shows results for different alpha values (0.8,
0.5, 0.2, 0.1). Since the prompt asks for the STANDARD/DEFAULT configuration and does not specify
which alpha is default, I extracted all available configurations for MPI3D. Note that for
alpha=0.02, the model did not converge, so those rows were skipped.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*