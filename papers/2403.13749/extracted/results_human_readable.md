# Extraction: arXiv:2403.13749
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: LOW

## Proposed Model: 4-ell-GIN
- Type: GNN

## Results

### BREC — Num. of distinguished pairs ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 3-WL | 60.0000 | — | Yes | Wang et al. 2023 | Table 2 |
| PPGN | 60.0000 | — | Yes | Wang et al. 2023 | Table 2 |
| NGNN | 59.0000 | — | Yes | Wang et al. 2023 | Table 2 |
| WLSub | 60.0000 | — | Yes | Wang et al. 2023 | Table 2 |
| OrderGNN | 52.0000 | — | Yes | Wang et al. 2023 | Table 2 |
| 4-ell-GIN | 60.0000 | — | No | this paper | Table 2 |

### PEPTIDES — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Kipf et al. | 0.3496 | 0.0013 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| Kipf et al. | 0.5930 | 0.0023 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| Hu et al. | 0.3496 | 0.0013 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| Hu et al. | 0.5930 | 0.0023 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| Bresson et al. | 0.3420 | 0.0013 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| Bresson et al. | 0.5864 | 0.0077 | Yes | Dwivedi Long Range Graph Benchmark | Table 1 |
| 7-ℓGIN | 0.2513 | 0.0021 | No | this paper | Table 1 |
| 7-ℓGIN | 0.6570 | 0.0060 | No | this paper | Table 1 |

### Synthetic Subgraph Counting — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MPNN | 0.3000 | — | Yes | this paper | Table 2 |
| Subgraph GNN | 0.0110 | — | Yes | this paper | Table 2 |
| Local 2-GNN | 0.0080 | — | Yes | this paper | Table 2 |
| Local 2-FGNN | 0.0030 | — | Yes | this paper | Table 2 |
| r-lGIN (r=2) | 0.0010 | — | No | this paper | Table 2 |
| r-lGIN (r=3) | 0.0060 | — | No | this paper | Table 2 |
| r-lGIN (r=1) | 0.0005 | — | No | this paper | Table 2 |
| r-lGIN (r=4) | 0.0003 | — | No | this paper | Table 2 |

### ZINC12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| 0-lGIN | 0.2090 | 0.0070 | Yes | this paper | Table 1 |
| 1-lGIN | 0.2010 | 0.0040 | No | this paper | Table 1 |
| 2-lGIN | 0.1980 | 0.0080 | No | this paper | Table 1 |
| 3-lGIN | 0.1840 | 0.0070 | No | this paper | Table 1 |
| 4-lGIN | 0.0770 | 0.0010 | No | this paper | Table 1 |
| 5-lGIN | 0.0720 | 0.0020 | No | this paper | Table 1 |
| 6-lGIN | 0.0770 | 0.0000 | No | this paper | Table 1 |

## Baseline Models Identified

- **3-WL** (from: Weisfeiler and Leman (1968))
- **PPGN** (from: Maron et al. 2019)
- **NGNN** (from: Zhang et al. 2021)
- **WLSub** (from: Citation 9721082 (likely Xu et al. or similar subgraph GNN))
- **OrderGNN** (from: Qian et al. 2022)
- **MPNN**
- **Subgraph GNN**
- **Local 2-GNN**
- **Local 2-FGNN**
- **0-lGIN**
- **Kipf et al.** (from: Kipf 2017)
- **Hu et al.** (from: Hu 2020)
- **Bresson et al.** (from: Bresson 2017)

## Extraction Notes

[BREC] Extracted results from Table 2 (labeled tab:brec in the paper). The table presents 'Num. of
distinguished pairs' for the BREC dataset across four subsets: Basic, Regular, Extension, and CFI.
The prompt asks for the STANDARD/DEFAULT configuration. In the context of BREC (a dataset of
strongly regular graphs often used to test WL variants), the 'Basic' subset (60 graphs) is the
primary standard benchmark for distinguishing pairs of graphs. The 'Regular', 'Extension', and 'CFI'
columns represent specific subsets or variations. The text highlights that 4-ell-GIN distinguishes
all pairs in the full set (implied by the high numbers in Basic/Regular/Extension) and specifically
mentions outperforming baselines on the BREC dataset generally. The values in the 'Basic' column are
the most representative of the standard performance on the core dataset. Note: The table caption
says 'Results from Wang Better Evaluation GNN 2023', but the proposed model 4-ell-GIN is added in
this paper's table for comparison. The values for baselines are taken directly from the table cells.
The text mentions 4-ell-GIN distinguishes 257/400 pairs, which likely refers to a different split or
the full set of 400 pairs mentioned in the text, but the table only shows subsets. I have extracted
the 'Basic' column values as they represent the standard evaluation on the primary subset. If
'Regular' or others were considered standard, the values would differ, but 'Basic' is the first and
typically primary column. The text explicitly compares 4-ell-GIN (257/400) to PPGN (233/400) and
NGNN (166/400), which suggests the table might be showing a subset or the text refers to a different
metric/count. However, the table clearly labels the columns. I will extract the 'Basic' column as
the standard result for the dataset 'BREC' as requested, assuming 'Basic' is the default
configuration. The text's mention of 400 pairs suggests the full dataset size, while the table shows
subsets (60, 140, 100, 100). The 'Basic' subset has 60 graphs. The values in the table are counts of
distinguished pairs. I will use the 'Basic' column values. [Synthetic Subgraph Counting] The table
contains multiple columns representing different subgraph counts (homomorphism and subgraph counts
for various target graphs). The prompt asks for 'Synthetic Subgraph Counting' results. Since the
table aggregates these into one 'Test MAE' metric across different target graphs, I have extracted
all values. The 'r-lGIN' model has different 'r' values for different columns; I have included the
'r' value in the model name to distinguish them. The first table (Table 1) reports 'Num. of
distinguished pairs' which is not MAE, so it was excluded based on the FOCUS instruction. The
dataset name is inferred as 'Synthetic Subgraph Counting' from the caption and context. [QM9]
failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary or instance of
ExtractionOutput [type=model_type, input_value=[{'name': '1-GNN', 'param...': 'Maron et al. 2019'}],
input_type=list]     For further information visit https://errors.pydantic.dev/2.13/v/model_type
[ZINC12K] Extracted all rows from the ablation study table for ZINC12K. The table reports Train and
Test MAE; only Test MAE values were extracted as per instructions. The proposed model is the family
r-lGIN with varying r. 0-lGIN is treated as the baseline. All values are normalized correctly (MAE
is not a percentage). Standard deviations were parsed from the 'mean ± std' format. [ZINC250K] The
paper mentions ZINC250K in the text, stating that r-lGIN outperforms 0-lGIN by 400% on this dataset.
However, the provided text does not contain a table with the actual quantitative MAE values for
ZINC250K. Table 1 (tab:subgraphcount) reports MAE for homomorphism/subgraph counting tasks, not the
standard ZINC regression task. Table 3 (tab:qm9) and Table 4 (tab:qm9_full) report results for QM9.
Table 5 (tab:rl_dataset_statistics) only provides dataset statistics. Table 6 (tab:hyperparameters)
provides hyperparameters for ZINC250K but no performance metrics. Without a table containing the
specific MAE values for the ZINC250K regression task, no quantitative results can be extracted for
this dataset. [PEPTIDES] Extracted results for PEPTIDES dataset from Table 1. Note: The table lists
'STRUCT (MAE)' and 'FUNC (AP)'. The paper focuses on PEPTIDES, which typically has two tasks:
Peptides-struct (MAE) and Peptides-func (AP). The table header says 'PEPTIDES' with sub-columns for
STRUCT and FUNC. I have extracted both metrics for all models. The baseline values for Kipf and Hu
are identical in the table, likely a copy-paste error in the original paper or they share the same
baseline source, but I extracted exactly what is written. AP values were converted from percentages
(e.g., 59.30 -> 0.593) as per rules.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*