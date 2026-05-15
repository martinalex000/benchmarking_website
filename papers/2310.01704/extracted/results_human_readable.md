# Extraction: arXiv:2310.01704
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: SubFormer (0.6M params)
- Type: GraphTransformer

## Results

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 (right) |
| GIN | 0.3547 | 0.0045 | Yes | this paper | Table 1 (right) |
| GT | 0.2529 | 0.0016 | Yes | this paper | Table 1 (right) |
| SAN | 0.2545 | 0.0012 | Yes | this paper | Table 1 (right) |
| GraphGPS | 0.2500 | 0.0005 | Yes | Dwivedi 2022 | Table 1 (right) |
| Ours(567k) | 0.2487 | 0.0009 | No | this paper | Table 1 (right) |

### TOX21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Random Forest | 0.7690 | 0.0150 | Yes | this paper | Table 1 |
| XGBoost | 0.7940 | 0.0140 | Yes | this paper | Table 1 |
| Kernel SVM | 0.8220 | 0.0060 | Yes | this paper | Table 1 |
| Logistic Regression | 0.7940 | 0.0150 | Yes | this paper | Table 1 |
| GCN | 0.8400 | 0.0040 | Yes | this paper | Table 1 |
| GIN | 0.8500 | 0.0090 | Yes | this paper | Table 1 |
| HIMP | 0.8740 | 0.0050 | Yes | this paper | Table 1 |
| ChemRL-GEM | 0.8490 | 0.0030 | Yes | this paper | Table 1 |
| GraphGPS | 0.8490 | — | Yes | this paper | Table 1 |
| Ours | 0.8410 | 0.0030 | Yes | this paper | Table 1 |
| Ours(dual readout,VN) | 0.8440 | 0.0060 | Yes | this paper | Table 1 |
| Ours(dual readout) | 0.8510 | 0.0080 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 1 |
| GIN | 0.4080 | 0.0080 | Yes | this paper | Table 1 |
| HIMP | 0.1510 | 0.0060 | Yes | HIMP2020 | Table 1 |
| AUTOBAHN | 0.1060 | 0.0040 | Yes | thiede2021autobahn | Table 1 |
| GT | 0.2260 | 0.0140 | Yes | GraphGPS2022 | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | GraphGPS2022 | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | Graphormer2021 | Table 1 |
| GraphGPS | 0.0700 | 0.0040 | Yes | GraphGPS2022 | Table 1 |
| Ours(580k) | 0.0940 | 0.0030 | No | this paper | Table 1 |
| Ours(dual readout,slim,200k) | 0.0840 | 0.0040 | No | this paper | Table 1 |
| Ours(dual readout,VN, 567k) | 0.0780 | 0.0030 | No | this paper | Table 1 |
| Ours(dual readout,567k) | 0.0770 | 0.0030 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling)
- **GAT** (from: Veličković et al.)
- **GIN** (from: Xu et al.)
- **HIMP** (from: HIMP2020)
- **AUTOBAHN** (from: thiede2021autobahn)
- **GT** (from: GraphGPS2022)
- **SAN** (from: GraphGPS2022)
- **Graphormer** (from: Graphormer2021)
- **GraphGPS** (from: GraphGPS2022)
- **Random Forest**
- **XGBoost**
- **Kernel SVM**
- **Logistic Regression**
- **ChemRL-GEM**

## Extraction Notes

[ZINC] Extracted all rows from Table 1 labeled 'Results for the ZINC dataset'. The table caption
explicitly states 'Lower values are better', confirming MAE is the metric and lower is better. The
proposed model is referred to as 'Ours' with various configurations; these are mapped to 'SubFormer'
variants. Baseline scores are cited from external papers as noted in the caption. [Peptides-struct]
Extracted results from the right-hand table in Table 1, labeled 'Results for the Peptides-struct
dataset of long-range graph benchmarks'. The proposed model is referred to as 'Ours(567k)' in the
table, corresponding to the 567k parameter configuration mentioned in the text and hyperparameter
table. All baseline results are taken directly from the table. The metric is MAE, where lower is
better. [TOX21] Extracted only TOX21 results as requested. The table lists multiple variants of the
proposed model ('Ours', 'Ours(dual readout,VN)', 'Ours(dual readout)'). 'Ours(dual readout)' is
selected as the primary proposed model because it achieves the best performance (bolded) on TOX21.
GraphGPS value has no standard deviation reported in the table (marked with *), so std is null. All
values are normalized to [0,1] range. [TOXCAST] failed: 2 validation errors for ExtractionOutput
results.0.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.7.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[MUV] failed: 2 validation errors for ExtractionOutput results.0.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [MOLHIV] failed: 1 validation error for
ExtractionOutput results.8.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*