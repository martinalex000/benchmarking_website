# Extraction: On Measuring Long-Range Interactions in Graph Neural Networks
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: HIGH

## Proposed Model: N/A
- Type: Other

## Baseline Models Identified

- **GCN**, 0.5M params (from: Kipf & Welling 2017)
- **GINE**, 0.5M params (from: Xu et al. 2019)
- **GatedGCN**, 0.5M params (from: Corso et al. 2020)
- **GPS**, 0.5M params (from: Dwivedi et al. 2022)
- **GCN+VN**, 0.5M params (from: this paper)
- **GT**, 0.5M params (from: this paper)

## Extraction Notes

[PascalVOC-SP] The provided text contains tables with dataset statistics (Table 1), sampling
hyperparameters (Table 2), and model hyperparameters (Table 3). However, none of the provided tables
contain the actual experimental performance results (e.g., F1 scores, Accuracy, MAE) for the
PascalVOC-SP dataset or any other dataset. Table 1 reports 'average validation range' which is a
dataset property/statistic, not a model performance metric. Therefore, no quantitative results could
be extracted. [Peptides-func] The paper focuses on analyzing the 'range' (SPD/Resistance distance)
of models during training rather than reporting final benchmark performance scores (like AP, MAE, or
Accuracy) for the Peptides-func dataset. The text explicitly states: 'We report only validation
results as range estimates were found to be highly consistent across splits.' The tables provided
(Table 1, Table 2, Table 3) contain dataset statistics, sampling hyperparameters, and model
hyperparameters, but no performance metrics (AP) for Peptides-func. Therefore, no quantitative
benchmark results could be extracted for the requested metric.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*