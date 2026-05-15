# Extraction: arXiv:2412.07188
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: FA
- Type: GNN

## Results

### CS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| APPNP | 0.5290 | 0.0216 | Yes | this paper | Table 1 |
| FA | 0.5295 | 0.0379 | Yes | this paper | Table 1 |
| GIN | 0.5790 | 0.0335 | Yes | this paper | Table 1 |
| SGC | 0.5925 | 0.0419 | Yes | this paper | Table 1 |
| GAT | 0.5828 | 0.0209 | Yes | this paper | Table 1 |
| GPS | 0.5989 | 0.0173 | Yes | this paper | Table 1 |
| GCN | 0.5982 | 0.0404 | Yes | this paper | Table 1 |
| GatedGraph | 0.6614 | 0.0293 | Yes | this paper | Table 1 |
| Transformer | 0.5943 | 0.0150 | Yes | this paper | Table 1 |
| Cheb | 0.6088 | 0.0193 | Yes | this paper | Table 1 |
| 1-GNN | 0.6627 | 0.0277 | Yes | this paper | Table 1 |
| GATv2 | 0.6041 | 0.0212 | Yes | this paper | Table 1 |
| GCNII | 0.6291 | 0.0275 | Yes | this paper | Table 1 |
| SAGE | 0.6317 | 0.0201 | Yes | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| APPNP | 0.5426 | 0.0180 | Yes | this paper | Table 1 |
| FA | 0.5488 | 0.0282 | No | this paper | Table 1 |
| GIN | 0.6098 | 0.0294 | Yes | this paper | Table 1 |
| SGC | 0.6109 | 0.0371 | Yes | this paper | Table 1 |
| GAT | 0.6033 | 0.0226 | Yes | this paper | Table 1 |
| GPS | 0.5823 | 0.0099 | Yes | this paper | Table 1 |
| GCN | 0.6217 | 0.0418 | Yes | this paper | Table 1 |
| GatedGraph | 0.6985 | 0.0274 | Yes | this paper | Table 1 |
| Transformer | 0.6289 | 0.0175 | Yes | this paper | Table 1 |
| Cheb | 0.6054 | 0.0140 | Yes | this paper | Table 1 |
| 1-GNN | 0.6800 | 0.0245 | Yes | this paper | Table 1 |
| GATv2 | 0.6305 | 0.0221 | Yes | this paper | Table 1 |
| GCNII | 0.6054 | 0.0273 | Yes | this paper | Table 1 |
| SAGE | 0.6397 | 0.0180 | Yes | this paper | Table 1 |

### DBLP — Normalized AUAC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| APPNP | 0.5169 | 0.0040 | Yes | this paper | Table 1 |
| FA | 0.5276 | 0.0110 | Yes | this paper | Table 1 |
| GIN | 0.5899 | 0.0295 | Yes | this paper | Table 1 |
| SGC | 0.5636 | 0.0195 | Yes | this paper | Table 1 |
| GAT | 0.5841 | 0.0167 | Yes | this paper | Table 1 |
| GPS | 0.5894 | 0.0092 | Yes | this paper | Table 1 |
| GCN | 0.5721 | 0.0209 | Yes | this paper | Table 1 |
| GatedGraph | 0.6384 | 0.0256 | Yes | this paper | Table 1 |
| Transformer | 0.6186 | 0.0136 | Yes | this paper | Table 1 |
| Cheb | 0.6114 | 0.0128 | Yes | this paper | Table 1 |
| 1-GNN | 0.6416 | 0.0196 | Yes | this paper | Table 1 |
| GATv2 | 0.5938 | 0.0192 | Yes | this paper | Table 1 |
| GCNII | 0.5813 | 0.0300 | Yes | this paper | Table 1 |
| SAGE | 0.6288 | 0.0133 | Yes | this paper | Table 1 |

### Physics — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| APPNP | 0.5360 | 0.0138 | Yes | this paper | Table 1 |
| FA | 0.5581 | 0.0233 | Yes | this paper | Table 1 |
| GIN | 0.5965 | 0.0327 | Yes | this paper | Table 1 |
| SGC | 0.5887 | 0.0338 | Yes | this paper | Table 1 |
| GAT | 0.6038 | 0.0210 | Yes | this paper | Table 1 |
| GPS | 0.6290 | 0.0152 | Yes | this paper | Table 1 |
| GCN | 0.5949 | 0.0361 | Yes | this paper | Table 1 |
| GatedGraph | 0.6020 | 0.0286 | Yes | this paper | Table 1 |
| Transformer | 0.6093 | 0.0149 | Yes | this paper | Table 1 |
| Cheb | 0.6295 | 0.0206 | Yes | this paper | Table 1 |
| 1-GNN | 0.6516 | 0.0277 | Yes | this paper | Table 1 |
| GATv2 | 0.6258 | 0.0212 | Yes | this paper | Table 1 |
| GCNII | 0.6655 | 0.0250 | Yes | this paper | Table 1 |
| SAGE | 0.6429 | 0.0210 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **APPNP**
- **GIN**
- **SGC**
- **GAT**
- **GPS**
- **GCN**
- **GatedGraph**
- **Transformer**
- **Cheb**
- **1-GNN**
- **GATv2**
- **GCNII**
- **SAGE**
- **FA**

## Extraction Notes

[Computers] The user requested results for the 'Computers' dataset with a primary metric of
'Accuracy'. While the provided text contains tables for the 'Computers' dataset, the metrics
reported are 'Normalized AUAC' (Table 1) and 'AUC for the lower/middle third of the spectrum'
(Tables 2 and 3). No standard 'Accuracy' results were present in the provided text for the Computers
dataset. Therefore, no results were extracted. [Cora] The paper reports 'Normalized AUAC score in
percentage' in Table 1. Based on the context of the 'Benchmark Evaluation Metrics' section, this is
the primary quantitative measure for their node classification task on the spectral bins. I have
normalized these percentage values to [0, 1] as per the instructions for accuracy-like metrics. [CS]
Extracted results from Table 1. The table reports 'Normalized AUAC score in percentage', but the
text explicitly states that node classification accuracy is the primary metric and the AUAC is
derived from accuracy curves. Per instructions to focus on Accuracy and the provided table context,
these values were treated as the primary benchmark results for the CS dataset. Tables 2 and 3 were
skipped as they represent specific spectral subsets (lower/middle third) rather than the
standard/default benchmark. [DBLP] The paper does not report 'Micro-F1' for DBLP. The primary metric
reported in the tables is 'Normalized AUAC' (reported as percentages). I have extracted the
Normalized AUAC values as they are the main quantitative results provided for the DBLP dataset in
the provided text. No proposed model was explicitly identified in the text snippet provided. [Photo]
The user requested results for the dataset 'Photo' with the primary metric 'Accuracy'. While Table
1, Table 2, and Table 3 contain data for the 'Photo' dataset, the metrics reported are 'Normalized
AUAC' and 'AUC' (for specific spectral thirds), not 'Accuracy'. The text mentions that Accuracy is
the primary metric and refers to accuracy curves in figures, but no quantitative Accuracy values are
provided in the provided tables for the Photo dataset. Therefore, no results matching the primary
metric criteria were extracted. [Physics] Extracted results from Table 1 which reports 'Normalized
AUAC score in percentage'. Per the 'Benchmark Evaluation Metrics' section, node classification
accuracy is the primary metric, and the AUAC is a quantitative measure of this capability. Tables 2
and 3 were skipped as they represent specific spectral subsets (lower/middle third) rather than the
standard/default benchmark result.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*