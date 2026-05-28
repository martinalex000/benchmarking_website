---
title: Photonics-Enhanced Graph Convolutional Networks
arxiv_id: '2512.15549'
source_url: ''
authors: []
published_date: Dec 2025
published_date_iso: 2025-12
abstract: Photonics can offer a hardware-native route for machine learning (ML). However,
  efficient deployment of photonics-enhanced ML requires hybrid workflows that integrate
  optical processing with conventional CPU/GPU based neural network architectures.
  Here, we propose such a workflow that combines photonic positional embeddings (PEs)
  with advanced graph ML models. We introduce a photonics-based method that augments
  graph convolutional networks (GCNs) with PEs derived from light propagation on synthetic
  frequency lattices whose couplings match the input graph. We simulate propagation
  and readout to obtain internode intensity correlation matrices, which are used as
  PEs in GCNs to provide global structural information. Evaluated on Long Range Graph
  Benchmark molecular datasets, the method outperforms baseline GCNs with Laplacian
  based PEs, achieving $6.3\
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN+PhotPE
mrr: 0.0035
adjusted_mrr: 0.0024
mrr_dataset_count: 2
benchmark_categories:
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4396
    std: 0.0048
    paper_value: 0.4396
    paper_std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2865
    value_note: ''
    paper_rank: 307
    rank_delta: 298
    rank_delta_abs: 298
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.4776
    std: 0.004
    paper_value: 0.4776
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 233
    true_value: 0.6218
    true_std: 0.0055
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1442
    value_note: ''
    paper_rank: 302
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.6218
    sort_std: 0.0055
    is_best: false
  - model: GCN+PhotPE
    model_key: gcn+photpe
    model_plain: GCN+PhotPE
    value: 0.4886
    std: 0.0052
    paper_value: 0.4886
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 300
    true_value: 0.4886
    true_std: 0.0052
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4886
    sort_std: 0.0052
    is_best: false
  - model: GCN
    model_key: gcn from ref.~\cite{dwivedi2022long}
    model_plain: GCN
    value: 0.4566
    std: 0.0059
    paper_value: 0.4566
    paper_std: 0.0059
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 305
    true_value: 0.4566
    true_std: 0.0059
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 305
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4566
    sort_std: 0.0059
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
    value: 0.4077
    std: 0.0009
    paper_value: 0.4077
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1656
    value_note: ''
    paper_rank: 332
    rank_delta: 329
    rank_delta_abs: 329
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: false
  - model: GCN+PhotPE
    model_key: gcn+photpe
    model_plain: GCN+PhotPE
    value: 0.2995
    std: 0.0005
    paper_value: 0.2995
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 269
    true_value: 0.2995
    true_std: 0.0005
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 269
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2995
    sort_std: 0.0005
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.3195
    std: 0.0014
    paper_value: 0.3195
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 287
    true_value: 0.3195
    true_std: 0.0014
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3195
    sort_std: 0.0014
    is_best: false
  - model: GCN
    model_key: gcn from ref.~\cite{dwivedi2022long}
    model_plain: GCN
    value: 0.395
    std: 0.0017
    paper_value: 0.395
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: Dwivedi et al. 2022
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 330
    true_value: 0.395
    true_std: 0.0017
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 330
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.395
    sort_std: 0.0017
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
single_proposed_model: GCN+PhotPE
main_figure: /figures/2512.15549/main_figure.png
---

