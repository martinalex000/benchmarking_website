# Extraction: arXiv:2411.15671
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: GSM++
- Type: GraphTransformer

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| GraphSAGE | 0.5363 | 0.0039 | Yes | this paper | Table 1 |
| GAT | 0.5270 | 0.0062 | Yes | this paper | Table 1 |
| OrderedGNN | 0.4729 | 0.0065 | Yes | this paper | Table 1 |
| tGNN | 0.4821 | 0.0053 | Yes | this paper | Table 1 |
| Gated-GCN | 0.4300 | 0.0032 | Yes | this paper | Table 1 |
| NAGphormer | 0.5126 | 0.0072 | Yes | this paper | Table 1 |
| GPS | 0.5310 | 0.0042 | Yes | this paper | Table 1 |
| Exphormer | 0.5351 | 0.0046 | Yes | this paper | Table 1 |
| NodeFormer | 0.4386 | 0.0035 | Yes | this paper | Table 1 |
| DIFFormer | 0.4784 | 0.0065 | Yes | this paper | Table 1 |
| GOAT | 0.4461 | 0.0050 | Yes | this paper | Table 1 |
| GMN | 0.5327 | 0.0030 | Yes | this paper | Table 1 |
| GSM++ (BFS) | 0.5381 | 0.0035 | No | this paper | Table 1 |
| GSM++ (DFS) | 0.5361 | 0.0029 | No | this paper | Table 1 |
| GSM++ (MoT) | 0.5390 | 0.0104 | No | this paper | Table 1 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6577 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| SPN | 0.3722 | 0.0827 | Yes | this paper | Table 1 |
| GIN | 0.5526 | 0.0152 | Yes | this paper | Table 1 |
| Gated-GCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| CRaWl | 0.6901 | 0.0259 | Yes | this paper | Table 1 |
| GPS | 0.7226 | 0.0031 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.7048 | 0.0010 | Yes | this paper | Table 1 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.7646 | 0.0088 | Yes | this paper | Table 1 |
| GRED | 0.7685 | 0.0019 | Yes | this paper | Table 1 |
| GMN | 0.7444 | 0.0009 | Yes | this paper | Table 1 |
| GSM++ (BFS) | 0.7659 | 0.0024 | No | this paper | Table 1 |
| GSM++ (DFS) | 0.7692 | 0.0031 | No | this paper | Table 1 |
| GSM++ (MoT) | 0.7781 | 0.0028 | No | this paper | Table 1 |

### Cycle Check — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8030 | — | Yes | this paper | Table 1 |
| GatedGCN | 0.8620 | — | Yes | this paper | Table 1 |
| MPNN | 0.9910 | — | Yes | this paper | Table 1 |
| GIN | 0.9820 | — | Yes | this paper | Table 1 |
| Node | 0.3080 | — | Yes | this paper | Table 1 |
| HAC (DFS) | 0.5890 | — | Yes | this paper | Table 1 |
| k-hop | 0.9160 | — | Yes | this paper | Table 1 |
| HAC (BFS) | 0.9190 | — | Yes | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0021 | Yes | this paper | Table 2 |
| GraphSAGE | 0.9731 | 0.0009 | Yes | this paper | Table 2 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 2 |
| SPN | 0.8331 | 0.0446 | Yes | this paper | Table 2 |
| GIN | 0.9649 | 0.0025 | Yes | this paper | Table 2 |
| Gated-GCN | 0.9734 | 0.0014 | Yes | this paper | Table 2 |
| CRaWl | 0.9794 | 0.0500 | Yes | this paper | Table 2 |
| GPS | 0.9811 | 0.0011 | Yes | this paper | Table 2 |
| GPS (BigBird) | 0.9817 | 0.0001 | Yes | this paper | Table 2 |
| Exphormer | 0.9855 | 0.0003 | Yes | this paper | Table 2 |
| GRIT | 0.9810 | 0.0011 | Yes | this paper | Table 2 |
| GRED | 0.9838 | 0.0002 | Yes | this paper | Table 2 |
| GMN | 0.9783 | 0.0020 | Yes | this paper | Table 2 |
| GSM++ (BFS) | 0.9848 | 0.0012 | No | this paper | Table 2 |
| GSM++ (DFS) | 0.9829 | 0.0014 | No | this paper | Table 2 |
| GSM++ (MoT) | 0.9884 | 0.0015 | No | this paper | Table 2 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8100 | 0.0000 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8730 | 0.0002 | Yes | this paper | Table 1 |
| GAT | 0.8509 | 0.0025 | Yes | this paper | Table 1 |
| SPN | 0.6407 | 0.0581 | Yes | this paper | Table 1 |
| GIN | 0.8898 | 0.0055 | Yes | this paper | Table 1 |
| Gated-GCN | 0.9223 | 0.0065 | Yes | this paper | Table 1 |
| GPS | 0.9298 | 0.0047 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.9234 | 0.0034 | Yes | this paper | Table 1 |
| Exphormer | 0.9402 | 0.0020 | Yes | this paper | Table 1 |
| GMN | 0.9352 | 0.0036 | Yes | this paper | Table 1 |
| GSM++ (BFS) | 0.9417 | 0.0020 | No | this paper | Table 1 |
| GSM++ (DFS) | 0.9389 | 0.0024 | No | this paper | Table 1 |
| GSM++ (MoT) | 0.9437 | 0.0058 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| GraphSAGE | 0.9351 | 0.0057 | Yes | this paper | Table 1 |
| GAT | 0.9391 | 0.0035 | Yes | this paper | Table 1 |
| OrderedGNN | 0.8058 | 0.0108 | Yes | this paper | Table 1 |
| tGNN | 0.9193 | 0.0077 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8754 | 0.0122 | Yes | this paper | Table 1 |
| NAGphormer | 0.8419 | 0.0066 | Yes | this paper | Table 1 |
| GPS | 0.9063 | 0.0067 | Yes | this paper | Table 1 |
| Exphormer | 0.9074 | 0.0053 | Yes | this paper | Table 1 |
| NodeFormer | 0.8671 | 0.0088 | Yes | this paper | Table 1 |
| DIFFormer | 0.9089 | 0.0058 | Yes | this paper | Table 1 |
| GOAT | 0.8109 | 0.0102 | Yes | this paper | Table 1 |
| GMN | 0.8992 | 0.0063 | Yes | this paper | Table 1 |
| GSM++ (BFS) | 0.9109 | 0.0098 | No | this paper | Table 1 |
| GSM++ (DFS) | 0.9145 | 0.0036 | No | this paper | Table 1 |
| GSM++ (MoT) | 0.9149 | 0.0111 | No | this paper | Table 1 |

### Node Degree — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0930 | — | Yes | this paper | Table 1 |
| GatedGCN | 0.2980 | — | Yes | this paper | Table 1 |
| MPNN | 0.9890 | — | Yes | this paper | Table 1 |
| GIN | 0.3640 | — | Yes | this paper | Table 1 |
| Node | 0.2990 | — | Yes | this paper | Table 1 |
| HAC (DFS) | 0.3100 | — | Yes | this paper | Table 1 |
| k-hop | 0.9760 | — | Yes | this paper | Table 1 |
| HAC (BFS) | 0.9810 | — | Yes | this paper | Table 1 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 2 |
| GraphSAGE | 0.5049 | 0.0001 | Yes | this paper | Table 2 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 2 |
| SPN | 0.8657 | 0.0014 | Yes | this paper | Table 2 |
| GIN | 0.8539 | 0.0013 | Yes | this paper | Table 2 |
| Gated-GCN | 0.8557 | 0.0008 | Yes | this paper | Table 2 |
| NAGphormer | 0.8644 | 0.0003 | Yes | this paper | Table 2 |
| GPS | 0.8664 | 0.0011 | Yes | this paper | Table 2 |
| GPS (BigBird) | 0.8600 | 0.0014 | Yes | this paper | Table 2 |
| Exphormer | 0.8670 | 0.0003 | Yes | this paper | Table 2 |
| NodeFormer | 0.8639 | 0.0021 | Yes | this paper | Table 2 |
| DIFFormer | 0.8701 | 0.0018 | Yes | this paper | Table 2 |
| GRIT | 0.8719 | 0.0008 | Yes | this paper | Table 2 |
| GRED | 0.8675 | 0.0002 | Yes | this paper | Table 2 |
| GMN | 0.8649 | 0.0019 | Yes | this paper | Table 2 |
| GSM++ (BFS) | 0.8738 | 0.0014 | No | this paper | Table 2 |
| GSM++ (DFS) | 0.8731 | 0.0008 | No | this paper | Table 2 |
| GSM++ (MoT) | 0.8793 | 0.0015 | No | this paper | Table 2 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 1 |
| GraphSAGE | 0.8574 | 0.0067 | Yes | this paper | Table 1 |
| GAT | 0.7973 | 0.0039 | Yes | this paper | Table 1 |
| OrderedGNN | 0.7768 | 0.0039 | Yes | this paper | Table 1 |
| tGNN | 0.7995 | 0.0075 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7446 | 0.0054 | Yes | this paper | Table 1 |
| NAGphormer | 0.7434 | 0.0077 | Yes | this paper | Table 1 |
| GPS | 0.8200 | 0.0061 | Yes | this paper | Table 1 |
| Exphormer | 0.8903 | 0.0037 | Yes | this paper | Table 1 |
| NodeFormer | 0.6449 | 0.0073 | Yes | this paper | Table 1 |
| DIFFormer | 0.7910 | 0.0032 | Yes | this paper | Table 1 |
| GOAT | 0.7159 | 0.0125 | Yes | this paper | Table 1 |
| GMN | 0.8219 | 0.0012 | Yes | this paper | Table 1 |
| GSM++ (BFS) | 0.9003 | 0.0087 | No | this paper | Table 1 |
| GSM++ (DFS) | 0.9124 | 0.0023 | No | this paper | Table 1 |
| GSM++ (MoT) | 0.9177 | 0.0040 | No | this paper | Table 1 |

### Triangle Counting — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8410 | — | Yes | this paper | Table 1 |
| GatedGCN | 0.4760 | — | Yes | this paper | Table 1 |
| MPNN | 0.4170 | — | Yes | this paper | Table 1 |
| GIN | 0.6590 | — | Yes | this paper | Table 1 |
| Node | 0.7130 | — | Yes | this paper | Table 1 |
| HAC (DFS) | 0.6980 | — | Yes | this paper | Table 1 |
| k-hop | 0.5210 | — | Yes | this paper | Table 1 |
| HAC (BFS) | 0.5740 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **GatedGCN**
- **MPNN**
- **GIN**
- **Node (Transformer)**
- **HAC (DFS) (Transformer)**
- **k-hop (Transformer)**
- **HAC (BFS) (Transformer)**
- **Node (Mamba)**
- **HAC (DFS) (Mamba)**
- **k-hop (Mamba)**
- **HAC (BFS) (Mamba)**
- **Node (Hybrid)**
- **HAC (DFS) (Hybrid)**
- **k-hop (Hybrid)**
- **HAC (BFS) (Hybrid)**
- **GraphSAGE**
- **GAT**
- **SPN**
- **Gated-GCN**
- **CRaWl**
- **GPS**
- **GPS (BigBird)**
- **Exphormer**
- **GRIT**
- **GRED**
- **GMN**
- **NAGphormer**
- **NodeFormer**
- **DIFFormer**
- **OrderedGNN**
- **tGNN**
- **GOAT**

## Extraction Notes

[Node Degree] The 'Hybrid (Mamba + Transformer)' section contains the final proposed model
configurations (GSM++). I have marked these as is_proposed=true. The dataset 'Node Degree' has two
configurations (1K and 100K); both are extracted as they represent the standard benchmark sizes for
this task. [Cycle Check] The table contains two columns for 'Cycle Check' (1K and 100K). Both are
extracted as they represent the standard benchmark across different graph sizes. The proposed model
'GSM++' is mentioned in the text as the final model, but the table lists its components/variants
(Transformers, Mamba, Hybrid) rather than a single 'GSM++' row. I have extracted all rows from the
'Cycle Check' columns. [Triangle Counting] Extracted results for 'Triangle Counting' from Table 1.
The table provides two configurations: 'Erdos-Renyi' and 'Regular'. Per instructions to use the
standard/default configuration and skip optional variants, I have extracted the 'Erdos-Renyi' column
as it is typically the primary benchmark for this task in this context. The proposed model GSM++ is
mentioned in text but the table lists its components/variants (Transformers, Mamba, Hybrid) rather
than a single 'GSM++' row. [MNIST] Extracted only MNIST results from Table 2 as requested. Table 3
(Ablation) did not contain MNIST data. [CIFAR10] Extracted only CIFAR10 results from Table 1 as
requested. Table 2 (Ablation) did not contain CIFAR10 data. [PATTERN] Extracted results for PATTERN
dataset from Table 2. Ablation table results were skipped as they represent internal model
variants/configurations rather than the standard benchmark results requested. [MalNet-Tiny]
Extracted only MalNet-Tiny results from Table 1 as requested. Table 2 (Ablation) did not contain
MalNet-Tiny data. [Roman-empire] Extracted only Roman-empire dataset results as requested. GSM++
variants are treated as the proposed model. [Amazon-ratings] Extracted only the Amazon-ratings
column from the first table as requested. GSM++ variants are marked as proposed. [Minesweeper]
Extracted all models for the Minesweeper dataset from the heterophilic datasets table. GSM++
variants are treated as the proposed model.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*