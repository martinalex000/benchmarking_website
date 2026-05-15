# Extraction: arXiv:2309.04941
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: 2-DRFWL(2) GNN
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
| SAN+RWSE | 0.6439 | 0.0075 | No | this paper | Table 1 |
| 2-DRFWL(2) GNN | 0.5953 | 0.0048 | Yes | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | No | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| 2-DRFWL(2) GNN | 0.2594 | 0.0038 | Yes | this paper | Table 1 |

### Synthetic — Normalized MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MPNN | 0.3515 | — | Yes | this paper | Table 2 |
| ID-GNN | 0.0006 | — | Yes | this paper | Table 2 |
| NGNN | 0.0003 | — | Yes | this paper | Table 2 |
| GNNAK+ | 0.0004 | — | Yes | this paper | Table 2 |
| PPGN | 0.0003 | — | Yes | this paper | Table 2 |
| I$^2$-GNN | 0.0003 | — | Yes | this paper | Table 2 |
| 2-DRFWL(2) GNN | 0.0004 | — | No | this paper | Table 2 |
| 3-DRFWL(2) GNN | 0.0006 | — | Yes | this paper | Table 1 |

### ZINC-250K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| d-DRFWL(2) GNN | 0.0250 | 0.0030 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN* | 0.7707 | 0.0149 | Yes | this paper | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | this paper | Table 1 |
| DGN | 0.7970 | 0.0097 | Yes | this paper | Table 1 |
| HIMP | 0.7880 | 0.0082 | Yes | this paper | Table 1 |
| GSN | 0.8039 | 0.0090 | Yes | this paper | Table 1 |
| Deep LRP | 0.7719 | 0.0140 | Yes | this paper | Table 1 |
| CIN-small | 0.8005 | 0.0104 | Yes | this paper | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | this paper | Table 1 |
| Nested GIN* | 0.7834 | 0.0186 | Yes | this paper | Table 1 |
| GNNAK+ | 0.7961 | 0.0119 | Yes | this paper | Table 1 |
| SUN (EGO) | 0.8003 | 0.0055 | Yes | this paper | Table 1 |
| I$^2$-GNN | 0.7868 | 0.0093 | Yes | this paper | Table 1 |
| d-DRFWL(2) GNN | 0.7818 | 0.0219 | No | this paper | Table 1 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN* | 0.2703 | 0.0023 | Yes | this paper | Table 1 (labeled exp-zinc in text) |
| PNA | 0.2838 | 0.0035 | Yes | this paper | Table 1 (labeled exp-zinc in text) |
| DGN | 0.2885 | 0.0030 | Yes | this paper | Table 1 (labeled exp-zinc in text) |
| Nested GIN* | 0.2832 | 0.0041 | Yes | this paper | Table 1 (labeled exp-zinc in text) |
| GNNAK+ | 0.2930 | 0.0044 | Yes | this paper | Table 1 (labeled exp-zinc in text) |
| d-DRFWL(2) GNN | 0.2538 | 0.0019 | No | this paper | Table 1 (labeled exp-zinc in text) |

## Baseline Models Identified

- **MPNN**
- **ID-GNN**
- **NGNN**
- **GNNAK+**
- **PPGN**
- **I$^2$-GNN**
- **3-DRFWL(2) GNN**
- **GIN***
- **PNA**
- **DGN**
- **HIMP**
- **GSN**
- **Deep LRP**
- **CIN-small**
- **CIN**
- **Nested GIN***
- **SUN (EGO)**
- **I^2-GNN**
- **GIN** (from: Zhang et al. 2019 (implied by GIN citation))
- **Nested GIN** (from: Zhang et al. 2021 (NGNN))
- **GCN** (from: Kipf & Welling 2017)
- **GCNII** (from: Chen et al. 2020)
- **GINE** (from: Xu et al. 2019)
- **GatedGCN** (from: Bresson & Laurent 2017)
- **GatedGCN+RWSE** (from: this paper (variant))
- **Transformer+LapPE** (from: this paper (variant))
- **SAN+LapPE** (from: this paper (variant))
- **2-DRFWL(2) GNN** (from: this paper (variant))
- **SAN+RWSE** (from: Corso et al. 2020; Vignac et al. 2020)

## Extraction Notes

[Synthetic] Extracted all rows from Table 1 and Table 2 for the 'Synthetic' dataset. Table 1
contains results for 2-DRFWL(2) GNN and 3-DRFWL(2) GNN on 3-7 cycles. Table 2 contains results for
MPNN, ID-GNN, NGNN, GNNAK+, PPGN, I^2-GNN, and 2-DRFWL(2) GNN on 3-7 cycles and other substructures.
Table 3 (Ablation) was skipped as it contains variants of the proposed model rather than distinct
baseline comparisons, and the prompt asks for standard/default configuration results. All values are
Normalized MAE, so lower is better. No standard deviations were reported. [QM9] failed: 1 validation
error for ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': '1-GNN', 'param...inal_paper_hint': None}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [ZINC-12K] failed: 1
validation error for ExtractionOutput results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ZINC-250K] Extracted only the ZINC-250K MAE results
as requested. The proposed model is d-DRFWL(2) GNN. Other baselines with missing values for
ZINC-250K (marked as '--') were excluded from the results list as they have no quantitative result
for this specific dataset/metric combination. [ogbg-molhiv] Extracted all rows from Table 1 for the
'ogbg-molhiv' dataset. The metric column is labeled 'AUC' in the table header, which corresponds to
ROC-AUC for this benchmark. Values were converted from percentages (e.g., 77.07) to decimals
(0.7707) as per standard practice for ROC-AUC. Standard deviations were parsed from the 'mean ± std'
format. [ogbg-molpcba] Extracted results from the table labeled 'exp-zinc' which contains columns
for ZINC-12K, ZINC-250K, ogbg-molhiv, and ogbg-molpcba. Focused strictly on the 'ogbg-molpcba (AP)'
column as requested. Values are percentages from the table (e.g., 27.03) converted to [0,1] range
(0.2703). Standard deviations are parsed from the '±' notation. Note that the table caption mentions
'four-runs AP results', implying the std is based on 4 runs. The proposed model 'd-DRFWL(2) GNN' is
listed at the bottom. [Peptides-func] Extracted all rows from Table 1 for the 'Peptides-func'
dataset. The proposed model is identified as 'SAN+RWSE' based on the bolded value in the AP column
and the table caption categorizing methods into MPNNs, Transformer-based, and 'our method'. The
table presents results for both Peptides-func and Peptides-struct; only Peptides-func AP results
were extracted as per instructions. All values are normalized to [0,1] range for AP metric.
[Peptides-struct] Extracted all rows for Peptides-struct from Table 1. The proposed model is
identified as 'Transformer+LapPE' based on the table caption categorization ('our method') and the
bolded best result. All values are MAE, lower is better. No external data usage is indicated for
these standard LRGB benchmarks. [ProteinsDB] failed: 2 validation errors for ExtractionOutput
results.8.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.9.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[HomologyTAPE] failed: 1 validation error for ExtractionOutput results.3.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*