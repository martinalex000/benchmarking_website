# Extraction: When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as Effectively as We Expected
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: LLaGA
- Type: Other

## Results

### Amazon Ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LLaGA (ND) | 0.4097 | 0.0056 | Yes | this paper | Table 2 |
| LLaGA (HN-1) | 0.4167 | 0.0022 | Yes | this paper | Table 2 |
| LLaGA (CO) | 0.4038 | 0.0114 | Yes | this paper | Table 2 |
| MLP | 0.4078 | 0.0035 | Yes | this paper | Table 3 |
| GCN | 0.4052 | 0.0051 | Yes | this paper | Table 3 |
| GAT | 0.4071 | 0.0023 | Yes | this paper | Table 3 |
| GIN | 0.3876 | 0.0018 | Yes | this paper | Table 3 |

### BACE — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5899 | 0.0166 | Yes | this paper | Table 4 |
| GCN | 0.5877 | 0.0913 | Yes | this paper | Table 4 |
| GIN | 0.5899 | 0.0552 | Yes | this paper | Table 4 |
| GAT | 0.5746 | 0.0362 | Yes | this paper | Table 4 |

### BBBP — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5457 | 0.0138 | Yes | this paper | Table 4 |
| GCN | 0.5784 | 0.0049 | Yes | this paper | Table 4 |
| GIN | 0.6029 | 0.0049 | No | this paper | Table 4 |
| GAT | 0.5196 | 0.0147 | Yes | this paper | Table 4 |

### Citeseer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LLaGA (ND) | 0.8031 | 0.0081 | No | this paper | Table 2 |
| LLaGA (HN-1) | 0.8020 | 0.0094 | No | this paper | Table 2 |
| LLaGA (CO) | 0.7774 | 0.0031 | No | this paper | Table 2 |
| MLP | 0.7939 | 0.0138 | Yes | this paper | Table 3 |
| GCN | 0.8020 | 0.0013 | Yes | this paper | Table 3 |
| GAT | 0.7974 | 0.0041 | Yes | this paper | Table 3 |
| GIN | 0.7932 | 0.0111 | Yes | this paper | Table 3 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ND | 0.8807 | 0.0074 | No | this paper | Table 2 |
| HN-1 | 0.8856 | 0.0080 | No | this paper | Table 2 |
| CO | 0.8542 | 0.0178 | No | this paper | Table 2 |
| MLP | 0.8709 | 0.0066 | Yes | this paper | Table 3 |
| GCN | 0.8764 | 0.0084 | Yes | this paper | Table 3 |
| GAT | 0.8825 | 0.0053 | Yes | this paper | Table 3 |
| GIN | 0.8303 | 0.0541 | Yes | this paper | Table 3 |
| Llama2-7B (ND) | 0.8776 | 0.0021 | Yes | this paper | Table 5 |
| Llama2-7B (HN-1) | 0.8801 | 0.0056 | Yes | this paper | Table 5 |
| Llama2-13B (ND) | 0.8758 | 0.0059 | Yes | this paper | Table 5 |
| Llama2-13B (HN-1) | 0.8745 | 0.0019 | Yes | this paper | Table 5 |

### HIV — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.9685 | 0.0001 | Yes | this paper | Table 4 |
| GCN | 0.9681 | 0.0003 | Yes | this paper | Table 4 |
| GIN | 0.9679 | 0.0000 | Yes | this paper | Table 4 |
| GAT | 0.9682 | 0.0003 | Yes | this paper | Table 4 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ND | 0.9256 | 0.0071 | Yes | this paper | Table 2 |
| HN-1 | 0.9480 | 0.0017 | Yes | this paper | Table 2 |
| CO | 0.9484 | 0.0004 | Yes | this paper | Table 2 |
| MLP | 0.9476 | 0.0010 | Yes | this paper | Table 3 |
| GCN | 0.9224 | 0.0123 | Yes | this paper | Table 3 |
| GAT | 0.9201 | 0.0024 | Yes | this paper | Table 3 |
| GIN | 0.9140 | 0.0063 | Yes | this paper | Table 3 |

### Roman Empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LLaGA (CO) | 0.6224 | 0.0019 | No | this paper | Table 2 |
| LLaGA (HN-1) | 0.5970 | 0.0242 | No | this paper | Table 2 |
| LLaGA (ND) | 0.4856 | 0.0117 | No | this paper | Table 2 |
| GIN | 0.4692 | 0.2237 | Yes | this paper | Table 3 |
| MLP | 0.6539 | 0.0029 | Yes | this paper | Table 3 |
| GAT | 0.3697 | 0.1392 | Yes | this paper | Table 3 |
| GCN | 0.3651 | 0.1806 | Yes | this paper | Table 3 |

### School — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LLaGA (CO) | 0.9113 | 0.0166 | No | this paper | Table 2 |
| LLaGA (HN-1) | 0.8202 | 0.1279 | No | this paper | Table 2 |
| LLaGA (ND) | 0.6643 | 0.0369 | No | this paper | Table 2 |
| MLP | 0.9017 | 0.0362 | Yes | this paper | Table 3 |
| GCN | 0.6787 | 0.0324 | Yes | this paper | Table 3 |
| GAT | 0.6475 | 0.0000 | Yes | this paper | Table 3 |
| GIN | 0.7002 | 0.0219 | Yes | this paper | Table 3 |

## Baseline Models Identified

- **MLP**
- **GCN** (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GIN** (from: Xu et al. 2019)

## Extraction Notes

[Cora] Extracted all Node Classification Accuracy results for Cora from Tables 2, 3, and 5. Table 2
compares LLaGA templates (ND, HN-1, CO). Table 3 compares GNN adapters (MLP, GCN, GAT, GIN). Table 5
compares different LLM backbones (Llama2-7B, Llama2-13B) with templates. All values were converted
from percentages to [0,1] range. Standard deviations were extracted from parentheses.
'uses_external_data' is set to true for Llama2 models as they are pre-trained LLMs. [CiteSeer]
Extracted Node Classification Accuracy results for Citeseer from Table 2 (LLaGA variants) and Table
3 (MLP/GCN/GAT/GIN baselines). Link Prediction results for Citeseer were ignored as per the FOCUS
instruction to prioritize the primary benchmark metric 'Accuracy' for node classification datasets.
Values were converted from percentages to floats. [PubMed] Extracted results for PubMed from Table 2
(LLaGA templates) and Table 3 (GNN adapters). Note: Table 2 lists 'Pubmed' while Table 3 lists
'Pubmed'. Both refer to the same dataset. The FOCUS instruction specified 'PubMed', so these are
included. The values are normalized from percentages to [0,1]. Standard deviations are parsed from
the parentheses. Table 2 compares LLaGA structural templates (ND, HN-1, CO). Table 3 compares GNN
adapters (MLP, GCN, GAT, GIN). All are treated as baselines/comparisons against the proposed LLaGA
framework's findings. [School] Extracted results for 'School' dataset from Table 2, Table 3, and
Table 5. Note: Table 2 and Table 5 contain results for 'Shool' which is a typo for 'School' based on
Table 1. Table 2 reports LLaGA variants (ND, HN-1, CO). Table 3 reports MLP, GCN, GAT, GIN
baselines. Table 5 reports LLaGA results with different LLM backbones (Llama2-7B, Llama2-13B). All
values are normalized to [0,1]. Standard deviations are extracted from parentheses. [Roman Empire]
Extracted results for 'Roman Empire' from Table 2 (LLaGA variants) and Table 3 (GNN/MLP baselines).
Table 2 reports Node Classification Accuracy for LLaGA templates (ND, HN-1, CO). Table 3 reports
Node Classification Accuracy for MLP, GCN, GAT, and GIN. Values were converted from percentages to
decimals. Standard deviations were parsed from the parentheses. Note: Table 3 also contains Link
Prediction results for Roman Empire, but the FOCUS instruction specified 'Accuracy' as the primary
metric, so Link Prediction results were excluded. [Amazon Ratings] Extracted Node Classification
Accuracy results for 'Amazon Ratings' from Table 2 (LLaGA variants) and Table 3 (MLP/GCN/GAT/GIN
baselines). Values were converted from percentages to decimals. Standard deviations were extracted
from the parentheses. Link Prediction results for Amazon Ratings were ignored as per the FOCUS
instruction to prioritize Accuracy. [BACE] Extracted results for the BACE dataset from Table 4
(Molecular Property Prediction). The table reports ROC-AUC percentages. All values were divided by
100 to normalize to [0, 1]. The proposed model (LLaGA) is not explicitly listed as a separate row in
this specific table; the table compares MLP, GCN, GIN, and GAT adapters. The caption mentions
LLaGA's ND template in previous tables, but Table 4 focuses on the adapter comparison. The highest
value (0.5899) is shared by MLP and GIN, marked as best. Standard deviations are provided in
parentheses. [BBBP] Extracted results for BBBP from Table 4 (Molecular Property Prediction). The
table reports ROC-AUC percentages. Values were divided by 100 to normalize to [0,1]. The proposed
model is identified as GIN based on the caption context comparing LLM adapters (MLP, GCN, GAT, GIN)
where GIN achieves the best result. Note: The paper title/context suggests the proposed method
involves LLMs with structural encodings, but the specific table compares GNN-based adapters. GIN is
treated as the proposed/best-performing model in this specific comparison context. [HIV] Extracted
results for the HIV dataset from Table 4 (Molecular Property Prediction). The table reports ROC-AUC
scores for MLP, GCN, GIN, and GAT baselines. The proposed model (LLaGA) is not explicitly listed in
this specific table row for HIV, but the table caption and context imply these are the baselines
being compared against the proposed method's findings. The values are percentages, so they were
divided by 100. Standard deviations were parsed from the parentheses.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*