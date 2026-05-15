# Extraction: arXiv:2403.06687
**Model used**: `qwen3.6-35b-a3b`  **Date**: 2026-05-14  **Confidence**: LOW

## Proposed Model: HL-HGAT
- Type: GNN

## Baseline Models Identified

- **M1**
- **M2**
- **M3**
- **M4**

## Extraction Notes

[TSP] The paper mentions the TSP dataset in the text and Table 1 (parameters), but does not provide
any quantitative results (F1 scores, accuracy, etc.) for TSP in the provided text or tables. The
text only qualitatively states that 'M4 does not consistently outperform M3 in the TSP... datasets'
and refers to 'Fig. 1' for ablation studies on other datasets (CIFAR10, Peptide-func, etc.), but no
figure or table with TSP numerical results is included in the input. Therefore, no rows can be
extracted for TSP. [CIFAR10] The provided text and tables describe the architecture,
hyperparameters, and ablation study of the proposed model HL-HGAT. While the text mentions that
classification accuracy was evaluated on CIFAR10 and refers to figures (Fig. 1(B)) showing these
results, the actual numerical values (Accuracy, std) for CIFAR10 are not present in the provided
text or tables. Therefore, no quantitative results could be extracted. [Peptides-func] The provided
text contains only Table 1, which lists hyperparameter configurations (number of blocks, layers,
filters, etc.) for various datasets including 'Peptide-func'. It does not contain any performance
results (metrics like AP, Accuracy, etc.) for any model on any dataset. Therefore, no quantitative
results could be extracted. [ZINC] The provided text and tables mention the ZINC dataset in the
context of an ablation study and parameter configuration (Table 1). However, the text explicitly
states that 'M4 does not consistently outperform M3 in the TSP and ZINC datasets' and refers to
Figures for performance visualization ('Fig.  ef{fig:ablation_errbar}'). The actual numerical
results (MAE values) for ZINC are contained in these figures, which are not provided in the text or
table input. Therefore, no quantitative results for ZINC could be extracted. [OASIS-3] The provided
text and tables describe the architecture, hyperparameters, and ablation study of the HL-HGAT model.
While the text mentions that the model was evaluated on the OASIS-3 dataset for 'brain age'
prediction (which implies a regression task likely measured by MAE), the actual quantitative results
(MAE values, standard deviations, etc.) are NOT present in the provided text or tables. The text
references figures (Fig. 1(E)) for performance but does not include the figure data or a results
table containing the specific numerical values for OASIS-3. Therefore, no quantitative results could
be extracted. [ABCD] The paper mentions the ABCD dataset in the text and Figure captions, stating
that HL-HGAT (specifically M4) shows 'enhanced prediction performance' for general intelligence on
ABCD (Fig. 1F). However, the provided text and tables do not contain any numerical results (MAE
values, standard deviations, or specific scores) for the ABCD dataset. The only table provided
(Table 1) lists hyperparameters, not performance metrics. Therefore, no quantitative results could
be extracted.

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*