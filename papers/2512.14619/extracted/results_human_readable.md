# Extraction: ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: ParaFormer
- Type: GNN

## Results

### 20News — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LP | 55.9000 | — | Yes | this paper | Table 1 |
| ManiReg | 56.3000 | 1.2000 | Yes | this paper | Table 1 |
| GCN-kNN | 56.1000 | 0.6000 | Yes | this paper | Table 1 |
| GAT-kNN | 55.2000 | 0.8000 | Yes | this paper | Table 1 |
| DenseGAT | 54.6000 | 0.2000 | Yes | this paper | Table 1 |
| GLCN | 56.2000 | 0.8000 | Yes | this paper | Table 1 |
| DIFFomer-s | 57.7000 | 0.3000 | Yes | this paper | Table 1 |
| DIFFomer-a | 57.9000 | 0.7000 | Yes | this paper | Table 1 |
| ParaFormer | 59.5000 | 0.4000 | No | this paper | Table 1 |

### Amazon2M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 83.9000 | 0.1000 | Yes | this paper | Table 1 |
| SGC | 81.2100 | 0.1200 | Yes | this paper | Table 1 |
| GCN-Nsampler | 83.8400 | 0.4200 | Yes | this paper | Table 1 |
| GAT-NSampler | 85.1700 | 0.3200 | Yes | this paper | Table 1 |
| SIGN | 80.9800 | 0.3100 | Yes | this paper | Table 1 |
| NodeFormer | 87.8500 | 0.2400 | Yes | this paper | Table 1 |
| SGFormer | 89.0900 | 0.1000 | Yes | this paper | Table 1 |
| ParaFormer | 89.3600 | 0.1400 | No | this paper | Table 1 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 36.7000 | 4.7000 | Yes | this paper | Table 1 |
| GCN | 41.3000 | 3.0000 | Yes | this paper | Table 1 |
| GAT | 39.2000 | 3.1000 | Yes | this paper | Table 1 |
| SGC | 39.0000 | 3.3000 | Yes | this paper | Table 1 |
| JKNet | 39.4000 | 3.8000 | Yes | this paper | Table 1 |
| APPNP | 38.4000 | 3.5000 | Yes | this paper | Table 1 |
| GPRGNN | 39.9000 | 3.3000 | Yes | this paper | Table 1 |
| H2GCN | 38.1000 | 4.0000 | Yes | this paper | Table 1 |
| SIGN | 41.7000 | 2.2000 | Yes | this paper | Table 1 |
| CPGNN | 40.8000 | 2.0000 | Yes | this paper | Table 1 |
| GLoGNN | 40.2000 | 3.9000 | Yes | this paper | Table 1 |
| Graphormer | 41.3000 | 2.8000 | Yes | this paper | Table 1 |
| GraphTrans | 42.2000 | 2.9000 | Yes | this paper | Table 1 |
| NodeFormer | 34.7000 | 4.1000 | Yes | this paper | Table 1 |
| SGFormer | 44.9000 | 3.9000 | Yes | this paper | Table 1 |
| NAGphormer | 42.4000 | 5.7000 | Yes | this paper | Table 1 |
| CobFormer-G | 39.9000 | 2.4000 | Yes | this paper | Table 1 |
| CobFormer-T | 39.7000 | 4.6000 | Yes | this paper | Table 1 |
| Polynormer | 41.8000 | 3.5000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 45.9000 | 3.3000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 42.1000 | 4.5000 | No | this paper | Table 1 |
| ParaFormer (a) | 45.9000 | — | No | this paper | Table 2 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 74.0000 | 2.0000 | Yes | this paper | Table 1 |
| GCN | 76.5000 | 1.4000 | Yes | this paper | Table 1 |
| GAT | 76.6000 | 1.2000 | Yes | this paper | Table 1 |
| SGC | 76.2000 | 0.3000 | Yes | this paper | Table 1 |
| JKNet | 77.7000 | 0.4000 | Yes | this paper | Table 1 |
| APPNP | 79.3000 | 0.4000 | Yes | this paper | Table 1 |
| GPRGNN | 77.1000 | 1.8000 | Yes | this paper | Table 1 |
| H2GCN | 77.1000 | 1.6000 | Yes | this paper | Table 1 |
| SIGN | 76.6000 | 0.6000 | Yes | this paper | Table 1 |
| CPGNN | 75.5000 | 1.8000 | Yes | this paper | Table 1 |
| GLoGNN | 77.4000 | 1.7000 | Yes | this paper | Table 1 |
| Graphormer | 66.2000 | 0.8000 | Yes | this paper | Table 1 |
| GraphTrans | 72.1000 | 0.8000 | Yes | this paper | Table 1 |
| NodeFormer | 76.1000 | 0.2000 | Yes | this paper | Table 1 |
| SGFormer | 77.4000 | 0.8000 | Yes | this paper | Table 1 |
| NAGphormer | 80.1000 | 0.2000 | Yes | this paper | Table 1 |
| CobFormer-G | 76.4000 | 0.4000 | Yes | this paper | Table 1 |
| CobFormer-T | 76.5000 | 0.7000 | Yes | this paper | Table 1 |
| Polynormer | 77.4000 | 0.7000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 78.6000 | 0.1000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 80.5000 | 0.6000 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 75.7000 | 2.0000 | Yes | this paper | Table 1 |
| GCN | 87.1000 | 1.0000 | Yes | this paper | Table 1 |
| GAT | 88.0000 | 0.8000 | Yes | this paper | Table 1 |
| SGC | 86.6000 | 0.3000 | Yes | this paper | Table 1 |
| JKNet | 87.0000 | 0.3000 | Yes | this paper | Table 1 |
| APPNP | 88.0000 | 0.2000 | Yes | this paper | Table 1 |
| GPRGNN | 88.5000 | 1.0000 | Yes | this paper | Table 1 |
| H2GCN | 87.9000 | 1.2000 | Yes | this paper | Table 1 |
| SIGN | 86.5000 | 0.6000 | Yes | this paper | Table 1 |
| CPGNN | 87.2000 | 1.1000 | Yes | this paper | Table 1 |
| GLoGNN | 88.3000 | 1.1000 | Yes | this paper | Table 1 |
| Graphormer | 72.9000 | 0.8000 | Yes | this paper | Table 1 |
| GraphTrans | 86.7000 | 0.6000 | Yes | this paper | Table 1 |
| NodeFormer | 88.7000 | 0.2000 | Yes | this paper | Table 1 |
| SGFormer | 88.1000 | 0.7000 | Yes | this paper | Table 1 |
| NAGphormer | 88.2000 | 0.5000 | Yes | this paper | Table 1 |
| CobFormer-G | 88.4000 | 0.4000 | Yes | this paper | Table 1 |
| CobFormer-T | 88.2000 | 1.2000 | Yes | this paper | Table 1 |
| Polynormer | 87.9000 | 1.2000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 88.7000 | 0.5000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 89.4000 | 0.9000 | No | this paper | Table 1 |
| ParaFormer (a) | 88.7000 | — | No | this paper | Table 2 |

### Deezer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 66.6000 | 0.7000 | Yes | this paper | Table 1 |
| GCN | 62.7000 | 0.7000 | Yes | this paper | Table 1 |
| GAT | 61.7000 | 0.8000 | Yes | this paper | Table 1 |
| SGC | 62.3000 | 0.4000 | Yes | this paper | Table 1 |
| JKNet | 61.5000 | 0.4000 | Yes | this paper | Table 1 |
| APPNP | 66.1000 | 0.6000 | Yes | this paper | Table 1 |
| GPRGNN | 66.9000 | 0.5000 | Yes | this paper | Table 1 |
| H2GCN | 66.2000 | 0.8000 | Yes | this paper | Table 1 |
| SIGN | 66.3000 | 0.3000 | Yes | this paper | Table 1 |
| CPGNN | 65.8000 | 0.3000 | Yes | this paper | Table 1 |
| GLoGNN | 65.8000 | 0.8000 | Yes | this paper | Table 1 |
| NodeFormer | 66.4000 | 0.7000 | Yes | this paper | Table 1 |
| SGFormer | 67.1000 | 1.1000 | Yes | this paper | Table 1 |
| NAGphormer | 63.5000 | 0.6000 | Yes | this paper | Table 1 |
| CobFormer-G | 64.2000 | 0.7000 | Yes | this paper | Table 1 |
| CobFormer-T | 66.6000 | 0.7000 | Yes | this paper | Table 1 |
| Polynormer | 67.6000 | 0.4000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 67.3000 | 0.9000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 67.7000 | 0.5000 | No | this paper | Table 1 |
| ParaFormer (a) | 67.3000 | — | No | this paper | Table 2 |
| ParaFormer (b) | 66.7000 | — | No | this paper | Table 2 |
| ParaFormer (c) | 65.8000 | — | No | this paper | Table 2 |
| ParaFormer (d) | 65.0000 | — | No | this paper | Table 2 |
| ParaFormer (e) | 63.7000 | — | No | this paper | Table 2 |

### Film — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 36.5000 | 0.7000 | Yes | this paper | Table 1 |
| GCN | 30.1000 | 0.2000 | Yes | this paper | Table 1 |
| GAT | 29.8000 | 0.6000 | Yes | this paper | Table 1 |
| SGC | 27.0000 | 0.9000 | Yes | this paper | Table 1 |
| JKNet | 30.8000 | 0.7000 | Yes | this paper | Table 1 |
| APPNP | 31.3000 | 1.5000 | Yes | this paper | Table 1 |
| GPRGNN | 34.6000 | 1.2000 | Yes | this paper | Table 1 |
| H2GCN | 34.4000 | 1.7000 | Yes | this paper | Table 1 |
| SIGN | 36.5000 | 1.0000 | Yes | this paper | Table 1 |
| CPGNN | 34.5000 | 0.7000 | Yes | this paper | Table 1 |
| GLoGNN | 36.4000 | 1.6000 | Yes | this paper | Table 1 |
| Graphormer | 33.9000 | 1.4000 | Yes | this paper | Table 1 |
| GraphTrans | 32.1000 | 0.8000 | Yes | this paper | Table 1 |
| NodeFormer | 36.9000 | 1.0000 | Yes | this paper | Table 1 |
| SGFormer | 37.2000 | 1.6000 | Yes | this paper | Table 1 |
| NAGphormer | 36.4000 | 1.3000 | Yes | this paper | Table 1 |
| CobFormer-G | 30.9000 | 1.7000 | Yes | this paper | Table 1 |
| CobFormer-T | 34.9000 | 3.3000 | Yes | this paper | Table 1 |
| Polynormer | 36.8000 | 1.5000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 38.0000 | 1.2000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 37.3000 | 1.0000 | No | this paper | Table 1 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 87.2000 | 0.4000 | Yes | this paper | Table 1 |
| GCN | 88.4000 | 0.5000 | Yes | this paper | Table 1 |
| GAT | 86.3000 | 0.5000 | Yes | this paper | Table 1 |
| SGC | 83.5000 | 0.1000 | Yes | this paper | Table 1 |
| JKNet | 87.4000 | 0.1000 | Yes | this paper | Table 1 |
| APPNP | 87.0000 | 0.2000 | Yes | this paper | Table 1 |
| GPRGNN | 87.6000 | 0.4000 | Yes | this paper | Table 1 |
| H2GCN | 89.5000 | 0.4000 | Yes | this paper | Table 1 |
| SIGN | 89.4000 | 0.1000 | Yes | this paper | Table 1 |
| CPGNN | 89.1000 | 0.6000 | Yes | this paper | Table 1 |
| GLoGNN | 89.6000 | 0.4000 | Yes | this paper | Table 1 |
| Graphormer | 82.8000 | 0.2000 | Yes | this paper | Table 1 |
| GraphTrans | 87.8000 | 0.6000 | Yes | this paper | Table 1 |
| NodeFormer | 89.3000 | 0.1000 | Yes | this paper | Table 1 |
| SGFormer | 89.7000 | 0.2000 | Yes | this paper | Table 1 |
| NAGphormer | 89.7000 | 0.2000 | Yes | this paper | Table 1 |
| CobFormer-G | 87.3000 | 0.2000 | Yes | this paper | Table 1 |
| CobFormer-T | 89.0000 | 0.4000 | Yes | this paper | Table 1 |
| Polynormer | 90.3000 | 0.1000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 90.3000 | 0.2000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 90.0000 | 0.1000 | No | this paper | Table 1 |
| ParaFormer (Full) | 90.3000 | — | No | this paper | Table 2 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 36.6000 | 1.8000 | Yes | this paper | Table 1 |
| GCN | 38.6000 | 1.8000 | Yes | this paper | Table 1 |
| GAT | 35.6000 | 2.1000 | Yes | this paper | Table 1 |
| SGC | 39.3000 | 2.3000 | Yes | this paper | Table 1 |
| JKNet | 39.4000 | 1.6000 | Yes | this paper | Table 1 |
| APPNP | 35.3000 | 1.9000 | Yes | this paper | Table 1 |
| GPRGNN | 39.0000 | 2.0000 | Yes | this paper | Table 1 |
| H2GCN | 35.1000 | 1.2000 | Yes | this paper | Table 1 |
| SIGN | 40.7000 | 2.5000 | Yes | this paper | Table 1 |
| CPGNN | 38.9000 | 1.2000 | Yes | this paper | Table 1 |
| GLoGNN | 35.7000 | 1.3000 | Yes | this paper | Table 1 |
| Graphormer | 39.9000 | 2.4000 | Yes | this paper | Table 1 |
| GraphTrans | 40.6000 | 2.4000 | Yes | this paper | Table 1 |
| NodeFormer | 38.5000 | 1.5000 | Yes | this paper | Table 1 |
| SGFormer | 41.8000 | 2.2000 | Yes | this paper | Table 1 |
| NAGphormer | 39.8000 | 1.7000 | Yes | this paper | Table 1 |
| CobFormer-G | 35.4000 | 1.1000 | Yes | this paper | Table 1 |
| CobFormer-T | 33.1000 | 1.6000 | Yes | this paper | Table 1 |
| Polynormer | 40.9000 | 2.0000 | Yes | this paper | Table 1 |
| ParaFormer_GCN | 43.0000 | 2.8000 | No | this paper | Table 1 |
| ParaFormer_GPRGNN | 42.1000 | 2.1000 | No | this paper | Table 1 |
| ParaFormer (Full) | 43.3000 | — | No | this paper | Table 2 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 71.7400 | 0.2900 | Yes | this paper | Table 1 |
| SGC | 67.7900 | 0.2700 | Yes | this paper | Table 1 |
| GCN-Nsampler | 68.5000 | 0.2300 | Yes | this paper | Table 1 |
| GAT-NSampler | 67.6300 | 0.2300 | Yes | this paper | Table 1 |
| SIGN | 70.2800 | 0.2500 | Yes | this paper | Table 1 |
| NodeFormer | 59.9000 | 0.4200 | Yes | this paper | Table 1 |
| SGFormer | 72.6300 | 0.1300 | Yes | this paper | Table 1 |
| ParaFormer | 72.8700 | 0.2100 | No | this paper | Table 1 |

### pokec — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 62.3100 | 1.1300 | Yes | this paper | Table 1 |
| SGC | 52.0300 | 0.8400 | Yes | this paper | Table 1 |
| GCN-Nsampler | 63.7500 | 0.7700 | Yes | this paper | Table 1 |
| GAT-NSampler | 62.3200 | 0.6500 | Yes | this paper | Table 1 |
| SIGN | 68.0100 | 0.2500 | Yes | this paper | Table 1 |
| NodeFormer | 70.3200 | 0.4500 | Yes | this paper | Table 1 |
| SGFormer | 73.7600 | 0.2400 | Yes | this paper | Table 1 |
| ParaFormer | 74.9300 | 0.4000 | No | this paper | Table 1 |

## Baseline Models Identified

- **MLP**
- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **SGC** (from: Wu et al. 2019)
- **JKNet** (from: Xu et al. 2018)
- **APPNP** (from: Klicpera et al. 2019)
- **GPRGNN** (from: Wang et al. 2020)
- **H2GCN** (from: Zhu et al. 2020)
- **SIGN** (from: Frasca et al. 2020)
- **CPGNN** (from: Bo et al. 2022)
- **GLoGNN** (from: Huang et al. 2022)
- **Graphormer** (from: Bian et al. 2021)
- **GraphTrans** (from: You et al. 2020)
- **NodeFormer** (from: Ying et al. 2021)
- **SGFormer** (from: Wu et al. 2022)
- **NAGphormer** (from: Chen et al. 2022)
- **CobFormer-G** (from: this paper)
- **CobFormer-T** (from: this paper)
- **Polynormer** (from: this paper)
- **LP**
- **ManiReg**
- **GCN-kNN**
- **GAT-kNN**
- **DenseGAT**
- **GLCN**
- **DIFFomer-s**
- **DIFFomer-a**
- **GCN-Nsampler**
- **GAT-NSampler**

## Extraction Notes

[Cora] Extracted results for Cora from Table 1 (main comparison) and Table 2 (ablation study). Table
2 only reports mean accuracy without standard deviation for ablation variants. ParaFormer variants
are listed as ParaFormer_GCN and ParaFormer_GPRGNN in Table 1. The ablation study in Table 2 uses
variant (a) which corresponds to the full proposed model configuration. [CiteSeer] Extracted only
CiteSeer results from Table 1. The proposed model is referred to as ParaFormer with two variants
(GCN and GPRGNN backbones). All other models are baselines. Standard deviation is parsed from the
'mean ± std' format. No external data usage is indicated for these standard node classification
benchmarks. [PubMed] Extracted PubMed Accuracy results from Table 1 (main comparison) and Table 2
(ablation study). Note that Table 2 reports mean accuracy without standard deviation for the
ablation variants. The proposed model 'ParaFormer' appears in Table 1 as two variants
(ParaFormer_GCN and ParaFormer_GPRGNN) and in Table 2 as the full ablation variant (a). All values
are test set results. [Film] Extracted all rows for the 'Film' dataset from Table 1. The proposed
model is identified as 'ParaFormer' with two variants (GCN and GPRGNN backbones). All values are
mean accuracy ± standard deviation. No external data usage is indicated for these standard GNN
benchmarks. [Squirrel] Extracted all rows for the 'Squirrel' dataset from Table 1 and Table 2. Table
1 reports mean accuracy and standard deviation over five runs. Table 2 reports test accuracy for
ablation studies; note that Table 2 does not report standard deviations, so std is null for those
entries. The proposed model variants in Table 1 are ParaFormer_GCN and ParaFormer_GPRGNN. The full
ParaFormer variant is detailed in Table 2 (row a). All other models are treated as baselines.
[Chameleon] Extracted results for Chameleon from Table 1 (main comparison) and Table 2 (ablation
study). Table 2 only reports mean accuracy without standard deviation, so std is set to null for
those entries. The proposed model variants in Table 1 are ParaFormer_GCN and ParaFormer_GPRGNN.
Table 2 lists 'ParaFormer (a)' which corresponds to the best configuration (all components enabled),
matching the ParaFormer_GCN result in Table 1. [Deezer] Extracted all rows for the 'Deezer' dataset
from Table 1 and Table 2. Table 1 contains the main comparison results with standard deviations.
Table 2 contains ablation study results without standard deviations. Graphormer and GraphTrans are
marked as OOM (Out of Memory) in Table 1 and thus excluded. ParaFormer variants (GCN and GPRGNN
backbones) are treated as the proposed model. Ablation variants (a-e) are also included as they
represent configurations of the proposed model. [STL-10] failed: 3 validation errors for
ExtractionOutput results.12.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.13.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.14.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [20News] Extracted all results for the '20News'
dataset from Table 1. The table presents results for three different label settings (1000, 2000,
4000 labels). Since the prompt asks for the 'STANDARD / DEFAULT configuration' but the table does
not explicitly define a single default, and all three are primary results for the dataset under
varying semi-supervised settings, all three columns were extracted. The metric is Accuracy. No other
datasets were included. [ogbn-arxiv] Extracted all rows for the 'ogbn-arxiv' column from Table 1.
The metric is Accuracy (node classification). Standard configuration assumed as no variants were
listed in this specific table cell. [pokec] Extracted only the 'pokec' column from Table 1 as
requested. All values are test-set accuracies. Standard deviations are parsed from the '±' notation.
[Amazon2M] Extracted only Amazon2M results as requested. The table presents Accuracy for node
classification. All values include standard deviation. ParaFormer is the proposed model (bolded). No
external data usage indicated for these baselines in the context of this specific table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*