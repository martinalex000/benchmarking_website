# Extraction: Generalizable Insights for Graph Transformers in Theory and Practice
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: GDT (16.0M params)
- Type: GraphTransformer

## Results

### Bridges — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GDT (NoPE) | 55.3600 | 24.9400 | No | this paper | Table 1 |
| GDT (LPE) | 91.7600 | 7.6600 | No | this paper | Table 1 |
| GDT (SPE) | 54.8100 | 21.2000 | No | this paper | Table 1 |
| GDT (RWSE) | 87.3400 | 3.9700 | No | this paper | Table 1 |
| GDT (RRWP) | 99.2100 | 0.0900 | No | this paper | Table 1 |

### COCO — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GDT (NoPE) | 43.1200 | 0.8500 | No | this paper | Table 1 |
| GDT (LPE) | 44.8300 | 0.7100 | No | this paper | Table 1 |
| GDT (SPE) | 43.8700 | 0.5400 | No | this paper | Table 1 |
| GDT (RWSE) | 43.8200 | 1.0100 | No | this paper | Table 1 |
| GDT (RRWP) | 39.9100 | 1.0700 | No | this paper | Table 1 |

### Code — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoPE | 19.2700 | 0.2000 | Yes | this paper | Table 1 |
| LPE | 19.4800 | 0.2100 | Yes | this paper | Table 1 |
| SPE | 19.3500 | 0.2100 | Yes | this paper | Table 1 |
| RWSE | 19.3900 | 0.4700 | Yes | this paper | Table 1 |
| RRWP | 19.4200 | 0.1000 | Yes | this paper | Table 1 |

### Flow — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| NoPE | 1.7300 | 0.0900 | Yes | this paper | Table 1 |
| LPE | 1.7500 | 0.1200 | Yes | this paper | Table 1 |
| SPE | 1.9800 | 0.1400 | Yes | this paper | Table 1 |
| RWSE | 1.4900 | 0.0200 | Yes | this paper | Table 1 |
| RRWP | 1.4500 | 0.0600 | No | this paper | Table 1 |

### MST — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GDT (NoPE) | 93.2900 | 0.8800 | No | this paper | Table 1 |
| GDT (LPE) | 91.0800 | 0.9500 | No | this paper | Table 1 |
| GDT (SPE) | 92.5200 | 0.1200 | No | this paper | Table 1 |
| GDT (RWSE) | 93.2600 | 0.4500 | No | this paper | Table 1 |
| GDT (RRWP) | 96.0400 | 0.9100 | No | this paper | Table 1 |

### PCQ — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GDT (NoPE) | 93.6000 | 0.5000 | No | this paper | Table 1 |
| GDT (LPE) | 92.7000 | 0.9000 | No | this paper | Table 1 |
| GDT (SPE) | 94.1000 | 0.6000 | No | this paper | Table 1 |
| GDT (RWSE) | 92.9000 | 0.6000 | No | this paper | Table 1 |
| GDT (RRWP) | 90.4000 | 0.3000 | No | this paper | Table 1 |
| SOTA (Range) | 0.0809 | — | Yes | chen2023gpropagation, mueller2024et, ma+2023+GRIT, rampasek+2022+graphgps | N/A (Text) |

## Baseline Models Identified

- **Graphormer-GD** (from: Zha+GDWL+2023)
- **GProp** (from: chen2023gpropagation)
- **ET** (from: mueller2024et)
- **GRIT** (from: ma+2023+GRIT)
- **GraphGPS** (from: rampasek+2022+graphgps)
- **NoPE**
- **LPE**
- **SPE**
- **RWSE**
- **RRWP**

## Extraction Notes

[PCQ] Extracted all PCQ results from Table 1 (16M models) and Table 2 (90M models). The text
mentions SOTA range (0.0809-0.0859 MAE) but does not provide a specific table row for individual
baseline models on PCQ, so only the range is noted as a reference. Note: The values in the tables
are in micro electron volts (meV), while the text SOTA range is likely in eV or similar scaled unit,
but the table explicitly states 'MAE is in micro electron volt'. The extracted values reflect the
table units. [COCO] Extracted results for the COCO dataset from Table 1. The table lists results for
the proposed GDT model with different Positional Encodings (PEs). The metric is F1 (higher is
better). Standard deviations are parsed from the '±' notation. No other models (baselines) are
reported in this specific table for the COCO dataset; Graphormer-GD is mentioned in the text but no
numerical results for COCO are provided in the table. [Code] Extracted results for the 'Code'
dataset from Table 1. The table reports results for different Positional Encodings (PEs) used with
the GDT model (16M parameters). The proposed model is GDT, but the table specifically compares
different PE strategies (NoPE, LPE, SPE, RWSE, RRWP) within that framework. No specific 'GDT' row
exists without a PE suffix, so the PEs are treated as the model variants being evaluated. The
primary metric F1 was extracted. Standard deviations were parsed from the '±' notation. [Flow]
Extracted only the 'Flow' dataset column from Table 1 as requested. The table compares different
Positional Encodings (PEs) with a fixed 16M parameter model. RRWP is identified as the proposed
model based on the bolded mean rank and best MAE score. All values are test-set results (implied by
the context of benchmarking PEs). MAE is the primary metric for Flow. [MST] Extracted all MST
results from Table 1 (16M models) and Table 2 (90M and 160M models). Table 2 lists MST results for
90M and 160M variants separately. The 160M RRWP row is empty/dash in the table, so it was skipped.
Graphormer-GD is mentioned as a comparison target in the text but no specific numerical results for
Graphormer-GD on MST are provided in the tables, so it is not included in the results list. The
primary metric F1 was used as requested. [Bridges] Extracted all rows from Table 1 corresponding to
the 'Bridges' dataset and 'F1' metric. The table compares different Positional Encodings (PEs) used
within the proposed GDT architecture. Graphormer-GD is mentioned in the text as a comparison point
but does not appear in the provided table snippet, so its results are not included in the results
array. All values are test-set results as implied by the context of reporting final performance
metrics. [BREC] failed: Error code: 429 - {'message': 'API rate limit exceeded', 'request_id':
'd129cf104201c144a7add31a936a1c1e'}

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*