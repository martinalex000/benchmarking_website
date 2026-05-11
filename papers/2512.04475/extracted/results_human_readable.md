# Extraction: GraphBench: Next-generation graph learning benchmarking
**Model used**: `glm-4.7`  **Date**: 2026-05-11  **Confidence**: LOW

## Proposed Model: GraphBench
- Type: Other

## Main Figure: Figure 1
> Overview of the GraphBench framework. GraphBench integrates diverse domain datasets —ranging from social scie
- Figure 1 provides the high-level overview of the GraphBench framework, illustrating the integration of diverse domain datasets into different learning regimes and the unified evaluation pipeline, which is the core contribution of the paper.

## Results

### 10 comp — RSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.2900 | 0.0300 | No | this paper | Table 6 |
| GIN | 0.4400 | 0.1300 | Yes | this paper | Table 6 |
| GAT | 0.3800 | 0.0500 | Yes | this paper | Table 6 |
| GCN | 0.5300 | 0.0600 | Yes | this paper | Table 6 |

### 5 comp — RSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.0700 | 0.0300 | No | this paper | Table 6 |
| GIN | 0.0900 | 0.0600 | Yes | this paper | Table 6 |
| GAT | 0.1100 | 0.0500 | Yes | this paper | Table 6 |
| GCN | 0.1300 | 0.0700 | Yes | this paper | Table 6 |

### 7 comp — RSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GT | 0.1800 | 0.0600 | No | this paper | Table 6 |
| GIN | 0.2100 | 0.0400 | Yes | this paper | Table 6 |
| GAT | 0.2200 | 0.0500 | Yes | this paper | Table 6 |
| GCN | 0.3000 | 0.0400 | Yes | this paper | Table 6 |

### AIG (6,1) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 73.9000 | — | Yes | this paper | Table 5 |
| Resyn | 86.7900 | — | Yes | this paper | Table 5 |
| Compress2 | 92.5300 | — | Yes | this paper | Table 5 |
| Resyn2rs | 93.3000 | — | No | this paper | Table 5 |

### AIG (6,2) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 74.2300 | — | Yes | this paper | Table 5 |
| Resyn | 88.1600 | — | Yes | this paper | Table 5 |
| Compress2 | 93.5700 | — | Yes | this paper | Table 5 |
| Resyn2rs | 95.2400 | — | No | this paper | Table 5 |

### AIG (7,1) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 76.5500 | — | Yes | this paper | Table 5 |
| Resyn | 89.2800 | — | Yes | this paper | Table 5 |
| Compress2 | 93.1800 | — | Yes | this paper | Table 5 |
| Resyn2rs | 95.1500 | — | No | this paper | Table 5 |

### AIG (7,2) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 75.7100 | — | Yes | this paper | Table 5 |
| Resyn | 89.0500 | — | Yes | this paper | Table 5 |
| Compress2 | 92.7900 | — | Yes | this paper | Table 5 |
| Resyn2rs | 95.6400 | — | No | this paper | Table 5 |

### AIG (8,1) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 77.6300 | — | Yes | this paper | Table 5 |
| Resyn | 90.4500 | — | Yes | this paper | Table 5 |
| Compress2 | 93.2800 | — | Yes | this paper | Table 5 |
| Resyn2rs | 96.2400 | — | No | this paper | Table 5 |

### AIG (8,2) — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 76.5200 | — | Yes | this paper | Table 5 |
| Resyn | 89.7800 | — | Yes | this paper | Table 5 |
| Compress2 | 92.4900 | — | Yes | this paper | Table 5 |
| Resyn2rs | 96.1100 | — | No | this paper | Table 5 |

### AIG Overall — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Strash | 75.7600 | — | Yes | this paper | Table 5 |
| Resyn | 88.9200 | — | Yes | this paper | Table 5 |
| Compress2 | 92.9700 | — | Yes | this paper | Table 5 |
| Resyn2rs | 95.2800 | — | No | this paper | Table 5 |

### Bridges-easy — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9831 | 0.0184 | Yes | this paper | Table 16 |
| GT | 0.9269 | 0.0103 | No | this paper | Table 16 |

### Bridges-hard — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9680 | 0.0178 | Yes | this paper | Table 16 |
| GT | 0.8897 | 0.0304 | No | this paper | Table 16 |

### Bridges-medium — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.9622 | 0.0077 | Yes | this paper | Table 16 |
| GT | 0.8762 | 0.0258 | No | this paper | Table 16 |

### ER graph Large — MIS ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.3520 | 0.2650 | Yes | this paper | Table 12 |
| GT | 9.6410 | 15.3350 | Yes | this paper | Table 12 |
| MLP | 0.9140 | 0.3070 | Yes | this paper | Table 12 |

### ER graph Small — MIS ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.2340 | 0.1910 | Yes | this paper | Table 12 |
| GT | 6.4860 | 8.1010 | Yes | this paper | Table 12 |
| MLP | 0.7510 | 0.7670 | Yes | this paper | Table 12 |
| DeepSet | 0.7560 | — | Yes | this paper | Table 12 |

### Large SAT instances — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.5800 | 0.0000 | Yes | this paper | Table 9 |
| XGB | 0.6300 | 0.0000 | Yes | this paper | Table 9 |

### MST-easy — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.6906 | 0.1655 | Yes | this paper | Table 16 |
| GT | 0.8566 | 0.0068 | No | this paper | Table 16 |

### MST-hard — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.6107 | 0.2015 | Yes | this paper | Table 16 |
| GT | 0.8421 | 0.0115 | No | this paper | Table 16 |

### MST-medium — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.7288 | 0.0894 | Yes | this paper | Table 16 |
| GT | 0.8504 | 0.0148 | No | this paper | Table 16 |

### Max Clique-easy — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4584 | 0.0101 | Yes | this paper | Table 16 |
| GT | 0.5407 | 0.0088 | No | this paper | Table 16 |

### Max Clique-hard — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4102 | — | Yes | this paper | Table 16 |

### Max Clique-medium — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.3996 | 0.0852 | Yes | this paper | Table 16 |
| GT | 0.4859 | 0.0017 | No | this paper | Table 16 |

### Medium-size SAT instances — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.5900 | 0.0000 | Yes | this paper | Table 9 |
| XGB | 0.6200 | 0.0000 | Yes | this paper | Table 9 |

### RB graph Large — MIS ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 2.1250 | 0.4840 | Yes | this paper | Table 12 |
| GT | 0.9150 | 0.2350 | Yes | this paper | Table 12 |
| MLP | 1.4370 | 0.5200 | Yes | this paper | Table 12 |
| DeepSet | 1.4270 | 0.2240 | Yes | this paper | Table 12 |

### RB graph Small — MIS ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4910 | 0.0990 | Yes | this paper | Table 12 |
| GT | 4.1120 | 2.3530 | Yes | this paper | Table 12 |
| MLP | 1.5830 | 0.0520 | Yes | this paper | Table 12 |
| DeepSet | 0.9180 | 0.1860 | Yes | this paper | Table 12 |

### SAT Solving (BreakIDKissat, LCG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.5200 | 0.0100 | No | this paper | Table 8 |

### SAT Solving (BreakIDKissat, SATzilla) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.6500 | 0.0000 | Yes | this paper | Table 8 |
| XGB | 0.6800 | 0.0100 | Yes | this paper | Table 8 |

### SAT Solving (BreakIDKissat, VCG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.3300 | 0.1500 | No | this paper | Table 8 |

### SAT Solving (BreakIDKissat, VG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.2900 | 0.0300 | No | this paper | Table 8 |

### SAT Solving (Kissat, LCG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.4900 | 0.0200 | No | this paper | Table 8 |

### SAT Solving (Kissat, SATzilla) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RF | 0.6100 | 0.0000 | Yes | this paper | Table 8 |
| XGB | 0.6300 | 0.0000 | Yes | this paper | Table 8 |

### SAT Solving (Kissat, VCG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.1500 | 0.0300 | No | this paper | Table 8 |

### SAT Solving (Kissat, VG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.3600 | 0.1500 | No | this paper | Table 8 |

### SAT Solving (KissatMABDC, VG) — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 1.2700 | — | No | this paper | Table 8 |

### SAT Solving (Large) — Gap closed ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PC | 0.3300 | 0.0100 | Yes | this paper | Table 10 |
| PR | 0.5400 | 0.0200 | Yes | this paper | Table 10 |
| MC | 0.2300 | 0.0200 | Yes | this paper | Table 10 |

### SAT Solving (Medium) — Gap closed ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| PC | 0.1300 | 0.0200 | Yes | this paper | Table 10 |
| PR | 0.4400 | 0.0200 | Yes | this paper | Table 10 |
| MC | -0.1300 | 0.0200 | Yes | this paper | Table 10 |

### SAT Solving (Small) — Gap closed ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0500 | 0.0000 | Yes | this paper | Table 10 |
| PC | 0.0300 | 0.0200 | Yes | this paper | Table 10 |
| PR | 0.4800 | 0.0300 | Yes | this paper | Table 10 |
| MC | -0.3200 | 0.0200 | Yes | this paper | Table 10 |

### Steiner Trees-easy — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.6691 | 0.0288 | Yes | this paper | Table 16 |
| GT | 0.6691 | 0.0112 | No | this paper | Table 16 |

### Steiner Trees-hard — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5516 | 0.2368 | Yes | this paper | Table 16 |
| GT | 0.5212 | 0.0219 | No | this paper | Table 16 |

### Steiner Trees-medium — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.5628 | 0.1100 | Yes | this paper | Table 16 |
| GT | 0.5672 | 0.0790 | No | this paper | Table 16 |

### likes — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DeepSets | 0.8100 | 0.0050 | Yes | this paper | Table 3 |
| DeepSets | 0.1400 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.7680 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.1650 | 0.0020 | Yes | this paper | Table 3 |
| MLP | 0.7840 | 0.0010 | Yes | this paper | Table 3 |
| MLP | 0.1450 | 0.0010 | Yes | this paper | Table 3 |

### quotes — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DeepSets | 0.3070 | 0.0040 | Yes | this paper | Table 3 |
| DeepSets | 0.1780 | 0.0020 | Yes | this paper | Table 3 |
| DeepSets | 0.3340 | 0.0030 | Yes | this paper | Table 3 |
| GNN | 0.3300 | 0.0030 | Yes | this paper | Table 3 |
| GNN | 0.1920 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.3370 | 0.0220 | Yes | this paper | Table 3 |
| MLP | 0.3080 | 0.0030 | Yes | this paper | Table 3 |
| MLP | 0.1760 | 0.0020 | Yes | this paper | Table 3 |
| MLP | 0.3350 | 0.0020 | Yes | this paper | Table 3 |

### replies — R2 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DeepSets | 0.1020 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.1340 | 0.0020 | Yes | this paper | Table 3 |
| MLP | 0.1070 | 0.0010 | Yes | this paper | Table 3 |
| DeepSets | 0.7890 | 0.0330 | Yes | this paper | Table 3 |
| DeepSets | 0.2530 | 0.0030 | Yes | this paper | Table 3 |
| GNN | 0.6940 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.2580 | 0.0090 | Yes | this paper | Table 3 |
| MLP | 0.7250 | 0.0040 | Yes | this paper | Table 3 |
| MLP | 0.2490 | 0.0040 | Yes | this paper | Table 3 |

### reposts — R2 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DeepSets | 0.1380 | 0.0020 | Yes | this paper | Table 3 |
| GNN | 0.1750 | 0.0020 | Yes | this paper | Table 3 |
| MLP | 0.1410 | 0.0010 | Yes | this paper | Table 3 |
| DeepSets | 0.9180 | 0.0130 | Yes | this paper | Table 3 |
| DeepSets | 0.2290 | 0.0040 | Yes | this paper | Table 3 |
| GNN | 0.8320 | 0.0090 | Yes | this paper | Table 3 |
| GNN | 0.2840 | 0.0440 | Yes | this paper | Table 3 |
| MLP | 0.8740 | 0.0030 | Yes | this paper | Table 3 |
| MLP | 0.2340 | 0.0080 | Yes | this paper | Table 3 |

## Baseline Models Identified

- **DeepSets** (from: Zaheer et al. 2017)
- **MLP**
- **MPNN** (from: Gilmer et al. 2017)
- **Graph Transformer** (from: Müller et al. 2023)
- **GIN**
- **GNN**
- **Strash** (from: brayton2010abc)
- **Resyn** (from: brayton2010abc)
- **Compress2** (from: brayton2010abc)
- **Resyn2rs** (from: brayton2010abc)
- **GT**
- **GCN**
- **GAT**
- **RF**
- **XGB**
- **SATzilla**
- **PC**
- **PR**
- **MC**
- **DeepSet**

## Extraction Notes

[Section 1] The provided text contains the introduction, overview, and dataset descriptions of the
GraphBench paper. It lists the datasets and their statistics (Table 1 and Table 2) and mentions the
baselines used (DeepSets, MLP, MPNN, Graph Transformer, GIN). However, the specific quantitative
results tables (e.g., Table 3 mentioned in the text) are not included in the provided excerpt. The
text ends abruptly at the beginning of the 'Results' section for the BlueSky dataset. Therefore, no
numerical performance values (metrics like MAE, Accuracy, etc.) can be extracted from this text.
[Section 2] Table 3 has a complex structure with multiple sub-columns for R2 and sigma corresponding
to different target variables (likes, replies, reposts, quotes). The table header is repeated for
each target variable group (likes, replies, reposts). The extraction assumes the column order is
MAE, R2_likes, R2_replies, R2_reposts, sigma_likes, sigma_replies, sigma_reposts for the 'likes'
dataset row, and similarly for others, though the text representation is ambiguous. Specifically,
for the 'replies' and 'reposts' sections, the first column is MAE, followed by R2 values for
different targets, then sigma values. The exact mapping of columns to specific metrics (e.g., which
R2 column corresponds to which target) is inferred from the pattern but could be misaligned due to
the formatting. Table 5 is referenced in the text but not provided in the input, so no results were
extracted from it. [Section 3] The text mentions Table 6 for the Electronic Circuits benchmark
(comparing GT, GCN, GAT, GIN on RSE), but the actual table content is missing from the provided
text. Only Table 5 (Chip Design / AIG dataset) was fully available and extracted. The metric for
Table 5 is assumed to be Accuracy based on 'Higher is better' and the context of ABC methods, though
the specific metric name is not explicitly stated in the table caption. [Section 4] Table 6 contains
results for two tasks (Efficiency and Voltage) across three dataset sizes (5 comp, 7 comp, 10 comp).
The metric is RSE (Relative Squared Error), where lower is better. The table structure was parsed by
associating the 'Task' column with the subsequent rows of methods. The 'Voltage' task rows follow
the 'Efficiency' task rows in the text representation. [Section 5] The input text cuts off at the
end of Table 8, specifically for the 'KissatMABDC' solver row. The value 1.27 was extracted, but the
standard deviation and subsequent columns (VCG, LCG, SATzilla) are missing. Dataset names were
constructed by combining the 'Solver' column (e.g., Kissat) with the graph representation (e.g., VG)
or feature set (SATzilla) to distinguish the specific experimental conditions. [Section 6] The input
text contains fragmented table data and references to tables (Table 8, 9, 10) that are not fully
visible. The provided text lists results for 'Medium-size SAT instances' and 'Large SAT instances'
under Table 9, but the 'Solver' column is ambiguous (e.g., 'SATzilla', 'Kissat', 'BreakIDKissat'
appear as headers or labels). The 'Method' column lists 'RF' and 'XGB'. The proposed model 'AMSAT'
is mentioned in the text and appears in the fragmented data, but its specific results in Table 9 are
not clearly paired with a metric value in the provided snippet. The extracted results focus on the
clear RF/XGB values in Table 9. The 'Solver' context was inferred from the table structure but may
be incomplete. [Section 7] Table 10 contains results for SAT Solving (Algorithm selection). The
columns VG, VCG, LCG appear to be dataset variants or metrics, but the values are only present for
the 'Method' column (GIN, PC, PR, MC) under specific conditions. The extraction assumes the values
correspond to the 'Gap closed' metric as stated in the caption. The text mentions Tables 12 and 13
for CO results, but these tables are not provided in the input text, so those results could not be
extracted. The proposed model details are inferred from the text description ('Encoder-Decoder
(RWSE+Degree)'), but no specific results for it are present in the provided text. [Section 8] The
provided text is a fragment of a table (Table 12) and does not explicitly state the proposed model
name or the specific metric column header (assumed 'MIS' based on context 'Results for each CO
dataset with supervised learning (MIS)'). The table structure is inferred from the layout (Dataset,
Method, Size, Small, Large). The 'DeepSet' entry for 'ER graph Large' is missing from the text
snippet. The metric is assumed to be a performance score where higher is better, typical for MIS
(Maximum Independent Set) size or approximation ratio, though the exact unit is not specified in the
snippet. [Section 9] failed: JSON parse error from 'glm-4.7': Expecting value: line 1032 column 15
(char 26386) [Section 10] The provided text contains only Table 14, which describes graph generation
parameters for algorithmic reasoning tasks (e.g., Erdős–Rényi, NWS, BA, DBA, PC, SBM generators). It
does not contain any quantitative experimental results, model performance metrics, or benchmark
scores (like Accuracy, MAE, etc.) for a proposed model or baselines. Therefore, no results could be
extracted. [Section 11] The provided text contains descriptions of experimental setup, dataset
generation parameters (Table 15), and qualitative analysis of results for Tables 16, 17, and 18.
However, the actual numerical data for Tables 16, 17, and 18 (containing F1 scores and MAE values)
is missing from the input text. Only the generation parameters in Table 15 were present, which do
not represent model performance results. Therefore, no quantitative results could be extracted.
[Section 12] The input text cuts off at the end of Table 16. The last row (GIN, Max Clique, hard)
has a value (0.4102) but the standard deviation is missing. The corresponding GT row for Max Clique
hard is also missing. The dataset names are constructed by combining the 'Task' and 'Difficulty'
columns (e.g., 'MST-easy') as is standard for these algorithmic reasoning benchmarks. [Section 13]
failed: Request timed out. [Section 14] failed: Request timed out.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*