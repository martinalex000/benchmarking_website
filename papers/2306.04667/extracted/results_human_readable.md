# Extraction: arXiv:2306.04667
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GAT
- Type: GAT_variant

## Results

### SCOPe — F1-Score ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GAT (Euclidean) | 0.8557 | 0.0020 | No | this paper | Table 1 |
| GAT (Cosine) | 0.8290 | 0.0080 | No | this paper | Table 1 |
| GAT (Manhattan) | 0.8481 | 0.0070 | No | this paper | Table 1 |
| GAT (Square) | 0.8406 | 0.0060 | No | this paper | Table 1 |
| SGM | 0.6289 | — | Yes | Rogen 2003 | Table 1 |
| SSEF | 0.4920 | — | Yes | Zotenko 2006 | Table 1 |
| DeepFold | 0.7615 | — | Yes | Liu 2018 | Table 1 |
| GraSR | 0.8124 | — | Yes | Xia 2022 | Table 1 |

## Baseline Models Identified

- **SGM** (from: rogen2003automatic)
- **SSEF** (from: zotenko2006secondary)
- **DeepFold** (from: liu2018learning)
- **GraSR** (from: xia2022fast)

## Extraction Notes

[Kinase] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or
instance of ExtractionOutput [type=model_type, input_value=[{'name': 'GCN',
'params_...inal_paper_hint': None}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [SCOPe] Extracted F1-Score results from Table 1 for
the SCOPe dataset. The table caption distinguishes between OOD F1-Score and standard F1-Score. The
FOCUS instruction requested the primary benchmark metric. While OOD is mentioned, the standard
F1-Score column represents the primary in-distribution classification performance typically used for
benchmarking unless OOD is explicitly specified as the ONLY metric. Given the ambiguity, I extracted
the standard F1-Score column as it is the main performance indicator for the models trained on
SCOPe. The GAT model has multiple configurations (distance functions); all are extracted. Baselines
SGM, SSEF, DeepFold, and GraSR are extracted from the same table. MSE results were ignored as per
instructions to focus on F1-Score.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*