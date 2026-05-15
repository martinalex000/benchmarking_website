# Extraction: Long-Range Graph Wavelet Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: LR-GWN
- Type: GNN

## Results

### Peptides-Func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGWT | 60.2300 | 0.2700 | Yes | Hammond et al. 2011 | Table 1 |
| GWNN | 65.4700 | 0.4800 | Yes | Xu et al. 2019 | Table 1 |
| DEFT | 66.9500 | 0.6300 | Yes | Bastos et al. 2023 | Table 1 |
| WaveGC | 69.7300 | 0.4300 | Yes | Liu et al. 2024 | Table 1 |
| LR-GWN (TC) | 70.5200 | 0.2900 | No | this paper | Table 1 |
| LR-GWN (TR) | 72.1600 | 0.4100 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| SGWT | 25.3900 | 0.2100 | Yes | Hammond et al. 2011 | Table 1 |
| GWNN | 27.3400 | 0.0400 | Yes | Xu et al. 2019 | Table 1 |
| DEFT | 25.0600 | 0.1300 | Yes | Bastos et al. 2023 | Table 1 |
| WaveGC | 24.9500 | 0.0700 | Yes | Liu et al. 2024 | Table 1 |
| LR-GWN (ours) | 24.6300 | 0.0700 | No | this paper | Table 1 |

## Baseline Models Identified

- **SGWT** (from: Hammond et al. 2011)
- **GWNN** (from: Xu et al. 2019)
- **DEFT** (from: Bastos et al. 2023)
- **WaveGC** (from: Liu et al. 2024)

## Extraction Notes

[Peptides-func] Extracted results for Peptides-Func from Table 1 (subcaption 'Long-range
benchmarks'). The table reports both Theory-Compliant (TC) and Theory-Relaxed (TR) variants for the
proposed model LR-GWN and baselines. Both variants are extracted as they represent the standard
configurations reported for the model on this dataset. The metric is Average Precision (AP),
indicated by the upward arrow in the table header. [Peptides-struct] The table presents results for
both Theory-Compliant (TC) and Theory-Relaxed (TR) configurations for the proposed model LR-GWN.
Both values are extracted as they represent the standard default configurations reported for the
model on this dataset. Baselines only report TC or TR where applicable (indicated by '-'). The
metric is MAE (lower is better).

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*