# Extraction: 2402.00789
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: Graph-Mamba (0.3M params)
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 4 |
| GIN | 0.5526 | 0.0152 | Yes | this paper | Table 4 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 4 |
| GPS+Transformer | 0.7226 | 0.0031 | Yes | this paper | Table 4 |
| GPS+Performer | 0.7067 | 0.0033 | Yes | this paper | Table 4 |
| GPS+BigBird | 0.7048 | 0.0010 | Yes | this paper | Table 4 |
| Exphormer | 0.7413 | 0.0050 | Yes | this paper | Table 4 |
| Graph-Mamba | 0.7370 | 0.0034 | No | this paper | Table 4 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0097 | Yes | this paper | Table 2 |
| GIN | 0.6472 | 0.0155 | Yes | this paper | Table 2 |
| GatedGCN | 0.7384 | 0.0032 | Yes | this paper | Table 2 |
| GPS+Transformer | 0.7799 | 0.0017 | Yes | this paper | Table 2 |
| GPS+Performer | 0.7829 | 0.0004 | Yes | this paper | Table 2 |
| GPS+BigBird | 0.7746 | 0.0002 | Yes | this paper | Table 2 |
| Exphormer | 0.7802 | 0.0011 | Yes | this paper | Table 2 |
| Graph-Mamba | 0.7680 | 0.0036 | No | this paper | Table 2 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0021 | Yes | this paper | Table 4 |
| GIN | 0.9649 | 0.0025 | Yes | this paper | Table 4 |
| GatedGCN | 0.9734 | 0.0014 | Yes | this paper | Table 4 |
| GPS+Transformer | 0.9811 | 0.0011 | Yes | this paper | Table 4 |
| GPS+Performer | 0.9834 | 0.0003 | Yes | this paper | Table 4 |
| GPS+BigBird | 0.9817 | 0.0001 | Yes | this paper | Table 4 |
| Exphormer | 0.9843 | 0.0004 | Yes | this paper | Table 4 |
| Graph-Mamba | 0.9842 | 0.0008 | No | this paper | Table 4 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 4 |
| GIN | 0.8539 | 0.0013 | Yes | this paper | Table 4 |
| GatedGCN | 0.8557 | 0.0008 | Yes | this paper | Table 4 |
| GPS+Transformer | 0.8664 | 0.0011 | Yes | this paper | Table 4 |
| GPS+Performer | 0.8334 | 0.0029 | Yes | this paper | Table 4 |
| GPS+BigBird | 0.8600 | 0.0014 | Yes | this paper | Table 4 |
| Exphormer | 0.8670 | 0.0003 | Yes | this paper | Table 4 |
| Graph-Mamba | 0.8671 | 0.0005 | No | this paper | Table 4 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table 2 |
| GIN | 0.3180 | 0.0027 | Yes | this paper | Table 2 |
| GatedGCN | 0.3218 | 0.0011 | Yes | this paper | Table 2 |
| GPS+Transformer | 0.3442 | 0.0009 | Yes | this paper | Table 2 |
| GPS+Performer | 0.3437 | 0.0005 | Yes | this paper | Table 2 |
| GPS+BigBird | 0.3391 | 0.0002 | Yes | this paper | Table 2 |
| Exphormer | 0.3587 | 0.0025 | Yes | this paper | Table 2 |
| Graph-Mamba | 0.3395 | 0.0013 | No | this paper | Table 2 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline training procedure | 0.3105 | — | Yes | this paper | Table 1 |
| Permutation-only | 0.4193 | — | Yes | this paper | Table 1 |
| Graph-Mamba (Node Level + Degree) | 0.4314 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Graph-Mamba (Baseline) | 0.6581 | — | Yes | this paper | Table 1 |
| Graph-Mamba (Node Level Permutation) | 0.6821 | — | Yes | this paper | Table 1 |
| Graph-Mamba (Node Level Permutation + Degree Prioritization) | 0.6834 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **GPS+Transformer**, 0.3M params (from: this paper (consolidated from Exphormer benchmark))
- **Exphormer** (from: Shirzad et al. 2023)
- **GPS+Performer** (from: this paper (consolidated from Exphormer benchmark))
- **GPS+BigBird** (from: this paper (consolidated from Exphormer benchmark))
- **Baseline training procedure** (from: this paper)
- **Permutation-only** (from: this paper)
- **GCN** (from: Kipf & Welling 2017)
- **GIN** (from: Xu et al. 2019)
- **GatedGCN** (from: Bresson & Laurent 2017)

## Extraction Notes

[Peptides-func] Extracted results from Table 1 (Ablation Study). The table reports AP scores for
Peptides-Func under three configurations of the Graph-Mamba model. The text confirms these are
single-run results (seed 0) for the ablation study, so no standard deviation is reported. The
'Proposed' model is identified as the final configuration (Node Level + Degree) which the paper
recommends as the default recipe. Other baselines (GPS+Transformer, Exphormer, etc.) are mentioned
in the text as being benchmarked on LRGB datasets (including Peptides-Func) in other tables (Table
2/3), but their specific numerical values for Peptides-Func are not present in the provided text or
tables. Therefore, only the Graph-Mamba ablation rows could be extracted. [PascalVOC-SP] Extracted
results from Table 1 (ablation study) for PascalVOC-SP. The table reports F1 scores for three
configurations: Baseline, Node Level Permutation, and Node Level + Degree Prioritization (which
corresponds to the proposed Graph-Mamba default recipe). No standard deviation is reported in this
specific ablation table (single run with seed 0 as per text). Other tables (Table 2/3 mentioned in
text) were not provided in the input, so only Table 1 results are extracted. [CIFAR10] Extracted
only CIFAR10 results from Table 4 ('Benchmark on Short to Medium-Range Graph Datasets'). All other
tables were ignored as they did not contain CIFAR10 results or were ablation/hyperparameter tables.
The primary metric Accuracy was used. Standard configuration was assumed as no variants were listed
for CIFAR10 in the benchmark table. [MNIST] Extracted only MNIST results from Table 4 as requested.
The table caption refers to 'Short to Medium-Range Graph Datasets'. The dataset name in the table is
'MNIST'. The metric is 'Accuracy'. All rows for MNIST were extracted. [CLUSTER] Extracted results
for the CLUSTER dataset from Table 2 ('Benchmark on Short to Medium-Range Graph Datasets'). The
primary metric is Accuracy. All models listed in the table for the CLUSTER column were extracted.
The proposed model Graph-Mamba achieved 0.7680 ± 0.0036. [PATTERN] Extracted only the 'PATTERN'
dataset results from Table 4 ('Benchmark on Short to Medium-Range Graph Datasets'). The primary
metric is Accuracy. All rows from the table were included. Standard deviations were parsed from the
'±' notation. The proposed model is Graph-Mamba. [PCQM-Contact] Extracted only the PCQM-Contact
results from Table 2 (Benchmark on Short to Medium-Range Graph Datasets). The primary metric MRR was
used. All other tables were ignored as they did not contain PCQM-Contact results or were
ablation/hyperparameter tables.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*