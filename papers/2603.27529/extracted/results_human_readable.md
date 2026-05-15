# Extraction: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in GNNs
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: CaCoSE
- Type: GNN

## Results

### Amazon Photos — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 92.1200 | — | Yes | this paper | Table 1 |
| GAT | 92.0100 | — | Yes | this paper | Table 1 |
| SAGE | 91.5800 | — | Yes | this paper | Table 1 |
| LRGB | 74.0400 | — | Yes | this paper | Table 1 |
| BORF | 91.9300 | — | Yes | this paper | Table 1 |
| FOSR | 91.8300 | — | Yes | this paper | Table 1 |
| SDRF | 91.7100 | — | Yes | this paper | Table 1 |
| GTR | 91.7600 | — | Yes | this paper | Table 1 |
| DR | 79.8600 | — | Yes | this paper | Table 1 |
| LASER | 67.3600 | — | Yes | this paper | Table 1 |
| GOKU | 92.5100 | — | Yes | this paper | Table 1 |
| CaCoSE | 92.9800 | — | No | this paper | Table 1 |

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 63.3200 | — | Yes | this paper | Table 1 |
| GAT | 61.7000 | — | Yes | this paper | Table 1 |
| SAGE | 62.6400 | — | Yes | this paper | Table 1 |
| LRGB | 46.9300 | — | Yes | this paper | Table 1 |
| BORF | 60.2400 | — | Yes | this paper | Table 1 |
| FOSR | 60.3100 | — | Yes | this paper | Table 1 |
| SDRF | 60.7400 | — | Yes | this paper | Table 1 |
| GTR | 63.7800 | — | Yes | this paper | Table 1 |
| DR | 27.8700 | — | Yes | this paper | Table 1 |
| LASER | 41.9000 | — | Yes | this paper | Table 1 |
| GOKU | 65.9000 | — | Yes | this paper | Table 1 |
| CaCoSE | 68.9900 | — | No | this paper | Table 1 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 69.1000 | — | Yes | this paper | Table 1 |
| GAT | 67.9400 | — | Yes | this paper | Table 1 |
| SAGE | 67.7600 | — | Yes | this paper | Table 1 |
| LRGB | 57.5800 | — | Yes | this paper | Table 1 |
| BORF | 67.0800 | — | Yes | this paper | Table 1 |
| FOSR | 67.2400 | — | Yes | this paper | Table 1 |
| SDRF | 67.4200 | — | Yes | this paper | Table 1 |
| GTR | 69.1500 | — | Yes | this paper | Table 1 |
| DR | 24.9000 | — | Yes | this paper | Table 1 |
| LASER | 64.2600 | — | Yes | this paper | Table 1 |
| GOKU | 66.0800 | — | Yes | this paper | Table 1 |
| CaCoSE | 69.4200 | — | No | this paper | Table 1 |

### CoAuthor CS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 88.8600 | — | Yes | this paper | Table 1 |
| GAT | 87.1300 | — | Yes | this paper | Table 1 |
| SAGE | 88.4200 | — | Yes | this paper | Table 1 |
| LRGB | 59.5000 | — | Yes | this paper | Table 1 |
| BORF | 90.5200 | — | Yes | this paper | Table 1 |
| FOSR | 90.4400 | — | Yes | this paper | Table 1 |
| SDRF | 90.5600 | — | Yes | this paper | Table 1 |
| GTR | 88.8700 | — | Yes | this paper | Table 1 |
| DR | 72.5000 | — | Yes | this paper | Table 1 |
| LASER | 76.9000 | — | Yes | this paper | Table 1 |
| GOKU | 90.0400 | — | Yes | this paper | Table 1 |
| CaCoSE | 90.7300 | — | No | this paper | Table 1 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 84.2400 | — | Yes | this paper | Table 1 |
| GAT | 85.0000 | — | Yes | this paper | Table 1 |
| SAGE | 83.6000 | — | Yes | this paper | Table 1 |
| LRGB | 71.0200 | — | Yes | this paper | Table 1 |
| BORF | 83.6800 | — | Yes | this paper | Table 1 |
| FOSR | 83.6600 | — | Yes | this paper | Table 1 |
| SDRF | 84.0400 | — | Yes | this paper | Table 1 |
| GTR | 84.0700 | — | Yes | this paper | Table 1 |
| DR | 44.3500 | — | Yes | this paper | Table 1 |
| LASER | 75.7700 | — | Yes | this paper | Table 1 |
| GOKU | 82.6600 | — | Yes | this paper | Table 1 |
| CaCoSE | 85.0000 | — | No | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CaCoSE | 73.2000 | — | No | this paper | Table 2 |
| SDRF | 62.9000 | — | Yes | this paper | Table 2 |
| FOSR | 60.4000 | — | Yes | this paper | Table 2 |
| BORF | 60.8200 | — | Yes | this paper | Table 2 |
| GTR | 70.2000 | — | Yes | this paper | Table 2 |
| DR | 53.6000 | — | Yes | this paper | Table 2 |
| LASER | 67.3000 | — | Yes | this paper | Table 2 |
| GOKU | 64.8000 | — | Yes | this paper | Table 2 |
| CaCoSE (without Attention) | 73.0000 | — | Yes | this paper | Table 4 |
| CaCoSE (without CaEF) | 73.1000 | — | Yes | this paper | Table 4 |
| CaCoSE (TopkPool) | 72.9000 | — | Yes | this paper | Table 4 |
| CaCoSE (DMon) | 67.5000 | — | Yes | this paper | Table 4 |
| CaCoSE (GMT) | 60.7100 | — | Yes | this paper | Table 4 |
| CaCoSE (GAT) | 71.7000 | — | Yes | this paper | Table 4 |
| CaCoSE (SAGE) | 73.9000 | — | Yes | this paper | Table 4 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SDRF | 41.5300 | — | Yes | this paper | Table 2 |
| FOSR | 37.3300 | — | Yes | this paper | Table 2 |
| BORF | 38.2000 | — | Yes | this paper | Table 2 |
| GTR | 45.3300 | — | Yes | this paper | Table 2 |
| DR | 35.6000 | — | Yes | this paper | Table 2 |
| LASER | 45.4000 | — | Yes | this paper | Table 2 |
| GOKU | 42.4000 | — | Yes | this paper | Table 2 |
| CaCoSE | 49.1400 | — | No | this paper | Table 2 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SDRF | 74.5300 | — | Yes | this paper | Table 2 |
| FOSR | 75.8900 | — | Yes | this paper | Table 2 |
| BORF | 64.0000 | — | Yes | this paper | Table 2 |
| GTR | 76.0000 | — | Yes | this paper | Table 2 |
| DR | 71.0000 | — | Yes | this paper | Table 2 |
| LASER | 68.0000 | — | Yes | this paper | Table 2 |
| GOKU | 74.5000 | — | Yes | this paper | Table 2 |
| CaCoSE | 76.9900 | — | No | this paper | Table 2 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SDRF | 66.8800 | — | Yes | this paper | Table 2 |
| FOSR | 66.7000 | — | Yes | this paper | Table 2 |
| BORF | 68.4100 | — | Yes | this paper | Table 2 |
| GTR | 71.5200 | — | Yes | this paper | Table 2 |
| DR | 72.2300 | — | Yes | this paper | Table 2 |
| LASER | 71.0700 | — | Yes | this paper | Table 2 |
| GOKU | 70.8000 | — | Yes | this paper | Table 2 |
| CaCoSE | 71.7900 | — | No | this paper | Table 2 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 52.3600 | — | Yes | this paper | Table 1 |
| GAT | 52.3700 | — | Yes | this paper | Table 1 |
| SAGE | 56.0500 | — | Yes | this paper | Table 1 |
| LRGB | 57.3600 | — | Yes | this paper | Table 1 |
| BORF | 54.2100 | — | Yes | this paper | Table 1 |
| FOSR | 52.3700 | — | Yes | this paper | Table 1 |
| SDRF | 52.6300 | — | Yes | this paper | Table 1 |
| GTR | 52.3700 | — | Yes | this paper | Table 1 |
| DR | 69.4500 | — | Yes | this paper | Table 1 |
| LASER | 32.6300 | — | Yes | this paper | Table 1 |
| GOKU | 37.1000 | — | Yes | this paper | Table 1 |
| CaCoSE | 54.4700 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: kipf2016semi)
- **GAT** (from: velivckovic2017graph)
- **SAGE** (from: hamilton2017inductive)
- **LRGB** (from: dwivedi2022long)
- **BORF** (from: nguyen2023revisiting)
- **FOSR** (from: karhadkar2022fosr)
- **SDRF** (from: topping2021understanding)
- **GTR** (from: black2023understanding)
- **DR** (from: attali2024delaunay)
- **LASER** (from: barbero2023locality)
- **GOKU** (from: liang2025mitigating)
- **CaCoSE (without Attention)** (from: this paper)
- **CaCoSE (without CaEF)** (from: this paper)
- **CaCoSE (TopkPool)** (from: this paper)
- **CaCoSE (DMon)** (from: this paper)
- **CaCoSE (GMT)** (from: this paper)
- **CaCoSE (GAT)** (from: this paper)
- **CaCoSE (SAGE)** (from: this paper)

## Extraction Notes

[Cora] Extracted only the 'Cora' column from Table 1 (Node Classification Accuracy Comparison).
Standard configuration used. No standard deviation reported in the table. Table 3 (delta
sensitivity) and Table 4 (ablation) were ignored as they represent variants/ablations rather than
the primary benchmark comparison against baselines. [CiteSeer] Extracted results for CiteSeer from
Table 1 (Node Classification Accuracy Comparison). The dataset is referred to as 'C.Seer' in the
table header. No standard deviation values were reported in the table. All values are test
accuracies as implied by the context of node classification benchmarks. [CoAuthor CS] Extracted only
the 'CoAuthor CS' column from Table 1 as requested. All other tables (graph classification,
ablation, delta sensitivity) were ignored. No standard deviation values were reported in the table
for this dataset. [Amazon Computers] failed: 1 validation error for ExtractionOutput
results.10.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[Amazon Photos] Extracted only the 'Amazon Photos' (abbreviated as 'Am. Pto' in the table) column
from Table 1. All other tables were ignored as they do not contain Amazon Photos results or are
ablation/sensitivity studies not reporting standard benchmark results for this specific dataset. No
standard deviation values were reported in the table. [Texas] Extracted only the 'Texas' column from
Table 1 (Node Classification Accuracy Comparison). All other datasets were ignored as per
instructions. No standard deviation values were reported in the table for this dataset. [Chameleon]
Extracted only the 'Chameleon' dataset results from Table 1 (labeled 'Cham.' in the table). The
paper does not report standard deviations for these results. Other tables (Table 2, Table 3, Table
4) do not contain Chameleon results or are for graph classification/ablation on other datasets.
[Squirrel] failed: 1 validation error for ExtractionOutput results.5.value   Input should be a valid
number [type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [MUTAG] Extracted only MUTAG results from Table 2
(Graph Classification benchmarks). Table 1 contains Node Classification results and is ignored.
Table 3 and 4 contain ablation/sensitivity analysis and are ignored as they are not primary
benchmark results for the standard configuration. No standard deviations were reported in the table
for these values. [IMDB-BINARY] Extracted results for IMDB-B (IMDB-BINARY) from Table 2 (main
comparison) and Table 4 (ablation study). Note that Table 4 lists ablation variants as separate
rows. The standard configuration is delta=3, which corresponds to the main CaCoSE result in Table 2.
Other delta values in Table 3 are excluded as per instructions to skip optional variants. No
standard deviation values were reported in the tables. [IMDB-MULTI] Extracted results for IMDB-M
(IMDB-MULTI) from Table 2. The table header uses 'IMDB-M' which corresponds to IMDB-MULTI in
standard graph classification benchmarks (alongside IMDB-B for IMDB-BINARY). No standard deviation
values were reported in the table. The proposed model is CaCoSE. [REDDIT-BINARY] The dataset
'REDDIT-BINARY' is not present in any of the provided tables. Table 1 contains node classification
datasets (Cora, C.Seer, etc.). Table 2 contains graph classification datasets (MUTAG, IMDB-B,
IMDB-M, RDT-B, COLLAB, PROTEINS). Table 3 and 4 are ablation/sensitivity studies on subsets of the
datasets in Tables 1 and 2. No results for REDDIT-BINARY were found. [COLLAB] failed: 1 validation
error for ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [PROTEINS] Extracted results for the PROTEINS dataset
from Table 2 (Graph Classification Benchmarks). The primary metric is Accuracy. Standard
configuration results are used. Sensitivity analysis in Table 3 and ablation in Table 4 were
excluded as they represent variations/ablations rather than the standard benchmark comparison.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*