# Extraction: arXiv:2404.00477
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: DE-HNN
- Type: GNN

## Results

### Superblue — RMSE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GCN | 1.6910 | — | Yes | this paper | Table 1 |
| GATv2 | 1.7170 | — | Yes | this paper | Table 1 |
| AllSet | 1.8370 | — | Yes | this paper | Table 1 |
| HMPNN | 1.7850 | — | Yes | this paper | Table 1 |
| HNHN | 1.7540 | — | Yes | this paper | Table 1 |
| NetlistGNN | 1.7620 | — | Yes | this paper | Table 1 |
| base DE-HNN | 1.7310 | — | Yes | this paper | Table 1 |
| full DE-HNN | 1.6770 | — | No | this paper | Table 1 |

## Baseline Models Identified

- **GCN** (from: Kipf & Welling 2017)
- **GATv2** (from: Brody et al. 2022)
- **AllSet** (from: Tang et al. 2022)
- **HMPNN** (from: Mirhoseini et al. 2021)
- **HNHN** (from: Mirhoseini et al. 2021)
- **NetlistGNN** (from: Mirhoseini et al. 2021)
- **HyperConv** (from: Mirhoseini et al. 2021)

## Extraction Notes

[Superblue] Extracted RMSE results for the 'Superblue' dataset from Table 1 (Net-based wirelength
regression) and Table 2 (Net-based demand regression) under the 'Cross-Design' setting, which
corresponds to the standard evaluation on Superblue designs (1-17 train, 18 val, 19 test). Single-
design results were excluded as they are averaged across designs and not the primary benchmark
metric for the dataset as a whole. Table 3 (classification) was excluded as the primary metric
requested was RMSE. Table 4 contains per-design breakdowns which are redundant with the aggregated
Cross-Design results in Table 1/2 for the purpose of extracting the main benchmark score.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*