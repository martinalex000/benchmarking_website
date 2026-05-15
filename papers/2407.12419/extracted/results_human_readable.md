# Extraction: arXiv:2407.12419
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: DBGNN (0.1M params)
- Type: GNN

## Results

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| Transform+LapPE | 0.2529 | 0.0016 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | dwivediLongRangeGraph2023 | Table 1 |
| DBGNN | 0.2864 | 0.0046 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**, 0.5M params (from: dwivediLongRangeGraph2023)
- **GCNII**, 0.5M params (from: dwivediLongRangeGraph2023)
- **GINE**, 0.5M params (from: dwivediLongRangeGraph2023)
- **GatedGCN**, 0.5M params (from: dwivediLongRangeGraph2023)
- **GatedGCN+RWSE**, 0.5M params (from: dwivediLongRangeGraph2023)
- **Transform+LapPE**, 0.5M params (from: dwivediLongRangeGraph2023)
- **SAN+LapPE**, 0.5M params (from: dwivediLongRangeGraph2023)
- **SAN+RWSE**, 0.5M params (from: dwivediLongRangeGraph2023)

## Extraction Notes

[SNBS] failed: JSON parse error from 'qwen3.6-35b-a3b': could not extract valid JSON [Peptides-
struct] Extracted all test MAE results from Table 1 for the Peptides-struct dataset. The table
explicitly lists 'test MAE' values. All values are normalized correctly (MAE is not a percentage).
The proposed model is DBGNN. Baselines are taken from dwivediLongRangeGraph2023 as stated in the
caption and text.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*