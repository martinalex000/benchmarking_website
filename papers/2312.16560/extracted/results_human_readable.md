# Extraction: Adaptive Message Passing: A General Framework to Mitigate Oversmoothing, Oversquashing, and Underreaching
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: AMP
- Type: GNN

## Main Figure: Figure 1
> The graphical model of AMP , where white and blue circles denote, respectively, latent and observable random v
- This figure illustrates the graphical model of the proposed Adaptive Message Passing (AMP) framework, serving as the primary visual representation of the method's architecture and latent variable structure.

## Results

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 35.8600 | 1.0300 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 35.6200 | 1.3000 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 34.2300 | 0.9900 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 34.1100 | 1.0900 | Yes | Defferrard et al. 2016 | Table 1 |
| MixHop | 32.2200 | 2.3400 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 34.2800 | 1.0100 | Yes | Hamilton et al. 2017; Xu et al. 2018 | Table 1 |
| Cheby+JK | 35.1400 | 1.3700 | Yes | Defferrard et al. 2016; Xu et al. 2018 | Table 1 |
| GCN+JK | 34.1800 | 0.8500 | Yes | Kipf & Welling 2016; Xu et al. 2018 | Table 1 |
| GAT | 26.2800 | 1.7300 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 31.6300 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 35.7600 | 0.9800 | Yes | Generic baseline | Table 1 |
| GCN | 28.0200 | 0.5900 | Yes | Kipf & Welling 2016 | Table 1 |
| AMP | 34.1400 | 0.7100 | Yes | Zhu et al. 2020 | Table 1 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 57.1100 | 1.5800 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 59.3900 | 1.9800 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 58.7300 | 1.6800 | Yes | Zhu et al. 2020 | Table 1 |
| GCN-Cheby | 55.2400 | 2.7600 | Yes | Zhu et al. 2020 | Table 1 |
| MixHop | 60.5000 | 2.5300 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE+JK | 58.1100 | 1.9700 | Yes | Zhu et al. 2020 | Table 1 |
| Cheby+JK | 63.7900 | 2.2700 | Yes | Zhu et al. 2020 | Table 1 |
| GCN+JK | 63.4200 | 2.0000 | Yes | Zhu et al. 2020 | Table 1 |
| GAT | 54.6900 | 1.9500 | Yes | Zhu et al. 2020 | Table 1 |
| GEOM-GCN* | 60.9000 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 46.3600 | 2.5200 | Yes | Zhu et al. 2020 | Table 1 |
| GCN | 41.8900 | 1.8300 | Yes | Zhu et al. 2020 | Table 1 |
| AMP_GCN | 48.5600 | 1.7000 | Yes | Zhu et al. 2020 | Table 1 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 77.0700 | 1.6400 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 76.8800 | 1.7700 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 76.0400 | 1.3000 | Yes | Zhu et al. 2020 | Table 1 |
| GCN-Cheby | 75.8200 | 1.5300 | Yes | Zhu et al. 2020 | Table 1 |
| MixHop | 76.2600 | 1.3300 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE+JK | 76.0500 | 1.3700 | Yes | Zhu et al. 2020 | Table 1 |
| Cheby+JK | 74.9800 | 1.1800 | Yes | Zhu et al. 2020 | Table 1 |
| GCN+JK | 74.5100 | 1.7500 | Yes | Zhu et al. 2020 | Table 1 |
| GAT | 75.4600 | 1.7200 | Yes | Zhu et al. 2020 | Table 1 |
| GEOM-GCN* | 77.9900 | — | Yes | Zhu et al. 2020 | Table 1 |
| MLP | 72.4100 | 2.1800 | Yes | Zhu et al. 2020 | Table 1 |
| GCN | 72.7100 | 1.5400 | Yes | Zhu et al. 2020 | Table 1 |
| AMP_GCN | 75.0700 | 1.2900 | Yes | Zhu et al. 2020 | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 86.9200 | 1.3700 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 87.8100 | 1.3500 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 86.9000 | 1.0400 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 86.7600 | 0.9500 | Yes | Defferrard et al. 2016 | Table 1 |
| MixHop | 87.6100 | 0.8500 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 85.9600 | 0.8300 | Yes | Huang et al. 2020 | Table 1 |
| Cheby+JK | 85.4900 | 1.2700 | Yes | Huang et al. 2020 | Table 1 |
| GCN+JK | 85.7900 | 0.9200 | Yes | Huang et al. 2020 | Table 1 |
| GAT | 82.6800 | 1.8000 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 85.2700 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 74.7500 | 2.2200 | Yes | Standard baseline | Table 1 |
| GCN | 84.2400 | 1.4400 | Yes | Kipf & Welling 2017 | Table 1 |
| AMP_GCN | 85.6800 | 1.5200 | Yes | Zhu et al. 2020 | Table 1 |

### Diameter — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6146 | 0.0375 | Yes | this paper | Table 1 |
| GAT | 1.4367 | 0.3558 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6146 | 0.0744 | Yes | this paper | Table 1 |
| GIN | 0.2408 | 0.0154 | Yes | this paper | Table 1 |
| GCNII | 0.5057 | 0.0309 | Yes | this paper | Table 1 |
| DGC | 0.5601 | 0.0220 | Yes | this paper | Table 1 |
| GRAND | 0.9477 | 0.2160 | Yes | this paper | Table 1 |
| ADGN | -0.4530 | 0.0883 | Yes | this paper | Table 1 |
| AMP_GCN | -0.1072 | 0.0791 | No | this paper | Table 1 |
| AMP_GIN | -0.4874 | 0.1111 | No | this paper | Table 1 |
| AMP_ADGN | -0.5891 | 0.0720 | No | this paper | Table 1 |

### Eccentricity — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7398 | 0.0705 | Yes | this paper | Table 1 |
| GAT | 1.0714 | 0.0616 | Yes | this paper | Table 1 |
| GraphSAGE | 1.0859 | 0.0001 | Yes | this paper | Table 1 |
| GIN | 0.9229 | 0.0002 | Yes | this paper | Table 1 |
| GCNII | 0.7112 | 0.0255 | Yes | this paper | Table 1 |
| DGC | 0.8051 | 0.0017 | Yes | this paper | Table 1 |
| GRAND | 0.7450 | 0.1369 | Yes | this paper | Table 1 |
| ADGN | 0.0547 | 0.0732 | Yes | this paper | Table 1 |
| AMP_GCN | 0.6054 | 0.0919 | No | this paper | Table 1 |
| AMP_GIN | 0.4093 | 0.0546 | No | this paper | Table 1 |
| AMP_ADGN | 0.0515 | 0.1819 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| GatedGCN | 0.6069 | 0.0035 | Yes | this paper | Table 1 |
| Transformer | 0.6326 | 0.0126 | Yes | this paper | Table 1 |
| SAN | 0.6439 | 0.0075 | Yes | this paper | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table 1 |
| CRaWl | 0.7074 | 0.0032 | Yes | this paper | Table 1 |
| DRew | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| Graph ViT | 0.6942 | 0.0075 | Yes | this paper | Table 1 |
| G-MLPMixer | 0.6921 | 0.0054 | Yes | this paper | Table 1 |
| LASER | 0.6440 | 0.0010 | Yes | this paper | Table 1 |
| CO-GNN | 0.6990 | 0.0093 | Yes | this paper | Table 1 |
| NBA | 0.7207 | 0.0028 | Yes | this paper | Table 1 |
| PH-DGN | 0.7012 | 0.0045 | Yes | this paper | Table 1 |
| GRED | 0.7041 | 0.0049 | Yes | this paper | Table 1 |
| PR-MPNN | 0.6825 | 0.0086 | Yes | this paper | Table 1 |
| IPR-MPNN | 0.7210 | 0.0039 | Yes | this paper | Table 1 |
| AMP | 0.7161 | 0.0047 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 2 |
| GINE | 0.3547 | 0.0045 | Yes | this paper | Table 2 |
| GatedGCN | 0.3357 | 0.0006 | Yes | this paper | Table 2 |
| Transformer | 0.2529 | 0.0016 | Yes | this paper | Table 2 |
| SAN | 0.2545 | 0.0012 | Yes | this paper | Table 2 |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table 2 |
| CRaWl | 0.2506 | 0.0022 | Yes | this paper | Table 2 |
| DRew | 0.2536 | 0.0015 | Yes | this paper | Table 2 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 2 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 2 |
| Graph ViT | 0.2449 | 0.0016 | Yes | this paper | Table 2 |
| G-MLPMixer | 0.2475 | 0.0015 | Yes | this paper | Table 2 |
| LASER | 0.3043 | 0.0019 | Yes | this paper | Table 2 |
| NBA | 0.2472 | 0.0008 | Yes | this paper | Table 2 |
| PH-DGN | 0.2465 | 0.0020 | Yes | this paper | Table 2 |
| GRED | 0.2584 | 0.0015 | Yes | this paper | Table 2 |
| PR-MPNN | 0.2477 | 0.0005 | Yes | this paper | Table 2 |
| IPR-MPNN | 0.2422 | 0.0007 | Yes | this paper | Table 2 |
| AMP | 0.2446 | 0.0026 | No | this paper | Table 2 |

### Pubmed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 89.4000 | 0.3400 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 89.5900 | 0.3300 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 88.4500 | 0.5000 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 88.7200 | 0.5500 | Yes | Zhu et al. 2020 | Table 1 |
| MixHop | 85.3100 | 0.6100 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 88.3400 | 0.6200 | Yes | Zhu et al. 2020 | Table 1 |
| Cheby+JK | 89.0700 | 0.3000 | Yes | Zhu et al. 2020 | Table 1 |
| GCN+JK | 88.4100 | 0.4500 | Yes | Zhu et al. 2020 | Table 1 |
| GAT | 84.6800 | 0.4400 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 90.0500 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 86.6500 | 0.3500 | Yes | Zhu et al. 2020 | Table 1 |
| GCN | 87.6200 | 0.5900 | Yes | Kipf & Welling 2017 | Table 1 |
| AMP_GCN | 89.6700 | 1.2900 | No | this paper | Table 1 |

### SSSP — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9132 | 0.0051 | Yes | this paper | Table 1 |
| GAT | 0.6070 | 0.0375 | Yes | this paper | Table 1 |
| GraphSAGE | -1.0139 | 0.0120 | Yes | this paper | Table 1 |
| GIN | -0.2648 | 0.4437 | Yes | this paper | Table 1 |
| GCNII | -0.9172 | 0.4396 | Yes | this paper | Table 1 |
| DGC | -0.0254 | 0.0077 | Yes | this paper | Table 1 |
| GRAND | 0.1909 | 0.3103 | Yes | this paper | Table 1 |
| ADGN | -3.5448 | 0.2749 | Yes | this paper | Table 1 |
| AMP_GCN | 0.5440 | 0.0108 | No | this paper | Table 1 |
| AMP_GIN | -3.0628 | 0.3159 | No | this paper | Table 1 |
| AMP_ADGN | -3.9579 | 0.0769 | No | this paper | Table 1 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 36.4200 | 1.8900 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 37.9000 | 2.0200 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 41.6100 | 0.7400 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 43.8600 | 1.6400 | Yes | Zhu et al. 2020 | Table 1 |
| MixHop | 43.8000 | 1.4800 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 40.8500 | 1.2900 | Yes | Zhu et al. 2020 | Table 1 |
| Cheby+JK | 45.0300 | 1.7300 | Yes | Zhu et al. 2020 | Table 1 |
| GCN+JK | 40.4500 | 1.6100 | Yes | Zhu et al. 2020 | Table 1 |
| GAT | 30.6200 | 2.1100 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 38.1400 | — | Yes | Zhu et al. 2020 | Table 1 |
| MLP | 29.6800 | 1.8100 | Yes | this paper | Table 1 |
| GCN | 27.7300 | 0.9100 | Yes | Kipf & Welling 2017 | Table 1 |
| AMP_GCN | 35.2800 | 0.9500 | Yes | Zhu et al. 2020 | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 84.8600 | 6.7700 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 82.1600 | 5.2800 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 82.4300 | 6.1400 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 77.3000 | 4.0700 | Yes | Defferrard et al. 2016 | Table 1 |
| MixHop | 77.8400 | 7.7300 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 83.7800 | 2.2100 | Yes | Huang et al. 2020 | Table 1 |
| Cheby+JK | 78.3800 | 6.3700 | Yes | Huang et al. 2020 | Table 1 |
| GCN+JK | 66.4900 | 6.6400 | Yes | Huang et al. 2020 | Table 1 |
| GAT | 58.3800 | 4.4500 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 67.5700 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 81.8900 | 4.7800 | Yes | Baseline | Table 1 |
| GCN | 52.7300 | 5.9800 | Yes | Kipf & Welling 2017 | Table 1 |
| AMP_GCN | 81.4600 | 3.0600 | No | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| H2GCN-1 | 86.6700 | 4.6900 | Yes | Zhu et al. 2020 | Table 1 |
| H2GCN-2 | 85.8800 | 4.2200 | Yes | Zhu et al. 2020 | Table 1 |
| GraphSAGE | 81.1800 | 5.5600 | Yes | Hamilton et al. 2017 | Table 1 |
| GCN-Cheby | 79.4100 | 4.4600 | Yes | Zhu et al. 2020 | Table 1 |
| MixHop | 75.8800 | 4.9000 | Yes | Abbasnejad et al. 2019 | Table 1 |
| GraphSAGE+JK | 81.9600 | 4.9600 | Yes | Zhu et al. 2020 | Table 1 |
| Cheby+JK | 82.5500 | 4.5700 | Yes | Zhu et al. 2020 | Table 1 |
| GCN+JK | 74.3100 | 6.4300 | Yes | Zhu et al. 2020 | Table 1 |
| GAT | 55.2900 | 8.7100 | Yes | Veličković et al. 2018 | Table 1 |
| GEOM-GCN* | 64.1200 | — | Yes | Pei et al. 2020 | Table 1 |
| MLP | 85.2900 | 3.6100 | Yes | Baseline | Table 1 |
| GCN | 44.9000 | 7.3800 | Yes | Kipf & Welling 2017 | Table 1 |
| AMP_GCN | 80.4500 | 4.4700 | Yes | Zhu et al. 2020 | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GraphSAGE** (from: Hamilton et al. 2017)
- **GIN** (from: Xu et al. 2019)
- **GCNII** (from: Chen et al. 2020)
- **DGC** (from: Zhang et al. 2018)
- **GRAND** (from: Eraslan et al. 2020)
- **ADGN** (from: Gravina et al. 2023)
- **GINE** (from: LRGB / Re-Eval)
- **GatedGCN** (from: LRGB / Re-Eval)
- **Transformer** (from: LRGB)
- **SAN** (from: LRGB)
- **GPS** (from: LRGB / Re-Eval)
- **CRaWl** (from: Others)
- **DRew** (from: Others)
- **Exphormer** (from: Others)
- **GRIT** (from: Others)
- **Graph ViT** (from: Others)
- **G-MLPMixer** (from: Others)
- **LASER** (from: Others)
- **CO-GNN** (from: Others)
- **NBA** (from: Others)
- **PH-DGN** (from: Others)
- **GRED** (from: Others)
- **PR-MPNN** (from: Others)
- **IPR-MPNN** (from: Others)
- **H2GCN-1** (from: Zhu et al. 2020)
- **H2GCN-2** (from: Zhu et al. 2020)
- **GCN-Cheby** (from: Defferrard et al. 2016)
- **MixHop** (from: Abbasnejad et al. 2019)
- **GraphSAGE+JK** (from: Huang et al. 2020)
- **Cheby+JK** (from: Huang et al. 2020)
- **GCN+JK** (from: Huang et al. 2020)
- **GEOM-GCN*** (from: Pei et al. 2020)
- **MLP** (from: Baseline)
- **AMP_GCN** (from: Zhu et al. 2020)
- **H2GCN** (from: Zhu et al. 2020)
- **AMP** (from: Zhu et al. 2020)

## Extraction Notes

[Diameter] The table reports log10(MSE). The values extracted are the log10(MSE) values as presented
in the table cells. The metric name is normalized to MSE as per instructions, but the values are
logarithmic. The table caption explicitly states 'mean log10(mse)'. Since the prompt asks for MSE
and the table provides log10(MSE), I have extracted the log10(MSE) values directly. Note: Lower
log10(MSE) indicates better performance (lower MSE). The values are negative for good performance
(MSE < 1). The 'higher_is_better' is set to false because lower MSE is better, and lower log10(MSE)
corresponds to lower MSE. [SSSP] The table reports mean log10(MSE). The values extracted are the
log10(MSE) values as reported in the table. The metric name is normalized to MSE as per
instructions, but the values are logarithmic. The table caption explicitly states 'mean log10(mse)'.
Since the prompt asks for the metric 'MSE' and the table provides log10(MSE), I have extracted the
log10(MSE) values directly. Note: Lower log10(MSE) indicates better performance (lower MSE). The
'higher_is_better' flag is set to false because for MSE (and log10(MSE)), lower is better.
[Eccentricity] The table reports log10(MSE). The values extracted are the log10(MSE) values as
presented in the table cells. The metric name is normalized to MSE as per instructions, but the
values represent log10(MSE). Higher is better is false because lower MSE (and thus lower log10(MSE))
is better. The proposed model variants are AMP_GCN, AMP_GIN, and AMP_ADGN. [Peptides-func] Extracted
all rows from Table 1 for the 'peptides-func' dataset column. The table lists multiple
configurations for the proposed model AMP (AMP_GCN, AMP_GINE, AMP_GatedGCN) and baselines (e.g.,
DRew_GCN, DRew_GatedGCN, NBA_GCN, NBA_GatedGCN). All these are treated as distinct model entries in
the results list. The metric is AP (Average Precision), higher is better. Standard deviations are
included where available. [Peptides-struct] Extracted all rows from Table 2 for the 'peptides-
struct' column. The table lists results from three categories: 'LRGB' (original evaluations), 'Re-
Eval' (re-evaluations by the authors), and 'Others' (other baselines). The proposed model AMP is
listed at the bottom with three variants (GCN, GINE, GatedGCN). All values are Test MAE. CO-GNN has
no value for Peptides-struct and was skipped. Metric direction is lower-is-better (MAE). [Texas]
Extracted only the 'Texas' column from Table 1. The table caption indicates results are taken from
Zhu et al. 2020, but the AMP model is presented in the current paper's table as a comparison.
AMP_GCN is treated as the proposed model based on the context of the table structure (bottom row,
distinct from standard baselines). All other models are baselines. Standard deviations are parsed
from the LaTeX scriptstyle notation. [Wisconsin] Extracted only Wisconsin column results. The table
caption indicates results are taken from Zhu et al. 2020, so no proposed model is identified in this
specific table context. All values are Accuracy. Standard deviations are parsed from the LaTeX
script style formatting. [Actor] Extracted all rows for the 'Actor' dataset from Table 1. The table
caption indicates results are taken from Zhu et al. 2020. No proposed model is explicitly identified
in this specific table context, so all models are treated as baselines. Standard configuration
results were used. No standard deviation was reported for GEOM-GCN*. [Squirrel] Extracted only the
'Squirrel' column from Table 1. All values are Accuracy. Standard deviations are parsed from the
LaTeX scriptstyle notation. GEOM-GCN* has no reported standard deviation in the table. [Chameleon]
Extracted only the Chameleon column from Table 1. The table caption indicates results are taken from
Zhu et al. 2020. No proposed model is explicitly identified in this specific table context, so all
models are treated as baselines. Standard configuration used as no variants were specified for
Chameleon in this table. [Citeseer] Extracted only Citeseer results from Table 1. The table caption
indicates results are taken from Zhu et al. 2020. No proposed model is explicitly identified in this
specific table context, so all models are treated as baselines. Standard deviation is parsed from
the LaTeX scriptstyle notation. GEOM-GCN* has no reported standard deviation in the table. [Pubmed]
Extracted only the Pubmed column from Table 1. The table caption indicates results are taken from
Zhu et al. 2020, but AMP is presented as the proposed method in the current context (likely AMP
paper citing Zhu et al. for baselines or comparing against them). AMP_GCN is treated as the proposed
model based on the table structure where it is listed last and bolded in other columns (though not
explicitly bolded here, it is the novel entry). All other models are baselines. Standard
configuration used. [Cora] Extracted only Cora results from Table 1. The table caption indicates
results are taken from Zhu et al. 2020. No proposed model is explicitly identified in this specific
table context as it serves as a comparison table for existing methods on heterophilic/homophilic
graphs. All values parsed from the 'Cora' column.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*