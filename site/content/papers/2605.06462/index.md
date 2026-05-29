---
title: Invariant-Based Diagnostics for Graph Benchmarks
arxiv_id: '2605.06462'
source_url: ''
authors: []
published_date: May 2026
published_date_iso: 2026-05
abstract: Progress on graph foundation models is hindered by benchmark practices that
  conflate the contributions of node features and graph structure, making it hard
  to tell whether a model actually learns from connectivity, or whether it even needs
  to. We propose addressing this using graph invariants, i.e., permutation-invariant,
  task-agnostic structural descriptors that serve as a diagnostic framework for graph
  benchmarks. We show that [(i)] invariants are more expressive than standard GNNs,
  invariants characterize structural heterogeneity within and across benchmark datasets,
  invariants predict multi-task performance, and simple invariant-based models are
  competitive with, and sometimes exceed, transformer and message-passing baselines
  across 26 datasets. Our results suggest that expressivity is not the main driver
  of predictive performance, and that on tasks where structure matters, a non-trainable
  structural proxy often matches trained message-passing models. We thus posit that
  invariant baselines should become a standard for evaluating whether structure is
  required for a task and whether a model picks up on it, serving as a stepping stone
  towards graph foundation models.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- LRGB
- OGB
- MoleculeNet
- GraphBench
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id005
  dataset: BACE
  rows:
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.857
    std: 0.002
    paper_value: 0.857
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 1
    true_value: 0.857
    true_std: 0.002
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.857
    sort_std: 0.002
    is_best: true
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.856
    std: 0.011
    paper_value: 0.856
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 2
    true_value: 0.856
    true_std: 0.011
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.856
    sort_std: 0.011
    is_best: true
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.845
    std: 0.007
    paper_value: 0.845
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 3
    true_value: 0.845
    true_std: 0.007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.007
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
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.827
    std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.274
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.827
    sort_std: 0.018
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.826
    std: 0.007
    paper_value: 0.826
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 6
    true_value: 0.826
    true_std: 0.007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.007
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.824
    std: 0.009
    paper_value: 0.824
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 0.824
    true_std: 0.009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.009
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.8239
    std: 0.0053
    paper_value: 0.8239
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 0.8239
    true_std: 0.0053
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8239
    sort_std: 0.0053
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.812
    std: 0.009
    paper_value: 0.812
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 9
    true_value: 0.812
    true_std: 0.009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.009
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.81
    std: 0.014
    paper_value: 0.81
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 10
    true_value: 0.81
    true_std: 0.014
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.014
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.809
    std: 0.006
    paper_value: 0.809
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 11
    true_value: 0.809
    true_std: 0.006
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7915
    std: 0.0144
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.7915
    sort_std: 0.0144
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.791
    std: 0.013
    paper_value: 0.791
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 13
    true_value: 0.791
    true_std: 0.013
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.013
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.784
    std: 0.0
    paper_value: 0.784
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 15
    true_value: 0.784
    true_std: 0.0
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.0
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.779
    std: 0.015
    paper_value: 0.779
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 16
    true_value: 0.779
    true_std: 0.015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.015
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: BBBP
  rows:
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.7408
    std: 0.0
    paper_value: 0.7408
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 1
    true_value: 0.7408
    true_std: 0.0
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7408
    sort_std: 0.0
    is_best: true
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.729
    std: 0.006
    paper_value: 0.729
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 2
    true_value: 0.729
    true_std: 0.006
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.729
    sort_std: 0.006
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.724
    std: 0.016
    paper_value: 0.724
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 3
    true_value: 0.724
    true_std: 0.016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.016
    is_best: false
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.724
    std: 0.004
    paper_value: 0.724
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 4
    true_value: 0.724
    true_std: 0.004
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.004
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.722
    std: 0.021
    paper_value: 0.722
    paper_std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 0.722
    true_std: 0.021
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.722
    sort_std: 0.021
    is_best: true
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.71
    std: 0.003
    paper_value: 0.71
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 6
    true_value: 0.71
    true_std: 0.003
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.003
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.7
    std: 0.001
    paper_value: 0.7
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 0.7
    true_std: 0.001
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.001
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.697
    std: 0.006
    paper_value: 0.697
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 0.697
    true_std: 0.006
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.006
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.695
    std: 0.001
    paper_value: 0.695
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 9
    true_value: 0.695
    true_std: 0.001
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.001
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.691
    std: 0.008
    paper_value: 0.691
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 10
    true_value: 0.691
    true_std: 0.008
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.691
    sort_std: 0.008
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.687
    std: 0.013
    paper_value: 0.687
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 11
    true_value: 0.687
    true_std: 0.013
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.687
    sort_std: 0.013
    is_best: false
  - model: UnionSNN
    model_key: unionsnn
    model_plain: UnionSNN
    value: 0.6828
    std: 0.0147
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.6828
    sort_std: 0.0147
    is_best: false
  - model: CurvGN
    model_key: curvgn
    model_plain: CurvGN
    value: 0.6651
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 13
    sort_value: 0.6651
    sort_std: 0.008
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.643
    std: 0.018
    paper_value: 0.643
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 14
    true_value: 0.643
    true_std: 0.018
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.018
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.641
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 15
    sort_value: 0.641
    sort_std: 0.0105
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
  dataset: Flow
  rows:
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 16.0
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 1.45
    sort_std: 0.06
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 1.49
    sort_std: 0.02
    is_best: true
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 1.73
    sort_std: 0.09
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 1.83
    std: 0.01
    paper_value: 1.83
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to easy (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 5.3
    std: 0.12
    paper_value: 5.3
    paper_std: 0.12
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to medium (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 3.4699999999999998
    value_note: ''
    paper_rank: 8
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 5.26
    std: 0.03
    paper_value: 5.26
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to hard (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 5
    true_value: 1.83
    true_std: 0.01
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 3.4299999999999997
    value_note: ''
    paper_rank: 8
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 1.83
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 3.44
    std: null
    paper_value: 3.44
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to easy (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.44
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 3.44
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.6
    std: null
    paper_value: 9.6
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to medium (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.44
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 6.16
    value_note: ''
    paper_rank: 8
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 3.44
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.51
    std: null
    paper_value: 9.51
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to hard (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 7
    true_value: 3.44
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 6.07
    value_note: ''
    paper_rank: 8
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 3.44
    sort_std: null
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 4.27
    std: null
    paper_value: 4.27
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to easy (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.27
    sort_std: null
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 6.38
    std: null
    paper_value: 6.38
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to medium (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.1100000000000003
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.27
    sort_std: null
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 6.48
    std: null
    paper_value: 6.48
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Stoll et al.
    variant_inference_reason: 'dataset: fuzzy match to hard (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 8
    true_value: 4.27
    true_std: null
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.210000000000001
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.27
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Peptides-func
  rows:
  - model: S2GCN +PE
    model_key: s2gcn +pe
    model_plain: S2GCN +PE
    value: 0.7311
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: true
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.7275
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7275
    sort_std: 0.0066
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.7182
    std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7182
    sort_std: 0.0024
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 4
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7074
    std: 0.0032
    paper_value: 0.7074
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 12
    true_value: 0.7074
    true_std: 0.0032
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7074
    sort_std: 0.0032
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6988
    std: 0.0082
    paper_value: 0.6988
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 19
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 23
    true_value: 0.6942
    true_std: 0.0075
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6942
    sort_std: 0.0075
    is_best: false
  - model: G.MLPMixer
    model_key: g.mlpmixer
    model_plain: G.MLPMixer
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 24
    true_value: 0.6921
    true_std: 0.0054
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6921
    sort_std: 0.0054
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.6874
    std: 0.0022
    paper_value: 0.6874
    paper_std: 0.0022
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 27
    true_value: 0.6874
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6874
    sort_std: 0.0022
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 28
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09300000000000008
    value_note: ''
    paper_rank: 78
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn (retuned)
    model_plain: GCN
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
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 29
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.005
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 35
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09009999999999996
    value_note: ''
    paper_rank: 78
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6765
    sort_std: 0.0047
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn (retuned)
    model_plain: GatedGCN
    value: 0.6765
    std: 0.0047
    paper_value: 0.6765
    paper_std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 36
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6765
    sort_std: 0.0047
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 45
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 83
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GINE
    model_key: gine (retuned)
    model_plain: GINE
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
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 46
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
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
    source_ref: Rampásek et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 50
    true_value: 0.6565
    true_std: 0.0038
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.6565 within std
    paper_rank: 52
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.6565
    sort_std: 0.0038
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 51
    true_value: 0.6562
    true_std: 0.0075
    value_gap_source_arxiv: '2302.08647'
    value_gap_source_title: Multiresolution Graph Transformers and Wavelet Positional
      Encoding for Learning Hierarchical Structures
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012299999999999978
    value_note: ''
    paper_rank: 63
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.6562
    sort_std: 0.0075
    is_best: false
  - model: GPS
    model_key: gps (retuned)
    model_plain: GPS
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 56
    true_value: 0.6534
    true_std: 0.0091
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6534
    sort_std: 0.0091
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 58
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 67
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 69
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    paper_value: 0.6069
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 75
    true_value: 0.6069
    true_std: 0.0035
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6069
    sort_std: 0.0035
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: 0.0078
    paper_value: 0.5543
    paper_std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 83
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
  higher_is_better: true
- &id001
  dataset: Peptides-struct
  rows:
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
    global_rank: 1
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: true
  - model: B-PEARL+SRF
    model_key: b-pearl+srf
    model_plain: B-PEARL+SRF
    value: 0.243
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.243
    sort_std: null
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.2436
    std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
    is_best: true
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 6
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 14
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10360000000000003
    value_note: ''
    paper_rank: 94
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.246
    std: 0.0012
    paper_value: 0.246
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 15
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: GCN
    model_key: gcn (retuned)
    model_plain: GCN
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 16
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 22
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 94
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: GINE
    model_key: gine (retuned)
    model_plain: GINE
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 24
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: G.MLPMixer
    model_key: g.mlpmixer
    model_plain: G.MLPMixer
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 29
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.2476
    std: 0.0002
    paper_value: 0.2476
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 30
    true_value: 0.2476
    true_std: 0.0002
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2476
    sort_std: 0.0002
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 31
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09430000000000002
    value_note: ''
    paper_rank: 93
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn (retuned)
    model_plain: GatedGCN
    value: 0.2477
    std: 0.0009
    paper_value: 0.2477
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 32
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0009
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 37
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
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
    source_ref: Rampásek et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 44
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.2506
    std: 0.0022
    paper_value: 0.2506
    paper_std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 50
    true_value: 0.2506
    true_std: 0.0022
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0022
    is_best: false
  - model: GPS
    model_key: gps (retuned)
    model_plain: GPS
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 52
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2509
    sort_std: 0.0014
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 55
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
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
    source_ref: Tönsheff et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 57
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2545
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 64
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 78
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
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    paper_value: 0.3357
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 92
    true_value: 0.3357
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3357
    sort_std: 0.0006
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
    source_ref: Dwivedi et al.
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 94
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id007
  dataset: QM9
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.025
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.025
    sort_std: 0.001
    is_best: true
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.026
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.026
    sort_std: 0.001
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.028
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.028
    sort_std: 0.001
    is_best: false
  - model: XGBoost (agg_+_i)
    model_key: xgboost (agg_+_i)
    model_plain: XGBoost (agg_+_i)
    value: 0.5846
    std: 0.0012
    paper_value: 0.5846
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
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 28
    true_value: 0.5846
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5846
    sort_std: 0.0012
    is_best: false
  - model: XGBoost (agg_+_subset)
    model_key: xgboost (agg_+_subset)
    model_plain: XGBoost (agg_+_subset)
    value: 0.5961
    std: 0.0012
    paper_value: 0.5961
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
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 29
    true_value: 0.5961
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5961
    sort_std: 0.0012
    is_best: false
  - model: XGBoost (feature_agg)
    model_key: xgboost (feature_agg)
    model_plain: XGBoost (feature_agg)
    value: 0.6047
    std: 0.0009
    paper_value: 0.6047
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 30
    true_value: 0.6047
    true_std: 0.0009
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6047
    sort_std: 0.0009
    is_best: false
  - model: XGBoost (sum_+_i)
    model_key: xgboost (sum_+_i)
    model_plain: XGBoost (sum_+_i)
    value: 0.6509
    std: 0.0002
    paper_value: 0.6509
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 31
    true_value: 0.6509
    true_std: 0.0002
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6509
    sort_std: 0.0002
    is_best: false
  - model: XGBoost (sum_+_subset)
    model_key: xgboost (sum_+_subset)
    model_plain: XGBoost (sum_+_subset)
    value: 0.6948
    std: 0.0
    paper_value: 0.6948
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 32
    true_value: 0.6948
    true_std: 0.0
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6948
    sort_std: 0.0
    is_best: false
  - model: XGBoost (feature_sum)
    model_key: xgboost (feature_sum)
    model_plain: XGBoost (feature_sum)
    value: 0.7634
    std: 0.0006
    paper_value: 0.7634
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 33
    true_value: 0.7634
    true_std: 0.0006
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7634
    sort_std: 0.0006
    is_best: false
  - model: XGBoost (all_invariants)
    model_key: xgboost (all_invariants)
    model_plain: XGBoost (all_invariants)
    value: 0.794
    std: 0.0001
    paper_value: 0.794
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 34
    true_value: 0.794
    true_std: 0.0001
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.0001
    is_best: false
  - model: XGBoost (invariants_subset)
    model_key: xgboost (invariants_subset)
    model_plain: XGBoost (invariants_subset)
    value: 0.8919
    std: 0.0003
    paper_value: 0.8919
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 35
    true_value: 0.8919
    true_std: 0.0003
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8919
    sort_std: 0.0003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: ogbg-molhiv
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.862
    sort_std: 0.002
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.858
    sort_std: 0.002
    is_best: true
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.855
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.855
    sort_std: 0.002
    is_best: false
  - model: Uni-Mol
    model_key: uni-mol
    model_plain: Uni-Mol
    value: 0.808
    std: 0.003
    paper_value: 0.808
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.808
    sort_std: 0.003
    is_best: false
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.806
    std: 0.009
    paper_value: 0.806
    paper_std: 0.009
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.806
    sort_std: 0.009
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.799
    std: 0.007
    paper_value: 0.799
    paper_std: 0.007
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.799
    sort_std: 0.007
    is_best: false
  - model: N-Gram_XGB
    model_key: n-gram_xgb
    model_plain: N-Gram_XGB
    value: 0.787
    std: 0.004
    paper_value: 0.787
    paper_std: 0.004
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.787
    sort_std: 0.004
    is_best: false
  - model: MolCLR
    model_key: molclr
    model_plain: MolCLR
    value: 0.781
    std: 0.005
    paper_value: 0.781
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.781
    sort_std: 0.005
    is_best: false
  - model: N-Gram_RF
    model_key: n-gram_rf
    model_plain: N-Gram_RF
    value: 0.772
    std: 0.001
    paper_value: 0.772
    paper_std: 0.001
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.772
    sort_std: 0.001
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.771
    std: 0.005
    paper_value: 0.771
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.771
    sort_std: 0.005
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.77
    std: 0.012
    paper_value: 0.77
    paper_std: 0.012
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.77
    sort_std: 0.012
    is_best: false
  - model: agg + I
    model_key: agg + i
    model_plain: agg + I
    value: 0.7695
    std: 0.0034
    paper_value: 0.7695
    paper_std: 0.0034
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.7695
    sort_std: 0.0034
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.757
    std: 0.014
    paper_value: 0.757
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.757
    sort_std: 0.014
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.682
    std: 0.011
    paper_value: 0.682
    paper_std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.682
    sort_std: 0.011
    is_best: false
  - model: GROVER_base
    model_key: grover_base
    model_plain: GROVER_base
    value: 0.625
    std: 0.009
    paper_value: 0.625
    paper_std: 0.009
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al.
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: null
    sort_value: 0.625
    sort_std: 0.009
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: OGB
  datasets:
  - *id003
- benchmark: MoleculeNet
  datasets:
  - *id004
  - *id005
- benchmark: GraphBench
  datasets:
  - *id006
- benchmark: Quantum Chemistry
  datasets:
  - *id007
main_figure: /figures/2605.06462/main_figure.png
---

