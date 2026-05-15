# Extraction: arXiv:2306.08277
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Frigate
- Type: GNN

## Results

### Chengdu — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Frigate | 3.5470 | 0.2000 | No | this paper | Table 1 |
| STNN | 5.6330 | 0.1800 | Yes | this paper | Table 1 |
| DCRNN | 4.8930 | 0.2600 | Yes | this paper | Table 1 |
| LocaleGN | 4.5970 | 0.2200 | Yes | this paper | Table 1 |
| STGODE | 4.6930 | 0.1900 | Yes | this paper | Table 1 |
| STGCN | 5.7120 | 0.3300 | Yes | this paper | Table 1 |
| GraphWavenet | 5.3080 | 0.3000 | Yes | this paper | Table 1 |
| OURS | 3.5470 | 0.2000 | No | this paper | Table 2 |
| OURS (without Lipschitz) | 3.7870 | 0.1800 | Yes | this paper | Table 2 |
| OURS (without Gating) | 3.7340 | 0.1800 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **STNN**
- **DCRNN**
- **LocaleGN**
- **STGODE**
- **STGCN**
- **GraphWavenet**

## Extraction Notes

[Beijing] failed: 3 validation errors for ExtractionOutput results.4.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Chengdu] Extracted results for the Chengdu dataset
from Table 1 (main comparison) and Table 2 (ablation study). Table 1 includes the proposed model
Frigate and 6 baselines. Table 2 includes the full model (OURS) and two ablation variants. All
values are MAE. Standard deviations were parsed from the ± notation. No other datasets were included
as per instructions. [Harbin] failed: 2 validation errors for ExtractionOutput results.5.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*