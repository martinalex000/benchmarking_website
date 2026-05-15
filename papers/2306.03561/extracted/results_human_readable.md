# Extraction: arXiv:2306.03561
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: CIN++ (0.5M params)
- Type: GNN

## Results

### MOLHIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7606 | 0.0097 | Yes | Kipf 2017 | Table 1 |
| GIN | 0.7707 | 0.0149 | Yes | Xu et al. | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | Corso 2020 | Table 1 |
| DGN | 0.7970 | 0.0097 | Yes | Beaini 2020 | Table 1 |
| HIMP | 0.7880 | 0.0082 | Yes | Fey 2020 | Table 1 |
| GSN | 0.7799 | 0.0100 | Yes | Bouritsas 2020 | Table 1 |
| CIN-small | 0.8055 | 0.0104 | Yes | Bodnar et al. | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | Bodnar et al. | Table 1 |
| CIN++-small (ours) | 0.8026 | 0.0102 | Yes | this paper | Table 1 |
| CIN++ (ours) | 0.8063 | 0.0094 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWK | 0.7920 | 0.0210 | Yes | Gartner 2003 | Table 1 |
| GK (k=3) | 0.8140 | 0.0170 | Yes | Shervashidze 2009 | Table 1 |
| PK | 0.7600 | 0.0270 | Yes | Neumann 2016 | Table 1 |
| WL kernel | 0.9040 | 0.0570 | Yes | Shervashidze 2011 | Table 1 |
| DGCNN | 0.8580 | 0.0180 | Yes | Zhang 2018 | Table 1 |
| IGN | 0.8390 | 0.1300 | Yes | Maron 2019 | Table 1 |
| GIN | 0.8940 | 0.0560 | Yes | this paper | Table 1 |
| PPGNs | 0.9060 | 0.0870 | Yes | Maron 2019 | Table 1 |
| Natural GN | 0.8940 | 0.0160 | Yes | De 2020 | Table 1 |
| GSN | 0.9220 | 0.0750 | Yes | Bouritsas 2020 | Table 1 |
| CIN | 0.9270 | 0.0610 | Yes | Bodnar et al. | Table 1 |
| CAN | 0.9410 | 0.0480 | Yes | Giusti 2022 | Table 1 |
| CIN++ (Ours) | 0.9440 | 0.0370 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWK | 0.5960 | 0.0010 | Yes | Gartner 2003 | Table 1 |
| GK (k=3) | 0.7140 | 0.0030 | Yes | Shervashidze 2009 | Table 1 |
| PK | 0.7370 | 0.0070 | Yes | Neumann 2016 | Table 1 |
| WL kernel | 0.7500 | 0.0310 | Yes | Shervashidze 2011 | Table 1 |
| DCNN | 0.6130 | 0.0160 | Yes | DCNN 2016 | Table 1 |
| DGCNN | 0.7550 | 0.0090 | Yes | Zhang 2018 | Table 1 |
| IGN | 0.7660 | 0.0550 | Yes | Maron 2019 | Table 1 |
| GIN | 0.7620 | 0.0280 | Yes | GIN | Table 1 |
| PPGNs | 0.7720 | 0.0470 | Yes | Maron 2019 | Table 1 |
| Natural GN | 0.7170 | 0.0100 | Yes | De 2020 | Table 1 |
| GSN | 0.7660 | 0.0500 | Yes | Bouritsas 2020 | Table 1 |
| SIN | 0.7640 | 0.0330 | Yes | Bodnar 2021 | Table 1 |
| CIN | 0.7700 | 0.0430 | Yes | Bodnar CWN | Table 1 |
| CAN | 0.7820 | 0.0200 | Yes | Giusti 2022 | Table 1 |
| CIN++ (Ours) | 0.8050 | 0.0390 | No | this paper | Table 1 |

### PTC_MR — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RWK | 0.5590 | 0.0030 | Yes | Gartner 2003 | Table 1 |
| GK (k=3) | 0.5570 | 0.0050 | Yes | Shervashidze 2009 | Table 1 |
| PK | 0.5950 | 0.0240 | Yes | Neumann 2016 | Table 1 |
| WL kernel | 0.5990 | 0.0430 | Yes | Shervashidze 2011 | Table 1 |
| DGCNN | 0.5860 | 0.0250 | Yes | Zhang 2018 | Table 1 |
| IGN | 0.5850 | 0.0690 | Yes | Maron 2019 | Table 1 |
| GIN | 0.6460 | 0.0700 | Yes | this paper | Table 1 |
| PPGNs | 0.6620 | 0.0660 | Yes | Maron 2019 | Table 1 |
| Natural GN | 0.6680 | 0.0170 | Yes | De 2020 | Table 1 |
| GSN | 0.6820 | 0.0720 | Yes | Bouritsas 2020 | Table 1 |
| CIN | 0.6820 | 0.0560 | Yes | Bodnar CWN | Table 1 |
| CAN | 0.7280 | 0.0830 | Yes | Giusti 2022 | Table 1 |
| CIN++ (Ours) | 0.7320 | 0.0640 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.4060 | 0.0021 | Yes | this paper | Table 1 |
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| CIN++ | 0.6569 | 0.0117 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.4351 | 0.0008 | Yes | this paper | Table 1 |
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | this paper | Table 1 |
| CIN++ | 0.2523 | 0.0013 | No | this paper | Table 1 |

## Baseline Models Identified

- **MLP**
- **GCN**
- **GCNII**
- **GINE**
- **GatedGCN**
- **GatedGCN+RWSE**
- **Transformer+LapPE**
- **SAN+LapPE**
- **SAN+RWSE**
- **GAT** (from: Veličković 2017)
- **GIN** (from: Xu et al.)
- **PNA** (from: Corso 2020)
- **DGN** (from: Beaini 2020)
- **HIMP** (from: Fey 2020)
- **GSN** (from: Bouritsas 2020)
- **CIN-small** (from: Bodnar et al.)
- **CIN** (from: Bodnar et al.)
- **RWK** (from: Gartner 2003)
- **GK (k=3)** (from: Shervashidze 2009)
- **PK** (from: Neumann 2016)
- **WL kernel** (from: Shervashidze 2011)
- **DCNN** (from: 2016)
- **DGCNN** (from: Zhang 2018)
- **IGN** (from: Maron 2019)
- **PPGNs** (from: Maron 2019)
- **Natural GN** (from: De 2020)
- **SIN** (from: Bodnar 2021)
- **CAN** (from: Giusti 2022)

## Extraction Notes

[ZINC] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or
instance of ExtractionOutput [type=model_type, input_value=[{'name': 'GIN', 'params_...er_hint':
'this paper'}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [Peptides-func] Extracted only Peptides-func Test AP
results as requested. All values are normalized to [0,1]. The proposed model is CIN++. Baselines
include standard GNNs and Graph Transformers with positional encodings. [Peptides-struct] Extracted
only Peptides-struct Test MAE results as requested. The table provides Train MAE and Test MAE; only
Test MAE was extracted. All values are normalized correctly (MAE is not a percentage). The proposed
model CIN++ achieves the best score (indicated by gold circle/first rank). [MOLHIV] Extracted only
MOLHIV results as requested. Values were converted from percentages (e.g., 76.06) to decimals
(0.7606) for ROC-AUC. Standard deviations were parsed from the 'mean ± std' format. GAT, GatedGCN,
and PNA had N/A for MOLHIV and were skipped. [MUTAG] Extracted only MUTAG results as requested. All
values are percentages converted to [0,1] range. Standard deviations are parsed from the ± notation.
DCNN and SIN have N/A for MUTAG and were excluded. [PTC_MR] Extracted only PTC_MR results as
requested. All values are percentages from the table, converted to [0,1] range. Standard deviations
parsed from 'mean ± std' format. DCNN and SIN have N/A for PTC_MR and were excluded. [PROTEINS]
Extracted all rows for the PROTEINS dataset from Table 1. Values are percentages from the table,
converted to [0,1] range as per rules. Standard deviation is parsed from the 'mean ± std' format.
All models are treated as baselines except CIN++ which is marked as proposed. [NCI1] failed: 1
validation error for ExtractionOutput results.0.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [NCI109] failed: 9 validation errors for
ExtractionOutput results.0.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.3.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.9.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*