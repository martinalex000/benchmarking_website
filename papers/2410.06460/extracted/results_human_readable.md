# Extraction: arXiv:2410.06460
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: BI-GPS-T
- Type: GraphTransformer

## Results

### HLS — Ranking ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCN | 15.0000 | — | Yes | this paper | Table 1 |
| DiGCN | 12.0000 | — | Yes | this paper | Table 1 |
| MagNet | 7.0000 | — | Yes | zhang2021magnet | Table 1 |
| GCN | 14.0000 | — | Yes | this paper | Table 1 |
| DI-GCN | 13.5000 | — | Yes | this paper | Table 1 |
| BI-GCN | 11.0000 | — | Yes | this paper | Table 1 |
| GIN | 6.0000 | — | Yes | this paper | Table 1 |
| DI-GIN | 2.5000 | — | Yes | this paper | Table 1 |
| BI-GIN | 1.0000 | — | Yes | this paper | Table 1 |
| GAT | 8.5000 | — | Yes | this paper | Table 1 |
| DI-GAT | 10.0000 | — | Yes | this paper | Table 1 |
| BI-GAT | 9.0000 | — | Yes | this paper | Table 1 |
| GPS-T | 4.0000 | — | Yes | this paper | Table 1 |
| DI-GPS-T | 5.0000 | — | Yes | this paper | Table 1 |
| BI-GPS-T | 3.0000 | — | No | this paper | Table 1 |
| BI-GIN(E) | 9.0000 | — | Yes | this paper | Table 2 |
| BI-GIN(E)+NPE | 5.0000 | — | Yes | this paper | Table 2 |
| BI-GIN(E)+EPE | 5.0000 | — | Yes | this paper | Table 2 |
| BI-GPS-T (NPE) | 4.5000 | — | Yes | this paper | Table 2 |
| BI-GPS-T+EPE | 2.5000 | — | No | this paper | Table 2 |

### SR — Ranking ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCN | 10.0000 | — | Yes | this paper | Table 4 |
| DiGCN | 8.5000 | — | Yes | this paper | Table 4 |
| MagNet | 1.8000 | — | Yes | Zhang 2021 | Table 4 |
| GCN | 13.3000 | — | Yes | this paper | Table 4 |
| DI-GCN | 15.0000 | — | Yes | this paper | Table 4 |
| BI-GCN | 5.5000 | — | Yes | this paper | Table 4 |
| GIN | 10.0000 | — | Yes | this paper | Table 4 |
| DI-GIN | 6.5000 | — | Yes | this paper | Table 4 |
| BI-GIN | 2.8000 | — | No | this paper | Table 4 |
| GAT | 13.8000 | — | Yes | this paper | Table 4 |
| DI-GAT | 11.8000 | — | Yes | this paper | Table 4 |
| BI-GAT | 4.0000 | — | Yes | this paper | Table 4 |
| GPS-P | 5.5000 | — | Yes | this paper | Table 4 |
| DI-GPS-P | 6.5000 | — | Yes | this paper | Table 4 |
| BI-GPS-P | 7.8000 | — | Yes | this paper | Table 4 |
| BI-GIN(E) | 4.8000 | — | Yes | this paper | Table 5 |
| BI-GIN(E)+NPE | 3.0000 | — | Yes | this paper | Table 5 |
| BI-GIN(E)+EPE | 4.0000 | — | Yes | this paper | Table 5 |

### TIME — Ranking ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| DGCN | 15.0000 | — | Yes | this paper | Table 1 |
| DiGCN | 13.5000 | — | Yes | this paper | Table 1 |
| MagNet | 11.0000 | — | Yes | zhang2021magnet | Table 1 |
| GCN | 9.5000 | — | Yes | this paper | Table 1 |
| DI-GCN | 11.0000 | — | Yes | this paper | Table 1 |
| BI-GCN | 5.0000 | — | Yes | this paper | Table 1 |
| GIN | 1.0000 | — | Yes | this paper | Table 1 |
| DI-GIN | 3.0000 | — | Yes | this paper | Table 1 |
| BI-GIN | 2.0000 | — | No | this paper | Table 1 |
| GAT | 10.5000 | — | Yes | this paper | Table 1 |
| DI-GAT | 13.5000 | — | Yes | this paper | Table 1 |
| BI-GAT | 6.5000 | — | Yes | this paper | Table 1 |
| GPS-P | 6.5000 | — | Yes | this paper | Table 1 |
| DI-GPS-P | 4.0000 | — | Yes | this paper | Table 1 |
| BI-GPS-P | 8.0000 | — | Yes | this paper | Table 1 |
| BI-GIN(E) | 2.5000 | — | Yes | this paper | Table 2 |
| BI-GIN(E)+NPE | 5.5000 | — | Yes | this paper | Table 2 |
| BI-GIN(E)+EPE | 2.0000 | — | No | this paper | Table 2 |

## Baseline Models Identified

- **GCN**
- **DI-GCN**
- **BI-GCN**
- **GIN**
- **DI-GIN**
- **BI-GIN**
- **GAT**
- **DI-GAT**
- **BI-GAT**
- **GPS-T**
- **DI-GPS-T**
- **DGCN**
- **DiGCN**
- **MagNet** (from: zhang2021magnet)
- **BI-GIN(E)**
- **BI-GIN(E)+NPE**
- **BI-GIN(E)+EPE**
- **BI-GPS-T (NPE)**
- **BI-GPS-T+EPE**
- **Hierarchical GNN** (from: wu2022high)
- **GPS-P**
- **DI-GPS-P**
- **BI-GPS-P**
- **GAMORA** (from: wu2023gamora)
- **Timer-GNN** (from: guo2022timing)

## Extraction Notes

[HLS] Extracted Ranking values for HLS dataset from Table 1 and Table 2. Table 1 provides rankings
for the DSP task (ID), and Table 2 provides rankings for the DSP task (ID) for a different set of
models including EPE variants. Only the DSP task was used as the representative for the HLS dataset
ranking as per the focus on standard configuration. [AMP] failed: 1 validation error for
ExtractionOutput   Input should be a valid dictionary or instance of ExtractionOutput
[type=model_type, input_value=[{'name': 'GCN', 'params_...int': 'dong2023cktgnn'}], input_type=list]
For further information visit https://errors.pydantic.dev/2.13/v/model_type [SR] Extracted Ranking
values for SR dataset from Table 4 and Table 5. Table 4 contains both ID and OOD rankings for
'share' and 'root' tasks. Table 5 contains rankings for the same tasks for EPE/NPE variants. Note
that 'Ranking' is a relative metric where lower is better. [TIME] Extracted 'Ranking' values for the
'TIME' dataset from the ID columns of Table 1 and Table 2. Table 3 contains R2 for TIME, which was
skipped per the PRIMARY METRIC instruction. [CG] failed: 1 validation error for ExtractionOutput
Input should be a valid dictionary or instance of ExtractionOutput [type=model_type,
input_value=[{'name': 'DGCN', 'params...r_hint': 'zhang2021nn'}], input_type=list]     For further
information visit https://errors.pydantic.dev/2.13/v/model_type

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*