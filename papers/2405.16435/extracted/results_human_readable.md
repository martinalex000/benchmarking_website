# Extraction: Node Identifiers: Compact, Discrete Representations for Efficient Graph Learning
**Model used**: `glm-4.7`  **Date**: 2026-05-11  **Confidence**: LOW

## Proposed Model: NID
- Type: Other

## Main Figure: Figure 3
> Overview of our proposed NID framework.
- Figure 3 provides the architectural overview of the proposed NID framework, illustrating the generation of Node IDs via vector quantization, which is the core methodological contribution of the paper.

## Results

### Amazon-Computers — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 58.2000 | — | No | this paper | Table 6 |

### Amazon-Photo — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 75.6000 | — | No | this paper | Table 6 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 54.8000 | 0.7000 | Yes | this paper | Table 13 |
| ContextPred | 59.1000 | 0.2000 | Yes | this paper | Table 13 |
| AttrMask | 61.0000 | 1.3000 | Yes | this paper | Table 13 |
| JOAO | 63.7000 | 0.3000 | Yes | this paper | Table 13 |
| SimGRACE | 65.4000 | 1.2000 | Yes | this paper | Table 13 |
| GraphCL | 62.4000 | 0.7000 | Yes | this paper | Table 13 |
| NID_CL | 66.9000 | 0.6000 | No | this paper | Table 13 |

### Bace — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 68.8000 | 0.9000 | Yes | this paper | Table 13 |
| ContextPred | 64.4000 | 0.6000 | Yes | this paper | Table 13 |
| AttrMask | 64.4000 | 2.5000 | Yes | this paper | Table 13 |
| JOAO | 71.2000 | 1.0000 | Yes | this paper | Table 13 |
| SimGRACE | 67.8000 | 1.3000 | Yes | this paper | Table 13 |
| GraphCL | 71.1000 | 0.7000 | Yes | this paper | Table 13 |
| NID_CL | 66.1000 | 1.2000 | No | this paper | Table 13 |

### COLLAB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 70.6000 | 1.1000 | Yes | this paper | Table 7 |
| JOAO | 69.3000 | 0.3000 | Yes | this paper | Table 7 |
| GraphMAE | 80.3000 | 0.5000 | Yes | this paper | Table 7 |
| AD-GCL | 73.3000 | 0.6000 | Yes | this paper | Table 7 |
| GraphCL | 71.3000 | 1.1000 | Yes | this paper | Table 7 |
| NID_CL | 76.9000 | 0.3000 | No | this paper | Table 7 |
| AutoGCL | 70.1000 | 0.6000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 74.5000 | 1.1000 | No | this paper | Table 7 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 73.9000 | — | No | this paper | Table 6 |
| GAE | 65.8000 | 0.4000 | Yes | this paper | Table 6 |
| DGI | 71.8000 | 0.7000 | Yes | this paper | Table 6 |
| MVGRL | 73.3000 | 0.5000 | Yes | this paper | Table 6 |
| InfoGCL | 73.5000 | 0.4000 | Yes | this paper | Table 6 |
| CCA-SSG | 73.1000 | 0.3000 | Yes | this paper | Table 6 |
| MLP | 54.7000 | — | Yes | this paper | Table 6 |
| VQGraph | 0.8000 | — | No | this paper | Table 8 |
| NID_GCN | 97.9000 | — | Yes | this paper | Table 8 |
| NID_GCN(M=1) | 81.3000 | — | Yes | this paper | Table 8 |
| Random | 4.8300 | — | Yes | this paper | Table 4.2 |
| VQGraph | 4.7300 | — | Yes | this paper | Table 4.2 |
| NID_GCN | 3.8900 | — | No | this paper | Table 4.2 |
| VQGraph tokens | 32.0700 | 2.7000 | Yes | Yang et al., 2024 | Table 15 |
| NID_GCN | 76.8900 | 1.0900 | No | this paper | Table 15 |
| VQGraph | 78.4000 | 1.7100 | No | this paper | Table 16 |
| VQGraph without reconstruction loss | 78.0300 | 1.5800 | Yes | this paper | Table 16 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NID_GCN (End-to-End Learning) | 76.8900 | 1.0900 | No | this paper | Table 17 |
| NID_GCN (Post-hoc RVQ) | 75.4700 | 1.3100 | Yes | this paper | Table 17 |

### ClinTox — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 48.9000 | 6.5000 | Yes | this paper | Table 13 |
| ContextPred | 43.2000 | 1.7000 | Yes | this paper | Table 13 |
| AttrMask | 51.6000 | 0.7000 | Yes | this paper | Table 13 |
| JOAO | 54.1000 | 2.6000 | Yes | this paper | Table 13 |
| SimGRACE | 63.4000 | 2.6000 | Yes | this paper | Table 13 |
| GraphCL | 59.8000 | 1.2000 | Yes | this paper | Table 13 |
| NID_CL | 65.3000 | 2.2000 | No | this paper | Table 13 |

### Coauthor-CS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 75.4000 | — | No | this paper | Table 6 |

### Coauthor-Physics — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 69.8000 | — | No | this paper | Table 6 |

### Computer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 93.7800 | — | Yes | this paper | Table 4.2 |
| SAGE | 93.5900 | — | Yes | this paper | Table 4.2 |
| VQGraph | 90.2800 | — | Yes | this paper | Table 4.2 |
| NID_SAGE | 93.3200 | — | No | this paper | Table 4.2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NID_SAGE | 76.7800 | 0.5900 | No | this paper | Table 2 |
| SAGE | 70.5200 | 0.1400 | Yes | this paper | Table 2 |
| GCN | 81.8300 | 0.2600 | Yes | this paper | Table 2 |
| NID_GCN | 85.6300 | 0.3100 | No | this paper | Table 2 |
| DGCluster | 70.5000 | — | No | this paper | Table 6 |
| GAE | 71.5000 | 0.4000 | Yes | this paper | Table 6 |
| DGI | 82.3000 | 0.6000 | Yes | this paper | Table 6 |
| MVGRL | 83.5000 | 0.4000 | Yes | this paper | Table 6 |
| InfoGCL | 83.5000 | 0.3000 | Yes | this paper | Table 6 |
| CCA-SSG | 84.0000 | 0.4000 | Yes | this paper | Table 6 |
| MLP | 57.8000 | 0.5000 | Yes | this paper | Table 6 |
| VQGraph | 1.3000 | — | No | this paper | Table 8 |
| NID_GCN | 84.7000 | — | Yes | this paper | Table 8 |
| NID_GCN(M=1) | 83.3000 | — | Yes | this paper | Table 8 |
| Random | 7.2100 | — | Yes | this paper | Table 4.2 |
| VQGraph | 6.8500 | — | Yes | this paper | Table 4.2 |
| NID_GCN | 6.1500 | — | No | this paper | Table 4.2 |
| VQGraph tokens | 63.3900 | 1.1500 | Yes | Yang et al., 2024 | Table 15 |
| VQGraph | 76.0800 | 0.5500 | No | this paper | Table 16 |
| VQGraph without reconstruction loss | 76.1700 | 0.4700 | Yes | this paper | Table 16 |
| NID_GCN (End-to-End Learning) | 87.8800 | 0.6900 | No | this paper | Table 17 |
| NID_GCN (Post-hoc RVQ) | 86.1700 | 0.3300 | Yes | this paper | Table 17 |

### DD — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 72.8000 | 1.7000 | Yes | this paper | Table 7 |
| JOAO | 77.4000 | 1.1000 | Yes | this paper | Table 7 |
| AD-GCL | 74.4000 | 0.5000 | Yes | this paper | Table 7 |
| GraphCL | 78.6000 | 0.4000 | Yes | this paper | Table 7 |
| NID_CL | 77.8000 | 1.1000 | No | this paper | Table 7 |
| AutoGCL | 77.5000 | 0.6000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 77.2000 | 0.9000 | No | this paper | Table 7 |

### HIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 64.9000 | 2.0000 | Yes | this paper | Table 13 |
| ContextPred | 68.9000 | 0.4000 | Yes | this paper | Table 13 |
| AttrMask | 60.9000 | 1.3000 | Yes | this paper | Table 13 |
| JOAO | 68.1000 | 0.9000 | Yes | this paper | Table 13 |
| SimGRACE | 66.3000 | 1.5000 | Yes | this paper | Table 13 |
| GraphCL | 63.7000 | 2.3000 | Yes | this paper | Table 13 |
| NID_CL | 64.3000 | 0.8000 | No | this paper | Table 13 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 73.0000 | 0.8000 | Yes | this paper | Table 7 |
| MVGRL | 74.2000 | 0.7000 | Yes | this paper | Table 7 |
| JOAO | 70.8000 | 0.2000 | Yes | this paper | Table 7 |
| GraphMAE | 75.5000 | 0.6000 | Yes | this paper | Table 7 |
| AD-GCL | 71.5000 | 1.0000 | Yes | this paper | Table 7 |
| GraphCL | 71.1000 | 0.4000 | Yes | this paper | Table 7 |
| NID_CL | 72.3000 | 1.2000 | No | this paper | Table 7 |
| AutoGCL | 73.3000 | 0.4000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 72.4000 | 0.8000 | No | this paper | Table 7 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 89.0000 | 1.1000 | Yes | this paper | Table 7 |
| MVGRL | 89.7000 | 1.1000 | Yes | this paper | Table 7 |
| JOAO | 87.6000 | 0.7000 | Yes | this paper | Table 7 |
| GraphMAE | 88.1000 | 1.3000 | Yes | this paper | Table 7 |
| GraphCL | 86.8000 | 1.3000 | Yes | this paper | Table 7 |
| NID_CL | 88.6000 | 1.7000 | No | this paper | Table 7 |
| AutoGCL | 88.6000 | 1.0000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 90.4000 | 0.8000 | No | this paper | Table 7 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 76.2000 | 1.0000 | Yes | this paper | Table 7 |
| JOAO | 78.3000 | 0.5000 | Yes | this paper | Table 7 |
| GraphMAE | 80.4000 | 0.3000 | Yes | this paper | Table 7 |
| AD-GCL | 69.6000 | 0.5000 | Yes | this paper | Table 7 |
| GraphCL | 77.8000 | 0.4000 | Yes | this paper | Table 7 |
| NID_CL | 75.9000 | 0.6000 | No | this paper | Table 7 |
| AutoGCL | 82.0000 | 0.2000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 78.2000 | 1.5000 | No | this paper | Table 7 |

### NID — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 63.3000 | — | No | this paper | Table 6 |

### PPI — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 32.4000 | — | No | this paper | Table 6 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 74.4000 | 0.3000 | Yes | this paper | Table 7 |
| JOAO | 74.0000 | 1.1000 | Yes | this paper | Table 7 |
| GraphMAE | 75.3000 | 0.4000 | Yes | this paper | Table 7 |
| AD-GCL | 73.5000 | 0.6000 | Yes | this paper | Table 7 |
| GraphCL | 74.3000 | 0.4000 | Yes | this paper | Table 7 |
| NID_CL | 75.1000 | 0.5000 | No | this paper | Table 7 |
| AutoGCL | 75.8000 | 0.3000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 75.9000 | 0.6000 | No | this paper | Table 7 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.6326 | 0.0126 | Yes | this paper | Table 3 |
| GraphGPS | 0.6535 | 0.0041 | Yes | this paper | Table 3 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 3 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 3 |
| Graph ViT | 0.6970 | 0.0080 | Yes | this paper | Table 3 |
| GCN | 0.6762 | 0.0053 | Yes | this paper | Table 3 |
| NID_GCN | 0.6608 | 0.0058 | No | this paper | Table 3 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2529 | 0.0016 | Yes | this paper | Table 3 |
| GraphGPS | 0.2500 | 0.0012 | Yes | this paper | Table 3 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 3 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 3 |
| Graph ViT | 0.2449 | 0.0016 | Yes | this paper | Table 3 |
| GCN | 0.2512 | 0.0007 | Yes | this paper | Table 3 |
| NID_GCN | 0.2589 | 0.0014 | No | this paper | Table 3 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 54.1000 | — | No | this paper | Table 6 |
| GAE | 72.1000 | 0.5000 | Yes | this paper | Table 6 |
| DGI | 76.8000 | 0.6000 | Yes | this paper | Table 6 |
| MVGRL | 80.1000 | 0.7000 | Yes | this paper | Table 6 |
| InfoGCL | 79.1000 | 0.2000 | Yes | this paper | Table 6 |
| CCA-SSG | 81.0000 | 0.4000 | Yes | this paper | Table 6 |
| VQGraph | 18.1000 | — | No | this paper | Table 8 |
| NID_GCN | 79.1000 | — | Yes | this paper | Table 8 |
| NID_GCN(M=1) | 78.1000 | — | Yes | this paper | Table 8 |
| Random | 9.6100 | — | Yes | this paper | Table 4.2 |
| VQGraph | 9.0300 | — | Yes | this paper | Table 4.2 |
| NID_GCN | 6.2200 | — | No | this paper | Table 4.2 |
| VQGraph tokens | 54.3700 | 4.7600 | Yes | Yang et al., 2024 | Table 15 |
| NID_GCN | 89.4200 | 0.4400 | No | this paper | Table 15 |
| VQGraph | 83.9300 | 0.8700 | No | this paper | Table 16 |
| VQGraph without reconstruction loss | 83.8500 | 1.2400 | Yes | this paper | Table 16 |
| NID_GCN (End-to-End Learning) | 89.4200 | 0.4400 | No | this paper | Table 17 |
| NID_GCN (Post-hoc RVQ) | 88.3200 | 0.5400 | Yes | this paper | Table 17 |

### RDT-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 82.5000 | 1.4000 | Yes | this paper | Table 7 |
| MVGRL | 84.5000 | 0.6000 | Yes | this paper | Table 7 |
| JOAO | 86.4000 | 1.4000 | Yes | this paper | Table 7 |
| GraphMAE | 88.0000 | 0.2000 | Yes | this paper | Table 7 |
| AD-GCL | 85.5000 | 0.7000 | Yes | this paper | Table 7 |
| GraphCL | 89.5000 | 0.8000 | Yes | this paper | Table 7 |
| NID_CL | 90.7000 | 0.9000 | No | this paper | Table 7 |
| AutoGCL | 88.5000 | 1.4000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 89.8000 | 0.7000 | No | this paper | Table 7 |

### RDT-M5K — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| InfoGraph | 53.4000 | 1.0000 | Yes | this paper | Table 7 |
| JOAO | 56.0000 | 0.2000 | Yes | this paper | Table 7 |
| AD-GCL | 53.0000 | 0.8000 | Yes | this paper | Table 7 |
| GraphCL | 55.9000 | 0.2000 | Yes | this paper | Table 7 |
| NID_CL | 55.0000 | 0.5000 | No | this paper | Table 7 |
| AutoGCL | 56.7000 | 0.1000 | Yes | this paper | Table 7 |
| NID_AutoGCL | 54.2000 | 0.6000 | No | this paper | Table 7 |

### Reddit — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 35.6000 | — | No | this paper | Table 6 |

### Sider — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 51.0000 | 0.3000 | Yes | this paper | Table 13 |
| ContextPred | 59.4000 | 0.3000 | Yes | this paper | Table 13 |
| AttrMask | 51.7000 | 0.1000 | Yes | this paper | Table 13 |
| JOAO | 57.4000 | 0.6000 | Yes | this paper | Table 13 |
| SimGRACE | 54.9000 | 0.6000 | Yes | this paper | Table 13 |
| GraphCL | 54.6000 | 0.3000 | Yes | this paper | Table 13 |
| NID_CL | 60.1000 | 0.4000 | No | this paper | Table 13 |

### Tox21 — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 62.7000 | 0.6000 | Yes | this paper | Table 13 |
| ContextPred | 68.4000 | 0.3000 | Yes | this paper | Table 13 |
| AttrMask | 69.1000 | 0.2000 | Yes | this paper | Table 13 |
| JOAO | 70.6000 | 0.4000 | Yes | this paper | Table 13 |
| SimGRACE | 64.6000 | 0.4000 | Yes | this paper | Table 13 |
| GraphCL | 64.4000 | 0.5000 | Yes | this paper | Table 13 |
| NID_CL | 66.3000 | 0.4000 | No | this paper | Table 13 |

### ToxCast — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| EdgePred | 55.3000 | 0.4000 | Yes | this paper | Table 13 |
| ContextPred | 59.1000 | 0.2000 | Yes | this paper | Table 13 |
| AttrMask | 58.2000 | 0.2000 | Yes | this paper | Table 13 |
| JOAO | 60.5000 | 0.3000 | Yes | this paper | Table 13 |
| SimGRACE | 59.1000 | 0.2000 | Yes | this paper | Table 13 |
| GraphCL | 59.4000 | 0.2000 | Yes | this paper | Table 13 |
| NID_CL | 59.1000 | 0.3000 | No | this paper | Table 13 |

### WikiCS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 65.4000 | — | No | this paper | Table 6 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 40.6000 | — | No | this paper | Table 6 |
| VQGraph tokens | 43.5700 | 0.4900 | Yes | Yang et al., 2024 | Table 15 |
| NID_GCN | 71.2700 | 0.2400 | No | this paper | Table 15 |

### ogbn-papers100M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 62.1000 | — | No | this paper | Table 6 |

### ogbn-products — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCluster | 50.9000 | — | No | this paper | Table 6 |
| GCN | 82.3300 | — | Yes | this paper | Table 4.2 |
| SAGE | 83.2700 | — | Yes | this paper | Table 4.2 |
| VQGraph | 79.1700 | — | Yes | this paper | Table 4.2 |
| NID_SAGE | 81.8300 | — | No | this paper | Table 4.2 |
| VQGraph without reconstruction loss | 79.2300 | 0.2600 | Yes | this paper | Table 16 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018a)
- **SAGE** (from: Hamilton et al. 2017)
- **GIN** (from: Xu et al. 2018)
- **GraphMAE** (from: Hou et al. 2022)
- **GraphCL** (from: You et al. 2020)
- **DeepWalk** (from: Perozzi et al. 2014)
- **node2vec** (from: Grover & Leskovec 2016)
- **GT**
- **GraphGPS**
- **GRIT**
- **Exphormer**
- **Graph ViT**
- **GAE**
- **DGI**
- **MVGRL**
- **InfoGCL**
- **CCA-SSG**
- **MLP**
- **InfoGraph** (from: Xu et al., 2020)
- **JOAO** (from: Jin et al., 2021)
- **AD-GCL** (from: Chen et al., 2022)
- **AutoGCL** (from: Yin et al., 2022)
- **NID_GCN**
- **NID_GCN(M=1)**
- **VQGraph** (from: Yang et al. 2024)
- **Random**
- **SBM** (from: Peixoto 2014)
- **AGC** (from: Zhang et al. 2019)
- **SDCN** (from: Bo et al. 2020)
- **DAEGC** (from: Wang et al. 2019a)
- **NOCD** (from: Shchur & Günnemann 2019)
- **DiffPool** (from: Ying et al. 2018)
- **MinCut** (from: Bianchi et al. 2020)
- **Ortho** (from: Bianchi et al. 2020)
- **DMoN** (from: Tsitsulin et al. 2023)
- **DGCluster** (from: Bhowmick et al. 2024)
- **APPNP** (from: Gasteiger et al. 2018)
- **GPRGNN** (from: Chien et al. 2020)
- **LINKX** (from: Lim et al. 2021)
- **Polynormer** (from: Deng et al. 2024)
- **SGFormer** (from: Wu et al. 2023)
- **SEAL** (from: Zhang & Chen 2018)
- **NBFnet** (from: Zhu et al. 2021)
- **Neo-GNN** (from: Yun et al. 2021)
- **BUDDY** (from: Chamberlain et al. 2022)
- **NCN** (from: Wang et al. 2023c)
- **Tönshoff et al.** (from: Tönshoff et al., 2023)
- **EdgePred**
- **ContextPred**
- **AttrMask**
- **SimGRACE**
- **VQGraph without reconstruction loss**
- **NID_GCN (Post-hoc RVQ)**

## Extraction Notes

[Section 1] The provided text contains the introduction, preliminaries, methodology, and the
beginning of the evaluation section. However, it cuts off before presenting the actual experimental
results tables (e.g., Table 1, Table 2) or specific numerical values for the datasets mentioned
(Cora, PubMed, etc.). The text mentions 'Extensive experiments on 34 datasets' and lists dataset
names in the abstract and appendix sections, but the quantitative results (accuracy, MAE, etc.) are
not present in the provided snippet. Therefore, no results could be extracted. [Section 2] failed:
Request timed out. [Section 3] failed: 2 validation errors for ExtractionOutput results.14.value
Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For
further information visit https://errors.pydantic.dev/2.13/v/float_type results.20.value   Input
should be a valid number [type=float_type, input_value=None, input_type=NoneType]     For further
information visit https://errors.pydantic.dev/2.13/v/float_type [Section 4] The input text contains
LaTeX artifacts and fragmented table structures. Table 2 (node-level results on Cora) was
reconstructed from scattered text fragments. Table 3 (graph-level on LRGB) was clearer. Parameter
counts were not found in the provided text. The 'Infer. Time' and 'Storage Space' columns were
present but not extracted as they are not standard performance metrics for the schema. [Section 5]
failed: 1 validation error for ExtractionOutput results.22.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Section 6] failed: JSON parse error from 'glm-4.7':
Unterminated string starting at: line 1143 column 7 (char 26748) [Section 7] The input text contains
a fragmented table structure. The first block of numbers (70.5, 73.9, etc.) appears to be results
for the proposed model 'DGCluster' across various datasets, but the dataset names were not
explicitly aligned with the values in the provided text snippet. I inferred the dataset names based
on standard benchmarks (Cora, CiteSeer, PubMed, NID, ogbn-arxiv, ogbn-products, ogbn-papers100M,
Amazon-Computers, Amazon-Photo, Coauthor-CS, Coauthor-Physics, WikiCS, PPI, Reddit) commonly used in
such papers and the count of values. The second block is a clearer table for baselines (GAE, DGI,
MVGRL, InfoGCL, CCA-SSG, MLP) on Cora, CiteSeer, and PubMed. The 'Clustering Time' values were
ignored as they are not classification accuracy metrics. The 'dim' column was ignored as it is a
hyperparameter, not a result. [Section 8] Table 7 was parsed successfully. Some baseline models
(MVGRL, GraphMAE) had missing values for certain datasets, represented as '-' in the source text;
these were omitted. The proposed model has variants NID_CL and NID_AutoGCL, both marked as proposed.
Dataset names RDT-B and RDT-M5K are kept as in the table, likely referring to REDDIT-B and
REDDIT-M5K. [Section 9] The provided text contains only partial data from Table 8 (Codebook usage
rates) and a header for Table 9 (Average GEDs) without values. No standard benchmark results
(Accuracy, MAE, etc.) were present in the snippet. Model parameters were not found. [Section 10] The
text contains LaTeX artifacts and fragmented table structures. Table 4.2 is referenced multiple
times for different metrics (GED, Accuracy, Time). The values for Accuracy and Time were extracted
from the 'Accuracy vs Inference Time' section which appears to correspond to Table 4.2. The GED
values were extracted from the 'Subgraph Retrieval' section. Inference time values were excluded as
they are not standard performance metrics for benchmark comparison. The model names 'NID_GCN' and
'NID_SAGE' were inferred from the text 'NID_{GCN}' and 'NID_{SAGE}'. [Section 11] The provided text
contains descriptions of datasets, baselines, and experimental setup, but does not contain the
actual result tables (e.g., Table 1, Table 2) with quantitative performance metrics (Accuracy, MAE,
etc.). The text lists the datasets and metrics used, but no numerical results for the proposed model
or baselines are present in this excerpt. [Section 12] The provided text contains detailed
hyperparameter settings (Table 12) and experimental setup descriptions for various tasks (Attributed
Graph Clustering, Unsupervised/Supervised Node Classification, Link Prediction, Graph
Classification) and datasets (Cora, Citeseer, Pubmed, OGB, ZINC, MoleculeNet). However, the text
does not contain the actual quantitative performance results (e.g., Accuracy, ROC-AUC scores) for
these experiments. It mentions that results are presented in Table 13 for linear probing, but Table
13 itself is not included in the provided text. Therefore, no quantitative results could be
extracted. [Section 13] Table 13 was fully parsed. The text mentions Table 14 and VQGraph
comparisons, but the actual data rows for Table 14 were not present in the provided text snippet, so
no results were extracted from it. The proposed model name in the table is formatted as 'NID_CL'
(subscript CL), which has been normalized to 'NID_CL' for the JSON key. [Section 14] The provided
text snippet contains Table 14 which compares codebook sizes (Cora, CiteSeer, PubMed, Computer) for
VQGraph and NID_GCN, but does not contain quantitative performance metrics (e.g., Accuracy, F1) or
values associated with these datasets. Table 15 is referenced but not provided. Therefore, no
performance results could be extracted. [Section 15] The input text contains LaTeX artifacts and
formatting noise (e.g., 'start_POSTSUBSCRIPT', 'italic_K'). Table 15 was partially reconstructed
from the text. The baseline 'VQGraph tokens' appears to be a specific configuration of VQGraph.
Parameter counts were not found in the provided text. The text mentions Table 16 for ablation, but
the data for Table 16 was not provided in the input. [Section 16] Only Table 16 was provided in the
text snippet. The metric is assumed to be Accuracy (%) based on the dataset types (Cora, CiteSeer,
PubMed, ogbn-products) and the magnitude of the values, though the table header did not explicitly
state the metric name. [Section 17] The provided text contains only Table 17. The text mentions
Table 3 and 4 for Peptides-func and inductive inference, but the actual data for those tables is not
included in the input text. Only results from Table 17 were extracted. The metric is assumed to be
Accuracy based on the dataset types (Cora, Citeseer, PubMed) and the magnitude of the values.
[Section 18] failed: JSON parse error from 'glm-4.7': Expecting property name enclosed in double
quotes: line 1134 column 22 (char 27422)

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*