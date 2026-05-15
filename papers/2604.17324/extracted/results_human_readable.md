# Extraction: SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated Attention
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-11  **Confidence**: HIGH

## Proposed Model: SigGate-GT
- Type: GraphTransformer

## Results

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (tuned) | 0.6860 | 0.0050 | Yes | Tonshoff et al. | Table 1 |
| GatedGCN | 0.6765 | 0.0047 | Yes | Bresson et al. | Table 1 |
| GraphGPS | 0.6535 | 0.0041 | Yes | Rampásek et al. | Table 1 |
| Exphormer | 0.6527 | 0.0043 | Yes | Shirzad et al. | Table 1 |
| GRIT | 0.6988 | 0.0082 | Yes | Ma et al. | Table 1 |
| SigGate-GT | 0.6947 | 0.0037 | No | this paper | Table 1 |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN (tuned) | 0.2460 | 0.0007 | Yes | Tonshoff et al. 2024 | Table 1 |
| GatedGCN | 0.2477 | 0.0009 | Yes | Bresson et al. 2017 | Table 1 |
| GraphGPS | 0.2500 | 0.0012 | Yes | Rampásek et al. 2022 | Table 1 |
| Exphormer | 0.2481 | 0.0007 | Yes | Shirzad et al. 2023 | Table 1 |
| GRIT | 0.2460 | 0.0012 | Yes | Ma et al. 2023 | Table 1 |
| SigGate-GT | 0.2431 | 0.0012 | No | this paper | Table 1 |
| Baseline (no modification) | 0.2500 | 0.0012 | Yes | this paper | Table 2 |
| + DropEdge | 0.2488 | 0.0015 | Yes | Rong et al. 2020 | Table 2 |
| + PairNorm | 0.2491 | 0.0011 | Yes | Zhao et al. 2020 | Table 2 |
| + SigGate | 0.2431 | 0.0012 | Yes | this paper | Table 2 |
| + SigGate + DropEdge | 0.2428 | 0.0010 | Yes | this paper | Table 2 |

### ZINC — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 0.3670 | 0.0110 | Yes | this paper | Table 1 |
| GatedGCN | 0.2820 | 0.0150 | Yes | this paper | Table 1 |
| PNA | 0.1880 | 0.0040 | Yes | this paper | Table 1 |
| SAN | 0.1390 | 0.0060 | Yes | this paper | Table 1 |
| Graphormer | 0.1220 | 0.0060 | Yes | this paper | Table 1 |
| GraphGPS | 0.0700 | 0.0040 | Yes | this paper | Table 1 |
| Exphormer | 0.0660 | 0.0030 | Yes | this paper | Table 1 |
| GRIT | 0.0590 | 0.0020 | Yes | this paper | Table 1 |
| SigGate-GT | 0.0590 | 0.0020 | No | this paper | Table 1 |

### ogbg-molhiv — ROC-AUC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 76.0600 | 0.9700 | Yes | Kipf & Welling 2017 | Table 1 |
| PNA | 79.0500 | 1.3200 | Yes | Corso et al. 2020 | Table 1 |
| DeeperGCN | 78.5800 | 1.0000 | Yes | Li et al. 2020 | Table 1 |
| Graphormer | 80.5100 | 0.5300 | Yes | Ying et al. 2021 | Table 1 |
| GraphGPS | 78.8000 | 1.0100 | Yes | Rampásek et al. 2022 | Table 1 |
| Exphormer | 80.7500 | 0.9400 | Yes | Shirzad et al. 2023 | Table 1 |
| SigGate-GT | 82.4700 | 0.6300 | No | this paper | Table 1 |
| GraphGPS baseline | 78.8000 | — | Yes | Rampásek et al. 2022 | Table 2 |
| G3 | 77.9500 | — | Yes | this paper | Table 2 |
| G2 | 80.1200 | — | Yes | this paper | Table 2 |
| G1 | 82.4700 | — | No | this paper | Table 2 |
| Shared | 80.5800 | — | Yes | this paper | Table 2 |
| Per-head | 82.4700 | — | No | this paper | Table 2 |

### ogbg-molpcba — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 24.2400 | 0.3400 | Yes | Kipf 2017 | Table 1 |
| PNA | 28.3800 | 0.3500 | Yes | Corso 2020 | Table 1 |
| DeeperGCN | 27.8100 | 0.3800 | Yes | Li 2020 | Table 1 |
| GraphGPS | 29.0700 | 0.2800 | Yes | Rampásek 2022 | Table 1 |
| Exphormer | 29.2000 | 0.3000 | Yes | Shirzad 2023 | Table 1 |
| SigGate-GT | 29.8400 | 0.3100 | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf 2017)
- **GatedGCN** (from: Bresson 2017)
- **PNA** (from: Corso 2020)
- **SAN** (from: Kreuzer 2021)
- **Graphormer** (from: Ying 2021)
- **GraphGPS** (from: Rampásek 2022)
- **Exphormer** (from: Shirzad 2023)
- **GRIT** (from: Ma 2023)
- **DeeperGCN** (from: Li et al. 2020)
- **GCN (tuned)** (from: Tonshoff et al.)
- **Baseline (no modification)** (from: this paper)
- **+ DropEdge** (from: Rong et al. 2020)
- **+ PairNorm** (from: Zhao et al. 2020)
- **+ SigGate** (from: this paper)
- **+ SigGate + DropEdge** (from: this paper)

## Extraction Notes

[ZINC] Extracted only the main benchmark results from Table 1 for the ZINC dataset. Other tables
(ablation, over-smoothing, stability, activation) contain variations or subsets of results for the
same model/dataset but are not the primary benchmark comparison. The primary metric MAE was used.
All values are test set results. [ogbg-molhiv] Extracted all rows from Table 1 and Table 2
corresponding to 'molhiv'. Table 1 provides standard benchmark results with standard deviations.
Table 2 provides ablation results without standard deviations. The proposed model 'SigGate-GT'
corresponds to the 'G1' configuration with 'Per-head' sharing in the ablation study, both reporting
82.47. Baselines from Table 1 are included with their original citations. Table 2 baselines
(GraphGPS baseline, G3, G2, Shared) are treated as variants/baselines for the ablation. [ogbg-
molpcba] Extracted only the 'molpcba (AP)' column as requested. Graphormer has no result for molpcba
(marked as ---), so it is excluded from results. All other baselines and the proposed model have
valid values. [Peptides-func] Extracted only Peptides-func results as requested. The table caption
and text confirm the metric is AP (Average Precision) and higher is better. All standard
configurations were used. No external data usage was indicated for these baselines or the proposed
model. [Peptides-struct] Extracted all rows from Table 1 and Table 2 that report Peptides-struct
MAE. Table 1 lists standard baselines and the proposed SigGate-GT. Table 2 lists ablation variants
of GraphGPS. Note: The row '+ SigGate + DropEdge' in Table 2 has a lower MAE (0.2428) than the
proposed 'SigGate-GT' (0.2431) in Table 1, but since the prompt asks for ALL quantitative results
and '+ SigGate + DropEdge' is a distinct configuration/variant reported in the paper, it is
included. The primary proposed model 'SigGate-GT' is marked as is_proposed=true.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*