# Extraction: arXiv:2405.11951
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GatedGCN-VN (57.0M params)
- Type: GCN_variant

## Results

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2483 | 0.0037 | Yes | Tonshoff et al. 2023 | Table 1 |
| GINE | 0.2703 | 0.0023 | Yes | Tonshoff et al. 2023 | Table 1 |
| GatedGCN | 0.3066 | 0.0013 | Yes | Tonshoff et al. 2023 | Table 1 |
| SAN | 0.2765 | 0.0042 | Yes | Kreuzer et al. 2021 | Table 1 |
| GPS | 0.2907 | 0.0028 | Yes | Rampásek et al. 2022 | Table 1 |
| LGI-GT | 0.3040 | 0.0029 | Yes | LGI-GT | Table 1 |
| GatedGCN-VN | 0.3141 | 0.0019 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Tonshoff et al. 2023)
- **GINE** (from: Tonshoff et al. 2023)
- **GatedGCN** (from: Tonshoff et al. 2023)
- **SAN** (from: Kreuzer et al. 2021)
- **GPS** (from: Rampásek et al. 2022)
- **LGI-GT** (from: LGI-GT)
- **Exphormer** (from: Shirzad et al. 2023)
- **GCN-VN** (from: this paper)

## Extraction Notes

[PascalVOC-SP] failed: 1 validation error for ExtractionOutput results.5.value   Input should be a
valid number [type=float_type, input_value=None, input_type=NoneType]     For further information
visit https://errors.pydantic.dev/2.13/v/float_type [COCO-SP] failed: 1 validation error for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] failed: 1 validation error for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-struct] failed: 1 validation error for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbg-code2] failed: 3 validation errors for
ExtractionOutput results.3.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbg-molpcba] Extracted only the 'ogbg-molpcba'
column results as requested. The proposed model is identified as GatedGCN-VN based on the text
stating 'we provide new results for GatedGCN on ogbg-molpcba (with and without virtual nodes)' and
the table highlighting GatedGCN-VN as the best performer. Params for GatedGCN-VN are taken from
Table 2 (57M). Other baseline params are not explicitly listed in the tables for ogbg-molpcba, so
they are null. Graphormer is mentioned in text as SOTA but not in the table, so it is excluded.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*