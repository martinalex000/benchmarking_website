# Extraction: arXiv:2502.09263
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: GNN+ (0.5M params)
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.5975 | 0.0029 | Yes | dwivedi2020generalization | Table 2 |
| EGT | 0.6870 | 0.0041 | Yes | hussain2022global | Table 2 |
| GraphGPS | 0.7230 | 0.0036 | Yes | rampavsek2022recipe | Table 2 |
| Graph ViT/MLP-Mixer | 0.7396 | 0.0033 | Yes | he2023generalization | Table 2 |
| Exphormer | 0.7475 | 0.0019 | Yes | shirzad2023exphormer | Table 2 |
| GRIT | 0.7647 | 0.0088 | Yes | ma2023graph | Table 2 |
| GRED | 0.7685 | 0.0019 | Yes | ding2024recurrent | Table 2 |
| GEAET | 0.7663 | 0.0043 | Yes | liang2024graph | Table 2 |
| TIGT | 0.7396 | 0.0036 | Yes | choi2024topology | Table 2 |
| GMN | 0.7456 | 0.0038 | Yes | behrouz2024graph | Table 2 |
| Graph-Mamba | 0.7370 | 0.0034 | Yes | wang2024graph | Table 2 |
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 2 |
| GCN+ | 0.6982 | 0.0041 | No | this paper | Table 2 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 2 |
| GIN+ | 0.6959 | 0.0029 | No | this paper | Table 2 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 2 |
| GatedGCN+ | 0.7722 | 0.0038 | No | this paper | Table 2 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.7317 | 0.0062 | Yes | dwivedi2020generalization | Table 2 |
| SAN | 0.7669 | 0.0065 | Yes | kreuzer2021rethinking | Table 2 |
| SAT | 0.7786 | 0.0010 | Yes | chen2022structure | Table 2 |
| EGT | 0.7923 | 0.0035 | Yes | hussain2022global | Table 2 |
| GraphGPS | 0.7802 | 0.0018 | Yes | rampavsek2022recipe | Table 2 |
| GRIT | 0.8003 | 0.0028 | Yes | ma2023graph | Table 2 |
| GRED | 0.7850 | 0.0010 | Yes | ding2024recurrent | Table 2 |
| TIGT | 0.7802 | 0.0022 | Yes | choi2024topology | Table 2 |
| Graph-Mamba | 0.7680 | 0.0036 | Yes | wang2024graph | Table 2 |
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 2 |
| GCN+ | 0.7711 | 0.0087 | No | this paper | Table 2 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 2 |
| GIN+ | 0.7479 | 0.0021 | No | this paper | Table 2 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 2 |
| GatedGCN+ | 0.7913 | 0.0024 | No | this paper | Table 2 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2618 | 0.0031 | Yes | dwivedi2020generalization | Table 3 |
| SAN | 0.2592 | 0.0158 | Yes | kreuzer2021rethinking | Table 3 |
| GraphGPS | 0.3412 | 0.0044 | Yes | rampavsek2022recipe | Table 3 |
| NAGphormer | 0.3458 | 0.0070 | Yes | chen2023nagphormer | Table 3 |
| DIFFormer | 0.3620 | 0.0012 | Yes | wu2023difformer | Table 3 |
| Exphormer | 0.3430 | 0.0108 | Yes | shirzad2023exphormer | Table 3 |
| GEAET | 0.3219 | 0.0052 | Yes | liang2024graph | Table 3 |
| GECO | 0.3320 | 0.0032 | Yes | sancak2024scalable | Table 3 |
| Graph-Mamba | 0.3960 | 0.0175 | Yes | wang2024graph | Table 3 |
| GCN | 0.1338 | 0.0007 | Yes | this paper | Table 3 |
| GCN+ | 0.2733 | 0.0041 | No | this paper | Table 3 |
| GIN | 0.2125 | 0.0009 | Yes | this paper | Table 3 |
| GIN+ | 0.2483 | 0.0046 | No | this paper | Table 3 |
| GatedGCN | 0.2922 | 0.0018 | Yes | this paper | Table 3 |
| GatedGCN+ | 0.3802 | 0.0015 | No | this paper | Table 3 |

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LDP | 0.7810 | — | Yes | cai2018simple | Table 1 |
| HRN | 0.8180 | — | Yes | wu2022simple | Table 1 |
| GCN+ | 0.8090 | — | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LDP | 0.7540 | — | Yes | cai2018simple | Table 1 |
| HRN | 0.7750 | — | Yes | wu2022simple | Table 1 |
| GCN+ | 0.7690 | — | No | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LDP | 0.5000 | — | Yes | cai2018simple | Table 1 |
| HRN | 0.5280 | — | Yes | wu2022simple | Table 1 |
| GCN+ | 0.5230 | — | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.9083 | 0.0016 | Yes | dwivedi2020generalization | Table 2 |
| EGT | 0.9817 | 0.0009 | Yes | hussain2022global | Table 2 |
| GraphGPS | 0.9805 | 0.0013 | Yes | rampavsek2022recipe | Table 2 |
| Graph ViT/MLP-Mixer | 0.9846 | 0.0009 | Yes | he2023generalization | Table 2 |
| Exphormer | 0.9841 | 0.0004 | Yes | shirzad2023exphormer | Table 2 |
| GRIT | 0.9811 | 0.0011 | Yes | ma2023graph | Table 2 |
| GRED | 0.9838 | 0.0001 | Yes | ding2024recurrent | Table 2 |
| GEAET | 0.9851 | 0.0009 | Yes | liang2024graph | Table 2 |
| TIGT | 0.9823 | 0.0013 | Yes | choi2024topology | Table 2 |
| GMN | 0.9839 | 0.0018 | Yes | behrouz2024graph | Table 2 |
| Graph-Mamba | 0.9842 | 0.0008 | Yes | wang2024graph | Table 2 |
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 2 |
| GCN+ | 0.9838 | 0.0009 | No | this paper | Table 2 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 2 |
| GIN+ | 0.9829 | 0.0010 | No | this paper | Table 2 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 2 |
| GatedGCN+ | 0.9871 | 0.0014 | No | this paper | Table 2 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LDP | 0.9030 | — | Yes | cai2018simple | Table 1 |
| HRN | 0.9040 | — | Yes | wu2022simple | Table 1 |
| GCN+ | 0.9010 | — | No | this paper | Table 1 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS | 0.9350 | 0.0041 | Yes | rampavsek2022recipe | Table 3 |
| Exphormer | 0.9402 | 0.0021 | Yes | shirzad2023exphormer | Table 3 |
| Graph-Mamba | 0.9340 | 0.0027 | Yes | wang2024graph | Table 3 |
| GSSC | 0.9406 | 0.0064 | Yes | huang2024can | Table 3 |
| GCN | 0.8100 | 0.0081 | Yes | this paper | Table 3 |
| GCN+ | 0.9354 | 0.0045 | No | this paper | Table 3 |
| GIN | 0.8898 | 0.0055 | Yes | this paper | Table 3 |
| GIN+ | 0.9325 | 0.0040 | No | this paper | Table 3 |
| GatedGCN | 0.9223 | 0.0065 | Yes | this paper | Table 3 |
| GatedGCN+ | 0.9460 | 0.0057 | No | this paper | Table 3 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.8481 | 0.0007 | Yes | dwivedi2020generalization | Table 2 |
| SAN | 0.8658 | 0.0004 | Yes | kreuzer2021rethinking | Table 2 |
| SAT | 0.8685 | 0.0004 | Yes | chen2022structure | Table 2 |
| EGT | 0.8682 | 0.0002 | Yes | hussain2022global | Table 2 |
| GraphGPS | 0.8669 | 0.0006 | Yes | rampavsek2022recipe | Table 2 |
| GRPE | 0.8702 | 0.0004 | Yes | park2022grpe | Table 2 |
| LGI-GT | 0.8693 | 0.0004 | Yes | yinlgi | Table 2 |
| GPTrans-Nano | 0.8673 | 0.0008 | Yes | chen2023graph | Table 2 |
| Exphormer | 0.8673 | 0.0001 | Yes | shirzad2023exphormer | Table 2 |
| GRIT | 0.8720 | 0.0008 | Yes | ma2023graph | Table 2 |
| GRED | 0.8676 | 0.0002 | Yes | ding2024recurrent | Table 2 |
| GEAET | 0.8699 | 0.0003 | Yes | liang2024graph | Table 2 |
| TIGT | 0.8668 | 0.0006 | Yes | choi2024topology | Table 2 |
| GMN | 0.8709 | 0.0126 | Yes | behrouz2024graph | Table 2 |
| Graph-Mamba | 0.8671 | 0.0005 | Yes | wang2024graph | Table 2 |
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 2 |
| GCN+ | 0.8702 | 0.0009 | No | this paper | Table 2 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 2 |
| GIN+ | 0.8684 | 0.0005 | No | this paper | Table 2 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 2 |
| GatedGCN+ | 0.8703 | 0.0004 | No | this paper | Table 2 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2694 | 0.0098 | Yes | dwivedi2020generalization | Table 3 |
| SAN | 0.3230 | 0.0039 | Yes | kreuzer2021rethinking | Table 3 |
| GraphGPS | 0.3748 | 0.0109 | Yes | rampavsek2022recipe | Table 3 |
| NAGphormer | 0.4006 | 0.0061 | Yes | chen2023nagphormer | Table 3 |
| DIFFormer | 0.3988 | 0.0045 | Yes | wu2023difformer | Table 3 |
| DRew | 0.3314 | 0.0024 | Yes | gutteridge2023drew | Table 3 |
| Exphormer | 0.3446 | 0.0064 | Yes | shirzad2023exphormer | Table 3 |
| GEAET | 0.3933 | 0.0027 | Yes | liang2024graph | Table 3 |
| GECO | 0.4210 | 0.0080 | Yes | sancak2024scalable | Table 3 |
| Graph-Mamba | 0.4191 | 0.0126 | Yes | wang2024graph | Table 3 |
| GSSC | 0.4561 | 0.0039 | Yes | huang2024can | Table 3 |
| GCN | 0.2078 | 0.0031 | Yes | this paper | Table 3 |
| GCN+ | 0.3357 | 0.0087 | No | this paper | Table 3 |
| GIN | 0.2718 | 0.0054 | Yes | this paper | Table 3 |
| GIN+ | 0.3189 | 0.0105 | No | this paper | Table 3 |
| GatedGCN | 0.3880 | 0.0040 | Yes | this paper | Table 3 |
| GatedGCN+ | 0.4263 | 0.0057 | No | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.6326 | 0.0126 | Yes | dwivedi2020generalization | Table 3 |
| SAN | 0.6439 | 0.0075 | Yes | kreuzer2021rethinking | Table 3 |
| GraphGPS | 0.6535 | 0.0041 | Yes | rampavsek2022recipe | Table 3 |
| MGT | 0.6817 | 0.0064 | Yes | ngo2023multiresolution | Table 3 |
| DRew | 0.7150 | 0.0044 | Yes | gutteridge2023drew | Table 3 |
| Graph ViT/MLP-Mixer | 0.6970 | 0.0080 | Yes | he2023generalization | Table 3 |
| Exphormer | 0.6258 | 0.0092 | Yes | shirzad2023exphormer | Table 3 |
| GRIT | 0.6988 | 0.0082 | Yes | ma2023graph | Table 3 |
| Subgraphormer | 0.6415 | 0.0052 | Yes | bar2024subgraphormer | Table 3 |
| GRED | 0.7133 | 0.0011 | Yes | ding2024recurrent | Table 3 |
| GEAET | 0.6485 | 0.0035 | Yes | liang2024graph | Table 3 |
| TIGT | 0.6679 | 0.0074 | Yes | choi2024topology | Table 3 |
| GECO | 0.6975 | 0.0025 | Yes | sancak2024scalable | Table 3 |
| GPNN | 0.6955 | 0.0057 | Yes | lin2024understanding | Table 3 |
| Graph-Mamba | 0.6739 | 0.0087 | Yes | wang2024graph | Table 3 |
| GSSC | 0.7081 | 0.0062 | Yes | huang2024can | Table 3 |
| GCN | 0.6860 | 0.0050 | Yes | this paper | Table 3 |
| GCN+ | 0.7261 | 0.0067 | No | this paper | Table 3 |
| GIN | 0.6621 | 0.0067 | Yes | this paper | Table 3 |
| GIN+ | 0.7059 | 0.0089 | No | this paper | Table 3 |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 3 |
| GatedGCN+ | 0.7006 | 0.0033 | No | this paper | Table 3 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2529 | 0.0016 | Yes | dwivedi2020generalization | Table 3 |
| SAN | 0.2545 | 0.0012 | Yes | kreuzer2021rethinking | Table 3 |
| GraphGPS | 0.2500 | 0.0005 | Yes | rampavsek2022recipe | Table 3 |
| MGT | 0.2453 | 0.0025 | Yes | ngo2023multiresolution | Table 3 |
| DRew | 0.2536 | 0.0015 | Yes | gutteridge2023drew | Table 3 |
| Graph ViT/MLP-Mixer | 0.2449 | 0.0016 | Yes | he2023generalization | Table 3 |
| Exphormer | 0.2512 | 0.0025 | Yes | shirzad2023exphormer | Table 3 |
| GRIT | 0.2460 | 0.0012 | Yes | ma2023graph | Table 3 |
| Subgraphormer | 0.2475 | 0.0007 | Yes | bar2024subgraphormer | Table 3 |
| GRED | 0.2455 | 0.0013 | Yes | ding2024recurrent | Table 3 |
| GEAET | 0.2547 | 0.0009 | Yes | liang2024graph | Table 3 |
| TIGT | 0.2485 | 0.0015 | Yes | choi2024topology | Table 3 |
| GECO | 0.2464 | 0.0009 | Yes | sancak2024scalable | Table 3 |
| GPNN | 0.2454 | 0.0003 | Yes | lin2024understanding | Table 3 |
| Graph-Mamba | 0.2478 | 0.0016 | Yes | wang2024graph | Table 3 |
| GSSC | 0.2459 | 0.0020 | Yes | huang2024can | Table 3 |
| GCN | 0.2460 | 0.0007 | Yes | this paper | Table 3 |
| GCN+ | 0.2421 | 0.0016 | No | this paper | Table 3 |
| GIN | 0.2473 | 0.0017 | Yes | this paper | Table 3 |
| GIN+ | 0.2429 | 0.0019 | No | this paper | Table 3 |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 3 |
| GatedGCN+ | 0.2431 | 0.0020 | No | this paper | Table 3 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2260 | 0.0140 | Yes | dwivedi2020generalization | Table 2 |
| SAN | 0.1390 | 0.0060 | Yes | kreuzer2021rethinking | Table 2 |
| Graphormer | 0.1220 | 0.0060 | Yes | ying2021transformers | Table 2 |
| SAT | 0.0940 | 0.0080 | Yes | chen2022structure | Table 2 |
| EGT | 0.1080 | 0.0090 | Yes | hussain2022global | Table 2 |
| GraphGPS | 0.0700 | 0.0040 | Yes | rampavsek2022recipe | Table 2 |
| GRPE | 0.0940 | 0.0020 | Yes | park2022grpe | Table 2 |
| Graphormer-URPE | 0.0860 | 0.0070 | Yes | luo2022your | Table 2 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | zhang2023rethinking | Table 2 |
| Specformer | 0.0660 | 0.0030 | Yes | bo2023specformer | Table 2 |
| Graph ViT/MLP-Mixer | 0.0730 | 0.0010 | Yes | he2023generalization | Table 2 |
| GRIT | 0.0590 | 0.0020 | Yes | ma2023graph | Table 2 |
| GRED | 0.0770 | 0.0020 | Yes | ding2024recurrent | Table 2 |
| TIGT | 0.0570 | 0.0020 | Yes | choi2024topology | Table 2 |
| Cluster-GT | 0.0710 | 0.0040 | Yes | huang2024clusterwise | Table 2 |
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 2 |
| GCN+ | 0.0760 | 0.0090 | No | this paper | Table 2 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 2 |
| GIN+ | 0.0650 | 0.0040 | No | this paper | Table 2 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 2 |
| GatedGCN+ | 0.0770 | 0.0050 | No | this paper | Table 2 |

### ogbg-code2 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.1670 | 0.0015 | Yes | dwivedi2020generalization | Table 4 |
| GraphTrans | 0.1830 | 0.0024 | Yes | wu2021representing | Table 4 |
| SAT | 0.1937 | 0.0028 | Yes | chen2022structure | Table 4 |
| GraphGPS | 0.1894 | 0.0024 | Yes | rampavsek2022recipe | Table 4 |
| GECO | 0.1915 | 0.0020 | Yes | sancak2024scalable | Table 4 |
| GCN | 0.1507 | 0.0018 | Yes | this paper | Table 4 |
| GCN+ | 0.1787 | 0.0026 | Yes | this paper | Table 4 |
| GIN | 0.1495 | 0.0023 | Yes | this paper | Table 4 |
| GIN+ | 0.1803 | 0.0019 | Yes | this paper | Table 4 |
| GatedGCN | 0.1606 | 0.0015 | Yes | this paper | Table 4 |
| GatedGCN+ | 0.1896 | 0.0024 | No | this paper | Table 4 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SAN | 0.7785 | 0.2470 | Yes | kreuzer2021rethinking | Table 4 |
| Graphormer (pre-trained) | 0.8051 | 0.0053 | Yes | ying2021transformers | Table 4 |
| EGT (pre-trained) | 0.8060 | 0.0065 | Yes | hussain2022global | Table 4 |
| GraphGPS | 0.7880 | 0.0101 | Yes | rampavsek2022recipe | Table 4 |
| Specformer | 0.7889 | 0.0124 | Yes | bo2023specformer | Table 4 |
| Graph ViT/MLP-Mixer | 0.7997 | 0.0102 | Yes | he2023generalization | Table 4 |
| Exphormer | 0.7834 | 0.0044 | Yes | shirzad2023exphormer | Table 4 |
| GRIT | 0.7835 | 0.0054 | Yes | ma2023graph | Table 4 |
| Subgraphormer | 0.8038 | 0.0192 | Yes | bar2024subgraphormer | Table 4 |
| GECO | 0.7980 | 0.0200 | Yes | sancak2024scalable | Table 4 |
| GSSC | 0.8035 | 0.0142 | Yes | huang2024can | Table 4 |
| GCN | 0.7606 | 0.0097 | Yes | this paper | Table 4 |
| GCN+ | 0.8012 | 0.0124 | Yes | this paper | Table 4 |
| GIN | 0.7835 | 0.0125 | Yes | this paper | Table 4 |
| GIN+ | 0.7928 | 0.0099 | Yes | this paper | Table 4 |
| GatedGCN | 0.7687 | 0.0136 | Yes | this paper | Table 4 |
| GatedGCN+ | 0.8040 | 0.0164 | No | this paper | Table 4 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphTrans | 0.2761 | 0.0029 | Yes | wu2021representing | Table 4 |
| SAN | 0.2765 | 0.0042 | Yes | kreuzer2021rethinking | Table 4 |
| EGT (pre-trained) | 0.2961 | 0.0024 | Yes | hussain2022global | Table 4 |
| GraphGPS | 0.2907 | 0.0028 | Yes | rampavsek2022recipe | Table 4 |
| Specformer | 0.2972 | 0.0023 | Yes | bo2023specformer | Table 4 |
| Exphormer | 0.2849 | 0.0025 | Yes | shirzad2023exphormer | Table 4 |
| GRIT | 0.2362 | 0.0020 | Yes | ma2023graph | Table 4 |
| GECO | 0.2961 | 0.0008 | Yes | sancak2024scalable | Table 4 |
| GCN | 0.2020 | 0.0024 | Yes | this paper | Table 4 |
| GCN+ | 0.2721 | 0.0046 | Yes | this paper | Table 4 |
| GIN | 0.2266 | 0.0028 | Yes | this paper | Table 4 |
| GIN+ | 0.2703 | 0.0024 | Yes | this paper | Table 4 |
| GatedGCN | 0.2670 | 0.0020 | Yes | this paper | Table 4 |
| GatedGCN+ | 0.2981 | 0.0024 | No | this paper | Table 4 |

### ogbg-ppa — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.6454 | 0.0033 | Yes | dwivedi2020generalization | Table 4 |
| SAT | 0.7522 | 0.0056 | Yes | chen2022structure | Table 4 |
| GraphGPS | 0.8015 | 0.0033 | Yes | rampavsek2022recipe | Table 4 |
| GECO | 0.7982 | 0.0042 | Yes | sancak2024scalable | Table 4 |
| GCN | 0.6839 | 0.0084 | Yes | this paper | Table 4 |
| GCN+ | 0.8077 | 0.0041 | Yes | this paper | Table 4 |
| GIN | 0.6892 | 0.0100 | Yes | this paper | Table 4 |
| GIN+ | 0.8107 | 0.0053 | Yes | this paper | Table 4 |
| GatedGCN | 0.7531 | 0.0083 | Yes | this paper | Table 4 |
| GatedGCN+ | 0.8258 | 0.0055 | No | this paper | Table 4 |

## Baseline Models Identified

- **GT** (from: dwivedi2020generalization)
- **SAN** (from: kreuzer2021rethinking)
- **Graphormer** (from: ying2021transformers)
- **SAT** (from: chen2022structure)
- **EGT** (from: hussain2022global)
- **GraphGPS** (from: rampavsek2022recipe)
- **GRPE** (from: park2022grpe)
- **Graphormer-URPE** (from: luo2022your)
- **Graphormer-GD** (from: zhang2023rethinking)
- **Specformer** (from: bo2023specformer)
- **Graph ViT/MLP-Mixer** (from: he2023generalization)
- **GRIT** (from: ma2023graph)
- **GRED** (from: ding2024recurrent)
- **TIGT** (from: choi2024topology)
- **Cluster-GT** (from: huang2024clusterwise)
- **GCN**
- **GIN**
- **GatedGCN**
- **Exphormer** (from: shirzad2023exphormer)
- **GEAET** (from: liang2024graph)
- **GMN** (from: behrouz2024graph)
- **Graph-Mamba** (from: wang2024graph)
- **LGI-GT** (from: yinlgi)
- **GPTrans-Nano** (from: chen2023graph)
- **NAGphormer** (from: chen2023nagphormer)
- **DIFFormer** (from: wu2023difformer)
- **MGT** (from: ngo2023multiresolution)
- **DRew** (from: gutteridge2023drew)
- **Subgraphormer** (from: bar2024subgraphormer)
- **GECO** (from: sancak2024scalable)
- **GPNN** (from: lin2024understanding)
- **GSSC** (from: huang2024can)
- **GraphTrans** (from: wu2021representing)
- **GCN+**
- **GIN+**
- **LDP** (from: cai2018simple)
- **HRN** (from: wu2022simple)

## Extraction Notes

[ZINC] Extracted all models from Table 2 for the ZINC dataset. Ablation table results were skipped
as they represent model variants rather than the standard configuration. Parameter count for ZINC
was noted as ~500K in the table caption. [MNIST] Extracted all models from Table 2 for the MNIST
dataset. Ablation study results were skipped as they represent non-standard configurations (e.g.,
removing FFN or Norm) rather than the default model performance. [CIFAR10] Extracted only CIFAR10
results as requested. Normalized percentages to [0, 1]. Ablation table was partially provided but
contained duplicate results of the main table for the proposed models, so they were not duplicated
in the JSON. [PATTERN] Extracted only PATTERN dataset results from Table 2. Ablation table was
skipped as per instructions to use only the standard/default configuration. All percentage values
were normalized to [0, 1]. [CLUSTER] Extracted only CLUSTER dataset results from Table 2. Ablation
table was skipped as it contains variants of the proposed models rather than the standard
configuration. [Peptides-func] Extracted only Peptides-func results from Table 3. Ablation table
results for GCN+ and GIN+ were redundant with Table 3 and thus not duplicated. Param count estimated
from caption '# Param ~ 500K for all'. [Peptides-struct] Extracted all models from Table 3 for the
Peptides-struct dataset using the MAE metric. Ablation table results for GCN+ and GIN+ were
redundant with Table 3 and omitted to avoid duplication. Param count estimated from caption '# Param
~ 500K for all'. [PascalVOC-SP] Extracted all models for PascalVOC-SP from Table 3. Ablation study
results were skipped as they represent non-standard configurations (e.g., removing dropout/norm)
rather than the default model performance. [COCO-SP] Extracted only COCO-SP results from Table 3.
Ablation study results (Table 4) were skipped as they represent non-standard/modified configurations
of the proposed models. [MalNet-Tiny] Extracted only MalNet-Tiny results from Table 3. Ablation
study results (Table 4) were skipped as they represent non-standard configurations (e.g., removing
edge features or normalization) rather than the default model performance. [ogbg-molhiv] Extracted
only ogbg-molhiv results from Table 4. Ablation study results were skipped as they represent non-
standard configurations (e.g., removing edge features or PE) rather than the default model
performance. [ogbg-molpcba] Extracted only ogbg-molpcba results from Table 4. Ablation table results
for GCN+, GIN+, and GatedGCN+ were identical to Table 4 and thus redundant. Only the primary metric
'Avg. Precision' (normalized to AP) was extracted. [ogbg-ppa] Extracted only ogbg-ppa results from
Table 4. Ablation study results were skipped as they represent non-standard configurations (e.g.,
removing normalization or edge features) as per the prompt instructions to use only the
standard/default configuration. [ogbg-code2] Extracted results for ogbg-code2 from Table 4. Ablation
study results for GCN+, GIN+, and GatedGCN+ were identical to the main results table and thus
redundant, but the main benchmark results are fully captured. [IMDB-B] Extracted only IMDB-B results
as requested. Normalized percentages to decimals. [IMDB-M] Extracted only IMDB-M results as
requested. Normalized percentages to [0, 1] range. [COLLAB] Extracted only COLLAB dataset results as
requested. Normalized percentages to decimals. [MUTAG] Extracted only MUTAG results as requested.
Normalized percentages to decimals. [PTC] failed: Connection error.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*