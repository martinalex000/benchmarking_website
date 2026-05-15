# Extraction: arXiv:2410.05593
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: MEDIUM

## Proposed Model: DMD-GNNs
- Type: GNN

## Results

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.0310 | 0.0160 | Yes | this paper | Table lrgb |
| GCN | 0.0790 | 0.0250 | Yes | this paper | Table lrgb |
| GPRGNN | 0.0440 | 0.0150 | Yes | this paper | Table lrgb |
| SGC | 0.0560 | 0.0110 | Yes | this paper | Table lrgb |
| DMD-GCN | 0.0810 | 0.0150 | No | this paper | Table lrgb |
| DMD-SGC | 0.0830 | 0.0120 | No | this paper | Table lrgb |
| DMD++ | 0.0910 | 0.0090 | No | this paper | Table lrgb |

### Chickenpox — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9240 | 0.0010 | Yes | this paper | Table stg_main_results |
| GCN | 0.9230 | 0.0010 | Yes | this paper | Table stg_main_results |
| GAT | 0.9240 | 0.0020 | Yes | this paper | Table stg_main_results |
| GAT-KNN | 0.9260 | 0.0040 | Yes | this paper | Table stg_main_results |
| GCN-KNN | 0.9260 | 0.0040 | Yes | this paper | Table stg_main_results |
| ChebNet | 0.9160 | 0.0140 | Yes | this paper | Table stg_main_results |
| Grand++ | 0.9910 | 0.0090 | Yes | this paper | Table stg_main_results |
| Framelet | 0.9230 | 0.0300 | Yes | this paper | Table stg_main_results |
| DMD-GCN | 0.9780 | 0.0930 | Yes | this paper | Table stg_main_results |
| DMD-SGC | 0.9350 | 0.0140 | Yes | this paper | Table stg_main_results |
| DMD-ACMP | 0.9240 | 0.0010 | Yes | this paper | Table stg_main_results |
| DMD++ | 0.9100 | 0.0020 | No | this paper | Table stg_main_results |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5910 | 0.0050 | Yes | this paper | Table 1 |
| GCN | 0.7090 | 0.0050 | Yes | this paper | Table 1 |
| GAT | 0.7200 | 0.0070 | Yes | this paper | Table 1 |
| GPRGNN | 0.7590 | 0.0120 | Yes | this paper | Table 1 |
| APPNP | 0.7590 | 0.0060 | Yes | this paper | Table 1 |
| H2GCN | 0.7310 | 0.0040 | Yes | this paper | Table 1 |
| SAGE | 0.6720 | 0.0100 | Yes | this paper | Table 1 |
| GRAND++ | 0.7080 | 0.0110 | Yes | this paper | Table 1 |
| Framelets | 0.7100 | 0.0060 | Yes | this paper | Table 1 |
| DMD-GCN | 0.7140 | 0.0260 | No | this paper | Table 1 |
| DMD-SGC | 0.7260 | 0.0080 | No | this paper | Table 1 |
| DMD++ | 0.7320 | 0.0040 | No | this paper | Table 1 |
| DMD-ACMP | 0.7300 | 0.0210 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5510 | 0.0130 | Yes | this paper | Table 1 |
| GCN | 0.8150 | 0.0050 | Yes | this paper | Table 1 |
| GAT | 0.8300 | 0.0070 | Yes | this paper | Table 1 |
| GPRGNN | 0.8380 | 0.0090 | Yes | this paper | Table 1 |
| APPNP | 0.8350 | 0.0070 | Yes | this paper | Table 1 |
| H2GCN | 0.8340 | 0.0050 | Yes | this paper | Table 1 |
| SAGE | 0.7450 | 0.0080 | Yes | this paper | Table 1 |
| GRAND++ | 0.8290 | 0.0140 | Yes | this paper | Table 1 |
| Framelets | 0.8330 | 0.0050 | Yes | this paper | Table 1 |
| DMD-GCN | 0.8260 | 0.0070 | No | this paper | Table 1 |
| DMD-SGC | 0.8410 | 0.0040 | No | this paper | Table 1 |
| DMD++ | 0.8230 | 0.0030 | No | this paper | Table 1 |
| DMD-ACMP | 0.8290 | 0.0090 | No | this paper | Table 1 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9130 | 0.0070 | Yes | this paper | Table 1 |
| GCN | 0.6650 | 0.1380 | Yes | this paper | Table 1 |
| GAT | 0.7600 | 0.0100 | Yes | this paper | Table 1 |
| GPRGNN | 0.8500 | 0.0520 | Yes | this paper | Table 1 |
| APPNP | 0.8980 | 0.0060 | Yes | this paper | Table 1 |
| H2GCN | 0.8510 | 0.0640 | Yes | this paper | Table 1 |
| SAGE | 0.7140 | 0.0120 | Yes | this paper | Table 1 |
| GRAND++ | 0.7560 | 0.0320 | Yes | this paper | Table 1 |
| Framelets | 0.7260 | 0.0030 | Yes | this paper | Table 1 |
| DMD-GCN | 0.8360 | 0.0310 | Yes | this paper | Table 1 |
| DMD-SGC | 0.8000 | 0.0190 | Yes | this paper | Table 1 |
| DMD++ | 0.9140 | 0.0170 | No | this paper | Table 1 |
| DMD-ACMP | 0.8810 | 0.0240 | Yes | this paper | Table 1 |

### Covid — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9560 | 0.0340 | Yes | this paper | Table stg_main_results |
| GCN | 0.9560 | 0.0290 | Yes | this paper | Table stg_main_results |
| GAT | 1.0520 | 0.0810 | Yes | this paper | Table stg_main_results |
| GAT-KNN | 0.8610 | 0.0450 | Yes | this paper | Table stg_main_results |
| GCN-KNN | 1.4750 | 0.0280 | Yes | this paper | Table stg_main_results |
| ChebNet | 0.9910 | 0.0780 | Yes | this paper | Table stg_main_results |
| Grand++ | 1.2710 | 0.0730 | Yes | this paper | Table stg_main_results |
| Framelet | 0.9380 | 0.0810 | Yes | this paper | Table stg_main_results |
| DMD-GCN | 0.7600 | 0.0250 | No | this paper | Table stg_main_results |
| DMD-SGC | 0.8050 | 0.0670 | No | this paper | Table stg_main_results |
| DMD-ACMP | 0.8090 | 0.0110 | No | this paper | Table stg_main_results |
| DMD++ | 0.7840 | 0.0130 | No | this paper | Table stg_main_results |

### OGB-arXiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5500 | 0.0030 | Yes | this paper | Table 1 |
| GCN | 0.7270 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.7200 | 0.0050 | Yes | this paper | Table 1 |
| GPRGNN | 0.7040 | 0.0150 | Yes | this paper | Table 1 |
| APPNP | 0.7030 | 0.0250 | Yes | this paper | Table 1 |
| H2GCN | 0.7280 | 0.0240 | Yes | this paper | Table 1 |
| SAGE | 0.7060 | 0.0160 | Yes | this paper | Table 1 |
| GRAND++ | 0.7410 | 0.0230 | Yes | this paper | Table 1 |
| Framelets | 0.7190 | 0.0020 | Yes | this paper | Table 1 |
| DMD-GCN | 0.7390 | 0.0280 | No | this paper | Table 1 |
| DMD-SGC | 0.7410 | 0.0090 | No | this paper | Table 1 |
| DMD++ | 0.7440 | 0.0150 | No | this paper | Table 1 |
| DMD-ACMP | 0.7550 | 0.0080 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.1140 | 0.0230 | Yes | this paper | Table 1 |
| GCN | 0.2380 | 0.0160 | Yes | this paper | Table 1 |
| GPRGNN | 0.1520 | 0.0240 | Yes | this paper | Table 1 |
| SGC | 0.2160 | 0.0390 | Yes | this paper | Table 1 |
| DMD-GCN | 0.2430 | 0.0140 | No | this paper | Table 1 |
| DMD-SGC | 0.2170 | 0.0360 | No | this paper | Table 1 |
| DMD++ | 0.2410 | 0.0170 | No | this paper | Table 1 |

### Pubmed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.7140 | 0.0040 | Yes | this paper | Table 1 |
| GCN | 0.7900 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.7850 | 0.0030 | Yes | this paper | Table 1 |
| GPRGNN | 0.7980 | 0.0080 | Yes | this paper | Table 1 |
| APPNP | 0.7900 | 0.0030 | Yes | this paper | Table 1 |
| H2GCN | 0.7920 | 0.0030 | Yes | this paper | Table 1 |
| SAGE | 0.7680 | 0.0060 | Yes | this paper | Table 1 |
| GRAND++ | 0.7920 | 0.0150 | Yes | this paper | Table 1 |
| Framelets | 0.7940 | 0.0040 | Yes | this paper | Table 1 |
| DMD-GCN | 0.7930 | 0.0090 | No | this paper | Table 1 |
| DMD-SGC | 0.7940 | 0.0140 | No | this paper | Table 1 |
| DMD++ | 0.7990 | 0.0070 | No | this paper | Table 1 |
| DMD-ACMP | 0.8120 | 0.0150 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9230 | 0.0070 | Yes | this paper | Table 1 |
| GCN | 0.7570 | 0.0100 | Yes | this paper | Table 1 |
| GAT | 0.7880 | 0.0090 | Yes | this paper | Table 1 |
| GPRGNN | 0.7590 | 0.0620 | Yes | this paper | Table 1 |
| APPNP | 0.8390 | 0.0070 | Yes | this paper | Table 1 |
| H2GCN | 0.8590 | 0.0460 | Yes | this paper | Table 1 |
| SAGE | 0.7930 | 0.0120 | Yes | this paper | Table 1 |
| GRAND++ | 0.8140 | 0.0350 | Yes | this paper | Table 1 |
| Framelets | 0.8230 | 0.0250 | Yes | this paper | Table 1 |
| DMD-GCN | 0.8420 | 0.0260 | Yes | this paper | Table 1 |
| DMD-SGC | 0.8120 | 0.0250 | Yes | this paper | Table 1 |
| DMD++ | 0.9260 | 0.0340 | No | this paper | Table 1 |
| DMD-ACMP | 0.8940 | 0.0380 | Yes | this paper | Table 1 |

### WikiMath — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 1.0730 | 0.0420 | Yes | this paper | Table stg_main_results |
| GCN | 1.2920 | 0.1250 | Yes | this paper | Table stg_main_results |
| GAT | 1.3390 | 0.0730 | Yes | this paper | Table stg_main_results |
| GAT-KNN | 0.8260 | 0.0700 | Yes | this paper | Table stg_main_results |
| GCN-KNN | 1.0230 | 0.0580 | Yes | this paper | Table stg_main_results |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9180 | 0.0310 | Yes | this paper | Table 1 |
| GCN | 0.6670 | 0.0140 | Yes | this paper | Table 1 |
| GAT | 0.7100 | 0.0460 | Yes | this paper | Table 1 |
| GPRGNN | 0.8990 | 0.0300 | Yes | this paper | Table 1 |
| APPNP | 0.9010 | 0.0350 | Yes | this paper | Table 1 |
| H2GCN | 0.8790 | 0.0420 | Yes | this paper | Table 1 |
| SAGE | 0.6480 | 0.0520 | Yes | this paper | Table 1 |
| GRAND++ | 0.8860 | 0.0210 | Yes | this paper | Table 1 |
| Framelets | 0.8890 | 0.0320 | Yes | this paper | Table 1 |
| DMD-GCN | 0.8520 | 0.0210 | Yes | this paper | Table 1 |
| DMD-SGC | 0.8300 | 0.0180 | Yes | this paper | Table 1 |
| DMD++ | 0.9190 | 0.0260 | No | this paper | Table 1 |
| DMD-ACMP | 0.8940 | 0.0220 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **MLP**
- **GCN**
- **GAT**
- **GPRGNN**
- **APPNP**
- **H2GCN**
- **SAGE**
- **GRAND++**
- **Framelets**
- **DMD-GCN**
- **DMD-SGC**
- **DMD-ACMP**
- **SGC**
- **GAT-KNN**
- **GCN-KNN**
- **ChebNet**
- **Framelet**

## Extraction Notes

[Cora] Extracted only Cora dataset results as requested. Normalized percentages to [0, 1] range.
[Citeseer] Extracted only Citeseer results as requested. Normalized percentages to [0, 1] range.
[Pubmed] Extracted only Pubmed results as requested. Normalized percentages to [0, 1] range. [Texas]
Extracted only the Texas dataset column as requested. Normalized percentages to [0, 1] range.
[Wisconsin] Extracted only the Wisconsin column as requested. Normalized percentages to [0, 1]
range. [Cornell] Extracted only the Cornell column as requested. Normalized percentages to decimals.
[OGB-arXiv] Extracted only OGB-arXiv results as requested. Normalized percentages to [0, 1] range.
[COCO-SP] Extracted only COCO-SP results as requested. Macro-F1 was normalized to F1. [PascalVOC-SP]
Extracted only PascalVOC-SP results from Table 1 as requested. Macro-F1 was normalized to F1.
[Chickenpox] Extracted results only for the Chickenpox dataset from Table stg_main_results as
requested. All models in that row were included. [Covid] The primary metric requested was RMSE, but
the table explicitly reports MSE. Extracted MSE as it is the only available error metric for the
Covid dataset in the provided text. [Wikimath] The table for WikiMath was truncated in the provided
text. Only the first 5 models (MLP, GCN, GAT, GAT-KNN, GCN-KNN) had their values listed before the
text ended. Results for ChebNet, Grand++, Framelet, and the DMD variants for WikiMath are missing
from the input.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*