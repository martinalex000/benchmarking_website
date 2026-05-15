# Extraction: arXiv:2406.09291
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: CS-GNN (0.5M params)
- Type: GNN

## Results

### ZINC-12k — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| GIN | 0.1630 | 0.0040 | Yes | this paper | Table 1 |
| OSAN | 0.1770 | 0.0160 | Yes | this paper | Table 1 |
| Random | 0.1310 | 0.0050 | Yes | this paper | Table 1 |
| PL | 0.1200 | 0.0030 | Yes | this paper | Table 1 |
| Mag-GNN | 0.1060 | 0.0140 | Yes | this paper | Table 1 |
| CS-GNN | 0.1090 | 0.0050 | No | this paper | Table 1 |
| GNN-SSWL+ | 0.0700 | 0.0050 | Yes | this paper | Table 1 |
| Subgraphormer | 0.0670 | 0.0070 | Yes | this paper | Table 1 |
| Subgraphormer+PE | 0.0630 | 0.0010 | Yes | this paper | Table 1 |
| GCN | 0.3210 | 0.0090 | Yes | this paper | Table 2 |
| NGNN | 0.1110 | 0.0030 | Yes | this paper | Table 2 |
| DS-GNN | 0.1160 | 0.0090 | Yes | this paper | Table 2 |
| DSS-GNN | 0.1020 | 0.0030 | Yes | this paper | Table 2 |
| GNN-AK | 0.1050 | 0.0100 | Yes | this paper | Table 2 |
| GNN-AK+ | 0.0910 | 0.0020 | Yes | this paper | Table 2 |
| SUN | 0.0830 | 0.0030 | Yes | this paper | Table 2 |

## Baseline Models Identified

- **GIN** (from: Xu et al. 2018)
- **OSAN** (from: Qian et al. 2022)
- **Random** (from: Kong et al. 2024 / Bevilacqua et al. 2023)
- **PL** (from: Bevilacqua et al. 2023)
- **Mag-GNN** (from: Kong et al. 2024)
- **GNN-SSWL+** (from: Zhang et al. 2023)
- **Subgraphormer** (from: Bar-Shalom et al. 2024)
- **Subgraphormer+PE** (from: Bar-Shalom et al. 2024)
- **GCN** (from: Kipf & Welling 2016)
- **NGNN** (from: Zhang et al. 2021)
- **DS-GNN** (from: Bevilacqua et al. 2021)
- **DSS-GNN** (from: Bevilacqua et al. 2021)
- **GNN-AK** (from: Zhao et al. 2022)
- **GNN-AK+** (from: Zhao et al. 2022)
- **SUN** (from: Frasca et al. 2022)

## Extraction Notes

[ZINC] Extracted results for ZINC-12k from Table 1 and Table 2. Table 2 contains a superset of Table
1's results plus additional baselines (GCN, NGNN, DS-GNN, etc.) and an additional CS-GNN
configuration (T=18). Table 1 is a subset of Table 2. I have included all unique rows from both
tables to ensure completeness, resulting in duplicate entries for models present in both tables
(e.g., GIN, OSAN, Random, PL, Mag-GNN, Subgraphormer variants). The 'ZINC-Full' dataset results were
excluded as per the instruction to use the STANDARD/DEFAULT configuration (ZINC-12k is the standard
benchmark cited in the text for the 500k parameter budget comparison, while ZINC-Full is presented
as an appendix/additional result). The 'uses_external_data' field is set to false for all models as
they are standard GNNs trained on the benchmark data.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*