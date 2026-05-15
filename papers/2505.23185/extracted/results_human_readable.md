# Extraction: arXiv:2505.23185
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: IM-GatedGCN (0.5M params)
- Type: GNN

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Exphormer | 0.5351 | 0.0046 | Yes | this paper | Table 1 |
| GOAT | 0.4461 | 0.0050 | Yes | this paper | Table 1 |
| GPS₃₀GCN+Performer (RWSE) | 0.4808 | 0.0085 | Yes | this paper | Table 1 |
| GPS₃₀GAT+Performer (RWSE) | 0.4992 | 0.0068 | Yes | this paper | Table 1 |
| GT-sep | 0.5218 | 0.0080 | Yes | this paper | Table 1 |
| FSGNN | 0.5274 | 0.0083 | Yes | this paper | Table 1 |
| GBK-GNN | 0.4598 | 0.0071 | Yes | this paper | Table 1 |
| JacobiConv | 0.4355 | 0.0048 | Yes | this paper | Table 1 |
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| Gated-GCN | 0.4300 | 0.0032 | Yes | this paper | Table 1 |
| GAT | 0.4909 | 0.0063 | Yes | this paper | Table 1 |
| GAT-sep | 0.5270 | 0.0062 | Yes | this paper | Table 1 |
| CO-GNN(Σ, Σ) | 0.5128 | 0.0056 | Yes | this paper | Table 1 |
| CO-GNN(μ, μ) | 0.5417 | 0.0037 | Yes | this paper | Table 1 |
| IM-GCN | 0.5237 | 0.0066 | No | this paper | Table 1 |
| IM-GatedGCN | 0.5401 | 0.0027 | No | this paper | Table 1 |
| IM-GAT | 0.5116 | 0.0055 | No | this paper | Table 1 |
| IM-GAT-sep | 0.5397 | 0.0058 | No | this paper | Table 1 |
| IM-CO-GNN(Σ,Σ) | 0.5311 | 0.0059 | No | this paper | Table 1 |
| IM-CO-GNN(μ,μ) | 0.5443 | 0.0041 | No | this paper | Table 1 |
| GAT (LapPE) | 0.4490 | 0.0073 | Yes | this paper | Table 2 |
| GAT (RWSE) | 0.4858 | 0.0041 | Yes | this paper | Table 2 |
| GAT (DEG) | 0.5165 | 0.0060 | Yes | this paper | Table 2 |
| GCN (LapPE) | 0.4435 | 0.0036 | Yes | this paper | Table 2 |
| GCN (RWSE) | 0.4640 | 0.0055 | Yes | this paper | Table 2 |
| GCN (DEG) | 0.5001 | 0.0069 | Yes | this paper | Table 2 |
| SAGE | 0.5363 | 0.0039 | Yes | this paper | Table 2 |
| NAGphormer | 0.5126 | 0.0072 | Yes | this paper | Table 2 |
| GPS | 0.5310 | 0.0042 | Yes | this paper | Table 2 |
| GPS₃₀GCN+Performer | 0.4820 | 0.0067 | Yes | this paper | Table 2 |
| GPS₃₀GCN+Performer (DEG) | 0.4893 | 0.0047 | Yes | this paper | Table 2 |
| GPS₃₀GAT+Performer (LapPE) | 0.4886 | 0.0038 | Yes | this paper | Table 2 |
| GPS₃₀GAT+Performer | 0.5103 | 0.0060 | Yes | this paper | Table 2 |
| GT | 0.5117 | 0.0066 | Yes | this paper | Table 2 |
| CPGNN | 0.3979 | 0.0077 | Yes | this paper | Table 2 |
| FAGCN | 0.4412 | 0.0030 | Yes | this paper | Table 2 |
| GloGNN | 0.3689 | 0.0014 | Yes | this paper | Table 2 |
| GPR-GNN | 0.4488 | 0.0034 | Yes | this paper | Table 2 |
| H2GCN | 0.3647 | 0.0023 | Yes | this paper | Table 2 |
| IM-FAGCN | 0.5281 | 0.0035 | No | this paper | Table 2 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1338 | 0.0007 | Yes | this paper | Table 1 |
| IM-GCN | 0.1655 | 0.0013 | No | this paper | Table 1 |
| GINE | 0.2125 | 0.0009 | Yes | this paper | Table 1 |
| IM-GINE | 0.2289 | 0.0009 | No | this paper | Table 1 |
| GatedGCN | 0.2922 | 0.0018 | Yes | this paper | Table 1 |
| IM-GatedGCN | 0.3294 | 0.0021 | No | this paper | Table 1 |

### London — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4380 | 0.0030 | Yes | this paper | Table 1 |
| IM-GCN | 0.5380 | 0.0030 | No | this paper | Table 1 |

### Los Angeles — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4590 | 0.0100 | Yes | this paper | Table 1 |
| IM-GCN | 0.5980 | 0.0020 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Exphormer | 0.9074 | 0.0053 | Yes | this paper | Table 1 |
| GOAT | 0.8109 | 0.0102 | Yes | this paper | Table 1 |
| GPS₃₀GCN+Performer (RWSE) | 0.9288 | 0.0050 | Yes | this paper | Table 1 |
| GPS₃₀GAT+Performer (RWSE) | 0.9108 | 0.0058 | Yes | this paper | Table 1 |
| GT-sep | 0.9229 | 0.0047 | Yes | this paper | Table 1 |
| FSGNN | 0.9008 | 0.0070 | Yes | this paper | Table 1 |
| GBK-GNN | 0.9085 | 0.0058 | Yes | this paper | Table 1 |
| JacobiConv | 0.8966 | 0.0040 | Yes | this paper | Table 1 |
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8754 | 0.0122 | Yes | this paper | Table 1 |
| GAT | 0.9201 | 0.0068 | Yes | this paper | Table 1 |
| GAT-sep | 0.9391 | 0.0035 | Yes | this paper | Table 1 |
| CO-GNN(Σ, Σ) | 0.9509 | 0.0118 | Yes | this paper | Table 1 |
| CO-GNN(μ, μ) | 0.9731 | 0.0041 | Yes | this paper | Table 1 |
| IM-GCN | 0.9180 | 0.0058 | No | this paper | Table 1 |
| IM-GatedGCN | 0.9732 | 0.0083 | No | this paper | Table 1 |
| IM-GAT | 0.9268 | 0.0049 | No | this paper | Table 1 |
| IM-GAT-sep | 0.9615 | 0.0037 | No | this paper | Table 1 |
| IM-CO-GNN(Σ,Σ) | 0.9579 | 0.0096 | No | this paper | Table 1 |
| IM-CO-GNN(μ,μ) | 0.9739 | 0.0035 | No | this paper | Table 1 |
| GAT (LapPE) | 0.9350 | 0.0054 | Yes | this paper | Table 2 |
| GAT (RWSE) | 0.9253 | 0.0065 | Yes | this paper | Table 2 |
| GAT (DEG) | 0.9304 | 0.0062 | Yes | this paper | Table 2 |
| GCN (LapPE) | 0.9426 | 0.0049 | Yes | this paper | Table 2 |
| GCN (RWSE) | 0.9384 | 0.0048 | Yes | this paper | Table 2 |
| GCN (DEG) | 0.9414 | 0.0050 | Yes | this paper | Table 2 |
| SAGE | 0.9351 | 0.0057 | Yes | this paper | Table 2 |
| NAGphormer | 0.8419 | 0.0066 | Yes | this paper | Table 2 |
| GPS | 0.9063 | 0.0067 | Yes | this paper | Table 2 |
| GPS₃₀GCN+Performer | 0.9385 | 0.0041 | Yes | this paper | Table 2 |
| GPS₃₀GCN+Performer (DEG) | 0.9360 | 0.0047 | Yes | this paper | Table 2 |
| GPS₃₀GAT+Performer (LapPE) | 0.9262 | 0.0079 | Yes | this paper | Table 2 |
| GPS₃₀GAT+Performer | 0.9152 | 0.0046 | Yes | this paper | Table 2 |
| GT | 0.9185 | 0.0076 | Yes | this paper | Table 2 |
| CPGNN | 0.5203 | 0.0546 | Yes | this paper | Table 2 |
| FAGCN | 0.8817 | 0.0073 | Yes | this paper | Table 2 |
| GloGNN | 0.5108 | 0.0123 | Yes | this paper | Table 2 |
| GPR-GNN | 0.8624 | 0.0061 | Yes | this paper | Table 2 |
| H2GCN | 0.8971 | 0.0031 | Yes | this paper | Table 2 |
| IM-FAGCN | 0.9517 | 0.0084 | No | this paper | Table 2 |

### Paris — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4730 | 0.0020 | Yes | this paper | Table 1 |
| IM-GCN | 0.5440 | 0.0020 | No | this paper | Table 1 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | Yes | this paper | Table lrgb-sp |
| IM-GCN | 0.2672 | 0.0045 | Yes | this paper | Table lrgb-sp |
| GINE | 0.2718 | 0.0054 | Yes | this paper | Table lrgb-sp |
| IM-GINE | 0.2757 | 0.0013 | Yes | this paper | Table lrgb-sp |
| GatedGCN | 0.3880 | 0.0040 | Yes | this paper | Table lrgb-sp |
| IM-GatedGCN | 0.4180 | 0.0062 | No | this paper | Table lrgb-sp |
| Graph U-Net | 0.1801 | 0.0055 | Yes | this paper | Table hierarchical |
| DRew(GatedGCN) | 0.3909 | 0.0051 | Yes | this paper | Table hierarchical |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6860 | 0.0050 | Yes | this paper | Table 1 |
| IM-GCN | 0.6822 | 0.0088 | No | this paper | Table 1 |
| GINE | 0.6621 | 0.0067 | Yes | this paper | Table 1 |
| IM-GINE | 0.6745 | 0.0022 | No | this paper | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 1 |
| IM-GatedGCN | 0.6713 | 0.0051 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | Yes | this paper | Table 1 |
| IM-GCN | 0.2453 | 0.0009 | No | this paper | Table 1 |
| GINE | 0.2473 | 0.0017 | Yes | this paper | Table 1 |
| IM-GINE | 0.2477 | 0.0007 | No | this paper | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 1 |
| IM-GatedGCN | 0.2456 | 0.0010 | No | this paper | Table 1 |

### Questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Exphormer | 0.7394 | 0.0106 | Yes | this paper | Table 1 |
| GOAT | 0.7576 | 0.0166 | Yes | this paper | Table 1 |
| GPS₃₂GCN+Performer (RWSE) | 0.7645 | 0.0151 | Yes | this paper | Table 1 |
| GPS₃₂GAT+Performer (RWSE) | 0.7714 | 0.0149 | Yes | this paper | Table 1 |
| GT-sep | 0.7805 | 0.0093 | Yes | this paper | Table 1 |
| FSGNN | 0.7886 | 0.0092 | Yes | this paper | Table 1 |
| GBK-GNN | 0.7447 | 0.0086 | Yes | this paper | Table 1 |
| JacobiConv | 0.7388 | 0.0116 | Yes | this paper | Table 1 |
| GCN | 0.7609 | 0.0127 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7661 | 0.0113 | Yes | this paper | Table 1 |
| GAT | 0.7743 | 0.0120 | Yes | this paper | Table 1 |
| GAT-sep | 0.7679 | 0.0071 | Yes | this paper | Table 1 |
| CO-GNN(Σ, Σ) | 0.8002 | 0.0086 | Yes | this paper | Table 1 |
| CO-GNN(μ, μ) | 0.7654 | 0.0095 | Yes | this paper | Table 1 |
| IM-GCN | 0.7817 | 0.0089 | No | this paper | Table 1 |
| IM-GatedGCN | 0.7927 | 0.0091 | No | this paper | Table 1 |
| IM-GAT | 0.7798 | 0.0101 | No | this paper | Table 1 |
| IM-GAT-sep | 0.7792 | 0.0083 | No | this paper | Table 1 |
| IM-CO-GNN(Σ,Σ) | 0.8049 | 0.0092 | No | this paper | Table 1 |
| IM-CO-GNN(μ,μ) | 0.7892 | 0.0087 | No | this paper | Table 1 |
| GAT (LapPE) | 0.7655 | 0.0084 | Yes | this paper | Table 2 |
| GAT (RWSE) | 0.7783 | 0.0122 | Yes | this paper | Table 2 |
| GAT (DEG) | 0.7710 | 0.0123 | Yes | this paper | Table 2 |
| GCN (LapPE) | 0.7779 | 0.0134 | Yes | this paper | Table 2 |
| GCN (RWSE) | 0.7781 | 0.0140 | Yes | this paper | Table 2 |
| GCN (DEG) | 0.7696 | 0.0121 | Yes | this paper | Table 2 |
| SAGE | 0.7644 | 0.0062 | Yes | this paper | Table 2 |
| NAGphormer | 0.6817 | 0.0153 | Yes | this paper | Table 2 |
| GPS | 0.7173 | 0.0147 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer | 0.7785 | 0.0125 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer (DEG) | 0.7424 | 0.0118 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer (LapPE) | 0.7671 | 0.0098 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer | 0.7651 | 0.0119 | Yes | this paper | Table 2 |
| GT | 0.7795 | 0.0068 | Yes | this paper | Table 2 |
| CPGNN | 0.6596 | 0.0195 | Yes | this paper | Table 2 |
| FAGCN | 0.7724 | 0.0126 | Yes | this paper | Table 2 |
| GloGNN | 0.6574 | 0.0119 | Yes | this paper | Table 2 |
| GPR-GNN | 0.5548 | 0.0091 | Yes | this paper | Table 2 |
| H2GCN | 0.6359 | 0.0146 | Yes | this paper | Table 2 |
| IM-FAGCN | 0.7817 | 0.0106 | No | this paper | Table 2 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Exphormer | 0.8903 | 0.0037 | Yes | this paper | Table 1 |
| GOAT | 0.7159 | 0.0125 | Yes | this paper | Table 1 |
| GPS₃₂GCN+Performer (RWSE) | 0.8472 | 0.0065 | Yes | this paper | Table 1 |
| GPS₃₂GAT+Performer (RWSE) | 0.8704 | 0.0058 | Yes | this paper | Table 1 |
| GT-sep | 0.8732 | 0.0039 | Yes | this paper | Table 1 |
| FSGNN | 0.7992 | 0.0056 | Yes | this paper | Table 1 |
| GBK-GNN | 0.7457 | 0.0047 | Yes | this paper | Table 1 |
| JacobiConv | 0.7114 | 0.0042 | Yes | this paper | Table 1 |
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7446 | 0.0054 | Yes | this paper | Table 1 |
| GAT | 0.8087 | 0.0030 | Yes | this paper | Table 1 |
| GAT-sep | 0.8875 | 0.0041 | Yes | this paper | Table 1 |
| CO-GNN(Σ, Σ) | 0.9157 | 0.0032 | Yes | this paper | Table 1 |
| CO-GNN(μ, μ) | 0.9137 | 0.0035 | Yes | this paper | Table 1 |
| IM-GCN | 0.8353 | 0.0057 | No | this paper | Table 1 |
| IM-GatedGCN | 0.9082 | 0.0059 | No | this paper | Table 1 |
| IM-GAT | 0.8448 | 0.0032 | No | this paper | Table 1 |
| IM-GAT-sep | 0.8993 | 0.0034 | No | this paper | Table 1 |
| IM-CO-GNN(Σ,Σ) | 0.9208 | 0.0033 | No | this paper | Table 1 |
| IM-CO-GNN(μ,μ) | 0.9200 | 0.0041 | No | this paper | Table 1 |
| GAT (LapPE) | 0.8480 | 0.0046 | Yes | this paper | Table 2 |
| GAT (RWSE) | 0.8662 | 0.0053 | Yes | this paper | Table 2 |
| GAT (DEG) | 0.8551 | 0.0056 | Yes | this paper | Table 2 |
| GCN (LapPE) | 0.8337 | 0.0055 | Yes | this paper | Table 2 |
| GCN (RWSE) | 0.8484 | 0.0055 | Yes | this paper | Table 2 |
| GCN (DEG) | 0.8421 | 0.0047 | Yes | this paper | Table 2 |
| SAGE | 0.8574 | 0.0067 | Yes | this paper | Table 2 |
| NAGphormer | 0.7434 | 0.0077 | Yes | this paper | Table 2 |
| GPS | 0.8200 | 0.0061 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer | 0.8396 | 0.0053 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer (DEG) | 0.8338 | 0.0068 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer (LapPE) | 0.8593 | 0.0052 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer | 0.8554 | 0.0058 | Yes | this paper | Table 2 |
| GT | 0.8651 | 0.0073 | Yes | this paper | Table 2 |
| CPGNN | 0.6396 | 0.0062 | Yes | this paper | Table 2 |
| FAGCN | 0.6522 | 0.0056 | Yes | this paper | Table 2 |
| GloGNN | 0.5963 | 0.0069 | Yes | this paper | Table 2 |
| GPR-GNN | 0.6485 | 0.0027 | Yes | this paper | Table 2 |
| H2GCN | 0.6011 | 0.0052 | Yes | this paper | Table 2 |
| IM-FAGCN | 0.8626 | 0.0044 | No | this paper | Table 2 |

### Shanghai — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5240 | 0.0030 | Yes | this paper | Table 1 |
| IM-GCN | 0.6340 | 0.0080 | No | this paper | Table 1 |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Exphormer | 0.8377 | 0.0078 | Yes | this paper | Table 1 |
| GOAT | 0.8311 | 0.0104 | Yes | this paper | Table 1 |
| GPS₃₂GCN+Performer (RWSE) | 0.8481 | 0.0086 | Yes | this paper | Table 1 |
| GPS₃₂GAT+Performer (RWSE) | 0.8438 | 0.0091 | Yes | this paper | Table 1 |
| GT-sep | 0.8252 | 0.0092 | Yes | this paper | Table 1 |
| FSGNN | 0.8276 | 0.0061 | Yes | this paper | Table 1 |
| GBK-GNN | 0.8101 | 0.0067 | Yes | this paper | Table 1 |
| JacobiConv | 0.6866 | 0.0065 | Yes | this paper | Table 1 |
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7731 | 0.0114 | Yes | this paper | Table 1 |
| GAT | 0.8370 | 0.0047 | Yes | this paper | Table 1 |
| GAT-sep | 0.8378 | 0.0043 | Yes | this paper | Table 1 |
| CO-GNN(Σ, Σ) | 0.8336 | 0.0089 | Yes | this paper | Table 1 |
| CO-GNN(μ, μ) | 0.8445 | 0.0117 | Yes | this paper | Table 1 |
| IM-GCN | 0.8417 | 0.0071 | No | this paper | Table 1 |
| IM-GatedGCN | 0.8510 | 0.0084 | No | this paper | Table 1 |
| IM-GAT | 0.8521 | 0.0043 | No | this paper | Table 1 |
| IM-GAT-sep | 0.8544 | 0.0040 | No | this paper | Table 1 |
| IM-CO-GNN(Σ,Σ) | 0.8525 | 0.0103 | No | this paper | Table 1 |
| IM-CO-GNN(μ,μ) | 0.8577 | 0.0105 | No | this paper | Table 1 |
| GAT (LapPE) | 0.8499 | 0.0054 | Yes | this paper | Table 2 |
| GAT (RWSE) | 0.8502 | 0.0067 | Yes | this paper | Table 2 |
| GAT (DEG) | 0.8422 | 0.0081 | Yes | this paper | Table 2 |
| GCN (LapPE) | 0.8495 | 0.0078 | Yes | this paper | Table 2 |
| GCN (RWSE) | 0.8511 | 0.0077 | Yes | this paper | Table 2 |
| GCN (DEG) | 0.8251 | 0.0083 | Yes | this paper | Table 2 |
| SAGE | 0.8243 | 0.0044 | Yes | this paper | Table 2 |
| NAGphormer | 0.7832 | 0.0095 | Yes | this paper | Table 2 |
| GPS | 0.8371 | 0.0048 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer | 0.8472 | 0.0077 | Yes | this paper | Table 2 |
| GPS₃₂GCN+Performer (DEG) | 0.8049 | 0.0097 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer (LapPE) | 0.8462 | 0.0054 | Yes | this paper | Table 2 |
| GPS₃₂GAT+Performer | 0.8245 | 0.0089 | Yes | this paper | Table 2 |
| GT | 0.8323 | 0.0064 | Yes | this paper | Table 2 |
| CPGNN | 0.7336 | 0.0101 | Yes | this paper | Table 2 |
| FAGCN | 0.7775 | 0.0105 | Yes | this paper | Table 2 |
| GloGNN | 0.7339 | 0.0117 | Yes | this paper | Table 2 |
| GPR-GNN | 0.7294 | 0.0097 | Yes | this paper | Table 2 |
| H2GCN | 0.7335 | 0.0101 | Yes | this paper | Table 2 |
| IM-FAGCN | 0.8449 | 0.0097 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN**
- **IM-GCN**
- **GINE**
- **IM-GINE**
- **GatedGCN**
- **Graph U-Net**
- **DRew(GatedGCN)**
- **Exphormer**
- **GOAT**
- **GPS**
- **GT**
- **GT-sep**
- **FSGNN**
- **GBK-GNN**
- **JacobiConv**
- **Gated-GCN**
- **GAT**
- **GAT-sep**
- **CO-GNN**
- **SAGE**
- **CPGNN**
- **FAGCN**
- **GloGNN**
- **GPR-GNN**
- **H2GCN**
- **NAGphormer**

## Extraction Notes

[PascalVOC-SP] Extracted all rows for PascalVOC-SP. The 'scales' column in Table lrgb-sp represents
different configurations of the IM- models; all were included as they are reported results for the
dataset. Params budget of 500k mentioned in caption used for proposed model params. [COCO-SP]
Extracted all rows for COCO-SP from Table 1. The 'scales' column was treated as part of the model
configuration. The budget of 500k params mentioned in the caption was used for params_millions.
[Peptides-func] Extracted only Peptides-func AP results as requested. The 'scales' column was
treated as part of the model configuration for the IM- variants. Params budget of 500k mentioned in
caption. [Peptides-struct] Extracted only Peptides-struct MAE results. The 'scales' column was
treated as part of the model configuration; since no specific 'default' scale was defined, all scale
variants for the IM- models were included as they represent the proposed multiscale approach.
[Paris] The proposed model is referred to as IM-MPNN in the text, while the table lists IM-GCN
(which is a specific instance of the proposed IM-MPNN framework). Extracted all scales for IM-GCN as
they represent the model's performance across different configurations on the Paris dataset.
[Shanghai] Extracted all IM-GCN scale variants for the Shanghai dataset as they represent the
proposed model's performance across different configurations. [Los Angeles] Extracted only the 'Los
Angeles' column as requested. The 'scales' column in the table represents different configurations
of the proposed IM-GCN model; all were included as they are variations of the proposed architecture.
[London] Extracted results for London dataset. IM-GCN is listed with different 'scales' (1, 2, 3,
4), all of which are treated as versions of the proposed model. [Roman-empire] Extracted all models
for the Roman-empire dataset from both Table 1 and Table 2. Normalised accuracy percentages to [0,
1] range. [Amazon-ratings] Extracted all models for Amazon-ratings from both Table 1 and Table 2.
Normalised accuracy percentages to [0, 1] range. [Minesweeper] Extracted all models for the
Minesweeper dataset from both Table 1 and Table 2. Normalized AUC values from percentages to [0, 1]
range. [Tolokers] Extracted all models for the Tolokers dataset from both Table 1 and Table 2.
Normalised AUC values from percentages to [0, 1] range. Identified IM- variants as proposed models.
[Questions] Extracted all results for the 'Questions' dataset from both Table 1 and Table 2.
Normalized AUC to ROC-AUC as per primary metric instruction. Values were divided by 100 to fit the
[0, 1] range.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*