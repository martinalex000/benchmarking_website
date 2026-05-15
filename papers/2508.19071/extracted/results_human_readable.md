# Extraction: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: TRIGON
- Type: GNN

## Results

### Chameleon — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 65.3500 | 0.5400 | Yes | this paper | Table 2 |
| DIGL | 54.8200 | 0.4800 | Yes | this paper | Table 2 |
| FA | 26.3400 | 0.6100 | Yes | this paper | Table 2 |
| SRDF | 63.0800 | 0.3700 | Yes | this paper | Table 2 |
| FOSR | 67.9800 | 0.4000 | Yes | this paper | Table 2 |
| BORF | 65.3500 | 0.5100 | Yes | this paper | Table 2 |
| GTR | 68.0300 | 0.6100 | Yes | this paper | Table 2 |
| JDR | 65.8500 | 0.4900 | Yes | this paper | Table 2 |
| DR | 74.2800 | 0.4800 | Yes | this paper | Table 2 |
| TRIGON | 75.5200 | 0.5000 | No | this paper | Table 2 |
| Base (GAT) | 65.0700 | 0.4100 | Yes | this paper | Table 3 |

### Cora — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 87.7300 | 0.2500 | Yes | this paper | Table 2 |
| DIGL | 88.3100 | 0.2900 | Yes | this paper | Table 2 |
| FA | 29.8600 | 0.2800 | Yes | this paper | Table 2 |
| SRDF | 87.7300 | 0.3100 | Yes | this paper | Table 2 |
| FOSR | 87.9400 | 0.2600 | Yes | this paper | Table 2 |
| BORF | 87.7200 | 0.2700 | Yes | this paper | Table 2 |
| GTR | 87.8600 | 0.2800 | Yes | this paper | Table 2 |
| JDR | 87.5400 | 0.2500 | Yes | this paper | Table 2 |
| DR | 91.3900 | 0.2400 | Yes | this paper | Table 2 |
| TRIGON | 91.7100 | 0.2900 | No | this paper | Table 2 |
| Base (GAT) | 87.6500 | 0.2400 | Yes | this paper | Table 3 |

### Cornell — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 44.7800 | 1.4500 | Yes | this paper | Table 2 (HeteroGCN) |
| DIGL | 44.4600 | 1.3700 | Yes | this paper | Table 2 (HeteroGCN) |
| FA | 45.3300 | 1.5500 | Yes | this paper | Table 2 (HeteroGCN) |
| SRDF | 47.7300 | 1.5100 | Yes | this paper | Table 2 (HeteroGCN) |
| FOSR | 45.1100 | 1.4700 | Yes | this paper | Table 2 (HeteroGCN) |
| BORF | 46.8100 | 1.5600 | Yes | this paper | Table 2 (HeteroGCN) |
| GTR | 47.5700 | 1.5200 | Yes | this paper | Table 2 (HeteroGCN) |
| JDR | 57.3100 | 1.6000 | Yes | this paper | Table 2 (HeteroGCN) |
| DR | 67.2200 | 1.4800 | Yes | this paper | Table 2 (HeteroGCN) |
| TRIGON | 69.1100 | 1.5300 | No | this paper | Table 2 (HeteroGCN) |
| Base (GAT) | 46.0500 | 1.4900 | Yes | this paper | Table 3 (HeteroGAT) |

### Squirrel — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 51.3000 | 0.3800 | Yes | this paper | Table 2 |
| DIGL | 40.5300 | 0.2900 | Yes | this paper | Table 2 |
| FA | 22.8800 | 0.4200 | Yes | this paper | Table 2 |
| SRDF | 49.1100 | 0.2800 | Yes | this paper | Table 2 |
| FOSR | 52.6300 | 0.3000 | Yes | this paper | Table 2 |
| GTR | 53.3200 | 0.4400 | Yes | this paper | Table 2 |
| JDR | 53.7800 | 0.4600 | Yes | this paper | Table 2 |
| DR | 65.2500 | 0.2600 | Yes | this paper | Table 2 |
| TRIGON | 66.4800 | 0.3500 | No | this paper | Table 2 |
| Base (GAT) | 50.8700 | 0.5600 | Yes | this paper | Table 3 |

### Texas — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 56.1900 | 1.6100 | Yes | this paper | Table 2 |
| DIGL | 45.9500 | 1.5800 | Yes | this paper | Table 2 |
| FA | 55.9300 | 1.7600 | Yes | this paper | Table 2 |
| SRDF | 59.7900 | 1.7100 | Yes | this paper | Table 2 |
| FOSR | 61.3500 | 1.2500 | Yes | this paper | Table 2 |
| BORF | 56.3000 | 1.6100 | Yes | this paper | Table 2 |
| GTR | 57.1800 | 1.6400 | Yes | this paper | Table 2 |
| JDR | 69.5600 | 1.7100 | Yes | this paper | Table 2 |
| DR | 70.4600 | 1.6100 | Yes | this paper | Table 2 |
| TRIGON | 75.7400 | 1.6100 | No | this paper | Table 2 |
| Base (GAT) | 56.8400 | 1.6100 | Yes | this paper | Table 3 |

### Wisconsin — Accuracy ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Base (GCN) | 55.1200 | 1.5100 | Yes | this paper | Table 2 |
| DIGL | 46.9000 | 1.2800 | Yes | this paper | Table 2 |
| FA | 46.7700 | 1.4800 | Yes | this paper | Table 2 |
| SRDF | 58.4900 | 1.2300 | Yes | this paper | Table 2 |
| FOSR | 55.6000 | 1.2500 | Yes | this paper | Table 2 |
| BORF | 55.3700 | 1.4700 | Yes | this paper | Table 2 |
| GTR | 57.2200 | 1.5000 | Yes | this paper | Table 2 |
| JDR | 67.8700 | 1.6200 | Yes | this paper | Table 2 |
| DR | 70.9800 | 1.5000 | Yes | this paper | Table 2 |
| TRIGON | 73.9000 | 1.6100 | No | this paper | Table 2 |
| Base (GAT) | 53.5800 | 1.3900 | Yes | this paper | Table 3 |

## Baseline Models Identified

- **Base (GCN)** (from: GCN (Kipf & Welling))
- **DIGL**
- **FA**
- **SRDF**
- **FOSR**
- **BORF**
- **GTR**
- **JDR**
- **DR** (from: Attali et al. 2024)
- **Base (GAT)** (from: GAT (Veličković et al.))

## Extraction Notes

[Cora] Extracted results for Cora from Table 2 (GCN backbone) and Table 3 (GAT backbone). Both
tables report Accuracy. The proposed model TRIGON achieves the highest accuracy in both
configurations. All other baselines are included as requested. [Chameleon] Extracted results for
Chameleon from Table 2 (GCN backbone) and Table 3 (GAT backbone). Figure 1 also contains Chameleon
data points for specific layer depths, but these are not standard benchmark results with statistical
significance (std dev) and are excluded in favor of the comprehensive tables. All values are test
accuracy. [Squirrel] Extracted results for 'Squirrel' dataset from Table 2 (GCN backbone) and Table
3 (GAT backbone). BORF row for Squirrel in Table 2 and Table 3 contains '>=24h' or '>= 24h'
indicating timeout/computation failure, so it was excluded from results as no accuracy value is
reported. All other rows contain valid Accuracy values with standard deviations. [Cornell] Extracted
all rows for the 'Cornell' dataset from Table 2 (GCN backbone) and Table 3 (GAT backbone). The
metric is Accuracy. Standard deviations were parsed from the 'value ± std' format. All models use
the standard configuration as described in the Experimental Setup section. [Texas] Extracted all
Texas rows from Table 2 (GCN backbone) and Table 3 (GAT backbone). Both tables report Accuracy.
Standard configuration used as per paper description (2 layers, dropout 0.5, lr 0.005, hidden dim
32). No other datasets included. [Wisconsin] Extracted results for 'Wisconsin' (labeled as 'Wisc.'
in tables) from Table 2 (GCN backbone) and Table 3 (GAT backbone). All values are test accuracies
with standard deviations. No other datasets were included as per instructions. [Pokec] The dataset
'Pokec' is not present in the provided tables. The tables only contain results for Texas, Cornell,
Wisconsin, Chameleon, Actor, Squirrel, Roman-Empire, Cora, Citeseer, and Pubmed. Therefore, no
results for 'Pokec' could be extracted. [Roman-empire] failed: 2 validation errors for
ExtractionOutput results.2.value   Input should be a valid number [type=float_type,
input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type results.12.value   Input should be a valid number
[type=float_type, input_value=None, input_type=NoneType]     For further information visit
https://errors.pydantic.dev/2.13/v/float_type [Amazon-ratings] The dataset 'Amazon-ratings' is not
present in the provided tables. The tables only contain results for Cham., Squir., Actor, Texas,
Wisc., Cornell, R-Emp., Cora, Citeseer, and Pubmed. Therefore, no results were extracted.
[Minesweeper] The dataset 'Minesweeper' is not present in the provided tables. The tables contain
results for datasets: Texas, Cornell, Wisconsin, Chameleon, Actor, Squirrel, Roman-Empire, Cora,
Citeseer, and Pubmed. No results for 'Minesweeper' were extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*