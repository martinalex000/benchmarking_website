# Extraction: arXiv:2406.09639
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: TGB (Temporal Benchmark)
- Type: Other

## Results

### thgl-forum — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgeBank_tw | 0.5340 | — | Yes | this paper | Table 1 |
| EdgeBank_inf | 0.6170 | — | Yes | this paper | Table 1 |
| RecB_default | 0.5610 | — | Yes | this paper | Table 1 |
| TGN | 0.6490 | 0.0970 | Yes | this paper | Table 1 |
| TGN_edge-type | 0.7290 | 0.0090 | No | this paper | Table 1 |

### thgl-software — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgeBank_tw | 0.2880 | — | Yes | this paper | Table 1 |
| EdgeBank_inf | 0.4490 | — | Yes | this paper | Table 1 |
| RecB_default | 0.0990 | — | Yes | this paper | Table 1 |
| TGN | 0.3240 | 0.0170 | Yes | this paper | Table 1 |
| TGN_edge-type | 0.4240 | 0.0130 | Yes | this paper | Table 1 |
| STHN | 0.7310 | 0.0050 | Yes | this paper | Table 1 |

### tkgl-icews — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgeBank_tw | 0.0200 | — | Yes | Poursafaei et al. 2022 | Table 1 |
| EdgeBank_inf | 0.0090 | — | Yes | Poursafaei et al. 2022 | Table 1 |
| RecB_train | 0.2110 | — | Yes | Gastinger et al. 2024 | Table 1 |
| RecB_default | 0.2060 | — | Yes | Gastinger et al. 2024 | Table 1 |
| RE-GCN | 0.1820 | 0.0030 | Yes | Li et al. 2021 | Table 1 |
| CEN | 0.1870 | 0.0030 | Yes | Li et al. 2022 | Table 1 |
| TLogic | 0.1860 | 0.0010 | Yes | Liu et al. 2021 | Table 1 |

### tkgl-polecat — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgeBank_tw | 0.0560 | — | Yes | Poursafaei 2022 | Table 1 |
| EdgeBank_inf | 0.0450 | — | Yes | Poursafaei 2022 | Table 1 |
| RecB_train | 0.1980 | — | Yes | Gastinger 2024 | Table 1 |
| RecB_default | 0.1670 | — | Yes | Gastinger 2024 | Table 1 |
| RE-GCN | 0.1750 | 0.0020 | Yes | Li 2021 | Table 1 |
| CEN | 0.1840 | 0.0020 | Yes | Li 2022 | Table 1 |
| TLogic | 0.2280 | 0.0010 | Yes | Liu 2021 | Table 1 |

### tkgl-smallpedia — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgeBank_tw | 0.3530 | — | Yes | Poursafaei et al. 2022 | Table 1 |
| EdgeBank_inf | 0.3330 | — | Yes | Poursafaei et al. 2022 | Table 1 |
| RecB_train | 0.6050 | — | Yes | Gastinger et al. 2024 | Table 1 |
| RecB_default | 0.4860 | — | Yes | Gastinger et al. 2024 | Table 1 |
| RE-GCN | 0.5940 | 0.0010 | Yes | Li et al. 2021 | Table 1 |
| CEN | 0.6120 | 0.0010 | Yes | Li et al. 2022 | Table 1 |
| TLogic | 0.5950 | 0.0010 | Yes | Liu et al. 2021 | Table 1 |

## Baseline Models Identified

- **EdgeBank_tw** (from: Poursafaei et al. 2022)
- **EdgeBank_inf** (from: Poursafaei et al. 2022)
- **RecB_train** (from: Gastinger et al. 2024)
- **RecB_default** (from: Gastinger et al. 2024)
- **RE-GCN** (from: Li et al. 2021)
- **CEN** (from: Li et al. 2022)
- **TLogic** (from: Liu et al. 2021)
- **TGN** (from: Rossi et al. 2020)
- **TGN_edge-type** (from: Rossi et al. 2020 (adapted))
- **STHN** (from: Li et al. 2023)

## Extraction Notes

[tkgl-smallpedia] Extracted only the Test MRR results for the 'tkgl-smallpedia' dataset from Table
1. Standard deviations are provided for RE-GCN, CEN, and TLogic. Other models report point estimates
only. The paper does not propose a new model but evaluates existing baselines on the TGB benchmark.
[tkgl-polecat] Extracted only the 'tkgl-polecat' dataset results from Table 1 (MRR results). The
table provides Test MRR values. Standard deviations are provided for RE-GCN, CEN, and TLogic. Other
models do not report std in Table 1. Table 2 also contains tkgl-polecat MRR results which match
Table 1 exactly, so no duplicate extraction was needed. The proposed model 'TGB' is the
framework/benchmark suite, not a specific model with reported MRR results in the table, so it is not
included in the results list. [tkgl-icews] Extracted only the 'tkgl-icews' dataset results from
Table 1 (MRR column). The paper does not propose a new model but evaluates existing baselines.
Standard deviation is only reported for RE-GCN, CEN, and TLogic in Table 1; heuristic baselines
(EdgeBank, RecB) do not report std in Table 1, though Table 2 shows point estimates. Table 2
confirms the MRR values. All values are normalized to [0,1]. [tkgl-wikidata] failed: 5 validation
errors for ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.3.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [thgl-software] Extracted only the 'thgl-software'
dataset results as requested. The table provides Validation and Test columns; per instructions, only
Test results were extracted. No proposed model is explicitly named in the text for this specific
table, so all models are treated as baselines. Standard deviations are parsed from the scriptsize
notation. [thgl-forum] Extracted only the 'thgl-forum' Test MRR results as requested. The proposed
model is identified as TGN_edge-type based on the text highlighting its improvement and bolded best
performance. Baselines are extracted from the same column. Standard deviations are parsed from the
table cells containing '±' notation. RecB_default has a test value but no std reported in the table
cell (only validation/test values shown without error bars in that specific cell, though other rows
have them; however, looking closely at the table, RecB_default row has '0.552' and '0.561' without
±, implying no std or single run, but TGN/TGN_edge-type have ±. I will set std to null for RecB as
it is not explicitly provided in the cell format like the others). [thgl-github] failed: 4
validation errors for ExtractionOutput results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.3.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [thgl-myket] failed: 4 validation errors for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.3.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*