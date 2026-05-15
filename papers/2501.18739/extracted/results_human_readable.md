# Extraction: arXiv:2501.18739
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: GPM
- Type: GraphTransformer

## Results

### Arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7174 | 0.0029 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.7201 | 0.0020 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.6940 | 0.0050 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.7110 | 0.0012 | Yes | chien2021adaptive | Table 1 |
| RUM | 0.7054 | 0.0030 | Yes | wang2024nonconvolutional | Table 1 |
| GraphGPS | 0.7097 | 0.0041 | Yes | rampasek2022recipe | Table 1 |
| NodeFormer | 0.6719 | 0.0083 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.7241 | 0.0040 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.7013 | 0.0055 | Yes | chen2023nagphormer | Table 1 |
| GraphMamba | 0.7248 | 0.0000 | Yes | behrouz2024graph | Table 1 |
| GPM | 0.7289 | 0.0068 | No | this paper | Table 1 |

### Blog — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9412 | 0.0079 | Yes | kipf2017semisupervised | Table ef{tab:node} |
| GAT | 0.9347 | 0.0063 | Yes | velickovic2018graph | Table ef{tab:node} |
| APPNP | 0.9477 | 0.0019 | Yes | gasteiger2018combining | Table ef{tab:node} |
| GPRGNN | 0.9436 | 0.0029 | Yes | chien2021adaptive | Table ef{tab:node} |
| OrderedGNN | 0.9590 | 0.0044 | Yes | song2023ordered | Table ef{tab:node} |
| RAW-GNN | 0.9496 | 0.0070 | Yes | jin2022raw | Table ef{tab:node} |
| RUM | 0.9416 | 0.0035 | Yes | wang2024nonconvolutional | Table ef{tab:node} |
| GraphGPS | 0.9435 | 0.0052 | Yes | rampasek2022recipe | Table ef{tab:node} |
| SAN | 0.9021 | 0.0020 | Yes | kreuzer2021rethinking | Table ef{tab:node} |
| NodeFormer | 0.9379 | 0.0076 | Yes | wu2022nodeformer | Table ef{tab:node} |
| GOAT | 0.9440 | 0.0008 | Yes | kong2023goat | Table ef{tab:node} |
| NAGphormer | 0.9442 | 0.0063 | Yes | chen2023nagphormer | Table ef{tab:node} |
| VCR-Graphormer | 0.9392 | 0.0037 | Yes | fu2024vcrgraphormer | Table ef{tab:node} |
| GCFormer | 0.9603 | 0.0044 | Yes | chen2024leveraging | Table ef{tab:node} |
| GPM | 0.9671 | 0.0059 | No | this paper | Table ef{tab:node} |

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.8059 | 0.0027 | Yes | xu2018how | Table 1 |
| DGK | 0.7309 | 0.0025 | Yes | yanardag2015deep | Table 1 |
| PNA | 0.7473 | 0.0109 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.7735 | 0.0093 | Yes | zhao2022from | Table 1 |
| AWE | 0.7393 | 0.0194 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.7717 | 0.0078 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.7730 | 0.0198 | Yes | martinkus2023agentbased | Table 1 |
| RUM | 0.7550 | 0.0058 | Yes | wang2024nonconvolutional | Table 1 |
| GMT | 0.7894 | 0.0044 | Yes | baek2021accurate | Table 1 |
| SAN | 0.7445 | 0.0246 | Yes | kreuzer2021rethinking | Table 1 |
| Graphormer | 0.7882 | 0.0121 | Yes | ying2021transformers | Table 1 |
| GPS | 0.7741 | 0.0056 | Yes | rampasek2022recipe | Table 1 |
| SAT | 0.7835 | 0.0085 | Yes | chen2022structure | Table 1 |
| GraphViT | 0.7879 | 0.0074 | Yes | he2023generalization | Table 1 |
| GPM | 0.8070 | 0.0074 | No | this paper | Table 1 |

### Computer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8965 | 0.0052 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.9078 | 0.0013 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.9018 | 0.0017 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.8932 | 0.0029 | Yes | chien2021adaptive | Table 1 |
| OrderedGNN | 0.9203 | 0.0013 | Yes | song2023ordered | Table 1 |
| RAW-GNN | 0.9098 | 0.0073 | Yes | jin2022raw | Table 1 |
| RUM | 0.9062 | 0.0024 | Yes | wang2024nonconvolutional | Table 1 |
| GraphGPS | 0.9119 | 0.0054 | Yes | rampasek2022recipe | Table 1 |
| SAN | 0.8983 | 0.0016 | Yes | kreuzer2021rethinking | Table 1 |
| NodeFormer | 0.8698 | 0.0062 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.9096 | 0.0090 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.9122 | 0.0014 | Yes | chen2023nagphormer | Table 1 |
| VCR-Graphormer | 0.9104 | 0.0012 | Yes | fu2024vcrgraphormer | Table 1 |
| GCFormer | 0.9163 | 0.0018 | Yes | chen2024leveraging | Table 1 |
| GPM | 0.9228 | 0.0039 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8414 | 0.0119 | Yes | kipf2017semisupervised | Table 1 |
| LLP | 0.8995 | 0.0201 | Yes | guo2023linkless | Table 1 |
| RUM | 0.8874 | 0.0060 | Yes | wang2024nonconvolutional | Table 1 |
| NodeFormer | 0.8078 | 0.0144 | Yes | wu2022nodeformer | Table 1 |
| NAGphormer | 0.8687 | 0.0158 | Yes | chen2023nagphormer | Table 1 |
| GPM | 0.9285 | 0.0054 | No | this paper | Table 1 |

### CoraFull — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6176 | 0.0014 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.6447 | 0.0018 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.6516 | 0.0028 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.6712 | 0.0031 | Yes | chien2021adaptive | Table 1 |
| OrderedGNN | 0.6921 | 0.0023 | Yes | song2023ordered | Table 1 |
| RAW-GNN | 0.6864 | 0.0055 | Yes | jin2022raw | Table 1 |
| RUM | 0.7042 | 0.0008 | Yes | wang2024nonconvolutional | Table 1 |
| GraphGPS | 0.5576 | 0.0023 | Yes | rampasek2022recipe | Table 1 |
| SAN | 0.5901 | 0.0034 | Yes | kreuzer2021rethinking | Table 1 |
| NodeFormer | 0.7101 | 0.0014 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.6855 | 0.0034 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.7151 | 0.0013 | Yes | chen2023nagphormer | Table 1 |
| VCR-Graphormer | 0.6878 | 0.0029 | Yes | fu2024vcrgraphormer | Table 1 |
| GCFormer | 0.6970 | 0.0054 | Yes | chen2024leveraging | Table 1 |
| GPM | 0.7123 | 0.0051 | No | this paper | Table 1 |

### Deezer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6270 | 0.0070 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.6170 | 0.0080 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.6610 | 0.0060 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.6320 | 0.0084 | Yes | chien2021adaptive | Table 1 |
| OrderedGNN | 0.6612 | 0.0075 | Yes | song2023ordered | Table 1 |
| RAW-GNN | 0.6511 | 0.0064 | Yes | jin2022raw | Table 1 |
| RUM | 0.6425 | 0.0062 | Yes | wang2024nonconvolutional | Table 1 |
| GraphGPS | 0.6056 | 0.0062 | Yes | rampasek2022recipe | Table 1 |
| SAN | 0.6429 | 0.0035 | Yes | kreuzer2021rethinking | Table 1 |
| NodeFormer | 0.6640 | 0.0070 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.6531 | 0.0024 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.6554 | 0.0057 | Yes | chen2023nagphormer | Table 1 |
| VCR-Graphormer | 0.6528 | 0.0051 | Yes | fu2024vcrgraphormer | Table 1 |
| GCFormer | 0.6516 | 0.0033 | Yes | chen2024leveraging | Table 1 |
| GPM | 0.6726 | 0.0022 | No | this paper | Table 1 |

### EXP — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5190 | — | Yes | kipf2017semisupervised | Table 1 |
| GatedGCN | 0.5170 | — | Yes | bresson2017residual | Table 1 |
| GraphTrans | 0.5240 | — | Yes | dwivedi2020generalization | Table 1 |
| 3-GNN | 0.9970 | — | Yes | morris2019weisfeiler | Table 1 |
| GIN-AK+ | 1.0000 | — | Yes | zhao2022from | Table 1 |
| GraphViT | 1.0000 | — | Yes | he2023generalization | Table 1 |
| ESC-GNN | 1.0000 | — | Yes | yan2024efficient | Table 1 |
| GPM | 1.0000 | — | No | this paper | Table 1 |

### Flickr — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5090 | 0.0012 | Yes | kipf2017semisupervised | Table ef{tab:node} |
| GAT | 0.5070 | 0.0032 | Yes | velickovic2018graph | Table ef{tab:node} |
| APPNP | 0.5036 | 0.0055 | Yes | gasteiger2018combining | Table ef{tab:node} |
| GPRGNN | 0.4832 | 0.0120 | Yes | chien2021adaptive | Table ef{tab:node} |
| OrderedGNN | 0.5120 | 0.0032 | Yes | song2023ordered | Table ef{tab:node} |
| RAW-GNN | 0.4958 | 0.0038 | Yes | jin2022raw | Table ef{tab:node} |
| RUM | 0.5097 | 0.0032 | Yes | wang2024nonconvolutional | Table ef{tab:node} |
| GraphGPS | 0.4515 | 0.0241 | Yes | rampasek2022recipe | Table ef{tab:node} |
| NodeFormer | 0.5123 | 0.0064 | Yes | wu2022nodeformer | Table ef{tab:node} |
| GOAT | 0.4830 | 0.0047 | Yes | kong2023goat | Table ef{tab:node} |
| NAGphormer | 0.4966 | 0.0029 | Yes | chen2023nagphormer | Table ef{tab:node} |
| VCR-Graphormer | 0.5077 | 0.0061 | Yes | fu2024vcrgraphormer | Table ef{tab:node} |
| GCFormer | 0.5028 | 0.0069 | Yes | chen2024leveraging | Table ef{tab:node} |
| GPM | 0.5222 | 0.0019 | No | this paper | Table ef{tab:node} |

### Flickr-S — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8458 | 0.0049 | Yes | kipf2017semisupervised | Table ef{tab:node} |
| GAT | 0.8511 | 0.0067 | Yes | velickovic2018graph | Table ef{tab:node} |
| APPNP | 0.8466 | 0.0031 | Yes | gasteiger2018combining | Table ef{tab:node} |
| GPRGNN | 0.8591 | 0.0051 | Yes | chien2021adaptive | Table ef{tab:node} |
| OrderedGNN | 0.8868 | 0.0054 | Yes | song2023ordered | Table ef{tab:node} |
| RAW-GNN | 0.8653 | 0.0065 | Yes | jin2022raw | Table ef{tab:node} |
| RUM | 0.8725 | 0.0066 | Yes | wang2024nonconvolutional | Table ef{tab:node} |
| GraphGPS | 0.8361 | 0.0070 | Yes | rampasek2022recipe | Table ef{tab:node} |
| NodeFormer | 0.8830 | 0.0022 | Yes | wu2022nodeformer | Table ef{tab:node} |
| GOAT | 0.8816 | 0.0095 | Yes | kong2023goat | Table ef{tab:node} |
| NAGphormer | 0.8685 | 0.0085 | Yes | chen2023nagphormer | Table ef{tab:node} |
| VCR-Graphormer | 0.8623 | 0.0074 | Yes | fu2024vcrgraphormer | Table ef{tab:node} |
| GCFormer | 0.8790 | 0.0045 | Yes | chen2024leveraging | Table ef{tab:node} |
| GPM | 0.8941 | 0.0047 | No | this paper | Table ef{tab:node} |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.7326 | 0.0046 | Yes | xu2018how | Table 1 |
| DGK | 0.6696 | 0.0056 | Yes | yanardag2015deep | Table 1 |
| PNA | 0.7231 | 0.0367 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.7500 | 0.0420 | Yes | zhao2022from | Table 1 |
| AWE | 0.7445 | 0.0583 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.7369 | 0.0205 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.7588 | 0.0360 | Yes | martinkus2023agentbased | Table 1 |
| RUM | 0.8110 | 0.0450 | Yes | wang2024nonconvolutional | Table 1 |
| GMT | 0.7348 | 0.0076 | Yes | baek2021accurate | Table 1 |
| SAN | 0.7600 | 0.0190 | Yes | kreuzer2021rethinking | Table 1 |
| Graphormer | 0.7674 | 0.0086 | Yes | ying2021transformers | Table 1 |
| GPS | 0.7776 | 0.0098 | Yes | rampasek2022recipe | Table 1 |
| SAT | 0.7829 | 0.0126 | Yes | chen2022structure | Table 1 |
| GraphViT | 0.7805 | 0.0100 | Yes | he2023generalization | Table 1 |
| GPM | 0.8267 | 0.0047 | No | this paper | Table 1 |

### Products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7564 | 0.0021 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.7945 | 0.0059 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.7758 | 0.0047 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.7976 | 0.0059 | Yes | chien2021adaptive | Table 1 |
| RUM | 0.7868 | 0.0140 | Yes | wang2024nonconvolutional | Table 1 |
| NodeFormer | 0.7293 | 0.0013 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.8200 | 0.0043 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.7355 | 0.0021 | Yes | chen2023nagphormer | Table 1 |
| GPM | 0.8262 | 0.0039 | No | this paper | Table 1 |

### Pubmed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8506 | 0.0379 | Yes | kipf2017semisupervised | Table 1 |
| LLP | 0.8723 | 0.0492 | Yes | guo2023linkless | Table 1 |
| RUM | 0.8587 | 0.0393 | Yes | wang2024nonconvolutional | Table 1 |
| NodeFormer | 0.8393 | 0.0472 | Yes | wu2022nodeformer | Table 1 |
| NAGphormer | 0.8646 | 0.0409 | Yes | chen2023nagphormer | Table 1 |
| GPM | 0.8829 | 0.0515 | No | this paper | Table 1 |

### Reddit-M12K — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.3937 | 0.0140 | Yes | xu2018how | Table 1 |
| DGK | 0.3222 | 0.0010 | Yes | yanardag2015deep | Table 1 |
| PNA | 0.3857 | 0.0186 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.4060 | 0.0099 | Yes | zhao2022from | Table 1 |
| AWE | 0.3920 | 0.0209 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.4072 | 0.0065 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.4215 | 0.0013 | Yes | martinkus2023agentbased | Table 1 |
| RUM | 0.4166 | 0.0015 | Yes | wang2024nonconvolutional | Table 1 |
| GMT | 0.4063 | 0.0094 | Yes | baek2021accurate | Table 1 |
| SAN | 0.3992 | 0.0102 | Yes | kreuzer2021rethinking | Table 1 |
| Graphormer | 0.4142 | 0.0042 | Yes | ying2021transformers | Table 1 |
| GPS | 0.4155 | 0.0016 | Yes | rampasek2022recipe | Table 1 |
| SAT | 0.4214 | 0.0007 | Yes | chen2022structure | Table 1 |
| GraphViT | 0.4017 | 0.0052 | Yes | he2023generalization | Table 1 |
| GPM | 0.4307 | 0.0029 | No | this paper | Table 1 |

### Reddit-M5K — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4588 | 0.0078 | Yes | xu2018how | Table 1 |
| DGK | 0.4127 | 0.0018 | Yes | yanardag2015deep | Table 1 |
| PNA | 0.4218 | 0.0296 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.4778 | 0.0112 | Yes | zhao2022from | Table 1 |
| AWE | 0.5046 | 0.0191 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.4881 | 0.0167 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.4771 | 0.0094 | Yes | martinkus2023agentbased | Table 1 |
| RUM | 0.4866 | 0.0076 | Yes | wang2024nonconvolutional | Table 1 |
| GMT | 0.4996 | 0.0121 | Yes | baek2021accurate | Table 1 |
| SAN | 0.5076 | 0.0041 | Yes | kreuzer2021rethinking | Table 1 |
| Graphormer | 0.4898 | 0.0030 | Yes | ying2021transformers | Table 1 |
| GPS | 0.4909 | 0.0071 | Yes | rampasek2022recipe | Table 1 |
| SAT | 0.4702 | 0.0088 | Yes | chen2022structure | Table 1 |
| GraphViT | 0.4839 | 0.0078 | Yes | he2023generalization | Table 1 |
| GPM | 0.5187 | 0.0104 | No | this paper | Table 1 |

### SR25 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0670 | — | Yes | kipf2017semisupervised | Table 1 |
| GatedGCN | 0.0670 | — | Yes | bresson2017residual | Table 1 |
| GraphTrans | 0.0670 | — | Yes | dwivedi2020generalization | Table 1 |
| 3-GNN | 0.0670 | — | Yes | morris2019weisfeiler | Table 1 |
| GIN-AK+ | 0.0670 | — | Yes | zhao2022from | Table 1 |
| GraphViT | 1.0000 | — | Yes | he2023generalization | Table 1 |
| ESC-GNN | 1.0000 | — | Yes | yan2024efficient | Table 1 |
| GPM | 1.0000 | — | No | this paper | Table 1 |

### Twitch — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5668 | — | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.5686 | — | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.5426 | — | Yes | gasteiger2018combining | Table 1 |
| RUM | 0.5859 | — | Yes | wang2024nonconvolutional | Table 1 |
| NodeFormer | 0.5417 | — | Yes | wu2022nodeformer | Table 1 |
| NAGphormer | 0.5419 | — | Yes | chen2023nagphormer | Table 1 |
| DANN | 0.6071 | — | Yes | ganin2016domain | Table 1 |
| SR-GNN | 0.5965 | — | Yes | zhu2021shift | Table 1 |
| StruRW | 0.6146 | — | Yes | liu2023structural | Table 1 |
| SSReg | 0.6043 | — | Yes | you2023graph | Table 1 |
| GPM | 0.6163 | — | No | this paper | Table 1 |
| GPM + DANN | 0.6298 | — | No | this paper | Table 1 |
| GPM + SSReg | 0.6277 | — | No | this paper | Table 1 |

### WikiCS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7747 | 0.0085 | Yes | kipf2017semisupervised | Table 1 |
| GAT | 0.7691 | 0.0082 | Yes | velickovic2018graph | Table 1 |
| APPNP | 0.7887 | 0.0011 | Yes | gasteiger2018combining | Table 1 |
| GPRGNN | 0.7812 | 0.0023 | Yes | chien2021adaptive | Table 1 |
| OrderedGNN | 0.7901 | 0.0068 | Yes | song2023ordered | Table 1 |
| RAW-GNN | 0.7801 | 0.0058 | Yes | jin2022raw | Table 1 |
| RUM | 0.7820 | 0.0029 | Yes | wang2024nonconvolutional | Table 1 |
| GraphGPS | 0.7866 | 0.0049 | Yes | rampasek2022recipe | Table 1 |
| SAN | 0.7846 | 0.0099 | Yes | kreuzer2021rethinking | Table 1 |
| NodeFormer | 0.7473 | 0.0094 | Yes | wu2022nodeformer | Table 1 |
| GOAT | 0.7700 | 0.0077 | Yes | kong2023goat | Table 1 |
| NAGphormer | 0.7716 | 0.0072 | Yes | chen2023nagphormer | Table 1 |
| VCR-Graphormer | 0.7769 | 0.0033 | Yes | fu2024vcrgraphormer | Table 1 |
| GCFormer | 0.7812 | 0.0050 | Yes | chen2024leveraging | Table 1 |
| GPM | 0.8019 | 0.0041 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5260 | 0.0510 | Yes | xu2018how | Table 1 |
| PNA | 0.1420 | 0.0100 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.0800 | 0.0010 | Yes | zhao2022from | Table 1 |
| AWE | 0.0940 | 0.0050 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.0850 | 0.0040 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.1440 | 0.0160 | Yes | martinkus2023agentbased | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | kreuzer2021rethinking | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | ying2021transformers | Table 1 |
| GPS | 0.0700 | 0.0040 | Yes | rampasek2022recipe | Table 1 |
| SAT | 0.0940 | 0.0080 | Yes | chen2022structure | Table 1 |
| DeepGraph | 0.0720 | 0.0040 | Yes | zhao2023are | Table 1 |
| GraphViT | 0.0730 | 0.0010 | Yes | he2023generalization | Table 1 |
| GEANet | 0.1930 | 0.0010 | Yes | liang2024graph | Table 1 |
| GPM | 0.0640 | 0.0040 | No | this paper | Table 1 |

### ZINC-Full — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0880 | 0.0020 | Yes | xu2018how | Table 1 |
| PNA | 0.0670 | 0.0090 | Yes | corso2020principal | Table 1 |
| GNN-AK+ | 0.0340 | 0.0070 | Yes | zhao2022from | Table 1 |
| AWE | 0.0590 | 0.0050 | Yes | ivanov2018anonymous | Table 1 |
| CRaWl | 0.0360 | 0.0050 | Yes | tonshoff2023walking | Table 1 |
| AgentNet | 0.0400 | 0.0060 | Yes | martinkus2023agentbased | Table 1 |
| Graphormer | 0.0250 | 0.0040 | Yes | ying2021transformers | Table 1 |
| SAT | 0.0360 | 0.0020 | Yes | chen2022structure | Table 1 |
| GraphViT | 0.0350 | 0.0050 | Yes | he2023generalization | Table 1 |
| GPM | 0.0210 | 0.0020 | No | this paper | Table 1 |

### ogbl-Collab — Hits@50 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4475 | 0.0107 | Yes | kipf2017semisupervised | Table 1 |
| LLP | 0.4910 | 0.0057 | Yes | guo2023linkless | Table 1 |
| RUM | 0.4819 | 0.0094 | Yes | wang2024nonconvolutional | Table 1 |
| NodeFormer | 0.4656 | 0.0062 | Yes | wu2022nodeformer | Table 1 |
| NAGphormer | 0.4756 | 0.0052 | Yes | chen2023nagphormer | Table 1 |
| GPM | 0.4970 | 0.0059 | No | this paper | Table 1 |
| GPM w/o PE | 0.4959 | 0.0065 | Yes | this paper | Table 2 |
| GPM w/o AP | 0.4843 | 0.0097 | Yes | this paper | Table 2 |
| GPM w/o PE & AP | 0.4824 | 0.0097 | Yes | this paper | Table 2 |
| GPM Mean | 0.4783 | 0.0100 | Yes | this paper | Table 2 |
| GPM GRU | 0.4812 | 0.0055 | Yes | this paper | Table 2 |
| GPM Transformer | 0.4970 | 0.0059 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: kipf2017semisupervised)
- **GAT** (from: velickovic2018graph)
- **APPNP** (from: gasteiger2018combining)
- **GPRGNN** (from: chien2021adaptive)
- **OrderedGNN** (from: song2023ordered)
- **RAW-GNN** (from: jin2022raw)
- **RUM** (from: wang2024nonconvolutional)
- **GraphGPS** (from: rampasek2022recipe)
- **SAN** (from: kreuzer2021rethinking)
- **NodeFormer** (from: wu2022nodeformer)
- **GOAT** (from: kong2023goat)
- **NAGphormer** (from: chen2023nagphormer)
- **GraphMamba** (from: behrouz2024graph)
- **VCR-Graphormer** (from: fu2024vcrgraphormer)
- **GCFormer** (from: chen2024leveraging)
- **LLP** (from: guo2023linkless)
- **GIN** (from: xu2018how)
- **DGK** (from: yanardag2015deep)
- **PNA** (from: corso2020principal)
- **GNN-AK+** (from: zhao2022from)
- **AWE** (from: ivanov2018anonymous)
- **CRaWl** (from: tonshoff2023walking)
- **AgentNet** (from: martinkus2023agentbased)
- **GMT** (from: baek2021accurate)
- **Graphormer** (from: ying2021transformers)
- **GPS** (from: rampasek2022recipe)
- **SAT** (from: chen2022structure)
- **GraphViT** (from: he2023generalization)
- **DeepGraph** (from: zhao2023are)
- **GEANet** (from: liang2024graph)
- **DANN** (from: ganin2016domain)
- **SR-GNN** (from: zhu2021shift)
- **StruRW** (from: liu2023structural)
- **SSReg** (from: you2023graph)
- **GatedGCN** (from: bresson2017residual)
- **GraphTrans** (from: dwivedi2020generalization)
- **3-GNN** (from: morris2019weisfeiler)
- **GIN-AK+** (from: zhao2022from)
- **ESC-GNN** (from: yan2024efficient)

## Extraction Notes

[Products] Extracted only 'Products' dataset results from Table 1. Ablation results from Table 2
were skipped as they represent model variants rather than the standard configuration. OOM and '-'
values were ignored. [Computer] Extracted only results for the 'Computer' dataset as requested.
Ablation table results were skipped as they represent model variants rather than the standard
configuration of the proposed model or baselines. [Arxiv] Extracted only Arxiv results from Table 1.
Ablation results from Table 2 were skipped as they represent model variants rather than the standard
configuration of the proposed model or baselines. Some baselines (OrderedGNN, RAW-GNN, SAN, VCR-
Graphormer, GCFormer) had no reported values for Arxiv in Table 1. [WikiCS] Extracted only WikiCS
results from Table 1 as requested. Ablation results from Table 2 were skipped as they represent
model variants rather than the standard configuration of the proposed model or baselines. [CoraFull]
Extracted only CoraFull results from Table 1. Ablation table results were skipped as they represent
model variants rather than the standard configuration of the proposed model or baselines. [Deezer]
The primary metric requested was ROC-AUC, but the provided tables for the Deezer dataset report node
classification results, which are typically Accuracy. I have extracted these as Accuracy. Ablation
results from Table 2 were skipped as they represent model variants rather than the standard
configuration. [Blog] Extracted only results for the 'Blog' dataset from the main results table.
Ablation table results were skipped as they represent model variants rather than the standard
configuration of the proposed model or baselines. [Flickr] Extracted only the 'Flickr' column as
requested. 'Flickr-S' was ignored as it is a variant. SAN and GraphMamba had no values for Flickr
(OOM or missing). [Flickr-S] Extracted only Flickr-S column from Table  ef{tab:node}. SAN and
GraphMamba had OOM or missing values for this dataset and were excluded from the results list.
[Cora] The table caption mentions 'link prediction results', but the primary metric requested was
Accuracy. Link prediction is typically evaluated via AUC or Accuracy; given the values (80-92%),
these are treated as Accuracy percentages and normalized to [0, 1]. [Pubmed] Extracted only Pubmed
results as requested. Normalized percentages to [0, 1] range. [ogbl-Collab] Extracted results for
ogbl-Collab from both the main results table and the ablation table. Metric assumed to be Hits@50
based on the primary metric instruction and common ogbl-Collab benchmarks. [IMDB-B] Extracted only
IMDB-B results as requested. Values were converted from percentages to decimals. [COLLAB] Extracted
only COLLAB results from Table 1. Table 2 contains ablation studies for the proposed model on
COLLAB, but per instructions to focus on the standard benchmark results, the primary results from
Table 1 were prioritized. All percentage values were normalized to [0, 1]. [Reddit-M5K] Extracted
only Reddit-M5K results as requested. Normalized percentage values to [0, 1] range. [Reddit-M12K]
Extracted only Reddit-M12K results as requested. Normalized percentages to [0, 1] range. [ZINC]
Extracted only ZINC dataset results as requested. ZINC-Full was ignored. Metric was identified as
MAE based on the downward arrow (lower is better) and standard ZINC benchmark usage. [ZINC-Full]
Extracted only ZINC-Full results as requested. Metric is MAE (indicated by downward arrow in table
header). Models with '-' for ZINC-Full were skipped. [Twitch] Extracted only the Twitch column as
requested. Values were converted from percentages to decimals. No standard deviations were provided
for the Twitch dataset in the table. [CSL] failed: 1 validation error for ExtractionOutput
results.4.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[EXP] Values in Table 1 were reported as percentages (e.g., 51.9) and normalized to [0, 1] as per
instructions. Metric was inferred as Accuracy based on the context of distinguishing non-isomorphic
graphs. [SR25] Values in the table were reported as percentages (e.g., 6.7, 100) and have been
normalized to [0, 1] as per instructions.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*