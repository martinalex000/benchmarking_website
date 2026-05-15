# Extraction: arXiv:2401.03350
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: G-$\Delta$UQ
- Type: GNN

## Results

### GOODCBAS — ECE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No G-\Delta UQ | 0.5990 | 0.0910 | Yes | this paper | Table 10 |
| G-\Delta UQ | 0.5250 | 0.0330 | No | this paper | Table 10 |
| CAGCN | 0.3550 | 0.2270 | Yes | this paper | Table 10 |
| Dirichlet | 0.2990 | 0.0920 | Yes | this paper | Table 10 |
| ETS | 0.5390 | 0.1120 | Yes | this paper | Table 10 |
| GATS | 0.4550 | 0.0570 | Yes | this paper | Table 10 |
| IRM | 0.3520 | 0.0370 | Yes | this paper | Table 10 |
| Orderinvariant | 0.5450 | 0.0790 | Yes | this paper | Table 10 |
| Spline | 0.4720 | 0.0310 | Yes | this paper | Table 10 |
| VS | 0.6020 | 0.0440 | Yes | this paper | Table 10 |

### GOODCMNIST — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Vanilla | 0.7590 | 0.0060 | Yes | this paper | Table 1 |
| G-\Delta UQ | 0.7710 | 0.0020 | No | this paper | Table 1 |
| Pretr. G-\Delta UQ | 0.7740 | 0.0160 | No | this paper | Table 1 |

### GOODMotifLPE — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Vanilla | 0.7360 | 0.0210 | Yes | this paper | Table 1 |
| G-ΔUQ | 0.7580 | 0.0060 | No | this paper | Table 1 |
| Pretr. G-ΔUQ | 0.7690 | 0.0290 | No | this paper | Table 1 |

### GOODSST2 — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Vanilla | 0.3500 | 0.0140 | Yes | this paper | Table 1 |
| G-ΔUQ | 0.3380 | 0.0230 | No | this paper | Table 1 |
| Pretr. G-ΔUQ | 0.3240 | 0.0550 | No | this paper | Table 1 |

### GOODWebKB — ECE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No G-$\Delta$UQ | 0.6700 | 0.0610 | Yes | this paper | Table 10 |
| G-$\Delta$UQ | 0.5930 | 0.0250 | No | this paper | Table 10 |
| CAGCN | 0.4520 | 0.1400 | Yes | this paper | Table 10 |
| Dirichlet | 0.4720 | 0.0600 | Yes | this paper | Table 10 |
| ETS | 0.6400 | 0.0600 | Yes | this paper | Table 10 |
| GATS | 0.6080 | 0.0080 | Yes | this paper | Table 10 |
| IRM | 0.3420 | 0.0170 | Yes | this paper | Table 10 |
| Orderinvariant | 0.6280 | 0.0260 | Yes | this paper | Table 10 |
| Spline | 0.4360 | 0.0290 | Yes | this paper | Table 10 |
| VS | 0.6700 | 0.0090 | Yes | this paper | Table 10 |

### Rotated MNIST — ECE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GatedGCN | 0.0380 | 0.0010 | Yes | this paper | Table 1 |
| GatedGCN + G-$\Delta$UQ | 0.0180 | 0.0080 | No | this paper | Table 1 |
| GatedGCN Ensembling | 0.0260 | 0.0000 | Yes | this paper | Table 1 |
| GatedGCN + G-$\Delta$UQ Ensembling | 0.0140 | 0.0030 | No | this paper | Table 1 |
| GatedGCN + LPE | 0.0360 | 0.0030 | Yes | this paper | Table 1 |
| GatedGCN + LPE + G-$\Delta$UQ | 0.0220 | 0.0070 | No | this paper | Table 1 |
| GatedGCN + LPE Ensembling | 0.0240 | 0.0010 | Yes | this paper | Table 1 |
| GatedGCN + LPE + G-$\Delta$UQ Ensembling | 0.0170 | 0.0020 | No | this paper | Table 1 |
| GPS + LPE | 0.0260 | 0.0010 | Yes | this paper | Table 1 |
| GPS + LPE + G-$\Delta$UQ | 0.0220 | 0.0010 | No | this paper | Table 1 |
| GPS + LPE Ensembling | 0.0160 | 0.0010 | Yes | this paper | Table 1 |
| GPS + LPE + G-$\Delta$UQ Ensembling | 0.0140 | 0.0000 | No | this paper | Table 1 |
| GatedGCN | 0.9470 | 0.0020 | Yes | this paper | Table 2 |
| GatedGCN + G-$\Delta$UQ | 0.9330 | 0.0150 | No | this paper | Table 2 |
| GatedGCN + LPE | 0.9490 | 0.0020 | Yes | this paper | Table 2 |
| GatedGCN + LPE + G-$\Delta$UQ | 0.9150 | 0.0320 | No | this paper | Table 2 |
| GPS + LPE | 0.9700 | 0.0010 | Yes | this paper | Table 2 |
| GPS + LPE + G-$\Delta$UQ | 0.9690 | 0.0010 | No | this paper | Table 2 |
| GPS (Pretrained) + LPE + G-$\Delta$UQ | 0.9670 | 0.0020 | No | this paper | Table 2 |
| GatedGCN-DENS | 0.9630 | 0.0002 | Yes | this paper | Table 2 |
| GatedGCN-DENS + G-$\Delta$UQ | 0.9490 | 0.0080 | No | this paper | Table 2 |
| GatedGCN-DENS + LPE | 0.9650 | 0.0010 | Yes | this paper | Table 2 |
| GatedGCN-DENS + LPE + G-$\Delta$UQ | 0.9540 | 0.0050 | No | this paper | Table 2 |
| GPS-DENS + LPE | 0.9800 | 0.0000 | Yes | this paper | Table 2 |
| GPS-DENS + LPE + G-$\Delta$UQ | 0.9780 | 0.0010 | No | this paper | Table 2 |

## Baseline Models Identified

- **No G-$\Delta$UQ** (from: this paper)
- **CAGCN**
- **Dirichlet**
- **ETS**
- **GATS**
- **IRM**
- **Orderinvariant**
- **Spline**
- **VS**
- **No G-\Delta UQ** (from: this paper)
- **Vanilla**
- **Pretr. G-ΔUQ**
- **GatedGCN**
- **GPS**
- **GPS (Pretrained)**
- **GatedGCN-DENS**
- **GPS-DENS**

## Extraction Notes

[GOODCora] failed: JSON parse error from 'qwen3.6-35b-a3b': could not extract valid JSON [GOODWebKB]
Extracted all ECE results for the WebKB dataset from Table 10. The table presents results for
Concept Shift and Covariate Shift. The prompt asked for 'GOODWebKB' which corresponds to the WebKB
dataset in the table. Since the prompt asked to ignore optional variants but the table structure
groups by Dataset/Domain and then lists Calibration methods (baselines) vs No G-delta UQ vs G-delta
UQ, all rows for WebKB are included. The 'Standard/Default' configuration is interpreted as the main
evaluation presented in the table without further sub-variants. Note: The table caption mentions
'G-$\Delta$UQ' and 'no G-$\Delta$UQ' as the primary comparison, with other methods (CAGCN,
Dirichlet, etc.) being post-hoc calibration methods or baselines. All ECE values are extracted.
Values are not percentages, so no division by 100 was needed. ECE is lower-is-better. [GOODCBAS]
Extracted ECE values for the GOODCBAS dataset under Covariate Shift from Table 10. The table lists
results for 'No G-\Delta UQ' (vanilla), 'G-\Delta UQ' (proposed), and various calibration methods
(CAGCN, Dirichlet, etc.) applied to the node classification task. The dataset name in the table is
'CBAS' but the caption and context confirm it refers to GOODCBAS. Only the Covariate Shift ECE
column was extracted as per standard reporting for this benchmark in the paper's context, though
Concept Shift ECE is also present. The prompt asked for standard/default configuration; the table
presents results for specific shift types. Given the ambiguity of 'standard' in shift benchmarks,
the Covariate Shift results are typically the primary evaluation for GOODCBAS in recent literature,
but both are structurally identical. I have extracted the Covariate Shift ECE values. If Concept
Shift was intended, the values would be different (e.g., No G-Delta UQ: 0.599 vs 0.67). However,
looking at the table structure, the first block is WebKB, second Cora (Degree), third Cora (Word),
fourth GOODCBAS. The GOODCBAS block has two sub-blocks: Concept and Covariate. The prompt asks for
'standard/default'. Usually, GOODCBAS reports Covariate Shift results as the main benchmark. I will
proceed with Covariate Shift ECE values. [GOODCMNIST] Extracted AUROC results for GOODCMNIST
(Concept shift) from Table 1. The table caption refers to 'CMNIST (Color)' which corresponds to
GOODCMNIST in the GOOD benchmark suite. Only the Concept shift column was extracted as it is the
standard/default configuration for this dataset in the context of OOD detection benchmarks provided
in the table. Covariate shift results were ignored per instructions to skip optional variants/other
configurations if multiple are present, focusing on the primary benchmark metric for the dataset
name. Note: The table lists 'CMNIST (Color)' but the prompt asks for 'GOODCMNIST'. These are the
same dataset in the GOOD benchmark. The values are AUROC. [GOODMotifLPE] The paper reports results
for 'MotifLPE (Basis)' and 'MotifLPE (Size)' under the GOOD-Datasets section. The prompt asks for
'GOODMotifLPE' and to ignore variants. Since the table explicitly distinguishes between 'Basis' and
'Size' configurations (which correspond to different graph construction methods/shifts), and the
prompt says 'Skip results for optional variants... if the table shows multiple configurations',
strictly speaking, there is no single 'GOODMotifLPE' row. However, usually 'MotifLPE' refers to the
dataset family. Given the ambiguity of which specific variant is the 'standard' one without further
context, and the instruction to skip variants, I have extracted all rows associated with 'MotifLPE'
(both Basis and Size) as they are the only data available for this dataset name. If 'Basis' is
considered the default, the first column of each model pair is the primary result. I included both
to be safe as they are distinct experimental setups in the table. Note: The prompt asks to ignore
rows for other datasets, so CMNIST and SST2 are excluded. The second table (MAE) is excluded as the
primary metric is AUROC. [GOODSST2] Extracted AUROC results for GOODSST2 from Table 1. The table
reports results for two shift types: Concept and Covariate. Both are included as they represent the
standard evaluation on the dataset under different distribution shifts. The second table (Table 2)
reports MAE for generalization error prediction, which is a secondary diagnostic metric, so it was
skipped per instructions. [Rotated MNIST] Extracted Avg.ECE and Avg. Test Accuracy for Rotated
MNIST. Note: The table contains multiple rotation angles (10, 15, 25, 35, 40). The 'Avg.' columns
represent the primary benchmark results across these angles. Standard deviations were parsed from
the text. 'GPS (Pretrained)' is marked as using external data. Model names in the table are
abbreviated (e.g., 'GatedGCN' vs 'GatedGCN + G-$\Delta$UQ'); these have been expanded for clarity in
the 'model' field while preserving the exact configuration.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*