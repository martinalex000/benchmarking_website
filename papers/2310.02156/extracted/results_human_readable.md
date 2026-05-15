# Extraction: arXiv:2310.02156
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: PR-MPNN
- Type: GNN

## Results

### Alchemy — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base | 11.1200 | 0.6900 | Yes | this paper | Table 1 |
| Base w. PE | 7.1970 | 0.0940 | Yes | this paper | Table 1 |
| PR-MPNN (Gumbel SoftSub-ST) | 6.8580 | 0.0900 | No | this paper | Table 1 |
| PR-MPNN (I-MLE) | 6.6920 | 0.0610 | No | this paper | Table 1 |
| PR-MPNN (Simple) | 6.4470 | 0.0570 | No | this paper | Table 1 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base | 0.5740 | 0.0060 | Yes | this paper | Table 1 |
| Base w. PE | 0.5400 | 0.0430 | Yes | this paper | Table 1 |
| DIGL | 0.5820 | 0.0050 | Yes | Klicpera et al. 2019 | Table 1 |
| DIGL + Undirected | 0.5950 | 0.0060 | Yes | Klicpera et al. 2019 | Table 1 |
| Geom-GCN | 0.6080 | — | Yes | Pei et al. 2020 | Table 1 |
| SDRF | 0.5460 | 0.0040 | Yes | Topping et al. 2021 | Table 1 |
| SDRF + Undirected | 0.5750 | 0.0030 | Yes | Topping et al. 2021 | Table 1 |
| PR-MPNN (ours) | 0.6590 | 0.0400 | No | this paper | Table 1 |
| GPS (LapPE) | 0.6620 | 0.0380 | Yes | Dwivedi et al. 2022 | Table 1 |
| GPS (RWSE) | 0.7080 | 0.0200 | Yes | Dwivedi et al. 2022 | Table 1 |
| GPS (DEG) | 0.7180 | 0.0240 | Yes | Dwivedi et al. 2022 | Table 1 |
| Graphormer (DEG) | 0.6830 | 0.0170 | Yes | Bian et al. 2021 | Table 1 |
| Graphormer (DEG + attn bias) | 0.6830 | 0.0170 | Yes | Bian et al. 2021 | Table 1 |

### IMDB-BINARY — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.7000 | 0.0090 | Yes | Zhou et al. 2018 | Table 2 |
| IGN | 0.7130 | 0.0450 | Yes | Maron et al. 2019 | Table 2 |
| GIN | 0.7510 | 0.0510 | Yes | Xu et al. 2018 | Table 2 |
| PPGNs | 0.7300 | 0.0570 | Yes | Maron et al. 2019 | Table 2 |
| Natural GN | 0.7480 | 0.0200 | Yes | De Cao et al. 2020 | Table 2 |
| GSN | 0.7780 | 0.0330 | Yes | Botsas et al. 2020 | Table 2 |
| CIN | 0.7560 | 0.0320 | Yes | Bodnar et al. 2021 | Table 2 |
| PR-MPNN (10-fold CV) | 0.7520 | 0.0320 | No | this paper | Table 2 |
| PR-MPNN (train/val/test) | 0.7160 | 0.0120 | No | this paper | Table 2 |

### IMDB-MULTI — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCNN | 0.4780 | 0.0090 | Yes | Zha+2018 | Table 1 |
| IGN | 0.4860 | 0.0390 | Yes | Mar+2019c | Table 1 |
| GIN | 0.5230 | 0.0280 | Yes | xu2018how | Table 1 |
| PPGNs | 0.5040 | 0.0360 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.5120 | 0.0150 | Yes | de2020natural | Table 1 |
| GSN | 0.5430 | 0.0330 | Yes | botsas2020improving | Table 1 |
| CIN | 0.5250 | 0.0300 | Yes | Bod+2021 | Table 1 |
| PR-MPNN (10-fold CV) | 0.5290 | 0.0320 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.4580 | 0.0080 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.8140 | 0.0170 | Yes | She+2009 | Table 1 |
| PK | 0.7600 | 0.0270 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.9040 | 0.0570 | Yes | She+2011 | Table 1 |
| DGCNN | 0.8580 | 0.0180 | Yes | Zha+2018 | Table 1 |
| IGN | 0.8390 | 0.1300 | Yes | Mar+2019c | Table 1 |
| GIN | 0.8940 | 0.0560 | Yes | xu2018how | Table 1 |
| PPGNs | 0.9060 | 0.0870 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.8940 | 0.0160 | Yes | de2020natural | Table 1 |
| GSN | 0.9220 | 0.0750 | Yes | botsas2020improving | Table 1 |
| CIN | 0.9270 | 0.0610 | Yes | Bod+2021 | Table 1 |
| CAN | 0.9410 | 0.0480 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.9440 | 0.0370 | Yes | giusti2023cin | Table 1 |
| FoSR | 0.8620 | 0.0150 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.9040 | 0.0700 | Yes | Pap+2021 | Table 1 |
| PR-MPNN (10-fold CV) | 0.9840 | 0.0240 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.9100 | 0.0370 | No | this paper | Table 2 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.6250 | 0.0030 | Yes | She+2009 | Table 1 |
| PK | 0.8250 | 0.0050 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.8600 | 0.0180 | Yes | She+2011 | Table 1 |
| DGCNN | 0.7440 | 0.0050 | Yes | Zha+2018 | Table 1 |
| IGN | 0.7430 | 0.0270 | Yes | Mar+2019c | Table 1 |
| GIN | 0.8270 | 0.0170 | Yes | xu2018how | Table 1 |
| PPGNs | 0.8320 | 0.0110 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.8240 | 0.0130 | Yes | de2020natural | Table 1 |
| GSN | 0.8350 | 0.0200 | Yes | botsas2020improving | Table 1 |
| CIN | 0.8360 | 0.0140 | Yes | Bod+2021 | Table 1 |
| CAN | 0.8450 | 0.0160 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.8530 | 0.0120 | Yes | giusti2023cin | Table 1 |
| FoSR | 0.7290 | 0.0060 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.8160 | 0.0180 | Yes | Pap+2021 | Table 1 |
| PR-MPNN (10-fold CV) | 0.8560 | 0.0080 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.8150 | 0.0160 | No | this paper | Table 2 |

### NCI109 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.6240 | 0.0030 | Yes | She+2009 | Table 1 |
| IGN | 0.7280 | 0.0150 | Yes | Mar+2019c | Table 1 |
| PPGNs | 0.8220 | 0.0140 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.8300 | 0.0190 | Yes | de2020natural | Table 1 |
| GSN | 0.8350 | 0.0230 | Yes | botsas2020improving | Table 1 |
| CIN | 0.8400 | 0.0160 | Yes | Bod+2021 | Table 1 |
| CAN | 0.8360 | 0.0120 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.8450 | 0.0240 | Yes | giusti2023cin | Table 1 |
| FoSR | 0.7110 | 0.0060 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.8080 | 0.0260 | Yes | Pap+2021 | Table 1 |
| PR-MPNN (10-fold CV) | 0.8460 | 0.0120 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.8180 | 0.0150 | No | this paper | Table 2 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.7140 | 0.0030 | Yes | She+2009 | Table 1 |
| PK | 0.7370 | 0.0070 | Yes | Neu+2016 | Table 1 |
| WL kernel | 0.7500 | 0.0310 | Yes | She+2011 | Table 1 |
| DGCNN | 0.7550 | 0.0090 | Yes | Zha+2018 | Table 1 |
| IGN | 0.7660 | 0.0550 | Yes | Mar+2019c | Table 1 |
| GIN | 0.7620 | 0.0280 | Yes | xu2018how | Table 1 |
| PPGNs | 0.7720 | 0.0470 | Yes | Mar+2019 | Table 1 |
| Natural GN | 0.7170 | 0.0100 | Yes | de2020natural | Table 1 |
| GSN | 0.7660 | 0.0500 | Yes | botsas2020improving | Table 1 |
| CIN | 0.7700 | 0.0430 | Yes | Bod+2021 | Table 1 |
| CAN | 0.7820 | 0.0200 | Yes | giusti2022cell | Table 1 |
| CIN++ | 0.8050 | 0.0390 | Yes | giusti2023cin | Table 1 |
| FoSR | 0.7510 | 0.0080 | Yes | Karhadkar2022-uz | Table 1 |
| DropGNN | 0.7630 | 0.0610 | Yes | Pap+2021 | Table 1 |
| PR-MPNN (10-fold CV) | 0.8070 | 0.0390 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.7910 | 0.0280 | No | this paper | Table 2 |

### PTC_MR — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GK (k=3) | 0.5570 | 0.0050 | Yes | this paper | Table 1 |
| PK | 0.5950 | 0.0240 | Yes | this paper | Table 1 |
| WL kernel | 0.5990 | 0.0430 | Yes | this paper | Table 1 |
| DGCNN | 0.5860 | 0.0250 | Yes | this paper | Table 1 |
| IGN | 0.5850 | 0.0690 | Yes | this paper | Table 1 |
| GIN | 0.6460 | 0.0700 | Yes | this paper | Table 1 |
| PPGNs | 0.6620 | 0.0660 | Yes | this paper | Table 1 |
| Natural GN | 0.6680 | 0.0170 | Yes | this paper | Table 1 |
| GSN | 0.6820 | 0.0720 | Yes | this paper | Table 1 |
| CIN | 0.6820 | 0.0560 | Yes | this paper | Table 1 |
| CAN | 0.7280 | 0.0830 | Yes | this paper | Table 1 |
| CIN++ | 0.7320 | 0.0640 | Yes | this paper | Table 1 |
| FoSR | 0.5850 | 0.0170 | Yes | this paper | Table 1 |
| DropGNN | 0.6630 | 0.0860 | Yes | this paper | Table 1 |
| PR-MPNN (10-fold CV) | 0.7430 | 0.0390 | No | this paper | Table 1 |
| PR-MPNN (train/val/test) | 0.5890 | 0.0500 | No | this paper | Table 2 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+PE | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| DIGL+MPNN | 0.6469 | 0.0019 | Yes | this paper | Table 1 |
| DIGL+MPNN+LapPE | 0.6830 | 0.0026 | Yes | this paper | Table 1 |
| MixHop-GCN | 0.6592 | 0.0036 | Yes | this paper | Table 1 |
| MixHop-GCN+LapPE | 0.6843 | 0.0049 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| GraphGPS+LapPE | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| DRew-GCN | 0.6996 | 0.0076 | Yes | this paper | Table 1 |
| DRew-GCN+LapPE | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| DRew-GIN | 0.6940 | 0.0074 | Yes | this paper | Table 1 |
| DRew-GIN+LapPE | 0.7126 | 0.0045 | Yes | this paper | Table 1 |
| DRew-GatedGCN | 0.6733 | 0.0094 | Yes | this paper | Table 1 |
| DRew-GatedGCN+LapPE | 0.6977 | 0.0026 | Yes | this paper | Table 1 |
| PR-MPNN | 0.6825 | 0.0086 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| GatedGCN+PE | 0.3357 | 0.0006 | Yes | this paper | Table 1 |
| DIGL+MPNN | 0.3173 | 0.0007 | Yes | this paper | Table 1 |
| DIGL+MPNN+LapPE | 0.2616 | 0.0018 | Yes | this paper | Table 1 |
| MixHop-GCN | 0.2921 | 0.0023 | Yes | this paper | Table 1 |
| MixHop-GCN+LapPE | 0.2614 | 0.0023 | Yes | this paper | Table 1 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| GraphGPS+LapPE | 0.2500 | 0.0005 | Yes | this paper | Table 1 |
| DRew-GCN | 0.2781 | 0.0028 | Yes | this paper | Table 1 |
| DRew-GCN+LapPE | 0.2536 | 0.0015 | Yes | this paper | Table 1 |
| DRew-GIN | 0.2799 | 0.0016 | Yes | this paper | Table 1 |
| DRew-GIN+LapPE | 0.2606 | 0.0014 | Yes | this paper | Table 1 |
| DRew-GatedGCN | 0.2699 | 0.0018 | Yes | this paper | Table 1 |
| DRew-GatedGCN+LapPE | 0.2539 | 0.0007 | Yes | this paper | Table 1 |
| PR-MPNN | 0.2477 | 0.0005 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base | 0.6740 | 0.0100 | Yes | this paper | Table 1 |
| Base w. PE | 0.6540 | 0.0100 | Yes | this paper | Table 1 |
| DIGL | 0.6200 | 0.0030 | Yes | Kli+2019 | Table 1 |
| DIGL + Undirected | 0.6350 | 0.0040 | Yes | Kli+2019 | Table 1 |
| Geom-GCN | 0.6760 | — | Yes | webkb | Table 1 |
| SDRF | 0.6440 | 0.0040 | Yes | Topping2021-iy | Table 1 |
| SDRF + Undirected | 0.7030 | 0.0060 | Yes | Topping2021-iy | Table 1 |
| PR-MPNN (ours) | 0.8270 | 0.0320 | No | this paper | Table 1 |
| GPS (LapPE) | 0.7780 | 0.0100 | Yes | this paper | Table 1 |
| GPS (RWSE) | 0.7750 | 0.0120 | Yes | this paper | Table 1 |
| GPS (DEG) | 0.7730 | 0.0130 | Yes | this paper | Table 1 |
| Graphormer (DEG) | 0.7670 | 0.0170 | Yes | this paper | Table 1 |
| Graphormer (DEG + attn bias) | 0.7670 | 0.0170 | Yes | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base | 0.6970 | 0.0130 | Yes | this paper | Table 1 |
| Base w. PE | 0.6490 | 0.0180 | Yes | this paper | Table 1 |
| DIGL | 0.4950 | 0.0030 | Yes | Klicpera et al. 2019 | Table 1 |
| DIGL + Undirected | 0.5220 | 0.0050 | Yes | Klicpera et al. 2019 | Table 1 |
| Geom-GCN | 0.6410 | — | Yes | Pei et al. 2020 | Table 1 |
| SDRF | 0.5550 | 0.0030 | Yes | Topping et al. 2021 | Table 1 |
| SDRF + Undirected | 0.6150 | 0.0080 | Yes | Topping et al. 2021 | Table 1 |
| PR-MPNN (ours) | 0.7500 | 0.0150 | No | this paper | Table 1 |
| GPS (LapPE) | 0.7470 | 0.0290 | Yes | Dwivedi et al. 2022 | Table 1 |
| GPS (RWSE) | 0.8020 | 0.0220 | Yes | Dwivedi et al. 2022 | Table 1 |
| GPS (DEG) | 0.7980 | 0.0900 | Yes | Dwivedi et al. 2022 | Table 1 |
| Graphormer (DEG) | 0.7700 | 0.0190 | Yes | Bian et al. 2021 | Table 1 |
| Graphormer (DEG + attn bias) | 0.7700 | 0.0190 | Yes | Bian et al. 2021 | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PR-MPNN_Sim (ours) | 0.1390 | 0.0010 | No | this paper | Table 1 |
| PR-MPNN_Imle (ours) | 0.1510 | 0.0010 | No | this paper | Table 1 |
| PR-MPNN_Gmb (ours) | 0.1530 | 0.0030 | No | this paper | Table 1 |
| Base w. PE | 0.1620 | 0.0010 | Yes | this paper | Table 1 |
| Base | 0.2580 | 0.0060 | Yes | this paper | Table 1 |
| K-ST SAT | 0.1660 | 0.0070 | Yes | Chen22a | Table 1 |
| K-SG SAT | 0.1620 | 0.0130 | Yes | Chen22a | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | Rampasek2022-uc | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PR-MPNN_Sim (ours) | 0.7950 | 0.0090 | No | this paper | Table 1 |
| GPS | 0.7880 | 0.0100 | Yes | Rampasek 2022 | Table 1 |
| PR-MPNN_Imle (ours) | 0.7740 | 0.0150 | No | this paper | Table 1 |
| Base | 0.7750 | 0.0110 | Yes | this paper | Table 1 |
| PR-MPNN_Gmb (ours) | 0.7600 | 0.0250 | No | this paper | Table 1 |
| Base w. PE | 0.7640 | 0.0180 | Yes | this paper | Table 1 |
| K-ST SAT | 0.6250 | 0.0390 | Yes | this paper | Table 1 |
| K-SG SAT | 0.6130 | 0.0100 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **Base** (from: this paper)
- **Base w. PE** (from: this paper)
- **K-ST SAT** (from: Chen22a)
- **K-SG SAT** (from: Chen22a)
- **GPS** (from: Rampasek2022-uc)
- **GK (k=3)** (from: She+2009)
- **PK** (from: Neu+2016)
- **WL kernel** (from: She+2011)
- **DGCNN** (from: Zha+2018)
- **IGN** (from: Mar+2019c)
- **GIN** (from: xu2018how)
- **PPGNs** (from: Mar+2019)
- **Natural GN** (from: de2020natural)
- **GSN** (from: botsas2020improving)
- **CIN** (from: Bod+2021)
- **CAN** (from: giusti2022cell)
- **CIN++** (from: giusti2023cin)
- **FoSR** (from: Karhadkar2022-uz)
- **DropGNN** (from: Pap+2021)
- **DIGL** (from: Klicpera et al. 2019)
- **DIGL + Undirected** (from: Klicpera et al. 2019)
- **Geom-GCN** (from: Pei et al. 2020)
- **SDRF** (from: Topping et al. 2021)
- **SDRF + Undirected** (from: Topping et al. 2021)
- **GPS (LapPE)** (from: Dwivedi et al. 2022)
- **GPS (RWSE)** (from: Dwivedi et al. 2022)
- **GPS (DEG)** (from: Dwivedi et al. 2022)
- **Graphormer (DEG)** (from: Bian et al. 2021)
- **Graphormer (DEG + attn bias)** (from: Bian et al. 2021)
- **GCN** (from: Kipf & Welling)
- **GINE** (from: Xu et al.)
- **GatedGCN** (from: Bresson & Laurent)
- **GatedGCN+PE** (from: Gutteridge et al. (LRGB))
- **DIGL+MPNN** (from: Gutteridge et al. (LRGB))
- **DIGL+MPNN+LapPE** (from: Gutteridge et al. (LRGB))
- **MixHop-GCN** (from: Bianco et al.)
- **MixHop-GCN+LapPE** (from: Gutteridge et al. (LRGB))
- **Transformer+LapPE** (from: Gutteridge et al. (LRGB))
- **SAN+LapPE** (from: Gutteridge et al. (LRGB))
- **GraphGPS+LapPE** (from: Gutteridge et al. (LRGB))
- **DRew-GCN** (from: Topping et al.)
- **DRew-GCN+LapPE** (from: Topping et al.)
- **DRew-GIN** (from: Topping et al.)
- **DRew-GIN+LapPE** (from: Topping et al.)
- **DRew-GatedGCN** (from: Topping et al.)
- **DRew-GatedGCN+LapPE** (from: Topping et al.)

## Extraction Notes

[ZINC] Extracted results for ZINC from Table 1. The table reports MAE for two configurations: '-
Edge' (without edge features) and '+ Edge' (with edge features). Both configurations are standard
for ZINC depending on whether edge features are utilized. The paper compares PR-MPNN variants
(Gumbel, I-MLE, Simple) against Base GIN, Base GIN with PE, and Graph Transformers (GPS, SAT). All
values are normalized to [0,1] range as they are MAE values < 1. Note: The table header indicates
'Zinc' with sub-columns '- Edge' and '+ Edge'. I have extracted both columns as they represent the
standard evaluation on the dataset under different feature settings. The 'PNA' row group contains
GPS and SAT variants; GPS is listed under PNA backbone in the table structure but is a distinct
model. I included all rows present in the table for ZINC. [ogbg-molhiv] Extracted all rows from
Table 1 corresponding to the 'OGBG-molhiv' column. The metric is ROC-AUC (indicated by upward arrow
in table header). Values are normalized to [0,1]. Standard deviations are parsed from the '±'
notation. Note: The table header indicates '+ Edge' for OGBG-molhiv, implying edge features are
used, but the baseline 'Base' and 'Base w. PE' rows do not explicitly distinguish edge usage in the
cell values, so they are extracted as reported. The proposed model variants are PR-MPNN_Gmb, PR-
MPNN_Imle, and PR-MPNN_Sim. [Alchemy] Extracted only Alchemy results from Table 1. The table reports
MAE (indicated by downward arrow) for Alchemy. The proposed model PR-MPNN has three variants based
on gradient estimators (Gumbel SoftSub-ST, I-MLE, Simple). All values are test-set results as
implied by the context of 'comparison between pr-mpnn and baselines' and standard reporting
practices in such tables. No other datasets were included per instructions. [QM9] failed: 1
validation error for ExtractionOutput   Input should be a valid dictionary or instance of
ExtractionOutput [type=model_type, input_value=[{'name': 'R-GIN+FA', 'pa...er_hint': 'this paper'}],
input_type=list]     For further information visit https://errors.pydantic.dev/2.13/v/model_type
[MUTAG] Extracted results for MUTAG from Table 1 and Table 2. Table 1 reports 10-fold CV results for
all baselines and the proposed model. Table 2 reports train/val/test split results for the proposed
model. The primary metric Accuracy was used. Values were converted from percentages to [0,1] range.
Standard deviations were parsed from the '±' notation. [PTC_MR] Extracted all models for PTC_MR from
Table 1 and Table 2. Table 1 reports 10-fold CV results which are the primary benchmark results.
Table 2 reports train/val/test split results for PR-MPNN only. Both sets of results are included as
they represent different evaluation protocols reported in the paper. Values are normalized from
percentages to [0,1] range. [PROTEINS] Extracted results for PROTEINS from Table 1 (10-fold CV) and
Table 2 (train/val/test split). All values were percentages in the paper, converted to [0,1] range.
Standard deviations were parsed from the LaTeX formatting (e.g., \pm0.3 -> 0.003). The primary
metric Accuracy was used as requested. [NCI1] Extracted results for NCI1 from Table 1 (10-fold CV)
and Table 2 (train/val/test split). The primary metric is Accuracy. All values were converted from
percentages to decimals. The WL Kernel is noted as the best in Table 1, with PR-MPNN being second-
best. PR-MPNN results are reported in two configurations: 10-fold CV and train/val/test split.
[NCI109] Extracted results for NCI109 from Table 1 and Table 2. Table 1 reports 10-fold CV results,
while Table 2 reports train/val/test split results for the proposed model. Baselines in Table 1 are
taken from cited papers. Values were converted from percentages to [0,1] range. N/A values in Table
1 were skipped. [IMDB-BINARY] Extracted results for IMDB-BINARY from Table 2. The table lists
'IMDB-B' which corresponds to IMDB-BINARY. Two configurations for the proposed model PR-MPNN are
reported: '10-fold CV' and 'train/val/test'. Both are included as they represent different
evaluation protocols for the same dataset/model. Values were converted from percentages to [0,1]
range. Standard deviations were parsed from the '±' notation. [IMDB-MULTI] Extracted results for
IMDB-MULTI from Table 1. The table caption refers to 'IMDB-M', which corresponds to IMDB-MULTI in
the TUDataset collection. Two configurations for the proposed model PR-MPNN are reported: '10-fold
CV' and 'train/val/test'. Both were extracted as they represent different evaluation protocols for
the same proposed method. Standard deviations were parsed from the '±' notation. Values were
converted from percentages to [0,1] range. [Cornell] Extracted all rows from Table 1 corresponding
to the 'Cornell' dataset. The metric is Accuracy (indicated by upward arrow). Standard deviations
are parsed from the '±' notation. 'N/A' for Geom-GCN std is converted to null. All values are
normalized to [0,1]. Baseline source references are inferred from citations in the text and table.
[Texas] Extracted all rows from Table 1 (labeled tab: hetero) corresponding to the 'Texas' column.
The metric is Accuracy (indicated by up arrow). Standard deviations are parsed from the text (e.g.,
0.010 -> 0.01). Geom-GCN has N/A for std, so std is null. All values are normalized to [0,1] range
as they are percentages in the table but represented as decimals in the source text (e.g., 0.827).
The proposed model is PR-MPNN. [Wisconsin] Extracted all rows from Table 1 corresponding to the
'Wisconsin' dataset column. The metric is Accuracy (indicated by up arrow). Standard deviations are
parsed from the text (e.g., 0.750±0.015). Geom-GCN has N/A for std, so it is set to null. All values
are normalized to [0,1] as they are percentages in the table but represent accuracy scores.
[Peptides-func] Extracted all rows from Table 1 for the Peptides-func dataset. The table caption
indicates that results are reported from Gutteridge et al. (LRGB) for baselines, but the table
itself contains the values. PR-MPNN is the proposed model. All values are AP scores, normalized to
[0,1]. Standard deviations are parsed from the scriptsize text following the values. [Peptides-
struct] Extracted all rows from Table 1 for the Peptides-struct dataset. The table explicitly lists
MAE as the metric for Peptides-struct. All values were parsed correctly including standard
deviations. The proposed model PR-MPNN achieved the best score (bolded). No other tables or datasets
were included as per instructions.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*