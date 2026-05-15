# Extraction: arXiv:2501.17901
**Model used**: `MiniMaxAI/MiniMax-M2.5`  **Date**: 2026-05-13  **Confidence**: HIGH

## Proposed Model: LightGBM
- Type: Other

## Results

### ADAPTABLE — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.8170 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.7940 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.6130 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.5590 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.7390 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.8200 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.8060 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.8080 | — | Yes | this paper | Table results_bert_benchmark |

### AMPBenchmark — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AmPEP | 0.6169 | 0.0693 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| iAMP-2L | 0.6260 | 0.0951 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| SVM-LZ | 0.7971 | 0.0243 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| CS-AMPPred | 0.8669 | 0.0436 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| AMAP | 0.8987 | 0.0418 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| Deep-AmPEP30 | 0.9098 | 0.0561 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| AmPEPpy | 0.9535 | 0.0299 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| AmpGram | 0.9556 | 0.0254 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| MACREL | 0.9629 | 0.0243 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| MLAMP | 0.9668 | 0.0235 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| ampir | 0.9671 | 0.0208 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| AMPScannerV2 | 0.9679 | 0.0208 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| TT | 0.9719 | 0.0189 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| RDKit | 0.9725 | 0.0184 | Yes | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |
| ECFP | 0.9737 | 0.0174 | No | this paper | Table ef{table_results_ampbenchmark_sidorczuk} |

### APD — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.7830 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.9010 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.7410 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.7170 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.8960 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.9300 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.9430 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.9300 | — | Yes | this paper | Table results_bert_benchmark |

### AutoPeptideML — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| ProtBERT | 0.7590 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ESM2-150M | 0.7770 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| Prost-T5 | 0.7710 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ESM2-8M | 0.7750 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ESM2-35M | 0.7800 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ESM1b-650M | 0.7890 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ESM2-650M | 0.7970 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| Prot-T5-XL | 0.7970 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| RDKit | 0.7690 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| TT | 0.7710 | — | Yes | this paper | Table ef{table_results_autopeptideml} |
| ECFP | 0.7810 | — | No | this paper | Table ef{table_results_autopeptideml} |

### Average F1 — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.7530 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.7510 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.6410 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.6380 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.7030 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.8720 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.8780 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.8760 | — | Yes | this paper | Table results_bert_benchmark |

### CAMP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.8230 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.8060 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.7280 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.6450 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.8360 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.8840 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.8880 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.8820 | — | Yes | this paper | Table results_bert_benchmark |

### DRAMP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.6400 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.5880 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.3920 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.4760 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.6480 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.7640 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.7690 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.7630 | — | Yes | this paper | Table results_bert_benchmark |

### PeptideReactor — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| FP encoding | 0.8290 | — | No | this paper | Table ef{table_results_peptidereactor} |
| ECFP | 0.8170 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| TT | 0.8060 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| RDKit | 0.8060 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| cksaap | 0.8240 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| dist_f | 0.8220 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| psekraac | 0.8180 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| ngram_ | 0.8160 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| dde | 0.8130 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| qsar | 0.7280 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| delaun | 0.6950 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| distan | 0.6130 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| electr | 0.6090 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| disord | 0.5350 | — | Yes | this paper | Table ef{table_results_peptidereactor} |
| dpc | 0.8060 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| fldpc_ | 0.7940 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| qsorde | 0.7890 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| waac_a | 0.7880 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| apaac_ | 0.7820 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| aac | 0.7810 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| binary | 0.7790 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ctdd | 0.7790 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| paac_l | 0.7790 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| aainde | 0.7780 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| tpc | 0.7660 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| cksaag | 0.7650 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ctriad | 0.7590 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ctdt | 0.7570 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ctdc | 0.7560 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ksctri | 0.7560 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| gtpc | 0.7500 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| gdpc | 0.7400 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| flgc_a | 0.7380 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| fft_aa | 0.7330 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| nmbrot | 0.7230 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| zscale | 0.7210 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| eaac_w | 0.7160 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| blomap | 0.7090 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| egaac_ | 0.7030 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| blosum | 0.6980 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| gaac | 0.6950 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| moran_ | 0.6900 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| socnum | 0.6900 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| geary_ | 0.6890 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| cgr_re | 0.6880 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| sseb | 0.5170 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| asa | 0.5150 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ta | 0.5140 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |
| ssec | 0.4830 | — | Yes | this paper | Table ef{appendix_table_results_peptidereactor} |

### Peptides-func — AP ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LightGBM (RDKit) | 0.7311 | — | No | this paper | Table appendix_peptides_func_additional_classifiers |
| Random Forest (RDKit) | 0.7148 | 0.0013 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |
| Extremely Randomized Trees (RDKit) | 0.6938 | 0.0006 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |
| LightGBM (TT) | 0.7318 | — | No | this paper | Table appendix_peptides_func_additional_classifiers |
| Random Forest (TT) | 0.7166 | 0.0009 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |
| Extremely Randomized Trees (TT) | 0.6986 | 0.0008 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |
| LightGBM (ECFP) | 0.7460 | — | No | this paper | Table appendix_peptides_func_additional_classifiers |
| Random Forest (ECFP) | 0.7355 | 0.0010 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |
| Extremely Randomized Trees (ECFP) | 0.7198 | 0.0008 | Yes | this paper | Table appendix_peptides_func_additional_classifiers |

### Peptides-struct — MAE ↓

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| LightGBM (RDKit) | 0.2459 | — | No | this paper | Table appendix_peptides_struct_additional_classifiers |
| Random Forest (RDKit) | 0.2459 | 0.0002 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |
| Extremely Randomized Trees (RDKit) | 0.2440 | 0.0001 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |
| LightGBM (TT) | 0.2438 | — | No | this paper | Table appendix_peptides_struct_additional_classifiers |
| Random Forest (TT) | 0.2471 | 0.0003 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |
| Extremely Randomized Trees (TT) | 0.2467 | 0.0003 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |
| LightGBM (ECFP) | 0.2432 | — | No | this paper | Table appendix_peptides_struct_additional_classifiers |
| Random Forest (ECFP) | 0.2442 | 0.0002 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |
| Extremely Randomized Trees (ECFP) | 0.2433 | 0.0001 | Yes | this paper | Table appendix_peptides_struct_additional_classifiers |

### XUAMP — AUROC ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMPscannerV2 | 0.5850 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| iAMP-2L | 0.5920 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| ADAM-SVM | 0.6120 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| ampir | 0.6190 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| MLAMP | 0.6290 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| ADAM-HMM | 0.6840 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| AMPlify | 0.6970 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| AMPEP | 0.7270 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| AMPfun | 0.7350 | — | Yes | AMPfun | Table ef{table_results_xu_amp} |
| RDKit | 0.7450 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| TT | 0.7310 | — | Yes | this paper | Table ef{table_results_xu_amp} |
| ECFP | 0.7500 | — | No | this paper | Table ef{table_results_xu_amp} |

### YADAMP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.8260 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.5880 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.8500 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.8210 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.8440 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.9200 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.9580 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.9580 | — | Yes | this paper | Table results_bert_benchmark |

### dbAMP — F1 ↑

| Model | Value | ±Std | Baseline? | Source | Table |
|-------|-------|------|-----------|--------|-------|
| AMP-BERT | 0.6270 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| BERT-Protein | 0.8290 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| cAMPs_pred | 0.5240 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred | 0.6070 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| LM_pred (BFD) | 0.6870 | — | Yes | BERT_benchmark | Table results_bert_benchmark |
| RDKit | 0.9140 | — | Yes | this paper | Table results_bert_benchmark |
| TT | 0.9080 | — | No | this paper | Table results_bert_benchmark |
| ECFP | 0.9150 | — | Yes | this paper | Table results_bert_benchmark |

## Baseline Models Identified

- **Random Forest**
- **Extremely Randomized Trees**
- **AMP-BERT** (from: BERT_benchmark)
- **BERT-Protein** (from: BERT_benchmark)
- **cAMPs_pred** (from: BERT_benchmark)
- **LM_pred** (from: BERT_benchmark)
- **LM_pred (BFD)** (from: BERT_benchmark)
- **RDKit**
- **ECFP**
- **AMPscannerV2**
- **iAMP-2L**
- **ADAM-SVM**
- **ampir**
- **MLAMP**
- **ADAM-HMM**
- **AMPlify**
- **AMPEP**
- **AMPfun** (from: AMPfun)
- **TT**
- **SVM-LZ**
- **CS-AMPPred**
- **AMAP**
- **Deep-AmPEP30** (from: DeepAmPEP30)
- **AmPEPpy**
- **AmpGram** (from: AmpGram)
- **MACREL**
- **ProtBERT**, 420.0M params
- **ESM2-150M**, 150.0M params
- **Prost-T5**, 3000.0M params
- **ESM2-8M**, 8.0M params
- **ESM2-35M**, 35.0M params
- **ESM1b-650M**, 650.0M params
- **ESM2-650M**, 650.0M params
- **Prot-T5-XL**, 3000.0M params
- **disord** (from: PeptideReactor)
- **electr** (from: PeptideReactor)
- **distan** (from: PeptideReactor)
- **delaun** (from: PeptideReactor)
- **qsar** (from: PeptideReactor)
- **dde** (from: PeptideReactor)
- **ngram_** (from: PeptideReactor)
- **psekraac** (from: PeptideReactor)
- **dist_f** (from: PeptideReactor)
- **cksaap** (from: PeptideReactor)
- **dpc** (from: PeptideReactor)
- **fldpc_** (from: PeptideReactor)
- **qsorde** (from: PeptideReactor)
- **waac_a** (from: PeptideReactor)
- **apaac_** (from: PeptideReactor)
- **aac** (from: PeptideReactor)
- **binary** (from: PeptideReactor)
- **ctdd** (from: PeptideReactor)
- **paac_l** (from: PeptideReactor)
- **aainde** (from: PeptideReactor)
- **tpc** (from: PeptideReactor)
- **cksaag** (from: PeptideReactor)
- **ctriad** (from: PeptideReactor)
- **ctdt** (from: PeptideReactor)
- **ctdc** (from: PeptideReactor)
- **ksctri** (from: PeptideReactor)
- **gtpc** (from: PeptideReactor)
- **gdpc** (from: PeptideReactor)
- **flgc_a** (from: PeptideReactor)
- **fft_aa** (from: PeptideReactor)
- **nmbrot** (from: PeptideReactor)
- **zscale** (from: PeptideReactor)
- **eaac_w** (from: PeptideReactor)
- **blomap** (from: PeptideReactor)
- **egaac_** (from: PeptideReactor)
- **blosum** (from: PeptideReactor)
- **gaac** (from: PeptideReactor)
- **moran_** (from: PeptideReactor)
- **socnum** (from: PeptideReactor)
- **geary_** (from: PeptideReactor)
- **cgr_re** (from: PeptideReactor)
- **sseb** (from: PeptideReactor)
- **asa** (from: PeptideReactor)
- **ta** (from: PeptideReactor)
- **ssec** (from: PeptideReactor)

## Extraction Notes

[Peptides-func] Extracted results from Table appendix_peptides_func_additional_classifiers. AUPRC
was normalized to AP as per primary metric instructions. Shuffling and sequence length split tables
were ignored as they represent non-standard/variant configurations. The proposed model is identified
as LightGBM based on the text. [Peptides-struct] Extracted results from the provided table. The
table uses a matrix format where rows are fingerprints (RDKit, TT, ECFP) and columns are classifiers
(LightGBM, RF, ERT). I have combined these into unique model names for the results list. [BERT-based
models benchmark] Extracted F1 values from the first table provided. The second table contained
Recall, Precision, and AUROC, which were skipped per the PRIMARY METRIC instruction. BERT-based
models are marked as using external data because the text explicitly mentions they were pretrained.
[XUAMP] Extracted results from Table  ef{table_results_xu_amp}. Shuffling results and sequence
length split results were ignored as per instructions to use only the standard/default configuration
and avoid optional variants. [AMPBenchmark] Values were reported as percentages (e.g., 97.37) and
normalized to [0, 1] as per instructions. ECFP is identified as the proposed fingerprint-based model
based on the text stating 'fingerprint-based models achieve the best performance' and the bolding in
the table. [AutoPeptideML] Extracted AUROC results from the primary results table. Shuffling results
and sequence length split results were ignored as they represent non-standard
configurations/variants. Params for ECFP/RDKit/TT were converted from 'k' to millions.
[PeptideReactor] Extracted all models from the main results table and the full results appendix
table for PeptideReactor. Skipped the 'tuned vs untuned' table as it represents a variant
configuration. Skipped the shuffling results table as it represents a specific experimental variant
(shuffling ratio) rather than the standard benchmark result. Normalised F1 scores from percentages
to [0, 1].

---
*This file is auto-generated. Edit `overrides.yaml` to correct errors.*