# Extraction: KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: KAN-based GNNs (BS-KAGCN, RBF-KAGCN, BS-KAGAT, RBF-KAGAT, BS-KAGIN, RBF-KAGIN)
- Type: GNN

## Results

### Actor — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 32.8100 | 1.1100 | Yes | this paper | Table 1 |
| BS-KAGCN | 34.4500 | 1.1200 | No | this paper | Table 1 |
| RBF-KAGCN | 34.7700 | 1.2000 | No | this paper | Table 1 |
| GAT | 32.5100 | 1.1700 | Yes | this paper | Table 1 |
| BS-KAGAT | 31.6600 | 1.2300 | No | this paper | Table 1 |
| RBF-KAGAT | 34.0400 | 0.9400 | No | this paper | Table 1 |
| GIN | 33.4600 | 1.3800 | Yes | this paper | Table 1 |
| BS-KAGIN | 34.2600 | 1.0600 | No | this paper | Table 1 |
| RBF-KAGIN | 34.3700 | 0.9500 | No | this paper | Table 1 |

### CiteSeer — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 71.6000 | 0.4000 | Yes | this paper | Table 1 |
| BS-KAGCN | 70.0400 | 1.6600 | Yes | this paper | Table 1 |
| RBF-KAGCN | 68.1600 | 0.6100 | Yes | this paper | Table 1 |
| GAT | 60.9100 | 1.0400 | Yes | this paper | Table 2 |
| BS-KAGAT | 56.8700 | 1.6700 | Yes | this paper | Table 2 |
| RBF-KAGAT | 48.6500 | 2.3900 | Yes | this paper | Table 2 |
| GIN | 47.9800 | 0.9100 | Yes | this paper | Table 2 |
| BS-KAGIN | 55.7700 | 1.5100 | Yes | this paper | Table 2 |
| RBF-KAGIN | 46.8700 | 1.9300 | Yes | this paper | Table 2 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 81.6000 | 0.4000 | Yes | this paper | Table 1 |
| BS-KAGCN | 80.8400 | 1.6100 | No | this paper | Table 1 |
| RBF-KAGCN | 81.7200 | 0.7900 | No | this paper | Table 1 |
| GAT | 76.5100 | 0.7900 | Yes | this paper | Table 2 |
| BS-KAGAT | 78.2800 | 0.8300 | No | this paper | Table 2 |
| RBF-KAGAT | 72.6200 | 1.6400 | No | this paper | Table 2 |
| GIN | 70.8500 | 1.7500 | Yes | this paper | Table 2 |
| BS-KAGIN | 65.7800 | 1.6800 | No | this paper | Table 2 |
| RBF-KAGIN | 72.7700 | 1.3500 | No | this paper | Table 2 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 66.1300 | 6.0900 | Yes | this paper | Table 1 |
| BS-KAGCN | 67.7500 | 6.5400 | No | this paper | Table 1 |
| RBF-KAGCN | 67.7500 | 7.2400 | Yes | this paper | Table 1 |
| GAT | 66.8500 | 5.5900 | Yes | this paper | Table 1 |
| BS-KAGAT | 67.6600 | 6.9400 | No | this paper | Table 1 |
| RBF-KAGAT | 64.1400 | 6.1400 | Yes | this paper | Table 1 |
| GIN | 69.1000 | 4.8500 | Yes | this paper | Table 1 |
| BS-KAGIN | 69.6400 | 7.4000 | No | this paper | Table 1 |
| RBF-KAGIN | 67.3000 | 6.4400 | Yes | this paper | Table 1 |

### DD — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 65.8700 | 6.3300 | Yes | this paper | Table 1 |
| BS-KAGCN | 72.7400 | 4.1600 | Yes | this paper | Table 1 |
| RBF-KAGCN | 66.7800 | 5.9100 | Yes | this paper | Table 1 |
| GAT | 71.9200 | 5.8800 | Yes | this paper | Table 1 |
| BS-KAGAT | 78.2700 | 2.3700 | Yes | this paper | Table 1 |
| RBF-KAGAT | 73.4200 | 4.7600 | Yes | this paper | Table 1 |
| GIN | 74.7800 | 3.8200 | Yes | this paper | Table 1 |
| BS-KAGIN | 76.0600 | 5.1000 | No | this paper | Table 1 |
| RBF-KAGIN | 75.9200 | 3.4900 | Yes | this paper | Table 1 |

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 20.5600 | 3.7000 | Yes | this paper | Table 1 |
| BS-KAGCN | 59.0600 | 4.4800 | No | this paper | Table 1 |
| RBF-KAGCN | 56.8300 | 8.3700 | Yes | this paper | Table 1 |
| GAT | 18.1700 | 1.3400 | Yes | this paper | Table 1 |
| BS-KAGAT | 51.3300 | 12.9000 | Yes | this paper | Table 1 |
| RBF-KAGAT | 49.7800 | 7.6500 | Yes | this paper | Table 1 |
| GIN | 54.7200 | 6.5500 | Yes | this paper | Table 1 |
| BS-KAGIN | 44.5000 | 8.5300 | Yes | this paper | Table 1 |
| RBF-KAGIN | 44.7800 | 9.5800 | Yes | this paper | Table 1 |

### IMDB-B — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 68.4000 | 4.0100 | Yes | this paper | Table 1 |
| BS-KAGCN | 72.8700 | 5.1200 | No | this paper | Table 1 |
| RBF-KAGCN | 73.1300 | 4.5000 | Yes | this paper | Table 1 |
| GAT | 67.3700 | 3.8300 | Yes | this paper | Table 1 |
| BS-KAGAT | 72.0000 | 3.8000 | Yes | this paper | Table 1 |
| RBF-KAGAT | 71.0000 | 5.0400 | Yes | this paper | Table 1 |
| GIN | 73.3700 | 2.9000 | Yes | this paper | Table 1 |
| BS-KAGIN | 73.1300 | 4.4600 | Yes | this paper | Table 1 |
| RBF-KAGIN | 69.9300 | 3.8400 | Yes | this paper | Table 1 |

### IMDB-M — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 48.5600 | 3.7100 | Yes | this paper | Table 1 |
| BS-KAGCN | 50.0400 | 3.9900 | No | this paper | Table 1 |
| RBF-KAGCN | 49.8400 | 3.7800 | Yes | this paper | Table 1 |
| GAT | 48.2400 | 5.0200 | Yes | this paper | Table 1 |
| BS-KAGAT | 50.0900 | 4.3400 | Yes | this paper | Table 1 |
| RBF-KAGAT | 48.1300 | 4.1500 | Yes | this paper | Table 1 |
| GIN | 50.3600 | 4.1000 | Yes | this paper | Table 1 |
| BS-KAGIN | 50.3300 | 3.8700 | Yes | this paper | Table 1 |
| RBF-KAGIN | 49.2200 | 4.4100 | Yes | this paper | Table 1 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 59.9500 | 8.9800 | Yes | this paper | Table 1 |
| BS-KAGCN | 71.7000 | 7.5400 | No | this paper | Table 1 |
| RBF-KAGCN | 77.8600 | 9.4500 | Yes | this paper | Table 1 |
| GAT | 57.5100 | 12.3000 | Yes | this paper | Table 1 |
| BS-KAGAT | 82.6600 | 4.7800 | Yes | this paper | Table 1 |
| RBF-KAGAT | 75.8800 | 12.1000 | Yes | this paper | Table 1 |
| GIN | 86.1600 | 5.9600 | Yes | this paper | Table 1 |
| BS-KAGIN | 85.7900 | 8.0600 | Yes | this paper | Table 1 |
| RBF-KAGIN | 85.1000 | 5.6000 | Yes | this paper | Table 1 |

### NCI1 — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 60.1000 | 4.6300 | Yes | this paper | Table 1 |
| BS-KAGCN | 73.9700 | 4.0100 | No | this paper | Table 1 |
| RBF-KAGCN | 73.0700 | 2.9000 | No | this paper | Table 1 |
| GAT | 60.4200 | 8.2100 | Yes | this paper | Table 1 |
| BS-KAGAT | 76.4600 | 3.6600 | No | this paper | Table 1 |
| RBF-KAGAT | 72.6300 | 4.6500 | No | this paper | Table 1 |
| GIN | 79.3200 | 1.6300 | Yes | this paper | Table 1 |
| BS-KAGIN | 80.3400 | 1.4600 | No | this paper | Table 1 |
| RBF-KAGIN | 79.1900 | 1.8100 | No | this paper | Table 1 |

### Ogbn-arxiv — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 53.2100 | 0.1300 | Yes | this paper | Table 1 |
| BS-KAGCN | 53.7600 | 0.3100 | No | this paper | Table 1 |
| RBF-KAGCN | 53.6500 | 0.2000 | Yes | this paper | Table 1 |
| GAT | 53.6800 | 0.1200 | Yes | this paper | Table 1 |
| BS-KAGAT | 55.1700 | 0.1200 | Yes | this paper | Table 1 |
| RBF-KAGAT | 54.2400 | 0.2500 | Yes | this paper | Table 1 |
| GIN | 53.5800 | 0.7400 | Yes | this paper | Table 1 |
| BS-KAGIN | 53.0500 | 0.5500 | Yes | this paper | Table 1 |
| RBF-KAGIN | 53.5600 | 0.3700 | Yes | this paper | Table 1 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 63.1000 | 3.7500 | Yes | this paper | Table 1 |
| BS-KAGCN | 75.6800 | 3.4900 | No | this paper | Table 1 |
| RBF-KAGCN | 73.6700 | 3.9900 | Yes | this paper | Table 1 |
| GAT | 59.7800 | 0.8700 | Yes | this paper | Table 1 |
| BS-KAGAT | 72.7500 | 2.1800 | Yes | this paper | Table 1 |
| RBF-KAGAT | 71.9300 | 4.2300 | Yes | this paper | Table 1 |
| GIN | 70.6600 | 3.6000 | Yes | this paper | Table 1 |
| BS-KAGIN | 73.3700 | 2.8100 | Yes | this paper | Table 1 |
| RBF-KAGIN | 74.3300 | 3.5200 | Yes | this paper | Table 1 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 55.0100 | 0.7500 | Yes | this paper | Table 1 |
| BS-KAGIN | 58.7100 | 1.0200 | No | this paper | Table 1 |
| RBF-KAGIN | 57.6800 | 2.0500 | Yes | this paper | Table 1 |

### QM9 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.0969 | 0.0017 | Yes | this paper | Table 1 |
| BS-KAGIN | 0.0618 | 0.0007 | No | this paper | Table 1 |
| RBF-KAGIN | 0.0778 | 0.0023 | Yes | this paper | Table 1 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 72.3400 | 5.9200 | Yes | this paper | Table 1 |
| BS-KAGCN | 72.1600 | 5.6800 | No | this paper | Table 1 |
| RBF-KAGCN | 71.6200 | 4.6900 | Yes | this paper | Table 1 |
| GAT | 69.0100 | 6.1400 | Yes | this paper | Table 1 |
| BS-KAGAT | 73.7800 | 6.3900 | No | this paper | Table 1 |
| RBF-KAGAT | 71.7100 | 6.4900 | Yes | this paper | Table 1 |
| GIN | 73.5100 | 5.8700 | Yes | this paper | Table 1 |
| BS-KAGIN | 72.9700 | 5.6300 | No | this paper | Table 1 |
| RBF-KAGIN | 73.6000 | 5.0500 | Yes | this paper | Table 1 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 78.6300 | 5.4300 | Yes | this paper | Table 1 |
| BS-KAGCN | 78.6300 | 5.2600 | No | this paper | Table 1 |
| RBF-KAGCN | 77.4500 | 4.1100 | Yes | this paper | Table 1 |
| GAT | 78.1700 | 5.7000 | Yes | this paper | Table 1 |
| BS-KAGAT | 78.4300 | 5.4700 | Yes | this paper | Table 1 |
| RBF-KAGAT | 76.3400 | 4.3400 | Yes | this paper | Table 1 |
| GIN | 78.2400 | 4.7600 | Yes | this paper | Table 1 |
| BS-KAGIN | 78.6300 | 5.1600 | Yes | this paper | Table 1 |
| RBF-KAGIN | 76.7300 | 4.8800 | Yes | this paper | Table 1 |

### ZINC-12K — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.4131 | 0.0215 | Yes | this paper | Table 1 |
| BS-KAGIN | 0.3000 | 0.0332 | No | this paper | Table 1 |
| RBF-KAGIN | 0.3026 | 0.0663 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **GCN**, 3.3M params (from: Kipf & Welling 2017)
- **GAT** (from: Veličković et al. 2018)
- **GIN** (from: Xu et al. 2019)
- **BS-KAGCN** (from: this paper)
- **RBF-KAGCN** (from: this paper)
- **BS-KAGAT** (from: this paper)
- **RBF-KAGAT** (from: this paper)
- **BS-KAGIN** (from: this paper)
- **RBF-KAGIN** (from: this paper)

## Extraction Notes

[Cora] Extracted node classification accuracy results for Cora from Table 1 and Table 2. Table 1
reports results based on Luo et al. using GCN-based models, while Table 2 reports results for GCN,
GAT, and GIN variants (including KAN-based versions). Both tables use the standard Cora dataset.
Link prediction results (Table 3) were ignored as per instructions to focus on Accuracy for node
classification. The 'standard/default' configuration is assumed to be the one reported in these
tables, as no other variants are specified for Cora in the text. [CiteSeer] Extracted Accuracy
results for CiteSeer from Table 1 and Table 2. Table 1 reports results from Luo et al. using GCN-
based models, while Table 2 reports node classification accuracies for various GNN variants (GCN,
GAT, GIN) and their KAN-based counterparts (BS-KAGCN, RBF-KAGCN, etc.). The link prediction results
in Table 3 were ignored as per the FOCUS instruction to prioritize Accuracy. Note that Table 1 and
Table 2 present different experimental setups/configurations (Table 1 seems to be a
reproduction/comparison with Luo et al. using specific GCN variants, while Table 2 is the main node
classification experiment). Both sets of results for CiteSeer Accuracy were extracted. [Ogbn-arxiv]
Extracted all models from Table 1 for the Ogbn-arxiv dataset. The table caption indicates 'Average
node classification accuracies (± standard deviation)'. The proposed model is identified as BS-KAGCN
based on the text 'Our second approach... replace the MLP with KAN' and the fact that BS-KAGCN is
bolded (best result) for Ogbn-arxiv in the table, although BS-KAGAT also has a high score. The
prompt asks to extract ALL rows, so all baselines and variants are included. The dataset name is
exactly 'Ogbn-arxiv' as in the table header. [Cornell] Extracted all rows from Table 1 for the
'Cornell' dataset column. The table caption indicates 'average node classification accuracies (±
standard deviation)'. All values are test-set results as implied by the context of reporting final
accuracies. No other datasets were included per instructions. [Texas] Extracted all rows from Table
1 corresponding to the 'Texas' dataset column. The table reports 'Average node classification
accuracies (± standard deviation)'. All values were parsed correctly. The proposed models are
identified as the KAN-based variants (BS-KAGCN, BS-KAGAT, BS-KAGIN) based on the text describing the
replacement of MLP with KAN. [Wisconsin] Extracted all rows from Table 1 for the 'Wisconsin' dataset
column. The table caption indicates 'Average node classification accuracies (± standard deviation)'.
All values were parsed correctly. The proposed model is identified as BS-KAGCN based on the text
describing the comparison of vanilla architectures with KAN replacements, where BS-KAGCN is the
primary proposed variant compared against baselines like GCN, GAT, GIN. [Actor] Extracted all rows
from Table 1 for the 'Actor' dataset column. The table caption indicates 'Average node
classification accuracies (± standard deviation)'. All values are test-set results as implied by the
context of reporting final accuracies. The proposed models are variants of KAN-based GNNs (BS-KAGCN,
RBF-KAGCN, etc.). [MUTAG] Extracted all rows from Table 1 for the MUTAG dataset. The table caption
indicates 'Average graph classification accuracy (± standard deviation)'. The proposed model appears
to be one of the KAGCN/KAGAT/KAGIN variants (likely BS-KAGCN based on the 'proposed' field
assumption, though the paper text doesn't explicitly name a single 'proposed' model in the snippet,
BS-KAGCN is listed first among the new variants). All other models are treated as baselines. No
external data usage is indicated. [DD] Extracted all rows from Table 1 for the 'DD' dataset column.
The metric is Accuracy. Standard deviations are parsed from the '±' notation. BS-KAGIN is identified
as the proposed model based on the paper's focus on KAN-based GNNs (KAGIN variants) and the specific
mention of comparing vanilla architectures with KAN replacements. [NCI1] Extracted all rows from
Table 1 corresponding to the NCI1 dataset column. The table caption indicates 'Average graph
classification accuracy (± standard deviation)'. The proposed models appear to be variants of
KAGCN/KAGAT/KAGIN (BS and RBF versions). Baselines are standard GCN, GAT, and GIN. [PROTEINS]
Extracted only the PROTEINS column from Table 1 as requested. The table caption indicates 'Average
graph classification accuracy (± standard deviation)'. All values are test-set results implied by
the context of benchmark reporting. BS-KAGCN is identified as the proposed model based on the
bolding in the PROTEINS column and the figure captions highlighting it. [ENZYMES] Extracted all rows
from Table 1 corresponding to the ENZYMES dataset column. The proposed model is identified as BS-
KAGCN based on the bolding of its result in the ENZYMES column (59.06) and the figure captions
highlighting BS-KAGCN/GCN comparisons. All other models are treated as baselines. Standard deviation
values were parsed from the 'mean ± std' format. [IMDB-B] Extracted all rows from Table 1 for the
'IMDB-B' column. The proposed model is identified as BS-KAGCN based on the context of the figures
and the typical structure of such papers where the first variant of the proposed method is
highlighted or listed first in its group, although RBF-KAGCN actually has a slightly higher mean
accuracy. However, BS-KAGCN is listed first under the GCN baseline group and is often the primary
proposed variant. If the paper proposes both BS and RBF variants, both are treated as proposed, but
typically one is the main focus. Given the ambiguity in 'proposed' status without explicit text
stating 'we propose BS-KAGCN', I have marked BS-KAGCN as proposed based on it being the first new
model listed. All other new models (RBF-KAGCN, BS-KAGAT, etc.) are marked as false for is_proposed
to be conservative, or could be considered proposed if the paper proposes the whole
KAGCN/KAGAT/KAGIN family. However, usually 'BS' and 'RBF' are ablations or variants. I will stick to
marking the first one as proposed or null if unclear. Re-reading the prompt: 'is_proposed: true if
it is the model introduced in the paper'. Without explicit text, it's hard. I will mark BS-KAGCN as
true as it's the first new entry. Actually, looking at the table, BS-KAGCN, RBF-KAGCN, BS-KAGAT,
RBF-KAGAT, BS-KAGIN, RBF-KAGIN are all new. I will mark BS-KAGCN as true and others as false for
simplicity, or mark all KAGCN/KAGAT/KAGIN variants as false if they are just baselines for the
proposed method. Let's assume BS-KAGCN is the primary proposed model. Wait, the prompt asks for
'proposed_model' in the header. I will set it to BS-KAGCN. For the results, I will mark BS-KAGCN as
true. The others are likely variants/ablations. If the paper proposes 'KAGCN' with BS and RBF
kernels, then both are proposed. I will mark BS-KAGCN as true and others as false to avoid
overclaiming, or mark all as false if unsure. Let's look at the 'baseline_models' list. I included
GCN, GAT, GIN as baselines. The KAGCN variants are the new ones. I will mark BS-KAGCN as true.
[IMDB-M] Extracted all rows from Table 1 for the 'IMDB-M' column. The table caption indicates
'Average graph classification accuracy (± standard deviation)'. The proposed model is identified as
BS-KAGCN based on the context of the paper focusing on KAGCN variants, though the paper presents
multiple variants (BS/RBF for GCN/GAT/GIN). All values were parsed correctly. [ZINC-12K] Extracted
all rows from Table 1 for the ZINC-12K dataset. The metric is MAE (lower is better). Standard
deviations are provided in the format 'mean ± std'. BS-KAGIN is identified as the proposed model
based on the text highlighting its performance and the bold formatting in the table. [QM9] Extracted
MAE results for QM9 from Table 1. The table reports average MAE with standard deviation. BS-KAGIN is
the proposed model (indicated by bold values and text description). GIN is the primary baseline.
RBF-KAGIN is an ablation/variant baseline. All values are test-set results as per the experimental
setup description ('report the average performance on the test set'). [Peptides-func] Extracted all
three models from Table 1 for the Peptides-func dataset. The metric is Average Precision (AP).
Standard deviations are explicitly provided in the table. BS-KAGIN is identified as the proposed
model based on the text highlighting its performance and the bold formatting in the table.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*