# Extraction: arXiv:2307.07107
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GPS+GPSE
- Type: GNN

## Results

### BACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.7010 | 0.0540 | Yes | Hu* 2020 Strategies | Table 1 |
| Self-supervised pre-trained | 0.7990 | 0.0090 | Yes | Hu* 2020 Strategies | Table 1 |
| GraphCL pre-trained | 0.7540 | 0.0140 | Yes | you 2020 graph | Table 1 |
| InfoGraph pre-trained | 0.6480 | 0.0080 | Yes | wang 2022 evaluating | Table 1 |
| JOAOv2 pre-trained | 0.6740 | 0.0070 | Yes | wang 2022 evaluating | Table 1 |
| GraphMAE | 0.8310 | 0.0090 | Yes | hou 2022 graphmae | Table 1 |
| GraphLoG | 0.8350 | 0.0120 | Yes | xu 2021 self | Table 1 |
| GraphLoG augmented | 0.8250 | 0.0120 | Yes | this paper | Table 1 |
| LapPE augmented | 0.8040 | 0.0150 | Yes | this paper | Table 1 |
| RWSE augmented | 0.7960 | 0.0280 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.7700 | 0.0440 | Yes | this paper | Table 1 |
| GPSE augmented | 0.8080 | 0.0310 | No | this paper | Table 1 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.6580 | 0.0450 | Yes | Hu* 2020 Strategies | Table 1 |
| SSL InfoMax pre-trained | 0.6880 | 0.0080 | Yes | Hu* 2020 Strategies | Table 1 |
| SSL EdgePred pre-trained | 0.6730 | 0.0240 | Yes | Hu* 2020 Strategies | Table 1 |
| SSL AttrMasking pre-trained | 0.6430 | 0.0280 | Yes | Hu* 2020 Strategies | Table 1 |
| SSL ContextPred pre-trained | 0.6800 | 0.0200 | Yes | Hu* 2020 Strategies | Table 1 |
| GraphCL pre-trained | 0.6970 | 0.0070 | Yes | you 2020 graph | Table 1 |
| InfoGraph pre-trained | 0.6630 | 0.0060 | Yes | wang 2022 evaluating | Table 1 |
| JOAOv2 pre-trained | 0.6640 | 0.0090 | Yes | wang 2022 evaluating | Table 1 |
| GraphMAE | 0.7200 | 0.0060 | Yes | hou 2022 graphmae | Table 1 |
| GraphLoG | 0.7250 | 0.0080 | Yes | xu 2021 self | Table 1 |
| GraphLoG augmented | 0.6560 | 0.0100 | Yes | this paper | Table 1 |
| LapPE augmented | 0.6710 | 0.0160 | Yes | this paper | Table 1 |
| RWSE augmented | 0.6700 | 0.0140 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.6760 | 0.0120 | Yes | this paper | Table 1 |
| GPSE augmented | 0.6620 | 0.0090 | No | this paper | Table 1 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5526 | 0.0153 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| Graph MLP-Mixer | 0.7246 | 0.0036 | Yes | this paper | Table 1 |
| GPS+none | 0.7167 | 0.0001 | Yes | this paper | Table 1 |
| GPS+(RWSE/LapPE) | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GPS+AllPSE | 0.7205 | 0.0035 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.7231 | 0.0025 | No | this paper | Table 1 |

### CSL — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1000 | 0.0000 | Yes | this paper | Table 1 |
| GIN+rand | 0.1270 | 0.0640 | Yes | this paper | Table 1 |
| GIN+GPSE | 0.4290 | 0.0790 | No | this paper | Table 1 |
| GIN+LapPE | 0.9250 | 0.0420 | Yes | this paper | Table 1 |
| GIN+RWSE | 1.0000 | 0.0000 | Yes | this paper | Table 1 |

### ClinTox — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.5800 | 0.0440 | Yes | Hu 2020 | Table 1 |
| SSL InfoMax pre-trained | 0.6990 | 0.0030 | Yes | Hu 2020 | Table 2 |
| SSL EdgePred pre-trained | 0.6410 | 0.0370 | Yes | Hu 2020 | Table 2 |
| SSL AttrMasking pre-trained | 0.7180 | 0.0410 | Yes | Hu 2020 | Table 2 |
| SSL ContextPred pre-trained | 0.6590 | 0.0380 | Yes | Hu 2020 | Table 2 |
| GraphCL pre-trained | 0.7600 | 0.0270 | Yes | You 2020 | Table 1 |
| InfoGraph pre-trained | 0.6630 | 0.0060 | Yes | Wang 2022 | Table 1 |
| JOAOv2 pre-trained | 0.6450 | 0.0090 | Yes | Wang 2022 | Table 1 |
| GraphMAE | 0.8230 | 0.0120 | Yes | Hou 2022 | Table 1 |
| GraphLoG | 0.7670 | 0.0330 | Yes | Xu 2021 | Table 1 |
| GraphLoG augmented | 0.7250 | 0.0350 | Yes | this paper | Table 1 |
| LapPE augmented | 0.7640 | 0.0230 | Yes | this paper | Table 1 |
| RWSE augmented | 0.7450 | 0.0440 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.7260 | 0.0430 | Yes | this paper | Table 1 |
| GPSE augmented | 0.7880 | 0.0380 | No | this paper | Table 1 |

### EXP — ACC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4870 | 0.0220 | Yes | this paper | Table 1 |
| GIN+rand | 0.5130 | 0.0290 | Yes | this paper | Table 1 |
| GIN+GPSE | 0.6830 | 0.0750 | No | this paper | Table 1 |
| GIN+LapPE | 0.9950 | 0.0080 | Yes | this paper | Table 1 |
| GIN+RWSE | 0.9970 | 0.0060 | Yes | this paper | Table 1 |

### HIV — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.7530 | 0.0190 | Yes | Hu 2020 | Table 1 |
| SSL InfoMax pre-trained | 0.7600 | 0.0070 | Yes | Hu 2020 | Table 1 |
| SSL EdgePred pre-trained | 0.7630 | 0.0100 | Yes | Hu 2020 | Table 1 |
| SSL AttrMasking pre-trained | 0.7720 | 0.0110 | Yes | Hu 2020 | Table 1 |
| SSL ContextPred pre-trained | 0.7730 | 0.0100 | Yes | Hu 2020 | Table 1 |
| GraphCL pre-trained | 0.7850 | 0.0120 | Yes | You 2020 | Table 1 |
| InfoGraph pre-trained | 0.7020 | 0.0060 | Yes | Wang 2022 | Table 1 |
| JOAOv2 pre-trained | 0.6840 | 0.0050 | Yes | Wang 2022 | Table 1 |
| GraphMAE | 0.7720 | 0.0100 | Yes | Hou 2022 | Table 1 |
| GraphLoG | 0.7780 | 0.0080 | Yes | Xu 2021 | Table 1 |
| GraphLoG augmented | 0.7440 | 0.0150 | Yes | this paper | Table 1 |
| LapPE augmented | 0.7560 | 0.0110 | Yes | this paper | Table 1 |
| RWSE augmented | 0.7810 | 0.0150 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.7540 | 0.0150 | Yes | this paper | Table 1 |
| GPSE augmented | 0.7720 | 0.0150 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9649 | 0.0025 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| Graph MLP-Mixer | 0.9835 | 0.0010 | Yes | this paper | Table 1 |
| GPS+none | 0.9805 | 0.0000 | Yes | this paper | Table 1 |
| GPS+(RWSE/LapPE) | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GPS+AllPSE | 0.9808 | 0.0012 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.9808 | 0.0013 | No | this paper | Table 1 |

### MUV — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.7180 | 0.0250 | Yes | Hu 2020 | Table 1 |
| SSL InfoMax pre-trained | 0.7530 | 0.0250 | Yes | Hu 2020 | Table 1 |
| SSL EdgePred pre-trained | 0.7410 | 0.0210 | Yes | Hu 2020 | Table 1 |
| SSL AttrMasking pre-trained | 0.7470 | 0.0140 | Yes | Hu 2020 | Table 1 |
| SSL ContextPred pre-trained | 0.7580 | 0.0170 | Yes | Hu 2020 | Table 1 |
| GraphCL pre-trained | 0.6980 | 0.0270 | Yes | You 2020 | Table 1 |
| InfoGraph pre-trained | 0.4430 | 0.0060 | Yes | Wang 2022 | Table 1 |
| JOAOv2 pre-trained | 0.4740 | 0.0080 | Yes | Wang 2022 | Table 1 |
| GraphMAE | 0.7630 | 0.0240 | Yes | Hou 2022 | Table 1 |
| GraphLoG | 0.7600 | 0.0110 | Yes | Xu 2021 | Table 1 |
| GraphLoG augmented | 0.7240 | 0.0150 | Yes | this paper | Table 1 |
| LapPE augmented | 0.7560 | 0.0080 | Yes | this paper | Table 1 |
| RWSE augmented | 0.7500 | 0.0100 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.6790 | 0.0070 | Yes | this paper | Table 1 |
| GPSE augmented | 0.7660 | 0.0120 | No | this paper | Table 1 |

### MolHIV — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7599 | 0.0119 | Yes | Kipf 2017 | Table 1 |
| GIN | 0.7707 | 0.0149 | Yes | Xu 2018 | Table 1 |
| CIN | 0.8094 | 0.0057 | Yes | Bodnar 2021 | Table 1 |
| PR-MPNN_SIM | 0.7950 | 0.0090 | Yes | Qian 2023 | Table 1 |
| GPS+rand | 0.6210 | 0.0444 | Yes | this paper | Table 1 |
| GPS+none | 0.7798 | 0.0077 | Yes | this paper | Table 1 |
| GPS+LapPE | 0.7736 | 0.0097 | Yes | this paper | Table 1 |
| GPS+RWSE | 0.7880 | 0.0101 | Yes | this paper | Table 1 |
| GPS+LapPE+RWSE | 0.7719 | 0.0129 | Yes | this paper | Table 1 |
| GPS+AllPSE | 0.7645 | 0.0236 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.7815 | 0.0133 | No | this paper | Table 1 |
| Self-supervised pre-trained | 0.7730 | 0.0100 | Yes | Hu 2020 | Table 2 |
| GraphCL pre-trained | 0.7850 | 0.0120 | Yes | You 2020 | Table 2 |
| InfoGraph pre-trained | 0.7020 | 0.0060 | Yes | Wang 2022 | Table 2 |
| JOAOv2 pre-trained | 0.6840 | 0.0050 | Yes | Wang 2022 | Table 2 |
| GraphMAE | 0.7720 | 0.0100 | Yes | Hou 2022 | Table 2 |
| GraphLoG | 0.7780 | 0.0080 | Yes | Xu 2021 | Table 2 |
| No augmentation (baseline) | 0.7530 | 0.0190 | Yes | Hu 2020 | Table 2 |
| GraphLoG augmented | 0.7440 | 0.0150 | Yes | Xu 2021 | Table 2 |
| LapPE augmented | 0.7560 | 0.0110 | Yes | this paper | Table 2 |
| RWSE augmented | 0.7810 | 0.0150 | Yes | this paper | Table 2 |
| AllPSE augmented | 0.7540 | 0.0150 | Yes | this paper | Table 2 |
| GPSE augmented | 0.7720 | 0.0150 | Yes | this paper | Table 2 |

### MolPCBA — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2424 | 0.0034 | Yes | Kipf & Welling 2017 | Table 1 |
| GIN | 0.2703 | 0.0023 | Yes | Xu et al. 2018 | Table 1 |
| CRaWI | 0.2986 | 0.0025 | Yes | Toenshoff et al. 2021 | Table 1 |
| GPS+rand | 0.0753 | 0.0045 | Yes | this paper | Table 1 |
| GPS+none | 0.2869 | 0.0012 | Yes | this paper | Table 1 |
| GPS+LapPE | 0.2939 | 0.0016 | Yes | this paper | Table 1 |
| GPS+RWSE | 0.2907 | 0.0028 | Yes | this paper | Table 1 |
| GPS+LapPE+RWSE | 0.2854 | 0.0029 | Yes | this paper | Table 1 |
| GPS+AllPSE | 0.2826 | 0.0001 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.2911 | 0.0036 | No | this paper | Table 1 |

### PCQM4Mv2 (subset) — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS+GPSE | 0.1196 | 0.0004 | No | this paper | Table 1 |
| GPS+rand | 0.4768 | 0.0171 | Yes | this paper | Table 1 |
| GPS+none | 0.1329 | 0.0030 | Yes | this paper | Table 1 |
| GPS+LapPE | 0.1267 | 0.0004 | Yes | this paper | Table 1 |
| GPS+RWSE | 0.1230 | 0.0008 | Yes | this paper | Table 1 |
| GPS+LapPE+RWSE | 0.1273 | 0.0006 | Yes | this paper | Table 1 |
| GPS+AllPSE | 0.1254 | 0.0011 | Yes | this paper | Table 1 |
| GCN+GPSE | 0.1822 | 0.0028 | Yes | this paper | Table 2 |
| GatedGCN+GPSE | 0.1495 | 0.0015 | Yes | this paper | Table 2 |
| GIN+GPSE | 0.1615 | 0.0015 | Yes | this paper | Table 2 |
| GINE+GPSE | 0.1294 | 0.0006 | Yes | this paper | Table 2 |
| Transformer+GPSE | 0.1805 | 0.0021 | Yes | this paper | Table 2 |
| GPSE (Not finetuned) | 0.1196 | 0.0004 | Yes | this paper | Table 4 |
| GPSE (Finetuned) | 0.1195 | 0.0007 | Yes | this paper | Table 4 |
| GPSE (default) | 0.1216 | 0.0002 | Yes | this paper | Table 5 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | Bresson et al. 2017 | Table 1 |
| Graph MLP-Mixer | 0.6920 | 0.0054 | Yes | He et al. 2022 | Table 1 |
| DRew+GCN | 0.6996 | 0.0076 | Yes | Gutteridge et al. 2023 | Table 1 |
| PR-MPNN | 0.6825 | 0.0086 | Yes | Qian et al. 2023 | Table 1 |
| GCN+LapPE | 0.6218 | 0.0055 | Yes | Tönshoff et al. 2023 | Table 1 |
| GCN+RWSE | 0.6067 | 0.0069 | Yes | this paper | Table 1 |
| GCN+GPSE | 0.6316 | 0.0085 | Yes | this paper | Table 1 |
| GPS+none | 0.6231 | 0.0252 | Yes | this paper | Table 1 |
| GPS+(RWSE/LapPE) | 0.6535 | 0.0041 | Yes | Rampásek et al. 2022 | Table 1 |
| GPS+AllPSE | 0.6397 | 0.0092 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.6688 | 0.0151 | No | this paper | Table 1 |
| GPSE-abs (default) | 0.6584 | 0.0042 | No | this paper | Table 2 |
| GPSE-noabs | 0.6687 | 0.0119 | No | this paper | Table 2 |
| GPSE-signinvar | 0.6619 | 0.0097 | No | this paper | Table 2 |
| GPSE-SignNet | 0.6647 | 0.0093 | No | this paper | Table 2 |

### Proteins — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN+none | 0.8044 | 0.0056 | Yes | this paper | Table 1 |
| GCN+LapPE | 0.8038 | 0.0016 | Yes | this paper | Table 1 |
| GCN+GPSE | 0.8025 | 0.0019 | No | this paper | Table 1 |
| SAGE+none | 0.8035 | 0.0007 | Yes | this paper | Table 1 |
| SAGE+LapPE | 0.8027 | 0.0045 | Yes | this paper | Table 1 |
| SAGE+GPSE | 0.8014 | 0.0022 | No | this paper | Table 1 |
| GAT(E)v2+none | 0.8347 | 0.0013 | Yes | this paper | Table 1 |
| GAT(E)v2+LapPE | 0.8325 | 0.0005 | Yes | this paper | Table 1 |
| GAT(E)v2+GPSE | 0.8351 | 0.0011 | No | this paper | Table 1 |
| Transformer+none | 0.7393 | 0.0144 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.7405 | 0.0011 | Yes | this paper | Table 1 |
| Transformer+GPSE | 0.7467 | 0.0074 | No | this paper | Table 1 |
| GPS+none | 0.6955 | 0.0567 | Yes | this paper | Table 1 |
| GPS+LapPE | 0.7080 | 0.0414 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.7205 | 0.0375 | No | this paper | Table 1 |

### SIDER — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.5730 | 0.0160 | Yes | Hu* 2020 Strategies | Table 1 |
| Self-supervised pre-trained | 0.6100 | 0.0070 | Yes | Hu* 2020 Strategies | Table 1 |
| GraphCL pre-trained | 0.6050 | 0.0090 | Yes | you 2020 graph | Table 1 |
| InfoGraph pre-trained | 0.5710 | 0.0080 | Yes | wang 2022 evaluating | Table 1 |
| JOAOv2 pre-trained | 0.5910 | 0.0070 | Yes | wang 2022 evaluating | Table 1 |
| GraphMAE | 0.6030 | 0.0110 | Yes | hou 2022 graphmae | Table 1 |
| GraphLoG | 0.6120 | 0.0110 | Yes | xu 2021 self | Table 1 |
| GraphLoG augmented | 0.6090 | 0.0070 | Yes | this paper | Table 1 |
| LapPE augmented | 0.5930 | 0.0170 | Yes | this paper | Table 1 |
| RWSE augmented | 0.5850 | 0.0140 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.6300 | 0.0060 | Yes | this paper | Table 1 |
| GPSE augmented | 0.6110 | 0.0160 | No | this paper | Table 1 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.7400 | 0.0080 | Yes | Hu* 2020 Strategies | Table 1 |
| Self-supervised pre-trained | 0.7670 | 0.0040 | Yes | Hu* 2020 Strategies | Table 1 |
| GraphCL pre-trained | 0.7390 | 0.0070 | Yes | you 2020 graph | Table 1 |
| InfoGraph pre-trained | 0.6810 | 0.0060 | Yes | wang 2022 evaluating | Table 1 |
| JOAOv2 pre-trained | 0.6820 | 0.0080 | Yes | wang 2022 evaluating | Table 1 |
| GraphMAE | 0.7550 | 0.0060 | Yes | hou 2022 graphmae | Table 1 |
| GraphLoG | 0.7570 | 0.0050 | Yes | xu 2021 self | Table 1 |
| GraphLoG augmented | 0.7320 | 0.0050 | Yes | this paper | Table 1 |
| LapPE augmented | 0.7660 | 0.0030 | Yes | this paper | Table 1 |
| RWSE augmented | 0.7630 | 0.0050 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.7590 | 0.0100 | Yes | this paper | Table 1 |
| GPSE augmented | 0.7740 | 0.0080 | No | this paper | Table 1 |

### ToxCast — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| No pre-training (baseline) | 0.6340 | 0.0060 | Yes | Hu 2020 | Table 1 |
| Self-supervised pre-trained | 0.6420 | 0.0050 | Yes | Hu 2020 | Table 1 |
| GraphCL pre-trained | 0.6240 | 0.0060 | Yes | You 2020 | Table 1 |
| InfoGraph pre-trained | 0.5840 | 0.0060 | Yes | Wang 2022 | Table 1 |
| JOAOv2 pre-trained | 0.5700 | 0.0050 | Yes | Wang 2022 | Table 1 |
| GraphMAE | 0.6410 | 0.0030 | Yes | Hou 2022 | Table 1 |
| GraphLoG | 0.6350 | 0.0070 | Yes | Xu 2021 | Table 1 |
| GraphLoG augmented | 0.6360 | 0.0040 | Yes | this paper | Table 1 |
| LapPE augmented | 0.6590 | 0.0070 | Yes | this paper | Table 1 |
| RWSE augmented | 0.6560 | 0.0030 | Yes | this paper | Table 1 |
| AllPSE augmented | 0.6390 | 0.0030 | Yes | this paper | Table 1 |
| GPSE augmented | 0.6630 | 0.0080 | No | this paper | Table 1 |

### arXiv — ACC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN+none | 0.7162 | 0.0023 | Yes | this paper | Table 1 |
| GCN+LapPE | 0.7089 | 0.0020 | Yes | this paper | Table 1 |
| GCN+GPSE | 0.7170 | 0.0026 | No | this paper | Table 1 |
| SAGE+none | 0.7236 | 0.0043 | Yes | this paper | Table 1 |
| SAGE+LapPE | 0.7163 | 0.0016 | Yes | this paper | Table 1 |
| SAGE+GPSE | 0.7234 | 0.0019 | No | this paper | Table 1 |
| GAT(E)v2+none | 0.7169 | 0.0021 | Yes | this paper | Table 1 |
| GAT(E)v2+LapPE | 0.7130 | 0.0027 | Yes | this paper | Table 1 |
| GAT(E)v2+GPSE | 0.7217 | 0.0042 | No | this paper | Table 1 |
| Transformer+none | 0.5700 | 0.0079 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.5721 | 0.0025 | Yes | this paper | Table 1 |
| Transformer+GPSE | 0.5917 | 0.0021 | No | this paper | Table 1 |
| GPS+none | 0.7060 | 0.0028 | Yes | this paper | Table 1 |
| GPS+LapPE | 0.7062 | 0.0041 | Yes | this paper | Table 1 |
| GPS+GPSE | 0.7089 | 0.0036 | No | this paper | Table 1 |

### ogbg-molhiv — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GPS+GPSE | 0.7815 | 0.0133 | No | this paper | Table 3 |
| GPS+GPSE (LapPE & EigVals excluded) | 0.7849 | 0.0067 | No | this paper | Table 3 |
| GPS+GPSE (ElstaticPE excluded) | 0.7681 | 0.0146 | No | this paper | Table 3 |
| GPS+GPSE (RWSE excluded) | 0.7771 | 0.0105 | No | this paper | Table 3 |
| GPS+GPSE (HKdiagSE excluded) | 0.7787 | 0.0198 | No | this paper | Table 3 |
| GPS+GPSE (CycleSE excluded) | 0.7739 | 0.0240 | No | this paper | Table 3 |

## Baseline Models Identified

- **GPS+rand**
- **GPS+none**
- **GPS+LapPE**
- **GPS+RWSE**
- **GPS+LapPE+RWSE**
- **GPS+AllPSE**
- **GCN** (from: Kipf 2017)
- **GIN** (from: Xu 2018)
- **CIN** (from: Bodnar 2021)
- **CRaWI** (from: Toenshoff 2021)
- **PR-MPNN_SIM** (from: Qian 2023)
- **K-ST SAT+RWSE** (from: Chen 2022)
- **K-SG SAT+RWSE** (from: Chen 2022)
- **K-ST SAT+GPSE** (from: this paper)
- **K-SG SAT+GPSE** (from: this paper)
- **Self-supervised pre-trained** (from: Hu et al. 2020)
- **GraphCL pre-trained** (from: You et al. 2020)
- **InfoGraph pre-trained** (from: Wang et al. 2022)
- **JOAOv2 pre-trained** (from: Wang et al. 2022)
- **GraphMAE** (from: Hou et al. 2022)
- **GraphLoG** (from: Xu et al. 2021)
- **No augmentation (baseline)** (from: Hu et al. 2020)
- **GraphLoG augmented** (from: Xu et al. 2021)
- **LapPE augmented** (from: this paper)
- **RWSE augmented** (from: this paper)
- **AllPSE augmented** (from: this paper)
- **GPSE augmented** (from: this paper)
- **No pre-training (baseline)** (from: Hu* 2020 Strategies)
- **SSL InfoMax pre-trained** (from: Hu* 2020 Strategies)
- **SSL EdgePred pre-trained** (from: Hu* 2020 Strategies)
- **SSL AttrMasking pre-trained** (from: Hu* 2020 Strategies)
- **SSL ContextPred pre-trained** (from: Hu* 2020 Strategies)
- **GINE**
- **GatedGCN** (from: Bresson et al. 2017)
- **Graph MLP-Mixer** (from: He et al. 2022)
- **DRew+GCN** (from: Gutteridge et al. 2023)
- **PR-MPNN** (from: Qian et al. 2023)
- **GCN+LapPE** (from: Tönshoff et al. 2023)
- **GCN+RWSE** (from: this paper)
- **GPS+(RWSE/LapPE)** (from: Rampásek et al. 2022)
- **GCN+GPSE** (from: this paper)
- **SAGE** (from: Hamilton et al. 2017)
- **GATv2** (from: Brody et al. 2022)
- **Transformer** (from: Vaswani et al. 2017)
- **GPS** (from: Abboud et al. 2022)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **Graph Transformer** (from: this paper)
- **GIN+rand** (from: this paper)
- **GIN+LapPE** (from: Chen et al. 2020)
- **GIN+RWSE** (from: Fey et al. 2020)

## Extraction Notes

[ZINC] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or
instance of ExtractionOutput [type=model_type, input_value=[{'name': 'GCN', 'params_...er_hint':
'this paper'}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [PCQM4Mv2] Extracted results for PCQM4Mv2 (subset)
from Table 1, Table 2, Table 4, and Table 5. Table 1 contains the main comparison of GPS variants.
Table 2 contains ablation of PSEs on different GNN backbones. Table 4 contains ablation on training
datasets for GPSE. Table 5 contains ablation on GPSE training tasks. Note: Table 3 does not contain
PCQM4Mv2 results. Baselines like GCN, GIN, etc. in Table 1 do not have PCQM4Mv2 results reported
(marked as '--'). The proposed model is GPS+GPSE. Other rows with GPSE are variants/ablations of the
proposed method's component. [MolHIV] Extracted AUROC results for MolHIV from Table 1, Table 2, and
Table 3. Table 2 reports values as percentages (e.g., 77.3), which were divided by 100 to normalize
to [0,1]. Table 3 reports ablation results for 'ogbg-molhiv', which is the OGB version of MolHIV;
these are included as they represent the same benchmark task. The primary proposed model 'GPS+GPSE'
from Table 1 is the main result, while Table 3 provides ablation variants of the GPSE training
process. Table 2 includes pre-trained baselines which use external data. [MolPCBA] Extracted only
MolPCBA AP results from Table 1. Note that CRaWI is listed as a baseline in Table 1 with the best AP
score (0.2986), while the proposed model GPS+GPSE achieves 0.2911. Table 2 does not contain MolPCBA
results (only AUROC on other MoleculeNet datasets). CIN and PR-MPNN_SIM do not report MolPCBA
results in Table 1. [BBBP] Extracted all rows from Table 1 and Table 2 (sideways table)
corresponding to the BBBP dataset. The metric is AUROC/ROC-AUC reported as percentage, so values
were divided by 100. The proposed model is identified as 'GPSE augmented' based on the bold
formatting in the table caption and context. All baselines are included as requested. [BACE]
Extracted only BACE column results from Table 1 (and cross-verified with Table 2/sidewaystable). All
values are percentages from the paper, converted to [0,1] range as per instructions. The proposed
model is identified as 'GPSE augmented' based on bolding and context. Baselines include both pre-
trained and no-pre-training variants. 'Self-supervised pre-trained' refers to the best of four
strategies from Hu et al. 2020. [Tox21] Extracted results for Tox21 from Table 1 (and cross-verified
with Table 2/sidewaystable). All values are percentages from the paper, converted to [0,1] range as
per instructions. The primary metric AUROC/ROC-AUC was used. The proposed model is identified as
'GPSE augmented' based on bolding and context. [ToxCast] Extracted results for ToxCast from Table 1
(and cross-verified with Table 2/sidewaystable). All values are percentages in the table, converted
to [0,1] range. The primary metric AUROC/ROC-AUC was used. 'Self-supervised pre-trained' refers to
the best of four strategies from Hu et al. 2020 as noted in the footnote. GPSE augmented is the
proposed model. [SIDER] Extracted results for the SIDER dataset from Table 1. All values are
percentages reported in the table, converted to [0,1] range as per instructions. The metric is
AUROC/ROC-AUC. The proposed model is GPSE augmented. Baselines include various pre-training
strategies and augmentation methods. Note: The table caption says 'AUROC (%)', so values like 61.1
are treated as 61.1% -> 0.611. [ClinTox] Extracted all ClinTox results from Table 1 and Table 2.
Values are percentages from the paper (e.g., 78.8) converted to [0,1] range (0.788). The 'No pre-
training' baseline row in Table 2 is missing some columns compared to Table 2's expanded view, but
Table 1 provides the full set. Note: Table 2's 'Self-supervised pre-trained' row seems to correspond
to the best of Hu et al. strategies, while Table 2's expanded view lists them individually. I have
included the individual strategies from Table 2 (sidewaystable) as they provide more granular data,
and the aggregated/best ones from Table 1 where applicable. However, looking closely, Table 1 (main
text) lists 'Self-supervised pre-trained' with value 71.8 for ClinTox, which matches 'SSL
AttrMasking' in Table 2. The table in the prompt text has two tables: one sidewaystable (Table 2 in
caption logic, labeled tab:molnet_full) and one main table (Table 1, labeled tab:molnet). The main
table (tab:molnet) has a row 'Self-supervised pre-trained' which seems to be a summary or specific
strategy. The sidewaystable has the detailed breakdown. I will use the detailed breakdown from the
sidewaystable for the SSL methods to be precise, as they are distinct baselines. For the 'No pre-
training' baseline, both tables agree on 58.0. For the proposed model 'GPSE augmented', both tables
agree on 78.8. I have included all rows from the sidewaystable as they represent the full set of
baselines and variants reported. [MUV] Extracted AUROC results for the MUV dataset from Table 1 (and
cross-verified with Table 1 extended). All values were percentages in the paper (e.g., 71.8) and
were divided by 100 to fit the [0,1] range. The 'RWSE augmented' row in the extended table had a
typo '75.0 + 1.0' which was interpreted as '75.0 ± 1.0' consistent with other rows. The primary
metric AUROC was used. No other datasets were included. [HIV] Extracted AUROC results for the HIV
dataset from Table 1 (and cross-verified with Table 2/sidewaystable). All values were percentages in
the table (e.g., 75.3) and were divided by 100 to fit the [0,1] range as per instructions. The
proposed model is identified as 'GPSE augmented' based on the bolding and context. All baseline
models are included as requested. [Peptides-struct] failed: 1 validation error for ExtractionOutput
results.1.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[Peptides-func] Extracted all rows for Peptides-func from Table 1 and Table 2. Table 1 contains the
main comparison results, while Table 2 contains ablation study results for different GPSE variants.
All values are normalized to [0,1] as they represent AP scores. The primary metric AP was used as
requested. [CIFAR10] Extracted only CIFAR10 results as requested. The table reports Accuracy in
percentage (ACC (%)), so values were divided by 100 to normalize to [0, 1]. Standard deviations were
parsed from the 'mean ± std' format. Rows with '--' were skipped as they contain no data for
CIFAR10. [MNIST] Extracted only MNIST results as requested. The table reports Accuracy in percentage
(ACC (%)), so values were divided by 100 to normalize to [0, 1]. Standard deviations were parsed
from the 'mean ± std' format. Only test-set results are available in this table. [arXiv] Extracted
only ACC results for the arXiv dataset as requested. Values were converted from percentages to [0,1]
range. All rows from the table corresponding to arXiv were included. The proposed model is
identified as GPSE (Graph Positional Encoding) based on the bold/underline notation and context.
[Proteins] The paper focuses on OOD transferability. The table provides AUROC results for the
Proteins dataset. The FOCUS instruction requested 'Accuracy', but the table only reports AUROC for
Proteins (and ACC for arXiv). As AUROC is the standard benchmark metric for OGB node classification
benchmarks like Proteins when Accuracy is not explicitly provided in the primary results table,
AUROC was extracted. No Accuracy values are present in the table for the Proteins dataset. [CSL]
Extracted only CSL Test Accuracy results from Table 1. Values were reported as percentages in the
table (e.g., 10.0, 42.9, 92.5, 100.0) and were divided by 100 to normalize to [0, 1] range as per
instructions. The table caption indicates ACC (%). All rows for CSL Test column were extracted.
[EXP] Extracted only the 'EXP' dataset results from Table 1. The table reports ACC (%), so values
were divided by 100. Standard deviations were parsed from the 'mean ± std' format. All rows from the
EXP columns were included.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*