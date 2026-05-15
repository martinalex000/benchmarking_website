# Extraction: arXiv:2312.11730
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: GraphGPS with Edge Regularization
- Type: GNN

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| Baseline | 0.6435 | — | Yes | this paper | Figure: Regularization on Peptides-Func |
| 0.01 L1 | 0.6477 | — | No | this paper | Figure: Regularization on Peptides-Func |
| 0.05 L1 | 0.6468 | 0.0020 | No | this paper | Figure: Regularization on Peptides-Func |
| 0.01 CE | 0.6423 | — | No | this paper | Figure: Regularization on Peptides-Func |
| No-PE Baseline | 0.5866 | 0.0184 | Yes | this paper | Figure: Regularization on Peptides-Func |
| No-PE 0.1 L1 | 0.6192 | 0.0019 | No | this paper | Figure: Regularization on Peptides-Func |
| No-PE 0.5 L1 | 0.6096 | — | No | this paper | Figure: Regularization on Peptides-Func |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GraphGPS (w/ Positional Encoding, No Reg) | 0.2499 | 0.0003 | Yes | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.01 CE) | 0.2498 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.05 CE) | 0.2531 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.1 CE) | 0.2548 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.5 CE) | 0.2558 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE) | 0.2496 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.05 CE) | 0.2500 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.01 L1) | 0.2478 | 0.0024 | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.05 L1) | 0.2486 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.1 L1) | 0.2488 | — | No | this paper | Figure 1 |
| GraphGPS (w/ Positional Encoding, 0.5 L1) | 0.2491 | — | No | this paper | Figure 1 |
| Baseline (w/out Positional Encoding) | 0.2590 | 0.0010 | Yes | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 0.01 L1) | 0.2579 | — | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 0.05 L1) | 0.2580 | — | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 0.1 L1) | 0.2584 | — | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 0.2 L1) | 0.2577 | — | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 0.5 L1) | 0.2555 | 0.0015 | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 1.0 L1) | 0.2571 | — | No | this paper | Figure 2 |
| Baseline (w/out Positional Encoding, 2.0 L1) | 0.2570 | — | No | this paper | Figure 2 |

## Baseline Models Identified

- **GraphGPS** (from: Correia et al. 2021 (implied by context of GraphGPS))
- **Baseline (No PE)** (from: this paper)
- **Baseline**
- **No-PE Baseline**

## Extraction Notes

[Peptides-struct] Extracted results from Figure 1 and Figure 2 which explicitly plot MAE on
Peptides-Struct. Figure 1 shows results with Positional Encoding, Figure 2 shows results without.
The text mentions 'Peptides-Struct and PascalVOC-S are included in the appendix', but the figures
provided in the text contain the specific regularization ablation results for Peptides-Struct. The
table provided in the prompt refers to a 'PMT dataset' and is unrelated to Peptides-struct, so it
was ignored. Standard configuration implies using the default GraphGPS architecture with the
reported regularization variants. Values are normalized to [0,1] range for MAE (though MAE is not
strictly bounded by 1, the values are small decimals). Std deviations were parsed from the error bar
coordinates. [Peptides-func] Extracted results from the TikZ figure titled 'Regularization on
Peptides-Func'. The figure provides Average Precision (AP) values for various configurations
including the Baseline, No-PE Baseline, and proposed Edge Regularization variants (L1 and CE).
Standard deviations are explicitly provided for some points (e.g., 0.05 L1, No-PE Baseline, No-PE
0.1 L1) and inferred or missing for others. The PMT dataset table was ignored as it is not Peptides-
func. [PascalVOC-SP] The provided text contains only one table, which reports results on the 'PMT
dataset' using the 'MSE' metric. There are no results reported for the 'PascalVOC-SP' dataset.
Therefore, no rows match the FOCUS instruction.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*