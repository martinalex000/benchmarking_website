# Extraction: arXiv:2410.05499
**Model used**: `alias-huge-no-thinking`  **Date**: 2026-05-13  **Confidence**: MEDIUM

## Proposed Model: Unitary GCN
- Type: GCN_variant

## Results

### Amazon-r. — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4870 | 0.0063 | Yes | Platonov 2023 | Table 2 |
| SAGE | 0.5363 | 0.0039 | Yes | Platonov 2023 | Table 2 |
| GAT | 0.4909 | 0.0063 | Yes | Platonov 2023 | Table 2 |
| GT | 0.5117 | 0.0066 | Yes | Platonov 2023 | Table 2 |
| Unitary GCN | 0.5534 | 0.0074 | No | this paper | Table 2 |
| Lie Unitary GCN | 0.5235 | 0.0026 | No | this paper | Table 2 |

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2550 | 0.0120 | Yes | this paper | Table 3 |
| GIN | 0.3130 | 0.0110 | Yes | this paper | Table 3 |
| GAT | 0.2680 | 0.0120 | Yes | this paper | Table 3 |
| Unitary GCN | 0.4150 | 0.0160 | No | this paper | Table 3 |
| Wide Unitary GCN | 0.4210 | 0.0150 | No | this paper | Table 3 |

### IMDB — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.4930 | 0.0080 | Yes | this paper | Table 3 |
| GIN | 0.6900 | 0.0100 | Yes | this paper | Table 3 |
| GAT | 0.4700 | 0.0110 | Yes | this paper | Table 3 |
| Unitary GCN | 0.6120 | 0.0140 | No | this paper | Table 3 |
| Wide Unitary GCN | 0.6240 | 0.0130 | No | this paper | Table 3 |

### MUTAG — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.6880 | 0.0240 | Yes | this paper | Table 3 |
| GIN | 0.7570 | 0.0360 | Yes | this paper | Table 3 |
| GAT | 0.6850 | 0.0280 | Yes | this paper | Table 3 |
| Unitary GCN | 0.8680 | 0.0330 | No | this paper | Table 3 |
| Wide Unitary GCN | 0.8710 | 0.0350 | No | this paper | Table 3 |

### Minesweeper — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8975 | 0.0052 | Yes | Platonov 2023 | Table 2 |
| SAGE | 0.9351 | 0.0057 | Yes | Platonov 2023 | Table 2 |
| GAT | 0.9201 | 0.0068 | Yes | Platonov 2023 | Table 2 |
| GT | 0.9185 | 0.0076 | Yes | Platonov 2023 | Table 2 |
| Unitary GCN | 0.9427 | 0.0058 | No | this paper | Table 2 |
| Lie Unitary GCN | 0.9611 | 0.0010 | No | this paper | Table 2 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7060 | 0.0070 | Yes | this paper | Table 3 |
| GIN | 0.6970 | 0.0080 | Yes | this paper | Table 3 |
| GAT | 0.7260 | 0.0080 | Yes | this paper | Table 3 |
| Unitary GCN | 0.7510 | 0.0130 | No | this paper | Table 3 |
| Wide Unitary GCN | 0.7560 | 0.0100 | No | this paper | Table 3 |

### PascalVOC-SP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.2078 | 0.0031 | Yes | Tonshoff 2023 | Table 1 |
| GINE | 0.2718 | 0.0054 | Yes | Tonshoff 2023 | Table 1 |
| GatedGCN | 0.3880 | 0.0040 | Yes | Tonshoff 2023 | Table 1 |
| GPS | 0.4440 | 0.0065 | Yes | Tonshoff 2023 | Table 1 |
| DRew | 0.3314 | 0.0024 | Yes | this paper | Table 1 |
| Exphormer | 0.3960 | 0.0027 | Yes | this paper | Table 1 |
| CRAWL | 0.4588 | 0.0079 | Yes | this paper | Table 1 |
| UniGCN | 0.3516 | 0.0070 | No | this paper | Table 1 |
| Lie UniGCN | 0.4005 | 0.0067 | No | this paper | Table 1 |

### Questions — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7609 | 0.0127 | Yes | Platonov 2023 | Table 2 |
| SAGE | 0.7644 | 0.0062 | Yes | Platonov 2023 | Table 2 |
| GAT | 0.7743 | 0.0120 | Yes | Platonov 2023 | Table 2 |
| GT | 0.7795 | 0.0068 | Yes | Platonov 2023 | Table 2 |
| Unitary GCN | 0.7921 | 0.0079 | No | this paper | Table 2 |
| Lie Unitary GCN | 0.8001 | 0.0043 | No | this paper | Table 2 |

### Roman-empire — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.7369 | 0.0074 | Yes | Platonov 2023 | tab:platonov |
| SAGE | 0.8574 | 0.0067 | Yes | Platonov 2023 | tab:platonov |
| GAT | 0.8087 | 0.0030 | Yes | Platonov 2023 | tab:platonov |
| GT | 0.8651 | 0.0073 | Yes | Platonov 2023 | tab:platonov |
| Unitary GCN | 0.8721 | 0.0076 | No | this paper | tab:platonov |
| Lie Unitary GCN | 0.8550 | 0.0022 | No | this paper | tab:platonov |

### Tolokers — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.8364 | 0.0067 | Yes | Platonov 2023 | Table 2 |
| SAGE | 0.8243 | 0.0044 | Yes | Platonov 2023 | Table 2 |
| GAT | 0.8370 | 0.0047 | Yes | Platonov 2023 | Table 2 |
| GT | 0.8323 | 0.0064 | Yes | Platonov 2023 | Table 2 |
| Unitary GCN | 0.8483 | 0.0068 | No | this paper | Table 2 |
| Lie Unitary GCN | 0.8518 | 0.0043 | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN** (from: Kipf 2016)
- **GINE** (from: Xu 2018)
- **GatedGCN** (from: Bresson 2017)
- **GPS** (from: Rampasek 2022)
- **DRew** (from: Gutteridge 2023)
- **Exphormer** (from: Shirzad 2023)
- **CRAWL** (from: Tonshoff 2023)
- **SAGE** (from: Hamilton 2017)
- **GAT** (from: Veličković 2017)
- **GT** (from: Shi 2020)
- **GIN**

## Extraction Notes

[Peptides-func] failed: 1 validation error for ExtractionOutput   Input should be a valid dictionary
or instance of ExtractionOutput [type=model_type, input_value=[{'name': 'GCN', 'params_...hint':
'Tonshoff 2023'}], input_type=list]     For further information visit
https://errors.pydantic.dev/2.13/v/model_type [Peptides-struct] failed: 1 validation error for
ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': 'GCN', 'params_...hint': 'Tonshoff 2023'}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [COCO-SP] failed: JSON
parse error from 'alias-huge-no-thinking': could not extract valid JSON [PascalVOC-SP] The
hyperparameter table for PascalVOC-SP was truncated in the provided text, so exact parameter counts
for the proposed models on this dataset could not be extracted. The dataset name appears as 'PASCAL-
VOC' in the table header but as 'PascalVOC-SP' in the paper text; the latter is used as instructed.
Baselines marked with a dagger explicitly source results from Tonshoff 2023; unmarked baselines
(DRew, Exphormer, CRAWL) and the proposed models are attributed to 'this paper'. Rows with missing
values (GUMP, GRIT, Graph ViT) for PascalVOC-SP were skipped. [Roman-empire] The heterophilous table
header labels the Roman-empire column as 'Test AP', but the values are reported as percentages
(e.g., 73.69) and are sourced from Platonov et al. (2023), where the standard metric for Roman-
empire is Accuracy. We therefore treat these values as Accuracy and normalize them to [0,1].
Parameter counts for the heterophilous experiments are not provided in the extracted text. [Amazon-
ratings] The table reports Test AP for Amazon-r. rather than Accuracy. AP values were reported as
percentages (e.g., 48.70) and have been normalized to [0,1]. Baseline numbers are taken from
Platonov 2023 as indicated by the table footnote. [Minesweeper] Only the heterophilous datasets
table (Table 2 / tab:platonov) contains Minesweeper results. All ROC-AUC values were reported as
percentages (e.g., 89.75) and were normalized to the [0,1] range by dividing by 100. Parameter
counts for the Minesweeper configuration are not provided in the paper. [Tolokers] Only the
heterophilous datasets table (Table 2) contained Tolokers results. Values were reported as
percentages and normalized to [0,1]. Parameter counts were not provided for this dataset. All other
tables were ignored per the focus instruction. [Questions] Only the heterophilous datasets table
(Table 2) contained results for the Questions dataset. All reported ROC-AUC values were presented on
a 0-100 scale and have been normalised to [0,1]. No optional variants or multiple configurations
were shown for this dataset. [ENZYMES] The table header for ENZYMES reads 'Test AP', but the
reported values (25.5-42.1) are percentage-scale figures consistent with Accuracy, the standard
benchmark metric for ENZYMES. These values were normalized by dividing by 100. Parameter counts are
not provided for the TU dataset experiments. [IMDB-BINARY] The paper labels the dataset as 'IMDB'
(standard TU dataset identifier, commonly IMDB-BINARY) and reports the metric as 'Test AP'. The raw
values are given as percentages and were normalized to [0,1]. The user-requested primary metric is
Accuracy, but the table only contains the AP column; these numerical values are consistent with
typical Accuracy results for IMDB-BINARY in the literature, yet the paper explicitly uses the AP
label. No parameter counts are listed for this table. Baseline results lack external citation
markers, indicating they were run by the authors. [MUTAG] The MUTAG results appear in the TU-
datasets table. The metric is labeled 'Test AP' rather than 'Accuracy'; values were given as
percentages and have been normalized to [0,1]. Parameter counts are not provided for these runs, and
no external data usage is indicated. [PROTEINS] The TU datasets table (Table 3) labels the PROTEINS
column header as 'Test AP', but given the standard benchmark metric for PROTEINS is Accuracy and the
values match typical Accuracy scores (70-76%), this is treated as a header typo and the metric is
recorded as Accuracy. All values were reported as percentages and normalized to [0,1]. No exact
parameter counts are provided for the TU dataset experiments.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*