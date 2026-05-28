---
title: 'What Expressivity Theory Misses: Message Passing Complexity for GNNs'
arxiv_id: '2509.01254'
source_url: ''
authors: []
published_date: Sep 2025
published_date_iso: 2025-09
abstract: 'Expressivity theory, characterizing which graphs a GNN can distinguish,
  has become the predominant framework for analyzing GNNs, with new models striving
  for higher expressivity. However, we argue that this focus is misguided: First,
  higher expressivity is not necessary for most real-world tasks as these tasks rarely
  require expressivity beyond the basic WL test. Second, expressivity theory''s binary
  characterization and idealized assumptions fail to reflect GNNs'' practical capabilities.
  To overcome these limitations, we propose Message Passing Complexity: a continuous
  measure that quantifies the difficulty for a GNN architecture to solve a given task
  through message passing. captures practical limitations like over-squashing while
  preserving theoretical impossibility results from expressivity theory, effectively
  narrowing the gap between theory and practice. Through extensive validation on fundamental
  GNN tasks, we show that ''s theoretical predictions correlate with empirical performance,
  successfully explaining architectural successes and failures. Thereby, advances
  beyond expressivity theory to provide a more powerful and nuanced framework for
  understanding and improving GNN architectures.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CIN
mrr: 0.1429
adjusted_mrr: 0.0476
mrr_dataset_count: 1
benchmark_categories:
- Classic
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
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
    value: 0.077
    std: null
    paper_value: 0.077
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055
    value_note: ''
    paper_rank: 131
    rank_delta: 124
    rank_delta_abs: 124
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.077
    std: null
    paper_value: 0.077
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055
    value_note: ''
    paper_rank: 131
    rank_delta: 124
    rank_delta_abs: 124
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.53
    std: null
    paper_value: 0.53
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.465
    value_note: ''
    paper_rank: 293
    rank_delta: 218
    rank_delta_abs: 218
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.37
    std: null
    paper_value: 0.37
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.294
    value_note: ''
    paper_rank: 285
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: FragNet
    model_key: fragnet
    model_plain: FragNet
    value: 0.078
    std: null
    paper_value: 0.078
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 144
    true_value: 0.078
    true_std: null
    value_gap_source_arxiv: '2509.01254'
    value_gap_source_title: 'What Expressivity Theory Misses: Message Passing Complexity
      for GNNs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.078
    sort_std: null
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.12
    std: null
    paper_value: 0.12
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 188
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01899999999999999
    value_note: ''
    paper_rank: 206
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4
    std: null
    paper_value: 0.4
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 214
    true_value: 0.126
    true_std: 0.003
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.274
    value_note: ''
    paper_rank: 288
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.126
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
single_proposed_model: CIN
main_figure: /figures/2509.01254/main_figure.png
---

