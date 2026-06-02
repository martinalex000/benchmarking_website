---
title: 'What Expressivity Theory Misses: Message Passing Complexity for GNNs'
arxiv_id: '2509.01254'
source_url: ''
authors: []
published_date: Sep 2025
published_date_iso: 2025-09
published_venue: ''
abstract: 'Expressivity theory, characterizing which graphs a GNN can distinguish,
  has become the predominant framework for analyzing GNNs, with new models striving
  for higher expressivity. However, we argue that this focus is misguided: First,
  higher expressivity is not necessary for most real-world tasks as these tasks rarely
  require expressivity beyond the basic WL test. Second, expressivity theory''s binary
  characterization and idealized assumptions fail to reflect GNNs'' practical capabilities.
  To overcome these limitations, we propose Message Passing Complexity (MPC): a continuous
  measure that quantifies the difficulty for a GNN architecture to solve a given task
  through message passing. MPC captures practical limitations like over-squashing
  while preserving theoretical impossibility results from expressivity theory, effectively
  narrowing the gap between theory and practice. Through extensive validation on fundamental
  GNN tasks, we show that MPC''s theoretical predictions correlate with empirical
  performance, successfully explaining architectural successes and failures. Thereby,
  MPC advances beyond expressivity theory to provide a more powerful and nuanced framework
  for understanding and improving GNN architectures.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
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
    published_venue: null
    global_rank: 2
    true_value: 0.006
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.394
    value_note: ''
    paper_rank: 149
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.006
    sort_std: null
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
    published_venue: null
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.516
    value_note: ''
    paper_rank: 153
    rank_delta: 150
    rank_delta_abs: 150
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
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
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.021
    sort_std: 0.002
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
    published_venue: null
    global_rank: 10
    true_value: 0.0237
    true_std: 0.0
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0543
    value_note: ''
    paper_rank: 57
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.0237
    sort_std: 0.0
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
    published_venue: null
    global_rank: 11
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.346
    value_note: ''
    paper_rank: 146
    rank_delta: 135
    rank_delta_abs: 135
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
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
    published_venue: null
    global_rank: 17
    true_value: 0.027
    true_std: 0.007
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 54
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.027
    sort_std: 0.007
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
    published_venue: null
    global_rank: 73
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01899999999999999
    value_note: ''
    paper_rank: 84
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
---

