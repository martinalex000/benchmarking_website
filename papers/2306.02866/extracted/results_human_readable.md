# Extraction: arXiv:2306.02866
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: MLP-PS (Ours)
- Type: GNN

## Results

### EXP — EXP ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 600.0000 | — | Yes | this paper | Table 1 |
| GAT | 600.0000 | — | Yes | this paper | Table 1 |
| GIN | 600.0000 | — | Yes | this paper | Table 1 |
| ChebNet | 71.0000 | — | Yes | this paper | Table 1 |
| PPGN | 0.0000 | — | Yes | this paper | Table 1 |
| GNNML3 | 0.0000 | — | Yes | this paper | Table 1 |
| MLP-GA | 0.0000 | — | Yes | this paper | Table 1 |
| MLP-FA | 0.0000 | — | Yes | this paper | Table 1 |
| MLP-Canonical. | 0.0000 | — | Yes | this paper | Table 1 |
| MLP-PS (Ours), fixed epsilon | 0.0000 | — | No | this paper | Table 1 |
| MLP-PS (Ours) | 0.0000 | — | No | this paper | Table 1 |
| GIN-ID-GA | 0.0000 | — | Yes | this paper | Table 2 |
| GIN-ID-FA | 0.0000 | — | Yes | this paper | Table 2 |
| GIN-ID-Canonical. | 0.0000 | — | Yes | this paper | Table 2 |
| GIN-ID-PS (Ours) | 0.0000 | — | No | this paper | Table 2 |

### EXP-classify — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5000 | — | Yes | Kipf 2017 | Table 1 |
| GAT | 0.5000 | — | Yes | Veličković 2018 | Table 1 |
| GIN | 0.5000 | — | Yes | Xu 2019 | Table 1 |
| ChebNet | 0.8200 | — | Yes | Defferrard 2016 | Table 1 |
| PPGN | 1.0000 | — | Yes | Maron 2019 | Table 1 |
| GNNML3 | 1.0000 | — | Yes | Balcilar 2021 | Table 1 |
| MLP-GA | 0.5000 | — | Yes | Yarotsky 2018 | Table 1 |
| MLP-FA | 1.0000 | — | Yes | Puny 2022 | Table 1 |
| MLP-Canonical. | 0.5000 | — | Yes | this paper | Table 1 |
| MLP-PS (Ours), fixed epsilon | 0.7950 | — | Yes | this paper | Table 1 |
| MLP-PS (Ours) | 1.0000 | — | No | this paper | Table 1 |
| GIN-ID-GA | 0.5000 | — | Yes | Puny 2022 | Table 2 |
| GIN-ID-FA | 1.0000 | — | Yes | Puny 2022 | Table 2 |
| GIN-ID-Canonical. | 0.8400 | — | Yes | this paper | Table 2 |
| GIN-ID-PS (Ours) | 1.0000 | — | No | this paper | Table 2 |

### GRAPH8c — GRAPH8c ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 4755.0000 | — | Yes | Kipf 2017 | Table 1 |
| GAT | 1828.0000 | — | Yes | Velickovic 2018 | Table 1 |
| GIN | 386.0000 | — | Yes | Xu 2019 | Table 1 |
| ChebNet | 44.0000 | — | Yes | Defferrard 2016 | Table 1 |
| PPGN | 0.0000 | — | Yes | Maron 2019 | Table 1 |
| GNNML3 | 0.0000 | — | Yes | Balcilar 2021 | Table 1 |
| MLP-GA | 0.0000 | — | Yes | Yarotsky 2018 | Table 1 |
| MLP-FA | 0.0000 | — | Yes | Puny 2022 | Table 1 |
| MLP-Canonical | 0.0000 | — | Yes | this paper | Table 1 |
| MLP-PS (Ours), fixed epsilon | 0.0000 | — | No | this paper | Table 1 |
| MLP-PS (Ours) | 0.0000 | — | No | this paper | Table 1 |
| GIN-ID-GA | 0.0000 | — | Yes | Puny 2022 | Table 2 |
| GIN-ID-FA | 0.0000 | — | Yes | Puny 2022 | Table 2 |
| GIN-ID-Canonical | 0.0000 | — | Yes | this paper | Table 2 |
| GIN-ID-PS (Ours) | 0.0000 | — | No | this paper | Table 2 |

### PATTERN — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN, 16 layers | 0.8561 | — | Yes | Kipf 2017 | Table 1 |
| GAT, 16 layers | 0.7827 | — | Yes | Velickovic 2018 | Table 1 |
| GatedGCN, 16 layers | 0.8557 | — | Yes | Bresson 2017 | Table 1 |
| GIN, 16 layers | 0.8539 | — | Yes | Xu 2019 | Table 1 |
| RingGNN, 2 layers | 0.8625 | — | Yes | Chen 2019 | Table 1 |
| PPGN, 3 layers | 0.8566 | — | Yes | Maron 2019 | Table 1 |
| ViT-GA, 1-sample | 0.7696 | 0.0003 | Yes | this paper | Table 1 |
| ViT-GA, 10-sample | 0.8322 | 0.0006 | Yes | this paper | Table 1 |
| ViT-FA | 0.7138 | — | Yes | this paper | Table 1 |
| ViT-Canonical | 0.8582 | — | Yes | this paper | Table 1 |
| ViT-PS (Ours), 1-sample | 0.8587 | 0.0002 | No | this paper | Table 1 |
| ViT-PS (Ours), 10-sample | 0.8599 | 0.0001 | No | this paper | Table 1 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | — | Yes | Kipf 2017 | Table 1 |
| GCNII | 0.3161 | — | Yes | Chen 2020 | Table 1 |
| GINE | 0.3180 | — | Yes | Hu 2020 | Table 1 |
| GatedGCN | 0.3218 | — | Yes | Bresson 2017 | Table 1 |
| GatedGCN+RWSE | 0.3242 | — | Yes | Bresson 2017 | Table 1 |
| Transformer+LapPE | 0.3174 | — | Yes | Dwivedi 2022 | Table 1 |
| SAN+LapPE | 0.3350 | — | Yes | Kreuzer 2021 | Table 1 |
| SAN+RWSE | 0.3341 | — | Yes | Kreuzer 2021 | Table 1 |
| GraphGPS | 0.3337 | — | Yes | Rampasek 2022 | Table 1 |
| Exphormer | 0.3637 | — | Yes | Shirzad 2023 | Table 1 |
| ViT-PS | 0.5341 | — | No | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | — | Yes | Kipf 2017 | Table 1 |
| GCNII | 0.5543 | — | Yes | Chen 2020 | Table 1 |
| GINE | 0.5498 | — | Yes | Hu 2020 | Table 1 |
| GatedGCN | 0.5864 | — | Yes | Bresson 2017 | Table 1 |
| GatedGCN+RWSE | 0.6069 | — | Yes | Bresson 2017 | Table 1 |
| Transformer+LapPE | 0.6326 | — | Yes | Dwivedi 2022 | Table 1 |
| SAN+LapPE | 0.6384 | — | Yes | Kreuzer 2021 | Table 1 |
| SAN+RWSE | 0.6439 | — | Yes | Kreuzer 2021 | Table 1 |
| GraphGPS | 0.6535 | — | Yes | Rampasek 2022 | Table 1 |
| Exphormer | 0.6527 | — | Yes | Shirzad 2023 | Table 1 |
| ViT-PS | 0.6575 | — | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | — | Yes | Kipf 2017 | Table 1 |
| GCNII | 0.3471 | — | Yes | Chen 2020 | Table 1 |
| GINE | 0.3547 | — | Yes | Hu 2020 | Table 1 |
| GatedGCN | 0.3420 | — | Yes | Bresson 2017 | Table 1 |
| GatedGCN+RWSE | 0.3357 | — | Yes | Bresson 2017 | Table 1 |
| Transformer+LapPE | 0.2529 | — | Yes | Dwivedi 2022 | Table 1 |
| SAN+LapPE | 0.2683 | — | Yes | Kreuzer 2021 | Table 1 |
| SAN+RWSE | 0.2545 | — | Yes | Kreuzer 2021 | Table 1 |
| GraphGPS | 0.2500 | — | Yes | Rampasek 2022 | Table 1 |
| Exphormer | 0.2481 | — | Yes | Shirzad 2023 | Table 1 |
| ViT-PS (Ours) | 0.2559 | — | No | this paper | Table 1 |

### n-body — MSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SE(3) Transformer | 0.0244 | — | Yes | Fuchs et al. 2020 | Table 1 |
| TFN | 0.0155 | — | Yes | Thomas et al. 2018 | Table 1 |
| Radial Field | 0.0104 | — | Yes | Kohler et al. 2019 | Table 1 |
| EGNN | 0.0071 | — | Yes | Satorras et al. 2021 | Table 1 |
| GNN-FA | 0.0057 | — | Yes | Puny et al. 2022 | Table 1 |
| GNN-Canonical | 0.0043 | — | Yes | Kaba et al. 2022 | Table 1 |
| Transformer-Canonical | 0.0051 | — | Yes | this paper | Table 1 |
| Transformer-GA | 0.0041 | 0.0000 | Yes | this paper | Table 1 |
| Transformer-PS | 0.0040 | 0.0000 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2017)
- **GAT** (from: Velickovic 2018)
- **GIN** (from: Xu 2019)
- **ChebNet** (from: Defferrard 2016)
- **PPGN** (from: Maron 2019)
- **GNNML3** (from: Balcilar 2021)
- **MLP-GA** (from: Yarotsky 2018)
- **MLP-FA** (from: Puny 2022)
- **MLP-Canonical** (from: this paper)
- **GIN-ID-GA** (from: Puny 2022)
- **GIN-ID-FA** (from: Puny 2022)
- **GIN-ID-Canonical** (from: this paper)
- **MLP-Canonical.** (from: Kaba et al. 2022)
- **GIN-ID-Canonical.** (from: Kaba et al. 2022)
- **MLP-PS (Ours), fixed epsilon** (from: this paper)
- **GIN-ID-PS (Ours)** (from: this paper)
- **SE(3) Transformer** (from: Fuchs et al. 2020)
- **TFN** (from: Thomas et al. 2018)
- **Radial Field** (from: Kohler et al. 2019)
- **EGNN** (from: Satorras et al. 2021)
- **GNN-FA** (from: Puny et al. 2022)
- **GNN-Canonical** (from: Kaba et al. 2022)
- **Transformer-Canonical** (from: this paper)
- **Transformer-GA** (from: this paper)
- **GatedGCN** (from: Bresson 2017)
- **RingGNN** (from: Chen 2019)
- **ViT-GA** (from: this paper)
- **ViT-FA** (from: this paper)
- **ViT-Canonical** (from: this paper)
- **GCNII** (from: Chen 2020)
- **GINE** (from: Hu 2020)
- **GatedGCN+RWSE** (from: Bresson 2017)
- **Transformer+LapPE** (from: Dwivedi 2022)
- **SAN+LapPE** (from: Kreuzer 2021)
- **SAN+RWSE** (from: Kreuzer 2021)
- **GraphGPS** (from: Rampasek 2022)
- **Exphormer** (from: Shirzad 2023)

## Extraction Notes

[GRAPH8c] Extracted all rows from Table 1 and Table 2 corresponding to the GRAPH8c metric. The
metric is a count of pairs of graphs not separated by the model, where lower is better (indicated by
down arrow in table). Values are integers. Standard deviation is not reported for GRAPH8c results.
The proposed model 'MLP-PS (Ours)' appears in Table 1. A variant 'GIN-ID-PS (Ours)' appears in Table
2. Both are included as they are variants of the proposed approach/methodology. [EXP] Extracted
results for the 'EXP' dataset from Table 1 and Table 2. The metric 'EXP' refers to the number of
pairs of graphs not separated by the model (lower is better). The table also contains 'EXP-classify'
results, but per instructions, only the primary metric 'EXP' was extracted. Note that 'MLP-PS
(Ours), fixed epsilon' is a variant of the proposed model, included as it appears in the main
results table. [EXP-classify] Extracted results for EXP-classify from Table 1 and Table 2. Table 2
contains supplementary results for a specific variant (GIN-ID base function), but since the prompt
asks for standard/default configuration and these are distinct models (GIN-ID vs MLP) presented in
the same context of EXP-classify results, they are included. The primary metric Accuracy is
extracted from the 'EXP-classify' column. Values are converted from percentages to [0,1] range.
[n-body] Extracted all rows from Table 1 for the n-body dataset. The metric is Position MSE. Values
are normalized to [0, 1] range implicitly as they are small errors. Standard deviations are included
where reported. Baselines sourced from citations or 'this paper' as indicated in the table caption.
[PATTERN] Extracted all rows from Table 1 for the PATTERN dataset. Note that the table includes
multiple configurations (pretrained vs not, 1-sample vs 10-sample). The prompt asked for
STANDARD/DEFAULT configuration. Usually, 'default' implies no external pre-training (ImageNet) and
often the primary sampling method. However, since the table presents them as distinct rows and the
'best' result is highlighted, I extracted all rows to be safe, as 'standard' is ambiguous here
(could mean no pretrain, or could mean the main proposed method). The values are percentages divided
by 100. Standard deviations are small and correctly parsed. Diverged results were skipped.
[Peptides-func] Extracted only the 'Peptides-func' column as requested. The table provides single
values without standard deviations, so std is null. All values are normalized to [0,1] range as they
represent AP (Average Precision). The proposed model is identified as 'ViT-PS (Ours)'. [Peptides-
struct] Extracted only Peptides-struct MAE results as requested. All values are test performance at
best validation performance. No standard deviations reported in the table. [PCQM-Contact] Extracted
only the MRR metric for PCQM-Contact as requested. All other metrics (Hits@1, Hits@3, Hits@10) and
other datasets (Peptides-func, Peptides-struct) were ignored. No standard deviations were reported
in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*