---
title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
arxiv_id: '2501.17901'
source_url: ''
authors: []
published_date: Jan 29, 2025
published_date_iso: '2025-01-29'
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
paper_type: method
proposed_models:
- LightGBM (RDKit)
- LightGBM (TT)
- LightGBM (ECFP)
- TT
- ECFP
- FP encoding
mrr: 0.1867
adjusted_mrr: 0.1244
mrr_dataset_count: 2
benchmark_categories:
- Heterophilic Graphs
- LRGB
- TU Dortmund
- Hypergraph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
  dataset: AMAP
  rows:
  - model: ECFP
    model_key: ecfp
    model_plain: ECFP
    value: 0.9737
    std: 0.0174
    paper_value: 0.9737
    paper_std: 0.0174
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9737
    sort_std: 0.0174
    is_best: true
  - model: RDKit
    model_key: rdkit
    model_plain: RDKit
    value: 0.9725
    std: 0.0184
    paper_value: 0.9725
    paper_std: 0.0184
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9725
    sort_std: 0.0184
    is_best: true
  - model: TT
    model_key: tt
    model_plain: TT
    value: 0.9719
    std: 0.0189
    paper_value: 0.9719
    paper_std: 0.0189
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9719
    sort_std: 0.0189
    is_best: true
  - model: AMPScannerV2
    model_key: ampscannerv2
    model_plain: AMPScannerV2
    value: 0.9679
    std: 0.0208
    paper_value: 0.9679
    paper_std: 0.0208
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9679
    sort_std: 0.0208
    is_best: true
  - model: ampir
    model_key: ampir
    model_plain: ampir
    value: 0.9671
    std: 0.0208
    paper_value: 0.9671
    paper_std: 0.0208
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9671
    sort_std: 0.0208
    is_best: true
  - model: MLAMP
    model_key: mlamp
    model_plain: MLAMP
    value: 0.9668
    std: 0.0235
    paper_value: 0.9668
    paper_std: 0.0235
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9668
    sort_std: 0.0235
    is_best: true
  - model: MACREL
    model_key: macrel
    model_plain: MACREL
    value: 0.9629
    std: 0.0243
    paper_value: 0.9629
    paper_std: 0.0243
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9629
    sort_std: 0.0243
    is_best: true
  - model: AmpGram
    model_key: ampgram
    model_plain: AmpGram
    value: 0.9556
    std: 0.0254
    paper_value: 0.9556
    paper_std: 0.0254
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9556
    sort_std: 0.0254
    is_best: true
  - model: AmPEPpy
    model_key: ampeppy
    model_plain: AmPEPpy
    value: 0.9535
    std: 0.0299
    paper_value: 0.9535
    paper_std: 0.0299
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9535
    sort_std: 0.0299
    is_best: true
  - model: Deep-AmPEP30
    model_key: deep-ampep30
    model_plain: Deep-AmPEP30
    value: 0.9098
    std: 0.0561
    paper_value: 0.9098
    paper_std: 0.0561
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.9098
    sort_std: 0.0561
    is_best: true
  - model: AMAP
    model_key: amap
    model_plain: AMAP
    value: 0.8987
    std: 0.0418
    paper_value: 0.8987
    paper_std: 0.0418
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.8987
    sort_std: 0.0418
    is_best: false
  - model: CS-AMPPred
    model_key: cs-amppred
    model_plain: CS-AMPPred
    value: 0.8669
    std: 0.0436
    paper_value: 0.8669
    paper_std: 0.0436
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.8669
    sort_std: 0.0436
    is_best: false
  - model: SVM-LZ
    model_key: svm-lz
    model_plain: SVM-LZ
    value: 0.7971
    std: 0.0243
    paper_value: 0.7971
    paper_std: 0.0243
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.7971
    sort_std: 0.0243
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.67
    sort_std: 0.1
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.65
    sort_std: 0.07
    is_best: false
  - model: iAMP-2L
    model_key: iamp-2l
    model_plain: iAMP-2L
    value: 0.626
    std: 0.0951
    paper_value: 0.626
    paper_std: 0.0951
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.626
    sort_std: 0.0951
    is_best: false
  - model: AmPEP
    model_key: ampep
    model_plain: AmPEP
    value: 0.6169
    std: 0.0693
    paper_value: 0.6169
    paper_std: 0.0693
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_ampbenchmark_sidorczuk}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.6169
    sort_std: 0.0693
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.16
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Actor
  rows:
  - model: FP encoding
    model_key: fp encoding
    model_plain: FP encoding
    value: 0.829
    std: null
    paper_value: 0.829
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.829
    sort_std: null
    is_best: true
  - model: cksaap
    model_key: cksaap
    model_plain: cksaap
    value: 0.824
    std: null
    paper_value: 0.824
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.824
    sort_std: null
    is_best: false
  - model: dist_f
    model_key: dist_f
    model_plain: dist_f
    value: 0.822
    std: null
    paper_value: 0.822
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.822
    sort_std: null
    is_best: false
  - model: psekraac
    model_key: psekraac
    model_plain: psekraac
    value: 0.818
    std: null
    paper_value: 0.818
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.818
    sort_std: null
    is_best: false
  - model: ECFP
    model_key: ecfp
    model_plain: ECFP
    value: 0.817
    std: null
    paper_value: 0.817
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.817
    sort_std: null
    is_best: false
  - model: ngram_
    model_key: ngram_
    model_plain: ngram_
    value: 0.816
    std: null
    paper_value: 0.816
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.816
    sort_std: null
    is_best: false
  - model: dde
    model_key: dde
    model_plain: dde
    value: 0.813
    std: null
    paper_value: 0.813
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.813
    sort_std: null
    is_best: false
  - model: RDKit
    model_key: rdkit
    model_plain: RDKit
    value: 0.806
    std: null
    paper_value: 0.806
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.806
    sort_std: null
    is_best: false
  - model: TT
    model_key: tt
    model_plain: TT
    value: 0.806
    std: null
    paper_value: 0.806
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.806
    sort_std: null
    is_best: false
  - model: dpc
    model_key: dpc
    model_plain: dpc
    value: 0.806
    std: null
    paper_value: 0.806
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.806
    sort_std: null
    is_best: false
  - model: fldpc_
    model_key: fldpc_
    model_plain: fldpc_
    value: 0.794
    std: null
    paper_value: 0.794
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.794
    sort_std: null
    is_best: false
  - model: qsorde
    model_key: qsorde
    model_plain: qsorde
    value: 0.789
    std: null
    paper_value: 0.789
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.789
    sort_std: null
    is_best: false
  - model: waac_a
    model_key: waac_a
    model_plain: waac_a
    value: 0.788
    std: null
    paper_value: 0.788
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.788
    sort_std: null
    is_best: false
  - model: apaac_
    model_key: apaac_
    model_plain: apaac_
    value: 0.782
    std: null
    paper_value: 0.782
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.782
    sort_std: null
    is_best: false
  - model: aac
    model_key: aac
    model_plain: aac
    value: 0.781
    std: null
    paper_value: 0.781
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.781
    sort_std: null
    is_best: false
  - model: binary
    model_key: binary
    model_plain: binary
    value: 0.779
    std: null
    paper_value: 0.779
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.779
    sort_std: null
    is_best: false
  - model: ctdd
    model_key: ctdd
    model_plain: ctdd
    value: 0.779
    std: null
    paper_value: 0.779
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.779
    sort_std: null
    is_best: false
  - model: paac_l
    model_key: paac_l
    model_plain: paac_l
    value: 0.779
    std: null
    paper_value: 0.779
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.779
    sort_std: null
    is_best: false
  - model: aainde
    model_key: aainde
    model_plain: aainde
    value: 0.778
    std: null
    paper_value: 0.778
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.778
    sort_std: null
    is_best: false
  - model: tpc
    model_key: tpc
    model_plain: tpc
    value: 0.766
    std: null
    paper_value: 0.766
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.766
    sort_std: null
    is_best: false
  - model: cksaag
    model_key: cksaag
    model_plain: cksaag
    value: 0.765
    std: null
    paper_value: 0.765
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.765
    sort_std: null
    is_best: false
  - model: ctriad
    model_key: ctriad
    model_plain: ctriad
    value: 0.759
    std: null
    paper_value: 0.759
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.759
    sort_std: null
    is_best: false
  - model: ctdt
    model_key: ctdt
    model_plain: ctdt
    value: 0.757
    std: null
    paper_value: 0.757
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.757
    sort_std: null
    is_best: false
  - model: ctdc
    model_key: ctdc
    model_plain: ctdc
    value: 0.756
    std: null
    paper_value: 0.756
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.756
    sort_std: null
    is_best: false
  - model: ksctri
    model_key: ksctri
    model_plain: ksctri
    value: 0.756
    std: null
    paper_value: 0.756
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.756
    sort_std: null
    is_best: false
  - model: gtpc
    model_key: gtpc
    model_plain: gtpc
    value: 0.75
    std: null
    paper_value: 0.75
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.75
    sort_std: null
    is_best: false
  - model: gdpc
    model_key: gdpc
    model_plain: gdpc
    value: 0.74
    std: null
    paper_value: 0.74
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.74
    sort_std: null
    is_best: false
  - model: flgc_a
    model_key: flgc_a
    model_plain: flgc_a
    value: 0.738
    std: null
    paper_value: 0.738
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.738
    sort_std: null
    is_best: false
  - model: fft_aa
    model_key: fft_aa
    model_plain: fft_aa
    value: 0.733
    std: null
    paper_value: 0.733
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.733
    sort_std: null
    is_best: false
  - model: qsar
    model_key: qsar
    model_plain: qsar
    value: 0.728
    std: null
    paper_value: 0.728
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.728
    sort_std: null
    is_best: false
  - model: nmbrot
    model_key: nmbrot
    model_plain: nmbrot
    value: 0.723
    std: null
    paper_value: 0.723
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.723
    sort_std: null
    is_best: false
  - model: zscale
    model_key: zscale
    model_plain: zscale
    value: 0.721
    std: null
    paper_value: 0.721
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.721
    sort_std: null
    is_best: false
  - model: eaac_w
    model_key: eaac_w
    model_plain: eaac_w
    value: 0.716
    std: null
    paper_value: 0.716
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.716
    sort_std: null
    is_best: false
  - model: blomap
    model_key: blomap
    model_plain: blomap
    value: 0.709
    std: null
    paper_value: 0.709
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.709
    sort_std: null
    is_best: false
  - model: blosum
    model_key: blosum
    model_plain: blosum
    value: 0.698
    std: null
    paper_value: 0.698
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.698
    sort_std: null
    is_best: false
  - model: delaun
    model_key: delaun
    model_plain: delaun
    value: 0.695
    std: null
    paper_value: 0.695
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.695
    sort_std: null
    is_best: false
  - model: egaac_
    model_key: egaac_
    model_plain: egaac_
    value: 0.695
    std: null
    paper_value: 0.695
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.695
    sort_std: null
    is_best: false
  - model: moran_
    model_key: moran_
    model_plain: moran_
    value: 0.69
    std: null
    paper_value: 0.69
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.69
    sort_std: null
    is_best: false
  - model: socnum
    model_key: socnum
    model_plain: socnum
    value: 0.69
    std: null
    paper_value: 0.69
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.69
    sort_std: null
    is_best: false
  - model: geary_
    model_key: geary_
    model_plain: geary_
    value: 0.689
    std: null
    paper_value: 0.689
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.689
    sort_std: null
    is_best: false
  - model: cgr_re
    model_key: cgr_re
    model_plain: cgr_re
    value: 0.688
    std: null
    paper_value: 0.688
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.688
    sort_std: null
    is_best: false
  - model: distan
    model_key: distan
    model_plain: distan
    value: 0.613
    std: null
    paper_value: 0.613
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.613
    sort_std: null
    is_best: false
  - model: electr
    model_key: electr
    model_plain: electr
    value: 0.609
    std: null
    paper_value: 0.609
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.609
    sort_std: null
    is_best: false
  - model: disord
    model_key: disord
    model_plain: disord
    value: 0.535
    std: null
    paper_value: 0.535
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.535
    sort_std: null
    is_best: false
  - model: sseb
    model_key: sseb
    model_plain: sseb
    value: 0.517
    std: null
    paper_value: 0.517
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.517
    sort_std: null
    is_best: false
  - model: asa
    model_key: asa
    model_plain: asa
    value: 0.515
    std: null
    paper_value: 0.515
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.515
    sort_std: null
    is_best: false
  - model: ta
    model_key: ta
    model_plain: ta
    value: 0.514
    std: null
    paper_value: 0.514
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.514
    sort_std: null
    is_best: false
  - model: ssec
    model_key: ssec
    model_plain: ssec
    value: 0.483
    std: null
    paper_value: 0.483
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{appendix_table_results_peptidereactor}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: null
    sort_value: 0.483
    sort_std: null
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: false
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: cAMPs_pred
    model_key: camps_pred
    model_plain: cAMPs_pred
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
    sort_value: 0.85
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.85
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: LM_pred (BFD)
    model_key: lm_pred (bfd)
    model_plain: LM_pred (BFD)
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
    sort_value: 0.844
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.844
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: AMP-BERT
    model_key: amp-bert
    model_plain: AMP-BERT
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
    sort_value: 0.826
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.826
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: LM_pred
    model_key: lm_pred
    model_plain: LM_pred
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
    sort_value: 0.821
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.821
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ESM2-150M
    model_key: esm2-150m
    model_plain: ESM2-150M
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
    sort_value: 0.797
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.797
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Prot-T5-XL
    model_key: prot-t5-xl
    model_plain: Prot-T5-XL
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
    sort_value: 0.797
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.797
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ESM1b-650M
    model_key: esm1b-650m
    model_plain: ESM1b-650M
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
    sort_value: 0.789
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.789
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ECFP
    model_key: ecfp
    model_plain: ECFP
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
    sort_value: 0.781
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.781
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ESM2-35M
    model_key: esm2-35m
    model_plain: ESM2-35M
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
    sort_value: 0.78
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.78
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ESM2-8M
    model_key: esm2-8m
    model_plain: ESM2-8M
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
    sort_value: 0.775
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.775
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: TT
    model_key: tt
    model_plain: TT
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
    sort_value: 0.771
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.771
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Prost-T5
    model_key: prost-t5
    model_plain: Prost-T5
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
    sort_value: 0.771
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.771
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: RDKit
    model_key: rdkit
    model_plain: RDKit
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
    sort_value: 0.769
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.769
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: ProtBERT
    model_key: protbert
    model_plain: ProtBERT
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
    sort_value: 0.759
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.759
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BERT-Protein
    model_key: bert-protein
    model_plain: BERT-Protein
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
    sort_value: 0.588
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.588
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: null
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
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    paper_value: 0.746
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 1
    true_value: 0.746
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    paper_value: 0.7355
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 2
    true_value: 0.7355
    true_std: 0.001
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    paper_value: 0.7318
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 3
    true_value: 0.7318
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: LightGBM (RDKit)
    model_key: lightgbm (rdkit)
    model_plain: LightGBM (RDKit)
    value: 0.7311
    std: null
    paper_value: 0.7311
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 5
    true_value: 0.7311
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7311
    sort_std: null
    is_best: false
  - model: S2GCN+PE
    model_key: s2gcn+pe
    model_plain: S2GCN+PE
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: false
  - model: S4G
    model_key: s4g
    model_plain: S4G
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.7293
    sort_std: 0.0004
    is_best: false
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.7276
    std: 0.0065
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks for message diffusion on graphs
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.7276
    sort_std: 0.0065
    is_best: false
  - model: Extremely Randomized Trees (ECFP)
    model_key: extremely randomized trees (ecfp)
    model_plain: Extremely Randomized Trees (ECFP)
    value: 0.7198
    std: 0.0008
    paper_value: 0.7198
    paper_std: 0.0008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 15
    true_value: 0.7198
    true_std: 0.0008
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7198
    sort_std: 0.0008
    is_best: false
  - model: Random Forest
    model_key: random forest
    model_plain: Random Forest
    value: 0.7166
    std: 0.0009
    paper_value: 0.7166
    paper_std: 0.0009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 19
    true_value: 0.7166
    true_std: 0.0009
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7166
    sort_std: 0.0009
    is_best: false
  - model: Random Forest (RDKit)
    model_key: random forest (rdkit)
    model_plain: Random Forest (RDKit)
    value: 0.7148
    std: 0.0013
    paper_value: 0.7148
    paper_std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 25
    true_value: 0.7148
    true_std: 0.0013
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.0013
    is_best: false
  - model: Extremely Randomized Trees (TT)
    model_key: extremely randomized trees (tt)
    model_plain: Extremely Randomized Trees (TT)
    value: 0.6986
    std: 0.0008
    paper_value: 0.6986
    paper_std: 0.0008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 54
    true_value: 0.6986
    true_std: 0.0008
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6986
    sort_std: 0.0008
    is_best: false
  - model: Extremely Randomized Trees (RDKit)
    model_key: extremely randomized trees (rdkit)
    model_plain: Extremely Randomized Trees (RDKit)
    value: 0.6938
    std: 0.0006
    paper_value: 0.6938
    paper_std: 0.0006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_func_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 76
    true_value: 0.6938
    true_std: 0.0006
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6938
    sort_std: 0.0006
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.2432
    std: null
    paper_value: 0.2432
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 17
    true_value: 0.2432
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2432
    sort_std: null
    is_best: false
  - model: Extremely Randomized Trees (ECFP)
    model_key: extremely randomized trees (ecfp)
    model_plain: Extremely Randomized Trees (ECFP)
    value: 0.2433
    std: 0.0001
    paper_value: 0.2433
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 18
    true_value: 0.2433
    true_std: 0.0001
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2433
    sort_std: 0.0001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.2438
    std: null
    paper_value: 0.2438
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 25
    true_value: 0.2438
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2438
    sort_std: null
    is_best: false
  - model: Extremely Randomized Trees (RDKit)
    model_key: extremely randomized trees (rdkit)
    model_plain: Extremely Randomized Trees (RDKit)
    value: 0.244
    std: 0.0001
    paper_value: 0.244
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 28
    true_value: 0.244
    true_std: 0.0001
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.244
    sort_std: 0.0001
    is_best: false
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.2442
    std: 0.0002
    paper_value: 0.2442
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 29
    true_value: 0.2442
    true_std: 0.0002
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2442
    sort_std: 0.0002
    is_best: false
  - model: LightGBM (RDKit)
    model_key: lightgbm (rdkit)
    model_plain: LightGBM (RDKit)
    value: 0.2459
    std: null
    paper_value: 0.2459
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 52
    true_value: 0.2459
    true_std: null
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2459
    sort_std: null
    is_best: false
  - model: Random Forest (RDKit)
    model_key: random forest (rdkit)
    model_plain: Random Forest (RDKit)
    value: 0.2459
    std: 0.0002
    paper_value: 0.2459
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 53
    true_value: 0.2459
    true_std: 0.0002
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2459
    sort_std: 0.0002
    is_best: false
  - model: Extremely Randomized Trees (TT)
    model_key: extremely randomized trees (tt)
    model_plain: Extremely Randomized Trees (TT)
    value: 0.2467
    std: 0.0003
    paper_value: 0.2467
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 70
    true_value: 0.2467
    true_std: 0.0003
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2467
    sort_std: 0.0003
    is_best: false
  - model: Random Forest
    model_key: random forest
    model_plain: Random Forest
    value: 0.2471
    std: 0.0003
    paper_value: 0.2471
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table appendix_peptides_struct_additional_classifiers
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    global_rank: 74
    true_value: 0.2471
    true_std: 0.0003
    value_gap_source_arxiv: '2501.17901'
    value_gap_source_title: Molecular Fingerprints Are Strong Models for Peptide Function
      Prediction
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2471
    sort_std: 0.0003
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

