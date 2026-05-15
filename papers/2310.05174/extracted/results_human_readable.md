# Extraction: arXiv:2310.05174
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: HES-GSL
- Type: GNN

## Results

### ACM — Micro-F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9018 | 0.0061 | Yes | this paper | Table 1 |
| GAT | 0.9146 | 0.0062 | Yes | this paper | Table 1 |
| HAN | 0.9147 | 0.0022 | Yes | this paper | Table 1 |
| LDS | 0.9205 | 0.0026 | Yes | this paper | Table 1 |
| GRCN | 0.9294 | 0.0018 | Yes | this paper | Table 1 |
| IDGL | 0.9163 | 0.0124 | Yes | this paper | Table 1 |
| ProGNN | 0.9050 | 0.0129 | Yes | this paper | Table 1 |
| GEN | 0.8788 | 0.0261 | Yes | this paper | Table 1 |
| STABLE | 0.8338 | 0.0451 | Yes | this paper | Table 1 |
| SUBLIME | 0.9213 | 0.0037 | Yes | this paper | Table 1 |
| NodeFormer | 0.9060 | 0.0095 | Yes | this paper | Table 1 |
| GSR | 0.9211 | 0.0099 | Yes | this paper | Table 1 |
| GTN | 0.9194 | 0.0039 | Yes | this paper | Table 1 |
| HGSL | 0.9313 | 0.0051 | No | this paper | Table 1 |

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3001 | 0.0077 | Yes | this paper | Table 1 |
| GAT | 0.2891 | 0.0083 | Yes | this paper | Table 1 |
| GPRGNN | 0.3409 | 0.0109 | Yes | this paper | Table 1 |
| LDS | 0.3105 | 0.0131 | Yes | this paper | Table 1 |
| GRCN | 0.2997 | 0.0071 | Yes | this paper | Table 1 |
| ProGNN | 0.2235 | 0.0088 | Yes | this paper | Table 1 |
| IDGL | 0.2816 | 0.0141 | Yes | this paper | Table 1 |
| GEN | 0.2721 | 0.0205 | Yes | this paper | Table 1 |
| CoGSL | 0.3295 | 0.0120 | Yes | this paper | Table 1 |
| SUBLIME | 0.3357 | 0.0068 | Yes | this paper | Table 1 |
| STABLE | 0.3018 | 0.0100 | Yes | this paper | Table 1 |
| NodeFormer | 0.2551 | 0.0177 | Yes | this paper | Table 1 |
| GSR | 0.3023 | 0.0038 | Yes | this paper | Table 1 |
| HES-GSL | 0.3673 | 0.0076 | No | this paper | Table 2 |
| MLP | 0.3549 | 0.0104 | Yes | this paper | Table 2 |
| GCN_knn | 0.3298 | 0.0049 | Yes | this paper | Table 2 |
| GAT_knn | 0.3167 | 0.0119 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.3471 | 0.0151 | Yes | this paper | Table 2 |
| GRCN_knn | 0.3083 | 0.0076 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.3156 | 0.0114 | Yes | this paper | Table 2 |
| IDGL_knn | 0.3307 | 0.0137 | Yes | this paper | Table 2 |
| GEN_knn | 0.3128 | 0.0106 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.3452 | 0.0156 | Yes | this paper | Table 2 |
| GSR_knn | 0.3373 | 0.0112 | Yes | this paper | Table 2 |
| SLAPS | 0.3716 | 0.0091 | Yes | this paper | Table 2 |

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7696 | 0.0228 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.7714 | 0.0159 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.7806 | 0.0217 | No | this paper | Table 1 |
| GAT | 0.7908 | 0.0136 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.7754 | 0.0185 | Yes | this paper | Table 1 |
| SAGE | 0.7558 | 0.0204 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.7774 | 0.0152 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.7864 | 0.0147 | No | this paper | Table 1 |
| GIN | 0.7986 | 0.0164 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.7725 | 0.0234 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.8014 | 0.0151 | No | this paper | Table 1 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7136 | 0.0031 | Yes | this paper | Table 1 |
| GAT | 0.7069 | 0.0058 | Yes | this paper | Table 1 |
| GPRGNN | 0.7164 | 0.0049 | Yes | this paper | Table 1 |
| LDS | 0.7355 | 0.0054 | Yes | this paper | Table 1 |
| GRCN | 0.7243 | 0.0061 | Yes | this paper | Table 1 |
| ProGNN | 0.6851 | 0.0052 | Yes | this paper | Table 1 |
| IDGL | 0.7220 | 0.0118 | Yes | this paper | Table 1 |
| GEN | 0.7115 | 0.0181 | Yes | this paper | Table 1 |
| CoGSL | 0.7309 | 0.0042 | Yes | this paper | Table 1 |
| SUBLIME | 0.7230 | 0.0109 | Yes | this paper | Table 1 |
| STABLE | 0.6891 | 0.0101 | Yes | this paper | Table 1 |
| NodeFormer | 0.7131 | 0.0098 | Yes | this paper | Table 1 |
| GSR | 0.7110 | 0.0025 | Yes | this paper | Table 1 |
| MLP | 0.5952 | 0.0064 | Yes | this paper | Table 2 |
| GCN_knn | 0.6833 | 0.0089 | Yes | this paper | Table 2 |
| GAT_knn | 0.6805 | 0.0112 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.7029 | 0.0054 | Yes | this paper | Table 2 |
| LDS_knn | 0.7243 | 0.0061 | Yes | this paper | Table 2 |
| GRCN_knn | 0.6841 | 0.0050 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.6455 | 0.0095 | Yes | this paper | Table 2 |
| IDGL_knn | 0.6633 | 0.0084 | Yes | this paper | Table 2 |
| GEN_knn | 0.6729 | 0.0117 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.6872 | 0.0084 | Yes | this paper | Table 2 |
| GSR_knn | 0.6677 | 0.0062 | Yes | this paper | Table 2 |
| SLAPS | 0.7071 | 0.0113 | Yes | this paper | Table 2 |
| HES-GSL | 0.7012 | 0.0111 | Yes | this paper | Table 2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8146 | 0.0058 | Yes | this paper | Table 1 |
| GAT | 0.8141 | 0.0077 | Yes | this paper | Table 1 |
| GPRGNN | 0.8366 | 0.0077 | Yes | this paper | Table 1 |
| LDS | 0.8301 | 0.0041 | Yes | this paper | Table 1 |
| GRCN | 0.8387 | 0.0049 | Yes | this paper | Table 1 |
| ProGNN | 0.8030 | 0.0057 | Yes | this paper | Table 1 |
| IDGL | 0.8388 | 0.0042 | Yes | this paper | Table 1 |
| GEN | 0.8021 | 0.0172 | Yes | this paper | Table 1 |
| CoGSL | 0.8176 | 0.0024 | Yes | this paper | Table 1 |
| SUBLIME | 0.8340 | 0.0042 | Yes | this paper | Table 1 |
| STABLE | 0.8020 | 0.0068 | Yes | this paper | Table 1 |
| NodeFormer | 0.8028 | 0.0082 | Yes | this paper | Table 1 |
| GSR | 0.8248 | 0.0043 | Yes | this paper | Table 1 |
| HES-GSL | 0.7368 | 0.0104 | No | this paper | Table 2 |
| MLP | 0.5855 | 0.0080 | Yes | this paper | Table 2 |
| GCN_knn | 0.6610 | 0.0044 | Yes | this paper | Table 2 |
| GAT_knn | 0.6462 | 0.0104 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.6927 | 0.0062 | Yes | this paper | Table 2 |
| GRCN_knn | 0.6948 | 0.0066 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.6711 | 0.0056 | Yes | this paper | Table 2 |
| IDGL_knn | 0.6974 | 0.0057 | Yes | this paper | Table 2 |
| GEN_knn | 0.6695 | 0.0140 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.6665 | 0.0037 | Yes | this paper | Table 2 |
| GSR_knn | 0.6628 | 0.0059 | Yes | this paper | Table 2 |
| SLAPS | 0.7228 | 0.0097 | Yes | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4784 | 0.0555 | Yes | this paper | Table 1 |
| GAT | 0.4622 | 0.0633 | Yes | this paper | Table 1 |
| GPRGNN | 0.7676 | 0.0530 | Yes | this paper | Table 1 |
| LDS | 0.4787 | 0.0714 | Yes | this paper | Table 1 |
| GRCN | 0.5432 | 0.0824 | Yes | this paper | Table 1 |
| ProGNN | 0.5405 | 0.0616 | Yes | this paper | Table 1 |
| IDGL | 0.5000 | 0.0898 | Yes | this paper | Table 1 |
| GEN | 0.5702 | 0.0719 | Yes | this paper | Table 1 |
| CoGSL | 0.5216 | 0.0321 | Yes | this paper | Table 1 |
| SUBLIME | 0.7054 | 0.0598 | Yes | this paper | Table 1 |
| STABLE | 0.4403 | 0.0405 | Yes | this paper | Table 1 |
| NodeFormer | 0.4270 | 0.0551 | Yes | this paper | Table 1 |
| GSR | 0.4432 | 0.0216 | Yes | this paper | Table 1 |
| HES-GSL | 0.6622 | 0.0619 | No | this paper | Table 2 |
| MLP | 0.7135 | 0.0619 | Yes | this paper | Table 2 |
| GCN_knn | 0.7514 | 0.0265 | Yes | this paper | Table 2 |
| GAT_knn | 0.7405 | 0.0516 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.7568 | 0.0270 | Yes | this paper | Table 2 |
| GRCN_knn | 0.7108 | 0.0684 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.7135 | 0.0404 | Yes | this paper | Table 2 |
| IDGL_knn | 0.7270 | 0.0475 | Yes | this paper | Table 2 |
| GEN_knn | 0.7108 | 0.0554 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.7027 | 0.0342 | Yes | this paper | Table 2 |
| GSR_knn | 0.7027 | 0.0362 | Yes | this paper | Table 2 |
| SLAPS | 0.7459 | 0.0367 | Yes | this paper | Table 2 |

### DBLP — Micro-F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9099 | 0.0028 | Yes | this paper | Table 1 |
| GAT | 0.9113 | 0.0040 | Yes | this paper | Table 1 |
| HAN | 0.9147 | 0.0022 | Yes | this paper | Table 1 |
| LDS | 0.8874 | 0.0085 | Yes | this paper | Table 1 |
| GRCN | 0.8943 | 0.0044 | Yes | this paper | Table 1 |
| IDGL | 0.9061 | 0.0056 | Yes | this paper | Table 1 |
| ProGNN | 0.8483 | 0.0136 | Yes | this paper | Table 1 |
| GEN | 0.9065 | 0.0071 | Yes | this paper | Table 1 |
| STABLE | 0.7642 | 0.0195 | Yes | this paper | Table 1 |
| SUBLIME | 0.9182 | 0.0027 | Yes | this paper | Table 1 |
| NodeFormer | 0.8056 | 0.0062 | Yes | this paper | Table 1 |
| GSR | 0.7769 | 0.0042 | Yes | this paper | Table 1 |
| GTN | 0.9148 | 0.0039 | Yes | this paper | Table 1 |
| HGSL | 0.9249 | 0.0035 | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7320 | 0.0429 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.7190 | 0.0448 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.7410 | 0.0455 | No | this paper | Table 1 |
| GAT | 0.7230 | 0.0226 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.7210 | 0.0569 | Yes | this paper | Table 1 |
| SAGE | 0.7260 | 0.0369 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.7300 | 0.0478 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.7150 | 0.0524 | No | this paper | Table 1 |
| GIN | 0.7300 | 0.0267 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.6990 | 0.0390 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.7350 | 0.0625 | No | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4985 | 0.0384 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.4905 | 0.0552 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.5107 | 0.0200 | No | this paper | Table 1 |
| GAT | 0.4890 | 0.0298 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.4906 | 0.0455 | Yes | this paper | Table 1 |
| SAGE | 0.4855 | 0.0203 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.4879 | 0.0506 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.4967 | 0.0309 | No | this paper | Table 1 |
| GIN | 0.5030 | 0.0352 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.4997 | 0.0365 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.4867 | 0.0258 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7392 | 0.0884 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.6863 | 0.0515 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.7807 | 0.1085 | No | this paper | Table 1 |
| GAT | 0.7871 | 0.0751 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.7713 | 0.0995 | Yes | this paper | Table 1 |
| SAGE | 0.6865 | 0.0431 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.7281 | 0.1141 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.7713 | 0.0329 | No | this paper | Table 1 |
| GIN | 0.8719 | 0.0805 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.8518 | 0.1011 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.7392 | 0.0624 | No | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6752 | 0.0671 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.6568 | 0.0853 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.7080 | 0.0425 | No | this paper | Table 1 |
| GAT | 0.6863 | 0.0624 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.6709 | 0.0843 | Yes | this paper | Table 1 |
| SAGE | 0.6447 | 0.0715 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.6661 | 0.0448 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.7332 | 0.0206 | No | this paper | Table 1 |
| GIN | 0.6907 | 0.0562 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.7515 | 0.0572 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.6937 | 0.0395 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5831 | 0.0028 | Yes | this paper | Table 1 |
| GAT | 0.4559 | 0.0035 | Yes | this paper | Table 1 |
| GIN | 0.6092 | 0.0088 | Yes | this paper | Table 1 |
| SAGE | 0.5941 | 0.0057 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.5205 | 0.0240 | No | this paper | Table 1 |
| VIB-GSL (GAT) | 0.4264 | 0.0033 | No | this paper | Table 1 |
| VIB-GSL (GIN) | 0.4761 | 0.0093 | No | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.5411 | 0.0074 | No | this paper | Table 1 |
| HGP-SL (GCN) | 0.5216 | 0.0094 | Yes | this paper | Table 1 |
| HGP-SL (GIN) | 0.5530 | 0.0088 | Yes | this paper | Table 1 |
| HGP-SL (SAGE) | 0.5348 | 0.0071 | Yes | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3566 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.4375 | 0.0036 | Yes | this paper | Table 1 |
| GIN | 0.3647 | 0.0028 | Yes | this paper | Table 1 |
| SAGE | 0.3716 | 0.0011 | Yes | this paper | Table 1 |
| VIB-GSL (GCN) | 0.3089 | 0.0036 | Yes | this paper | Table 1 |
| VIB-GSL (GAT) | 0.3992 | 0.0129 | Yes | this paper | Table 1 |
| VIB-GSL (GIN) | 0.3032 | 0.0011 | Yes | this paper | Table 1 |
| VIB-GSL (SAGE) | 0.3063 | 0.0014 | Yes | this paper | Table 1 |
| HGP-SL (GCN) | 0.2935 | 0.0104 | No | this paper | Table 1 |
| HGP-SL (GIN) | 0.2786 | 0.0018 | No | this paper | Table 1 |
| HGP-SL (SAGE) | 0.2794 | 0.0058 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5783 | 0.0276 | Yes | this paper | Table 1 |
| GAT | 0.5405 | 0.0735 | Yes | this paper | Table 1 |
| GPRGNN | 0.8514 | 0.0368 | Yes | this paper | Table 1 |
| LDS | 0.5892 | 0.0432 | Yes | this paper | Table 1 |
| GRCN | 0.6216 | 0.0705 | Yes | this paper | Table 1 |
| ProGNN | 0.4837 | 0.1217 | Yes | this paper | Table 1 |
| IDGL | 0.6243 | 0.0609 | Yes | this paper | Table 1 |
| GEN | 0.6594 | 0.0138 | Yes | this paper | Table 1 |
| CoGSL | 0.5946 | 0.0436 | Yes | this paper | Table 1 |
| SUBLIME | 0.7703 | 0.0423 | Yes | this paper | Table 1 |
| STABLE | 0.5524 | 0.0604 | Yes | this paper | Table 1 |
| NodeFormer | 0.5892 | 0.0432 | Yes | this paper | Table 1 |
| GSR | 0.6081 | 0.0487 | Yes | this paper | Table 1 |
| MLP | 0.8027 | 0.0593 | Yes | this paper | Table 2 |
| GCN_knn | 0.7595 | 0.0443 | Yes | this paper | Table 2 |
| GAT_knn | 0.7649 | 0.0499 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.8108 | 0.0418 | Yes | this paper | Table 2 |
| GRCN_knn | 0.7432 | 0.0502 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.7189 | 0.0569 | Yes | this paper | Table 2 |
| IDGL_knn | 0.7540 | 0.0475 | Yes | this paper | Table 2 |
| GEN_knn | 0.7459 | 0.0346 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.7270 | 0.0426 | Yes | this paper | Table 2 |
| GSR_knn | 0.7486 | 0.0363 | Yes | this paper | Table 2 |
| SLAPS | 0.7919 | 0.0499 | Yes | this paper | Table 2 |
| HES-GSL | 0.7405 | 0.0642 | No | this paper | Table 2 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5745 | 0.0430 | Yes | this paper | Table 1 |
| GAT | 0.5765 | 0.0775 | Yes | this paper | Table 1 |
| GPRGNN | 0.8333 | 0.0342 | Yes | this paper | Table 1 |
| LDS | 0.6170 | 0.0358 | Yes | this paper | Table 1 |
| GRCN | 0.5608 | 0.0719 | Yes | this paper | Table 1 |
| ProGNN | 0.6254 | 0.0756 | Yes | this paper | Table 1 |
| IDGL | 0.5941 | 0.0411 | Yes | this paper | Table 1 |
| GEN | 0.6607 | 0.0372 | Yes | this paper | Table 1 |
| CoGSL | 0.5882 | 0.0152 | Yes | this paper | Table 1 |
| SUBLIME | 0.7882 | 0.0655 | Yes | this paper | Table 1 |
| STABLE | 0.5300 | 0.0527 | Yes | this paper | Table 1 |
| NodeFormer | 0.4843 | 0.0702 | Yes | this paper | Table 1 |
| GSR | 0.5686 | 0.0124 | Yes | this paper | Table 1 |
| MLP | 0.8471 | 0.0314 | Yes | this paper | Table 2 |
| GCN_knn | 0.8412 | 0.0397 | Yes | this paper | Table 2 |
| GAT_knn | 0.8216 | 0.0406 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.8412 | 0.0322 | Yes | this paper | Table 2 |
| GRCN_knn | 0.7863 | 0.0492 | Yes | this paper | Table 2 |
| ProGNN_knn | 0.7294 | 0.0793 | Yes | this paper | Table 2 |
| IDGL_knn | 0.7921 | 0.0394 | Yes | this paper | Table 2 |
| GEN_knn | 0.8176 | 0.0291 | Yes | this paper | Table 2 |
| CoGSL_knn | 0.7696 | 0.0525 | Yes | this paper | Table 2 |
| GSR_knn | 0.7862 | 0.0591 | Yes | this paper | Table 2 |
| SLAPS | 0.8196 | 0.0326 | Yes | this paper | Table 2 |
| HES-GSL | 0.7961 | 0.0528 | No | this paper | Table 2 |

### Yelp — Macro-F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7801 | 0.0189 | Yes | this paper | Table 1 |
| GAT | 0.8212 | 0.0147 | Yes | this paper | Table 1 |
| HAN | 0.8849 | 0.0173 | Yes | this paper | Table 1 |
| LDS | 0.7598 | 0.0235 | Yes | this paper | Table 1 |
| GRCN | 0.7605 | 0.0105 | Yes | this paper | Table 1 |
| IDGL | 0.7698 | 0.0578 | Yes | this paper | Table 1 |
| ProGNN | 0.5176 | 0.0146 | Yes | this paper | Table 1 |
| GEN | 0.8043 | 0.0378 | Yes | this paper | Table 1 |
| STABLE | 0.7148 | 0.0471 | Yes | this paper | Table 1 |
| SUBLIME | 0.7968 | 0.0079 | Yes | this paper | Table 1 |
| NodeFormer | 0.9169 | 0.0065 | Yes | this paper | Table 1 |
| GSR | 0.8385 | 0.0076 | Yes | this paper | Table 1 |
| GTN | 0.9298 | 0.0052 | Yes | this paper | Table 1 |
| HGSL | 0.9279 | 0.0044 | No | this paper | Table 1 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7077 | 0.0019 | Yes | this paper | Table 1 |
| GAT | 0.6990 | 0.0025 | Yes | this paper | Table 1 |
| GPRGNN | 0.5080 | 0.0029 | Yes | this paper | Table 1 |
| SUBLIME | 0.7175 | 0.0036 | Yes | this paper | Table 1 |
| NodeFormer | 0.5540 | 0.0023 | Yes | this paper | Table 1 |
| MLP | 0.5521 | 0.0011 | Yes | this paper | Table 2 |
| GCN_knn | 0.5521 | 0.0022 | Yes | this paper | Table 2 |
| GAT_knn | 0.5592 | 0.0030 | Yes | this paper | Table 2 |
| GPRGNN_knn | 0.5139 | 0.0013 | Yes | this paper | Table 2 |
| SLAPS | 0.5519 | 0.0021 | Yes | this paper | Table 2 |
| HES-GSL | 0.5646 | 0.0027 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GPRGNN** (from: Wang et al. 2020)
- **LDS** (from: null)
- **GRCN** (from: null)
- **ProGNN** (from: Jiang et al. 2020)
- **IDGL** (from: Luo et al. 2021)
- **GEN** (from: null)
- **CoGSL** (from: null)
- **SUBLIME** (from: null)
- **STABLE** (from: null)
- **NodeFormer** (from: Yu et al. 2022)
- **GSR** (from: null)
- **MLP** (from: null)
- **GCN_knn** (from: null)
- **GAT_knn** (from: null)
- **GPRGNN_knn** (from: null)
- **GRCN_knn** (from: null)
- **ProGNN_knn** (from: null)
- **IDGL_knn** (from: null)
- **GEN_knn** (from: null)
- **CoGSL_knn** (from: null)
- **GSR_knn** (from: null)
- **SLAPS** (from: You et al. 2020)
- **LDS_knn** (from: this paper)
- **HES-GSL** (from: this paper)
- **HAN** (from: Yun et al. 2019)
- **GTN**
- **VIB-GSL** (from: RingBDStack)
- **SAGE** (from: Hamilton et al.)
- **GIN** (from: Xu et al.)
- **HGP-SL**

## Extraction Notes

[Cora] Extracted results for Cora from Table 1 (Topology Refinement scenario) and Table 2 (Topology
Inference scenario). All values were percentages in the table, so they were divided by 100 to fit
the [0,1] range. The proposed model HES-GSL only appears in Table 2. Baselines appearing in both
tables are listed separately for each scenario as they represent different experimental settings (TR
vs TI). [Citeseer] Extracted results for Citeseer from Table 1 (Topology Refinement scenario) and
Table 2 (Topology Inference scenario). All values are percentages from the paper, converted to [0,1]
range. Standard deviations are also converted. No proposed model is explicitly named as the primary
contribution in the tables; 'GSLB' is the library name, and 'GSR' and 'HES-GSL' appear to be
specific methods evaluated within the benchmark. Since the paper focuses on the benchmark suite
(GSLB) rather than a single novel architecture, no single model is marked as 'is_proposed': true.
All baselines are treated as such. [PubMed] failed: 7 validation errors for ExtractionOutput
results.3.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.5.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.8.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.10.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.18.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.20.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.23.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[ogbn-arxiv] Extracted results for ogbn-arxiv from Table 1 (TR scenario) and Table 2 (TI scenario).
Note that many baseline models (LDS, GRCN, ProGNN, IDGL, GEN, CoGSL, GSR in TR; LDS, GRCN_knn,
ProGNN_knn, IDGL_knn, GEN_knn, CoGSL_knn, GSR_knn in TI) reported 'OOM' (Out of Memory) and were
excluded as they have no numerical value. The proposed model HES-GSL only appears in Table 2 (TI
scenario). All accuracy values were divided by 100 as they were reported in percentages. [Cornell]
Extracted results for the 'Cornell' dataset from two tables: Table 1 (Topology Refinement scenario)
and Table 2 (Topology Inference scenario). Both tables report Accuracy (%) with standard deviation.
Values were divided by 100 to normalize to [0, 1]. The proposed model HES-GSL appears only in Table
2. Baselines are consistent across both tables, though Table 2 includes knn-based variants for some
models (e.g., GCN_knn) and additional models like MLP and SLAPS. [Texas] Extracted results for the
'Texas' dataset from Table 1 (Topology Refinement scenario) and Table 2 (Topology Inference
scenario). All values were percentages in the table, so they were divided by 100 to fit the [0, 1]
range for Accuracy. The proposed model HES-GSL only appears in Table 2. Baselines appearing in both
tables are listed separately for each scenario as they represent different experimental settings (TR
vs TI). [Wisconsin] Extracted results for the 'Wisconsin' dataset from Table 1 (Topology Refinement
scenario) and Table 2 (Topology Inference scenario). Both tables report Accuracy (%) with standard
deviation. Values were converted from percentages to [0,1] range. The proposed model HES-GSL only
appears in Table 2. Baselines are extracted from both tables as they represent different
experimental settings (TR vs TI) but are all baselines for the proposed method. [Actor] Extracted
results for the 'Actor' dataset from Table 1 (Topology Refinement scenario) and Table 2 (Topology
Inference scenario). All values are percentages from the table, converted to [0,1] range. The
proposed model HES-GSL appears only in Table 2. Baselines are extracted from both tables as they
represent different experimental settings (TR vs TI) for the same dataset. [ACM] Extracted Micro-F1
results for the ACM dataset from Table 1. All values were percentages in the table, so they were
divided by 100 to fit the [0, 1] range. The proposed model is HGSL. Note: GEN appears twice in the
table with identical values; only one entry is included in the output to avoid duplication, though
it represents the same baseline result. [DBLP] Extracted Micro-F1 results for DBLP from Table 1.
Values were percentages in the table (e.g., 90.99) and were divided by 100 to normalize to [0,1].
Standard deviations were extracted from the ± notation. All rows from the DBLP Micro-F1 column were
included. [Yelp] Extracted only Macro-F1 results for the Yelp dataset from Table 1. All values were
percentages in the table (e.g., 92.79) and were divided by 100 to fit the [0, 1] range. Standard
deviations were extracted from the '±' notation. The proposed model is identified as HGSL based on
the context of the paper evaluating GSL algorithms and HGSL being highlighted as a key
contribution/best performer in the text. [IMDB-B] Extracted all rows from Table 1 for the IMDB-B
dataset. The table reports Accuracy (%) with standard deviation. Values were divided by 100 to
normalize to [0,1] range as per instructions. HGP-SL is the proposed model, appearing with three
different encoders (GCN, SAGE, GIN). All other models are baselines. [REDDIT-B] failed: 4 validation
errors for ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.7.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.10.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [COLLAB] Extracted all rows from Table 1 for the
COLLAB dataset. Values were converted from percentages to [0,1] range. Standard deviations were
parsed from the '±' notation. HGP-SL is identified as the proposed model based on the text stating
it 'consistently outperforms' baselines and is highlighted in the table. [IMDB-M] Extracted all rows
from Table 1 corresponding to the IMDB-M dataset. Values were converted from percentages to [0,1]
range as per instructions. Standard deviations were parsed from the '±' notation. HGP-SL is
identified as the proposed model based on the text stating it 'consistently outperforms' baselines
and is highlighted in the table. [MUTAG] Extracted all rows from Table 1 for the MUTAG dataset.
Values were converted from percentages to [0,1] range. Standard deviations were parsed from the '±'
notation. HGP-SL is identified as the proposed model based on the text description 'HGP-SL ...
consistently outperforms'. Baselines include GCN, GAT, SAGE, GIN, and VIB-GSL. [PROTEINS] Extracted
all rows from Table 1 for the PROTEINS dataset. Values were converted from percentages to [0,1]
range. Standard deviations were parsed from the '±' notation. HGP-SL is identified as the proposed
model based on the text description. [Peptides-func] Extracted only Peptides-func AP results as
requested. Values were percentages in the table (e.g., 58.31) and were divided by 100 to fit the
[0,1] range for AP. Standard deviations were also divided by 100. The proposed model is VIB-GSL.
Baselines include standard GNNs and HGP-SL. [Peptides-struct] Extracted all rows from Table 1
corresponding to the 'Peptides-Struct' column. The table caption indicates MAE is the metric for
this dataset and lower is better. Values are extracted directly from the table cells. Standard
deviations are parsed from the '±' notation. No other datasets were included as per instructions.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*