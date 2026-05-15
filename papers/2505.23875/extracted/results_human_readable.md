# Extraction: arXiv:2505.23875
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-12  **Confidence**: HIGH

## Proposed Model: PNA
- Type: GNN

## Results

### Dobbo — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.1800 | 0.1200 | Yes | this paper | Table 1 |
| Code2Vec | 0.2100 | 0.0200 | Yes | this paper | Table 1 |
| GCN | 0.1400 | 0.0200 | Yes | this paper | Table 1 |
| Cheb | 0.1300 | 0.0000 | Yes | this paper | Table 1 |
| GIN | 0.1400 | 0.0100 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1200 | 0.0100 | Yes | this paper | Table 1 |
| PNA | 0.1000 | 0.0100 | No | this paper | Table 1 |
| HeteroSage | 4.0500 | 5.6000 | Yes | this paper | Table 1 |
| HeteroGAT | 0.1900 | 0.0900 | Yes | this paper | Table 1 |

### H2 — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.2100 | 0.1200 | Yes | this paper | Table 1 |
| Code2Vec | 0.1700 | 0.0200 | Yes | this paper | Table 1 |
| GCN | 0.1800 | 0.0100 | Yes | this paper | Table 1 |
| Cheb | 0.1800 | 0.0100 | Yes | this paper | Table 1 |
| GIN | 0.2000 | 0.0100 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1900 | 0.0100 | Yes | this paper | Table 1 |
| PNA | 0.1700 | 0.0100 | No | this paper | Table 1 |
| HeteroSage | 4.3500 | 3.5100 | Yes | this paper | Table 1 |
| HeteroGAT | 1.0900 | 0.5400 | Yes | this paper | Table 1 |

### Hadoop — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.1400 | 0.1100 | Yes | this paper | Table 1 |
| Code2Vec | 0.1400 | 0.0100 | Yes | this paper | Table 1 |
| GCN | 0.1200 | 0.0000 | Yes | this paper | Table 1 |
| Cheb | 0.1100 | 0.0000 | Yes | this paper | Table 1 |
| GIN | 0.1200 | 0.0100 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1300 | 0.0000 | Yes | this paper | Table 1 |
| PNA | 0.0900 | 0.0100 | No | this paper | Table 1 |
| HeteroSage | 0.2700 | 0.1100 | Yes | this paper | Table 1 |
| HeteroGAT | 0.1400 | 0.0200 | Yes | this paper | Table 1 |

### OssBuilds — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.1500 | 0.0800 | Yes | this paper | Table 1 |
| Code2Vec | 0.1500 | 0.0100 | Yes | this paper | Table 1 |
| GCN | 0.1400 | 0.0100 | Yes | this paper | Table 1 |
| Cheb | 0.1500 | 0.0100 | Yes | this paper | Table 1 |
| GIN | 0.1400 | 0.0100 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1400 | 0.0100 | Yes | this paper | Table 1 |
| PNA | 0.1100 | 0.0000 | No | this paper | Table 1 |
| HeteroSage | 0.5800 | 0.3100 | Yes | this paper | Table 1 |
| HeteroGAT | 0.1800 | 0.0200 | Yes | this paper | Table 1 |

### RDF4J — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.1200 | 0.1000 | Yes | this paper | Table 1 |
| Code2Vec | 0.1700 | 0.0100 | Yes | this paper | Table 1 |
| GCN | 0.1300 | 0.0000 | Yes | this paper | Table 1 |
| Cheb | 0.1200 | 0.0100 | Yes | this paper | Table 1 |
| GIN | 0.1200 | 0.0000 | Yes | this paper | Table 1 |
| GraphSAGE | 0.1300 | 0.0100 | Yes | this paper | Table 1 |
| PNA | 0.0900 | 0.0100 | No | this paper | Table 1 |
| HeteroSage | 0.2000 | 0.0500 | Yes | this paper | Table 1 |
| HeteroGAT | 0.1500 | 0.0100 | Yes | this paper | Table 1 |

### SystemDS — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| CodeBERT | 0.1700 | 0.1300 | Yes | this paper | Table 1 |
| Code2Vec | 0.1900 | 0.0200 | Yes | this paper | Table 1 |
| GCN | 0.0700 | 0.0200 | Yes | this paper | Table 1 |
| Cheb | 0.0800 | 0.0400 | Yes | this paper | Table 1 |
| GIN | 0.0800 | 0.0500 | Yes | this paper | Table 1 |
| GraphSAGE | 0.0700 | 0.0300 | Yes | this paper | Table 1 |
| PNA | 0.0600 | 0.0000 | No | this paper | Table 1 |
| HeteroSage | 6.2200 | 5.4500 | Yes | this paper | Table 1 |
| HeteroGAT | 0.3100 | 0.1100 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **CodeBERT**
- **Code2Vec**
- **GCN**
- **Cheb**
- **GIN**
- **GraphSAGE**
- **HeteroSage**
- **HeteroGAT**

## Extraction Notes

[Hadoop] Extracted only test MAE for Hadoop as requested. PNA is identified as the proposed model
based on the text stating it achieves the lowest MAE and is highlighted in the table. [RDF4J]
Extracted only test MAE for RDF4J as requested. Validation tables and RMSE/MAPE tables were ignored.
[SystemDS] Extracted only test MAE for SystemDS from Table 1. Validation tables and RMSE/MAPE tables
were ignored per instructions. [H2] Extracted only test MAE for dataset H2 as requested. Validation
results and RMSE/MAPE metrics were skipped. [Dobbo] Extracted only test MAE for the 'Dobbo' dataset
as requested. Note that 'Dubbo' in RMSE/MAPE tables is treated as the same dataset 'Dobbo' from the
MAE table. [OssBuilds] Extracted only Test MAE for OssBuilds from Table 1. Skipped Table 2
(Validation), Table 3 (RMSE), and Table 4 (MAPE) as per instructions. Skipped Table 1's ablation
results (Table 2 in text) as they represent a specific configuration (ASTs only) rather than the
standard/default configuration.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*