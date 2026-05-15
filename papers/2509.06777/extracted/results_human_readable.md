# Extraction: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: CAMP
- Type: GNN

## Results

### ENZYMES — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 27.6600 | 1.1600 | Yes | this paper | Table 1 |
| GCN + DIGL | 27.5100 | 1.0500 | Yes | this paper | Table 1 |
| GCN + SDRF | 28.3600 | 1.1700 | Yes | this paper | Table 1 |
| GCN + FoSR | 25.0600 | 0.9900 | Yes | this paper | Table 1 |
| GCN + BORF | 24.7000 | 1.0000 | Yes | this paper | Table 1 |
| GCN + GTR | 27.5200 | 0.9900 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 17.3800 | 1.0300 | Yes | this paper | Table 1 |
| GCN + PANDA | 31.5500 | 1.2300 | Yes | this paper | Table 1 |
| GCN + CAMP (Ours) | 31.7300 | 2.3000 | No | this paper | Table 1 |
| GIN (None) | 33.8000 | 0.1100 | Yes | this paper | Table 1 |
| GIN + DIGL | 35.7100 | 1.1900 | Yes | this paper | Table 1 |
| GIN + SDRF | 35.8100 | 1.0000 | Yes | this paper | Table 1 |
| GIN + FoSR | 29.2000 | 1.3600 | Yes | this paper | Table 1 |
| GIN + BORF | 35.5000 | 1.2000 | Yes | this paper | Table 1 |
| GIN + GTR | 30.5700 | 1.4200 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 16.5800 | 0.9000 | Yes | this paper | Table 1 |
| GIN + PANDA | 46.2000 | 1.4100 | Yes | this paper | Table 1 |
| GIN + CAMP (Ours) | 46.6000 | 2.2600 | No | this paper | Table 1 |
| CAMP-GCN (Degree) | 28.9300 | 2.6500 | Yes | this paper | Table 2 |
| CAMP-GCN (Betweenness) | 30.2000 | 2.5600 | Yes | this paper | Table 2 |
| CAMP-GCN (PageRank) | 29.4000 | 2.3700 | Yes | this paper | Table 2 |
| CAMP-GCN (Load) | 31.1300 | 2.2200 | Yes | this paper | Table 2 |
| CAMP-GCN (Closeness) | 31.7300 | 2.3000 | No | this paper | Table 2 |
| CAMP-GIN (Degree) | 43.1300 | 2.8800 | Yes | this paper | Table 3 |
| CAMP-GIN (Betweenness) | 41.8700 | 2.6200 | Yes | this paper | Table 3 |
| CAMP-GIN (PageRank) | 41.0000 | 2.5400 | Yes | this paper | Table 3 |
| CAMP-GIN (Load) | 39.9300 | 2.4400 | Yes | this paper | Table 3 |
| CAMP-GIN (Closeness) | 46.6000 | 2.2600 | No | this paper | Table 3 |

### IMDB-BINARY — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 49.7700 | 0.8100 | Yes | this paper | Table 1 |
| + DIGL | 49.9100 | 0.8400 | Yes | this paper | Table 1 |
| + SDRF | 49.4000 | 0.9000 | Yes | this paper | Table 1 |
| + FoSR | 49.6600 | 0.8600 | Yes | this paper | Table 1 |
| + BORF | 50.1000 | 0.9000 | Yes | this paper | Table 1 |
| + GTR | 49.9200 | 0.9900 | Yes | this paper | Table 1 |
| + CT-Layer | 50.3200 | 0.9400 | Yes | this paper | Table 1 |
| + PANDA | 63.7600 | 1.0100 | Yes | this paper | Table 1 |
| + CAMP (Ours) | 62.4400 | 2.1500 | No | this paper | Table 1 |
| GIN (None) | 70.1800 | 0.9900 | Yes | this paper | Table 1 |
| CAMP-GCN (Degree) | 58.5200 | 2.3400 | Yes | this paper | Table 2 |
| CAMP-GCN (Betweenness) | 58.2400 | 2.3200 | Yes | this paper | Table 2 |
| CAMP-GCN (PageRank) | 60.4800 | 1.8900 | Yes | this paper | Table 2 |
| CAMP-GCN (Load) | 59.3200 | 1.9500 | Yes | this paper | Table 2 |
| CAMP-GCN (Closeness) | 59.5200 | 2.1400 | Yes | this paper | Table 2 |
| CAMP-GIN (Degree) | 70.6400 | 1.6800 | Yes | this paper | Table 3 |
| CAMP-GIN (Betweenness) | 69.7600 | 2.1500 | Yes | this paper | Table 3 |
| CAMP-GIN (PageRank) | 71.4800 | 1.4700 | Yes | this paper | Table 3 |
| CAMP-GIN (Load) | 69.8400 | 1.9400 | Yes | this paper | Table 3 |
| CAMP-GIN (Closeness) | 71.0000 | 1.9900 | Yes | this paper | Table 3 |

### MUTAG — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 72.1500 | 2.4400 | Yes | this paper | Table 1 |
| GCN + DIGL | 71.3500 | 2.3900 | Yes | this paper | Table 1 |
| GCN + SDRF | 71.0500 | 1.8700 | Yes | this paper | Table 1 |
| GCN + FoSR | 80.0000 | 1.5700 | Yes | this paper | Table 1 |
| GCN + BORF | 75.8000 | 1.9000 | Yes | this paper | Table 1 |
| GCN + GTR | 79.1000 | 1.8600 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 75.8900 | 3.0200 | Yes | this paper | Table 1 |
| GCN + PANDA | 85.7500 | 1.3900 | Yes | this paper | Table 1 |
| CAMP (Ours) with GCN | 80.8000 | 3.6800 | No | this paper | Table 1 |
| GIN (None) | 77.7000 | 0.3600 | Yes | this paper | Table 1 |
| GIN + DIGL | 79.7000 | 2.1500 | Yes | this paper | Table 1 |
| GIN + SDRF | 78.4000 | 2.8000 | Yes | this paper | Table 1 |
| GIN + FoSR | 78.4000 | 2.8000 | Yes | this paper | Table 1 |
| GIN + BORF | 80.8000 | 2.5000 | Yes | this paper | Table 1 |
| GIN + GTR | 77.6000 | 2.8400 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 56.8500 | 4.2500 | Yes | this paper | Table 1 |
| GIN + PANDA | 88.7500 | 1.5700 | Yes | this paper | Table 1 |
| CAMP (Ours) with GIN | 83.4000 | 3.9500 | No | this paper | Table 1 |
| CAMP-GCN (Degree) | 78.4000 | 4.4600 | Yes | this paper | Table 2 |
| CAMP-GCN (Betweenness) | 78.2000 | 4.2000 | Yes | this paper | Table 2 |
| CAMP-GCN (PageRank) | 78.4000 | 4.0700 | Yes | this paper | Table 2 |
| CAMP-GCN (Load) | 78.2000 | 4.1600 | Yes | this paper | Table 2 |
| CAMP-GCN (Closeness) | 77.6000 | 3.8800 | Yes | this paper | Table 2 |
| CAMP-GIN (Degree) | 80.0000 | 4.3600 | Yes | this paper | Table 3 |
| CAMP-GIN (Betweenness) | 77.0000 | 4.1600 | Yes | this paper | Table 3 |
| CAMP-GIN (PageRank) | 74.0000 | 4.0800 | Yes | this paper | Table 3 |
| CAMP-GIN (Load) | 76.0000 | 4.2800 | Yes | this paper | Table 3 |
| CAMP-GIN (Closeness) | 76.2000 | 2.9600 | Yes | this paper | Table 3 |

### PROTEINS — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 70.9800 | 0.7300 | Yes | this paper | Table 1 |
| GCN + DIGL | 70.6000 | 0.7300 | Yes | this paper | Table 1 |
| GCN + SDRF | 70.9200 | 0.7900 | Yes | this paper | Table 1 |
| GCN + FoSR | 73.4200 | 0.8100 | Yes | this paper | Table 1 |
| GCN + BORF | 71.0000 | 0.8000 | Yes | this paper | Table 1 |
| GCN + GTR | 72.5900 | 2.4800 | Yes | this paper | Table 1 |
| GCN + CT-Layer | 60.3500 | 1.0600 | Yes | this paper | Table 1 |
| GCN + PANDA | 76.0000 | 0.7700 | Yes | this paper | Table 1 |
| CAMP (Ours) with GCN | 74.4300 | 1.6400 | No | this paper | Table 1 |
| GIN (None) | 70.8000 | 0.8200 | Yes | this paper | Table 1 |
| GIN + DIGL | 70.7500 | 0.7700 | Yes | this paper | Table 1 |
| GIN + SDRF | 69.8100 | 0.7900 | Yes | this paper | Table 1 |
| GIN + FoSR | 73.1000 | 0.8100 | Yes | this paper | Table 1 |
| GIN + BORF | 73.7000 | 0.8000 | Yes | this paper | Table 1 |
| GIN + GTR | 73.1300 | 0.6900 | Yes | this paper | Table 1 |
| GIN + CT-Layer | 61.1000 | 1.1800 | Yes | this paper | Table 1 |
| GIN + PANDA | 75.7500 | 0.8500 | Yes | this paper | Table 1 |
| CAMP (Ours) with GIN | 74.0700 | 1.7300 | No | this paper | Table 1 |
| CAMP-GCN (Degree) | 72.0000 | 1.7500 | Yes | this paper | Table 2 |
| CAMP-GCN (Betweenness) | 71.5400 | 1.5800 | Yes | this paper | Table 2 |
| CAMP-GCN (PageRank) | 71.1400 | 1.9000 | Yes | this paper | Table 2 |
| CAMP-GCN (Load) | 72.1100 | 1.9800 | Yes | this paper | Table 2 |
| CAMP-GCN (Closeness) | 74.4300 | 1.6400 | No | this paper | Table 2 |
| CAMP-GIN (Degree) | 72.3900 | 1.8900 | Yes | this paper | Table 3 |
| CAMP-GIN (Betweenness) | 72.0700 | 2.0200 | Yes | this paper | Table 3 |
| CAMP-GIN (PageRank) | 72.6800 | 1.5500 | Yes | this paper | Table 3 |
| CAMP-GIN (Load) | 72.6400 | 2.2600 | Yes | this paper | Table 3 |
| CAMP-GIN (Closeness) | 74.0700 | 1.7300 | No | this paper | Table 3 |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 59.3000 | 0.2300 | Yes | this paper | Table 1 |
| GCN + SDRF | 59.4700 | 1.2600 | Yes | this paper | Table 1 |
| GCN + FoSR | 59.4700 | 0.3500 | Yes | this paper | Table 1 |
| GCN + BORF | 59.9400 | 0.3700 | Yes | this paper | Table 1 |
| GCN + PANDA | 60.2800 | 0.3100 | Yes | this paper | Table 1 |
| CAMP (Ours) | 56.6700 | 0.7600 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (None) | 0.3496 | 0.0013 | Yes | this paper | Table 1 |
| GCN + SDRF | 0.3478 | 0.0013 | Yes | this paper | Table 1 |
| GCN + FoSR | 0.3473 | 0.0007 | Yes | this paper | Table 1 |
| GCN + BORF | 0.3514 | 0.0009 | Yes | this paper | Table 1 |
| GCN + PANDA | 0.3272 | 0.0001 | Yes | this paper | Table 1 |
| CAMP (Ours) | 0.3138 | 0.0041 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GIN** (from: Xu et al. 2019)
- **DIGL** (from: null)
- **SDRF** (from: null)
- **FoSR** (from: null)
- **BORF** (from: null)
- **GTR** (from: null)
- **CT-Layer** (from: null)
- **PANDA** (from: null)
- **GCN (None)**
- **GCN + SDRF**
- **GCN + FoSR**
- **GCN + BORF**
- **GCN + PANDA**

## Extraction Notes

[ENZYMES] Extracted all rows for the ENZYMES dataset from Table 1, Table 2, and Table 3. Table 1
contains results for GCN and GIN backbones with various augmentation methods. Table 2 and Table 3
contain ablation studies for CAMP-GCN and CAMP-GIN respectively using different centrality measures.
The 'Closeness' centrality corresponds to the proposed CAMP method as indicated by the green
highlighting and consistency with Table 1. All values are test accuracies. [MUTAG] Extracted all
MUTAG results from Table 1, Table 2, and Table 3. Table 1 contains the main comparison of CAMP vs
baselines (GCN and GIN variants). Tables 2 and 3 contain ablation studies on centrality measures for
CAMP-GCN and CAMP-GIN respectively. All values are test accuracies. The proposed model is CAMP,
implemented with both GCN and GIN backbones. [PROTEINS] Extracted all rows from Table 1, Table 2,
and Table 3 for the PROTEINS dataset. Table 1 contains results for GCN and GIN backbones with
various rewiring methods (DIGL, SDRF, FoSR, BORF, GTR, CT-Layer, PANDA) and the proposed CAMP
method. Tables 2 and 3 provide ablation studies for CAMP using different centrality measures
(Degree, Betweenness, PageRank, Load, Closeness) for GCN and GIN respectively. The 'CAMP (Ours)'
rows in Table 1 correspond to the Closeness centrality variant as confirmed by Tables 2 and 3. All
values are test accuracies. [COLLAB] failed: 2 validation errors for ExtractionOutput
results.4.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
results.13.value   Input should be a valid number [type=float_type, input_value=None,
input_type=NoneType]     For further information visit https://errors.pydantic.dev/2.13/v/float_type
[IMDB-BINARY] Extracted all rows from Table 1, Table 2, and Table 3 corresponding to the IMDB-BINARY
dataset. Table 1 contains the main comparison of CAMP vs baselines (GCN and GIN variants). Tables 2
and 3 contain ablation studies on centrality measures for CAMP-GCN and CAMP-GIN respectively. All
values are test accuracies with standard deviations. The primary metric Accuracy was used. No
external data usage was indicated for these specific benchmarks. [REDDIT-BINARY] failed: 2
validation errors for ExtractionOutput results.4.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.13.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Peptides-func] Extracted only Peptides-func AP
results as requested. Note that CAMP (Ours) has a lower AP score (56.67) compared to baselines like
PANDA (60.28) on this specific metric, despite being the proposed model. The table caption indicates
green/blue for best/second-best, which aligns with PANDA being best for AP. CAMP is best for
Peptides-struct MAE. [Peptides-struct] Extracted only Peptides-struct MAE results as requested. CAMP
is identified as the proposed model ('Ours'). All baseline rows from the table were included.
Standard deviations were parsed from the 'value ± std' format.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*