# Extraction: arXiv:2409.11504
**Model used**: `alias-huge-no-thinking`  **Date**: 2026-05-13  **Confidence**: LOW

## Proposed Model: MRS-GCN_DA
- Type: GCN_variant

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.4621 | 0.0299 | Yes | Rossi 2023 | Table 4 |
| GCN | 0.6482 | 0.0224 | Yes | Rossi 2023 | Table 4 |
| H_2GCN | 0.5939 | 0.0198 | Yes | Rossi 2023 | Table 4 |
| GPR-GNN | 0.6285 | 0.0290 | Yes | Rossi 2023 | Table 4 |
| LINKX | 0.6842 | 0.0138 | Yes | Rossi 2023 | Table 4 |
| FSGNN | 0.7827 | 0.0128 | Yes | Rossi 2023 | Table 4 |
| ACM-GCN | 0.7476 | 0.0220 | Yes | Rossi 2023 | Table 4 |
| GloGNN | 0.7121 | 0.0184 | Yes | Rossi 2023 | Table 4 |
| Grad. Gating | 0.7140 | 0.0238 | Yes | Rossi 2023 | Table 4 |
| DiGCN | 0.5224 | 0.0365 | Yes | Rossi 2023 | Table 4 |
| MagNet | 0.5822 | 0.0287 | Yes | Rossi 2023 | Table 4 |
| Dir-GNN | 0.7971 | 0.0126 | Yes | Rossi 2023 | Table 4 |
| MRS-Dir-GCN_DA | 0.8017 | 0.0188 | No | this paper | Table 4 |

### Roman-Empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.6494 | 0.0062 | Yes | Rossi et al. 2023 | Table 4 |
| GCN | 0.7369 | 0.0074 | Yes | Rossi et al. 2023 | Table 4 |
| H_2GCN | 0.6011 | 0.0052 | Yes | Rossi et al. 2023 | Table 4 |
| GPR-GNN | 0.6485 | 0.0027 | Yes | Rossi et al. 2023 | Table 4 |
| LINKX | 0.3755 | 0.0036 | Yes | Rossi et al. 2023 | Table 4 |
| FSGNN | 0.7992 | 0.0056 | Yes | Rossi et al. 2023 | Table 4 |
| ACM-GCN | 0.6966 | 0.0062 | Yes | Rossi et al. 2023 | Table 4 |
| GloGNN | 0.5963 | 0.0069 | Yes | Rossi et al. 2023 | Table 4 |
| Grad. Gating | 0.8216 | 0.0078 | Yes | Rossi et al. 2023 | Table 4 |
| DiGCN | 0.5271 | 0.0032 | Yes | Rossi et al. 2023 | Table 4 |
| MagNet | 0.8807 | 0.0027 | Yes | Rossi et al. 2023 | Table 4 |
| Dir-GNN | 0.9123 | 0.0032 | Yes | Rossi et al. 2023 | Table 4 |
| MRS-Dir-GCN_DA | 0.9187 | 0.0042 | No | this paper | Table 4 |

### Snap-patents — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.3134 | 0.0005 | Yes | this paper | Table 4 |
| GCN | 0.5102 | 0.0006 | Yes | this paper | Table 4 |
| GPR-GNN | 0.4019 | 0.0003 | Yes | this paper | Table 4 |
| LINKX | 0.6195 | 0.0012 | Yes | this paper | Table 4 |
| FSGNN | 0.6507 | 0.0003 | Yes | this paper | Table 4 |
| ACM-GCN | 0.5514 | 0.0016 | Yes | this paper | Table 4 |
| GloGNN | 0.6209 | 0.0027 | Yes | this paper | Table 4 |
| Grad. Gating | 0.6950 | 0.0039 | Yes | this paper | Table 4 |
| Dir-GNN | 0.7395 | 0.0005 | Yes | Rossi et al. 2023 | Table 4 |
| MRS-Dir-GCN_DA | 0.7472 | 0.0005 | No | this paper | Table 4 |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.2877 | 0.0156 | Yes | this paper | Table~\ref{tab:hetero} |
| GCN | 0.5343 | 0.0201 | Yes | this paper | Table~\ref{tab:hetero} |
| H_2GCN | 0.3790 | 0.0202 | Yes | this paper | Table~\ref{tab:hetero} |
| GPR-GNN | 0.5435 | 0.0087 | Yes | this paper | Table~\ref{tab:hetero} |
| LINKX | 0.6181 | 0.0180 | Yes | this paper | Table~\ref{tab:hetero} |
| FSGNN | 0.7410 | 0.0189 | Yes | this paper | Table~\ref{tab:hetero} |
| ACM-GCN | 0.6740 | 0.0221 | Yes | this paper | Table~\ref{tab:hetero} |
| GloGNN | 0.5788 | 0.0176 | Yes | this paper | Table~\ref{tab:hetero} |
| Grad. Gating | 0.6426 | 0.0238 | Yes | this paper | Table~\ref{tab:hetero} |
| DiGCN | 0.3774 | 0.0154 | Yes | this paper | Table~\ref{tab:hetero} |
| MagNet | 0.3901 | 0.0193 | Yes | this paper | Table~\ref{tab:hetero} |
| Dir-GNN | 0.7531 | 0.0192 | Yes | this paper | Table~\ref{tab:hetero} |
| MRS-Dir-GCN_DA | 0.7601 | 0.0190 | No | this paper | Table~\ref{tab:hetero} |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.1550 | 0.0030 | Yes | this paper | tab:zinc_full |
| MRS-GCN_DA | 0.1340 | 0.0010 | No | this paper | tab:zinc_full |
| SAGE | 0.1230 | 0.0020 | Yes | this paper | tab:zinc_full |
| MRS-SAGE_DA | 0.1060 | 0.0020 | No | this paper | tab:zinc_full |
| GAT | 0.1490 | 0.0010 | Yes | this paper | tab:zinc_full |
| MRS-GAT_DA | 0.1280 | 0.0000 | No | this paper | tab:zinc_full |
| GIN | 0.1230 | 0.0040 | Yes | this paper | tab:zinc_full |
| MRS-GIN_DA | 0.1060 | 0.0040 | No | this paper | tab:zinc_full |
| GatedGCN | 0.0990 | 0.0110 | Yes | this paper | tab:zinc_full |
| MRS-GatedGCN_DA | 0.0880 | 0.0040 | No | this paper | tab:zinc_full |

### ZINC12k — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4040 | 0.0110 | Yes | this paper | Table 1 |
| MRS-GCN_DA (random) | 0.6230 | 0.0030 | No | this paper | Table 1 |
| MRS-GCN_DA (Features) | 0.3900 | 0.0040 | No | this paper | Table 1 |
| MRS-GCN_DA (PPR) | 0.3580 | 0.0060 | No | this paper | Table 1 |
| MRS-GCN_DA (Degree) | 0.3180 | 0.0310 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN**
- **SAGE**
- **GAT** (from: Veličković et al. 2018)
- **GIN** (from: Xu et al. 2018)
- **GatedGCN** (from: Dwivedi et al. 2023)
- **MLP**
- **H_2GCN**
- **GPR-GNN**
- **LINKX**
- **FSGNN**
- **ACM-GCN**
- **GloGNN**
- **Grad. Gating**
- **DiGCN**
- **MagNet**
- **Dir-GNN** (from: Rossi et al. 2023)

## Extraction Notes

[ZINC12k] Extracted only the main ZINC12k results table. Excluded the ZINC (non-12k) dataset table,
the directed benchmark graphs table, and all hyperparameter/runtime/parameter-count tables. Also
excluded the ZINC12k layer-ablation table because it reports multiple optional configurations
(varying layer counts and architectural variants Res/JK/LapPE), which falls under optional variants
per the focus instructions. Parameter counts were unavailable because the parameter-count table was
cut off in the provided text. [ZINC] Extracted Test MAE results for the ZINC dataset from Table
tab:zinc_full. Results for ZINC12k in other tables were excluded per the focus instruction. Train
MAE columns were skipped. The parameter count table (tab:parameter_count) was cut off in the
provided text, so parameter counts could not be extracted. No external pre-training data is
mentioned. [Squirrel] Accuracy values were normalized from percentages (e.g., 76.01%) to [0,1] by
dividing by 100. The text refers to the proposed method as MRS-MPNN (and MRS-GCN_DA for this
dataset), while the results table uses the exact name MRS-Dir-GCN_DA; the table name was used for
the result row. Parameter counts are not reported for these experiments. The text states that
baseline results were reused from a reference implementation by Rossi et al. 2023, but since all
values appear in the current paper's table, source_ref is set to 'this paper' for all rows.
[Chameleon] Accuracy values in Table 4 were reported as percentages and have been normalized to
[0,1]. Parameter counts are not provided for Chameleon or the heterophilic graph experiments. The
table number was inferred from the order of appearance in the source text. [Arxiv-year] failed: 1
validation error for ExtractionOutput   Input should be a valid dictionary or instance of
ExtractionOutput [type=model_type, input_value=[{'name': 'MLP', 'params_...': 'Rossi et al. 2023'}],
input_type=list]     For further information visit https://errors.pydantic.dev/2.13/v/model_type
[Snap-patents] Accuracy values were reported as percentages in Table 4 (tab:hetero) and were
normalized to [0,1]. H_2GCN, DiGCN, and MagNet reported OOM (out of memory) for Snap-patents and
were excluded because they lack quantitative values. Parameter counts were not provided for the
heterophilic/directed graph experiments. The proposed model is listed in the table as MRS-Dir-
GCN_DA, which corresponds to the paper's MRS-MPNN framework instantiated on top of Dir-GNN. [Roman-
Empire] The text states that MRS-SAGE_DA is used for Roman-Empire, but the results table (Table 4 /
tab:hetero) lists the proposed row as MRS-Dir-GCN_DA for all five datasets including Roman-Empire.
Parameter counts are not reported for Roman-Empire. All baseline results are explicitly noted as
reused from the reference implementation of Rossi et al. 2023. Values were given as percentages and
have been normalised to [0,1]. [Peptides-Func] The provided paper excerpts contain no results for
'Peptides-Func'. All included tables report only ZINC, ZINC12k, Squirrel, Chameleon, Arxiv-year,
Snap-patents, and Roman-Empire. Consequently, no AP scores or other Peptides-Func metrics could be
extracted. [Peptides-Struct] The provided paper text does not contain any results for the dataset
'Peptides-Struct'. All tables report results for ZINC, ZINC12k, and directed node-classification
benchmarks (Squirrel, Chameleon, Arxiv-year, Snap-patents, Roman-Empire) only. No MAE or other
metrics for Peptides-Struct were found. The parameter-count table (Table 5) was truncated and could
not be parsed. [Cora] The paper text mentions experiments on Cora and refers to Table~\ref{tab:homo}
for results, but the actual table is not included in the provided excerpts. The text only provides a
qualitative statement that MRS-GCN_DA achieves lower accuracy than GCN on Cora, without reporting
any numerical values. Consequently, no quantitative results for Cora could be extracted. [CiteSeer]
The text references Table~\ref{tab:homo} for Cora, CiteSeer, and PubMed results, but this table was
not included in the provided paper excerpt. No quantitative accuracy values (or any other metrics)
for CiteSeer are present in the pasted text or tables. All provided tables cover ZINC, ZINC12k,
directed heterophilic benchmarks, hyperparameters, runtimes, and parameter counts only. [PubMed] The
paper text describes PubMed experiments and cites Table~\ref{tab:homo} for the quantitative results,
but that table was not included in the provided excerpts. All pasted tables report only ZINC/ZINC12k
results or directed heterophilic node classification results (Squirrel, Chameleon, Arxiv-year, Snap-
patents, Roman-Empire). Therefore, no accuracy values for PubMed could be extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*