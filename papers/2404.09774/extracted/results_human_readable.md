# Extraction: arXiv:2404.09774
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: RandAlign
- Type: GNN

## Results

### CIFAR10 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5571 | 0.0038 | Yes | Kipf 2016 | Table 2 |
| GCN + RandAlign | 0.5527 | 0.0016 | No | this paper | Table 1 |
| GAT | 0.6422 | 0.0046 | Yes | this paper | Table 1 |
| GAT + RandAlign | 0.6539 | 0.0007 | No | this paper | Table 1 |
| GatedGCN | 0.6731 | 0.0031 | Yes | this paper | Table 1 |
| GatedGCN + RandAlign | 0.7208 | 0.0015 | No | this paper | Table 1 |
| MoNet | 0.5465 | 0.0052 | Yes | Monti 2017 | Table 2 |
| GraphSAGE | 0.6577 | 0.0031 | Yes | Hamilton 2017 | Table 2 |
| GIN | 0.5525 | 0.0153 | Yes | Xu 2019 | Table 2 |
| GCNII | 0.5608 | 0.0020 | Yes | Chen 2020 | Table 2 |
| PNA | 0.7035 | 0.0063 | Yes | Corso 2020 | Table 2 |
| DGN | 0.7284 | 0.0042 | Yes | Beaini 2021 | Table 2 |
| CRaWl | 0.6901 | 0.0026 | Yes | Toenshoff 2021 | Table 2 |
| GIN-AK+ | 0.7219 | 0.0013 | Yes | Zhao 2021 | Table 2 |
| 3WLGNN | 0.5917 | 0.0159 | Yes | Maron 2019 | Table 2 |
| EGT | 0.6870 | 0.0041 | Yes | Hussain 2022 | Table 2 |
| GPS | 0.7230 | 0.0036 | Yes | Rampasek 2022 | Table 2 |
| GatedGCN + SSFG | 0.7194 | 0.0019 | Yes | Zhang 2022 | Table 2 |
| GAT-16 | 0.6422 | 0.0046 | Yes | Velickovic 2018 | Table 2 |
| GAT-16 + RandAlign | 0.6992 | 0.0008 | No | this paper | Table 2 |
| GatedGCN-16 | 0.6731 | 0.0031 | Yes | Bresson 2017 | Table 2 |
| GatedGCN-16 + RandAlign | 0.7640 | 0.0019 | No | this paper | Table 2 |
| GAT-8 w/o Lrn&Align | 0.6445 | 0.0030 | Yes | this paper | Table 4 |
| RandAlign w/o scaling (GAT-8) | 0.6621 | 0.0018 | No | this paper | Table 4 |
| RandAlign + scaling (GAT-8) | 0.6916 | 0.0044 | No | this paper | Table 4 |
| GatedGCN-8 w/o RandAlign | 0.6981 | 0.0042 | Yes | this paper | Table 4 |
| RandAlign w/o scaling (GatedGCN-8) | 0.7444 | 0.0015 | No | this paper | Table 4 |
| RandAlign + scaling (GatedGCN-8) | 0.7501 | 0.0018 | No | this paper | Table 4 |

### CLUSTER — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6850 | 0.0098 | Yes | Kipf 2016 | Table 1 |
| GraphSAGE | 0.6384 | 0.0011 | Yes | Hamilton 2017 | Table 1 |
| GIN | 0.6472 | 0.0155 | Yes | Xu 2019 | Table 1 |
| GAT | 0.7059 | 0.0045 | Yes | Velickovic 2018 | Table 1 |
| RingGNN | 0.4242 | 0.2006 | Yes | Chen 2019 | Table 1 |
| MoNet | 0.6641 | 0.0054 | Yes | Monti 2017 | Table 1 |
| GatedGCN | 0.7384 | 0.0033 | Yes | Bresson 2017 | Table 1 |
| K-Subgraph SAT | 0.7786 | 0.0010 | Yes | Chen 2022 | Table 1 |
| GatedGCN + SSFG | 0.7596 | 0.0002 | Yes | Zhang 2022 | Table 1 |
| SAN | 0.7669 | 0.0065 | Yes | Kreuzer 2021 | Table 1 |
| SAN + RandAlign | 0.7785 | 0.0007 | Yes | this paper | Table 1 |
| GPS | 0.7802 | 0.0018 | Yes | Rampasek 2022 | Table 1 |
| GPS + RandAlign | 0.7859 | 0.0005 | No | this paper | Table 1 |

### MNIST — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.9071 | 0.0022 | Yes | Kipf 2016 | Table 2 |
| GCN + RandAlign | 0.9031 | 0.0014 | No | this paper | Table 1 |
| GAT | 0.9554 | 0.0021 | Yes | Veličković 2018 | Table 1 |
| GAT + RandAlign | 0.9755 | 0.0003 | No | this paper | Table 2 |
| GatedGCN | 0.9734 | 0.0014 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + RandAlign | 0.9851 | 0.0003 | No | this paper | Table 2 |
| MoNet | 0.9081 | 0.0003 | Yes | Monti 2017 | Table 2 |
| GraphSAGE | 0.9731 | 0.0010 | Yes | Hamilton 2017 | Table 2 |
| GIN | 0.9648 | 0.0025 | Yes | Xu 2019 | Table 2 |
| GCNII | 0.9067 | 0.0014 | Yes | Chen 2020 | Table 2 |
| PNA | 0.9794 | 0.0012 | Yes | Corso 2020 | Table 2 |
| CRaWl | 0.9794 | 0.0005 | Yes | Toenshoff 2021 | Table 2 |
| 3WLGNN | 0.9507 | 0.0096 | Yes | Maron 2019 | Table 2 |
| EGT | 0.9817 | 0.0009 | Yes | Hussain 2022 | Table 2 |
| GPS | 0.9805 | 0.0013 | Yes | Rampásek 2022 | Table 2 |
| GatedGCN + SSFG | 0.9798 | 0.0003 | Yes | Zhang 2022 | Table 2 |
| GAT-8 + RandAlign (w/o scaling) | 0.9698 | 0.0002 | No | this paper | Table 4 |
| GatedGCN-8 + RandAlign (w/o scaling) | 0.9825 | 0.0002 | No | this paper | Table 4 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7189 | 0.0033 | Yes | Kipf 2017 | Table 2 |
| GraphSAGE | 0.5049 | 0.0000 | Yes | Hamilton 2017 | Table 2 |
| GIN | 0.8539 | 0.0014 | Yes | Xu 2019 | Table 2 |
| GAT | 0.7827 | 0.0019 | Yes | Velickovic 2018 | Table 2 |
| RingGNN | 0.8625 | 0.0001 | Yes | Chen 2019 | Table 2 |
| MoNet | 0.8558 | 0.0004 | Yes | Monti 2017 | Table 2 |
| GatedGCN | 0.8557 | 0.0009 | Yes | Bresson 2017 | Table 2 |
| DGN | 0.8668 | 0.0003 | Yes | Beaini 2021 | Table 2 |
| K-Subgraph SAT | 0.8685 | 0.0004 | Yes | Chen 2022 | Table 2 |
| GatedGCN + SSFG | 0.8572 | 0.0007 | Yes | Zhang 2022 | Table 2 |
| SAN | 0.8658 | 0.0004 | Yes | Kreuzer 2021 | Table 2 |
| SAN + RandAlign | 0.8677 | 0.0007 | No | this paper | Table 2 |
| GPS | 0.8669 | 0.0006 | Yes | Rampasek 2022 | Table 2 |
| GPS + RandAlign | 0.8686 | 0.0001 | No | this paper | Table 2 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1268 | 0.0060 | Yes | Kipf 2016 | Table 1 |
| GINE | 0.1265 | 0.0076 | Yes | Hu 2019 | Table 1 |
| GatedGCN | 0.2873 | 0.0219 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + RWSE | 0.2860 | 0.0085 | Yes | Dwivedi 2021 | Table 1 |
| Transformer + LapPE | 0.2694 | 0.0098 | Yes | Dwivedi 2022 | Table 1 |
| SAN + LapPE | 0.3230 | 0.0039 | Yes | Dwivedi 2022 | Table 1 |
| SAN + RWSE | 0.3216 | 0.0027 | Yes | Dwivedi 2022 | Table 1 |
| GPS | 0.3748 | 0.0109 | Yes | Rampasek 2022 | Table 1 |
| GPS + RandAlign | 0.4288 | 0.0062 | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | Kipf 2016 | Table 1 |
| GINE | 0.5498 | 0.0079 | Yes | Hu 2019 | Table 1 |
| GatedGCN | 0.5864 | 0.0077 | Yes | Bresson 2017 | Table 1 |
| GatedGCN + RWSE | 0.6069 | 0.0035 | Yes | Dwivedi 2021 | Table 1 |
| Transformer + LapPE | 0.6326 | 0.0126 | Yes | Dwivedi 2022 | Table 1 |
| SAN + LapPE | 0.6384 | 0.0121 | Yes | Dwivedi 2022 | Table 1 |
| SAN + RWSE | 0.6439 | 0.0075 | Yes | Dwivedi 2022 | Table 1 |
| GPS | 0.6535 | 0.0041 | Yes | Rampasek 2022 | Table 1 |
| GPS + RandAlign | 0.6630 | 0.0005 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7599 | 0.0119 | Yes | Kipf 2016 | Table 1 |
| GIN | 0.7707 | 0.0149 | Yes | Xu 2019 | Table 1 |
| PNA | 0.7905 | 0.0132 | Yes | Corso 2020 | Table 1 |
| DeeperGCN | 0.7858 | 0.0117 | Yes | Li 2020 | Table 1 |
| DGN | 0.7970 | 0.0097 | Yes | Beaini 2021 | Table 1 |
| ExpC | 0.7799 | 0.0082 | Yes | Yang 2022 | Table 1 |
| GIN-AK+ | 0.7961 | 0.0119 | Yes | Zhao 2022 | Table 1 |
| SAN | 0.7785 | 0.2470 | Yes | Kreuzer 2021 | Table 1 |
| GPS | 0.7880 | 0.0101 | Yes | Rampasek 2022 | Table 1 |
| GPS + RandAlign | 0.8021 | 0.0305 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **GAT** (from: Veličković 2018)
- **GatedGCN** (from: Bresson 2017)
- **EGT** (from: Hussain 2022)
- **GPS** (from: Rampásek 2022)
- **MoNet** (from: Monti 2017)
- **GraphSAGE** (from: Hamilton 2017)
- **GIN** (from: Xu 2019)
- **GCNII** (from: Chen 2020)
- **PNA** (from: Corso 2020)
- **CRaWl** (from: Toenshoff 2021)
- **3WLGNN** (from: Maron 2019)
- **GatedGCN + SSFG** (from: Zhang 2022)
- **DGN** (from: Beaini 2021)
- **GIN-AK+** (from: Zhao 2021)
- **GINE** (from: Hu 2019)
- **GatedGCN + RWSE** (from: Dwivedi 2021)
- **Transformer + LapPE** (from: Dwivedi 2022)
- **SAN + LapPE** (from: Dwivedi 2022)
- **SAN + RWSE** (from: Dwivedi 2022)
- **RingGNN** (from: Chen 2019)
- **K-Subgraph SAT** (from: Chen 2022)
- **SAN** (from: Kreuzer 2021)
- **SAN + RandAlign** (from: this paper)
- **DeeperGCN** (from: Li 2020)
- **ExpC** (from: Yang 2022)

## Extraction Notes

[MNIST] Extracted only MNIST results. Focused on Accuracy metric. Included results from Table 1
(base models + RandAlign variants), Table 2 (comparison with previous methods), and Table 4
(ablation on scaling). Note: Table 1 reports GCN+RandAlign 16-layer result as 94.051%, but Table 2
reports GAT-16+RandAlign as 97.553% and GatedGCN-16+RandAlign as 98.512%. The text states 'Our model
achieves 0.337% improved performance compared with EGT (98.173%)', which aligns with the 98.512%
value in Table 2 for GatedGCN-16+RandAlign. Table 1's GCN+RandAlign 16-layer value (94.051%) seems
lower than the 90.305% for 4 layers, which might be a typo in the paper or specific to that
configuration, but I extracted the values as written. Table 2 provides the most comprehensive
comparison for the 'proposed' method (GatedGCN-16+RandAlign) against SOTA. I included all distinct
model configurations reported for MNIST. [CIFAR10] Extracted all CIFAR10 results from Table 1, Table
2, and Table 4. Table 3 was ignored as it contained training accuracy and parameter counts, not test
accuracy. Values were converted from percentages to decimals. Standard deviations were parsed from
the 'mean ± std' format. The proposed model is RandAlign, applied on top of various baselines (GCN,
GAT, GatedGCN) with different layer counts (4, 8, 16). Table 4 shows ablation studies for RandAlign
variants. [PascalVOC-SP] Extracted all rows from Table 1 (comp-voc) for the PascalVOC-SP dataset.
The metric is F1 (implied by context of classification task and standard reporting, though table
header just says 'PascalVOC-SP', the values and context of 'superpixel graph classification' confirm
it is a classification metric, likely F1 or Accuracy; given the focus instruction asks for F1 and
values are low, F1 is the standard metric for this dataset in LRGB benchmarks). All values are
normalized to [0,1]. Standard deviations are parsed from the ± notation. [PATTERN] Extracted results
for the PATTERN dataset from Table 2 (labeled table:cluster). The table provides Accuracy values for
multiple models. The proposed model is identified as 'GPS + RandAlign' based on the text claiming it
advances the state of the art. 'SAN + RandAlign' is also included as a variant of the proposed
method. Values were converted from percentages to [0,1] range. Standard deviations were parsed from
the 'mean ± std' format. [CLUSTER] Extracted only CLUSTER dataset results as requested. DGN was
skipped as it has no result for CLUSTER ('--'). All values normalized to [0,1] range. Metric is
Accuracy. [Peptides-func] Extracted all rows from Table 1 (labeled table:Peptides-struct in the
paper) for the Peptides-func dataset. The proposed model is identified as 'GPS + RandAlign' based on
the text description and bold formatting in the table. All values are normalized to [0,1] as they
represent AP scores. Standard deviations were parsed from the '±' notation. [ogbg-molhiv] Extracted
all rows from Table 1 for the ogbg-molhiv dataset. The proposed model is 'GPS + RandAlign'. All
values are ROC-AUC scores normalized to [0,1]. Standard deviations are parsed from the 'value ± std'
format. No other datasets were present in the provided text.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*