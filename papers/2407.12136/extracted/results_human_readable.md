# Extraction: arXiv:2407.12136
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: MOLTOP
- Type: GNN

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| MOLTOP | 0.6459 | 0.0005 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CIN | 0.8094 | 0.0057 | Yes | this paper | Table 1 |
| GSAT | 0.8067 | 0.0095 | Yes | this paper | Table 1 |
| Graphormer | 0.8051 | 0.0053 | Yes | this paper | Table 1 |
| MOLTOP | 0.8042 | 0.0025 | No | this paper | Table 1 |
| P-WL | 0.8039 | 0.0040 | Yes | this paper | Table 1 |
| Directional GSN | 0.8039 | 0.0090 | Yes | this paper | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | this paper | Table 1 |
| DeeperGCN | 0.7858 | 0.0117 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **CIN**
- **GSAT**
- **Graphormer**
- **P-WL**
- **Directional GSN**
- **PNA**
- **DeeperGCN**
- **GCN** (from: Kipf & Welling 2017)
- **GCNII** (from: Chen et al. 2020)
- **GINE** (from: Xu et al. 2019)
- **GatedGCN** (from: Battaglia et al. 2018 / Gilmer et al. 2017)
- **GatedGCN+RWSE** (from: LRGB 2021)
- **Transformer+LapPE** (from: LRGB 2021)
- **SAN+LapPE** (from: LRGB 2021)
- **SAN+RWSE** (from: LRGB 2021)

## Extraction Notes

[MoleculeNet] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary
or instance of ExtractionOutput [type=model_type, input_value=[{'name': 'GIN',
'params_...inal_paper_hint': None}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [ogbg-molhiv] Extracted Test AUROC results for ogbg-
molhiv from Table 1. Values were converted from percentages to [0,1] range. Standard deviations were
parsed from the 'mean ± std' format. Valid AUROC was ignored as per instructions to focus on test
results and primary metric. [Peptides-func] Extracted all rows from the provided table for Peptides-
func. Values were converted from percentages (e.g., 59.30) to decimals (0.593) as per standard AP
reporting conventions in the prompt instructions. Standard deviations were parsed from the '±'
notation.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*