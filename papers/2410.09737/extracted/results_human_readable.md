# Extraction: arXiv:2410.09737
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: OGE-Aug
- Type: Other

## Results

### Alchemy — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1120 | 0.0010 | Yes | this paper | Table_alchemy |
| GINE | 0.0870 | 0.0010 | No | this paper | Table_alchemy |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table LRGB |
| GINE | 0.3180 | 0.0027 | Yes | this paper | Table LRGB |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table LRGB |
| Transformer | 0.3174 | 0.0020 | Yes | this paper | Table LRGB |
| SAN | 0.3350 | 0.0003 | Yes | this paper | Table LRGB |
| GPS | 0.3337 | 0.0006 | Yes | this paper | Table LRGB |
| GPS & OGE-Aug (ours) | 0.3543 | 0.0004 | No | this paper | Table LRGB |

### Zinc12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1630 | 0.0040 | Yes | this paper | Table_zinc |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table_zinc |
| GSN | 0.1150 | 0.0120 | Yes | this paper | Table_zinc |
| OSAN | 0.1870 | 0.0040 | Yes | this paper | Table_zinc |
| KP-GIN+ | 0.1190 | 0.0020 | Yes | this paper | Table_zinc |
| GNN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table_zinc |
| CIN | 0.0790 | 0.0060 | Yes | this paper | Table_zinc |
| GIN, with PEG | 0.1440 | 0.0080 | Yes | this paper | Table_zinc |
| GIN, with SignNet | 0.0850 | 0.0030 | Yes | this paper | Table_zinc |
| GIN, with BasisNet | 0.1550 | 0.0070 | Yes | this paper | Table_zinc |
| GIN, with SPE | 0.0690 | 0.0040 | Yes | this paper | Table_zinc |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table_zinc |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table_zinc |
| GPS | 0.0700 | 0.0040 | Yes | this paper | Table_zinc |
| Specformer | 0.0660 | 0.0030 | Yes | this paper | Table_zinc |
| GINE, with OGE-Aug (ours) | 0.0660 | 0.0020 | No | this paper | Table_zinc |
| GPS, with OGE-Aug (ours) | 0.0640 | 0.0030 | No | this paper | Table_zinc |

## Baseline Models Identified

- **GIN**
- **PNA**
- **GSN**
- **OSAN**
- **KP-GIN+**
- **GNN-AK+**
- **CIN**
- **GIN, with PEG** (from: wang2022equivariant)
- **GIN, with SignNet** (from: lim2022sign)
- **GIN, with BasisNet** (from: lim2022sign)
- **GIN, with SPE** (from: huang2023stability)
- **SAN** (from: kreuzer2021rethinking)
- **Graphormer** (from: Graphormer)
- **GPS** (from: rampavsek2022recipe)
- **Specformer** (from: specformer)
- **PEG** (from: wang2022equivariant)
- **SignNet** (from: lim2022sign)
- **BasisNet** (from: lim2022sign)
- **SPE** (from: huang2023stability)
- **GCN**
- **GINE**
- **GatedGCN**
- **Transformer**

## Extraction Notes

[QM9] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or
instance of ExtractionOutput [type=model_type, input_value=[{'name': 'MPNN',
'params...inal_paper_hint': None}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [Zinc12K] Extracted all models from Table_zinc for the
Zinc12K dataset. The proposed model OGE-Aug is tested with two different backbones (GINE and GPS).
[Alchemy] The table lists GIN with different Positional Encodings (PE). I have extracted each row as
a separate result. The proposed model uses GINE backbone with OGE-Aug. [PCQM-Contact] Extracted all
rows for PCQM-Contact. The 'PE' column indicates positional encoding types used for specific model
variants.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*