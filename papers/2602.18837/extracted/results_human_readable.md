# Extraction: L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: Ours
- Type: GNN

## Results

### Amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | this paper | Table 9 |
| GAT | 0.4909 | 0.0063 | Yes | this paper | Table 9 |
| GAT (LapPE) | 0.4490 | 0.0073 | Yes | this paper | Table 9 |
| GAT (RWSE) | 0.4858 | 0.0041 | Yes | this paper | Table 9 |
| Gated-GCN | 0.4300 | 0.0032 | Yes | this paper | Table 9 |
| GCN (LapPE) | 0.4435 | 0.0036 | Yes | this paper | Table 9 |
| GCN (RWSE) | 0.4640 | 0.0055 | Yes | this paper | Table 9 |
| CO-GNN ($\Sigma,\Sigma$) | 0.5128 | 0.0056 | Yes | this paper | Table 9 |
| CO-GNN ($\mu,\mu$) | 0.5417 | 0.0037 | Yes | this paper | Table 9 |
| SAGE | 0.5363 | 0.0039 | Yes | this paper | Table 9 |
| Exphormer | 0.5351 | 0.0046 | Yes | this paper | Table 9 |
| NAGphormer | 0.5126 | 0.0072 | Yes | this paper | Table 9 |
| GOAT | 0.4461 | 0.0050 | Yes | this paper | Table 9 |
| GPS | 0.5310 | 0.0042 | Yes | this paper | Table 9 |
| GPSGCN+Performer (LapPE) | 0.4820 | 0.0067 | Yes | this paper | Table 9 |
| GPSGCN+Performer (RWSE) | 0.4808 | 0.0085 | Yes | this paper | Table 9 |
| GT | 0.5117 | 0.0066 | Yes | this paper | Table 9 |
| GT-sep | 0.5218 | 0.0080 | Yes | this paper | Table 9 |
| Polynormer | 0.5481 | 0.0049 | Yes | this paper | Table 9 |
| CPGNN | 0.3979 | 0.0077 | Yes | this paper | Table 9 |
| FAGCN | 0.4412 | 0.0030 | Yes | this paper | Table 9 |
| FSGNN | 0.5274 | 0.0083 | Yes | this paper | Table 9 |
| GBK-GNN | 0.4598 | 0.0071 | Yes | this paper | Table 9 |
| GloGNN | 0.3689 | 0.0014 | Yes | this paper | Table 9 |
| GPR-GNN | 0.4488 | 0.0034 | Yes | this paper | Table 9 |
| H2GCN | 0.3647 | 0.0023 | Yes | this paper | Table 9 |
| JacobiConv | 0.4355 | 0.0048 | Yes | this paper | Table 9 |
| GMN | 0.5407 | 0.0031 | Yes | this paper | Table 9 |
| GPS + Mamba | 0.4513 | 0.0097 | Yes | this paper | Table 9 |
| GRAMA | 0.5348 | 0.0062 | Yes | this paper | Table 9 |
| MP-SSM | 0.5365 | 0.0071 | Yes | this paper | Table 9 |
| Stable-ChebNet | 0.5315 | 0.0021 | Yes | this paper | Table 9 |
| Ours | 0.5341 | 0.0134 | No | this paper | Table 9 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | this paper | Table 9 |
| CO-GNN ($\Sigma,\Sigma$) | 0.9509 | 0.0118 | Yes | this paper | Table 9 |
| CO-GNN ($\mu,\mu$) | 0.9731 | 0.0041 | Yes | this paper | Table 9 |
| SAGE | 0.9351 | 0.0057 | Yes | this paper | Table 9 |
| GAT | 0.9201 | 0.0068 | Yes | this paper | Table 9 |
| GAT (LapPE) | 0.9350 | 0.0054 | Yes | this paper | Table 9 |
| GAT (RWSE) | 0.9253 | 0.0065 | Yes | this paper | Table 9 |
| Gated-GCN | 0.8754 | 0.0122 | Yes | this paper | Table 9 |
| GCN (LapPE) | 0.9426 | 0.0049 | Yes | this paper | Table 9 |
| GCN (RWSE) | 0.9384 | 0.0048 | Yes | this paper | Table 9 |
| Exphormer | 0.9074 | 0.0053 | Yes | this paper | Table 9 |
| NAGphormer | 0.8419 | 0.0066 | Yes | this paper | Table 9 |
| GOAT | 0.8109 | 0.0102 | Yes | this paper | Table 9 |
| GPS | 0.9063 | 0.0067 | Yes | this paper | Table 9 |
| GPSGCN+Performer (LapPE) | 0.9385 | 0.0041 | Yes | this paper | Table 9 |
| GPSGCN+Performer (RWSE) | 0.9288 | 0.0050 | Yes | this paper | Table 9 |
| GPSGCN+Transformer (LapPE) | 0.9182 | 0.0041 | Yes | this paper | Table 9 |
| GPSGCN+Transformer (RWSE) | 0.9117 | 0.0051 | Yes | this paper | Table 9 |
| GT | 0.9185 | 0.0076 | Yes | this paper | Table 9 |
| GT-sep | 0.9229 | 0.0047 | Yes | this paper | Table 9 |
| Polynormer | 0.9746 | 0.0036 | Yes | this paper | Table 9 |
| CPGNN | 0.5203 | 0.0546 | Yes | this paper | Table 9 |
| FAGCN | 0.8817 | 0.0073 | Yes | this paper | Table 9 |
| FSGNN | 0.9008 | 0.0070 | Yes | this paper | Table 9 |
| GBK-GNN | 0.9085 | 0.0058 | Yes | this paper | Table 9 |
| GloGNN | 0.5108 | 0.0123 | Yes | this paper | Table 9 |
| GPR-GNN | 0.8624 | 0.0061 | Yes | this paper | Table 9 |
| H2GCN | 0.8971 | 0.0031 | Yes | this paper | Table 9 |
| JacobiConv | 0.8966 | 0.0040 | Yes | this paper | Table 9 |
| GMN | 0.9101 | 0.0023 | Yes | this paper | Table 9 |
| GPS + Mamba | 0.8993 | 0.0054 | Yes | this paper | Table 9 |
| GRAMA$_{GCN}$ | 0.9527 | 0.0071 | Yes | this paper | Table 9 |
| MP-SSM | 0.9533 | 0.0072 | Yes | this paper | Table 9 |
| Stable-ChebNet | 0.9571 | 0.0226 | Yes | this paper | Table 9 |
| Ours | 0.9750 | 0.0026 | No | this paper | Table 9 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | this paper | Table 9 |
| GAT | 0.8087 | 0.0030 | Yes | this paper | Table 9 |
| GAT (LapPE) | 0.8480 | 0.0046 | Yes | this paper | Table 9 |
| GAT (RWSE) | 0.8662 | 0.0053 | Yes | this paper | Table 9 |
| Gated-GCN | 0.7446 | 0.0054 | Yes | this paper | Table 9 |
| GCN (LapPE) | 0.8337 | 0.0055 | Yes | this paper | Table 9 |
| GCN (RWSE) | 0.8484 | 0.0055 | Yes | this paper | Table 9 |
| CO-GNN ($\Sigma,\Sigma$) | 0.9157 | 0.0032 | Yes | this paper | Table 9 |
| CO-GNN ($\mu,\mu$) | 0.9137 | 0.0035 | Yes | this paper | Table 9 |
| SAGE | 0.8574 | 0.0067 | Yes | this paper | Table 9 |
| Exphormer | 0.8903 | 0.0037 | Yes | this paper | Table 9 |
| NAGphormer | 0.7434 | 0.0077 | Yes | this paper | Table 9 |
| GOAT | 0.7159 | 0.0125 | Yes | this paper | Table 9 |
| GPS | 0.8200 | 0.0061 | Yes | this paper | Table 9 |
| GPSGCN+Performer (LapPE) | 0.8396 | 0.0053 | Yes | this paper | Table 9 |
| GPSGCN+Performer (RWSE) | 0.8472 | 0.0065 | Yes | this paper | Table 9 |
| GT | 0.8651 | 0.0073 | Yes | this paper | Table 9 |
| GT-sep | 0.8732 | 0.0039 | Yes | this paper | Table 9 |
| Polynormer | 0.9255 | 0.0030 | Yes | this paper | Table 9 |
| CPGNN | 0.6396 | 0.0062 | Yes | this paper | Table 9 |
| FAGCN | 0.6522 | 0.0056 | Yes | this paper | Table 9 |
| FSGNN | 0.7992 | 0.0056 | Yes | this paper | Table 9 |
| GBK-GNN | 0.7457 | 0.0047 | Yes | this paper | Table 9 |
| GloGNN | 0.5963 | 0.0069 | Yes | this paper | Table 9 |
| GPR-GNN | 0.6485 | 0.0027 | Yes | this paper | Table 9 |
| H2GCN | 0.6011 | 0.0052 | Yes | this paper | Table 9 |
| JacobiConv | 0.7114 | 0.0042 | Yes | this paper | Table 9 |
| GMN | 0.8769 | 0.0050 | Yes | this paper | Table 9 |
| GPS + Mamba | 0.8310 | 0.0028 | Yes | this paper | Table 9 |
| GRAMA | 0.8861 | 0.0043 | Yes | this paper | Table 9 |
| MP-SSM | 0.9091 | 0.0048 | Yes | this paper | Table 9 |
| Stable-ChebNet | 0.9203 | 0.0085 | Yes | this paper | Table 9 |
| Ours | 0.9212 | 0.0112 | No | this paper | Table 9 |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | this paper | Table 9 |
| CO-GNN ($\Sigma,\Sigma$) | 0.8336 | 0.0089 | Yes | this paper | Table 9 |
| CO-GNN ($\mu,\mu$) | 0.8445 | 0.0117 | Yes | this paper | Table 9 |
| Polynormer | 0.8591 | 0.0074 | Yes | this paper | Table 9 |
| MP-SSM | 0.8526 | 0.0093 | Yes | this paper | Table 9 |
| Stable-ChebNet | 0.8555 | 0.0335 | Yes | this paper | Table 9 |
| Ours | 0.8557 | 0.0061 | No | this paper | Table 9 |
| GAT | 0.8370 | 0.0047 | Yes | this paper | Table 9 |
| GAT (LapPE) | 0.8499 | 0.0054 | Yes | this paper | Table 9 |
| GAT (RWSE) | 0.8502 | 0.0067 | Yes | this paper | Table 9 |
| Gated-GCN | 0.7731 | 0.0114 | Yes | this paper | Table 9 |
| GCN (LapPE) | 0.8495 | 0.0078 | Yes | this paper | Table 9 |
| GCN (RWSE) | 0.8511 | 0.0077 | Yes | this paper | Table 9 |
| SAGE | 0.8243 | 0.0044 | Yes | this paper | Table 9 |
| Exphormer | 0.8377 | 0.0078 | Yes | this paper | Table 9 |
| NAGphormer | 0.7832 | 0.0095 | Yes | this paper | Table 9 |
| GOAT | 0.8311 | 0.0104 | Yes | this paper | Table 9 |
| GPS | 0.8371 | 0.0048 | Yes | this paper | Table 9 |
| GPSGCN+Performer (LapPE) | 0.8472 | 0.0077 | Yes | this paper | Table 9 |
| GPSGCN+Performer (RWSE) | 0.8481 | 0.0086 | Yes | this paper | Table 9 |
| GPSGCN+Transformer (LapPE) | 0.8351 | 0.0093 | Yes | this paper | Table 9 |
| GPSGCN+Transformer (RWSE) | 0.8353 | 0.0106 | Yes | this paper | Table 9 |
| GT | 0.8323 | 0.0064 | Yes | this paper | Table 9 |
| GT-sep | 0.8252 | 0.0092 | Yes | this paper | Table 9 |
| CPGNN | 0.7336 | 0.0101 | Yes | this paper | Table 9 |
| FAGCN | 0.7775 | 0.0105 | Yes | this paper | Table 9 |
| FSGNN | 0.8276 | 0.0061 | Yes | this paper | Table 9 |
| GBK-GNN | 0.8101 | 0.0067 | Yes | this paper | Table 9 |
| GloGNN | 0.7339 | 0.0117 | Yes | this paper | Table 9 |
| GPR-GNN | 0.7294 | 0.0097 | Yes | this paper | Table 9 |
| H2GCN | 0.7335 | 0.0101 | Yes | this paper | Table 9 |
| JacobiConv | 0.6866 | 0.0065 | Yes | this paper | Table 9 |
| GMN | 0.8452 | 0.0021 | Yes | this paper | Table 9 |
| GPS + Mamba | 0.8370 | 0.0105 | Yes | this paper | Table 9 |
| GRAMA_GCN | 0.8623 | 0.0110 | Yes | this paper | Table 9 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GAT (LapPE)** (from: this paper)
- **GAT (RWSE)** (from: this paper)
- **Gated-GCN** (from: Bresson & Laurent 2017)
- **GCN (LapPE)** (from: this paper)
- **GCN (RWSE)** (from: this paper)
- **CO-GNN** (from: Platonov et al. 2023)
- **SAGE** (from: Hamilton et al. 2017)
- **Exphormer** (from: Ying et al. 2021)
- **NAGphormer** (from: Beaini et al. 2021)
- **GOAT** (from: this paper)
- **GPS** (from: You et al. 2021)
- **GPSGCN+Performer (LapPE)** (from: this paper)
- **GPSGCN+Performer (RWSE)** (from: this paper)
- **GPSGCN+Transformer (LapPE)** (from: this paper)
- **GPSGCN+Transformer (RWSE)** (from: this paper)
- **GT** (from: Ying et al. 2021)
- **GT-sep** (from: this paper)
- **Polynormer** (from: this paper)
- **CPGNN** (from: Zhu et al. 2020)
- **FAGCN** (from: Bo et al. 2020)
- **FSGNN** (from: this paper)
- **GBK-GNN** (from: this paper)
- **GloGNN** (from: this paper)
- **GPR-GNN** (from: Wang et al. 2020)
- **H2GCN** (from: Zhu et al. 2020)
- **JacobiConv** (from: this paper)
- **GMN** (from: this paper)
- **GPS + Mamba** (from: this paper)
- **GRAMA** (from: this paper)
- **MP-SSM** (from: this paper)
- **Stable-ChebNet** (from: this paper)
- **St-ChebNet** (from: Platonov et al. 2023)
- **CO-GNN ($\Sigma,\Sigma$)**
- **CO-GNN ($\mu,\mu$)**
- **GRAMA$_{GCN}$**
- **GRAMA_GCN** (from: Platonov et al. 2023)

## Extraction Notes

[Roman-empire] Extracted only Roman-empire results from Table 9. Table 1 was ignored as it contains
aggregated or different formatting results, and Table 9 is the comprehensive source. Values were
converted from percentages to [0,1] range. Standard deviations were parsed from the 'mean ± std'
format. OOM results were skipped. [Amazon-ratings] Extracted results for Amazon-ratings from Table
9. Values are percentages from the paper, converted to [0,1] range. Standard deviations are also
converted. Table 1 was ignored as it contains aggregated or different formatting results, and Table
9 provides the comprehensive breakdown with standard deviations in the format mean±std.
[Minesweeper] Extracted results exclusively for the 'Minesweeper' dataset from Table 9. The metric
used is AUC (ROC-AUC) as specified in the table caption and focus instructions. All values were
converted from percentages to [0,1] range. Standard deviations were parsed from the 'mean ± std'
format. Table 1 was ignored as it contains aggregated results for multiple datasets and less
detailed breakdowns compared to Table 9. 'Ours' is identified as the proposed model. [Tolokers]
Extracted all results for the 'Tolokers' dataset from Table 9. The metric is ROC-AUC (reported as
AUC in the table caption). Values are normalized to [0,1]. Standard deviations are parsed from the
'mean ± std' format. The proposed model 'Ours' is identified. Baselines include various GNNs,
Transformers, and Spectral methods. Note: Table 1 also contains results for Tolokers but uses a
different notation (Acc/AUC) and fewer models; Table 9 is the comprehensive benchmark table and was
used for extraction. The values in Table 1 for 'Ours' (85.57) and 'Polynormer' (85.91) match Table
9, confirming consistency. The 'Ours' model in Table 9 has a std of 0.61 (0.0061), while Table 1 has
0.6 (0.006). Table 9 is more precise.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*