---
title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based Centrality'
arxiv_id: '2501.03113'
source_url: ''
authors: []
published_date: Jan 2025
published_date_iso: 2025-01
abstract: 'Subgraph GNNs have emerged as promising architectures that overcome the
  expressiveness limitations of Graph Neural Networks (GNNs) by processing bags of
  subgraphs. Despite their compelling empirical performance, these methods are afflicted
  by a high computational complexity: they process bags whose size grows linearly
  in the number of nodes, hindering their applicability to larger graphs. In this
  work, we propose an effective and easy-to-implement approach to dramatically alleviate
  the computational cost of Subgraph GNNs and unleash broader applications thereof.
  Our method, dubbed HyMN, leverages walk-based centrality measures to sample a small
  number of relevant subgraphs and drastically reduce the bag size. By drawing a connection
  to perturbation analysis, we highlight the strength of the proposed centrality-based
  subgraph sampling, and further prove that these walk-based centralities can be additionally
  used as Structural Encodings for improved discriminative power. A comprehensive
  set of experimental results demonstrates that HyMN provides an effective synthesis
  of expressiveness, efficiency, and downstream performance, unlocking the application
  of Subgraph GNNs to dramatically larger graphs. Not only does our method outperform
  more sophisticated subgraph sampling approaches, it is also competitive, and sometimes
  better, than other state-of-the-art approaches for a fraction of their runtime.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- HyMN (GIN, T=2) no CSE
- HyMN (GIN, T=2)
- HyMN (GatedGCN, T=2) w/out CSE
- HyMN (GatedGCN, T=2)
- HyMN (GCN, T=1)
- HyMN (GIN, T=1) w/out CSE
- HyMN (T=2)
mrr: 0.0255
adjusted_mrr: 0.0255
mrr_dataset_count: 6
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id006
  dataset: BACE
  rows:
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.868
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.868
    sort_std: 0.004
    is_best: true
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.85
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.85
    sort_std: 0.011
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8435
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7297
    std: 0.04
    paper_value: 0.7297
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 11
    true_value: 0.825
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09529999999999994
    value_note: ''
    paper_rank: 58
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.825
    sort_std: 0.019
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.8064
    std: 0.0048
    paper_value: 0.8064
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 20
    true_value: 0.8064
    true_std: 0.0048
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8064
    sort_std: 0.0048
    is_best: false
  - model: CS-GNN (T = 2)
    model_key: cs-gnn (t = 2)
    model_plain: CS-GNN (T = 2)
    value: 0.7964
    std: 0.0143
    paper_value: 0.7964
    paper_std: 0.0143
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 27
    true_value: 0.7964
    true_std: 0.0143
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7964
    sort_std: 0.0143
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7915
    std: 0.0144
    paper_value: 0.7915
    paper_std: 0.0144
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 34
    true_value: 0.7915
    true_std: 0.0144
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7915
    sort_std: 0.0144
    is_best: false
  - model: HyMN (GIN, T=2) no CSE
    model_key: hymn (gin, t=2) no cse
    model_plain: HyMN (GIN, T=2) no CSE
    value: 0.7857
    std: 0.0131
    paper_value: 0.7857
    paper_std: 0.0131
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 37
    true_value: 0.7857
    true_std: 0.0131
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7857
    sort_std: 0.0131
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.7841
    std: 0.0194
    paper_value: 0.7841
    paper_std: 0.0194
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 39
    true_value: 0.7841
    true_std: 0.0194
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7841
    sort_std: 0.0194
    is_best: false
  - model: POLICY-LEARN (T = 2)
    model_key: policy-learn (t = 2)
    model_plain: POLICY-LEARN (T = 2)
    value: 0.7839
    std: 0.0228
    paper_value: 0.7839
    paper_std: 0.0228
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 42
    true_value: 0.7839
    true_std: 0.0228
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7839
    sort_std: 0.0228
    is_best: false
  - model: RANDOM (T = 2)
    model_key: random (t = 2)
    model_plain: RANDOM (T = 2)
    value: 0.7814
    std: 0.0236
    paper_value: 0.7814
    paper_std: 0.0236
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 43
    true_value: 0.7814
    true_std: 0.0236
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7814
    sort_std: 0.0236
    is_best: false
  - model: OSAN (T = 10)
    model_key: osan (t = 10)
    model_plain: OSAN (T = 10)
    value: 0.763
    std: 0.03
    paper_value: 0.763
    paper_std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 51
    true_value: 0.763
    true_std: 0.03
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.03
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id002
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
    value: 0.6739
    std: 0.0024
    paper_value: 0.6739
    paper_std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05219999999999991
    value_note: ''
    paper_rank: 116
    rank_delta: 107
    rank_delta_abs: 107
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6555
    std: 0.0088
    paper_value: 0.6555
    paper_std: 0.0088
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0504
    value_note: ''
    paper_rank: 165
    rank_delta: 124
    rank_delta_abs: 124
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6558
    std: 0.0068
    paper_value: 0.6558
    paper_std: 0.0068
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04479999999999995
    value_note: ''
    paper_rank: 165
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6942
    std: 0.0075
    paper_value: 0.6942
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 61
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027999999999999137
    value_note: global 0.6970 within std
    paper_rank: 74
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.6948
    std: 0.0052
    paper_value: 0.6948
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 72
    true_value: 0.6948
    true_std: 0.0052
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6948
    sort_std: 0.0052
    is_best: false
  - model: GINE-MLP-Mixer
    model_key: gine-mlp-mixer
    model_plain: GINE-MLP-Mixer
    value: 0.6921
    std: 0.0054
    paper_value: 0.6921
    paper_std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 79
    true_value: 0.6921
    true_std: 0.0054
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6921
    sort_std: 0.0054
    is_best: false
  - model: HyMN (GCN, T=1)
    model_key: hymn (gcn, t=1)
    model_plain: HyMN (GCN, T=1)
    value: 0.6912
    std: 0.017
    paper_value: 0.6912
    paper_std: 0.017
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 82
    true_value: 0.6912
    true_std: 0.017
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6912
    sort_std: 0.017
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.686
    std: 0.005
    paper_value: 0.686
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 89
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GCN + CSE
    model_key: gcn + cse
    model_plain: GCN + CSE
    value: 0.6812
    std: 0.0037
    paper_value: 0.6812
    paper_std: 0.0037
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 106
    true_value: 0.6812
    true_std: 0.0037
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6812
    sort_std: 0.0037
    is_best: false
  - model: HyMN (GatedGCN, T=2)
    model_key: hymn (gatedgcn, t=2)
    model_plain: HyMN (GatedGCN, T=2)
    value: 0.6788
    std: 0.0052
    paper_value: 0.6788
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 110
    true_value: 0.6788
    true_std: 0.0052
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6788
    sort_std: 0.0052
    is_best: false
  - model: HyMN (GIN, T=1) w/out CSE
    model_key: hymn (gin, t=1) w/out cse
    model_plain: HyMN (GIN, T=1) w/out CSE
    value: 0.6758
    std: 0.005
    paper_value: 0.6758
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 114
    true_value: 0.6758
    true_std: 0.005
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6758
    sort_std: 0.005
    is_best: false
  - model: HyMN (GatedGCN, T=2) w/out CSE
    model_key: hymn (gatedgcn, t=2) w/out cse
    model_plain: HyMN (GatedGCN, T=2) w/out CSE
    value: 0.6723
    std: 0.0079
    paper_value: 0.6723
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 124
    true_value: 0.6723
    true_std: 0.0079
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6723
    sort_std: 0.0079
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.6621
    std: 0.0067
    paper_value: 0.6621
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 144
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GIN+CSE
    model_key: gin+cse
    model_plain: GIN+CSE
    value: 0.6619
    std: 0.0077
    paper_value: 0.6619
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 146
    true_value: 0.6619
    true_std: 0.0077
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6619
    sort_std: 0.0077
    is_best: false
  - model: GatedGCN + CSE
    model_key: gatedgcn + cse
    model_plain: GatedGCN + CSE
    value: 0.6611
    std: 0.0058
    paper_value: 0.6611
    paper_std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 148
    true_value: 0.6611
    true_std: 0.0058
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6611
    sort_std: 0.0058
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 168
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
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
    value: 0.2505
    std: 0.0023
    paper_value: 0.2505
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00839999999999999
    value_note: ''
    paper_rank: 144
    rank_delta: 141
    rank_delta_abs: 141
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2497
    std: 0.0012
    paper_value: 0.2497
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0068000000000000005
    value_note: ''
    paper_rank: 130
    rank_delta: 121
    rank_delta_abs: 121
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2497
    std: 0.0007
    paper_value: 0.2497
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006599999999999995
    value_note: ''
    paper_rank: 130
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2449
    std: 0.0016
    paper_value: 0.2449
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: HyMN (GIN, T=1) w/out CSE
    model_key: hymn (gin, t=1) w/out cse
    model_plain: HyMN (GIN, T=1) w/out CSE
    value: 0.2466
    std: 0.001
    paper_value: 0.2466
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 69
    true_value: 0.2466
    true_std: 0.001
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2466
    sort_std: 0.001
    is_best: false
  - model: HyMN (GatedGCN, T=2)
    model_key: hymn (gatedgcn, t=2)
    model_plain: HyMN (GatedGCN, T=2)
    value: 0.2471
    std: 0.0007
    paper_value: 0.2471
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 75
    true_value: 0.2471
    true_std: 0.0007
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2471
    sort_std: 0.0007
    is_best: false
  - model: HyMN (GatedGCN, T=2) w/out CSE
    model_key: hymn (gatedgcn, t=2) w/out cse
    model_plain: HyMN (GatedGCN, T=2) w/out CSE
    value: 0.2473
    std: 0.0013
    paper_value: 0.2473
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 82
    true_value: 0.2473
    true_std: 0.0013
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0013
    is_best: false
  - model: GINE-MLP-Mixer
    model_key: gine-mlp-mixer
    model_plain: GINE-MLP-Mixer
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 87
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.2477
    std: 0.001
    paper_value: 0.2477
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 93
    true_value: 0.2477
    true_std: 0.001
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.001
    is_best: false
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 0.2478
    std: 0.0017
    paper_value: 0.2478
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 95
    true_value: 0.2478
    true_std: 0.0017
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2478
    sort_std: 0.0017
    is_best: false
  - model: GIN+CSE
    model_key: gin+cse
    model_plain: GIN+CSE
    value: 0.2479
    std: 0.0011
    paper_value: 0.2479
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 98
    true_value: 0.2479
    true_std: 0.0011
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2479
    sort_std: 0.0011
    is_best: false
  - model: HyMN (GCN, T=1)
    model_key: hymn (gcn, t=1)
    model_plain: HyMN (GCN, T=1)
    value: 0.2481
    std: 0.0013
    paper_value: 0.2481
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 103
    true_value: 0.2481
    true_std: 0.0013
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0013
    is_best: false
  - model: GatedGCN + CSE
    model_key: gatedgcn + cse
    model_plain: GatedGCN + CSE
    value: 0.2482
    std: 0.001
    paper_value: 0.2482
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 105
    true_value: 0.2482
    true_std: 0.001
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2482
    sort_std: 0.001
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.2498
    std: 0.0015
    paper_value: 0.2498
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 132
    true_value: 0.2498
    true_std: 0.0015
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2498
    sort_std: 0.0015
    is_best: false
  - model: GCN + CSE
    model_key: gcn + cse
    model_plain: GCN + CSE
    value: 0.2499
    std: 0.001
    paper_value: 0.2499
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 133
    true_value: 0.2499
    true_std: 0.001
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2499
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: RDT-B
  rows:
  - model: HyMN (T=2)
    model_key: hymn (t=2)
    model_plain: HyMN (T=2)
    value: 0.932
    std: 0.022
    paper_value: 0.932
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 1
    true_value: 0.932
    true_std: 0.022
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.932
    sort_std: 0.022
    is_best: true
  - model: POLICY-LEARN (T = 2)
    model_key: policy-learn (t = 2)
    model_plain: POLICY-LEARN (T = 2)
    value: 0.93
    std: 0.009
    paper_value: 0.93
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: bevilacqua2023efficient
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 2
    true_value: 0.93
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.93
    sort_std: 0.009
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.924
    std: 0.025
    paper_value: 0.924
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 3
    true_value: 0.924
    true_std: 0.025
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.924
    sort_std: 0.025
    is_best: true
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.924
    std: 0.021
    paper_value: 0.924
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: bodnar2021weisfeiler
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 4
    true_value: 0.924
    true_std: 0.021
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.924
    sort_std: 0.021
    is_best: true
  - model: RANDOM (T = 2)
    model_key: random (t = 2)
    model_plain: RANDOM (T = 2)
    value: 0.924
    std: 0.01
    paper_value: 0.924
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 5
    true_value: 0.924
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.924
    sort_std: 0.01
    is_best: true
  - model: SIN
    model_key: sin
    model_plain: SIN
    value: 0.922
    std: 0.01
    paper_value: 0.922
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:rdtb_accuracy}"
    source_ref: bodnar2021cellular
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 6
    true_value: 0.922
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.922
    sort_std: 0.01
    is_best: true
  metric: Accuracy
  higher_is_better: true
- &id007
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
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
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
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
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
  - model: HyMN (GIN, T=2) no CSE
    model_key: hymn (gin, t=2) no cse
    model_plain: HyMN (GIN, T=2) no CSE
    value: 0.7782
    std: 0.0059
    paper_value: 0.7782
    paper_std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 20
    true_value: 0.7782
    true_std: 0.0059
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7782
    sort_std: 0.0059
    is_best: false
  - model: POLICY-LEARN (T = 2)
    model_key: policy-learn (t = 2)
    model_plain: POLICY-LEARN (T = 2)
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
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 25
    true_value: 0.7736
    true_std: 0.006
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7736
    sort_std: 0.006
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.7699
    std: 0.0045
    paper_value: 0.7699
    paper_std: 0.0045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 26
    true_value: 0.7699
    true_std: 0.0045
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7699
    sort_std: 0.0045
    is_best: false
  - model: RANDOM (T = 2)
    model_key: random (t = 2)
    model_plain: RANDOM (T = 2)
    value: 0.7662
    std: 0.0089
    paper_value: 0.7662
    paper_std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 34
    true_value: 0.7662
    true_std: 0.0089
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7662
    sort_std: 0.0089
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.7625
    std: 0.0112
    paper_value: 0.7625
    paper_std: 0.0112
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 39
    true_value: 0.7625
    true_std: 0.011200000000000002
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
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
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 144
    rank_delta: 137
    rank_delta_abs: 137
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampášek et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 107
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.163
    std: 0.004
    paper_value: 0.163
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 246
    rank_delta: 171
    rank_delta_abs: 171
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GINE-MLP-Mixer
    model_key: gine-mlp-mixer
    model_plain: GINE-MLP-Mixer
    value: 0.073
    std: 0.001
    paper_value: 0.073
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 119
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.321
    std: 0.009
    paper_value: 0.321
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.245
    value_note: ''
    paper_rank: 276
    rank_delta: 145
    rank_delta_abs: 145
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.083
    std: 0.002
    paper_value: 0.083
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 151
    true_value: 0.083
    true_std: 0.002
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.083
    sort_std: 0.002
    is_best: false
  - model: GINE-ViT
    model_key: gine-vit
    model_plain: GINE-ViT
    value: 0.085
    std: 0.004
    paper_value: 0.085
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 162
    true_value: 0.085
    true_std: 0.004
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.004
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.087
    std: 0.003
    paper_value: 0.087
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 169
    true_value: 0.087
    true_std: 0.003
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.087
    sort_std: 0.003
    is_best: false
  - model: GIN+CSE
    model_key: gin+cse
    model_plain: GIN+CSE
    value: 0.092
    std: 0.002
    paper_value: 0.092
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 179
    true_value: 0.092
    true_std: 0.002
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.092
    sort_std: 0.002
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.101
    std: 0.01
    paper_value: 0.101
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bouritsas et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 188
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: POLICY-LEARN (T = 2)
    model_key: policy-learn (t = 2)
    model_plain: POLICY-LEARN (T = 2)
    value: 0.12
    std: 0.003
    paper_value: 0.12
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 207
    true_value: 0.12
    true_std: 0.003
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.12
    sort_std: 0.003
    is_best: false
  - model: HyMN (GIN, T=1) w/out CSE
    model_key: hymn (gin, t=1) w/out cse
    model_plain: HyMN (GIN, T=1) w/out CSE
    value: 0.125
    std: 0.004
    paper_value: 0.125
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 213
    true_value: 0.125
    true_std: 0.004
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.125
    sort_std: 0.004
    is_best: false
  - model: RANDOM (T = 2)
    model_key: random (t = 2)
    model_plain: RANDOM (T = 2)
    value: 0.136
    std: 0.005
    paper_value: 0.136
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 225
    true_value: 0.136
    true_std: 0.005
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 225
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.136
    sort_std: 0.005
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.177
    std: 0.016
    paper_value: 0.177
    paper_std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al.
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 236
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022999999999999993
    value_note: ''
    paper_rank: 247
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7606
    std: 0.0097
    paper_value: 0.7606
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2074999999999999
    value_note: ''
    paper_rank: 161
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7558
    std: 0.014
    paper_value: 0.7558
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21219999999999994
    value_note: ''
    paper_rank: 172
    rank_delta: 168
    rank_delta_abs: 168
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: HyMN (GatedGCN, T=2)
    model_key: hymn (gatedgcn, t=2)
    model_plain: HyMN (GatedGCN, T=2)
    value: 0.8107
    std: 0.0021
    paper_value: 0.8107
    paper_std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 8
    true_value: 0.8107
    true_std: 0.0021
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8107
    sort_std: 0.0021
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 9
    true_value: 0.8094
    true_std: 0.0057
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7827
    std: 0.0065
    paper_value: 0.7827
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 19
    true_value: 0.804
    true_std: 0.0164
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021300000000000097
    value_note: ''
    paper_rank: 97
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.804
    sort_std: 0.0164
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.8039
    std: 0.009
    paper_value: 0.8039
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 20
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: GatedGCN + CSE
    model_key: gatedgcn + cse
    model_plain: GatedGCN + CSE
    value: 0.8033
    std: 0.0056
    paper_value: 0.8033
    paper_std: 0.0056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 25
    true_value: 0.8033
    true_std: 0.0056
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8033
    sort_std: 0.0056
    is_best: false
  - model: HyMN (GIN, T=2)
    model_key: hymn (gin, t=2)
    model_plain: HyMN (GIN, T=2)
    value: 0.8017
    std: 0.014
    paper_value: 0.8017
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 30
    true_value: 0.8017
    true_std: 0.014
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8017
    sort_std: 0.014
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.8003
    std: 0.0055
    paper_value: 0.8003
    paper_std: 0.0055
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 32
    true_value: 0.8003
    true_std: 0.0055
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8003
    sort_std: 0.0055
    is_best: false
  - model: GINE-MLP-Mixer
    model_key: gine-mlp-mixer
    model_plain: GINE-MLP-Mixer
    value: 0.7997
    std: 0.0102
    paper_value: 0.7997
    paper_std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 35
    true_value: 0.7997
    true_std: 0.0102
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7997
    sort_std: 0.0102
    is_best: false
  - model: HyMN (GIN, T=2) no CSE
    model_key: hymn (gin, t=2) no cse
    model_plain: HyMN (GIN, T=2) no CSE
    value: 0.7962
    std: 0.0114
    paper_value: 0.7962
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 44
    true_value: 0.7962
    true_std: 0.0114
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7962
    sort_std: 0.0114
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.7961
    std: 0.0119
    paper_value: 0.7961
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 45
    true_value: 0.7961
    true_std: 0.0119
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7961
    sort_std: 0.0119
    is_best: false
  - model: CS-GNN (T = 2)
    model_key: cs-gnn (t = 2)
    model_plain: CS-GNN (T = 2)
    value: 0.7909
    std: 0.009
    paper_value: 0.7909
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 62
    true_value: 0.7909
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7909
    sort_std: 0.009
    is_best: false
  - model: HyMN (GatedGCN, T=2) w/out CSE
    model_key: hymn (gatedgcn, t=2) w/out cse
    model_plain: HyMN (GatedGCN, T=2) w/out CSE
    value: 0.7902
    std: 0.0091
    paper_value: 0.7902
    paper_std: 0.0091
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 64
    true_value: 0.7902
    true_std: 0.0091
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7902
    sort_std: 0.0091
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 76
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: POLICY-LEARN (T = 2)
    model_key: policy-learn (t = 2)
    model_plain: POLICY-LEARN (T = 2)
    value: 0.7849
    std: 0.0101
    paper_value: 0.7849
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 89
    true_value: 0.7849
    true_std: 0.0101
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7849
    sort_std: 0.0101
    is_best: false
  - model: Nested-GNN
    model_key: nested-gnn
    model_plain: Nested-GNN
    value: 0.7834
    std: 0.0186
    paper_value: 0.7834
    paper_std: 0.0186
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 93
    true_value: 0.7834
    true_std: 0.0186
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7834
    sort_std: 0.0186
    is_best: false
  - model: GINE-ViT
    model_key: gine-vit
    model_plain: GINE-ViT
    value: 0.7792
    std: 0.0142
    paper_value: 0.7792
    paper_std: 0.0142
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 120
    true_value: 0.7792
    true_std: 0.0142
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7792
    sort_std: 0.0142
    is_best: false
  - model: GIN+CSE
    model_key: gin+cse
    model_plain: GIN+CSE
    value: 0.7744
    std: 0.0187
    paper_value: 0.7744
    paper_std: 0.0187
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 126
    true_value: 0.7744
    true_std: 0.0187
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7744
    sort_std: 0.0187
    is_best: false
  - model: RANDOM (T = 2)
    model_key: random (t = 2)
    model_plain: RANDOM (T = 2)
    value: 0.773
    std: 0.0256
    paper_value: 0.773
    paper_std: 0.0256
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 129
    true_value: 0.773
    true_std: 0.0256
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.0256
    is_best: false
  - model: MAG-GNN (T = 2)
    model_key: mag-gnn (t = 2)
    model_plain: MAG-GNN (T = 2)
    value: 0.7712
    std: 0.0113
    paper_value: 0.7712
    paper_std: 0.0113
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 135
    true_value: 0.7712
    true_std: 0.0113
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7712
    sort_std: 0.0113
    is_best: false
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.7678
    std: 0.0166
    paper_value: 0.7678
    paper_std: 0.0166
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 145
    true_value: 0.7678
    true_std: 0.0166
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7678
    sort_std: 0.0166
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.7654
    std: 0.0137
    paper_value: 0.7654
    paper_std: 0.0137
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 150
    true_value: 0.7654
    true_std: 0.0137
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7654
    sort_std: 0.0137
    is_best: false
  - model: Reconstr. GNN
    model_key: reconstr. gnn
    model_plain: Reconstr. GNN
    value: 0.7632
    std: 0.014
    paper_value: 0.7632
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 155
    true_value: 0.7632
    true_std: 0.014
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7632
    sort_std: 0.014
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
- benchmark: MoleculeNet
  datasets:
  - *id006
  - *id007
main_figure: /figures/2501.03113/main_figure.png
---

