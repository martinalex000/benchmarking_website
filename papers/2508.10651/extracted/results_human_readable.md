# Extraction: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: Q-WL-RF
- Type: GNN

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Full | 0.7050 | 0.0030 | No | this paper | Table 1 |
| Plain | 0.3060 | 0.0010 | No | this paper | Table 1 |
| Maj. | 0.3060 | 0.0010 | No | this paper | Table 1 |
| Int. | 0.3060 | 0.0010 | No | this paper | Table 1 |
| Hyb. | 0.7050 | 0.0030 | No | this paper | Table 1 |
| WL-GK | 0.6710 | 0.0000 | Yes | this paper | Table 1 |
| GIN | 0.5940 | 0.0120 | Yes | this paper | Table 1 |
| GCN | 0.5410 | 0.0070 | Yes | this paper | Table 1 |
| GraphGPS | 0.6540 | 0.0100 | Yes | this paper | Table 1 |

### ogbg-molclintox — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Q-WL-RF (Ours) Full | 0.6560 | 0.0130 | No | this paper | Table 1 |
| Q-WL-RF (Ours) Plain | 0.7180 | 0.0200 | No | this paper | Table 1 |
| Q-WL-RF (Ours) Maj. | 0.7060 | 0.0330 | No | this paper | Table 1 |
| Q-WL-RF (Ours) Int. | 0.6950 | 0.0300 | No | this paper | Table 1 |
| Q-WL-RF (Ours) Hyb. | 0.6800 | 0.0220 | No | this paper | Table 1 |
| Kern. WL | 0.5370 | 0.0410 | Yes | this paper | Table 1 |
| GIN | 0.6400 | 0.0470 | Yes | this paper | Table 1 |
| GCN | 0.5910 | 0.0210 | Yes | this paper | Table 1 |
| GraphGPS | 0.8590 | 0.0400 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **WL-GK** (from: Curtiss et al. / standard WL kernel)
- **GIN** (from: Xu et al. 2019)
- **GCN** (from: Kipf & Welling 2017)
- **GraphGPS** (from: Rampásek et al. 2022)
- **Kern. WL**

## Extraction Notes

[ogbg-molhiv] failed: 1 validation error for ExtractionOutput results.5.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] Extracted all rows for
'Peptides-func' from Table 1. The table lists variants of the proposed Q-WL-RF method (Full, Plain,
Maj., Int., Hyb.) as well as baselines (WL-GK, GIN, GCN, GraphGPS). Note that 'Hyb.' has the same
value as 'Full' in the table (.705 ± .003), which is explicitly stated in the table. The text
mentions a 5.1 percentage point improvement over GraphGPS (0.705 - 0.654 = 0.051), confirming the
values. Standard deviations are parsed from the '±' notation. WL-GK std is listed as 0.000 in the
table. [ogbg-molclintox] Extracted all rows for the dataset 'molclintox' from Table 1. The dataset
name in the table is 'molclintox', which corresponds to 'ogbg-molclintox' as per the OGB dataset
naming convention and the paper's text reference. All values are test-set results (mean ± std). The
primary metric ROC-AUC was used.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*