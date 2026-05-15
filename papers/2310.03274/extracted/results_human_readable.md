# Extraction: arXiv:2310.03274
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GraphFP
- Type: GNN

## Results

### BACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.7930 | 0.0160 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.7960 | 0.0120 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.7300 | 0.0330 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.7930 | 0.0110 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.7790 | 0.0320 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.8020 | 0.0350 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.7540 | 0.0140 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.7730 | 0.0050 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.7550 | 0.0130 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.7680 | 0.0110 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.8210 | 0.0270 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.7970 | 0.0130 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.7420 | 0.0280 | No | this paper | Table 1 |
| GraphFP_C | 0.7820 | 0.0340 | No | this paper | Table 1 |
| GraphFP_P | 0.8070 | 0.0480 | No | this paper | Table 1 |
| GraphFP_CP | 0.8130 | 0.0220 | No | this paper | Table 1 |
| GraphFP_CF | 0.7710 | 0.0210 | No | this paper | Table 1 |
| GraphFP_CPF | 0.8050 | 0.0180 | No | this paper | Table 1 |
| GIN | 0.8250 | 0.0190 | Yes | this paper | Table 2 |
| GCN | 0.7620 | 0.0210 | Yes | this paper | Table 2 |
| GraphSage | 0.7800 | 0.0360 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.8250 | 0.0190 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.8320 | 0.0140 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.8130 | 0.0220 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.8210 | 0.0220 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.8190 | 0.0130 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.8050 | 0.0180 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.7990 | 0.0100 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.7820 | 0.0100 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.7880 | 0.0280 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.8010 | 0.0120 | No | this paper | Table 3 |
| GIN_C, Vocab=200 | 0.7940 | 0.0160 | No | this paper | Table 4 |
| GIN_C, Vocab=400 | 0.7750 | 0.0250 | No | this paper | Table 4 |
| GIN_C, Vocab=800 | 0.7820 | 0.0340 | No | this paper | Table 4 |
| GIN_C, Vocab=1600 | 0.7900 | 0.0430 | No | this paper | Table 4 |
| GIN_C, Vocab=3200 | 0.7940 | 0.0450 | No | this paper | Table 4 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.6430 | 0.0280 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.6800 | 0.0200 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.6690 | 0.0310 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.6990 | 0.0210 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.6450 | 0.0140 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.6780 | 0.0190 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.6970 | 0.0070 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.7020 | 0.0100 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.7140 | 0.0090 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.6850 | 0.0020 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.6890 | 0.0250 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.7150 | 0.0090 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.7020 | 0.0170 | No | this paper | Table 1 |
| GraphFP_C | 0.7150 | 0.0160 | No | this paper | Table 1 |
| GraphFP_P | 0.6820 | 0.0120 | No | this paper | Table 1 |
| GraphFP_CP | 0.7130 | 0.0170 | No | this paper | Table 1 |
| GraphFP_CF | 0.7010 | 0.0180 | No | this paper | Table 1 |
| GraphFP_CPF | 0.7200 | 0.0170 | No | this paper | Table 1 |
| GIN | 0.7130 | 0.0080 | Yes | this paper | Table 2 |
| GCN | 0.7050 | 0.0120 | Yes | this paper | Table 2 |
| GraphSage | 0.7230 | 0.0150 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.7130 | 0.0080 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.7080 | 0.0190 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.7130 | 0.0170 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.7010 | 0.0230 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.7060 | 0.0110 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.7200 | 0.0170 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.6940 | 0.0130 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.7000 | 0.0160 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.7170 | 0.0090 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.7030 | 0.0090 | No | this paper | Table 3 |
| GIN_C (Vocab 200) | 0.6980 | 0.0150 | Yes | this paper | Table 4 |
| GIN_C (Vocab 400) | 0.7160 | 0.0140 | Yes | this paper | Table 4 |
| GIN_C (Vocab 800) | 0.7150 | 0.0160 | Yes | this paper | Table 4 |
| GIN_C (Vocab 1600) | 0.7110 | 0.0160 | Yes | this paper | Table 4 |
| GIN_C (Vocab 3200) | 0.7130 | 0.0080 | Yes | this paper | Table 4 |

### ClinTox — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.7180 | 0.0410 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.6590 | 0.0380 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.7770 | 0.0270 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.6060 | 0.0520 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.5830 | 0.0520 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.6530 | 0.0320 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.7600 | 0.0270 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.8130 | 0.0250 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.8100 | 0.0160 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.7900 | 0.0250 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.6750 | 0.0550 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.7770 | 0.0450 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.7590 | 0.0560 | No | this paper | Table 1 |
| GraphFP_C | 0.7860 | 0.0270 | No | this paper | Table 1 |
| GraphFP_P | 0.5380 | 0.0380 | No | this paper | Table 1 |
| GraphFP_CP | 0.7370 | 0.0390 | No | this paper | Table 1 |
| GraphFP_CF | 0.8770 | 0.0580 | No | this paper | Table 1 |
| GraphFP_CPF | 0.8470 | 0.0580 | No | this paper | Table 1 |
| GIN | 0.6320 | 0.0100 | Yes | this paper | Table 2 |
| GCN | 0.7810 | 0.0580 | Yes | this paper | Table 2 |
| GraphSage | 0.6960 | 0.0310 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.6320 | 0.0100 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.6470 | 0.0790 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.7370 | 0.0390 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.6010 | 0.0670 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.6570 | 0.0420 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.8470 | 0.0880 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.7690 | 0.0320 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.8300 | 0.0560 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.8300 | 0.0690 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.7930 | 0.0310 | No | this paper | Table 3 |
| GIN_C, Vocab=200 | 0.7480 | 0.0430 | No | this paper | Table 4 |
| GIN_C, Vocab=400 | 0.7520 | 0.0660 | No | this paper | Table 4 |
| GIN_C, Vocab=800 | 0.7860 | 0.0270 | No | this paper | Table 4 |
| GIN_C, Vocab=1600 | 0.7640 | 0.0460 | No | this paper | Table 4 |
| GIN_C, Vocab=3200 | 0.7550 | 0.0590 | No | this paper | Table 4 |

### HIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.7720 | 0.0110 | Yes | hu2020pretraining | Table 1 |
| ContextPred | 0.7730 | 0.0100 | Yes | hu2020pretraining | Table 1 |
| G-Motif | 0.7380 | 0.0120 | Yes | rong2020grover | Table 1 |
| G-Contextual | 0.7630 | 0.0150 | Yes | rong2020grover | Table 1 |
| GPT-GNN | 0.6520 | 0.0210 | Yes | hu2020gpt | Table 1 |
| GraphLoG | 0.7370 | 0.0090 | Yes | xu21graphlog | Table 1 |
| GraphCL | 0.7850 | 0.0120 | Yes | You2020GraphCL | Table 1 |
| JOAO | 0.7670 | 0.0120 | Yes | pmlr-v139-you21a | Table 1 |
| JOAOv2 | 0.7750 | 0.0120 | Yes | pmlr-v139-you21a | Table 1 |
| GraphMVP | 0.7480 | 0.0140 | Yes | liu2022pretraining | Table 1 |
| MGSSL | 0.7570 | 0.0130 | Yes | zhang_mgssl | Table 1 |
| GraphFP-JT$_{C}$ | 0.7560 | 0.0100 | No | this paper | Table 1 |
| GraphFP-JT$_{CF}$ | 0.7300 | 0.0190 | No | this paper | Table 1 |
| GraphFP$_{C}$ | 0.7630 | 0.0100 | No | this paper | Table 1 |
| GraphFP$_{P}$ | 0.7670 | 0.0100 | No | this paper | Table 1 |
| GraphFP$_{CP}$ | 0.7630 | 0.0100 | No | this paper | Table 1 |
| GraphFP$_{CF}$ | 0.7610 | 0.0200 | No | this paper | Table 1 |
| GraphFP$_{CPF}$ | 0.7800 | 0.0150 | No | this paper | Table 1 |
| GIN | 0.7610 | 0.0140 | Yes | this paper | Table 2 |
| GCN | 0.7460 | 0.0090 | Yes | this paper | Table 2 |
| GraphSage | 0.7710 | 0.0110 | Yes | this paper | Table 2 |
| CP, \(\alpha = 0.1\) | 0.7610 | 0.0140 | No | this paper | Table 3 |
| CP, \(\alpha = 0.2\) | 0.7600 | 0.0110 | No | this paper | Table 3 |
| CP, \(\alpha = 0.3\) | 0.7630 | 0.0100 | No | this paper | Table 3 |
| CP, \(\alpha = 0.4\) | 0.7570 | 0.0100 | No | this paper | Table 3 |
| CP, \(\alpha = 0.5\) | 0.7560 | 0.0110 | No | this paper | Table 3 |
| CPF, \(\alpha = 0.1\) | 0.7800 | 0.0150 | No | this paper | Table 3 |
| CPF, \(\alpha = 0.2\) | 0.7760 | 0.0130 | No | this paper | Table 3 |
| CPF, \(\alpha = 0.3\) | 0.7760 | 0.0120 | No | this paper | Table 3 |
| CPF, \(\alpha = 0.4\) | 0.7770 | 0.0210 | No | this paper | Table 3 |
| CPF, \(\alpha = 0.5\) | 0.7670 | 0.0130 | No | this paper | Table 3 |
| GIN$_{C}$ (Vocab 200) | 0.7690 | 0.0100 | Yes | this paper | Table 4 |
| GIN$_{C}$ (Vocab 400) | 0.7590 | 0.0100 | Yes | this paper | Table 4 |
| GIN$_{C}$ (Vocab 800) | 0.7630 | 0.0100 | Yes | this paper | Table 4 |
| GIN$_{C}$ (Vocab 1600) | 0.7530 | 0.0160 | Yes | this paper | Table 4 |
| GIN$_{C}$ (Vocab 3200) | 0.7510 | 0.0130 | Yes | this paper | Table 4 |

### MUV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.7470 | 0.0140 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.7580 | 0.0170 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.7300 | 0.0180 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.7210 | 0.0070 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.7590 | 0.0230 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.7360 | 0.0120 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.6980 | 0.0270 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.7170 | 0.0140 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.7370 | 0.0100 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.7500 | 0.0140 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.7320 | 0.0190 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.7600 | 0.0220 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.7390 | 0.0130 | No | this paper | Table 1 |
| GraphFP_C | 0.7720 | 0.0150 | No | this paper | Table 1 |
| GraphFP_P | 0.7450 | 0.0210 | No | this paper | Table 1 |
| GraphFP_CP | 0.7660 | 0.0180 | No | this paper | Table 1 |
| GraphFP_CF | 0.7450 | 0.0180 | No | this paper | Table 1 |
| GraphFP_CPF | 0.7540 | 0.0190 | No | this paper | Table 1 |
| GIN | 0.7620 | 0.0200 | Yes | this paper | Table 2 |
| GCN | 0.7780 | 0.0180 | Yes | this paper | Table 2 |
| GraphSage | 0.7730 | 0.0130 | Yes | this paper | Table 2 |
| CP, alpha = 0.1 | 0.7620 | 0.0200 | No | this paper | Table 3 |
| CP, alpha = 0.2 | 0.7650 | 0.0120 | No | this paper | Table 3 |
| CP, alpha = 0.3 | 0.7660 | 0.0180 | No | this paper | Table 3 |
| CP, alpha = 0.4 | 0.7560 | 0.0200 | No | this paper | Table 3 |
| CP, alpha = 0.5 | 0.7410 | 0.0240 | No | this paper | Table 3 |
| CPF, alpha = 0.1 | 0.7540 | 0.0190 | No | this paper | Table 3 |
| CPF, alpha = 0.2 | 0.7300 | 0.0420 | No | this paper | Table 3 |
| CPF, alpha = 0.3 | 0.7420 | 0.0270 | No | this paper | Table 3 |
| CPF, alpha = 0.4 | 0.7330 | 0.0300 | No | this paper | Table 3 |
| CPF, alpha = 0.5 | 0.7340 | 0.0280 | No | this paper | Table 3 |
| GIN_C (Vocab 200) | 0.7490 | 0.0180 | No | this paper | Table 4 |
| GIN_C (Vocab 400) | 0.7570 | 0.0250 | No | this paper | Table 4 |
| GIN_C (Vocab 800) | 0.7720 | 0.0150 | No | this paper | Table 4 |
| GIN_C (Vocab 1600) | 0.7610 | 0.0210 | No | this paper | Table 4 |
| GIN_C (Vocab 3200) | 0.7710 | 0.0190 | No | this paper | Table 4 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCNII | 0.5543 | 0.0078 | Yes | this paper | Table 1 |
| GIN | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| GraphFP_CF | 0.6267 | 0.0073 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCNII | 0.3471 | 0.0010 | Yes | this paper | Table 1 |
| GIN | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| GraphFP_CF | 0.3137 | 0.0019 | No | this paper | Table 1 |

### SIDER — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.6100 | 0.0070 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.6090 | 0.0060 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.6100 | 0.0150 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.5870 | 0.0100 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.5810 | 0.0030 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.5950 | 0.0150 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.6050 | 0.0090 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.6000 | 0.0080 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.6050 | 0.0070 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.6230 | 0.0160 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.5770 | 0.0070 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.6200 | 0.0100 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.5930 | 0.0130 | No | this paper | Table 1 |
| GraphFP_C | 0.6140 | 0.0090 | No | this paper | Table 1 |
| GraphFP_P | 0.5930 | 0.0100 | No | this paper | Table 1 |
| GraphFP_CP | 0.6130 | 0.0060 | No | this paper | Table 1 |
| GraphFP_CF | 0.6470 | 0.0100 | No | this paper | Table 1 |
| GraphFP_CPF | 0.6360 | 0.0120 | No | this paper | Table 1 |
| GIN | 0.6130 | 0.0040 | Yes | this paper | Table 2 |
| GCN | 0.6150 | 0.0080 | Yes | this paper | Table 2 |
| GraphSage | 0.6120 | 0.0080 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.6130 | 0.0040 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.6210 | 0.0050 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.6130 | 0.0060 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.6120 | 0.0060 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.5920 | 0.0090 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.6360 | 0.0120 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.6330 | 0.0090 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.6260 | 0.0090 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.6350 | 0.0080 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.6270 | 0.0090 | No | this paper | Table 3 |
| GIN_C, Vocab=200 | 0.6130 | 0.0070 | No | this paper | Table 4 |
| GIN_C, Vocab=400 | 0.6130 | 0.0070 | No | this paper | Table 4 |
| GIN_C, Vocab=800 | 0.6140 | 0.0090 | No | this paper | Table 4 |
| GIN_C, Vocab=1600 | 0.6040 | 0.0050 | No | this paper | Table 4 |
| GIN_C, Vocab=3200 | 0.6060 | 0.0050 | No | this paper | Table 4 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.7670 | 0.0040 | Yes | Hu et al. 2020 | Table 1 |
| ContextPred | 0.7570 | 0.0070 | Yes | Hu et al. 2020 | Table 1 |
| G-Motif | 0.7360 | 0.0070 | Yes | Rong et al. 2020 | Table 1 |
| G-Contextual | 0.7500 | 0.0060 | Yes | Rong et al. 2020 | Table 1 |
| GPT-GNN | 0.7490 | 0.0030 | Yes | Hu et al. 2020 | Table 1 |
| GraphLoG | 0.7510 | 0.0100 | Yes | Xu et al. 2021 | Table 1 |
| GraphCL | 0.7390 | 0.0070 | Yes | You et al. 2020 | Table 1 |
| JOAO | 0.7500 | 0.0030 | Yes | You et al. 2021 | Table 1 |
| JOAOv2 | 0.7430 | 0.0060 | Yes | You et al. 2021 | Table 1 |
| GraphMVP | 0.7450 | 0.0040 | Yes | Liu et al. 2022 | Table 1 |
| MGSSL | 0.7490 | 0.0060 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.7520 | 0.0050 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.7270 | 0.0080 | No | this paper | Table 1 |
| GraphFP_C | 0.7550 | 0.0040 | No | this paper | Table 1 |
| GraphFP_P | 0.7600 | 0.0050 | No | this paper | Table 1 |
| GraphFP_CP | 0.7550 | 0.0050 | No | this paper | Table 1 |
| GraphFP_CF | 0.7430 | 0.0030 | No | this paper | Table 1 |
| GraphFP_CPF | 0.7400 | 0.0070 | No | this paper | Table 1 |
| GIN | 0.7580 | 0.0030 | Yes | this paper | Table 2 |
| GCN | 0.7430 | 0.0030 | Yes | this paper | Table 2 |
| GraphSage | 0.7450 | 0.0060 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.7580 | 0.0030 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.7530 | 0.0030 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.7550 | 0.0050 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.7610 | 0.0040 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.7610 | 0.0030 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.7400 | 0.0070 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.7370 | 0.0080 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.7390 | 0.0050 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.7330 | 0.0080 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.7420 | 0.0070 | No | this paper | Table 3 |
| GIN_C, Vocab=200 | 0.7560 | 0.0080 | No | this paper | Table 4 |
| GIN_C, Vocab=400 | 0.7580 | 0.0050 | No | this paper | Table 4 |
| GIN_C, Vocab=800 | 0.7550 | 0.0040 | No | this paper | Table 4 |
| GIN_C, Vocab=1600 | 0.7540 | 0.0080 | No | this paper | Table 4 |
| GIN_C, Vocab=3200 | 0.7540 | 0.0040 | No | this paper | Table 4 |

### ToxCast — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AttrMasking | 0.6420 | 0.0050 | Yes | Hu 2020 | Table 1 |
| ContextPred | 0.6390 | 0.0060 | Yes | Hu 2020 | Table 1 |
| G-Motif | 0.6230 | 0.0060 | Yes | Rong 2020 | Table 1 |
| G-Contextual | 0.6280 | 0.0070 | Yes | Rong 2020 | Table 1 |
| GPT-GNN | 0.6250 | 0.0040 | Yes | Hu 2020 | Table 1 |
| GraphLoG | 0.6240 | 0.0020 | Yes | Xu 2021 | Table 1 |
| GraphCL | 0.6240 | 0.0060 | Yes | You 2020 | Table 1 |
| JOAO | 0.6290 | 0.0050 | Yes | You 2021 | Table 1 |
| JOAOv2 | 0.6320 | 0.0050 | Yes | You 2021 | Table 1 |
| GraphMVP | 0.6270 | 0.0010 | Yes | Liu 2022 | Table 1 |
| MGSSL | 0.6330 | 0.0050 | Yes | Zhang et al. | Table 1 |
| GraphFP-JT_C | 0.6360 | 0.0050 | No | this paper | Table 1 |
| GraphFP-JT_CF | 0.6250 | 0.0090 | No | this paper | Table 1 |
| GraphFP_C | 0.6380 | 0.0060 | No | this paper | Table 1 |
| GraphFP_P | 0.6320 | 0.0070 | No | this paper | Table 1 |
| GraphFP_CP | 0.6470 | 0.0020 | No | this paper | Table 1 |
| GraphFP_CF | 0.6530 | 0.0080 | No | this paper | Table 1 |
| GraphFP_CPF | 0.6390 | 0.0090 | No | this paper | Table 1 |
| GIN | 0.6390 | 0.0040 | Yes | this paper | Table 2 |
| GCN | 0.6330 | 0.0050 | Yes | this paper | Table 2 |
| GraphSage | 0.6280 | 0.0030 | Yes | this paper | Table 2 |
| CP, alpha=0.1 | 0.6390 | 0.0040 | No | this paper | Table 3 |
| CP, alpha=0.2 | 0.6410 | 0.0030 | No | this paper | Table 3 |
| CP, alpha=0.3 | 0.6470 | 0.0020 | No | this paper | Table 3 |
| CP, alpha=0.4 | 0.6400 | 0.0030 | No | this paper | Table 3 |
| CP, alpha=0.5 | 0.6460 | 0.0050 | No | this paper | Table 3 |
| CPF, alpha=0.1 | 0.6390 | 0.0090 | No | this paper | Table 3 |
| CPF, alpha=0.2 | 0.6450 | 0.0040 | No | this paper | Table 3 |
| CPF, alpha=0.3 | 0.6500 | 0.0050 | No | this paper | Table 3 |
| CPF, alpha=0.4 | 0.6460 | 0.0050 | No | this paper | Table 3 |
| CPF, alpha=0.5 | 0.6480 | 0.0050 | No | this paper | Table 3 |
| GIN_C, Vocab=200 | 0.6350 | 0.0080 | No | this paper | Table 4 |
| GIN_C, Vocab=400 | 0.6380 | 0.0040 | No | this paper | Table 4 |
| GIN_C, Vocab=800 | 0.6380 | 0.0060 | No | this paper | Table 4 |
| GIN_C, Vocab=1600 | 0.6390 | 0.0090 | No | this paper | Table 4 |
| GIN_C, Vocab=3200 | 0.6370 | 0.0060 | No | this paper | Table 4 |

## Baseline Models Identified

- **AttrMasking** (from: Hu et al. 2020)
- **ContextPred** (from: Hu et al. 2020)
- **G-Motif** (from: Rong et al. 2020)
- **G-Contextual** (from: Rong et al. 2020)
- **GPT-GNN** (from: Hu et al. 2020)
- **GraphLoG** (from: Xu et al. 2021)
- **GraphCL** (from: You et al. 2020)
- **JOAO** (from: You et al. 2021)
- **JOAOv2** (from: You et al. 2021)
- **GraphMVP** (from: Liu et al. 2022)
- **MGSSL** (from: Zhang et al.)
- **GIN** (from: this paper (baseline architecture))
- **GCN** (from: this paper (baseline architecture))
- **GraphSage** (from: this paper (baseline architecture))
- **GCNII** (from: Chen et al. 2020)
- **GatedGCN** (from: Bresson & Laurent 2017)
- **GatedGCN+RWSE** (from: Bresson & Laurent 2017; Vignac et al. 2020)

## Extraction Notes

[BBBP] Extracted all rows from Table 1, Table 2, Table 3, and Table 4 for the BBBP dataset. Table 1
contains the main comparison with baselines and proposed GraphFP variants. Table 2 compares GNN
architectures. Table 3 compares hyperparameter alpha values for CP and CPF models. Table 4 compares
vocabulary sizes. All values are percentages from the table, converted to [0,1] range. Standard
deviations are parsed from 'mean ± std' format. [Tox21] Extracted all Tox21 results from Table 1,
Table 2, Table 3, and Table 4. Values are percentages from the paper, converted to [0,1] range.
Standard deviations are parsed from 'mean ± std' format. All models are pre-trained on molecular
graphs, so uses_external_data is false (no external non-molecular data like ImageNet or LLMs). The
'standard' configuration refers to the default GIN architecture and vocabulary size 800 for the main
ablation, but all reported Tox21 results were extracted as requested. [ToxCast] Extracted all
ToxCast results from Table 1, Table 2, Table 3, and Table 4. Values are percentages from the paper,
converted to [0,1] range. Standard deviations are parsed from 'mean ± std' format. All models use
external pretraining data (GraphFP variants, AttrMasking, ContextPred, etc.), so uses_external_data
is true. The 'FOCUS' instruction was followed to only include ToxCast rows. [SIDER] Extracted all
rows from all tables containing SIDER results. Values are percentages from the table, converted to
[0,1] range as per ROC-AUC metric rules. Standard deviations are parsed from 'mean ± std' format.
Model names for ablation studies (alpha, vocab size) are kept distinct as they represent different
experimental configurations reported in the paper. [ClinTox] Extracted all ClinTox results from
Table 1, Table 2, Table 3, and Table 4. Values are percentages from the paper, converted to [0,1]
range. Standard deviations are parsed from 'mean ± std' format. Table 3 and 4 contain hyperparameter
ablations (alpha and vocab size) which are included as they represent specific model configurations
reported in the paper. The primary proposed model variants (GraphFP_C, GraphFP_CF, GraphFP_CPF) are
identified from Table 1. [MUV] Extracted all MUV results from Table 1, Table 2, Table 3, and Table
4. Values are percentages from the paper, converted to [0,1] range. Standard deviations are parsed
from 'mean ± std' format. 'uses_external_data' is set to true for all models as they are all pre-
trained models evaluated on the MUV benchmark. [HIV] Extracted all rows from all tables where the
'HIV' column contains data. Values are percentages from the table, converted to [0,1] range as per
ROC-AUC metric rules. Standard deviations are parsed from 'mean ± std' format. All models use
external pretraining data (GraphFP variants, AttrMasking, ContextPred, etc. are pre-trained models).
The 'FOCUS' instruction was followed to only include HIV results. Table 4 contains ablation studies
on vocabulary size for GIN_C, which are included as they are standard benchmark configurations for
that specific model variant in this paper. [BACE] Extracted all BACE results from Table 1, Table 2,
Table 3, and Table 4. Values are percentages from the paper, converted to [0,1] range. Standard
deviations are parsed from 'mean ± std' format. Table 3 and 4 contain hyperparameter ablations
(alpha and vocab size) which are included as they represent specific model configurations reported
in the paper. Table 2 contains GNN architecture variants. Table 1 contains the main pretraining
strategy comparison. [Peptides-func] Extracted only Peptides-func AP results as requested. Dataset
name normalized from 'Peptide-func' in table to 'Peptides-func' as per standard LRGB naming
convention and prompt instruction. All values are AP scores, normalized to [0,1]. Standard
deviations parsed correctly. [Peptides-struct] Extracted only Peptides-struct MAE results as
requested. The table caption refers to 'Peptide-struct' but the dataset name in the prompt and
standard LRGB benchmark is 'Peptides-struct'. I used 'Peptides-struct' for the dataset field to
align with standard naming conventions while respecting the prompt's focus. All values are standard
MAE (lower is better). No external data usage is indicated for these standard GNN baselines.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*