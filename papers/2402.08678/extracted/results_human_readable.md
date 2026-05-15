# Extraction: arXiv:2402.08678
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GMN
- Type: GNN

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 1 |
| Gated-GCN | 0.4300 | 0.0032 | Yes | this paper | Table 1 |
| NAGphormer | 0.5126 | 0.0072 | Yes | this paper | Table 1 |
| GPS | 0.5310 | 0.0042 | Yes | this paper | Table 1 |
| Exphormer | 0.5351 | 0.0046 | Yes | this paper | Table 1 |
| GOAT | 0.4461 | 0.0050 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.4513 | 0.0097 | Yes | this paper | Table 1 |
| GMN | 0.5407 | 0.0031 | No | this paper | Table 1 |
| GMN w/o bidirectional Mamba | 0.5016 | 0.0045 | Yes | this paper | Table 2 |
| GMN w/o MPNN | 0.5312 | 0.0044 | Yes | this paper | Table 2 |
| GMN PPR ordering | 0.5299 | 0.0037 | Yes | this paper | Table 2 |
| GMN w/o PE | 0.5308 | 0.0026 | Yes | this paper | Table 2 |

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | this paper | Table 1 |
| GIN | 0.5526 | 0.0152 | Yes | this paper | Table 1 |
| Gated-GCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| CRaWl | 0.6901 | 0.0259 | Yes | this paper | Table 1 |
| GPS | 0.7226 | 0.0031 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.7048 | 0.0010 | Yes | this paper | Table 1 |
| Exphormer | 0.7469 | 0.0013 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.7341 | 0.0015 | Yes | this paper | Table 1 |
| GMN | 0.7576 | 0.0042 | No | this paper | Table 1 |
| S4G | 0.7065 | 0.0033 | Yes | De Bortoli et al. | Table 2 |
| GRED | 0.7537 | 0.6210 | Yes | Ding et al. | Table 2 |

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table 1 |
| GIN | 0.1339 | 0.0044 | Yes | this paper | Table 1 |
| Gated-GCN | 0.2641 | 0.0045 | Yes | this paper | Table 1 |
| CRaWl | 0.3219 | 0.0011 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2592 | 0.0158 | Yes | this paper | Table 1 |
| NAGphormer | 0.3458 | 0.0070 | Yes | this paper | Table 1 |
| GPS | 0.3774 | 0.0150 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.2622 | 0.0008 | Yes | this paper | Table 1 |
| Exphormer | 0.3430 | 0.0108 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.3895 | 0.0125 | Yes | this paper | Table 1 |
| GMN- | 0.3618 | 0.0053 | Yes | this paper | Table 1 |
| GMN | 0.3974 | 0.0101 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0021 | Yes | this paper | Table 1 |
| GIN | 0.9649 | 0.0025 | Yes | this paper | Table 1 |
| Gated-GCN | 0.9734 | 0.0014 | Yes | this paper | Table 1 |
| CRaWl | 0.9794 | 0.0500 | Yes | this paper | Table 1 |
| GPS | 0.9811 | 0.0011 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.9817 | 0.0001 | Yes | this paper | Table 1 |
| Exphormer | 0.9855 | 0.0003 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.9821 | 0.0004 | Yes | this paper | Table 1 |
| GMN | 0.9839 | 0.0018 | No | this paper | Table 1 |
| S4G | 0.9637 | 0.0017 | Yes | De Bortoli et al. | Table 2 |
| GRED | 0.9822 | 0.0095 | Yes | Ding et al. | Table 2 |

### MalNet-Tiny — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8100 | 0.0000 | Yes | this paper | Table 1 |
| GIN | 0.8898 | 0.0055 | Yes | this paper | Table 1 |
| Gated-GCN | 0.9223 | 0.0065 | Yes | this paper | Table 1 |
| GPS | 0.9298 | 0.0047 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.9234 | 0.0034 | Yes | this paper | Table 1 |
| Exphormer | 0.9402 | 0.0020 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.9311 | 0.0042 | Yes | this paper | Table 1 |
| GMN | 0.9415 | 0.0020 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8754 | 0.0122 | Yes | this paper | Table 1 |
| NAGphormer | 0.8419 | 0.0066 | Yes | this paper | Table 1 |
| GPS | 0.9063 | 0.0067 | Yes | this paper | Table 1 |
| Exphormer | 0.9074 | 0.0053 | Yes | this paper | Table 1 |
| GOAT | 0.8109 | 0.0102 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.8993 | 0.0054 | Yes | this paper | Table 1 |
| GMN | 0.9101 | 0.0023 | No | this paper | Table 1 |
| GMN w/o bidirectional Mamba | 0.8597 | 0.0028 | Yes | this paper | Table 2 |
| GMN w/o MPNN | 0.8983 | 0.0031 | Yes | this paper | Table 2 |
| GMN PPR ordering | 0.8991 | 0.0021 | Yes | this paper | Table 2 |
| GMN w/o PE | 0.9011 | 0.0025 | Yes | this paper | Table 2 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | this paper | Table 1 |
| GIN | 0.8539 | 0.0013 | Yes | this paper | Table 1 |
| Gated-GCN | 0.8557 | 0.0008 | Yes | this paper | Table 1 |
| NAGphormer | 0.8644 | 0.0003 | Yes | this paper | Table 1 |
| GPS | 0.8664 | 0.0011 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.8600 | 0.0014 | Yes | this paper | Table 1 |
| Exphormer | 0.8670 | 0.0003 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.8660 | 0.0007 | Yes | this paper | Table 1 |
| GMN | 0.8714 | 0.0012 | No | this paper | Table 1 |
| S4G | 0.8687 | 0.0002 | Yes | s4g | Table 2 |
| GRED | 0.8676 | 0.0200 | Yes | ding2023recurrent | Table 2 |

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table 1 |
| GIN | 0.5498 | 0.0079 | Yes | this paper | Table 1 |
| Gated-GCN | 0.5864 | 0.0077 | Yes | this paper | Table 1 |
| CRaWl | 0.6963 | 0.0079 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.6384 | 0.0121 | Yes | this paper | Table 1 |
| Graph ViT | 0.6855 | 0.0049 | Yes | this paper | Table 1 |
| GPS | 0.6575 | 0.0049 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.5854 | 0.0079 | Yes | this paper | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.6624 | 0.0079 | Yes | this paper | Table 1 |
| GMN- | 0.6860 | 0.0012 | Yes | this paper | Table 1 |
| GMN | 0.7071 | 0.0083 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| S4G | 0.7293 | 0.0004 | Yes | s4g | Table 2 |
| GRED | 0.7041 | 0.0049 | Yes | ding2023recurrent | Table 2 |
| GMN (Ours) | 0.7071 | 0.0083 | No | this paper | Table 2 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GIN | 0.3547 | 0.0045 | Yes | this paper | Table 1 |
| Gated-GCN | 0.3420 | 0.0013 | Yes | this paper | Table 1 |
| CRaWl | 0.2506 | 0.0022 | Yes | this paper | Table 1 |
| SAN+LapPE | 0.2683 | 0.0043 | Yes | this paper | Table 1 |
| Graph ViT | 0.2468 | 0.0015 | Yes | this paper | Table 1 |
| GPS | 0.2510 | 0.0015 | Yes | this paper | Table 1 |
| GPS (BigBird) | 0.2842 | 0.0130 | Yes | this paper | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.2518 | 0.0012 | Yes | this paper | Table 1 |
| GMN- | 0.2522 | 0.0035 | Yes | this paper | Table 1 |
| GMN | 0.2473 | 0.0025 | No | this paper | Table 1 |
| S4G | 0.2485 | 0.0017 | Yes | s4g | Table 2 |
| GRED | 0.2503 | 0.0019 | Yes | ding2023recurrent | Table 2 |
| GMN (Ours) | 0.2473 | 0.0025 | No | this paper | Table 2 |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 1 |
| Gated-GCN | 0.7731 | 0.0114 | Yes | this paper | Table 1 |
| NAGphormer | 0.7832 | 0.0095 | Yes | this paper | Table 1 |
| GPS | 0.8371 | 0.0048 | Yes | this paper | Table 1 |
| Exphormer | 0.8377 | 0.0078 | Yes | this paper | Table 1 |
| GOAT | 0.8311 | 0.0104 | Yes | this paper | Table 1 |
| GPS + Mamba | 0.8370 | 0.0105 | Yes | this paper | Table 1 |
| GMN | 0.8452 | 0.0021 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GIN** (from: Xu et al. 2019)
- **Gated-GCN** (from: Gilmer et al. 2017)
- **CRaWl** (from: Ahmad et al. 2021)
- **SAN+LapPE** (from: Ying et al. 2021 / Veličković et al. 2021)
- **NAGphormer** (from: Bouritsas et al. 2023)
- **Graph ViT** (from: Huang et al. 2022)
- **GPS** (from: Beaini et al. 2022)
- **GPS (BigBird)** (from: Beaini et al. 2022 / Zaheer et al. 2020)
- **Exphormer** (from: Fey et al. 2020)
- **GPS + Mamba** (from: Beaini et al. 2022 / Gu et al. 2021)
- **GMN-** (from: this paper (ablation))
- **S4G** (from: s4g)
- **GRED** (from: ding2023recurrent)
- **GOAT** (from: Chen et al. 2023)

## Extraction Notes

[COCO-SP] Extracted only COCO-SP F1 results as requested. All values are normalized to [0,1].
Standard deviations were parsed from the LaTeX subscripts. GMN is identified as the proposed model
as it achieves the best result (highlighted first) and is listed last in the block of advanced
models, typical for proposed methods in such tables. GMN- is treated as an ablation/baseline
variant. [PascalVOC-SP] failed: JSON parse error from 'qwen3.6-35b-a3b': could not extract valid
JSON [Peptides-func] Extracted AP results for Peptides-Func from Table 1 and Peptides-func from
Table 2. Note that Table 1 uses 'Peptides-Func' and Table 2 uses 'Peptides-func'. The GMN model
appears in both tables with identical values (0.7071 ± 0.0083). S4G and GRED results are cited from
external papers. NAGphormer has no result for Peptides-Func in Table 1. [Peptides-struct] Extracted
MAE results for Peptides-struct from Table 1 and Table 2. Note that GMN appears in both tables with
identical values (0.2473 ± 0.0025). Table 2 includes S4G and GRED results reported by other papers.
NAGphormer has no result for Peptides-struct in Table 1. All values are normalized to [0,1] range
where applicable (MAE is not percentage-based, so values remain as is). Higher is better is false
for MAE. [MNIST] Extracted MNIST Accuracy results from Table 1 and Table 2. Note that GMN appears in
both tables with identical values for MNIST. All other rows for MNIST were included. Values were
normalized to [0,1] range as they are percentages reported as decimals in the table (e.g., 0.9071).
Standard deviations were parsed from the subscript notation. [CIFAR10] Extracted CIFAR10 Accuracy
results from Table 1 and Table 2. Note that GMN appears in both tables with identical values. The
std for GRED in Table 2 is unusually high (0.6210), likely a typo in the original paper (possibly
meant 0.06210 or similar), but extracted exactly as written. All other values are standard.
[PATTERN] Extracted all PATTERN Accuracy results from Table 1 and Table 2. Note that GMN appears in
both tables with identical values; both are included as per instruction to include ALL rows. CRaWl
has no result for PATTERN in Table 1, so it is excluded from PATTERN results. S4G and GRED results
in Table 2 are cited from other papers. [MalNet-Tiny] Extracted only MalNet-Tiny results as
requested. The table provides Accuracy with standard deviation. GMN is identified as the proposed
model based on the context of the paper (GMN is the novel contribution). All other models are
baselines. Values are normalized to [0,1]. [Roman-empire] failed: JSON parse error from
'qwen3.6-35b-a3b': could not extract valid JSON [Amazon-ratings] Extracted all rows for Amazon-
ratings from Table 1 (Benchmark) and Table 2 (Ablation). Table 2 contains ablation variants of the
proposed GMN model, which are included as they represent specific model configurations reported in
the results. The primary metric Accuracy was used. Values were normalized to [0,1] range.
[Minesweeper] Extracted all rows for the 'Minesweeper' dataset from Table 1 (benchmark) and Table 2
(ablation). The primary metric ROC-AUC was used. Values are normalized to [0,1]. Standard deviations
are parsed from the underscore notation. GMN is identified as the proposed model based on the
ablation study context and highlighting. [Tolokers] Extracted all rows for the 'Tolokers' dataset
from Table 1. The metric is ROC-AUC. Values are normalized to [0,1]. Standard deviations are
extracted from the _{± ...} notation. GMN is identified as the proposed model as it achieves the
best result (highlighted first) and is listed last in the block of new methods.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*