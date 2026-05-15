# Extraction: arXiv:2312.01538
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GRED
- Type: GNN

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN* | 0.6860 | 0.0050 | Yes | Tonshoff 2023 | Table 1 |
| GINE* | 0.6621 | 0.0067 | Yes | Tonshoff 2023 | Table 1 |
| GatedGCN* | 0.6765 | 0.0047 | Yes | Tonshoff 2023 | Table 1 |
| PathNN | 0.6816 | 0.0026 | Yes | this paper | Table 1 |
| DRew | 0.6996 | 0.0076 | Yes | this paper | Table 1 |
| DRew+LapPE | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| Graph-MLPMixer | 0.6970 | 0.0080 | Yes | this paper | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| GRED (Ours) | 0.7085 | 0.0027 | No | this paper | Table 1 |
| GRED+LapPE | 0.7133 | 0.0011 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN* | 0.2460 | 0.0007 | Yes | Tonshoff 2023 | Table 1 |
| GINE* | 0.2473 | 0.0017 | Yes | Tonshoff 2023 | Table 1 |
| GatedGCN* | 0.2477 | 0.0009 | Yes | Tonshoff 2023 | Table 1 |
| PathNN | 0.2540 | 0.0046 | Yes | this paper | Table 1 |
| DRew | 0.2781 | 0.0028 | Yes | this paper | Table 1 |
| DRew+LapPE | 0.2536 | 0.0015 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| Graph-MLPMixer | 0.2475 | 0.0015 | Yes | this paper | Table 1 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| GRED (Ours) | 0.2503 | 0.0019 | No | this paper | Table 1 |
| GRED+LapPE | 0.2455 | 0.0013 | No | this paper | Table 1 |

### ZINC 12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2780 | 0.0030 | Yes | Kipf 2016 | Table 1 |
| GAT | 0.3840 | 0.0070 | Yes | Velickovic 2017 | Table 1 |
| GIN | 0.3870 | 0.0150 | Yes | Xu 2018 | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | Bresson 2017 | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | Corso 2020 | Table 1 |
| KP-GIN | 0.0930 | 0.0070 | Yes | Feng 2022 | Table 1 |
| PathNN | 0.0900 | 0.0040 | Yes | Michel 2023 | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | Kreuzer 2021 | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | Ying 2021 | Table 1 |
| K-subgraph SAT | 0.0940 | 0.0080 | Yes | Chen 2022 | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | Rampavsek 2022 | Table 1 |
| Graph MLP-Mixer | 0.0730 | 0.0010 | Yes | He 2023 | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | Ma 2023 | Table 1 |
| GRED | 0.0770 | 0.0020 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **GAT** (from: Velickovic 2017)
- **GIN** (from: Xu 2018)
- **GatedGCN** (from: Bresson 2017)
- **PNA** (from: Corso 2020)
- **KP-GIN** (from: Feng 2022)
- **PathNN** (from: Michel 2023)
- **SAN** (from: Kreuzer 2021)
- **Graphormer** (from: Ying 2021)
- **K-subgraph SAT** (from: Chen 2022)
- **GPS** (from: Rampavsek 2022)
- **Graph MLP-Mixer** (from: He 2023)
- **GRIT** (from: Ma 2023)
- **GINE** (from: Tonshoff 2023)
- **DRew** (from: this paper)
- **DRew+LapPE** (from: this paper)
- **SAN+LapPE** (from: this paper)
- **Graph-MLPMixer** (from: this paper)

## Extraction Notes

[MNIST] failed: 2 validation errors for ExtractionOutput results.5.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [CIFAR10] failed: 2 validation errors for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [PATTERN] failed: 1 validation error for
ExtractionOutput results.8.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [CLUSTER] failed: 1 validation error for
ExtractionOutput results.8.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ZINC 12K] Extracted all models from Table 1 for the
ZINC 12K dataset. The table caption specifies a parameter budget of approx 500k, but exact parameter
counts are not provided in the text or table, so params_millions is null. All values are Test MAE.
The proposed model is GRED. [Peptides-func] Extracted only Peptides-func AP results as requested.
Note that GRED+LapPE is a variant of the proposed model GRED, included in the table. The paper
mentions GRED outperforms all baselines except DRew+LapPE, but the table shows GRED+LapPE (0.7133)
is higher than DRew+LapPE (0.7150 is actually higher, wait: 0.7150 > 0.7133. The text says
'outperforms all baselines except DRew+LapPE'. This implies GRED (without LapPE) is the main result.
GRED+LapPE is an ablation/variant. I have included both as they are in the table. The primary
proposed model is GRED. [Peptides-struct] Extracted only Peptides-struct MAE results as requested.
Note that GRED+LapPE is a variant of the proposed model GRED, included in the table. The primary
proposed model is GRED. Baselines marked with * are from Tonshoff 2023. All values are Test MAE.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*