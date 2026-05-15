# Extraction: Cooperative Sheaf Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: CSNN
- Type: GNN

## Results

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GGCN | 85.6800 | 6.6300 | Yes | this paper | Table 2 |
| H2GCN | 82.7000 | 5.2800 | Yes | this paper | Table 2 |
| GPRGNN | 80.2700 | 8.1100 | Yes | this paper | Table 2 |
| FAGCN | 79.1900 | 9.7900 | Yes | this paper | Table 2 |
| MixHop | 73.5100 | 6.3400 | Yes | this paper | Table 2 |
| GCNII | 77.8600 | 3.7900 | Yes | this paper | Table 2 |
| Geom-GCN | 60.5400 | 3.6700 | Yes | this paper | Table 2 |
| PairNorm | 58.9200 | 3.1500 | Yes | this paper | Table 2 |
| GraphSAGE | 75.9500 | 5.0100 | Yes | this paper | Table 2 |
| GCN | 60.5400 | 5.3000 | Yes | this paper | Table 2 |
| GAT | 61.8900 | 5.0500 | Yes | this paper | Table 2 |
| MLP | 81.8900 | 6.4000 | Yes | this paper | Table 2 |
| FSGNN | 87.3000 | 4.5300 | Yes | this paper | Table 2 |
| GloGNN | 83.5100 | 4.2600 | Yes | this paper | Table 2 |
| ACMGCN | 85.1400 | 6.0700 | Yes | this paper | Table 2 |
| CO-GNN | 72.7000 | 5.4700 | Yes | this paper | Table 2 |
| Diag-NSD | 86.4900 | 7.3500 | Yes | this paper | Table 2 |
| O(d)-NSD | 84.8600 | 4.7100 | Yes | this paper | Table 2 |
| Gen-NSD | 85.6800 | 6.5100 | Yes | this paper | Table 2 |
| CSNN | 81.6200 | 4.3200 | No | this paper | Table 2 |

### Film — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GGCN | 37.5400 | 1.5600 | Yes | this paper | Table 2 |
| H2GCN | 35.7000 | 1.0000 | Yes | this paper | Table 2 |
| GPRGNN | 34.6300 | 1.2200 | Yes | this paper | Table 2 |
| FAGCN | 34.8700 | 1.2500 | Yes | this paper | Table 2 |
| MixHop | 32.2200 | 2.3400 | Yes | this paper | Table 2 |
| GCNII | 37.4400 | 1.3000 | Yes | this paper | Table 2 |
| Geom-GCN | 31.5900 | 1.1500 | Yes | this paper | Table 2 |
| PairNorm | 27.4000 | 1.2400 | Yes | this paper | Table 2 |
| GraphSAGE | 34.2300 | 0.9900 | Yes | this paper | Table 2 |
| GCN | 27.3200 | 1.1000 | Yes | this paper | Table 2 |
| GAT | 27.4400 | 0.8900 | Yes | this paper | Table 2 |
| MLP | 36.5300 | 0.7000 | Yes | this paper | Table 2 |
| FSGNN | 35.6200 | 0.8700 | Yes | this paper | Table 2 |
| GloGNN | 37.3500 | 1.3000 | Yes | this paper | Table 2 |
| ACMGCN | 36.2800 | 1.0900 | Yes | this paper | Table 2 |
| CO-GNN | 36.2600 | 3.7400 | Yes | this paper | Table 2 |
| Diag-NSD | 37.7900 | 1.0100 | Yes | this paper | Table 2 |
| O(d)-NSD | 37.8100 | 1.1500 | Yes | this paper | Table 2 |
| Gen-NSD | 37.8000 | 1.2200 | Yes | this paper | Table 2 |
| CSNN | 38.0300 | 1.1200 | No | this paper | Table 2 |

### Penn94 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| MLP | 73.6100 | 0.4000 | Yes | this paper | Table 1 |
| GCN | 82.4700 | 0.2700 | Yes | this paper | Table 1 |
| GAT | 81.5300 | 0.5500 | Yes | this paper | Table 1 |
| MixHop | 83.4700 | 0.7100 | Yes | this paper | Table 1 |
| GCNII | 82.9200 | 0.5900 | Yes | this paper | Table 1 |
| H2GCN | 81.3100 | 0.6000 | Yes | this paper | Table 1 |
| WRGAT | 74.3200 | 0.5300 | Yes | this paper | Table 1 |
| GPR-GNN | 81.3800 | 0.1600 | Yes | this paper | Table 1 |
| ACM-GCN | 82.5200 | 0.9600 | Yes | this paper | Table 1 |
| LINKX | 84.7100 | 0.5200 | Yes | this paper | Table 1 |
| GloGNN | 85.5700 | 0.3500 | Yes | this paper | Table 1 |
| CSNN | 86.0000 | 0.3900 | No | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GGCN | 84.8600 | 4.5500 | Yes | this paper | Table 2 |
| H2GCN | 84.8600 | 7.2300 | Yes | this paper | Table 2 |
| GPRGNN | 78.3800 | 4.3600 | Yes | this paper | Table 2 |
| FAGCN | 82.4300 | 6.8900 | Yes | this paper | Table 2 |
| MixHop | 77.8400 | 7.7300 | Yes | this paper | Table 2 |
| GCNII | 77.5700 | 3.8300 | Yes | this paper | Table 2 |
| Geom-GCN | 66.7600 | 2.7200 | Yes | this paper | Table 2 |
| PairNorm | 60.2700 | 4.3400 | Yes | this paper | Table 2 |
| GraphSAGE | 82.4300 | 6.1400 | Yes | this paper | Table 2 |
| GCN | 55.1400 | 5.1600 | Yes | this paper | Table 2 |
| GAT | 52.1600 | 6.6300 | Yes | this paper | Table 2 |
| MLP | 80.8100 | 4.7500 | Yes | this paper | Table 2 |
| FSGNN | 87.5700 | 4.8600 | Yes | this paper | Table 2 |
| GloGNN | 84.3200 | 4.1500 | Yes | this paper | Table 2 |
| ACMGCN | 87.8400 | 4.4000 | Yes | this paper | Table 2 |
| CO-GNN | 77.5700 | 5.4100 | Yes | this paper | Table 2 |
| Diag-NSD | 85.6700 | 6.9500 | Yes | this paper | Table 2 |
| O(d)-NSD | 85.9500 | 5.5100 | Yes | this paper | Table 2 |
| Gen-NSD | 82.9700 | 5.1300 | Yes | this paper | Table 2 |
| CSNN | 87.3000 | 5.9300 | No | this paper | Table 2 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GGCN | 86.8600 | 3.2900 | Yes | this paper | Table 2 |
| H2GCN | 87.6500 | 4.9800 | Yes | this paper | Table 2 |
| GPRGNN | 82.9400 | 4.2100 | Yes | this paper | Table 2 |
| FAGCN | 82.9400 | 7.9500 | Yes | this paper | Table 2 |
| MixHop | 75.8800 | 4.9000 | Yes | this paper | Table 2 |
| GCNII | 80.3900 | 3.4000 | Yes | this paper | Table 2 |
| Geom-GCN | 64.5100 | 3.6600 | Yes | this paper | Table 2 |
| PairNorm | 48.4300 | 6.1400 | Yes | this paper | Table 2 |
| GraphSAGE | 81.1800 | 5.5600 | Yes | this paper | Table 2 |
| GCN | 51.7600 | 3.0600 | Yes | this paper | Table 2 |
| GAT | 49.4100 | 4.0900 | Yes | this paper | Table 2 |
| MLP | 85.2900 | 3.3100 | Yes | this paper | Table 2 |
| FSGNN | 87.6500 | 3.5100 | Yes | this paper | Table 2 |
| GloGNN | 87.0600 | 3.5300 | Yes | this paper | Table 2 |
| ACMGCN | 88.4300 | 3.2200 | Yes | this paper | Table 2 |
| CO-GNN | 83.7300 | 4.0300 | Yes | this paper | Table 2 |
| Diag-NSD | 88.6300 | 2.7500 | Yes | this paper | Table 2 |
| O(d)-NSD | 89.4100 | 4.7400 | Yes | this paper | Table 2 |
| Gen-NSD | 89.2100 | 3.8400 | Yes | this paper | Table 2 |
| CSNN | 90.0000 | 2.8300 | No | this paper | Table 2 |

### amazon-ratings — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 48.7000 | 0.6300 | Yes | this paper | Table 1 |
| SAGE | 53.6300 | 0.3900 | Yes | this paper | Table 1 |
| GAT | 49.0900 | 0.6300 | Yes | this paper | Table 1 |
| GAT-sep | 52.7000 | 0.6200 | Yes | this paper | Table 1 |
| GT | 51.1700 | 0.6600 | Yes | this paper | Table 1 |
| GT-sep | 52.1800 | 0.8000 | Yes | this paper | Table 1 |
| CO-GNN | 54.2000 | 0.3400 | Yes | this paper | Table 1 |
| O(d)-NSD | 42.7600 | 0.5400 | Yes | this paper | Table 1 |
| BuNN | 53.7400 | 0.5100 | Yes | this paper | Table 1 |
| CSNN | 52.0700 | 1.0000 | No | this paper | Table 1 |

### minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 89.7500 | 0.5200 | Yes | this paper | Table 1 |
| SAGE | 93.5100 | 0.5700 | Yes | this paper | Table 1 |
| GAT | 92.0100 | 0.6800 | Yes | this paper | Table 1 |
| GAT-sep | 93.9100 | 0.3500 | Yes | this paper | Table 1 |
| GT | 91.8500 | 0.7600 | Yes | this paper | Table 1 |
| GT-sep | 92.2900 | 0.4700 | Yes | this paper | Table 1 |
| CO-GNN | 97.3500 | 0.6300 | Yes | this paper | Table 1 |
| O(d)-NSD | 92.1500 | 0.8400 | Yes | this paper | Table 1 |
| BuNN | 98.9900 | 0.1600 | Yes | this paper | Table 1 |
| CSNN | 99.0700 | 0.2500 | No | this paper | Table 1 |

### questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 76.0900 | 1.2700 | Yes | this paper | Table 1 |
| SAGE | 76.4400 | 0.6200 | Yes | this paper | Table 1 |
| GAT | 77.4300 | 1.2000 | Yes | this paper | Table 1 |
| GAT-sep | 76.7900 | 0.7100 | Yes | this paper | Table 1 |
| GT | 77.9500 | 0.6800 | Yes | this paper | Table 1 |
| GT-sep | 78.0500 | 0.9300 | Yes | this paper | Table 1 |
| CO-GNN | 75.9700 | 0.8900 | Yes | this paper | Table 1 |
| O(d)-NSD | 69.6900 | 1.4600 | Yes | this paper | Table 1 |
| BuNN | 78.7500 | 1.0900 | Yes | this paper | Table 1 |
| CSNN | 79.3100 | 1.2200 | No | this paper | Table 1 |

### roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 73.6900 | 0.7400 | Yes | this paper | Table 1 |
| SAGE | 85.7400 | 0.6700 | Yes | this paper | Table 1 |
| GAT | 80.8700 | 0.3000 | Yes | this paper | Table 1 |
| GAT-sep | 88.7500 | 0.4100 | Yes | this paper | Table 1 |
| GT | 86.5100 | 0.7300 | Yes | this paper | Table 1 |
| GT-sep | 87.3200 | 0.3900 | Yes | this paper | Table 1 |
| CO-GNN | 89.4400 | 0.5000 | Yes | this paper | Table 1 |
| O(d)-NSD | 80.4100 | 0.7200 | Yes | this paper | Table 1 |
| BuNN | 91.7500 | 0.3900 | Yes | this paper | Table 1 |
| CSNN | 92.6300 | 0.5000 | No | this paper | Table 1 |

### tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 83.6400 | 0.6700 | Yes | this paper | Table 1 |
| SAGE | 82.4300 | 0.4400 | Yes | this paper | Table 1 |
| GAT | 83.7000 | 0.4700 | Yes | this paper | Table 1 |
| GAT-sep | 83.7800 | 0.4300 | Yes | this paper | Table 1 |
| GT | 83.2300 | 0.6400 | Yes | this paper | Table 1 |
| GT-sep | 82.5200 | 0.9200 | Yes | this paper | Table 1 |
| CO-GNN | 84.8400 | 0.9600 | Yes | this paper | Table 1 |
| O(d)-NSD | 78.8300 | 0.7600 | Yes | this paper | Table 1 |
| BuNN | 84.7800 | 0.8000 | Yes | this paper | Table 1 |
| CSNN | 85.4500 | 0.5300 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling)
- **SAGE** (from: Hamilton et al.)
- **GAT** (from: Veličković et al.)
- **GAT-sep** (from: this paper)
- **GT** (from: this paper)
- **GT-sep** (from: this paper)
- **CO-GNN** (from: Finkelshtein et al.)
- **O(d)-NSD** (from: this paper)
- **BuNN** (from: this paper)
- **GGCN** (from: pei2020geom)
- **H2GCN** (from: pei2020geom)
- **GPRGNN** (from: pei2020geom)
- **FAGCN** (from: pei2020geom)
- **MixHop** (from: pei2020geom)
- **GCNII** (from: pei2020geom)
- **Geom-GCN** (from: pei2020geom)
- **PairNorm** (from: pei2020geom)
- **GraphSAGE** (from: pei2020geom)
- **MLP** (from: pei2020geom)
- **FSGNN** (from: pei2020geom)
- **GloGNN** (from: pei2020geom)
- **ACMGCN** (from: pei2020geom)
- **Diag-NSD** (from: pei2020geom)
- **Gen-NSD** (from: pei2020geom)
- **WRGAT**
- **GPR-GNN**
- **ACM-GCN**
- **LINKX**

## Extraction Notes

[roman-empire] Extracted only the 'roman-empire' column from Table 1 as requested. The metric is
Accuracy. All values include standard deviation. The proposed model is CSNN, which achieves the
highest accuracy. [amazon-ratings] Extracted only the 'amazon-ratings' column from Table 1. The
caption confirms Accuracy is the metric for this dataset. All models listed in the table were
extracted. Note that CO-GNN has the highest value (54.20) but is marked as best in the table (bold),
while CSNN is the proposed model. The table caption states CSNN is best in 6/7 datasets, but for
amazon-ratings specifically, CO-GNN (54.20) > BuNN (53.74) > SAGE (53.63) > GAT-sep (52.70) > GT-sep
(52.18) > CSNN (52.07) > GAT (49.09) > GCN (48.70) > O(d)-NSD (42.76). The bolding in the table for
amazon-ratings seems to highlight CO-GNN (54.20) and BuNN (53.74) with gray text, possibly
indicating a different comparison or error in the paper's bolding logic vs caption, but I extracted
all values as presented. [minesweeper] Extracted only the 'minesweeper' column from Table 1 as
requested. The metric for minesweeper is AUROC (ROC-AUC). All values are test-set results. BuNN has
missing values for squirrel and chameleon but valid values for minesweeper. [tolokers] Extracted
only the 'tolokers' column from Table 1. The caption confirms AUROC is reported for tolokers. All
values are test-set results as implied by the standard reporting format in such tables (no train/val
split indicated in the table structure). The proposed model is CSNN. [questions] Extracted only the
'questions' dataset column as requested. The table caption indicates AUROC is reported for
minesweeper, tolokers and questions. The values in the 'questions' column are percentages (e.g.,
76.09), which corresponds to the AUROC metric scaled by 100. All other datasets were ignored.
[squirrel] failed: 1 validation error for ExtractionOutput results.8.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [chameleon] failed: 1 validation error for
ExtractionOutput results.8.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Texas] Extracted only the 'Texas' column from Table 2
as requested. All models listed in the table were included. The proposed model is identified as CSNN
based on the caption and table structure. Standard deviations are parsed from the 'value ± std'
format. Metric is Accuracy, higher is better. [Wisconsin] Extracted only the Wisconsin column from
Table 2 as requested. All models listed in the table were included. The proposed model is CSNN.
Standard deviations are parsed from the 'value ± std' format. No external data usage is indicated
for these standard node classification benchmarks. [Film] Extracted only the 'Film' column from
Table 2 as requested. All models listed in the table were included. The proposed model is CSNN.
Standard deviations were parsed from the 'value ± std' format. No external data usage was indicated
for these standard GNN baselines. [Cornell] Extracted only the 'Cornell' column from Table 2 as
requested. All models listed in the table were included. The proposed model is CSNN. Note that while
the caption claims CSNN achieves best results in 3 out of 4 datasets, for Cornell specifically,
FSGNN (87.30) and Diag-NSD (86.49) have higher mean accuracy than CSNN (81.62). The bolding in the
table for Cornell is on FSGNN (87.30) and Diag-NSD (86.49) is grayed out but bolded in the source
LaTeX, likely indicating a specific condition or error in the paper's visual highlighting, but the
values are extracted as written. [Penn94] Extracted all rows from the provided table for the Penn94
dataset. The metric is Accuracy (implied by the context of classification and standard reporting,
though the column header is just 'Penn94', the values are percentages typical for accuracy). The
proposed model is CSNN. Baselines are standard GNN variants. No external data usage is indicated for
these baselines in the text provided.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*