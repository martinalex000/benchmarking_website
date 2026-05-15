# Extraction: arXiv:2504.12588
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: PPGT
- Type: GraphTransformer

## Results

### BREC — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 1-WL | 0.0000 | — | Yes | this paper | Table 1 |
| 3-WL | 0.6750 | — | Yes | this paper | Table 1 |
| SUN | 0.5580 | — | Yes | frasca2022UnderstandingExtendingSubgraph | Table 1 |
| SSWL+ | 0.6200 | — | Yes | zhang2023CompleteExpressivenessHierarchy | Table 1 |
| I$^2$GNN | 0.7020 | — | Yes | huang2023BoostingCycleCounting | Table 1 |
| PPGN | 0.5820 | — | Yes | maron2019ProvablyPowerfulGraph | Table 1 |
| 2-DRFWL(2) | 0.5225 | — | Yes | zhou2023DistanceRestrictedFolkloreWeisfeilerLeman | Table 1 |
| 3-DRFWL(2) | 0.5575 | — | Yes | zhou2023DistanceRestrictedFolkloreWeisfeilerLeman | Table 1 |
| N$^2$GNN | 0.7180 | — | Yes | feng2023ExtendingDesignSpace | Table 1 |
| Graphormer | 0.1980 | — | Yes | ying2021TransformersReallyPerform | Table 1 |
| EPNN | 0.5380 | — | Yes | zhang2024ExpressivePowerSpectral | Table 1 |
| CKGConv | 0.5450 | — | Yes | ma2024CKGConvGeneralGraph | Table 1 |
| GRIT | 0.5450 | — | Yes | ma2023GraphInductiveBiases | Table 1 |
| PPGT w/o SPE | 0.5450 | — | Yes | this paper | Table 1 |
| PPGT | 0.5850 | — | No | this paper | Table 1 |
| I$^2$GNN+PPGT | 0.7600 | — | Yes | this paper | Table 1 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5525 | 0.0153 | Yes | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| PNA | 0.7035 | 0.0063 | Yes | this paper | Table 1 |
| CRaW1 | 0.6901 | 0.0026 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | this paper | Table 1 |
| DGN | 0.7284 | 0.0042 | Yes | this paper | Table 1 |
| CKGCN | 0.7278 | 0.0044 | Yes | this paper | Table 1 |
| EGT | 0.6870 | 0.0041 | Yes | this paper | Table 1 |
| GPS | 0.7230 | 0.0036 | Yes | this paper | Table 1 |
| GRIT | 0.7647 | 0.0088 | Yes | this paper | Table 1 |
| PPGT | 0.7856 | 0.0070 | No | this paper | Table 1 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | this paper | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | this paper | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | this paper | Table 1 |
| CKGCN | 0.7900 | 0.0014 | Yes | this paper | Table 1 |
| SAN | 0.7669 | 0.0065 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.7786 | 0.0010 | Yes | this paper | Table 1 |
| EGT | 0.7923 | 0.0035 | Yes | this paper | Table 1 |
| GPS | 0.7802 | 0.0018 | Yes | this paper | Table 1 |
| GRIT | 0.8003 | 0.0028 | Yes | this paper | Table 1 |
| PPGT | 0.8003 | 0.0011 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | this paper | Table 1 |
| GIN | 0.9648 | 0.0025 | Yes | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | this paper | Table 1 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| PNA | 0.9794 | 0.0012 | Yes | this paper | Table 1 |
| CRaW1 | 0.9794 | 0.0005 | Yes | this paper | Table 1 |
| CKGCN | 0.9842 | 0.0015 | Yes | this paper | Table 1 |
| EGT | 0.9817 | 0.0009 | Yes | this paper | Table 1 |
| GPS | 0.9805 | 0.0013 | Yes | this paper | Table 1 |
| GRIT | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| PPGT | 0.9861 | 0.0010 | No | this paper | Table 1 |

### OGBN-ArXiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7174 | 0.0029 | Yes | this paper | Table 4 |
| GCN-NSampler | 0.6850 | 0.0023 | Yes | this paper | Table 4 |
| DeeperGCN | 0.7190 | — | Yes | li2022DeeperGCNAllYou | Table 4 |
| SIGN | 0.7028 | 0.0025 | Yes | this paper | Table 4 |
| NodeFormer | 0.5990 | 0.0042 | Yes | this paper | Table 4 |
| SGFormer | 0.7263 | 0.0013 | Yes | wu2023SGFormerSimplifyingEmpoweringa | Table 4 |
| Exphormer | 0.7244 | 0.0028 | Yes | shirzad2023ExphormerSparseTransformers | Table 4 |
| PPGT | 0.7246 | 0.0015 | No | this paper | Table 4 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0014 | Yes | this paper | Table 1 |
| GAT | 0.7827 | 0.0019 | Yes | this paper | Table 1 |
| GatedGCN | 0.8557 | 0.0009 | Yes | this paper | Table 1 |
| GIN-AK+ | 0.8685 | 0.0006 | Yes | this paper | Table 1 |
| DGN | 0.8668 | 0.0003 | Yes | this paper | Table 1 |
| CKGCN | 0.8866 | 0.0014 | Yes | this paper | Table 1 |
| SAN | 0.8658 | 0.0004 | Yes | this paper | Table 1 |
| K-Subgraph SAT | 0.8685 | 0.0004 | Yes | this paper | Table 1 |
| EGT | 0.8682 | 0.0002 | Yes | this paper | Table 1 |
| GPS | 0.8669 | 0.0006 | Yes | this paper | Table 1 |
| GRIT | 0.8720 | 0.0008 | Yes | this paper | Table 1 |
| PPGT | 0.8975 | 0.0003 | No | this paper | Table 1 |

### PCQM4Mv2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1379 | — | Yes | this paper | Table 4 |
| GCN-virtual | 0.1153 | — | Yes | this paper | Table 4 |
| GIN | 0.1195 | — | Yes | this paper | Table 4 |
| GIN-virtual | 0.1083 | — | Yes | this paper | Table 4 |
| GRPE | 0.0890 | — | Yes | this paper | Table 4 |
| Graphormer | 0.0864 | — | Yes | this paper | Table 4 |
| TokenGT (ORF) | 0.0962 | — | Yes | this paper | Table 4 |
| TokenGT (Lap) | 0.0910 | — | Yes | this paper | Table 4 |
| GPS-small | 0.0938 | — | Yes | this paper | Table 4 |
| GPS-medium | 0.0858 | — | Yes | this paper | Table 4 |
| GRIT | 0.0859 | — | Yes | this paper | Table 4 |
| PPGT | 0.0856 | — | No | this paper | Table 4 |

### PascalVoc-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | Yes | this paper | Table 1 |
| GINE | 0.2718 | 0.0054 | Yes | this paper | Table 1 |
| GatedGCN | 0.3880 | 0.0040 | Yes | this paper | Table 1 |
| DRew | 0.3314 | 0.0024 | Yes | this paper | Table 1 |
| Exphormer | 0.3960 | 0.0027 | Yes | this paper | Table 1 |
| GPS | 0.4440 | 0.0065 | Yes | this paper | Table 1 |
| PPGT | 0.4641 | 0.0033 | No | this paper | Table 1 |

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6860 | 0.0050 | Yes | this paper | Table 1 |
| GINE | 0.6621 | 0.0067 | Yes | this paper | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | this paper | Table 1 |
| DRew | 0.7150 | 0.0044 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GPS | 0.6534 | 0.0090 | Yes | this paper | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | this paper | Table 1 |
| PPGT | 0.6961 | 0.0062 | No | this paper | Table 1 |

### Peptides-Struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2460 | 0.0007 | Yes | this paper | Table 1 |
| GINE | 0.2473 | 0.0017 | Yes | this paper | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | this paper | Table 1 |
| DRew | 0.2536 | 0.0015 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| GPS | 0.2509 | 0.0010 | Yes | this paper | Table 1 |
| GRIT | 0.2460 | 0.0012 | Yes | this paper | Table 1 |
| PPGT | 0.2450 | 0.0017 | No | this paper | Table 1 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SUN | 0.0830 | — | Yes | this paper | Table 1 |
| SSWL+ | 0.0700 | — | Yes | this paper | Table 1 |
| I$^2$GNN | 0.0830 | — | Yes | this paper | Table 1 |
| 2-DRFWL(2) | 0.0770 | — | Yes | this paper | Table 1 |
| N$^2$GNN | 0.0590 | — | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | — | Yes | this paper | Table 1 |
| CKGConv | 0.0590 | — | Yes | this paper | Table 1 |
| GRIT | 0.0590 | — | Yes | this paper | Table 1 |
| PPGT | 0.0570 | — | No | this paper | Table 1 |
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 2 |
| GIN | 0.5260 | 0.0510 | Yes | this paper | Table 2 |
| GAT | 0.3840 | 0.0070 | Yes | this paper | Table 2 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 2 |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table 2 |
| CRaW1 | 0.0850 | 0.0040 | Yes | this paper | Table 2 |
| GIN-AK+ | 0.0800 | 0.0010 | Yes | this paper | Table 2 |
| DGN | 0.1680 | 0.0030 | Yes | this paper | Table 2 |
| CKGCN | 0.0590 | 0.0030 | Yes | this paper | Table 2 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 2 |
| K-Subgraph SAT | 0.0940 | 0.0080 | Yes | this paper | Table 2 |
| EGT | 0.1080 | 0.0090 | Yes | this paper | Table 2 |
| Graphormer-GD | 0.0810 | 0.0090 | Yes | this paper | Table 2 |
| GPS | 0.0700 | 0.0040 | Yes | this paper | Table 2 |
| GMLP-Mixer | 0.0770 | 0.0030 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **1-WL**
- **3-WL**
- **SUN** (from: frasca2022UnderstandingExtendingSubgraph)
- **SSWL+** (from: zhang2023CompleteExpressivenessHierarchy)
- **I$^2$GNN** (from: huang2023BoostingCycleCounting)
- **PPGN** (from: maron2019ProvablyPowerfulGraph)
- **2-DRFWL(2)** (from: zhou2023DistanceRestrictedFolkloreWeisfeilerLeman)
- **3-DRFWL(2)** (from: zhou2023DistanceRestrictedFolkloreWeisfeilerLeman)
- **N$^2$GNN** (from: feng2023ExtendingDesignSpace)
- **Graphormer** (from: ying2021TransformersReallyPerform)
- **EPNN** (from: zhang2024ExpressivePowerSpectral)
- **CKGConv** (from: ma2024CKGConvGeneralGraph)
- **GRIT** (from: ma2023GraphInductiveBiases)
- **GCN**
- **GIN**
- **GAT**
- **GatedGCN**
- **PNA**
- **CRaW1**
- **GIN-AK+**
- **DGN**
- **CKGCN**
- **SAN**
- **K-Subgraph SAT**
- **EGT**
- **Graphormer-GD**
- **GPS**
- **GMLP-Mixer**
- **GINE**
- **DRew**
- **Exphormer**
- **GCN-virtual**, 4.9M params
- **GIN-virtual**, 6.7M params
- **GRPE**, 46.2M params
- **TokenGT (ORF)**, 48.6M params
- **TokenGT (Lap)**, 48.5M params
- **GPS-small**, 6.2M params
- **GPS-medium**, 19.4M params
- **GCN-NSampler**
- **DeeperGCN** (from: li2022DeeperGCNAllYou)
- **SIGN**
- **NodeFormer**
- **SGFormer** (from: wu2023SGFormerSimplifyingEmpoweringa)

## Extraction Notes

[BREC] Extracted only the 'Total' Accuracy column for the BREC dataset as per the primary metric
focus. Skipped the ZINC column and the sensitivity study table (Table 2) as it focused on a specific
subset (CFI) and variant configurations. [ZINC] Extracted ZINC results from both Table 1
(expressivity comparison) and Table 2 (general benchmarking). Table 1 contains single values, while
Table 2 contains mean +/- std. [MNIST] Extracted only MNIST results as requested. Normalized
accuracy percentages to [0, 1] range. [CIFAR10] Extracted only CIFAR10 results as requested.
Normalized percentages to [0, 1] range. Models with no reported value for CIFAR10 (SAN, K-Subgraph
SAT, Graphormer-GD, GMLP-Mixer) were omitted from the results list. [PATTERN] Metric 'W. Accuracy'
was normalized to 'Accuracy' as per primary metric instructions. All values were divided by 100 to
fit the [0, 1] range. [CLUSTER] Metric 'W. Accuracy' was normalized to 'Accuracy' as per primary
metric instructions. Values were divided by 100 to fit [0, 1] range. [Peptides-Func] Extracted only
Peptides-Func results as requested. Model type for PPGT inferred as GNN based on context of LRGB
benchmarks. [Peptides-Struct] Extracted only Peptides-Struct results as requested. All models from
the table were included. [PascalVoc-SP] GRIT had no value reported for PascalVoc-SP and was excluded
from the results list. Only PascalVoc-SP results were extracted as per focus instructions.
[PCQM4Mv2] The paper explicitly states that the validation set was used in place of the private test
set for evaluation on PCQM4Mv2. Therefore, the 'Valid.' column in Table 4 is extracted as the
primary benchmark result. [OGBN-ArXiv] Table label was provided as tab:ogbn-arxiv-results; mapped to
Table 4 based on context of typical paper structures or simply referred to as the OGBN-ArXiv results
table. All values were percentages and normalized to [0, 1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*