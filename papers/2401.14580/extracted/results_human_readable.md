# Extraction: arXiv:2401.14580
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: LOW

## Proposed Model: UYGCN
- Type: GNN

## Results

### ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 0.5500 | 0.0030 | Yes | this paper | Table 1 |
| GCN | 0.7270 | 0.0030 | Yes | this paper | Table 1 |
| GAT | 0.7200 | 0.0050 | Yes | this paper | Table 1 |
| GIN | 0.6450 | 0.0250 | Yes | this paper | Table 1 |
| APPNP | 0.7030 | 0.0250 | Yes | this paper | Table 1 |
| H2GCN | 0.7280 | 0.0240 | Yes | this paper | Table 1 |
| GPRGNN | 0.7040 | 0.0150 | Yes | this paper | Table 1 |
| LEGCN | 0.7330 | 0.0030 | Yes | this paper | Table 1 |
| Replusion | 0.7190 | 0.0040 | Yes | this paper | Table 1 |
| GRAND | 0.7120 | 0.0020 | Yes | this paper | Table 1 |
| SJLR | 0.7200 | 0.0040 | Yes | this paper | Table 1 |
| ACMP | 0.6890 | 0.0030 | Yes | this paper | Table 1 |
| UYGCN | 0.7440 | 0.0090 | No | this paper | Table 1 |
| UYGAT | 0.7230 | 0.0030 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2016)
- **GAT** (from: Veličković et al. 2018)
- **GRAND** (from: Thorpe et al. 2022)
- **ACMP-GCN** (from: Wang et al. 2022)
- **MLP**
- **GIN** (from: Xu et al.)
- **APPNP** (from: Klicpera et al.)
- **H2GCN** (from: Zhu et al.)
- **GPRGNN** (from: Wang et al.)
- **LEGCN** (from: Bo et al.)
- **Replusion**
- **SJLR** (from: Zhang et al.)
- **ACMP**
- **UYGAT**

## Extraction Notes

[Cora] The paper mentions testing UYGNNs/UYGCN on Cora and compares it with GCN, GAT, GRAND, and
ACMP-GCN. However, the specific numerical results for the Cora dataset are presented in Figure 1
(referenced as Figure \ref{fig:osm} in the text) and Figure 2 (referenced as Figure
\ref{fig:sensitivity}). The provided text does not contain the actual data values from these
figures, nor are there any tables containing the Accuracy results for Cora. Therefore, no
quantitative results could be extracted. [CiteSeer] The paper mentions that learning accuracy
results for CiteSeer are presented in Figure 1 (over_smoothing_final_10.pdf) and Figure 2
(charts.pdf). However, the provided text does not contain the actual numerical values from these
figures, nor are there any tables with quantitative results for CiteSeer. Therefore, no specific
accuracy values, standard deviations, or other metrics could be extracted. [PubMed] The paper
mentions conducting experiments on PubMed and compares UYGNNs (specifically UYGCN) against GCN, GAT,
GRAND, and ACMP-GCN. However, the specific numerical results for the PubMed dataset are reported in
Figure 1 (referenced as Figure \ref{fig:osm} in the text, captioned 'Model performance under the
layer increases'). The provided text does not contain the image or data from Figure 1, nor are there
any tables in the provided text that list the Accuracy values for PubMed. Table 1 only contains
dataset statistics. Therefore, no quantitative results could be extracted. [Cornell] The paper
mentions testing UYGNNs/UYGCN on the Cornell dataset in the text and Figure 1 caption ('Learning
Accuracy of UYGCN with different number of CNs'). However, the provided text does not contain the
actual numerical results (Accuracy values) for the Cornell dataset. The only table provided (Table
1) contains dataset statistics (nodes, edges, homophily) but no performance metrics. Without the
specific accuracy values or a table containing them, no quantitative results can be extracted.
[Texas] The provided text contains only the introduction to the experimental section and a table
with dataset statistics (Table 1). It does not contain the actual performance results (accuracy
values) for the UYGNN model or any baselines on the Texas dataset. The text mentions that
experiments were conducted on Texas, but the specific numerical results are not present in the
provided snippet. [Wisconsin] The paper mentions testing UYGNNs/UYGCN on the Wisconsin dataset in
the text and Figure 1 caption. However, the provided text only includes the caption for Figure 1
('Learning Accuracy of UYGCN with different number of CNs') and Table 1 (Dataset Statistics). The
actual numerical results (Accuracy values) for the Wisconsin dataset are contained within Figure 1,
which is an image and not provided as parseable text/data. Therefore, no quantitative results could
be extracted. [ogbn-arxiv] Extracted results for 'Arxiv' from Table 1. The dataset name in the table
is 'Arxiv', which corresponds to 'ogbn-arxiv' as indicated in the text. All values are percentages
converted to [0,1] range. Standard deviations are parsed from the '±' notation. The table caption
indicates bold is best, underline is second best. UYGCN is the proposed model.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*