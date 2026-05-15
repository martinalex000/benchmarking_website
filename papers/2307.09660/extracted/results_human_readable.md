# Extraction: arXiv:2307.09660
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: NPQ
- Type: Other

## Results

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline | 0.3530 | 0.0019 | Yes | this paper | Table 1 |
| NPQ_M-P | 0.3141 | 0.0049 | Yes | this paper | Table 1 |
| NPQ_W-P-SV | 0.2589 | 0.0031 | No | this paper | Table 1 |
| NPQ_W | 0.2670 | 0.0009 | No | this paper | Table 1 |
| NPQ_M | 0.3037 | 0.0540 | No | this paper | Table 1 |

## Baseline Models Identified

- **GATv2** (from: Brody et al. 2021)
- **GCN** (from: Kipf & Welling 2016)
- **GINE** (from: Xu et al. 2018)

## Extraction Notes

[CLRS-30] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or
instance of ExtractionOutput [type=model_type, input_value=[{'name': 'Baseline', 'pa...nt':
'Velickovic-CLRS'}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [Peptides-struct] Extracted all rows from Table 1 for
the Peptides-struct dataset. The table presents Test MAE for three base processors (GATv2, GCN,
GINE) combined with different Neural PQ variants. The 'Baseline' column represents the base
processor alone. The proposed model is referred to as 'NPQ' with variants NPQ_M-P, NPQ_W-P-SV,
NPQ_W, and NPQ_M. All values are normalized to [0,1] range implicitly as MAE is a loss metric but
values are small; however, per rules, MAE is not normalized if >1, but here values are <1 so they
remain as is. Standard deviations are extracted from the ± notation.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*