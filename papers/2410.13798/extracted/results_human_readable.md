# Extraction: arXiv:2410.13798
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: GQT
- Type: GNN

## Results

### COCO-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.0841 | 0.0010 | Yes | this paper | Table ef{tab:LRGB} |
| Exphormer | 0.3430 | 0.0108 | Yes | this paper | Table ef{tab:LRGB} |
| GPS | 0.3412 | 0.0044 | Yes | this paper | Table ef{tab:LRGB} |
| Graph-Mamba | 0.3960 | 0.0175 | Yes | this paper | Table ef{tab:LRGB} |
| GQT (Ours) | 0.4007 | 0.0125 | No | this paper | Table ef{tab:LRGB} |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7650 | 0.0136 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GAT | 0.7655 | 0.0123 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| APPNP | 0.7653 | 0.0116 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GPRGNN | 0.7713 | 0.0167 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphSAGE | 0.7558 | 0.0133 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphGPS | 0.7699 | 0.0112 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GOAT | 0.7689 | 0.0119 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| NodeFormer | 0.7633 | 0.0059 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| DIFFormer | 0.7672 | 0.0068 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| NAGphormer | 0.7742 | 0.0141 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| Exphormer | 0.7683 | 0.0124 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GQT (ours) | 0.7784 | 0.0094 | No | this paper | Table 1 |

### CoraFull — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6176 | 0.0014 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GAT | 0.6447 | 0.0018 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| APPNP | 0.6516 | 0.0028 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GPRGNN | 0.6712 | 0.0031 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphSAINT | 0.6785 | 0.0021 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| PPRGo | 0.6354 | 0.0025 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GRAND+ | 0.7137 | 0.0011 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GT | 0.6105 | 0.0038 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| SAN | 0.5901 | 0.0034 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphGPS | 0.5576 | 0.0023 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| NAGphormer | 0.7151 | 0.0013 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| Exphormer | 0.6909 | 0.0072 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| VCR-Graphormer | 0.7167 | 0.0010 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GQT (ours) | 0.7181 | 0.0021 | No | this paper | Table 1 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| RQ-VAE | 0.8969 | 0.0035 | Yes | this paper | Table 4 |
| GQT (ours) | 0.9528 | 0.0044 | No | this paper | Table 4 |
| Linear | 0.9024 | 0.0049 | Yes | this paper | Table 6 |
| Transformer (2) | 0.9052 | 0.0039 | Yes | this paper | Table 6 |
| Transformer (3) | 0.9527 | 0.0046 | Yes | this paper | Table 6 |
| Transformer (4) | 0.9291 | 0.0055 | Yes | this paper | Table 6 |
| Transformer (5) | 0.9382 | 0.0046 | Yes | this paper | Table 6 |
| Transformer (6) | 0.9324 | 0.0036 | Yes | this paper | Table 6 |
| Transformer (7) | 0.9482 | 0.0041 | Yes | this paper | Table 6 |
| Transformer (8) | 0.9397 | 0.0058 | Yes | this paper | Table 6 |
| Transformer (9) | 0.9283 | 0.0035 | Yes | this paper | Table 6 |
| Transformer (10) | 0.9528 | 0.0044 | No | this paper | Table 6 |

### PCQM-Contact — MRR ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3234 | 0.0006 | Yes | this paper | Table ef{tab:LRGB} |
| Exphormer | 0.3587 | 0.0025 | Yes | this paper | Table ef{tab:LRGB} |
| GPS | 0.3337 | 0.0006 | Yes | this paper | Table ef{tab:LRGB} |
| Graph-Mamba | 0.3395 | 0.0013 | Yes | this paper | Table ef{tab:LRGB} |
| GQT (Ours) | 0.3427 | 0.0012 | No | this paper | Table ef{tab:LRGB} |

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.5930 | 0.0023 | Yes | this paper | Table ef{tab:LRGB} |
| Exphormer | 0.6258 | 0.0092 | Yes | this paper | Table ef{tab:LRGB} |
| GPS | 0.6535 | 0.0041 | Yes | this paper | Table ef{tab:LRGB} |
| Graph-Mamba | 0.6739 | 0.0087 | Yes | this paper | Table ef{tab:LRGB} |
| GQT (Ours) | 0.6903 | 0.0085 | No | this paper | Table ef{tab:LRGB} |

### Peptides-Struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3496 | 0.0013 | Yes | this paper | Table ef{tab:LRGB} |
| Exphormer | 0.2512 | 0.0025 | Yes | this paper | Table ef{tab:LRGB} |
| GPS | 0.2500 | 0.0005 | Yes | this paper | Table ef{tab:LRGB} |
| Graph-Mamba | 0.2478 | 0.0016 | Yes | this paper | Table ef{tab:LRGB} |
| GQT (Ours) | 0.2452 | 0.0018 | No | this paper | Table ef{tab:LRGB} |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8654 | 0.0012 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GAT | 0.8632 | 0.0016 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| APPNP | 0.8843 | 0.0015 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GPRGNN | 0.8934 | 0.0025 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphSAINT | 0.8896 | 0.0016 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphSAGE | 0.8748 | 0.0038 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| PPRGo | 0.8738 | 0.0011 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GRAND+ | 0.8864 | 0.0009 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GT | 0.8879 | 0.0012 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| SAN | 0.8822 | 0.0015 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GraphGPS | 0.8894 | 0.0016 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GOAT | 0.8687 | 0.0024 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| NodeFormer | 0.8932 | 0.0025 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| DIFFormer | 0.8951 | 0.0067 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| NAGphormer | 0.8970 | 0.0019 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| Exphormer | 0.8952 | 0.0054 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| VCR-Graphormer | 0.8977 | 0.0015 | Yes | wu2023simplifying, luo2024structure | Table 1 |
| GQT (ours) | 0.9014 | 0.0016 | No | this paper | Table 1 |

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7174 | 0.0029 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GAT | 0.7195 | 0.0036 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GPRGNN | 0.7110 | 0.0012 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| LINKX | 0.6618 | 0.0033 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GraphSAGE | 0.7149 | 0.0027 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| SIGN | 0.7195 | 0.0011 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GraphGPS | 0.7097 | 0.0041 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GOAT | 0.7241 | 0.0040 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| NodeFormer | 0.5990 | 0.0042 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| SGFormer | 0.7263 | 0.0013 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| NAGphormer | 0.7013 | 0.0055 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| Exphormer | 0.7244 | 0.0028 | Yes | wu2023simplifying, luo2024structure | Table 3 |
| GQT(ours) | 0.7314 | 0.0016 | No | this paper | Table 3 |
| RQ-VAE | 0.6605 | 0.0048 | Yes | this paper | Table 5 |
| GQT (ours) | 0.7314 | 0.0016 | No | this paper | Table 5 |

## Baseline Models Identified

- **GCN**
- **Exphormer**
- **GPS**
- **Graph-Mamba**
- **GAT**
- **APPNP** (from: gasteiger2018predict)
- **GPRGNN** (from: chien2020adaptive)
- **GraphSAINT** (from: zeng2019graphsaint)
- **GraphSAGE** (from: hamilton2017inductive)
- **PPRGo** (from: bojchevski2020scaling)
- **GRAND+** (from: feng2022grand+)
- **GT** (from: dwivedi2020generalization)
- **Graphormer** (from: ying2021transformers)
- **SAN** (from: kreuzer2021rethinking)
- **GraphGPS** (from: rampavsek2022recipe)
- **GOAT** (from: kong2023goat)
- **NodeFormer** (from: wu2022nodeformer)
- **DIFFormer** (from: wu2023difformer)
- **NAGphormer** (from: chen2023nagphormer)
- **VCR-Graphormer** (from: fu2024vcrgraphormer)
- **H2GCN** (from: zhu2020hybrid)
- **CPGNN** (from: zhu2021graph)
- **GloGNN** (from: li2022finding)
- **SGFormer**
- **GTAND+** (from: feng2022grand+)
- **DiffFormer** (from: wu2023difformer)
- **LINKX** (from: lim2021large)
- **SIGN** (from: frasca2020sign)
- **RQ-VAE** (from: lee2022autoregressive)
- **Linear**

## Extraction Notes

[Peptides-Func] Extracted only Peptides-Func results as requested. Baselines are listed as 'this
paper' because they are presented in the results table of the current text, although the text
mentions comparing to results reported in Wang 2024. [Peptides-Struct] Extracted only Peptides-
Struct results as requested. Baselines are listed as 'this paper' because they are reported in the
provided table, although the text mentions they are compared to results from Wang 2024. [COCO-SP]
Extracted only COCO-SP results as requested. Baselines are listed as 'this paper' because the table
presents them as direct comparisons, although the text mentions they were reported in Wang 2024.
[PCQM-Contact] Extracted only PCQM-Contact results as requested. Model type for GQT is inferred as
GNN based on context. [CoraFull] GraphSAGE, GOAT, NodeFormer, and DIFFormer had no reported values
for CoraFull. Graphormer was marked as OOM (Out of Memory). [CiteSeer] Extracted only CiteSeer
results as requested. Normalized percentages to [0, 1] range. Models with '-' or 'OOM' for CiteSeer
were skipped. [PubMed] Extracted only PubMed results from Table 1. Graphormer was marked as OOM (Out
of Memory) for PubMed and thus excluded from the results list. [Computer] The user requested results
ONLY for the dataset 'Computer'. While the text mentions 'Amazon Computers' as one of the homophilic
datasets used, the provided table (Table 1) only contains results for heterophilic datasets
(Squirrel, Chameleon, Amazon-Ratings, Roman-Empire, Minesweeper, Questions). No quantitative results
for 'Computer' or 'Amazon Computers' were present in the provided text or tables. [Photo] The user
requested results ONLY for the dataset 'Photo'. While the text mentions 'Amazon Photos' as a dataset
used for homophilic node classification, the provided table (Table 1) only contains results for
heterophilic datasets (Squirrel, Chameleon, Amazon-Ratings, Roman-Empire, Minesweeper, Questions).
No quantitative results for 'Photo' or 'Amazon Photos' were present in the provided text or tables.
[CS] The user requested results ONLY for the dataset 'CS' (Co-author CS). While the text mentions
'Co-author CS' as one of the datasets used for homophilic node classification, the provided table
(Table 1) only contains results for heterophilic datasets (Squirrel, Chameleon, Amazon-Ratings,
Roman-Empire, Minesweeper, Questions). The table containing the 'CS' results (referenced as Table
2/tab:results_small_homophilic in the text) was not provided in the input text. Therefore, no
quantitative results for 'CS' could be extracted. [Physics] The user requested results ONLY for the
dataset 'Physics'. While the text mentions the 'Physics' dataset and refers to Table 1
(tab:results_small_homophilic) for its results, the provided table snippet only contains Table 2
(tab:results_heterophilic), which lists heterophilic datasets (Squirrel, Chameleon, etc.). Since the
actual data for 'Physics' was not included in the provided table text, no quantitative results could
be extracted. [WikiCS] The user requested results ONLY for the dataset 'WikiCS'. While the text
mentions 'WikiCS' as one of the datasets used for homophilic node classification and refers to Table
1 (tab:results_small_homophilic) for those results, the provided table snippet only contains Table 2
(tab:results_heterophilic), which covers heterophilic datasets (Squirrel, Chameleon, etc.).
Therefore, no quantitative results for 'WikiCS' were available in the provided text/tables. [ogbn-
arxiv] Extracted results from the main results table (Table 3) and the generalization analysis table
(Table 5). Ablation study results were skipped as they represent model variants rather than the
standard configuration. [Minesweeper] Extracted results from the Generalization Analysis table and
the Ablation Study table. In the ablation table, the 'Transformer' rows are variants of the proposed
model; row (10) corresponds to the full GQT model. Values were divided by 100 to normalize ROC-AUC
to [0, 1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*