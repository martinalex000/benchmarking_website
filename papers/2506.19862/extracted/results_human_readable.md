# Extraction: DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: DualEquiNet
- Type: GNN

## Results

### COVID — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SchNet | 0.5340 | 0.0110 | Yes | this paper | Table 1 |
| EGNN | 0.5350 | 0.0110 | Yes | this paper | Table 1 |
| GVPGNN | 0.5310 | 0.0110 | Yes | this paper | Table 1 |
| TFN | 0.5350 | 0.0110 | Yes | this paper | Table 1 |
| FastEGNN | 0.4780 | 0.0310 | Yes | this paper | Table 1 |
| HEGNN | 0.5330 | 0.0110 | Yes | this paper | Table 1 |
| GotenNet | 0.4750 | 0.0090 | Yes | this paper | Table 1 |
| DualEquiNet | 0.3530 | 0.0060 | No | this paper | Table 1 |
| w/o CSIP | 0.3560 | 0.0020 | Yes | this paper | Table 2 |
| w/o CSIP/Cross | 0.3560 | 0.0130 | Yes | this paper | Table 2 |
| w/o CSIP/Cross/Dual | 0.3620 | 0.0100 | Yes | this paper | Table 2 |

### Ribonanza — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SchNet | 0.9370 | 0.0120 | Yes | this paper | Table 1 |
| EGNN | 0.9400 | 0.0120 | Yes | this paper | Table 1 |
| GVPGNN | 0.9320 | 0.0100 | Yes | this paper | Table 1 |
| TFN | 0.9390 | 0.0120 | Yes | this paper | Table 1 |
| FastEGNN | 0.8390 | 0.0200 | Yes | this paper | Table 1 |
| HEGNN | 0.9340 | 0.0100 | Yes | this paper | Table 1 |
| GotenNet | 0.8570 | 0.0130 | Yes | this paper | Table 1 |
| DualEquiNet | 0.5580 | 0.0120 | No | this paper | Table 1 |
| w/o CSIP | 0.5860 | 0.0160 | Yes | this paper | Table 2 |
| w/o CSIP/Cross | 0.5910 | 0.0810 | Yes | this paper | Table 2 |
| w/o CSIP/Cross/Dual | 0.5920 | 0.0280 | Yes | this paper | Table 2 |

### Tc-Ribo — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SchNet | 0.7370 | 0.0020 | Yes | this paper | Table 1 |
| EGNN | 0.7200 | 0.0220 | Yes | this paper | Table 1 |
| GVPGNN | 0.7360 | 0.0030 | Yes | this paper | Table 1 |
| TFN | 0.6940 | 0.0080 | Yes | this paper | Table 1 |
| FastEGNN | 0.7310 | 0.0060 | Yes | this paper | Table 1 |
| HEGNN | 0.7290 | 0.0070 | Yes | this paper | Table 1 |
| GotenNet | 0.7180 | 0.0020 | Yes | this paper | Table 1 |
| DualEquiNet | 0.6360 | 0.0490 | No | this paper | Table 1 |
| w/o CSIP | 0.6820 | 0.0260 | Yes | this paper | Table 2 |
| w/o CSIP/Cross | 0.6980 | 0.0100 | Yes | this paper | Table 2 |
| w/o CSIP/Cross/Dual | 0.6990 | 0.0100 | Yes | this paper | Table 2 |

### TorsionAngle — Circular MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SchNet | 18.5400 | 0.8600 | Yes | this paper | Table 1 |
| EGNN | 17.7900 | 0.6100 | Yes | this paper | Table 1 |
| GVPGNN | 17.5600 | 0.2100 | Yes | this paper | Table 1 |
| TFN | 21.9700 | 0.4500 | Yes | this paper | Table 1 |
| FastEGNN | 18.8900 | 0.2200 | Yes | this paper | Table 1 |
| HEGNN | 18.4100 | 0.2200 | Yes | this paper | Table 1 |
| GotenNet | 16.2700 | 1.1900 | Yes | this paper | Table 1 |
| DualEquiNet | 15.8700 | 2.0300 | No | this paper | Table 1 |

## Baseline Models Identified

- **SchNet**
- **EGNN**
- **GVPGNN**
- **TFN**
- **FastEGNN**
- **HEGNN**
- **GotenNet**

## Extraction Notes

[COVID] Extracted results for the 'COVID' dataset from Table 1 (main comparison) and Table 2
(ablation study). In Table 1, the 'COVID' section contains four sub-metrics (Reactivity, pH10, Mg
pH10, Avg.). The 'Avg.' column represents the primary benchmark result for the dataset as indicated
by the table structure and caption. Table 2 explicitly lists 'COVID' with a single RMSE value, which
matches the 'Avg.' value from Table 1 for the proposed model. All other rows in Table 1 for COVID
were skipped as they are sub-components of the average or secondary metrics. The standard deviations
were parsed from the '±' notation. [Ribonanza] Extracted results for Ribonanza from Table 1 (main
comparison) and Table 2 (ablation study). Table 1 reports the 'Avg.' metric for Ribonanza which
corresponds to the primary benchmark RMSE. Table 2 reports the aggregate RMSE for Ribonanza. Note
that the standard deviation for DualEquiNet in Table 2 (0.123) differs significantly from Table 1
(0.012), likely due to different experimental settings or reporting conventions in the ablation
table, but both values were extracted as they appear in the text. [Tc-Ribo] Extracted all rows for
Tc-Ribo from Table 1 (main comparison) and Table 2 (ablation study). Table 1 lists the primary
baselines and the proposed model. Table 2 lists the proposed model and its ablation variants. All
values are RMSE (lower is better). Standard deviations were parsed from the '±' notation. No
external data usage was indicated. [TorsionAngle] Extracted only the 'Avg.' column results for the
TorsionAngle dataset as requested. The table caption specifies 'Circular MAE ± std.' and the values
are presented in that format. All models listed are included. The proposed model is identified as
DualEquiNet based on the bolded best performance in the Avg. column and typical paper structure.
[RNASolo SASA] The user requested results ONLY for the dataset 'RNASolo SASA'. The provided text
contains tables for 'N-chain task', 'RNA property prediction' (datasets: COVID, Ribonanza, Tc-Ribo),
and 'TorsionAngle'. None of these tables contain a dataset named 'RNASolo SASA'. Therefore, no
results were extracted as per the strict filtering instruction. [mRFP Protein SASA] The user
requested results ONLY for the dataset 'mRFP Protein SASA'. The provided text contains tables for
'N-chain task', 'RNA property prediction' (COVID, Ribonanza, Tc-Ribo), and 'TorsionAngle' dataset.
None of these tables contain results for 'mRFP Protein SASA'. Therefore, the results list is empty.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*