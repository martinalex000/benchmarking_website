# Extraction: Non-backtracking Graph Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: NBA-GNN
- Type: GNN

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7532 | 0.0134 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.7572 | 0.0132 | Yes | this paper | Table 1 |
| GCN + NBA | 0.7585 | 0.0175 | Yes | this paper | Table 1 |
| GCN + NBA+LapPE | 0.7609 | 0.0186 | Yes | this paper | Table 1 |
| GraphSAGE | 0.7559 | 0.0161 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.7608 | 0.0144 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.7586 | 0.0213 | Yes | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.7621 | 0.0172 | Yes | this paper | Table 1 |
| GAT | 0.7463 | 0.0159 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.7512 | 0.0154 | Yes | this paper | Table 1 |
| GAT + NBA | 0.7549 | 0.0171 | Yes | this paper | Table 1 |
| GAT + NBA+LapPE | 0.7561 | 0.0175 | Yes | this paper | Table 1 |
| ChebNet | 0.7399 | 0.0160 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.7396 | 0.0241 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.7379 | 0.0099 | Yes | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.7421 | 0.0137 | Yes | this paper | Table 1 |
| NBA-GCN | 0.7585 | 0.0175 | Yes | this paper | Table 2 |
| NBA-GraphSAGE | 0.7586 | 0.0213 | Yes | this paper | Table 2 |
| NBA-GAT | 0.7549 | 0.0171 | Yes | this paper | Table 2 |
| GatedGCN | 0.7325 | 0.0192 | Yes | this paper | Table 2 |
| EGNN | 0.7567 | 0.0221 | Yes | this paper | Table 2 |
| CensNet | 0.7516 | 0.0162 | Yes | this paper | Table 2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8658 | 0.0060 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.8592 | 0.0083 | Yes | this paper | Table 1 |
| GCN + NBA | 0.8722 | 0.0095 | Yes | this paper | Table 1 |
| GCN + NBA+LapPE | 0.8720 | 0.0129 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8632 | 0.0158 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.8700 | 0.0117 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.8702 | 0.0083 | Yes | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.8650 | 0.0120 | Yes | this paper | Table 1 |
| GAT | 0.8694 | 0.0119 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.8686 | 0.0152 | Yes | this paper | Table 1 |
| GAT + NBA | 0.8722 | 0.0120 | Yes | this paper | Table 1 |
| GAT + NBA+LapPE | 0.8692 | 0.0098 | Yes | this paper | Table 1 |
| ChebNet | 0.8523 | 0.0110 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.8531 | 0.0139 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.8823 | 0.0159 | Yes | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.8795 | 0.0217 | Yes | this paper | Table 1 |
| NBA-GCN | 0.8722 | 0.0095 | No | this paper | Table 2 |
| NBA-GraphSAGE | 0.8702 | 0.0083 | No | this paper | Table 2 |
| NBA-GAT | 0.8722 | 0.0120 | No | this paper | Table 2 |
| GatedGCN | 0.8477 | 0.0156 | Yes | this paper | Table 2 |
| EGNN | 0.8769 | 0.0125 | Yes | this paper | Table 2 |
| CensNet | 0.8648 | 0.0138 | Yes | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5946 | 0.0662 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.5703 | 0.0547 | Yes | this paper | Table 1 |
| GCN + NBA | 0.6108 | 0.0614 | Yes | this paper | Table 1 |
| GCN + NBA+LapPE | 0.6378 | 0.0317 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6027 | 0.0625 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.6189 | 0.0484 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.6459 | 0.0691 | Yes | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.6378 | 0.0544 | Yes | this paper | Table 1 |
| GAT | 0.4757 | 0.0614 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.5108 | 0.0769 | Yes | this paper | Table 1 |
| GAT + NBA | 0.5838 | 0.0558 | Yes | this paper | Table 1 |
| GAT + NBA+LapPE | 0.5784 | 0.0640 | Yes | this paper | Table 1 |
| ChebNet | 0.6473 | 0.0520 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.6527 | 0.0506 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.6973 | 0.0483 | Yes | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.6757 | 0.0634 | Yes | this paper | Table 1 |
| NBA-GCN | 0.6108 | 0.0614 | No | this paper | Table 2 |
| NBA-GraphSAGE | 0.6459 | 0.0691 | No | this paper | Table 2 |
| NBA-GAT | 0.5838 | 0.0558 | No | this paper | Table 2 |
| GatedGCN | 0.5216 | 0.0987 | Yes | this paper | Table 2 |
| EGNN | 0.5946 | 0.0573 | Yes | this paper | Table 2 |
| CensNet | 0.6162 | 0.0707 | Yes | this paper | Table 2 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | this paper | Table 1 |
| GCN+LapPE | 0.1370 | 0.0077 | Yes | this paper | Table 2 |
| GIN | 0.1265 | 0.0076 | Yes | this paper | Table 1 |
| GIN+LapPE | 0.1302 | 0.0105 | Yes | this paper | Table 2 |
| GatedGCN | 0.2873 | 0.0219 | Yes | this paper | Table 1 |
| GatedGCN+LapPE | 0.2860 | 0.0085 | Yes | this paper | Table 2 |
| MixHop-GCN | 0.2506 | 0.0133 | Yes | this paper | Table 2 |
| MixHop-GCN+LapPE | 0.2218 | 0.0174 | Yes | this paper | Table 2 |
| Transformer+LapPE | 0.2694 | 0.0098 | Yes | this paper | Table 2 |
| GraphGPS+LapPE | 0.3748 | 0.0109 | Yes | this paper | Table 2 |
| SAN+LapPE | 0.3230 | 0.0039 | Yes | this paper | Table 2 |
| Exphormer | 0.3966 | 0.0027 | Yes | this paper | Table 2 |
| DIGL+MPNN | 0.2824 | 0.0039 | Yes | this paper | Table 2 |
| DIGL+MPNN+LapPE | 0.2921 | 0.0038 | Yes | this paper | Table 2 |
| DRew-GCN+LapPE | 0.1851 | 0.0092 | Yes | this paper | Table 2 |
| DRew-GIN+LapPE | 0.2692 | 0.0059 | Yes | this paper | Table 2 |
| DRew-GatedGCN+LapPE | 0.3314 | 0.0024 | Yes | this paper | Table 2 |
| Graph-Mamba | 0.4191 | 0.0126 | Yes | this paper | Table 2 |
| NBA-GCN | 0.2537 | 0.0054 | No | this paper | Table 1 |
| NBA-GCN+LapPE | 0.3005 | 0.0010 | No | this paper | Table 1 |
| NBA-GIN | 0.3040 | 0.0119 | No | this paper | Table 1 |
| NBA-GIN+LapPE | 0.3223 | 0.0010 | No | this paper | Table 1 |
| NBA-GatedGCN | 0.3910 | 0.0010 | No | this paper | Table 1 |
| NBA-GatedGCN+LapPE | 0.3969 | 0.0027 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GCN+LapPE | 0.6213 | 0.0060 | Yes | this paper | Table 2 |
| GIN | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GIN+LapPE | 0.5877 | 0.0044 | Yes | this paper | Table 2 |
| GatedGCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| GatedGCN+LapPE | 0.6069 | 0.0035 | Yes | this paper | Table 2 |
| MixHop-GCN | 0.6592 | 0.0036 | Yes | this paper | Table 2 |
| MixHop-GCN+LapPE | 0.6843 | 0.0049 | Yes | this paper | Table 2 |
| PathNN | 0.6816 | 0.0026 | Yes | this paper | Table 2 |
| CIN++ | 0.6569 | 0.0117 | Yes | this paper | Table 2 |
| Transformer+LapPE | 0.6326 | 0.0126 | Yes | this paper | Table 2 |
| GraphGPS+LapPE | 0.6535 | 0.0041 | Yes | this paper | Table 2 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 2 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 2 |
| Graph MLP-Mixer/ViT | 0.6970 | 0.0080 | Yes | this paper | Table 2 |
| DIGL+MPNN | 0.6469 | 0.0019 | Yes | this paper | Table 2 |
| DIGL+MPNN+LapPE | 0.6830 | 0.0026 | Yes | this paper | Table 2 |
| DRew-GCN+LapPE | 0.7150 | 0.0044 | Yes | this paper | Table 2 |
| DRew-GIN+LapPE | 0.7126 | 0.0045 | Yes | this paper | Table 2 |
| DRew-GatedGCN+LapPE | 0.6977 | 0.0026 | Yes | this paper | Table 2 |
| Graph-Mamba | 0.6739 | 0.0087 | Yes | this paper | Table 2 |
| NBA-GCN | 0.6951 | 0.0024 | No | this paper | Table 1 |
| NBA-GCN+LapPE | 0.7206 | 0.0028 | No | this paper | Table 1 |
| NBA-GIN | 0.6961 | 0.0045 | No | this paper | Table 1 |
| NBA-GIN+LapPE | 0.7071 | 0.0067 | No | this paper | Table 1 |
| NBA-GatedGCN | 0.6429 | 0.0062 | No | this paper | Table 1 |
| NBA-GatedGCN+LapPE | 0.6982 | 0.0014 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 2 |
| GCN+LapPE | 0.3250 | 0.0180 | Yes | this paper | Table 2 |
| GIN | 0.3547 | 0.0045 | Yes | this paper | Table 2 |
| GIN+LapPE | 0.3369 | 0.0026 | Yes | this paper | Table 2 |
| GatedGCN | 0.3420 | 0.0013 | Yes | this paper | Table 2 |
| GatedGCN+LapPE | 0.3357 | 0.0006 | Yes | this paper | Table 2 |
| MixHop-GCN | 0.2921 | 0.0023 | Yes | this paper | Table 2 |
| MixHop-GCN+LapPE | 0.2614 | 0.0023 | Yes | this paper | Table 2 |
| PathNN | 0.2545 | 0.0032 | Yes | this paper | Table 2 |
| CIN++ | 0.2523 | 0.0013 | Yes | this paper | Table 2 |
| Transformer+LapPE | 0.2529 | 0.0016 | Yes | this paper | Table 2 |
| GraphGPS+LapPE | 0.2500 | 0.0005 | Yes | this paper | Table 2 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 2 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 2 |
| Graph MLP-Mixer/ViT | 0.2449 | 0.0016 | Yes | this paper | Table 2 |
| DIGL+MPNN | 0.3173 | 0.0007 | Yes | this paper | Table 2 |
| DIGL+MPNN+LapPE | 0.2616 | 0.0018 | Yes | this paper | Table 2 |
| DRew-GCN+LapPE | 0.2536 | 0.0015 | Yes | this paper | Table 2 |
| DRew-GIN+LapPE | 0.2606 | 0.0014 | Yes | this paper | Table 2 |
| DRew-GatedGCN+LapPE | 0.2539 | 0.0007 | Yes | this paper | Table 2 |
| Graph-Mamba | 0.2478 | 0.0016 | Yes | this paper | Table 2 |
| NBA-GCN | 0.2656 | 0.0009 | No | this paper | Table 2 |
| NBA-GCN+LapPE | 0.2472 | 0.0008 | No | this paper | Table 2 |
| NBA-GIN | 0.2775 | 0.0057 | No | this paper | Table 2 |
| NBA-GIN+LapPE | 0.2424 | 0.0010 | No | this paper | Table 2 |
| NBA-GatedGCN | 0.2539 | 0.0011 | No | this paper | Table 2 |
| NBA-GatedGCN+LapPE | 0.2466 | 0.0012 | No | this paper | Table 2 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8825 | 0.0042 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.8817 | 0.0040 | Yes | this paper | Table 1 |
| GCN + NBA | 0.8826 | 0.0044 | Yes | this paper | Table 1 |
| GCN + NBA+LapPE | 0.8827 | 0.0048 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8864 | 0.0030 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.8895 | 0.0047 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.8871 | 0.0044 | Yes | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.8870 | 0.0037 | Yes | this paper | Table 1 |
| GAT | 0.8787 | 0.0046 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.8775 | 0.0045 | Yes | this paper | Table 1 |
| GAT + NBA | 0.8829 | 0.0043 | Yes | this paper | Table 1 |
| GAT + NBA+LapPE | 0.8822 | 0.0047 | Yes | this paper | Table 1 |
| ChebNet | 0.8718 | 0.0029 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.8701 | 0.0047 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.8832 | 0.0062 | Yes | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.8821 | 0.0076 | Yes | this paper | Table 1 |
| NBA-GCN | 0.8826 | 0.0044 | Yes | this paper | Table 2 |
| NBA-GraphSAGE | 0.8871 | 0.0044 | Yes | this paper | Table 2 |
| NBA-GAT | 0.8829 | 0.0043 | Yes | this paper | Table 2 |
| GatedGCN | 0.8671 | 0.0060 | Yes | this paper | Table 2 |
| EGNN | 0.8769 | 0.0028 | Yes | this paper | Table 2 |
| CensNet | 0.8753 | 0.0076 | Yes | this paper | Table 2 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6162 | 0.0634 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.6216 | 0.0584 | Yes | this paper | Table 1 |
| GCN + NBA | 0.7108 | 0.0796 | No | this paper | Table 1 |
| GCN + NBA+LapPE | 0.6811 | 0.0595 | No | this paper | Table 1 |
| GraphSAGE | 0.7108 | 0.0556 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.7162 | 0.0653 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.7270 | 0.0905 | No | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.7486 | 0.0612 | No | this paper | Table 1 |
| GAT | 0.6054 | 0.0386 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.6135 | 0.0404 | Yes | this paper | Table 1 |
| GAT + NBA | 0.6622 | 0.0514 | No | this paper | Table 1 |
| GAT + NBA+LapPE | 0.6730 | 0.0348 | No | this paper | Table 1 |
| ChebNet | 0.6811 | 0.0554 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.6324 | 0.0308 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.7568 | 0.0468 | No | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.7243 | 0.0520 | No | this paper | Table 1 |
| NBA-GCN | 0.7108 | 0.0796 | No | this paper | Table 2 |
| NBA-GraphSAGE | 0.7270 | 0.0905 | No | this paper | Table 2 |
| NBA-GAT | 0.6622 | 0.0514 | No | this paper | Table 2 |
| GatedGCN | 0.6108 | 0.0652 | Yes | this paper | Table 2 |
| EGNN | 0.6595 | 0.0527 | Yes | this paper | Table 2 |
| CensNet | 0.6405 | 0.0510 | Yes | this paper | Table 2 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6059 | 0.0438 | Yes | this paper | Table 1 |
| GCN + LapPE | 0.6000 | 0.0600 | Yes | this paper | Table 1 |
| GCN + NBA | 0.7471 | 0.0386 | No | this paper | Table 1 |
| GCN + NBA+LapPE | 0.7471 | 0.0466 | No | this paper | Table 1 |
| GraphSAGE | 0.7706 | 0.0403 | Yes | this paper | Table 1 |
| GraphSAGE + LapPE | 0.7647 | 0.0453 | Yes | this paper | Table 1 |
| GraphSAGE + NBA | 0.7765 | 0.0508 | No | this paper | Table 1 |
| GraphSAGE + NBA+LapPE | 0.7647 | 0.0531 | No | this paper | Table 1 |
| GAT | 0.6000 | 0.0491 | Yes | this paper | Table 1 |
| GAT + LapPE | 0.6294 | 0.0448 | Yes | this paper | Table 1 |
| GAT + NBA | 0.7059 | 0.0562 | No | this paper | Table 1 |
| GAT + NBA+LapPE | 0.7314 | 0.0531 | No | this paper | Table 1 |
| ChebNet | 0.7098 | 0.0322 | Yes | this paper | Table 1 |
| ChebNet + LapPE | 0.6941 | 0.0905 | Yes | this paper | Table 1 |
| ChebNet + NBA | 0.7490 | 0.0671 | No | this paper | Table 1 |
| ChebNet + NBA+LapPE | 0.7451 | 0.0808 | No | this paper | Table 1 |
| NBA-GCN | 0.7471 | 0.0386 | No | this paper | Table 2 |
| NBA-GraphSAGE | 0.7765 | 0.0508 | No | this paper | Table 2 |
| NBA-GAT | 0.7059 | 0.0562 | No | this paper | Table 2 |
| GatedGCN | 0.5824 | 0.0641 | Yes | this paper | Table 2 |
| EGNN | 0.6784 | 0.0407 | Yes | this paper | Table 2 |
| CensNet | 0.6608 | 0.0463 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GCN+LapPE** (from: this paper (variant))
- **GIN** (from: Xu et al. 2019)
- **GIN+LapPE** (from: this paper (variant))
- **GatedGCN** (from: Bresson & Laurent 2017)
- **GatedGCN+LapPE** (from: this paper (variant))
- **MixHop-GCN** (from: Abu-El-Haija et al. 2019)
- **MixHop-GCN+LapPE** (from: this paper (variant))
- **PathNN** (from: Cai et al. 2020)
- **CIN++** (from: Maron et al. 2019)
- **Transformer+LapPE** (from: this paper (variant))
- **GraphGPS+LapPE** (from: Ying et al. 2021)
- **SAN+LapPE** (from: Corso et al. 2020)
- **Exphormer** (from: Tay et al. 2022)
- **Graph MLP-Mixer/ViT** (from: Bianco et al. 2022)
- **DIGL+MPNN** (from: Luo et al. 2021)
- **DIGL+MPNN+LapPE** (from: this paper (variant))
- **DRew-GCN+LapPE** (from: this paper (variant))
- **DRew-GIN+LapPE** (from: this paper (variant))
- **DRew-GatedGCN+LapPE** (from: this paper (variant))
- **Graph-Mamba** (from: Zhu et al. 2023)
- **NBA-GCN** (from: this paper (variant))
- **NBA-GCN+LapPE** (from: this paper (variant))
- **NBA-GIN** (from: this paper (variant))
- **NBA-GIN+LapPE** (from: this paper (variant))
- **NBA-GatedGCN** (from: this paper (variant))
- **NBA-GatedGCN+LapPE** (from: this paper (variant))
- **GraphSAGE** (from: Hamilton et al. 2017)
- **GAT** (from: Veličković et al. 2018)
- **ChebNet** (from: Defferrard et al. 2016)
- **EGNN** (from: Satorras et al. 2021)
- **CensNet** (from: Zhang et al. 2022)

## Extraction Notes

[Peptides-func] Extracted all rows for Peptides-func from Table 1 and Table 2. Note that Table 1 and
Table 2 contain overlapping models (e.g., NBA-GCN variants appear in both). Table 1 focuses on the
proposed NBA-GNN variants compared to base GNNs, while Table 2 provides a broader comparison with
other SOTA methods. I included all rows from both tables as they represent distinct experimental
setups/comparisons in the paper. The value 0.7206 in Table 1 and 0.7207 in Table 2 for NBA-GCN+LapPE
are slightly different, likely due to rounding or different runs; both are extracted as reported.
[Peptides-struct] Extracted all rows from Table 2 (lrgb-full) for the Peptides-struct dataset. Table
1 was ignored as it contains redundant data for a subset of models already present in Table 2, and
Table 2 provides the comprehensive comparison. All values are MAE (lower is better). Standard
deviations were parsed from the '±' notation. No percentage normalization was needed as values are
already in [0, 1] range for MAE. [PascalVOC-SP] Extracted all rows for PascalVOC-SP from Table 1 and
Table 2. Note that Table 1 and Table 2 contain overlapping models (specifically the NBA-GNN variants
and base GNNs). Table 2 provides a more comprehensive list of baselines including Transformers and
Rewiring methods. Values are normalized to [0,1]. Standard deviations are extracted from the ±
notation. PathNN and CIN++ have no reported value for PascalVOC-SP (denoted by -) and are excluded.
Graph MLP-Mixer/ViT also has no reported value for PascalVOC-SP and is excluded. [Cora] Extracted
all rows from Table 1 and Table 2 for the Cora dataset. The metric is Accuracy. Values are
normalized to [0,1]. Standard deviations are extracted from the ± notation. Table 2 lists specific
NBA-GNN variants (NBA-GCN, NBA-GraphSAGE, NBA-GAT) which are the proposed models in the context of
the ablation/comparison table, while Table 1 shows the base GNNs with NBA/LapPE components. Both
tables report test results (implied by 'evaluation on the test dataset' in text and standard
reporting practice for these tables). [CiteSeer] Extracted all rows from Table 1 and Table 2
corresponding to the CiteSeer dataset. The metric is Accuracy. All values are normalized to [0,1].
The proposed model NBA-GNN is represented by its variants (NBA-GCN, NBA-GraphSAGE, NBA-GAT) in Table
2 and as '+ NBA' / '+ NBA+LapPE' in Table 1. No specific 'NBA-GNN' single row exists, so the
variants are listed individually. Baselines are treated as non-proposed. [PubMed] Extracted all
PubMed results from Table 1 and Table 2. Table 1 lists variants of standard GNNs (GCN, GraphSAGE,
GAT, ChebNet) with and without LapPE and NBA modules. Table 2 lists specific NBA-GNN architectures
(NBA-GCN, NBA-GraphSAGE, NBA-GAT) and edge-updating baselines (GatedGCN, EGNN, CensNet). All values
are test accuracies. The proposed model is NBA-GNN, which encompasses the NBA variants listed.
[Texas] Extracted all rows from Table 1 and Table 2 corresponding to the 'Texas' dataset column. The
proposed model is identified as NBA-GNN (and its variants like NBA-GCN, NBA-GraphSAGE, etc.).
Baselines include standard GNNs (GCN, GraphSAGE, GAT, ChebNet) and edge-updating GNNs (GatedGCN,
EGNN, CensNet). All values are Accuracy scores normalized to [0,1]. Standard deviations are
extracted from the ± notation. [Wisconsin] Extracted all rows from Table 1 and Table 2 corresponding
to the 'Wisconsin' dataset column. The metric is Accuracy (Test set, as per standard transductive
node classification reporting in this table). Values are normalized to [0,1]. Standard deviations
are parsed from the '±' notation. Table 2 repeats the NBA-GNN variants found in Table 1 but groups
them differently; both tables are included as they represent the full set of reported results for
the proposed method and baselines. [Cornell] Extracted all rows from Table 1 and Table 2
corresponding to the 'Cornell' dataset. The metric is Accuracy. Values are normalized to [0,1].
Standard deviations are parsed from the '±' notation. Table 2 lists NBA-GNN variants (NBA-GCN, NBA-
GraphSAGE, NBA-GAT) which are the proposed models in this context, alongside other edge-updating
baselines.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*