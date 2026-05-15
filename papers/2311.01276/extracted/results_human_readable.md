# Extraction: arXiv:2311.01276
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Neural Atoms
- Type: GNN

## Results

### OE62 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SchNet | 0.1351 | — | Yes | Schutt 2017 | Table 1 |
| + Ewald Block (SchNet) | 0.0811 | — | Yes | Kosmala 2023 | Table 1 |
| + Neural Atoms (SchNet) | 0.0834 | — | No | this paper | Table 1 |
| PaiNN | 0.6049 | — | Yes | Schutt 2021 | Table 1 |
| + Ewald Block (PaiNN) | 0.0590 | — | Yes | Kosmala 2023 | Table 1 |
| + Neural Atoms (PaiNN) | 0.0558 | — | No | this paper | Table 1 |
| DimeNet++ | 0.0501 | — | Yes | Gasteiger 2020 | Table 1 |
| + Ewald Block (DimeNet++) | 0.0479 | — | Yes | Kosmala 2023 | Table 1 |
| + Neural Atoms (DimeNet++) | 0.0551 | — | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer+LapPE | 0.3174 | 0.0020 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.3350 | 0.0003 | Yes | this paper | Table 1 |
| GraphGPS | 0.3337 | 0.0006 | Yes | this paper | Table 1 |
| GCN | 0.2329 | 0.0009 | Yes | this paper | Table 1 |
| GCN + Neural Atoms | 0.2534 | 0.0200 | No | this paper | Table 1 |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table 1 |
| GINE + Neural Atoms | 0.3126 | 0.0021 | No | this paper | Table 1 |
| GCNII | 0.3161 | 0.0004 | Yes | this paper | Table 1 |
| GCNII + Neural Atoms | 0.3049 | 0.0006 | No | this paper | Table 1 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 1 |
| GatedGCN + Neural Atoms | 0.3258 | 0.0003 | No | this paper | Table 1 |
| GatedGCN+RWSE | 0.3242 | 0.0008 | Yes | this paper | Table 1 |
| GatedGCN+RWSE + Neural Atoms | 0.3262 | 0.0010 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| GraphGPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCN + Neural Atoms | 0.6220 | 0.0046 | No | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GINE + Neural Atoms | 0.6154 | 0.0157 | No | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GCNII + Neural Atoms | 0.5996 | 0.0033 | No | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN + Neural Atoms | 0.6562 | 0.0075 | No | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| GatedGCN+RWSE + Neural Atoms | 0.6591 | 0.0050 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| GraphGPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCN + Neural Atoms | 0.2606 | 0.0027 | No | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GINE + Neural Atoms | 0.2553 | 0.0005 | No | this paper | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 1 |
| GCNII + Neural Atoms | 0.2563 | 0.0020 | No | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN + Neural Atoms | 0.2585 | 0.0017 | No | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| GatedGCN+RWSE + Neural Atoms | 0.2568 | 0.0005 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **GINE** (from: Hu 2020)
- **GCNII** (from: GCNII)
- **GatedGCN** (from: Bresson 2017)
- **GatedGCN+RWSE** (from: Bresson 2017)
- **Transformer+LapPE** (from: Vaswani 2017)
- **SAN+LapPE** (from: Kreuzer 2021)
- **GraphGPS** (from: Rampasek 2022)
- **SchNet**, 2.8M params (from: Schutt 2017)
- **+ Ewald Block**, 12.2M params (from: Kosmala 2023)
- **PaiNN**, 12.5M params (from: Schutt 2021)
- **DimeNet++**, 2.8M params (from: Gasteiger 2020)

## Extraction Notes

[Peptides-func] Extracted only Peptides-func AP results from Table 1. Table 2 and Table 3 contain
variant configurations (different proportions of neural atoms or virtual nodes) which were skipped
as per instructions to use standard/default configuration. The standard configuration corresponds to
the results in Table 1 where the full number of neural atoms is used (implied by the comparison with
baselines and the text stating '10 neural atoms' for 3D but Table 1 showing the main
ablation/comparison). Table 1 explicitly lists the main results for the proposed method variants
against baselines. [Peptides-struct] Extracted only the 'Peptides-struct' column from Table 1. Table
2 and Table 3 contain results for different grouping strategies or hyperparameter settings (number
of VNs/NAs), which are considered variants/ablations rather than the standard default configuration
results reported in the main comparison table. The primary metric MAE was used. Values are
normalized to [0,1] range as they are MAE values (though MAE is not strictly bounded by 1, the
values here are < 1). Standard deviations were parsed from the 'mean ± std' format. [PCQM-Contact]
Extracted all rows from Table 1 corresponding to the PCQM-Contact dataset and MRR metric. The
proposed method is 'Neural Atoms' which is appended to various baseline GNNs. Values were normalized
from percentages if necessary (none were percentages here, all were decimals). Standard deviations
were parsed from the 'mean ± s.d.' format. [OE62] The table caption specifies 'Validation energy
MAE', but the FOCUS instruction requires extracting results for the dataset OE62 using the primary
metric MAE. The table contains only validation results. No test results are provided in the text or
tables for OE62. The proposed model is referred to as '+ Neural Atoms' combined with different
backbones (SchNet, PaiNN, DimeNet++). I have extracted all rows for OE62. Note that the table
reports validation metrics, not test metrics, which is a deviation from the standard split rule, but
it is the only available data for this dataset in the provided text.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*