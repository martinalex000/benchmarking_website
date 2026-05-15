# Extraction: arXiv:2503.09008
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Results

### London — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.2790 | 0.0010 | Yes | this paper | Table 1 |
| ChebNet | 0.5470 | 0.0020 | Yes | this paper | Table 1 |
| GCN | 0.5010 | 0.0070 | Yes | this paper | Table 1 |
| GraphSAGE | 0.5540 | 0.0020 | Yes | this paper | Table 1 |
| GAT | 0.5200 | 0.0030 | Yes | this paper | Table 1 |
| GCNII | 0.4820 | 0.0030 | Yes | this paper | Table 1 |
| DropEdge | 0.4500 | 0.0030 | Yes | this paper | Table 1 |
| Exphormer | 0.4950 | 0.0040 | Yes | this paper | Table 1 |
| SGFormer | 0.4830 | 0.0030 | Yes | this paper | Table 1 |

### Los Angeles — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.2410 | 0.0050 | Yes | this paper | Table 1 |
| ChebNet | 0.6140 | 0.0040 | Yes | this paper | Table 1 |
| GCN | 0.5830 | 0.0030 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6140 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.5950 | 0.0030 | Yes | this paper | Table 1 |
| GCNII | 0.5600 | 0.0030 | Yes | this paper | Table 1 |
| DropEdge | 0.5550 | 0.0030 | Yes | this paper | Table 1 |
| GraphGPS | 0.5980 | 0.0050 | Yes | this paper | Table 1 |
| Exphormer | 0.6380 | 0.0060 | Yes | this paper | Table 1 |
| SGFormer | 0.6010 | 0.0070 | Yes | this paper | Table 1 |

### Paris — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.2550 | 0.0040 | Yes | this paper | Table 1 |
| ChebNet | 0.5410 | 0.0020 | Yes | this paper | Table 1 |
| GCN | 0.5320 | 0.0030 | Yes | this paper | Table 1 |
| GraphSAGE | 0.5460 | 0.0020 | Yes | this paper | Table 1 |
| GAT | 0.5110 | 0.0030 | Yes | this paper | Table 1 |
| GCNII | 0.5130 | 0.0020 | Yes | this paper | Table 1 |
| DropEdge | 0.4820 | 0.0020 | Yes | this paper | Table 1 |
| GraphGPS | 0.5210 | 0.0060 | Yes | this paper | Table 1 |
| Exphormer | 0.5510 | 0.0080 | Yes | this paper | Table 1 |
| SGFormer | 0.5200 | 0.0080 | Yes | this paper | Table 1 |

### Shanghai — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.2840 | 0.0060 | Yes | this paper | Table 1 |
| ChebNet | 0.6650 | 0.0010 | Yes | this paper | Table 1 |
| GCN | 0.6210 | 0.0020 | Yes | this paper | Table 1 |
| GraphSAGE | 0.6830 | 0.0050 | Yes | this paper | Table 1 |
| GAT | 0.6800 | 0.0050 | Yes | this paper | Table 1 |
| GCNII | 0.6150 | 0.0040 | Yes | this paper | Table 1 |
| DropEdge | 0.6080 | 0.0040 | Yes | this paper | Table 1 |
| GraphGPS | 0.6300 | 0.0050 | Yes | this paper | Table 1 |
| Exphormer | 0.7020 | 0.0040 | Yes | this paper | Table 1 |
| SGFormer | 0.6410 | 0.0030 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **MLP**
- **ChebNet**
- **GCN** (from: kipf2017semi)
- **GraphSAGE** (from: hamilton2017inductive)
- **GAT**
- **GCNII**
- **DropEdge**
- **GraphGPS**
- **Exphormer** (from: shirzad2023exphormer)
- **SGFormer** (from: wu2023simplifying)

## Extraction Notes

[Paris] Extracted results for Paris from Table 1. Values were reported as percentages (e.g., 25.5)
and normalized to [0, 1] as per instructions. No proposed model was explicitly listed in the results
table provided; only baselines were reported. [Shanghai] The provided text only contains baseline
results in Table 1; the proposed model's results for Shanghai were not present in the provided
snippet. Values were normalized from percentages to [0, 1] range. [Los Angeles] The provided text
only contains a table of baseline results; the proposed model's results for Los Angeles are not
present in the provided snippet. Values were normalized from percentages to [0, 1]. [London]
GraphGPS was marked as 'OOM' (Out-of-Memory) for the London dataset and thus no quantitative value
was extracted for it. All other values were normalized from percentages to [0, 1] range. [Cora] The
paper mentions the 'Cora' dataset and provides several tables containing data for it. However, the
tables provided (Table 1, Table 3, Table 4, Table 6, Table 7) contain dataset statistics, receptive
field sizes (R), and eigenvalue lower bounds. There are no tables reporting the primary benchmark
metric 'Accuracy' for the Cora dataset. The text mentions that performance degrades as L increases
on Cora, but no quantitative accuracy values are listed in the provided text or tables. [ogbn-arxiv]
The paper mentions 'ogbn-arxiv' as a benchmark dataset and provides statistics (Table 1) and a
specific diagnostic metric 'Average size of the influence-weighted receptive field R' (Table 3 and
Table 8). However, no quantitative results for the PRIMARY METRIC 'Accuracy' (or any other
performance metric) for the 'ogbn-arxiv' dataset are reported in the provided text or tables. Table
2 only contains results for 'City-Networks' (Paris, Shanghai, Los Angeles, London). [Amazon-Ratings]
The paper mentions 'Amazon-Ratings' in several tables, but these tables report statistics (Table 1),
the influence-weighted receptive field R (Table 3, Table 7, Table 8), or eigenvalue lower bounds
(Table 4). No quantitative benchmark results for the primary metric 'Accuracy' (or any other
performance metric) were provided for the Amazon-Ratings dataset in the provided text. Table 2 only
contains results for City-Networks. [PascalVOC-SP] The paper mentions benchmarking on 'PascalVOC-SP'
and discusses the results in the text and Figure 1, but the provided tables (Table 1, 2, 3, 4, 5, 6,
7) do not contain the quantitative performance metrics (F1/Accuracy) for PascalVOC-SP. Table 3, 6,
and 7 report the 'Average size of the influence-weighted receptive field R', which is a diagnostic
measure, not a benchmark performance metric like F1. Table 4 reports a 'Lower Bound' eigenvalue. No
F1 or Accuracy values for PascalVOC-SP were present in the provided text or tables. [Roman] The user
requested results for the dataset 'Roman' with a primary metric of 'Accuracy'. While the dataset
'Roman' appears in Table 7 (tab:R heterophilic), the values reported in that table are for the
'Average size of the influence-weighted receptive field R', which is a diagnostic metric, not a
performance metric like Accuracy. No Accuracy results for the 'Roman' dataset were provided in the
text or tables. [Wisconsin] The user requested results for the dataset 'Wisconsin' with a primary
metric of 'Accuracy'. While 'Wisconsin' appears in Table 7 (tab:R heterophilic), that table reports
the 'Average size of the influence-weighted receptive field R', which is a diagnostic metric, not a
performance metric like Accuracy. No tables in the provided text contain Accuracy or other benchmark
performance results for the Wisconsin dataset. [Texas] The user requested results for the dataset
'Texas' with a primary metric of 'Accuracy'. While 'Texas' appears in Table 7 (tab:R heterophilic),
the values reported in that table are for the 'Average size of the influence-weighted receptive
field R', which is a diagnostic metric, not a performance metric like Accuracy. No Accuracy results
for the 'Texas' dataset were provided in the provided text or tables. [Cornell] The dataset
'Cornell' is mentioned in the text and appears in Table 8 (tab:R heterophilic). However, the values
reported in that table are for the 'Average size of the influence-weighted receptive field R', which
is a diagnostic metric, not the primary benchmark metric 'Accuracy'. No accuracy results for the
Cornell dataset were provided in the provided text or tables.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*