# Extraction: Size Transferability of Graph Transformers with Convolutional Positional Encodings
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: LOW

## Proposed Model: GT + Mask + RPEARL
- Type: GraphTransformer

## Results

### snap-patents — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT (no PE) | 31.3300 | — | Yes | this paper | Table 1 |
| GT + RPEARL | 34.6300 | — | Yes | this paper | Table 1 |
| GT + Mask | 39.6900 | — | Yes | this paper | Table 1 |
| GT + Mask + RPEARL | 49.7000 | — | No | this paper | Table 1 |
| GT + Mask + RE | 31.0100 | — | Yes | this paper | Table 1 |
| GT + Mask + RPEARL + RE | 46.5500 | — | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GT (no PE)**
- **GT + RPEARL**
- **GT + Mask**
- **GT + Mask + RE**
- **GT + Mask + RPEARL + RE**
- **Dense GT**
- **GNN**
- **Exphormer** (from: Shirzad et al. 2023)
- **MLP**

## Extraction Notes

[snap-patents] Extracted results from Table 1 which reports test accuracy on snap-patents for
various ablation configurations of the Graph Transformer (GT). The proposed model is identified as
'GT + Mask + RPEARL' as it achieves the highest accuracy (bolded in table). No standard deviation
values were reported in the table. The table caption specifies alpha=0.3 training fraction, which is
the specific configuration evaluated in this table. [arXiv-year] The paper discusses results for
'arXiv-year' in the text and figures (Figures 1, 2, 3) and mentions that Sparse GT achieves superior
performance to Dense GT. However, the provided text does not contain a table with specific numerical
Accuracy values for the arXiv-year dataset. Table 1 (tab:ablation) is for SNAP-Patents. Table 2
(tab:datasets) lists dataset statistics. Table 3 (tab:hyperparameters) lists hyperparameters. Table
4 (tab:runtimes) lists training times. The figures are images and their data cannot be extracted as
text. Therefore, no quantitative results for arXiv-year could be extracted. [OGBN-MAG] The paper
text and provided tables do not contain the quantitative accuracy results for the OGBN-MAG dataset.
Table 1 (tab:ablation) reports results only for SNAP-Patents. Table 2 (tab:datasets) lists dataset
statistics. Table 3 (tab:hyperparameters) lists hyperparameters. Table 4 (tab:runtimes) lists
runtimes. While Figures 2 and 3 mention 'Test Accuracy Heatmaps on OGBN-MAG', the actual numerical
values are not present in the text or tables provided. Therefore, no results could be extracted for
OGBN-MAG. [Reddit-Binary] The paper provides hyperparameters (Table 3) and dataset statistics (Table
2) for Reddit-Binary, but does not contain any result tables reporting Accuracy or other metrics for
this dataset. The only result table (Table 1) reports results for SNAP-Patents. Therefore, no
quantitative results could be extracted for Reddit-Binary.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*