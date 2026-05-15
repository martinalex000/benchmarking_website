# Extraction: arXiv:2501.09821
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: BNPool
- Type: GNN

## Results

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DiffPool | 0.3790 | 0.0140 | Yes | this paper | Table 1 |
| MinCut | 0.5430 | 0.0500 | Yes | this paper | Table 1 |
| DMon | 0.5070 | 0.0240 | Yes | this paper | Table 1 |
| JBGNN | 0.4810 | 0.0500 | Yes | this paper | Table 1 |
| BNPool | 0.4790 | 0.0170 | No | this paper | Table 1 |

### Collab — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7000 | 0.0400 | Yes | this paper | Table 1 |
| Graclus | 0.7200 | 0.0300 | Yes | this paper | Table 1 |
| ECPool | 0.7200 | 0.0300 | Yes | this paper | Table 1 |
| KMIS | 0.7100 | 0.0200 | Yes | this paper | Table 1 |
| TopK | 0.7200 | 0.0200 | Yes | this paper | Table 1 |
| SEP | 0.7200 | 0.0300 | Yes | this paper | Table 1 |
| DiffPool | 0.7000 | 0.0200 | Yes | this paper | Table 1 |
| MinCut | 0.7000 | 0.0200 | Yes | this paper | Table 1 |
| DMON | 0.6800 | 0.0200 | Yes | this paper | Table 1 |
| JBGN | 0.7200 | 0.0200 | Yes | this paper | Table 1 |
| Eigen | 0.7300 | 0.0300 | Yes | this paper | Table 1 |
| HOSC | 0.7300 | 0.0200 | Yes | this paper | Table 1 |
| BNPool | 0.7500 | 0.0200 | No | this paper | Table 1 |

### Colors3 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7400 | 0.0900 | Yes | this paper | Table 1 |
| Graclus | 0.6800 | 0.0100 | Yes | this paper | Table 1 |
| ECPool | 0.6900 | 0.0200 | Yes | this paper | Table 1 |
| KMIS | 0.8400 | 0.0100 | Yes | this paper | Table 1 |
| TopK | 0.7800 | 0.0100 | Yes | this paper | Table 1 |
| SepPool | 0.7100 | 0.0100 | Yes | this paper | Table 1 |
| DiffPool | 0.6500 | 0.0100 | Yes | this paper | Table 1 |
| MinCut | 0.6900 | 0.0100 | Yes | this paper | Table 1 |
| DMON | 0.6900 | 0.0200 | Yes | this paper | Table 1 |
| JBGN | 0.6800 | 0.0200 | Yes | this paper | Table 1 |
| EigenPool | 0.4000 | 0.0200 | Yes | this paper | Table 1 |
| HOSC | 0.7200 | 0.0100 | Yes | this paper | Table 1 |
| BNPool | 0.9900 | 0.0000 | No | this paper | Table 1 |

### Community — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DiffPool | 0.8190 | 0.0130 | Yes | this paper | Table 1 |
| MinCut | 0.9710 | 0.0030 | Yes | this paper | Table 1 |
| DMon | 0.9620 | 0.0090 | Yes | this paper | Table 1 |
| JBGNN | 0.8390 | 0.0870 | Yes | this paper | Table 1 |
| BNPool | 0.9850 | 0.0050 | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DiffPool | 0.5040 | 0.0110 | Yes | this paper | Table 1 |
| MinCut | 0.5700 | 0.0210 | Yes | this paper | Table 1 |
| DMon | 0.5790 | 0.0380 | Yes | this paper | Table 1 |
| JBGNN | 0.5540 | 0.0240 | Yes | this paper | Table 1 |
| BNPool | 0.6680 | 0.0100 | No | this paper | Table 1 |

### DBLP — ACC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DiffPool | 0.4950 | 0.0490 | Yes | this paper | Table 1 |
| DiffPool | 0.5740 | 0.0000 | Yes | this paper | Table 1 |
| MinCut | 0.6920 | 0.0340 | Yes | this paper | Table 1 |
| MinCut | 0.5250 | 0.0390 | Yes | this paper | Table 1 |
| DMon | 0.6370 | 0.0320 | Yes | this paper | Table 1 |
| DMon | 0.4540 | 0.0130 | Yes | this paper | Table 1 |
| JBGNN | 0.6860 | 0.0180 | Yes | this paper | Table 1 |
| JBGNN | 0.5300 | 0.0440 | Yes | this paper | Table 1 |
| BNPool | 0.7520 | 0.0070 | No | this paper | Table 1 |
| BNPool | 0.5850 | 0.0070 | No | this paper | Table 1 |

### Enzymes — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.3300 | 0.1300 | Yes | this paper | Table 1 |
| Graclus | 0.3300 | 0.0700 | Yes | this paper | Table 1 |
| ECPool | 0.3500 | 0.0800 | Yes | this paper | Table 1 |
| KMIS | 0.3300 | 0.0800 | Yes | this paper | Table 1 |
| TopK | 0.2900 | 0.0700 | Yes | this paper | Table 1 |
| SepPool | 0.4000 | 0.0600 | Yes | this paper | Table 1 |
| DiffPool | 0.3600 | 0.0700 | Yes | this paper | Table 1 |
| MinCut | 0.3400 | 0.0900 | Yes | this paper | Table 1 |
| DMon | 0.3700 | 0.0700 | Yes | this paper | Table 1 |
| JBGN | 0.3900 | 0.0600 | Yes | this paper | Table 1 |
| EigenPool | 0.3900 | 0.0600 | Yes | this paper | Table 1 |
| HOSC | 0.3600 | 0.0900 | Yes | this paper | Table 1 |
| BNPool | 0.5400 | 0.0700 | No | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7800 | 0.1300 | Yes | this paper | Table 1 |
| Graclus | 0.8200 | 0.1200 | Yes | this paper | Table 1 |
| ECPool | 0.8400 | 0.1200 | Yes | this paper | Table 1 |
| KMIS | 0.8300 | 0.1000 | Yes | this paper | Table 1 |
| TopK | 0.8200 | 0.1000 | Yes | this paper | Table 1 |
| SEP | 0.8100 | 0.0900 | Yes | this paper | Table 1 |
| DiffPool | 0.8100 | 0.1100 | Yes | this paper | Table 1 |
| MinCut | 0.8100 | 0.1200 | Yes | this paper | Table 1 |
| DMON | 0.8200 | 0.1100 | Yes | this paper | Table 1 |
| JBGN | 0.8700 | 0.1400 | Yes | this paper | Table 1 |
| Eigen | 0.6900 | 0.1200 | Yes | this paper | Table 1 |
| HOSC | 0.8400 | 0.0700 | Yes | this paper | Table 1 |
| BNPool | 0.8800 | 0.0700 | No | this paper | Table 1 |

### MolHiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7400 | 0.0200 | Yes | this paper | Table 1 |
| Graclus | 0.7400 | 0.0300 | Yes | this paper | Table 1 |
| ECPool | 0.7400 | 0.0100 | Yes | this paper | Table 1 |
| KMIS | 0.7400 | 0.0200 | Yes | this paper | Table 1 |
| TopK | 0.7600 | 0.0100 | Yes | this paper | Table 1 |
| SEP | 0.7500 | 0.0000 | Yes | this paper | Table 1 |
| DiffPool | 0.7000 | 0.0400 | Yes | this paper | Table 1 |
| MinCut | 0.7600 | 0.0100 | Yes | this paper | Table 1 |
| DMON | 0.7700 | 0.0100 | Yes | this paper | Table 1 |
| JBGN | 0.7300 | 0.0200 | Yes | this paper | Table 1 |
| EigenPool | 0.7400 | 0.0200 | Yes | this paper | Table 1 |
| HOSC | 0.7400 | 0.0200 | Yes | this paper | Table 1 |
| BNPool | 0.7800 | 0.0100 | No | this paper | Table 1 |

### Multip. — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.1400 | 0.1200 | Yes | this paper | Table 1 |
| Graclus | 0.4800 | 0.0200 | Yes | this paper | Table 1 |
| ecpool | 0.5100 | 0.0200 | Yes | this paper | Table 1 |
| kmis | 0.6300 | 0.0200 | No | this paper | Table 1 |
| topk | 0.4500 | 0.0300 | Yes | this paper | Table 1 |
| sep | 0.6100 | 0.0200 | Yes | this paper | Table 1 |
| DiffPool | 0.5600 | 0.0300 | Yes | this paper | Table 1 |
| mincut | 0.5600 | 0.0300 | Yes | this paper | Table 1 |
| dmon | 0.6200 | 0.0300 | Yes | this paper | Table 1 |
| jbgnn | 0.5600 | 0.0300 | Yes | this paper | Table 1 |
| eigen | 0.6100 | 0.0200 | Yes | this paper | Table 1 |
| hosc | 0.4900 | 0.0700 | Yes | this paper | Table 1 |
| bnpool | 0.5800 | 0.0200 | Yes | this paper | Table 1 |

### Mutagenicity — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7800 | 0.0100 | Yes | this paper | Table 1 |
| Graclus | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| ECPool | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| KMIS | 0.7900 | 0.0200 | Yes | this paper | Table 1 |
| TopK | 0.7500 | 0.0300 | Yes | this paper | Table 1 |
| SEP | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| DiffPool | 0.7800 | 0.0200 | Yes | this paper | Table 1 |
| MinCut | 0.7800 | 0.0300 | Yes | this paper | Table 1 |
| DMON | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| JBGN | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| EigenPool | 0.7900 | 0.0200 | Yes | this paper | Table 1 |
| HOSC | 0.8000 | 0.0200 | Yes | this paper | Table 1 |
| BNPool | 0.8100 | 0.0100 | No | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7300 | 0.0300 | Yes | this paper | Table 1 |
| Graclus | 0.7700 | 0.0200 | Yes | this paper | Table 1 |
| ECPool | 0.7700 | 0.0300 | Yes | this paper | Table 1 |
| KMIS | 0.7500 | 0.0300 | Yes | this paper | Table 1 |
| TopK | 0.7300 | 0.0200 | Yes | this paper | Table 1 |
| SEP | 0.7700 | 0.0300 | Yes | this paper | Table 1 |
| DiffPool | 0.7500 | 0.0200 | Yes | this paper | Table 1 |
| MinCut | 0.7300 | 0.0300 | Yes | this paper | Table 1 |
| DMON | 0.7300 | 0.0300 | Yes | this paper | Table 1 |
| JBGN | 0.7800 | 0.0300 | Yes | this paper | Table 1 |
| Eigen | 0.7500 | 0.0300 | Yes | this paper | Table 1 |
| HOSC | 0.7800 | 0.0300 | Yes | this paper | Table 1 |
| BNPool | 0.8000 | 0.0200 | No | this paper | Table 1 |

### Pep-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.2950 | 0.0070 | Yes | this paper | Table 1 |
| Graclus | 0.2640 | 0.0010 | Yes | this paper | Table 1 |
| ECPool | 0.2620 | 0.0060 | Yes | this paper | Table 1 |
| KMIS | 0.2630 | 0.0010 | Yes | this paper | Table 1 |
| TopK | 0.2660 | 0.0000 | Yes | this paper | Table 1 |
| SEP | 0.3500 | 0.0020 | Yes | this paper | Table 1 |
| DiffPool | 0.2760 | 0.0180 | Yes | this paper | Table 1 |
| MinCut | 0.2650 | 0.0030 | Yes | this paper | Table 1 |
| DMON | 0.2800 | 0.0010 | Yes | this paper | Table 1 |
| JBGN | 0.2640 | 0.0010 | Yes | this paper | Table 1 |
| EigenPool | 0.2760 | 0.0020 | Yes | this paper | Table 1 |
| HOSC | 0.2830 | 0.0010 | Yes | this paper | Table 1 |
| BNPool | 0.2550 | 0.0010 | No | this paper | Table 1 |

### Proteins — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.7100 | 0.0400 | Yes | this paper | Table 1 |
| Graclus | 0.7300 | 0.0400 | Yes | this paper | Table 1 |
| ecpool | 0.7400 | 0.0500 | No | this paper | Table 1 |
| kmis | 0.7300 | 0.0500 | Yes | this paper | Table 1 |
| topk | 0.7400 | 0.0500 | Yes | this paper | Table 1 |
| sep | 0.7300 | 0.0700 | Yes | this paper | Table 1 |
| DiffPool | 0.7500 | 0.0300 | Yes | this paper | Table 1 |
| mincut | 0.7700 | 0.0500 | Yes | this paper | Table 1 |
| dmon | 0.7600 | 0.0400 | Yes | this paper | Table 1 |
| jbgnn | 0.7500 | 0.0500 | Yes | this paper | Table 1 |
| eigen | 0.7200 | 0.0400 | Yes | this paper | Table 1 |
| hosc | 0.7500 | 0.0500 | Yes | this paper | Table 1 |
| bnpool | 0.7500 | 0.0400 | Yes | this paper | Table 1 |

### PubMed — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DiffPool | 0.5240 | 0.0070 | Yes | this paper | Table 1 |
| MinCut | 0.6130 | 0.0020 | Yes | this paper | Table 1 |
| DMon | 0.5960 | 0.0140 | Yes | this paper | Table 1 |
| JBGNN | 0.5580 | 0.0380 | Yes | this paper | Table 1 |
| BNPool | 0.8130 | 0.0050 | No | this paper | Table 1 |

### RedditB — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| -- | 0.8600 | 0.0100 | Yes | this paper | Table 1 |
| Graclus | 0.9000 | 0.0300 | Yes | this paper | Table 1 |
| ecpool | 0.9100 | 0.0200 | No | this paper | Table 1 |
| kmis | 0.9000 | 0.0200 | Yes | this paper | Table 1 |
| topk | 0.7700 | 0.0200 | Yes | this paper | Table 1 |
| sep | 0.9000 | 0.0100 | Yes | this paper | Table 1 |
| DiffPool | 0.9000 | 0.0200 | Yes | this paper | Table 1 |
| mincut | 0.8700 | 0.0200 | Yes | this paper | Table 1 |
| dmon | 0.8800 | 0.0200 | Yes | this paper | Table 1 |
| jbgnn | 0.9000 | 0.0100 | Yes | this paper | Table 1 |
| eigen | 0.8900 | 0.0300 | Yes | this paper | Table 1 |
| hosc | 0.9000 | 0.0200 | Yes | this paper | Table 1 |
| bnpool | 0.9100 | 0.0200 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **DiffPool**
- **MinCut**
- **DMon**
- **JBGNN**
- **--**
- **Graclus**
- **ECPool**
- **KMIS**
- **TopK**
- **SEP**
- **JBGN**
- **Eigen**
- **HOSC**
- **SepPool**
- **EigenPool**
- **bnpool**

## Extraction Notes

[Community] Extracted only the 'Community' dataset and 'ACC' metric as requested. Normalized
percentages to [0, 1] range. [Cora] Extracted only Cora dataset results as requested. Normalised
Accuracy from percentages to [0, 1] range. [CiteSeer] Extracted only Accuracy for CiteSeer as
requested. Normalized percentages to [0, 1] range. [PubMed] Extracted only Accuracy for PubMed as
requested. COS metric was skipped. Values were normalized from percentages to [0, 1]. [DBLP] The
primary metric requested (Micro-F1) was not present in the provided table for DBLP; instead, ACC and
COS were reported for vertex clustering. I extracted both as they are the standard metrics for this
specific task in the table. [Collab] Extracted only the 'Collab' dataset from Table 1. Table 2 was
ignored as it contained optional variants (varying pooling ratios K) as per instructions. [Colors3]
Extracted results for Colors3 from Table 1. Table 2 was skipped as it contains optional variants
(varying pooling ratios K) as per instructions. [Mutagenicity] Extracted only the 'Mutagenicity'
column from Table 1. Table 2 was ignored as it contains optional variants (varying pooling ratios K)
as per the instructions. [NCI1] Extracted only NCI1 results from Table 1. Table 2 was ignored as it
contains optional variants (varying pooling ratios K) as per instructions. [RedditB] Extracted only
RedditB results from Table 1. Table 2 was ignored as it contains optional variants (varying pooling
ratios K) as per instructions. [MUTAG] Extracted only MUTAG results from Table 1. Table 2 was
ignored as it contains optional variants (varying pooling ratios K) as per instructions. [Enzymes]
Extracted only from Table 1 as requested (standard configuration). Table 2 was skipped because it
contains optional variants (varying pooling ratios K). All percentages were normalized to [0, 1].
[Proteins] Extracted only the 'Proteins' column from Table 1. Table 2 was ignored as it contains
optional variants (different pooling ratios K) as per instructions. [MolHiv] Extracted only MolHiv
results from Table 1. Table 2 was ignored as it contains optional variants (varying pooling ratios
K) as per instructions. [Pep-struct] Extracted only the default configuration from Table 1 as
requested. Table 2 was ignored as it contained optional variants (varying pooling ratios K).
[Multip.] Extracted only the 'Multip.' column from Table 1. Table 2 was ignored as it contained
optional variants (varying pooling ratios K) as per instructions. [GCB-H] The user requested results
ONLY for the dataset 'GCB-H'. After reviewing all provided tables, the dataset 'GCB-H' is not
mentioned in any of the tables. Therefore, no results could be extracted. [IMDB] The user requested
results ONLY for the dataset 'IMDB'. After reviewing all provided tables, the dataset 'IMDB' is not
mentioned in any of the tables. Therefore, no results could be extracted. [DD] The user requested
results ONLY for the dataset 'DD'. After reviewing all provided tables and text, no dataset named
'DD' was found. Datasets present include Collab, Colors3, Mutagenicity, NCI1, RedditB, MUTAG,
Enzymes, Proteins, MolHiv, Pep-struct, Multipartite, Community, Cora, CiteSeer, PubMed, and DBLP.
Consequently, no results were extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*