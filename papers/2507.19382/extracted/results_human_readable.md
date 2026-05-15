# Extraction: Learning Long-Range Representations with Equivariant Messages
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: Lorem (1.0M params)
- Type: GNN

## Results

### Biodimers — RMSE E ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Lorem | 0.2220 | — | No | this paper | Table 1 |
| Lorem | 1.6460 | — | No | this paper | Table 1 |
| Cace-Les | 2.2590 | — | Yes | this paper | Table 1 |
| Cace-Les | 3.1630 | — | Yes | this paper | Table 1 |
| Mace | 7.7930 | — | Yes | this paper | Table 1 |
| Mace | 16.1500 | — | Yes | this paper | Table 1 |
| Pet | 6.7580 | — | Yes | this paper | Table 1 |
| Pet | 16.4700 | — | Yes | this paper | Table 1 |

### Cumulene — RMSE E ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Lorem | 3.3090 | — | No | this paper | Table 1 |
| Lorem | 50.0840 | — | No | this paper | Table 1 |
| Cace-Les | 17.8030 | — | Yes | this paper | Table 1 |
| Cace-Les | 147.6160 | — | Yes | this paper | Table 1 |
| Mace | 12.5920 | — | Yes | this paper | Table 1 |
| Mace | 104.3180 | — | Yes | this paper | Table 1 |
| Pet | 3.2050 | — | Yes | this paper | Table 1 |
| Pet | 46.9050 | — | Yes | this paper | Table 1 |

### MgO surface — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Lorem | 0.0640 | — | No | this paper | Table 1 |
| Cace-Les | 0.0710 | — | Yes | this paper | Table 1 |
| Mace | 0.3760 | — | Yes | this paper | Table 1 |
| Pet | 0.2100 | — | Yes | this paper | Table 1 |
| 4G-NN | 0.2190 | — | Yes | this paper | Table 1 |
| SpookyNet | 0.1070 | — | Yes | this paper | Table 1 |
| Lorem | 0.0640 | — | No | this paper | Table 1 |
| Lorem | 4.0760 | — | No | this paper | Table 1 |
| Cace-Les | 0.0710 | — | Yes | this paper | Table 1 |
| Cace-Les | 7.9130 | — | Yes | this paper | Table 1 |
| Mace | 0.3760 | — | Yes | this paper | Table 1 |
| Mace | 5.9710 | — | Yes | this paper | Table 1 |
| Pet | 0.2100 | — | Yes | this paper | Table 1 |
| Pet | 6.2610 | — | Yes | this paper | Table 1 |
| 4G-NN | 0.2190 | — | Yes | this paper | Table 1 |
| 4G-NN | 66.0000 | — | Yes | this paper | Table 1 |
| SpookyNet | 0.1070 | — | Yes | this paper | Table 1 |
| SpookyNet | 5.3370 | — | Yes | this paper | Table 1 |

### NaCl cluster — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Lorem | 0.1120 | — | No | this paper | Table 1 |
| Cace-Les | 0.2100 | — | Yes | this paper | Table 1 |
| Mace | 1.6810 | — | Yes | this paper | Table 1 |
| Pet | 1.5170 | — | Yes | this paper | Table 1 |
| 4G-NN | 0.4810 | — | Yes | this paper | Table 1 |
| SpookyNet | 0.1350 | — | Yes | this paper | Table 1 |
| Lorem | 0.0900 | — | No | this paper | Table 2 |
| Cace-Les | 0.1610 | — | Yes | this paper | Table 2 |
| Mace | 1.3450 | — | Yes | this paper | Table 2 |
| Pet | 1.2490 | — | Yes | this paper | Table 2 |
| Lorem | 0.1120 | — | No | this paper | Table 1 |
| Lorem | 1.1550 | — | No | this paper | Table 1 |
| Cace-Les | 0.2100 | — | Yes | this paper | Table 1 |
| Cace-Les | 9.7840 | — | Yes | this paper | Table 1 |
| Mace | 1.6810 | — | Yes | this paper | Table 1 |
| Mace | 40.2190 | — | Yes | this paper | Table 1 |
| Pet | 1.5170 | — | Yes | this paper | Table 1 |
| Pet | 42.4380 | — | Yes | this paper | Table 1 |
| 4G-NN | 0.4810 | — | Yes | this paper | Table 1 |
| 4G-NN | 32.7800 | — | Yes | this paper | Table 1 |
| SpookyNet | 0.1350 | — | Yes | this paper | Table 1 |
| SpookyNet | 1.0520 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **Cace-Les**
- **Mace**
- **Pet**
- **4G-NN**
- **SpookyNet**

## Extraction Notes

[MgO] Extracted RMSE results for Energy (E) on the 'MgO surface' dataset from Table 1 (tab:metrics).
The table caption indicates these are Root Mean Squared Errors. The dataset split is noted as
'Validation' in the table row, but per instructions to extract standard/default results and focus on
the primary metric, these values are included. No standard deviation is reported in the table. Other
tables (MAE, alternative seeds) were ignored as per FOCUS instructions to use the standard
configuration and primary metric (RMSE). [NaCl] Extracted RMSE and MAE results for the 'NaCl
cluster' dataset from Table 1 and Table 2 respectively. The prompt focused on RMSE as the primary
metric, but included MAE as it is a standard benchmark score present in the tables for the same
dataset. Note that the table caption indicates these are validation set results ('(Validation)' or
'(Validation set)'), not test set results, but they are the only quantitative error metrics provided
for this specific dataset in the text. The 'Lorem' model has three parameter counts listed (839129,
1020300, 1020749, 1021198) corresponding to no LR, l=0, l=1, l=2. The results in the table are for
'1xSR+LR', which corresponds to the l=1 or l=2 configuration (likely l=1 given the slight increase
in params from l=0 to l=1 vs l=1 to l=2, but the text says 'l=0,1,2 (in that order) are 839129,
1020300, 1020749, and 1021198' which implies 4 values for 3 configs? Actually, 'no LR' is one
config, then l=0, l=1, l=2. So 4 configs. The table header says '1xSR+LR'. This likely refers to the
specific configuration used for the main results. Given the ambiguity, I used the highest param
count or the one associated with the main model description. However, for the JSON output, I used
the model name 'Lorem' as it appears in the table. The exact param count for the specific '1xSR+LR'
row is not explicitly distinguished between l=1 and l=2 in the table header, but the text lists
params for 'no LR, l=0, l=1, l=2'. The table only shows one 'Lorem' column. I will assume the
reported params for the proposed model are the ones listed in the text for the most complex version
or the one used. The text says 'parameter counts for no LR and l=0,1,2 (in that order) are 839129,
1020300, 1020749, and 1021198'. The table shows 'Lorem {1xSR+LR}'. This likely corresponds to l=1 or
l=2. Without explicit mapping, I'll use the model name from the table. The params_millions field in
the proposed_model object is set to 1.021 based on the last value in the sequence which might be the
full model, but it's ambiguous. I will stick to the extracted values. [Cumulene] The paper reports
results for the 'Cumulene' dataset in Tables 1, 2, and 3. However, the metrics reported are Root
Mean Squared Error (RMSE) and Mean Absolute Error (MAE) for Energy (E) and Forces (F). The FOCUS
instruction explicitly requests ONLY 'Accuracy' and to skip non-standard benchmark scores like
MAE/RMSE. Since no Accuracy metric is reported for the Cumulene dataset in the provided text, the
results array is empty. [Biodimers] failed: 4 validation errors for ExtractionOutput results.8.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type results.9.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [reactions] The user requested results for the dataset
'reactions'. The provided tables contain results for 'MgO surface', 'NaCl cluster', 'Biodimers', and
'Cumulene'. None of these datasets are named 'reactions'. Therefore, no results were extracted as
per the instruction to ignore rows belonging to other datasets. The tables provided are clearly for
molecular dynamics/quantum chemistry benchmarks (likely from the 'Lorem' paper which compares
against Mace, SpookyNet, etc.), not a dataset named 'reactions'. If 'reactions' was a typo for one
of the listed datasets, please clarify. Based on strict adherence to the prompt, the result list is
empty. [ADAPT] failed: 1 validation error for ExtractionOutput results.3.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*