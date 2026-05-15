# Extraction: Classic GNNs are Strong Baselines:\\ Reassessing GNNs for Node Classification
**Model used**: `glm-4.7`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: GCN*
- Type: GCN_variant

## Results

### Amazon-Ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.3647 | 0.0023 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| CPGNN | 0.3979 | 0.0077 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GPRGNN | 0.4488 | 0.0034 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| FSGNN | 0.5274 | 0.0083 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GloGNN | 0.3689 | 0.0014 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS | 0.5310 | 0.0042 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS* | 0.5327 | 0.0066 | Yes | this paper | Table 3 |
| NodeFormer | 0.4386 | 0.0035 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| NodeFormer* | 0.4379 | 0.0057 | Yes | this paper | Table 3 |
| SGFormer | 0.4801 | 0.0049 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| SGFormer* | 0.5414 | 0.0062 | Yes | this paper | Table 3 |
| Polynormer | 0.5481 | 0.0049 | Yes | deng2024polynormer | Table 3 |
| Polynormer* | 0.5496 | 0.0022 | Yes | this paper | Table 3 |
| GCN | 0.4870 | 0.0063 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GCN* | 0.5380 | 0.0060 | No | this paper | Table 3 |
| GraphSAGE | 0.5363 | 0.0039 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphSAGE* | 0.5540 | 0.0021 | Yes | this paper | Table 3 |
| GAT | 0.5270 | 0.0062 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GAT* | 0.5554 | 0.0051 | Yes | this paper | Table 3 |

### CS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.9393 | 0.0012 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphGPS* | 0.9404 | 0.0021 | No | this paper | Table 2 |
| NAGphormer | 0.9575 | 0.0009 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NAGphormer* | 0.9585 | 0.0016 | No | this paper | Table 2 |
| Exphormer | 0.9493 | 0.0001 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Exphormer* | 0.9592 | 0.0025 | No | this paper | Table 2 |
| GOAT | 0.9421 | 0.0038 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GOAT* | 0.9381 | 0.0019 | No | this paper | Table 2 |
| NodeFormer | 0.9564 | 0.0022 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NodeFormer* | 0.9569 | 0.0027 | No | this paper | Table 2 |
| SGFormer | 0.9478 | 0.0020 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| SGFormer* | 0.9571 | 0.0024 | No | this paper | Table 2 |
| Polynormer | 0.9553 | 0.0016 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Polynormer* | 0.9542 | 0.0019 | No | this paper | Table 2 |
| GCN | 0.9292 | 0.0012 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GCN* | 0.9617 | 0.0006 | No | this paper | Table 2 |
| GraphSAGE | 0.9391 | 0.0013 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphSAGE* | 0.9638 | 0.0011 | No | this paper | Table 2 |
| GAT | 0.9361 | 0.0014 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GAT* | 0.9621 | 0.0014 | No | this paper | Table 2 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.2675 | 0.0364 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| CPGNN | 0.3300 | 0.0315 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GPRGNN | 0.3993 | 0.0330 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| FSGNN | 0.4061 | 0.0297 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GloGNN | 0.2590 | 0.0358 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS | 0.4079 | 0.0403 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS* | 0.4155 | 0.0391 | Yes | this paper | Table 3 |
| NodeFormer | 0.3473 | 0.0414 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| NodeFormer* | 0.3638 | 0.0385 | Yes | this paper | Table 3 |
| SGFormer | 0.4493 | 0.0391 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| SGFormer* | 0.4521 | 0.0372 | Yes | this paper | Table 3 |
| Polynormer | 0.4182 | 0.0345 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| Polynormer* | 0.4197 | 0.0318 | Yes | this paper | Table 3 |
| GCN | 0.4131 | 0.0305 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GCN* | 0.4629 | 0.0340 | No | this paper | Table 3 |
| GraphSAGE | 0.3777 | 0.0414 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphSAGE* | 0.4481 | 0.0474 | Yes | this paper | Table 3 |
| GAT | 0.3921 | 0.0308 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GAT* | 0.4413 | 0.0417 | Yes | this paper | Table 3 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.7273 | 0.0123 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphGPS* | 0.7273 | 0.0123 | Yes | this paper | Table 2 |
| NAGphormer | 0.7147 | 0.0130 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NAGphormer* | 0.7059 | 0.0089 | Yes | this paper | Table 2 |
| Exphormer | 0.7163 | 0.0119 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Exphormer* | 0.7185 | 0.0111 | Yes | this paper | Table 2 |
| GOAT | 0.7199 | 0.0126 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GOAT* | 0.7221 | 0.0129 | Yes | this paper | Table 2 |
| NodeFormer | 0.7250 | 0.0110 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NodeFormer* | 0.7237 | 0.0120 | Yes | this paper | Table 2 |
| SGFormer | 0.7260 | 0.0020 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| SGFormer* | 0.7272 | 0.0115 | Yes | this paper | Table 2 |
| Polynormer | 0.7231 | 0.0078 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Polynormer* | 0.7219 | 0.0083 | Yes | this paper | Table 2 |
| GCN | 0.7160 | 0.0040 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GCN* | 0.7314 | 0.0067 | No | this paper | Table 2 |
| GraphSAGE | 0.7193 | 0.0085 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphSAGE* | 0.7226 | 0.0055 | Yes | this paper | Table 2 |
| GAT | 0.7210 | 0.0110 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GAT* | 0.7222 | 0.0084 | Yes | this paper | Table 2 |

### Computer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.9119 | 0.0054 | Yes | deng2024polynormer | Table 2 |
| GraphGPS* | 0.9179 | 0.0063 | No | this paper | Table 2 |
| NAGphormer | 0.9122 | 0.0014 | Yes | deng2024polynormer | Table 2 |
| NAGphormer* | 0.9169 | 0.0030 | No | this paper | Table 2 |
| Exphormer | 0.9147 | 0.0017 | Yes | deng2024polynormer | Table 2 |
| Exphormer* | 0.9180 | 0.0035 | No | this paper | Table 2 |
| GOAT | 0.9096 | 0.0090 | Yes | deng2024polynormer | Table 2 |
| GOAT* | 0.9229 | 0.0037 | No | this paper | Table 2 |
| NodeFormer | 0.8698 | 0.0062 | Yes | deng2024polynormer | Table 2 |
| NodeFormer* | 0.8729 | 0.0058 | No | this paper | Table 2 |
| SGFormer | 0.9199 | 0.0076 | Yes | deng2024polynormer | Table 2 |
| SGFormer* | 0.9242 | 0.0066 | No | this paper | Table 2 |
| Polynormer | 0.9368 | 0.0021 | Yes | deng2024polynormer | Table 2 |
| Polynormer* | 0.9378 | 0.0010 | No | this paper | Table 2 |
| GCN | 0.8965 | 0.0052 | Yes | deng2024polynormer | Table 2 |
| GCN* | 0.9399 | 0.0012 | No | this paper | Table 2 |
| GraphSAGE | 0.9120 | 0.0029 | Yes | deng2024polynormer | Table 2 |
| GraphSAGE* | 0.9325 | 0.0014 | No | this paper | Table 2 |
| GAT | 0.9078 | 0.0013 | Yes | deng2024polynormer | Table 2 |
| GAT* | 0.9409 | 0.0037 | No | this paper | Table 2 |
| GCN* (-) Normalization | 0.9260 | 0.0014 | No | this paper | Table 3 |
| GCN* (-) Dropout | 0.9378 | 0.0026 | No | this paper | Table 3 |
| GraphSAGE* (-) Normalization | 0.9277 | 0.0063 | No | this paper | Table 3 |
| GraphSAGE* (-) Dropout | 0.9202 | 0.0035 | No | this paper | Table 3 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.8284 | 0.0103 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphGPS* | 0.8387 | 0.0096 | Yes | this paper | Table 2 |
| NAGphormer | 0.8212 | 0.0118 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NAGphormer* | 0.8092 | 0.0117 | Yes | this paper | Table 2 |
| Exphormer | 0.8277 | 0.0138 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Exphormer* | 0.8329 | 0.0136 | Yes | this paper | Table 2 |
| GOAT | 0.8318 | 0.0127 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GOAT* | 0.8326 | 0.0124 | Yes | this paper | Table 2 |
| NodeFormer | 0.8220 | 0.0090 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NodeFormer* | 0.8273 | 0.0075 | Yes | this paper | Table 2 |
| SGFormer | 0.8450 | 0.0080 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| SGFormer* | 0.8482 | 0.0085 | Yes | this paper | Table 2 |
| Polynormer | 0.8325 | 0.0093 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Polynormer* | 0.8343 | 0.0089 | Yes | this paper | Table 2 |
| GCN | 0.8160 | 0.0040 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GCN* | 0.8510 | 0.0067 | No | this paper | Table 2 |
| GraphSAGE | 0.8268 | 0.0047 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphSAGE* | 0.8388 | 0.0065 | Yes | this paper | Table 2 |
| GAT | 0.8300 | 0.0070 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GAT* | 0.8446 | 0.0055 | Yes | this paper | Table 2 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.8971 | 0.0031 | Yes | Deng et al. 2024 | Table 3 |
| CPGNN | 0.5203 | 0.0546 | Yes | Deng et al. 2024 | Table 3 |
| GPRGNN | 0.8624 | 0.0061 | Yes | Deng et al. 2024 | Table 3 |
| FSGNN | 0.9008 | 0.0070 | Yes | Deng et al. 2024 | Table 3 |
| GloGNN | 0.5108 | 0.0123 | Yes | Deng et al. 2024 | Table 3 |
| GraphGPS | 0.9063 | 0.0067 | Yes | Deng et al. 2024 | Table 3 |
| GraphGPS* | 0.9075 | 0.0089 | Yes | this paper | Table 3 |
| NodeFormer | 0.8671 | 0.0088 | Yes | Deng et al. 2024 | Table 3 |
| NodeFormer* | 0.8771 | 0.0069 | Yes | this paper | Table 3 |
| SGFormer | 0.9089 | 0.0058 | Yes | Deng et al. 2024 | Table 3 |
| SGFormer* | 0.9142 | 0.0041 | Yes | this paper | Table 3 |
| Polynormer | 0.9746 | 0.0036 | Yes | Deng et al. 2024 | Table 3 |
| Polynormer* | 0.9749 | 0.0048 | Yes | this paper | Table 3 |
| GCN | 0.8975 | 0.0052 | Yes | Deng et al. 2024 | Table 3 |
| GCN* | 0.9786 | 0.0024 | No | this paper | Table 3 |
| GraphSAGE | 0.9351 | 0.0057 | Yes | Deng et al. 2024 | Table 3 |
| GraphSAGE* | 0.9777 | 0.0062 | Yes | this paper | Table 3 |
| GAT | 0.9391 | 0.0035 | Yes | Deng et al. 2024 | Table 3 |
| GAT* | 0.9773 | 0.0073 | Yes | this paper | Table 3 |

### Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.9506 | 0.0013 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphGPS* | 0.9489 | 0.0014 | No | this paper | Table 2 |
| NAGphormer | 0.9549 | 0.0011 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NAGphormer* | 0.9614 | 0.0016 | No | this paper | Table 2 |
| Exphormer | 0.9535 | 0.0022 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Exphormer* | 0.9569 | 0.0039 | No | this paper | Table 2 |
| GOAT | 0.9296 | 0.0148 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GOAT* | 0.9433 | 0.0021 | No | this paper | Table 2 |
| NodeFormer | 0.9346 | 0.0035 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NodeFormer* | 0.9343 | 0.0056 | No | this paper | Table 2 |
| SGFormer | 0.9510 | 0.0047 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| SGFormer* | 0.9558 | 0.0036 | No | this paper | Table 2 |
| Polynormer | 0.9646 | 0.0026 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Polynormer* | 0.9657 | 0.0023 | No | this paper | Table 2 |
| GCN | 0.9270 | 0.0020 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GCN* | 0.9610 | 0.0046 | No | this paper | Table 2 |
| GraphSAGE | 0.9459 | 0.0014 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphSAGE* | 0.9678 | 0.0023 | No | this paper | Table 2 |
| GAT | 0.9387 | 0.0011 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GAT* | 0.9660 | 0.0033 | No | this paper | Table 2 |

### Physics — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.9712 | 0.0019 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphGPS* | 0.9671 | 0.0015 | Yes | this paper | Table 2 |
| NAGphormer | 0.9734 | 0.0003 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NAGphormer* | 0.9735 | 0.0012 | Yes | this paper | Table 2 |
| Exphormer | 0.9689 | 0.0009 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Exphormer* | 0.9706 | 0.0013 | Yes | this paper | Table 2 |
| GOAT | 0.9624 | 0.0024 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GOAT* | 0.9647 | 0.0016 | Yes | this paper | Table 2 |
| NodeFormer | 0.9645 | 0.0028 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NodeFormer* | 0.9648 | 0.0034 | Yes | this paper | Table 2 |
| SGFormer | 0.9660 | 0.0018 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| SGFormer* | 0.9675 | 0.0026 | Yes | this paper | Table 2 |
| Polynormer | 0.9727 | 0.0008 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Polynormer* | 0.9718 | 0.0011 | Yes | this paper | Table 2 |
| GCN | 0.9618 | 0.0007 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GCN* | 0.9746 | 0.0010 | No | this paper | Table 2 |
| GraphSAGE | 0.9649 | 0.0006 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphSAGE* | 0.9719 | 0.0005 | Yes | this paper | Table 2 |
| GAT | 0.9617 | 0.0008 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GAT* | 0.9725 | 0.0006 | Yes | this paper | Table 2 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.7994 | 0.0026 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphGPS* | 0.7994 | 0.0026 | Yes | this paper | Table 2 |
| NAGphormer | 0.7973 | 0.0028 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NAGphormer* | 0.8014 | 0.0106 | Yes | this paper | Table 2 |
| Exphormer | 0.7946 | 0.0035 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Exphormer* | 0.7967 | 0.0073 | Yes | this paper | Table 2 |
| GOAT | 0.7913 | 0.0038 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GOAT* | 0.8006 | 0.0067 | Yes | this paper | Table 2 |
| NodeFormer | 0.7990 | 0.0100 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| NodeFormer* | 0.7959 | 0.0092 | Yes | this paper | Table 2 |
| SGFormer | 0.8030 | 0.0060 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| SGFormer* | 0.8060 | 0.0049 | Yes | this paper | Table 2 |
| Polynormer | 0.7924 | 0.0043 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| Polynormer* | 0.7935 | 0.0073 | Yes | this paper | Table 2 |
| GCN | 0.7880 | 0.0060 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GCN* | 0.8112 | 0.0052 | No | this paper | Table 2 |
| GraphSAGE | 0.7941 | 0.0053 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GraphSAGE* | 0.7972 | 0.0050 | Yes | this paper | Table 2 |
| GAT | 0.7900 | 0.0040 | Yes | deng2024polynormer,wu2023simplifying | Table 2 |
| GAT* | 0.8028 | 0.0064 | Yes | this paper | Table 2 |

### Questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.6359 | 0.0146 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| CPGNN | 0.6596 | 0.0195 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GPRGNN | 0.5548 | 0.0091 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| FSGNN | 0.7886 | 0.0092 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GloGNN | 0.6574 | 0.0119 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS | 0.7173 | 0.0147 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS* | 0.7256 | 0.0133 | Yes | this paper | Table 3 |
| NodeFormer | 0.7427 | 0.0146 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| NodeFormer* | 0.7502 | 0.0161 | Yes | this paper | Table 3 |
| SGFormer | 0.7215 | 0.0131 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| SGFormer* | 0.7381 | 0.0059 | Yes | this paper | Table 3 |
| Polynormer | 0.7892 | 0.0089 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| Polynormer* | 0.7894 | 0.0078 | Yes | this paper | Table 3 |
| GCN | 0.7609 | 0.0127 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GCN* | 0.7902 | 0.0060 | No | this paper | Table 3 |
| GraphSAGE | 0.7644 | 0.0062 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphSAGE* | 0.7721 | 0.0128 | Yes | this paper | Table 3 |
| GAT | 0.7679 | 0.0071 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GAT* | 0.7795 | 0.0051 | Yes | this paper | Table 3 |

### Roman-Empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.6011 | 0.0052 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| CPGNN | 0.6396 | 0.0062 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GPRGNN | 0.6485 | 0.0027 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| FSGNN | 0.7992 | 0.0056 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GloGNN | 0.5963 | 0.0069 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS | 0.8200 | 0.0061 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphGPS* | 0.8272 | 0.0068 | Yes | this paper | Table 3 |
| NodeFormer | 0.6449 | 0.0073 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| NodeFormer* | 0.7483 | 0.0081 | Yes | this paper | Table 3 |
| SGFormer | 0.7910 | 0.0032 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| SGFormer* | 0.8001 | 0.0044 | Yes | this paper | Table 3 |
| Polynormer | 0.9255 | 0.0037 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| Polynormer* | 0.9266 | 0.0060 | Yes | this paper | Table 3 |
| GCN | 0.7369 | 0.0074 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GCN* | 0.9127 | 0.0020 | No | this paper | Table 3 |
| GraphSAGE | 0.8574 | 0.0067 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GraphSAGE* | 0.9106 | 0.0027 | Yes | this paper | Table 3 |
| GAT | 0.8875 | 0.0041 | Yes | deng2024polynormer,wu2023simplifying,platonov2023critical | Table 3 |
| GAT* | 0.9063 | 0.0014 | Yes | this paper | Table 3 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN | 0.3510 | 0.0115 | Yes | this paper | Table 3 |
| CPGNN | 0.3004 | 0.0203 | Yes | this paper | Table 3 |
| GPRGNN | 0.3895 | 0.0199 | Yes | this paper | Table 3 |
| FSGNN | 0.3592 | 0.0132 | Yes | this paper | Table 3 |
| GloGNN | 0.3511 | 0.0124 | Yes | this paper | Table 3 |
| GraphGPS | 0.3967 | 0.0284 | Yes | this paper | Table 3 |
| GraphGPS* | 0.3981 | 0.0228 | No | this paper | Table 3 |
| NodeFormer | 0.3852 | 0.0157 | Yes | this paper | Table 3 |
| NodeFormer* | 0.3889 | 0.0267 | No | this paper | Table 3 |
| SGFormer | 0.4180 | 0.0227 | Yes | this paper | Table 3 |
| SGFormer* | 0.4265 | 0.0241 | No | this paper | Table 3 |
| Polynormer | 0.4087 | 0.0196 | Yes | deng2024polynormer | Table 3 |
| Polynormer* | 0.4197 | 0.0214 | No | this paper | Table 3 |
| GCN | 0.3867 | 0.0184 | Yes | this paper | Table 3 |
| GCN* | 0.4501 | 0.0163 | No | this paper | Table 3 |
| GraphSAGE | 0.3609 | 0.0199 | Yes | this paper | Table 3 |
| GraphSAGE* | 0.4078 | 0.0147 | No | this paper | Table 3 |
| GAT | 0.3562 | 0.0206 | Yes | this paper | Table 3 |
| GAT* | 0.4173 | 0.0207 | No | this paper | Table 3 |

### WikiCS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.7866 | 0.0049 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphGPS* | 0.7866 | 0.0049 | No | this paper | Table 2 |
| NAGphormer | 0.7716 | 0.0072 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NAGphormer* | 0.7792 | 0.0093 | No | this paper | Table 2 |
| Exphormer | 0.7854 | 0.0049 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Exphormer* | 0.7938 | 0.0062 | No | this paper | Table 2 |
| GOAT | 0.7700 | 0.0077 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GOAT* | 0.7796 | 0.0063 | No | this paper | Table 2 |
| NodeFormer | 0.7473 | 0.0094 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| NodeFormer* | 0.7513 | 0.0093 | No | this paper | Table 2 |
| SGFormer | 0.7346 | 0.0056 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| SGFormer* | 0.8005 | 0.0046 | No | this paper | Table 2 |
| Polynormer | 0.8010 | 0.0067 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| Polynormer* | 0.8026 | 0.0092 | No | this paper | Table 2 |
| GCN | 0.7747 | 0.0085 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GCN* | 0.8030 | 0.0062 | No | this paper | Table 2 |
| GraphSAGE | 0.7477 | 0.0095 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GraphSAGE* | 0.8069 | 0.0031 | No | this paper | Table 2 |
| GAT | 0.7691 | 0.0082 | Yes | Deng et al. 2024; Wu et al. 2023 | Table 2 |
| GAT* | 0.8107 | 0.0054 | No | this paper | Table 2 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.7097 | 0.0041 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GraphGPS* | 0.7123 | 0.0059 | No | this paper | Table 4 |
| NAGphormer | 0.7013 | 0.0055 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| NAGphormer* | 0.7088 | 0.0024 | No | this paper | Table 4 |
| Exphormer | 0.7244 | 0.0028 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| Exphormer* | 0.7232 | 0.0036 | No | this paper | Table 4 |
| GOAT | 0.7241 | 0.0040 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GOAT* | 0.7276 | 0.0029 | No | this paper | Table 4 |
| NodeFormer | 0.5990 | 0.0042 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| NodeFormer* | 0.6778 | 0.0028 | No | this paper | Table 4 |
| SGFormer | 0.7263 | 0.0013 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| SGFormer* | 0.7276 | 0.0033 | No | this paper | Table 4 |
| Polynormer | 0.7346 | 0.0016 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| Polynormer* | 0.7340 | 0.0022 | No | this paper | Table 4 |
| GCN | 0.7174 | 0.0029 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GCN* | 0.7353 | 0.0012 | No | this paper | Table 4 |
| GraphSAGE | 0.7149 | 0.0027 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GraphSAGE* | 0.7300 | 0.0028 | No | this paper | Table 4 |
| GAT | 0.7195 | 0.0036 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GAT* | 0.7330 | 0.0018 | No | this paper | Table 4 |
| GCN* (-) Normalization | 0.7153 | 0.0014 | No | this paper | Table 5 |
| GCN* (-) Dropout | 0.7206 | 0.0013 | No | this paper | Table 5 |
| GCN* (-) Residual Connections | 0.7291 | 0.0017 | No | this paper | Table 5 |
| GraphSAGE* (-) Normalization | 0.7113 | 0.0027 | No | this paper | Table 5 |
| GraphSAGE* (-) Dropout | 0.7130 | 0.0021 | No | this paper | Table 5 |
| GraphSAGE* (-) Residual Connections | 0.7222 | 0.0049 | No | this paper | Table 5 |
| GAT* (-) Normalization | 0.7133 | 0.0029 | No | this paper | Table 5 |
| GAT* (-) Dropout | 0.7168 | 0.0032 | No | this paper | Table 5 |
| GAT* (-) Residual Connections | 0.7247 | 0.0034 | No | this paper | Table 5 |

### ogbn-proteins — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.7683 | 0.0026 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GraphGPS* | 0.7715 | 0.0064 | No | this paper | Table 4 |
| NAGphormer | 0.7361 | 0.0033 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| NAGphormer* | 0.7217 | 0.0045 | No | this paper | Table 4 |
| Exphormer | 0.7458 | 0.0026 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| Exphormer* | 0.7762 | 0.0033 | No | this paper | Table 4 |
| GOAT | 0.7418 | 0.0037 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GOAT* | 0.7931 | 0.0042 | No | this paper | Table 4 |
| NodeFormer | 0.7745 | 0.0115 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| NodeFormer* | 0.7786 | 0.0084 | No | this paper | Table 4 |
| SGFormer | 0.7953 | 0.0038 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| SGFormer* | 0.7992 | 0.0048 | No | this paper | Table 4 |
| Polynormer | 0.7897 | 0.0047 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| Polynormer* | 0.7953 | 0.0067 | No | this paper | Table 4 |
| GCN | 0.7251 | 0.0035 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GCN* | 0.7729 | 0.0046 | No | this paper | Table 4 |
| GraphSAGE | 0.7768 | 0.0020 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GraphSAGE* | 0.8221 | 0.0032 | No | this paper | Table 4 |
| GAT | 0.7202 | 0.0044 | Yes | deng2024polynormer,wu2023simplifying | Table 4 |
| GAT* | 0.8501 | 0.0046 | No | this paper | Table 4 |

## Baseline Models Identified

- **GraphGPS** (from: Rampasek et al. 2022)
- **NAGphormer** (from: Chen et al. 2022)
- **Exphormer** (from: Shirzad et al. 2023)
- **GOAT** (from: Hussain et al. 2022)
- **NodeFormer** (from: Wu et al. 2023)
- **SGFormer** (from: Wu et al. 2023)
- **Polynormer** (from: Deng et al. 2024)
- **GCN** (from: Kipf & Welling 2017)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **GAT** (from: Velickovic et al. 2018)
- **H2GCN**
- **CPGNN**
- **GPRGNN**
- **FSGNN**
- **GloGNN**
- **GraphGPS*** (from: this paper)
- **NodeFormer*** (from: this paper)
- **SGFormer*** (from: this paper)
- **Polynormer*** (from: this paper)
- **GraphSAGE*** (from: this paper)
- **GAT*** (from: this paper)

## Extraction Notes

[Cora] The paper presents results for Cora in Table 2. The table includes both baseline results
(cited from Deng et al. 2024 and Wu et al. 2023) and the authors' own implementations (marked with
*). The primary metric is Accuracy. The proposed model is identified as GCN* based on the text
highlighting its performance improvements. All values are percentages and have been normalized to
the range [0, 1]. [CiteSeer] The paper presents results for CiteSeer in Table 2. The table includes
both baseline results (cited from Deng et al. 2024 and Wu et al. 2023) and the authors' own
implementations (marked with *). The primary metric is Accuracy, reported as percentages which have
been normalized to the range [0, 1]. The proposed model is identified as GCN* based on the text
highlighting its performance improvements. The ablation study table (Table 3) was skipped as it
contains variants of the proposed model rather than standard baselines or the primary proposed
configuration. [PubMed] Extracted results for PubMed dataset from Table 2. Values were reported as
percentages and converted to the range [0, 1]. Standard deviations were extracted from the text. The
proposed model is identified as GCN* based on the text highlighting its performance improvements.
[Computer] The paper presents results for the 'Computer' dataset in Table 2 (main results) and Table
3 (ablation study). The metric is Accuracy, reported as percentages in the tables (e.g., 91.19),
which have been normalized to the range [0, 1] (e.g., 0.9119). Standard deviations were extracted
from the small font text next to the values. Models marked with * are the proposed implementations
(GNN* variants). Baseline results without * are cited from Deng et al. 2024 and Wu et al. 2023. The
ablation table (Table 3) includes variants like '(-) Normalization' and '(-) Dropout', which were
extracted as separate model entries. [Photo] Extracted results for the 'Photo' dataset from Table 2.
The table reports Accuracy in percentages, which were normalized to the range [0, 1]. Standard
deviations were extracted from the small font text next to the values. Models marked with '*' are
treated as the proposed models (re-implemented baselines with tuned hyperparameters). [CS] The paper
presents results for the CS dataset in Table 2. The table includes both baseline results (from other
papers) and the authors' re-implemented versions (marked with *). The metric is Accuracy, reported
as percentages in the table, which have been normalized to the range [0, 1]. The standard deviations
are provided in the table. The 'proposed_model' field lists the re-implemented models (GCN*,
GraphSAGE*, GAT*) as the focus of the paper's contribution regarding tuning classic GNNs. [Physics]
The paper presents results for multiple datasets. Only the 'Physics' dataset column was extracted as
requested. The table reports Accuracy in percentages (e.g., 97.12), which were normalized to the
range [0, 1] (e.g., 0.9712). Standard deviations were extracted from the tiny font text next to the
values. The '*' suffix indicates the authors' re-implementation or tuned version of the baseline
models. The proposed model is identified as GCN* based on the text highlighting its performance and
the context of the paper focusing on tuning classic GNNs. [WikiCS] Values were reported as
percentages in the table (e.g., 81.07) and have been normalized to the range [0, 1] (0.8107) as per
the schema rules. Standard deviations were extracted from the tiny font text next to the values. The
'proposed' models are those marked with an asterisk (*) in the table, indicating the authors'
implementation/tuning. The source references for non-asterisked models are inferred from the table
caption citing Deng et al. 2024 and Wu et al. 2023. [Squirrel] Extracted results for Squirrel
dataset from Table 3. Values were reported as percentages and converted to the range [0, 1] by
dividing by 100. The 'proposed_model' is identified as GCN* based on the text highlighting GCN*
improvements, though the paper also reports re-implementations (marked with *) of other baselines.
All rows from the Squirrel column were extracted. [Chameleon] The paper presents results for the
Chameleon dataset using the standard split (Accuracy metric). The table includes both baseline
results from other papers and re-implemented versions (marked with *). The proposed model is
identified as GCN* based on the text highlighting its performance. All values were normalized from
percentages to the [0, 1] range. [Amazon-Ratings] The paper presents results for Amazon-Ratings in
Table 3. The primary metric is Accuracy. Values were reported as percentages (e.g., 36.47) and have
been normalized to the range [0, 1] (e.g., 0.3647). The table includes both baseline results (from
other papers) and results marked with '*' indicating the authors' implementation. The proposed model
appears to be GCN* based on the ablation study table (Table ab2) which highlights GCN* as the base
model for modifications, though the main results table (Table 3) compares it against many baselines.
All rows for Amazon-Ratings were extracted. [Roman-Empire] Values were reported as percentages in
the table (e.g., 60.11) and have been normalized to the range [0, 1] (e.g., 0.6011). The
'proposed_model' is identified as GCN* based on the paper's emphasis on its implementation and
performance improvements. Baseline models include both literature values and the paper's re-
implementations (marked with *). [Minesweeper] Values were reported as percentages (e.g., 97.86) and
normalized to the range [0, 1] (0.9786) for ROC-AUC. Standard deviations were extracted from the ±
values. The 'proposed_model' is identified as GCN* based on the text highlighting its performance
and the ablation study structure. [Questions] Values were reported as percentages (e.g., 79.02) and
normalized to the range [0, 1] (0.7902) as per the ROC-AUC metric. The table caption indicates that
results with '*' are the authors' implementation, while others are from cited papers. The
'Questions' dataset uses ROC-AUC as the primary metric. [ogbn-proteins] Values were reported as
percentages (e.g., 76.83) and have been normalized to the range [0, 1] (e.g., 0.7683) as per the
schema rules. The table caption indicates that results without * are taken from Deng et al. 2024 and
Wu et al. 2023, while results with * are the authors' implementation. The ablation study table
(Table ab3) was skipped as it contains variants of the proposed models rather than distinct
baselines or standard configurations. [ogbn-arxiv] Values were reported as percentages (e.g., 73.53)
and have been normalized to the range [0, 1] (e.g., 0.7353). The paper compares standard baselines
against the authors' implementations (marked with *). Table 4 contains the main comparison, while
Table 5 contains ablation studies on the proposed implementations. All extracted values correspond
to the 'ogbn-arxiv' dataset and the 'Accuracy' metric. [ogbn-products] failed: 4 validation errors
for ExtractionOutput results.0.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [pokec] failed: 4 validation errors for
ExtractionOutput results.0.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.1.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.5.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*