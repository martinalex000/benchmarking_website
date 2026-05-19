---
title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
arxiv_id: '2501.17901'
authors: []
published_date: '2025-01-29'
abstract: Understanding peptide properties is often assumed to require modeling long-range
  molecular interactions, motivating the use of complex graph neural networks and
  pretrained transformers. Yet, whether such long-range dependencies are essential
  remains unclear. We investigate if simple, domain-specific molecular fingerprints
  can capture peptide function without these assumptions. Atomic-level representation
  aims to provide richer information than purely sequence-based models and better
  efficiency than structural ones. Across 132 datasets, including LRGB and five other
  peptide benchmarks, models using count-based ECFP, Topological Torsion, and RDKit
  fingerprints with LightGBM achieve state-of-the-art accuracy. Despite encoding only
  short-range molecular features, these models outperform GNNs and transformer-based
  approaches. Control experiments with sequence shuffling and amino acid counts confirm
  that fingerprints, though inherently local, suffice for robust peptide property
  prediction. Our results challenge the presumed necessity of long-range interaction
  modeling and highlight molecular fingerprints as efficient, interpretable, and computationally
  lightweight alternatives for peptide prediction.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- LightGBM (RDKit)
- LightGBM (TT)
- LightGBM (ECFP)
- TT
- ECFP
- FP encoding
mrr: 0.1905
results:
- &id005
  dataset: AMAP
  rows:
  - model: ECFP
    value: 0.9737
    std: 0.0174
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: RDKit
    value: 0.9725
    std: 0.0184
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: TT
    value: 0.9719
    std: 0.0189
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: AMPScannerV2
    value: 0.9679
    std: 0.0208
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: ampir
    value: 0.9671
    std: 0.0208
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: MLAMP
    value: 0.9668
    std: 0.0235
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: MACREL
    value: 0.9629
    std: 0.0243
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: AmpGram
    value: 0.9556
    std: 0.0254
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: AmPEPpy
    value: 0.9535
    std: 0.0299
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: Deep-AmPEP30
    value: 0.9098
    std: 0.0561
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: AMAP
    value: 0.8987
    std: 0.0418
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: CS-AMPPred
    value: 0.8669
    std: 0.0436
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SVM-LZ
    value: 0.7971
    std: 0.0243
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMON
    value: 0.67
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: SUBLIME
    value: 0.65
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: iAMP-2L
    value: 0.626
    std: 0.0951
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: AmPEP
    value: 0.6169
    std: 0.0693
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: VGAER
    value: 0.61
    std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Actor
  rows:
  - model: FP encoding
    value: 0.829
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: cksaap
    value: 0.824
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: dist_f
    value: 0.822
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: psekraac
    value: 0.818
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ECFP
    value: 0.817
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ngram_
    value: 0.816
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: dde
    value: 0.813
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: RDKit
    value: 0.806
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: TT
    value: 0.806
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: dpc
    value: 0.806
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: fldpc_
    value: 0.794
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: qsorde
    value: 0.789
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: waac_a
    value: 0.788
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: apaac_
    value: 0.782
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: aac
    value: 0.781
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: binary
    value: 0.779
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ctdd
    value: 0.779
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: paac_l
    value: 0.779
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: aainde
    value: 0.778
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: tpc
    value: 0.766
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: cksaag
    value: 0.765
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ctriad
    value: 0.759
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ctdt
    value: 0.757
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ctdc
    value: 0.756
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ksctri
    value: 0.756
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: gtpc
    value: 0.75
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: gdpc
    value: 0.74
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: flgc_a
    value: 0.738
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: fft_aa
    value: 0.733
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: qsar
    value: 0.728
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: nmbrot
    value: 0.723
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: zscale
    value: 0.721
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: eaac_w
    value: 0.716
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: blomap
    value: 0.709
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: blosum
    value: 0.698
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: delaun
    value: 0.695
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: egaac_
    value: 0.695
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: moran_
    value: 0.69
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: socnum
    value: 0.69
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: geary_
    value: 0.689
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: cgr_re
    value: 0.688
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: distan
    value: 0.613
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: electr
    value: 0.609
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: disord
    value: 0.535
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: sseb
    value: 0.517
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: asa
    value: 0.515
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ta
    value: 0.514
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ssec
    value: 0.483
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GrokFormer
    value: 0.4298
    std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: GrokFilter
    value: 0.4215
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: SpecFormer
    value: 0.4193
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: TT
    metric_values:
    - 0.958
    - 0.771
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: ECFP
    metric_values:
    - 0.958
    - 0.781
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: RDKit
    metric_values:
    - 0.92
    - 0.769
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: cAMPs_pred
    metric_values:
    - 0.85
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: LM_pred (BFD)
    metric_values:
    - 0.844
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: AMP-BERT
    metric_values:
    - 0.826
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: LM_pred
    metric_values:
    - 0.821
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: BERT-Protein
    metric_values:
    - 0.588
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: ProtBERT
    metric_values:
    - null
    - 0.759
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 420.0
    is_best: false
    global_rank: null
  - model: ESM2-150M
    metric_values:
    - null
    - 0.797
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 150.0
    is_best: false
    global_rank: null
  - model: Prost-T5
    metric_values:
    - null
    - 0.771
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 3000.0
    is_best: false
    global_rank: null
  - model: ESM2-8M
    metric_values:
    - null
    - 0.775
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 8.0
    is_best: false
    global_rank: null
  - model: ESM2-35M
    metric_values:
    - null
    - 0.78
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 35.0
    is_best: false
    global_rank: null
  - model: ESM1b-650M
    metric_values:
    - null
    - 0.789
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 650.0
    is_best: false
    global_rank: null
  - model: Prot-T5-XL
    metric_values:
    - null
    - 0.797
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 3000.0
    is_best: false
    global_rank: null
  metrics:
  - F1
  - AUROC
  primary_metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: LightGBM (RDKit)
    value: 0.7311
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: S2GCN+PE
    value: 0.7311
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: S4G
    value: 0.7293
    std: 0.0004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    is_best: false
  - model: BuNN
    value: 0.7276
    std: 0.0065
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks - for message diffusion on graphs
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    is_best: false
  - model: Extremely Randomized Trees (ECFP)
    value: 0.7198
    std: 0.0008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: Random Forest
    value: 0.7166
    std: 0.0009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Random Forest (RDKit)
    value: 0.7148
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: Extremely Randomized Trees (TT)
    value: 0.6986
    std: 0.0008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: Extremely Randomized Trees (RDKit)
    value: 0.6938
    std: 0.0006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    global_rank: 74
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: LightGBM (ECFP)
    value: 0.2432
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 14
    is_best: true
  - model: Extremely Randomized Trees (ECFP)
    value: 0.2433
    std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 15
    is_best: true
  - model: LightGBM (TT)
    value: 0.2438
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 21
    is_best: true
  - model: Extremely Randomized Trees (RDKit)
    value: 0.244
    std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 22
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.2442
    std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 23
    is_best: true
  - model: LightGBM (RDKit)
    value: 0.2459
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: Random Forest (RDKit)
    value: 0.2459
    std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: Extremely Randomized Trees (TT)
    value: 0.2467
    std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: Random Forest
    value: 0.2471
    std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    global_rank: 67
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id005
main_figure: /figures/2501.17901/main_figure.png
---

