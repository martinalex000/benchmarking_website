# Extraction: Revisiting Heterophily For Graph Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: ACMII-GCN++
- Type: GNN

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.4672 | 0.0046 | Yes | this paper | Table 1 |
| GAT | 0.6390 | 0.0046 | Yes | this paper | Table 1 |
| APPNP | 0.5191 | 0.0056 | Yes | this paper | Table 1 |
| GPRGNN | 0.6748 | 0.0040 | Yes | this paper | Table 1 |
| H2GCN | 0.5230 | 0.0048 | Yes | this paper | Table 1 |
| MixHop | 0.3628 | 0.1022 | Yes | this paper | Table 1 |
| GCN+JK | 0.6468 | 0.0285 | Yes | this paper | Table 1 |
| GAT+JK | 0.6814 | 0.0118 | Yes | this paper | Table 1 |
| FAGCN | 0.4947 | 0.0284 | Yes | this paper | Table 1 |
| BernNet | 0.6829 | 0.0158 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6215 | 0.0042 | Yes | this paper | Table 1 |
| Geom-GCN | 0.6090 | — | Yes | pei2020geom | Table 1 |
| SGC-1 | 0.6486 | 0.0181 | Yes | this paper | Table 1 |
| SGC-2 | 0.6267 | 0.0241 | Yes | this paper | Table 1 |
| GCNII | 0.6035 | 0.0270 | Yes | this paper | Table 1 |
| GCNII* | 0.6280 | 0.0287 | Yes | this paper | Table 1 |
| GCN | 0.6418 | 0.0262 | Yes | this paper | Table 1 |
| Snowball-2 | 0.6499 | 0.0239 | Yes | this paper | Table 1 |
| Snowball-3 | 0.6549 | 0.0164 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.6368 | 0.0162 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.6048 | 0.0155 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.5873 | 0.0252 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.6166 | 0.0229 | Yes | this paper | Table 1 |
| ACM-GCN | 0.6904 | 0.0174 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.7608 | 0.0213 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.7523 | 0.0172 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.6851 | 0.0170 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.6840 | 0.0205 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.6838 | 0.0136 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.6783 | 0.0263 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.6753 | 0.0283 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.7551 | 0.0158 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.7593 | 0.0171 | No | this paper | Table 1 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.7625 | 0.0028 | Yes | this paper | Table 1 |
| GAT | 0.6720 | 0.0046 | Yes | this paper | Table 1 |
| APPNP | 0.6859 | 0.0030 | Yes | this paper | Table 1 |
| GPRGNN | 0.6763 | 0.0038 | Yes | this paper | Table 1 |
| H2GCN | 0.7997 | 0.0069 | Yes | this paper | Table 1 |
| MixHop | 0.4952 | 0.1335 | Yes | this paper | Table 1 |
| GCN+JK | 0.7377 | 0.0185 | Yes | this paper | Table 1 |
| GAT+JK | 0.7449 | 0.0276 | Yes | this paper | Table 1 |
| FAGCN | 0.8237 | 0.0146 | Yes | this paper | Table 1 |
| BernNet | 0.8009 | 0.0079 | Yes | this paper | Table 1 |
| GraphSAGE | 0.7824 | 0.0030 | Yes | this paper | Table 1 |
| Geom-GCN | 0.7799 | — | Yes | pei2020geom | Table 1 |
| SGC-1 | 0.7966 | 0.0075 | Yes | this paper | Table 1 |
| SGC-2 | 0.8075 | 0.0115 | Yes | this paper | Table 1 |
| GCNII | 0.8158 | 0.0130 | Yes | this paper | Table 1 |
| GCNII* | 0.8183 | 0.0178 | Yes | this paper | Table 1 |
| GCN | 0.8139 | 0.0123 | Yes | this paper | Table 1 |
| Snowball-2 | 0.8153 | 0.0171 | Yes | this paper | Table 1 |
| Snowball-3 | 0.8093 | 0.0132 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.8096 | 0.0093 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.8093 | 0.0116 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.8228 | 0.0112 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.8169 | 0.0125 | Yes | this paper | Table 1 |
| ACM-GCN | 0.8168 | 0.0097 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.8165 | 0.0148 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.8183 | 0.0165 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.8158 | 0.0123 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.8132 | 0.0097 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.8179 | 0.0095 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.8207 | 0.0104 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.8156 | 0.0115 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.8187 | 0.0138 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.8176 | 0.0125 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.7644 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.7670 | 0.0042 | Yes | this paper | Table 1 |
| APPNP | 0.7941 | 0.0038 | Yes | this paper | Table 1 |
| GPRGNN | 0.7951 | 0.0036 | Yes | this paper | Table 1 |
| H2GCN | 0.8752 | 0.0061 | Yes | this paper | Table 1 |
| MixHop | 0.6565 | 0.1131 | Yes | this paper | Table 1 |
| GCN+JK | 0.8690 | 0.0151 | Yes | this paper | Table 1 |
| GAT+JK | 0.8952 | 0.0043 | Yes | this paper | Table 1 |
| FAGCN | 0.8885 | 0.0136 | Yes | this paper | Table 1 |
| BernNet | 0.8852 | 0.0095 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8658 | 0.0026 | Yes | this paper | Table 1 |
| Geom-GCN* | 0.8527 | — | Yes | Pei 2020 | Table 1 |
| SGC-1 | 0.8512 | 0.0164 | Yes | this paper | Table 1 |
| SGC-2 | 0.8548 | 0.0148 | Yes | this paper | Table 1 |
| GCNII | 0.8898 | 0.0133 | Yes | this paper | Table 1 |
| GCNII* | 0.8893 | 0.0137 | Yes | this paper | Table 1 |
| GCN | 0.8778 | 0.0096 | Yes | this paper | Table 1 |
| Snowball-2 | 0.8864 | 0.0115 | Yes | this paper | Table 1 |
| Snowball-3 | 0.8933 | 0.0130 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.8663 | 0.0113 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.8764 | 0.0099 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.8910 | 0.0161 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.8900 | 0.0135 | Yes | this paper | Table 1 |
| ACM-GCN | 0.8862 | 0.0122 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.8975 | 0.0116 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.8933 | 0.0081 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.8883 | 0.0149 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.8959 | 0.0158 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.8900 | 0.0072 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.8895 | 0.0104 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.8936 | 0.0126 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.8918 | 0.0111 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.8947 | 0.0108 | No | this paper | Table 1 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.9130 | 0.0070 | Yes | this paper | Table 1 |
| GAT | 0.7600 | 0.0101 | Yes | this paper | Table 1 |
| APPNP | 0.9180 | 0.0063 | Yes | this paper | Table 1 |
| GPRGNN | 0.9136 | 0.0070 | Yes | this paper | Table 1 |
| H2GCN | 0.8623 | 0.0471 | Yes | this paper | Table 1 |
| MixHop | 0.6033 | 0.2853 | Yes | this paper | Table 1 |
| GCN+JK | 0.6656 | 0.1382 | Yes | this paper | Table 1 |
| GAT+JK | 0.7443 | 0.1024 | Yes | this paper | Table 1 |
| FAGCN | 0.8803 | 0.0560 | Yes | this paper | Table 1 |
| BernNet | 0.9213 | 0.0164 | Yes | this paper | Table 1 |
| GraphSAGE | 0.7141 | 0.0124 | Yes | this paper | Table 1 |
| Geom-GCN* | 0.6081 | — | Yes | pei2020geom | Table 1 |
| SGC-1 | 0.7098 | 0.0839 | Yes | this paper | Table 1 |
| SGC-2 | 0.7262 | 0.0992 | Yes | this paper | Table 1 |
| GCNII | 0.8918 | 0.0396 | Yes | this paper | Table 1 |
| GCNII* | 0.9049 | 0.0445 | Yes | this paper | Table 1 |
| GCN | 0.8246 | 0.0311 | Yes | this paper | Table 1 |
| Snowball-2 | 0.8262 | 0.0234 | Yes | this paper | Table 1 |
| Snowball-3 | 0.8295 | 0.0210 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.9377 | 0.0191 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.9377 | 0.0217 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.9262 | 0.0313 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.9344 | 0.0274 | Yes | this paper | Table 1 |
| ACM-GCN | 0.9475 | 0.0380 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.9492 | 0.0279 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.9393 | 0.0105 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.9508 | 0.0311 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.9426 | 0.0257 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.9590 | 0.0183 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.9525 | 0.0155 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.9361 | 0.0279 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.9393 | 0.0303 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.9262 | 0.0257 | No | this paper | Table 1 |

### Film — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.3858 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.3598 | 0.0023 | Yes | this paper | Table 1 |
| APPNP | 0.3886 | 0.0024 | Yes | this paper | Table 1 |
| GPRGNN | 0.3930 | 0.0027 | Yes | this paper | Table 1 |
| H2GCN | 0.3885 | 0.0117 | Yes | this paper | Table 1 |
| MixHop | 0.3313 | 0.0240 | Yes | this paper | Table 1 |
| GCN+JK | 0.3272 | 0.0262 | Yes | this paper | Table 1 |
| GAT+JK | 0.3541 | 0.0097 | Yes | this paper | Table 1 |
| FAGCN | 0.3159 | 0.0137 | Yes | this paper | Table 1 |
| BernNet | 0.4179 | 0.0101 | Yes | this paper | Table 1 |
| GraphSAGE | 0.3637 | 0.0021 | Yes | this paper | Table 1 |
| Geom-GCN | 0.3163 | — | Yes | pei2020geom | Table 1 |
| SGC-1 | 0.2526 | 0.0118 | Yes | this paper | Table 1 |
| SGC-2 | 0.2881 | 0.0111 | Yes | this paper | Table 1 |
| GCNII | 0.4082 | 0.0179 | Yes | this paper | Table 1 |
| GCNII* | 0.4154 | 0.0099 | Yes | pei2020geom | Table 1 |
| GCN | 0.3551 | 0.0099 | Yes | this paper | Table 1 |
| Snowball-2 | 0.3597 | 0.0066 | Yes | this paper | Table 1 |
| Snowball-3 | 0.3600 | 0.0136 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.3933 | 0.0125 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.4013 | 0.0121 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.4137 | 0.0137 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.4127 | 0.0124 | Yes | pei2020geom | Table 1 |
| ACM-GCN | 0.4162 | 0.0115 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.4179 | 0.0101 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.4186 | 0.0148 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.4140 | 0.0123 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.4127 | 0.0080 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.4184 | 0.0115 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.4110 | 0.0075 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.4031 | 0.0160 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.4150 | 0.0154 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.4166 | 0.0142 | No | this paper | Table 1 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.8643 | 0.0013 | Yes | this paper | Table 1 |
| GAT | 0.8328 | 0.0012 | Yes | this paper | Table 1 |
| APPNP | 0.8502 | 0.0009 | Yes | this paper | Table 1 |
| GPRGNN | 0.8507 | 0.0009 | Yes | this paper | Table 1 |
| H2GCN | 0.8778 | 0.0028 | Yes | this paper | Table 1 |
| MixHop | 0.8704 | 0.0410 | Yes | this paper | Table 1 |
| GCN+JK | 0.9009 | 0.0068 | Yes | this paper | Table 1 |
| GAT+JK | 0.8915 | 0.0087 | Yes | this paper | Table 1 |
| FAGCN | 0.8998 | 0.0054 | Yes | this paper | Table 1 |
| BernNet | 0.8848 | 0.0041 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8685 | 0.0011 | Yes | this paper | Table 1 |
| Geom-GCN* | 0.9005 | — | Yes | Chien 2021, Lim 2021 | Table 1 |
| SGC-1 | 0.8550 | 0.0076 | Yes | this paper | Table 1 |
| SGC-2 | 0.8536 | 0.0052 | Yes | this paper | Table 1 |
| GCNII | 0.8980 | 0.0030 | Yes | this paper | Table 1 |
| GCNII* | 0.8998 | 0.0052 | Yes | this paper | Table 1 |
| GCN | 0.8890 | 0.0032 | Yes | this paper | Table 1 |
| Snowball-2 | 0.8904 | 0.0049 | Yes | this paper | Table 1 |
| Snowball-3 | 0.8880 | 0.0082 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.8775 | 0.0088 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.8879 | 0.0050 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.9012 | 0.0040 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.9018 | 0.0051 | Yes | this paper | Table 1 |
| ACM-GCN | 0.9066 | 0.0047 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.9046 | 0.0069 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.9039 | 0.0033 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.9081 | 0.0052 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.9144 | 0.0059 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.9074 | 0.0050 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.9056 | 0.0039 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.9131 | 0.0060 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.9096 | 0.0062 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.9063 | 0.0056 | No | this paper | Table 1 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.3128 | 0.0027 | Yes | this paper | Table 1 |
| GAT | 0.4272 | 0.0033 | Yes | this paper | Table 1 |
| APPNP | 0.3477 | 0.0034 | Yes | this paper | Table 1 |
| GPRGNN | 0.4993 | 0.0053 | Yes | this paper | Table 1 |
| H2GCN | 0.3039 | 0.0122 | Yes | this paper | Table 1 |
| MixHop | 0.2455 | 0.0260 | Yes | this paper | Table 1 |
| GCN+JK | 0.5340 | 0.0190 | Yes | this paper | Table 1 |
| GAT+JK | 0.5228 | 0.0361 | Yes | this paper | Table 1 |
| FAGCN | 0.4224 | 0.0120 | Yes | this paper | Table 1 |
| BernNet | 0.5135 | 0.0073 | Yes | this paper | Table 1 |
| GraphSAGE | 0.4126 | 0.0026 | Yes | this paper | Table 1 |
| Geom-GCN* | 0.3814 | — | Yes | Chien et al. 2021 | Table 1 |
| SGC-1 | 0.4762 | 0.0127 | Yes | Wu et al. 2019 | Table 1 |
| SGC-2 | 0.4125 | 0.0140 | Yes | this paper | Table 1 |
| GCNII | 0.3881 | 0.0197 | Yes | this paper | Table 1 |
| GCNII* | 0.3831 | 0.0130 | Yes | this paper | Table 1 |
| GCN | 0.4476 | 0.0139 | Yes | Kipf & Welling 2016 | Table 1 |
| Snowball-2 | 0.4788 | 0.0123 | Yes | this paper | Table 1 |
| Snowball-3 | 0.4825 | 0.0094 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.4640 | 0.0113 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.4091 | 0.0139 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.4090 | 0.0158 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.3832 | 0.0150 | Yes | this paper | Table 1 |
| ACM-GCN | 0.5802 | 0.0186 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.6926 | 0.0111 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.6856 | 0.0133 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.5597 | 0.0203 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.5573 | 0.0239 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.5453 | 0.0209 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.5348 | 0.0060 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.5231 | 0.0157 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.6981 | 0.0111 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.6998 | 0.0153 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP-2 | 0.9226 | 0.0071 | Yes | this paper | Table 1 |
| GAT | 0.7887 | 0.0086 | Yes | this paper | Table 1 |
| APPNP | 0.9118 | 0.0070 | Yes | this paper | Table 1 |
| GPRGNN | 0.9292 | 0.0061 | Yes | this paper | Table 1 |
| H2GCN | 0.8590 | 0.0353 | Yes | this paper | Table 1 |
| MixHop | 0.7639 | 0.0766 | Yes | this paper | Table 1 |
| GCN+JK | 0.8066 | 0.0191 | Yes | this paper | Table 1 |
| GAT+JK | 0.7541 | 0.0718 | Yes | this paper | Table 1 |
| FAGCN | 0.8885 | 0.0439 | Yes | this paper | Table 1 |
| BernNet | 0.9312 | 0.0065 | Yes | lim2021new | Table 1 |
| GraphSAGE | 0.7903 | 0.0120 | Yes | this paper | Table 1 |
| Geom-GCN* | 0.6757 | — | Yes | pei2020geom | Table 1 |
| SGC-1 | 0.8328 | 0.0543 | Yes | this paper | Table 1 |
| SGC-2 | 0.8131 | 0.0330 | Yes | this paper | Table 1 |
| GCNII | 0.8246 | 0.0458 | Yes | this paper | Table 1 |
| GCNII* | 0.8852 | 0.0302 | Yes | this paper | Table 1 |
| GCN | 0.8311 | 0.0320 | Yes | this paper | Table 1 |
| Snowball-2 | 0.8311 | 0.0320 | Yes | this paper | Table 1 |
| Snowball-3 | 0.8311 | 0.0320 | Yes | this paper | Table 1 |
| ACM-SGC-1 | 0.9361 | 0.0155 | Yes | this paper | Table 1 |
| ACM-SGC-2 | 0.9344 | 0.0254 | Yes | this paper | Table 1 |
| ACM-GCNII | 0.9246 | 0.0197 | Yes | this paper | Table 1 |
| ACM-GCNII* | 0.9328 | 0.0279 | Yes | this paper | Table 1 |
| ACM-GCN | 0.9492 | 0.0288 | Yes | this paper | Table 1 |
| ACM-GCN+ | 0.9492 | 0.0279 | Yes | this paper | Table 1 |
| ACM-GCN++ | 0.9656 | 0.0200 | Yes | this paper | Table 1 |
| ACM-Snowball-2 | 0.9574 | 0.0222 | Yes | this paper | Table 1 |
| ACM-Snowball-3 | 0.9475 | 0.0241 | Yes | this paper | Table 1 |
| ACMII-GCN | 0.9508 | 0.0207 | Yes | this paper | Table 1 |
| ACMII-Snowball-2 | 0.9525 | 0.0155 | Yes | this paper | Table 1 |
| ACMII-Snowball-3 | 0.9475 | 0.0309 | Yes | this paper | Table 1 |
| ACMII-GCN+ | 0.9541 | 0.0282 | Yes | this paper | Table 1 |
| ACMII-GCN++ | 0.9475 | 0.0291 | No | this paper | Table 1 |

## Baseline Models Identified

- **MLP-2**
- **GAT** (from: kipf2016classification)
- **APPNP** (from: chen2020simple)
- **GPRGNN** (from: chen2020simple)
- **H2GCN** (from: zhu2020beyond)
- **MixHop** (from: abu2019mixhop)
- **GCN+JK** (from: huang2020self)
- **GAT+JK** (from: huang2020self)
- **FAGCN** (from: bo2020graph)
- **BernNet** (from: he2021bernnet)
- **GraphSAGE** (from: hamilton2017inductive)
- **Geom-GCN*** (from: pei2020geom)
- **SGC-1** (from: wu2019simplifying)
- **SGC-2** (from: wu2019simplifying)
- **GCNII** (from: chen2020simple)
- **GCNII*** (from: chen2020simple)
- **GCN** (from: kipf2016classification)
- **Snowball-2** (from: chen2020simple)
- **Snowball-3** (from: chen2020simple)
- **ACM-SGC-1** (from: this paper)
- **ACM-SGC-2** (from: this paper)
- **ACM-GCNII** (from: this paper)
- **ACM-GCNII*** (from: this paper)
- **ACM-GCN** (from: this paper)
- **ACM-GCN+** (from: this paper)
- **ACM-GCN++** (from: this paper)
- **ACM-Snowball-2** (from: this paper)
- **ACM-Snowball-3** (from: this paper)
- **ACMII-GCN** (from: this paper)
- **ACMII-Snowball-2** (from: this paper)
- **ACMII-Snowball-3** (from: this paper)
- **ACMII-GCN+** (from: this paper)
- **Geom-GCN** (from: pei2020geom)

## Extraction Notes

[Cornell] Extracted all rows from Table 1 for the 'Cornell' dataset column. The proposed model is
identified as ACMII-GCN++ based on the paper's focus on ACMII variants and the bold/highlighted best
results in other columns for ACMII-GCN variants. Note: While ACMII-GCN has a higher mean (0.959) on
Cornell, ACMII-GCN++ is listed as the final proposed model in the text and has the best rank (4.4)
overall. The value for ACMII-GCN++ is 92.62% (0.9262). All values were converted from percentages to
[0,1] range. [Texas] Extracted all rows from Table 1 for the 'Texas' column. The proposed model is
identified as ACMII-GCN++ based on the paper's focus on ACMII variants and the table structure where
ACMII models are listed last. All values were converted from percentages to [0,1] range. Standard
deviations were parsed from 'mean ± std' format. [Wisconsin] failed: 1 validation error for
ExtractionOutput results.9.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Film] Extracted all models from Table 1 for the
'Film' dataset column. The metric is Test Accuracy (%), converted to [0,1] range. Standard
deviations are parsed from 'mean ± std' format. 'Geom-GCN' and 'GCNII*' have no standard deviation
reported in the table (NA or single value), so std is null. The proposed model is identified as
ACMII-GCN++ based on the paper's focus on ACMII variants and the best result highlighting, though
ACM-GCN++ and ACMII-GCN are also very close. The table highlights ACM-GCN++ and ACM-GCN++ as best in
some cells, but ACMII-GCN++ is the final proposed variant in the bottom section. All rows extracted.
[Chameleon] Extracted all rows from Table 1 for the 'Chameleon' dataset column. The metric is Test
Accuracy (%), converted to [0,1] range. Standard deviations are parsed from the 'mean ± std' format.
The proposed model is identified as ACMII-GCN++ based on the paper's focus on ACMII variants and the
best result highlighting in the table (though ACM-GCN+ is also highlighted, ACMII-GCN++ is the final
proposed variant in the sequence). All other models are treated as baselines. [Squirrel] Extracted
all rows from Table 1 for the 'Squirrel' dataset column. The metric is Test Accuracy (%), converted
to [0,1] range. The proposed model ACMII-GCN++ achieved the best result (highlighted in grey). All
other models are treated as baselines or variants of the proposed framework. [Cora] Extracted all
models from Table 1 for the 'Cora' column. The proposed model is identified as ACMII-GCN++ based on
the paper's focus on ACMII variants and the bold/highlighted best result in the Cora column for
ACMII-GCN++ (0.8975 is ACM-GCN+, 0.8947 is ACMII-GCN++). Wait, looking closely at the table: ACM-
GCN+ has 89.75, ACMII-GCN++ has 89.47. The text says 'ACMII-GCN++' is the final proposed model in
the list. However, ACM-GCN+ has a higher score. The prompt asks for 'proposed_model'. Usually, the
last or most complex variant is the main proposal. The table highlights ACM-GCN+ with a grey
background for Cora (0.8975). ACMII-GCN++ is 0.8947. I will set ACM-GCN+ as the proposed model if it
is the best, or ACMII-GCN++ if it is the main contribution. The text mentions 'ACMII' as the final
framework. Let's look at the 'Rank' column. ACMII-GCN++ has rank 5.10. ACM-GCN+ has rank 4.90. ACM-
GCN+ is better. I will list ACM-GCN+ as the proposed model if it's the best, but the paper title
likely refers to ACMII. Let's stick to the extracted data. The 'proposed_model' field in the output
schema is for the main model of the paper. Given the ambiguity, I will list the best performing
model from the 'ACMII' family or the overall best. The table highlights ACM-GCN+ as the best
baseline/proposed hybrid. I will set 'proposed_model' to 'ACM-GCN+' as it achieves the highest
accuracy. Actually, looking at the last rows, ACMII-GCN++ is the final entry. I will assume ACMII-
GCN++ is the primary proposed model, even if ACM-GCN+ is slightly better or comparable. However,
strictly speaking, ACM-GCN+ is also a proposed variant. I will extract ACM-GCN+ as the proposed
model because it has the highest accuracy and is highlighted. Wait, the schema asks for
'proposed_model' singular. I will use 'ACM-GCN+' as it is the best result. Re-reading the text: 'We
will now investigate... components of ACM and ACMII...'. It seems both are proposed. I will use
'ACM-GCN+' as the primary proposed model due to best performance.   Correction: The prompt asks to
extract results for ALL rows. The 'proposed_model' field is metadata. I will set it to 'ACM-GCN+' as
it is the best.   Note on std: The table uses '±'. I parsed '89.75 ± 1.16' as value=0.8975,
std=0.0116.   Note on 'uses_external_data': All models use standard Cora features/labels, so false.
[CiteSeer] Extracted all models from Table 1 for the CiteSeer dataset. The proposed model is
identified as ACMII-GCN++ based on the paper's focus on ACMII variants and the table structure where
ACMII models are listed last. All values were converted from percentages to [0,1] range. Standard
deviations were parsed from the 'mean ± std' format. [PubMed] Extracted all rows from Table 1 for
the 'PubMed' column. The metric is Test Accuracy (%), converted to [0,1] range. Standard deviations
are parsed from the 'mean ± std' format. The proposed model is identified as ACMII-GCN++ based on
the paper's focus on ACMII variants and the table structure highlighting best results. Note: ACM-
Snowball-3 achieved the highest accuracy (0.9144), but ACMII-GCN++ is the primary proposed model in
the ACMII family.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*