# Extraction: arXiv:2410.18676
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: MoSE
- Type: Other

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| none | 0.7149 | 0.0019 | Yes | this paper | Table 1 |
| PEG^LapEig | 0.7210 | 0.0046 | Yes | this paper | Table 1 |
| LapPE | 0.7231 | 0.0034 | Yes | this paper | Table 1 |
| SignNet^MLP | 0.7174 | 0.0060 | Yes | this paper | Table 1 |
| SignNet^DeepSets | 0.7237 | 0.0034 | Yes | this paper | Table 1 |
| RWSE | 0.7196 | 0.0040 | Yes | this paper | Table 1 |
| MoSE | 0.7350 | 0.0044 | No | this paper | Table 1 |
| GPS+LapPE | 0.7231 | 0.0034 | Yes | gps | Table 2 |
| GPS_small+MoSE_S | 0.7334 | 0.0050 | No | this paper | Table 2 |
| GPS_big+MoSE_S | 0.7500 | 0.0059 | No | this paper | Table 2 |
| GPS_small+MoSE_Omega | 0.7350 | 0.0044 | No | this paper | Table 2 |
| GPS_big+MoSE_Omega | 0.7473 | 0.0064 | No | this paper | Table 2 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| CRaW1 | 0.9794 | 0.0005 | Yes | this paper | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 1 |
| GPS(+LapPE) | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GPS+MoSE | 0.9813 | 0.0000 | No | this paper | Table 1 |

### PCQM4Mv2-subset — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| none | 0.1355 | 0.0035 | Yes | this paper | Table 1 |
| PEG^LapEig | 0.1209 | 0.0003 | Yes | this paper | Table 1 |
| LapPE | 0.1201 | 0.0003 | Yes | this paper | Table 1 |
| SignNet^MLP | 0.1158 | 0.0008 | Yes | this paper | Table 1 |
| SignNet^DeepSets | 0.1144 | 0.0002 | Yes | this paper | Table 1 |
| RWSE | 0.1159 | 0.0004 | Yes | this paper | Table 1 |
| MoSE | 0.1133 | 0.0014 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT+none | 0.4470 | 0.0170 | Yes | this paper | Table 1 |
| GT+RWSE | 0.6250 | 0.0120 | Yes | this paper | Table 1 |
| GT+MoSE_S | 0.6350 | 0.0110 | No | this paper | Table 1 |
| GT+MoSE_Omega | 0.6290 | 0.0110 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT+none | 0.4540 | 0.0270 | Yes | this paper | Table 1 |
| GT+RWSE | 0.3440 | 0.0090 | Yes | this paper | Table 1 |
| GT+MoSE_S | 0.3390 | 0.0070 | No | this paper | Table 1 |
| GT+MoSE_Omega | 0.3180 | 0.0100 | No | this paper | Table 1 |

### ZINC-12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| none | 0.1130 | 0.0070 | Yes | this paper | Table 1 |
| PEG | 0.1610 | 0.0060 | Yes | this paper | Table 1 |
| LapPE | 0.1160 | 0.0090 | Yes | this paper | Table 1 |
| SignNet MLP | 0.0900 | 0.0070 | Yes | this paper | Table 1 |
| SignNet DeepSets | 0.0790 | 0.0060 | Yes | this paper | Table 1 |
| RWSE | 0.0700 | 0.0020 | Yes | this paper | Table 1 |
| MoSE | 0.0620 | 0.0020 | No | this paper | Table 1 |
| MLP-E (none) | 0.6060 | 0.0020 | Yes | this paper | Table 2 |
| MLP-E (RWSE) | 0.3610 | 0.0100 | Yes | this paper | Table 2 |
| MLP-E (MoSE) | 0.3470 | 0.0030 | No | this paper | Table 2 |
| GIN-E (none) | 0.2430 | 0.0060 | Yes | this paper | Table 2 |
| GIN-E (RWSE) | 0.1220 | 0.0030 | Yes | this paper | Table 2 |
| GIN-E (MoSE) | 0.1180 | 0.0070 | No | this paper | Table 2 |
| GIN-E+VN (none) | 0.1510 | 0.0060 | Yes | this paper | Table 2 |
| GIN-E+VN (RWSE) | 0.0850 | 0.0030 | Yes | this paper | Table 2 |
| GIN-E+VN (MoSE) | 0.0680 | 0.0040 | No | this paper | Table 2 |
| GT-E (none) | 0.1950 | 0.0250 | Yes | this paper | Table 2 |
| GT-E (RWSE) | 0.1040 | 0.0250 | Yes | this paper | Table 2 |
| GT-E (MoSE) | 0.0890 | 0.0180 | No | this paper | Table 2 |
| GPS (none) | 0.1190 | 0.0110 | Yes | this paper | Table 2 |
| GPS (RWSE) | 0.0690 | 0.0010 | Yes | this paper | Table 2 |
| GPS (MoSE) | 0.0620 | 0.0020 | No | this paper | Table 2 |
| GSN | 0.1010 | 0.0100 | Yes | this paper | Table 3 |
| CIN | 0.0790 | 0.0060 | Yes | this paper | Table 3 |
| GPS | 0.0700 | 0.0020 | Yes | this paper | Table 3 |
| Subgraphormer+PE | 0.0630 | 0.0010 | Yes | this paper | Table 3 |
| GT-E | 0.1950 | 0.0250 | Yes | this paper | Table 3 |
| GRIT+RRWP | 0.0590 | 0.0020 | Yes | this paper | Table 3 |
| GRIT+MoSE | 0.0560 | 0.0010 | No | this paper | Table 3 |
| R-GCN (none) | 0.4130 | 0.0050 | Yes | this paper | Table 4 |
| R-GCN (RWSE) | 0.2070 | 0.0070 | Yes | this paper | Table 4 |
| R-GCN (MoSE) | 0.1970 | 0.0040 | No | this paper | Table 4 |
| R-GCN (RWSE+MoSE) | 0.1880 | 0.0050 | Yes | this paper | Table 4 |

## Baseline Models Identified

- **RWSE**
- **PEG**
- **LapPE**
- **SignNet**
- **GSN**
- **CIN**
- **GPS**
- **Subgraphormer**
- **GRIT**
- **none**
- **PEG^LapEig**
- **SignNet^MLP**
- **SignNet^DeepSets**
- **GPS+LapPE** (from: gps)
- **GIN**
- **GAT**
- **CRaW1**
- **EGT**
- **GPS(+LapPE)**
- **GT+none** (from: dwivedi2020generalization)
- **GT+RWSE**

## Extraction Notes

[ZINC-12K] Extracted results from Tables 1, 2, 3, and 4. Table 5 (ZINC without edge features) was
ignored as per the instruction to use the standard/default configuration (which typically includes
edge features for ZINC-12K in this context, and the paper explicitly labels the other as 'without
edge features'). [PCQM4Mv2-subset] Extracted only PCQM4Mv2-subset results as requested. The models
listed are different encoding types used within the GPS model framework. [CIFAR10] Normalized
accuracy percentages to [0, 1] range. Table 2 contains specific model size variants of the proposed
MoSE method. [QM9] failed: 1 validation error for ExtractionOutput   Input should be a valid
dictionary or instance of ExtractionOutput [type=model_type, input_value=[{'name': 'R-GIN',
'param...inal_paper_hint': None}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [MNIST] Extracted results from Table 1 as it
represents the standard 100K parameter comparison. Table 2 was skipped as it contains various
configuration variants (small/big, S/Omega) as per the prompt instructions to use only the
standard/default configuration. [Peptides-struct] Extracted only Peptides-struct as requested. MoSE
variants were mapped to GT+MoSE_S and GT+MoSE_Omega based on the subscripts S and Omega in the
table. [Peptides-func] Extracted only Peptides-func as requested. MoSE variants were mapped to
GT+MoSE_S and GT+MoSE_Omega based on the subscripts S and Omega in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*