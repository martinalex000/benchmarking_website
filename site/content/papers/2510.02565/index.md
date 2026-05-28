---
title: On The Expressive Power of GNN Derivatives
arxiv_id: '2510.02565'
source_url: ''
authors: []
published_date: Oct 2025
published_date_iso: 2025-10
abstract: Despite significant advances in Graph Neural Networks (GNNs), their limited
  expressivity remains a fundamental challenge. Research on GNN expressivity has produced
  many expressive architectures, leading to architecture hierarchies with models of
  increasing expressive power. Separately, derivatives of GNNs with respect to node
  features have been widely studied in the context of the oversquashing and over-smoothing
  phenomena, GNN explainability, and more. To date, these derivatives remain unexplored
  as a means to enhance GNN expressivity. In this paper, we show that these derivatives
  provide a natural way to enhance the expressivity of GNNs. We introduce High-Order
  Derivative GNN, a novel method that enhances the expressivity of Message Passing
  Neural Networks (MPNNs) by leveraging high-order node derivatives of the base model.
  These derivatives generate expressive structure-aware node embeddings processed
  by a second GNN in an end-to-end trainable architecture. Theoretically, we show
  that the resulting architecture family's expressive power aligns with the WL hierarchy.
  We also draw deep connections between, Subgraph GNNs, and popular structural encoding
  schemes. For computational efficiency, we develop a message-passing algorithm for
  computing high-order derivatives of MPNNs that exploits graph sparsity and parallelism.
  Evaluations on multiple graph learning benchmarks demonstrate ’s excellent performance
  on popular graph learning tasks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- HOD-GNN
mrr: 0.0325
adjusted_mrr: 0.0325
mrr_dataset_count: 3
benchmark_categories:
- LRGB
- MoleculeNet
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
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.715
    std: 0.0044
    paper_value: 0.715
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: drew
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 23
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6919
    std: 0.0085
    paper_value: 0.6919
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 61
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005099999999999993
    value_note: global 0.6970 within std
    paper_rank: 80
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: HOD-GNN
    model_key: hod-gnn
    model_plain: HOD-GNN
    value: 0.6968000000000001
    std: 0.005600000000000001
    paper_value: 0.6968000000000001
    paper_std: 0.005600000000000001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 65
    true_value: 0.6968000000000001
    true_std: 0.005600000000000001
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6968000000000001
    sort_std: 0.005600000000000001
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.6067
    std: 0.0069
    paper_value: 0.6067
    paper_std: 0.0069
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2021graph
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 89
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07930000000000004
    value_note: ''
    paper_rank: 241
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: HyMN
    model_key: hymn
    model_plain: HyMN
    value: 0.6857
    std: 0.0055000000000000005
    paper_value: 0.6857
    paper_std: 0.0055000000000000005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: southern2025balancing
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 91
    true_value: 0.6857
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6857
    sort_std: 0.0055000000000000005
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.6843
    std: 0.0049
    paper_value: 0.6843
    paper_std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 93
    true_value: 0.6843
    true_std: 0.0049
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6843
    sort_std: 0.0049
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.6829999999999999
    std: 0.0026
    paper_value: 0.6829999999999999
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 96
    true_value: 0.683
    true_std: 0.0026
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.683
    sort_std: 0.0026
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.6688
    std: 0.0151
    paper_value: 0.6688
    paper_std: 0.0151
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: canturk_gpse
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 130
    true_value: 0.6688
    true_std: 0.0151
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6688
    sort_std: 0.0151
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 288
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.6067
    std: 0.0069
    paper_value: 0.6067
    paper_std: 0.0069
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2021graph
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 144
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055400000000000005
    value_note: ''
    paper_rank: 241
    rank_delta: 97
    rank_delta_abs: 97
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.6415000000000001
    std: 0.0052
    paper_value: 0.6415000000000001
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: bar-shalom2024subgraphormer
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 149
    true_value: 0.661
    true_std: 0.005
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019499999999999962
    value_note: ''
    paper_rank: 208
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.661
    sort_std: 0.005
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
    value: 0.6535
    std: 0.0040999999999999995
    paper_value: 0.6535
    paper_std: 0.0040999999999999995
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 169
    true_value: 0.6535
    true_std: 0.0040999999999999995
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0040999999999999995
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: 0.0043
    paper_value: 0.6527
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: Policy-Learn
    model_key: policy-learn
    model_plain: Policy-Learn
    value: 0.6459
    std: 0.0018
    paper_value: 0.6459
    paper_std: 0.0018
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: bevilacqua2023efficient
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 195
    true_value: 0.6459
    true_std: 0.0018
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6459
    sort_std: 0.0018
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384000000000001
    std: 0.0121
    paper_value: 0.6384000000000001
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LRGB
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: MOSE
    model_key: mose
    model_plain: MOSE
    value: 0.635
    std: 0.011000000000000001
    paper_value: 0.635
    paper_std: 0.011000000000000001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: bao2024homomorphism
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 214
    true_value: 0.635
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 214
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.635
    sort_std: 0.011000000000000001
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.6315999999999999
    std: 0.0085
    paper_value: 0.6315999999999999
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: canturk_gpse
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 222
    true_value: 0.6316
    true_std: 0.0085
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 222
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6316
    sort_std: 0.0085
    is_best: false
  - model: SignNet
    model_key: signnet
    model_plain: SignNet
    value: 0.6314
    std: 0.0059
    paper_value: 0.6314
    paper_std: 0.0059
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lim2022sign
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 223
    true_value: 0.6314
    true_std: 0.0059
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6314
    sort_std: 0.0059
    is_best: false
  - model: GIN + Laplacian PE
    model_key: gin + laplacian pe
    model_plain: GIN + Laplacian PE
    value: 0.6218
    std: 0.0055000000000000005
    paper_value: 0.6218
    paper_std: 0.0055000000000000005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2023benchmarking
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 234
    true_value: 0.6218
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6218
    sort_std: 0.0055000000000000005
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: 0.0078000000000000005
    paper_value: 0.5543
    paper_std: 0.0078000000000000005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 285
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
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
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2474
    std: 0.0016
    paper_value: 0.2474
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0025000000000000022
    value_note: ''
    paper_rank: 83
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: HOD-GNN
    model_key: hod-gnn
    model_plain: HOD-GNN
    value: 0.245
    std: 0.0011
    paper_value: 0.245
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 34
    true_value: 0.245
    true_std: 0.0011
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.245
    sort_std: 0.0011
    is_best: false
  - model: HyMN
    model_key: hymn
    model_plain: HyMN
    value: 0.2464
    std: 0.0013
    paper_value: 0.2464
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Southern et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 62
    true_value: 0.2464
    true_std: 0.0013
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2464
    sort_std: 0.0013
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.2464
    std: 0.0025
    paper_value: 0.2464
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cantürk et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 63
    true_value: 0.2464
    true_std: 0.0025
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2464
    sort_std: 0.0025
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: Policy-Learn
    model_key: policy-learn
    model_plain: Policy-Learn
    value: 0.2475
    std: 0.0011
    paper_value: 0.2475
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 85
    true_value: 0.2475
    true_std: 0.0011
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0011
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.2494
    std: 0.002
    paper_value: 0.2494
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bar-Shalom et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 86
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0019000000000000128
    value_note: global 0.2475 within std
    paper_rank: 128
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.2475
    sort_std: 0.0007
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.2574
    std: 0.002
    paper_value: 0.2574
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 95
    true_value: 0.2478
    true_std: 0.0017
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009600000000000025
    value_note: ''
    paper_rank: 207
    rank_delta: 112
    rank_delta_abs: 112
    rank_delta_direction: worse
    sort_value: 0.2478
    sort_std: 0.0017
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.2487
    std: 0.0011
    paper_value: 0.2487
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cantürk et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 114
    true_value: 0.2487
    true_std: 0.0011
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2487
    sort_std: 0.0011
    is_best: false
  - model: GIN + Laplacian PE
    model_key: gin + laplacian pe
    model_plain: GIN + Laplacian PE
    value: 0.2492
    std: 0.0019
    paper_value: 0.2492
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 128
    true_value: 0.2492
    true_std: 0.0019
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2492
    sort_std: 0.0019
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.2574
    std: 0.002
    paper_value: 0.2574
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 132
    true_value: 0.2498
    true_std: 0.0015
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007600000000000023
    value_note: ''
    paper_rank: 207
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.2498
    sort_std: 0.0015
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 138
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.2536
    std: 0.0015
    paper_value: 0.2536
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 175
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.2614
    std: 0.0023
    paper_value: 0.2614
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 217
    true_value: 0.2614
    true_std: 0.0023
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2614
    sort_std: 0.0023
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.2616
    std: 0.0018
    paper_value: 0.2616
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 218
    true_value: 0.2616
    true_std: 0.0018
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2616
    sort_std: 0.0018
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 242
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: MOSE
    model_key: mose
    model_plain: MOSE
    value: 0.318
    std: 0.01
    paper_value: 0.318
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bao et al.
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 285
    true_value: 0.318
    true_std: 0.01
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.01
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3471
    std: 0.001
    paper_value: 0.3471
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 300
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: Tox21
  rows:
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.874
    std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.874
    sort_std: 0.005
    is_best: true
  - model: Ours(dual readout)
    model_key: ours(dual readout)
    model_plain: Ours(dual readout)
    value: 0.851
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: GNNs (dual readout, VN)
    model_key: gnns (dual readout, vn)
    model_plain: GNNs (dual readout, VN)
    value: 0.851
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7491
    std: 0.0051
    paper_value: 0.7491
    paper_std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 5
    true_value: 0.85
    true_std: 0.009
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10089999999999999
    value_note: ''
    paper_rank: 55
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.85
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7529
    std: 0.0069
    paper_value: 0.7529
    paper_std: 0.0069
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 12
    true_value: 0.84
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08709999999999996
    value_note: ''
    paper_rank: 52
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.84
    sort_std: 0.004
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.7851
    std: 0.0077
    paper_value: 0.7851
    paper_std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 17
    true_value: 0.7851
    true_std: 0.0077
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7851
    sort_std: 0.0077
    is_best: false
  - model: HOD-GNN
    model_key: hod-gnn
    model_plain: HOD-GNN
    value: 0.7798999999999999
    std: 0.0070999999999999995
    paper_value: 0.7798999999999999
    paper_std: 0.0070999999999999995
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 19
    true_value: 0.7798999999999999
    true_std: 0.0070999999999999995
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7798999999999999
    sort_std: 0.0070999999999999995
    is_best: false
  - model: HyMN
    model_key: hymn
    model_plain: HyMN
    value: 0.7781999999999999
    std: 0.0059
    paper_value: 0.7781999999999999
    paper_std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 21
    true_value: 0.7781999999999999
    true_std: 0.0059
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7781999999999999
    sort_std: 0.0059
    is_best: false
  - model: GPSE
    model_key: gpse
    model_plain: GPSE
    value: 0.774
    std: null
    paper_value: 0.774
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 22
    true_value: 0.774
    true_std: null
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: null
    is_best: false
  - model: Policy-Learn
    model_key: policy-learn
    model_plain: Policy-Learn
    value: 0.7736
    std: 0.006
    paper_value: 0.7736
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 24
    true_value: 0.7736
    true_std: 0.006
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7736
    sort_std: 0.006
    is_best: false
  - model: Random
    model_key: random
    model_plain: Random
    value: 0.7662
    std: 0.0063
    paper_value: 0.7662
    paper_std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 33
    true_value: 0.7662
    true_std: 0.0063
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7662
    sort_std: 0.0063
    is_best: false
  - model: GIN + Laplacian PE
    model_key: gin + laplacian pe
    model_plain: GIN + Laplacian PE
    value: 0.7659999999999999
    std: null
    paper_value: 0.7659999999999999
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 36
    true_value: 0.7659999999999999
    true_std: null
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7659999999999999
    sort_std: null
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.763
    std: 0.005
    paper_value: 0.763
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 37
    true_value: 0.763
    true_std: 0.005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.005
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.7625
    std: 0.011200000000000002
    paper_value: 0.7625
    paper_std: 0.011200000000000002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 39
    true_value: 0.7625
    true_std: 0.011200000000000002
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7625
    sort_std: 0.011200000000000002
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.7608
    std: 0.0079
    paper_value: 0.7608
    paper_std: 0.0079
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 42
    true_value: 0.7608
    true_std: 0.0079
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7608
    sort_std: 0.0079
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.757
    std: 0.004
    paper_value: 0.757
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 47
    true_value: 0.757
    true_std: 0.004
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.004
    is_best: false
  - model: Reconstr. GNN
    model_key: reconstr. gnn
    model_plain: Reconstr. GNN
    value: 0.7515000000000001
    std: 0.013999999999999999
    paper_value: 0.7515000000000001
    paper_std: 0.013999999999999999
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 53
    true_value: 0.7515000000000001
    true_std: 0.013999999999999999
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7515000000000001
    sort_std: 0.013999999999999999
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.733
    std: null
    paper_value: 0.733
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 72
    true_value: 0.733
    true_std: null
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: null
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: MoleculeNet
  datasets:
  - *id003
single_proposed_model: HOD-GNN
main_figure: /figures/2510.02565/main_figure.png
---

