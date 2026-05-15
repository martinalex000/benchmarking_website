# Extraction: arXiv:2308.11129
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: HDSE
- Type: GNN

## Results

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3010 | 0.0020 | Yes | this paper | Table 4 |
| GAT | 0.2980 | 0.0060 | Yes | this paper | Table 4 |
| SGC | 0.2700 | 0.0090 | Yes | this paper | Table 4 |
| SIGN | 0.3650 | 0.0100 | Yes | this paper | Table 4 |
| NodeFormer | 0.3690 | 0.0100 | Yes | this paper | Table 4 |
| CoBFormer | 0.3740 | 0.0100 | Yes | this paper | Table 4 |
| SGFormer | 0.3790 | 0.0110 | Yes | this paper | Table 4 |
| GOAT | 0.3210 | 0.0180 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.3800 | 0.0150 | No | this paper | Table 4 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| Graph ViT/MLP-Mixer | 0.7396 | 0.0033 | Yes | this paper | Table 1 |
| Exphormer | 0.7470 | 0.0013 | Yes | this paper | Table 1 |
| GT | 0.5975 | 0.0029 | Yes | this paper | Table 1 |
| GT + HDSE | 0.6465 | 0.0059 | No | this paper | Table 1 |
| GraphGPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GraphGPS + HDSE | 0.7618 | 0.0028 | No | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| GRIT + HDSE | 0.7647 | 0.0043 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 2 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 2 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 2 |
| SGFormer | 0.6997 | 0.0063 | Yes | this paper | Table 2 |
| SAN | 0.7669 | 0.0065 | Yes | this paper | Table 2 |
| EGT | 0.7923 | 0.0035 | Yes | this paper | Table 2 |
| Exphormer | 0.7807 | 0.0004 | Yes | this paper | Table 2 |
| GT | 0.7317 | 0.0062 | Yes | this paper | Table 2 |
| GT + HDSE | 0.7422 | 0.0057 | No | this paper | Table 2 |
| SAT | 0.7786 | 0.0010 | Yes | this paper | Table 2 |
| SAT + HDSE | 0.7851 | 0.0010 | No | this paper | Table 2 |
| GraphGPS | 0.7802 | 0.0018 | Yes | this paper | Table 2 |
| GraphGPS + HDSE | 0.7850 | 0.0012 | No | this paper | Table 2 |
| GRIT | 0.8003 | 0.0028 | Yes | this paper | Table 2 |
| GRIT + HDSE | 0.7996 | 0.0020 | No | this paper | Table 2 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4130 | 0.0300 | Yes | this paper | Table 4 |
| GAT | 0.3920 | 0.0310 | Yes | this paper | Table 4 |
| SGC | 0.3900 | 0.0330 | Yes | this paper | Table 4 |
| SIGN | 0.4170 | 0.0220 | Yes | this paper | Table 4 |
| Graphormer | 0.4190 | 0.0280 | Yes | this paper | Table 4 |
| GraphGPS | 0.3620 | 0.0060 | Yes | this paper | Table 4 |
| NodeFormer | 0.3470 | 0.0410 | Yes | this paper | Table 4 |
| SGFormer | 0.4490 | 0.0390 | Yes | this paper | Table 4 |
| GOAT | 0.4330 | 0.0430 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.4600 | 0.0320 | No | this paper | Table 4 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8160 | 0.0040 | Yes | this paper | Table 1 |
| GAT | 0.8300 | 0.0070 | Yes | this paper | Table 1 |
| SGC | 0.8010 | 0.0020 | Yes | this paper | Table 1 |
| JKNet | 0.8180 | 0.0050 | Yes | this paper | Table 1 |
| APPNP | 0.8330 | 0.0050 | Yes | this paper | Table 1 |
| SIGN | 0.8210 | 0.0030 | Yes | this paper | Table 1 |
| HC-GNN | 0.8190 | 0.0040 | Yes | this paper | Table 1 |
| Graphormer | 0.7580 | 0.0110 | Yes | this paper | Table 1 |
| SAT | 0.7240 | 0.0030 | Yes | this paper | Table 1 |
| ANS-GT | 0.7940 | 0.0090 | Yes | this paper | Table 1 |
| AGT | 0.8170 | 0.0040 | Yes | this paper | Table 1 |
| HSGT | 0.8360 | 0.0180 | Yes | this paper | Table 1 |
| GraphGPS | 0.7650 | 0.0060 | Yes | this paper | Table 1 |
| Gapformer | 0.8350 | 0.0040 | Yes | this paper | Table 1 |
| NodeFormer | 0.8220 | 0.0090 | Yes | this paper | Table 1 |
| SGFormer | 0.8450 | 0.0080 | Yes | this paper | Table 1 |
| GOAT | 0.8210 | 0.0090 | Yes | this paper | Table 1 |
| GOAT + HDSE | 0.8390 | 0.0070 | No | this paper | Table 1 |
| H2GCN | 0.8792 | 0.0082 | Yes | this paper | Table 2 |
| GPRGNN | 0.8827 | 0.0040 | Yes | this paper | Table 2 |
| GT | 0.7184 | 0.0062 | Yes | this paper | Table 2 |
| SAN | 0.7402 | 0.0101 | Yes | this paper | Table 2 |
| Gophormer | 0.8765 | 0.0020 | Yes | this paper | Table 2 |
| Coarformer | 0.8869 | 0.0082 | Yes | this paper | Table 2 |
| ANS-GT + HDSE | 0.8967 | 0.0039 | No | this paper | Table 2 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 2 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 2 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 2 |
| PNA | 0.9794 | 0.0012 | Yes | this paper | Table 2 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 2 |
| Graph ViT/MLP-Mixer | 0.9742 | 0.0011 | Yes | this paper | Table 2 |
| Exphormer | 0.9855 | 0.0004 | Yes | this paper | Table 2 |
| GT | 0.9083 | 0.0016 | Yes | this paper | Table 2 |
| GT + HDSE | 0.9439 | 0.0018 | No | this paper | Table 2 |
| GraphGPS | 0.9805 | 0.0013 | Yes | this paper | Table 2 |
| GraphGPS + HDSE | 0.9837 | 0.0011 | No | this paper | Table 2 |
| GRIT | 0.9811 | 0.0011 | Yes | this paper | Table 2 |
| GRIT + HDSE | 0.9842 | 0.0012 | No | this paper | Table 2 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 2 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 2 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 2 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | this paper | Table 2 |
| SGFormer | 0.8529 | 0.0010 | Yes | this paper | Table 2 |
| SAN | 0.8658 | 0.0004 | Yes | this paper | Table 2 |
| EGT | 0.8682 | 0.0002 | Yes | this paper | Table 2 |
| Exphormer | 0.8674 | 0.0001 | Yes | this paper | Table 2 |
| GT | 0.8481 | 0.0007 | Yes | this paper | Table 2 |
| GT + HDSE | 0.8671 | 0.0005 | No | this paper | Table 2 |
| SAT | 0.8685 | 0.0004 | Yes | this paper | Table 2 |
| SAT + HDSE | 0.8693 | 0.0004 | No | this paper | Table 2 |
| GraphGPS | 0.8669 | 0.0006 | Yes | this paper | Table 2 |
| GraphGPS + HDSE | 0.8674 | 0.0006 | No | this paper | Table 2 |
| GRIT | 0.8720 | 0.0008 | Yes | this paper | Table 2 |
| GRIT + HDSE | 0.8728 | 0.0006 | No | this paper | Table 2 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | Kipf 2017 | Table 3 |
| GINE | 0.5498 | 0.0079 | Yes | Xu 2018 | Table 3 |
| GatedGCN | 0.5864 | 0.0035 | Yes | Bresson 2017 | Table 3 |
| GatedGCN+RWSE | 0.6069 | 0.0035 | Yes | Dwivedi 2021 | Table 3 |
| GT | 0.6326 | 0.0126 | Yes | Dwivedi 2020 | Table 3 |
| SAN+RWSE | 0.6439 | 0.0075 | Yes | Kreuzer 2021 | Table 3 |
| MGT+WavePE | 0.6817 | 0.0064 | Yes | Ngo 2023 | Table 3 |
| GRIT | 0.6988 | 0.0082 | Yes | Ma 2023 | Table 3 |
| Exphormer | 0.6527 | 0.0043 | Yes | Shirzad 2023 | Table 3 |
| Graph ViT/MLP-Mixer | 0.6970 | 0.0080 | Yes | He 2023 | Table 3 |
| DRew | 0.7150 | 0.0044 | Yes | Gutteridge 2023 | Table 3 |
| GraphGPS | 0.6535 | 0.0041 | Yes | Rampavsek 2022 | Table 3 |
| GraphGPS + HDSE | 0.7156 | 0.0058 | No | this paper | Table 3 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | Kipf 2017 | Table 3 |
| GINE | 0.3547 | 0.0045 | Yes | Xu 2019 | Table 3 |
| GatedGCN | 0.3420 | 0.0013 | Yes | Bresson 2017 | Table 3 |
| GatedGCN+RWSE | 0.3357 | 0.0006 | Yes | Dwivedi 2021 | Table 3 |
| GT | 0.2529 | 0.0016 | Yes | Dwivedi 2020 | Table 3 |
| SAN+RWSE | 0.2545 | 0.0012 | Yes | Kreuzer 2021 | Table 3 |
| MGT+WavePE | 0.2453 | 0.0025 | Yes | Ngo 2023 | Table 3 |
| GRIT | 0.2460 | 0.0012 | Yes | Ma 2023 | Table 3 |
| Exphormer | 0.2481 | 0.0007 | Yes | Shirzad 2023 | Table 3 |
| Graph ViT/MLP-Mixer | 0.2475 | 0.0015 | Yes | He 2023 | Table 3 |
| DRew | 0.2536 | 0.0015 | Yes | Gutteridge 2023 | Table 3 |
| GraphGPS | 0.2500 | 0.0012 | Yes | Rampásek 2022 | Table 3 |
| GraphGPS + HDSE | 0.2457 | 0.0013 | No | this paper | Table 3 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3860 | 0.0180 | Yes | this paper | Table 4 |
| GAT | 0.3560 | 0.0210 | Yes | this paper | Table 4 |
| SGC | 0.3930 | 0.0230 | Yes | this paper | Table 4 |
| SIGN | 0.4070 | 0.0250 | Yes | this paper | Table 4 |
| Graphormer | 0.4090 | 0.0250 | Yes | this paper | Table 4 |
| NodeFormer | 0.3850 | 0.0150 | Yes | this paper | Table 4 |
| SGFormer | 0.4180 | 0.0220 | Yes | this paper | Table 4 |
| GOAT | 0.4110 | 0.0250 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.4320 | 0.0240 | No | this paper | Table 4 |
| GOAT + HDSE (K=1) | 0.4320 | 0.0240 | No | this paper | Table 7 |
| GOAT + HDSE (K=2) | 0.4380 | 0.0210 | No | this paper | Table 7 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | Kipf 2017 | Table 2 |
| GIN | 0.5260 | 0.0510 | Yes | Xu 2018 | Table 2 |
| GatedGCN | 0.2820 | 0.0150 | Yes | Bresson 2017 | Table 2 |
| PNA | 0.1880 | 0.0040 | Yes | Corso 2020 | Table 2 |
| CIN | 0.0790 | 0.0060 | Yes | Bodnar 2021 | Table 2 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | Zhao 2021 | Table 2 |
| SGFormer | 0.3060 | 0.0230 | Yes | Wu 2023 | Table 2 |
| SAN | 0.1390 | 0.0060 | Yes | Kreuzer 2021 | Table 2 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | Zhang 2023 | Table 2 |
| Specformer | 0.0660 | 0.0030 | Yes | Bo 2023 | Table 2 |
| EGT | 0.1080 | 0.0090 | Yes | Hussain 2022 | Table 2 |
| Graph ViT/MLP-Mixer | 0.0730 | 0.0010 | Yes | He 2023 | Table 2 |
| GT | 0.2260 | 0.0140 | Yes | Dwivedi 2020 | Table 2 |
| GT + HDSE | 0.1590 | 0.0060 | No | this paper | Table 2 |
| SAT | 0.0940 | 0.0080 | Yes | Chen 2022 | Table 2 |
| SAT + HDSE | 0.0840 | 0.0030 | No | this paper | Table 2 |
| GraphGPS | 0.0700 | 0.0040 | Yes | Rampásek 2022 | Table 2 |
| GraphGPS + HDSE | 0.0620 | 0.0030 | No | this paper | Table 2 |
| GRIT | 0.0590 | 0.0020 | Yes | Ma 2023 | Table 2 |
| GRIT + HDSE | 0.0590 | 0.0040 | No | this paper | Table 2 |
| GraphGPS + HDSE (K=0) | 0.0690 | 0.0030 | No | this paper | Table 6 |
| GraphGPS + HDSE (K=1) | 0.0620 | 0.0030 | No | this paper | Table 6 |
| GraphGPS + HDSE (K=2) | 0.0640 | 0.0040 | No | this paper | Table 6 |

### ogbn-100M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6204 | 0.0027 | Yes | this paper | Table 4 |
| GAT | 0.6347 | 0.0039 | Yes | this paper | Table 4 |
| SGC | 0.6329 | 0.0019 | Yes | this paper | Table 4 |
| SIGN | 0.6511 | 0.0014 | Yes | this paper | Table 4 |
| LargeGT | 0.6473 | 0.0005 | Yes | this paper | Table 4 |
| SGFormer | 0.6601 | 0.0037 | Yes | this paper | Table 4 |
| GOAT | 0.6505 | 0.0013 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.6604 | 0.0015 | No | this paper | Table 4 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7174 | 0.0029 | Yes | this paper | Table 4 |
| GAT | 0.7195 | 0.0036 | Yes | this paper | Table 4 |
| SGC | 0.6779 | 0.0027 | Yes | this paper | Table 4 |
| SIGN | 0.7195 | 0.0011 | Yes | this paper | Table 4 |
| LINKX | 0.6618 | 0.0033 | Yes | this paper | Table 4 |
| HC-GNN | 0.7279 | 0.0025 | Yes | this paper | Table 4 |
| ANS-GT | 0.7234 | 0.0050 | Yes | this paper | Table 4 |
| AGT | 0.7228 | 0.0038 | Yes | this paper | Table 4 |
| HSGT | 0.7258 | 0.0031 | Yes | this paper | Table 4 |
| GraphGPS | 0.7097 | 0.0041 | Yes | this paper | Table 4 |
| Gapformer | 0.7190 | 0.0019 | Yes | this paper | Table 4 |
| NAGphormer | 0.7013 | 0.0055 | Yes | this paper | Table 4 |
| Exphormer | 0.7244 | 0.0028 | Yes | this paper | Table 4 |
| NodeFormer | 0.5990 | 0.0042 | Yes | this paper | Table 4 |
| CoBFormer | 0.7317 | 0.0018 | Yes | this paper | Table 4 |
| SGFormer | 0.7263 | 0.0013 | Yes | this paper | Table 4 |
| GOAT | 0.7241 | 0.0040 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.7326 | 0.0019 | No | this paper | Table 4 |
| GOAT + HDSE (K=1) | 0.7326 | 0.0019 | No | this paper | Table 7 |
| GOAT + HDSE (K=2) | 0.7336 | 0.0015 | No | this paper | Table 7 |

### ogbn-proteins — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7251 | 0.0035 | Yes | this paper | Table 4 |
| GAT | 0.7202 | 0.0044 | Yes | this paper | Table 4 |
| SGC | 0.7031 | 0.0023 | Yes | this paper | Table 4 |
| SIGN | 0.7124 | 0.0046 | Yes | this paper | Table 4 |
| ANS-GT | 0.7467 | 0.0065 | Yes | this paper | Table 4 |
| HSGT | 0.7813 | 0.0025 | Yes | this paper | Table 4 |
| NodeFormer | 0.7745 | 0.0115 | Yes | this paper | Table 4 |
| SGFormer | 0.7953 | 0.0038 | Yes | this paper | Table 4 |
| GOAT | 0.7837 | 0.0026 | Yes | this paper | Table 4 |
| GOAT + HDSE | 0.8034 | 0.0032 | No | this paper | Table 4 |
| GOAT+HDSE | 0.8030 | 0.0030 | No | this paper | Table 5 (Ablation) |
| w/o HDSE | 0.7940 | 0.0030 | Yes | this paper | Table 5 (Ablation) |
| w/o coarsening | 0.7830 | 0.0040 | Yes | this paper | Table 5 (Ablation) |

## Baseline Models Identified

- **GCN** (from: Kipf 2017)
- **GIN** (from: Xu 2018)
- **GatedGCN** (from: Bresson 2017)
- **PNA** (from: Corso 2020)
- **CIN** (from: Bodnar 2021)
- **GIN-AK+** (from: Zhao 2021)
- **SGFormer** (from: Wu 2023)
- **SAN** (from: Kreuzer 2021)
- **Graphormer-GD** (from: Zhang 2023)
- **Specformer** (from: Bo 2023)
- **EGT** (from: Hussain 2022)
- **Graph ViT/MLP-Mixer** (from: He 2023)
- **Exphormer** (from: Shirzad 2023)
- **GT** (from: Dwivedi 2020)
- **SAT** (from: Chen 2022)
- **GraphGPS** (from: Rampásek 2022)
- **GRIT** (from: Ma 2023)
- **GINE** (from: Xu 2018)
- **GatedGCN+RWSE** (from: Dwivedi 2021)
- **SAN+RWSE** (from: Kreuzer 2021)
- **MGT+WavePE** (from: Ngo 2023)
- **DRew** (from: Gutteridge 2023)
- **GAT** (from: Velickovic et al. 2018)
- **SGC** (from: Wu et al. 2019)
- **SIGN** (from: Rossi et al. 2020)
- **LINKX** (from: Lim et al. 2021)
- **HC-GNN** (from: Zhong et al. 2023)
- **Graphormer** (from: Ying et al. 2021)
- **ANS-GT** (from: Zhang et al. 2022)
- **AGT** (from: Ma et al. 2023)
- **HSGT** (from: Zhu et al. 2023)
- **Gapformer** (from: Liu et al. 2023)
- **LargeGT** (from: Dwivedi et al. 2023)
- **VCR-GT** (from: Fu et al. 2024)
- **NAGphormer** (from: Chen et al. 2022)
- **NodeFormer** (from: Wu et al. 2022)
- **CoBFormer** (from: Xing et al. 2024)
- **GOAT** (from: Kong et al. 2023)
- **JKNet** (from: xu2018representation)
- **APPNP** (from: gasteiger2018predict)
- **H2GCN** (from: zhu2020beyond)
- **GPRGNN** (from: chien2020adaptive)
- **Coarformer** (from: kuang2021coarformer)

## Extraction Notes

[ZINC] Extracted all ZINC MAE results from Table 2 and Table 6. Table 6 contains ablation results
for different hierarchy levels K, which are included as they represent specific configurations of
the proposed method on the target dataset. The primary metric MAE was used. All values are test-set
results. Standard deviations were parsed from the 'mean ± std' format. [MNIST] Extracted only MNIST
results from Table 2. Values were converted from percentages to [0,1] range. Standard deviations
were parsed from the 'mean ± std' format. Baselines with missing values ('–') were skipped. The
proposed model is identified as 'HDSE' which is appended to base models (GT, GraphGPS, GRIT).
[CIFAR10] Extracted only CIFAR10 Accuracy results from Table 1. Values were converted from
percentages to [0,1] range. Standard deviations were parsed from 'mean ± std' format. All models
listed in the table for CIFAR10 were included. [PATTERN] Extracted only PATTERN dataset results from
Table 2. All values are percentages divided by 100 to fit [0,1] range. Standard deviations were
parsed from the 'mean ± std' format. The proposed model is HDSE, which is applied as an enhancement
to various baselines (GT, SAT, GraphGPS, GRIT). All baseline results are from the current paper's
experiments as indicated by the table caption. [CLUSTER] Extracted all rows from Table 2 for the
CLUSTER dataset. The metric is Accuracy. Values are percentages in the table, so they were divided
by 100 to fit the [0,1] range. Standard deviations were parsed from the 'mean ± std' format. The
proposed model is identified as 'HDSE' which is added to various baselines (GT, SAT, GraphGPS,
GRIT). [Peptides-func] Extracted only Peptides-func AP results from Table 3. The table explicitly
lists 'AP' as the metric for Peptides-func. All values are normalized to [0,1]. Standard deviations
are parsed from the '±' notation. The proposed model is identified as 'GraphGPS + HDSE' based on the
bold formatting and context in the text. [Peptides-struct] Extracted only Peptides-struct MAE
results from Table 3. The table caption mentions 'two peptide datasets', but the FOCUS instruction
restricted extraction to Peptides-struct. The proposed model is identified as 'GraphGPS + HDSE'
based on the bolding and context in the text. All baseline models are taken from the table. Standard
deviations are parsed from the '±' notation. Values are not percentages. [Actor] Extracted only the
'Actor' dataset results as requested. The table reports Accuracy in percentage format (e.g., 30.1),
which was normalized to [0, 1] (0.301). The proposed model is 'GOAT + HDSE'. Baselines include
standard GNNs and Graph Transformers. Some baseline values for Actor were missing (marked as '-') in
the table and thus excluded. [Squirrel] Extracted all results for the 'Squirrel' dataset from Table
4 and Table 7. Table 4 reports the main benchmark results for various baselines and the proposed
model (GOAT + HDSE). Table 7 reports a sensitivity analysis on the hierarchy level K for the
proposed model. The primary metric is Accuracy. Values are normalized from percentages to [0,1].
Standard deviations are extracted from the 'mean ± std' format. Note that Table 4 lists 'GOAT +
HDSE' with K=1 results (43.2), while Table 7 shows K=2 yields a slightly higher result (43.8). Both
are included as they represent different configurations of the proposed method. [Chameleon]
Extracted only the Chameleon dataset results from Table 4. All values are percentages from the
table, converted to [0,1] range as per instructions. The proposed model is identified as 'GOAT +
HDSE' based on the bold formatting and context of the paper comparing GOAT variants. Baselines are
taken directly from the table rows. [ogbn-proteins] Extracted all rows for 'ogbn-proteins' from
Table 4 and Table 5. Table 4 contains the main comparison results. Table 5 contains ablation study
results for GOAT+HDSE variants. All values were converted from percentages to [0,1] range. Standard
deviations were parsed from the '±' notation. Baseline results in Table 4 are noted as primarily
taken from Wu et al. 2023 (SGFormer paper) or original papers, but extracted as reported in this
table. [ogbn-arxiv] Extracted all rows for ogbn-arxiv from Table 4 and Table 7. Table 7 provides
sensitivity analysis for K=1 and K=2, which are variants of the proposed model's configuration. The
primary result in Table 4 for GOAT+HDSE corresponds to K=1 (73.26), while K=2 yields 73.36. Both are
included as they represent the proposed model's performance under different hyperparameter settings
on the target dataset. All values were converted from percentages to [0,1] range. [arxiv-year]
failed: 14 validation errors for ExtractionOutput results.2.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.9.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.12.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.14.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.15.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.16.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.17.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.18.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbn-products] failed: 9 validation errors for
ExtractionOutput results.5.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.9.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.11.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.12.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.13.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.14.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.16.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbn-100M] Extracted only the 'ogbn-100M' column as
requested. The metric is Accuracy (%). Values were divided by 100 to normalize to [0,1]. Standard
deviations were parsed from the '±' notation. Bold/colored values indicate best performance but were
extracted normally. Other datasets (Actor, Squirrel, Chameleon, ogbn-proteins, ogbn-arxiv, arxiv-
year, ogbn-products) were ignored. [Cora] Extracted results from two tables (Table 1 and Table 2)
containing Cora results. Table 1 reports results for a set of baselines and the proposed GOAT+HDSE.
Table 2 reports results for a different set of baselines (including re-runs) and ANS-GT+HDSE. Both
tables report Accuracy as a percentage, which was normalized to [0,1]. The proposed model in the
paper is GOAT+HDSE, but Table 2 also reports ANS-GT+HDSE which appears to be a variant or ablation
using the same HDSE method on a different backbone. Both are treated as proposed/variant models in
their respective contexts, but strictly speaking, the main proposed model is GOAT+HDSE. ANS-GT+HDSE
is included as it is a result row for the proposed method's extension. Note: Table 2 caption
mentions 'ANS-GT + HDSE' as the header for the proposed method in that specific table context, while
Table 1 focuses on GOAT+HDSE. I have included both as they are distinct model configurations
reported in the paper. [CiteSeer] failed: 1 validation error for ExtractionOutput results.12.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type [PubMed] failed: 3
validation errors for ExtractionOutput results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.8.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*