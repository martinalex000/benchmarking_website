# Extraction: SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: SGFormer
- Type: GNN

## Results

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5550 | 0.0023 | Yes | this paper | Table 2 |
| GCN | 0.7174 | 0.0029 | Yes | this paper | Table 2 |
| SGC | 0.6779 | 0.0027 | Yes | this paper | Table 2 |
| GCN-NSampler | 0.6850 | 0.0023 | Yes | this paper | Table 2 |
| GAT-NSampler | 0.6763 | 0.0023 | Yes | this paper | Table 2 |
| SIGN | 0.7028 | 0.0025 | Yes | this paper | Table 2 |
| NodeFormer | 0.5990 | 0.0042 | Yes | this paper | Table 2 |
| SGFormer | 0.7263 | 0.0013 | No | this paper | Table 2 |

### ogbn-proteins — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.7204 | 0.0048 | Yes | this paper | Table 1 |
| GCN | 0.7251 | 0.0035 | Yes | this paper | Table 1 |
| SGC | 0.7031 | 0.0023 | Yes | this paper | Table 1 |
| GCN-NSampler | 0.7351 | 0.0131 | Yes | this paper | Table 1 |
| GAT-NSampler | 0.7463 | 0.0124 | Yes | this paper | Table 1 |
| SIGN | 0.7124 | 0.0046 | Yes | this paper | Table 1 |
| NodeFormer | 0.7745 | 0.0115 | Yes | nodeformer | Table 1 |
| SGFormer | 0.7953 | 0.0038 | No | this paper | Table 1 |

## Baseline Models Identified

- **MLP**
- **GCN** (from: Kipf & Welling)
- **SGC** (from: Zhang & Zitnik)
- **GCN-NSampler** (from: graphsaint)
- **GAT-NSampler** (from: graphsaint)
- **SIGN** (from: Fey & Lenssen)
- **NodeFormer** (from: nodeformer)

## Extraction Notes

[ogbn-proteins] Extracted only the 'ogbn-proteins' column from Table 1 as requested. The metric is
ROC-AUC. Values were converted from percentages (e.g., 79.53) to decimals (0.7953) per instructions.
Standard deviations were parsed from the 'mean ± std' format. [ogbn-papers100M] failed: 2 validation
errors for ExtractionOutput results.1.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.6.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [ogbn-arxiv] Extracted results for ogbn-arxiv from
Table 2 (tab:main-res-l). The table caption specifies 'Accuracy for other datasets' (ogbn-arxiv is
not ogbn-proteins). Values are percentages in the table (e.g., 72.63), converted to [0,1] range
(0.7263). Standard deviations are parsed from '±' notation. [ogbn-products] The dataset 'ogbn-
products' is NOT present in the provided tables. Table 1 contains small node classification
benchmarks (Cora, CiteSeer, etc.). Table 2 contains large node property prediction benchmarks (ogbn-
proteins, Amazon2m, pokec, ogbn-arxiv, ogbn-papers100M). Since the FOCUS instruction explicitly
requested results ONLY for 'ogbn-products' and instructed to ignore other datasets, no results were
extracted. [ogbn-mag] The dataset 'ogbn-mag' is not present in the provided tables. Table 1 contains
results for Cora, CiteSeer, PubMed, Actor, Squirrel, Chameleon, and Deezer. Table 2 contains results
for ogbn-proteins, Amazon2m, pokec, ogbn-arxiv, and ogbn-papers100M. No results for ogbn-mag were
extracted. [ogbn-scholar] The dataset 'ogbn-scholar' is not present in the provided tables. Table 1
contains Cora, CiteSeer, PubMed, Actor, Squirrel, Chameleon, and Deezer. Table 2 contains ogbn-
proteins, Amazon2m, pokec, ogbn-arxiv, and ogbn-papers100M. No results for ogbn-scholar were
extracted. [ogbn-proteins] Extracted only the 'ogbn-proteins' column from Table 1 as requested. The
metric is ROC-AUC. Values were converted from percentages (e.g., 79.53) to decimals (0.7953) per
instructions. Standard deviations were parsed from the 'mean ± std' format.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*