# Extraction: Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: GRIT
- Type: GraphTransformer

## Results

### ECHO-Charge — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| A-DGN | 6.5430 | 0.1460 | Yes | this paper | Table 1 |
| DRew | 9.0860 | 0.4730 | Yes | this paper | Table 1 |
| GCN | 8.4210 | 0.5120 | Yes | this paper | Table 1 |
| GCNII | 8.8290 | 0.0210 | Yes | this paper | Table 1 |
| GIN | 10.7840 | 0.0590 | Yes | this paper | Table 1 |
| GINE | 7.1760 | 0.3710 | Yes | this paper | Table 1 |
| GPS | 6.1820 | 0.2190 | Yes | this paper | Table 1 |
| GRIT | 7.1340 | 6.0900 | Yes | this paper | Table 1 |
| GraphCON | 19.6290 | 0.1950 | Yes | this paper | Table 1 |
| PH-DGN | 7.9150 | 0.2690 | Yes | this paper | Table 1 |
| SWAN | 6.1090 | 0.1030 | Yes | this paper | Table 1 |

### ECHO-Energy — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| A-DGN | 12.4860 | 1.6210 | Yes | this paper | Table 1 |
| DRew | 11.3250 | 2.3940 | Yes | this paper | Table 1 |
| GCN | 28.1120 | 1.2390 | Yes | this paper | Table 1 |
| GCNII | 13.2350 | 2.6300 | Yes | this paper | Table 1 |
| GIN | 47.8510 | 10.1540 | Yes | this paper | Table 1 |
| GINE | 23.5580 | 7.5680 | Yes | this paper | Table 1 |
| GPS | 5.2570 | 0.8420 | Yes | this paper | Table 1 |
| GRIT | 25.5080 | 2.5070 | Yes | this paper | Table 1 |
| GraphCON | 14.2950 | 0.8070 | Yes | this paper | Table 1 |
| PH-DGN | 16.0800 | 1.1230 | Yes | this paper | Table 1 |
| SWAN | 12.6290 | 1.1570 | Yes | this paper | Table 1 |

### ECHO-Synth — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| A-DGN | 1.1510 | 0.0380 | Yes | this paper | Table 1 |
| DRew | 1.2430 | 0.0470 | Yes | this paper | Table 1 |
| GraphCON | 2.9690 | 0.1890 | Yes | this paper | Table 1 |
| GCN | 3.8320 | 0.2620 | Yes | this paper | Table 1 |
| GCNII | 2.0050 | 0.0930 | Yes | this paper | Table 1 |
| GIN | 1.6300 | 0.1610 | Yes | this paper | Table 1 |
| GPS | 2.1600 | 0.0980 | Yes | this paper | Table 1 |
| GRIT | 1.0140 | 0.0460 | No | this paper | Table 1 |
| PH-DGN | 1.6270 | 0.3980 | Yes | this paper | Table 1 |
| SWAN | 1.1210 | 0.0700 | Yes | this paper | Table 1 |

## Baseline Models Identified

- **A-DGN**
- **DRew**
- **GraphCON**
- **GCN** (from: Kipf & Welling 2017)
- **GCNII** (from: Chen et al. 2020)
- **GIN** (from: Xu et al. 2019)
- **GPS** (from: Beaini et al. 2021)
- **PH-DGN**
- **SWAN**
- **GINE** (from: gine)
- **GRIT** (from: grit)

## Extraction Notes

[ECHO-Synth] Extracted all MAE results for the ECHO-Synth dataset from Table 1. The table contains
three sub-tasks (diam, ecc, sssp) under the ECHO-Synth umbrella. All models and their corresponding
MAE values with standard deviations were parsed. The proposed model is identified as GRIT based on
the text highlighting its superior performance and bolded best values in the table. [ECHO-Charge]
Extracted MAE results for ECHO-Charge from Table 1 (labeled as tab:test_results in text, but caption
matches). The table reports values scaled by 10^-3. The values extracted are the raw numbers from
the table (e.g., 6.543). The paper does not report a specific 'proposed model' with results in this
table; ECHO is the benchmark name. All baselines are included. Note: GRIT has a very high std
(6.090) which seems anomalous but is extracted as written. [ECHO-Energy] Extracted MAE results from
Table 1 (labeled as tab:test_results in text) for the ECHO-Energy dataset. The values are raw MAE
scores. Note: Table 2 (tab:test-metrics-energy-ext) reports Test MAE scaled by 10^-2 (e.g., GPS
0.053), which corresponds to 5.257 in the main table. The main table values are preferred as they
represent the standard benchmark scale without explicit scaling factors in the metric name column
header for the primary comparison. All baselines are included. The proposed model 'ECHO' is the
benchmark suite itself, not a specific model architecture, so no specific model row is marked as
proposed.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*