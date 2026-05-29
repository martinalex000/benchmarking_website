---
title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
arxiv_id: '2302.06835'
source_url: ''
authors: []
published_date: Feb 14, 2023
published_date_iso: '2023-02-14'
abstract: Message passing graph neural networks (GNNs) are a popular learning architectures
  for graph-structured data. However, one problem GNNs experience is oversquashing,
  where a GNN has difficulty sending information between distant nodes. Understanding
  and mitigating oversquashing has recently received significant attention from the
  research community. In this paper, we continue this line of work by analyzing oversquashing
  through the lens of the effective resistance between nodes in the input graph. Effective
  resistance intuitively captures the ``strength'' of connection between two nodes
  by paths in the graph, and has a rich literature spanning many areas of graph theory.
  We propose to use total effective resistance as a bound of the total amount of oversquashing
  in a graph and provide theoretical justification for its use. We further develop
  an algorithm to identify edges to be added to an input graph to minimize the total
  effective resistance, thereby alleviating oversquashing. We provide empirical evidence
  of the effectiveness of our total effective resistance based rewiring strategies
  for improving the performance of GNNs.
codebase_url: https://github.com/blackmit/gtr_rewiring
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id003
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.8672
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: SE2P-C3
    model_key: se2p-c3
    model_plain: SE2P-C3
    value: 0.835
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.835
    sort_std: 0.017
    is_best: true
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7745
    std: 0.0039
    paper_value: 0.7745
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 25
    true_value: 0.7745
    true_std: 0.0039
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7745
    sort_std: 0.0039
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.772
    std: 0.0038
    paper_value: 0.772
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 30
    true_value: 0.772
    true_std: 0.0038
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.0038
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.7648
    std: 0.0039
    paper_value: 0.7648
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 32
    true_value: 0.7648
    true_std: 0.0039
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7648
    sort_std: 0.0039
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.7554
    std: 0.0032
    paper_value: 0.7554
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 34
    true_value: 0.7554
    true_std: 0.0032
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7554
    sort_std: 0.0032
    is_best: false
  - model: R-GIN + Last FA
    model_key: r-gin + last fa
    model_plain: R-GIN + Last FA
    value: 0.7543
    std: 0.0049
    paper_value: 0.7543
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 36
    true_value: 0.7543
    true_std: 0.0049
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7543
    sort_std: 0.0049
    is_best: false
  - model: R-GIN + Every FA
    model_key: r-gin + every fa
    model_plain: R-GIN + Every FA
    value: 0.7543
    std: 0.0048
    paper_value: 0.7543
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 37
    true_value: 0.7543
    true_std: 0.0048
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7543
    sort_std: 0.0048
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.7434
    std: 0.0041
    paper_value: 0.7434
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 40
    true_value: 0.7434
    true_std: 0.0041
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7434
    sort_std: 0.0041
    is_best: false
  - model: R-GIN + DIGL
    model_key: r-gin + digl
    model_plain: R-GIN + DIGL
    value: 0.5471
    std: 0.0042
    paper_value: 0.5471
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 55
    true_value: 0.5471
    true_std: 0.0042
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5471
    sort_std: 0.0042
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.545
    std: 0.0041
    paper_value: 0.545
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 56
    true_value: 0.545
    true_std: 0.0041
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.545
    sort_std: 0.0041
    is_best: false
  - model: GCN + Every FA
    model_key: gcn + every fa
    model_plain: GCN + Every FA
    value: 0.518
    std: 0.0042
    paper_value: 0.518
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 57
    true_value: 0.518
    true_std: 0.0042
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.518
    sort_std: 0.0042
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.3384
    std: 0.0058
    paper_value: 0.3384
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 58
    true_value: 0.3384
    true_std: 0.0058
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3384
    sort_std: 0.0058
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.3378
    std: 0.0049
    paper_value: 0.3378
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 59
    true_value: 0.3378
    true_std: 0.0049
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3378
    sort_std: 0.0049
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.3345
    std: 0.0047
    paper_value: 0.3345
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 60
    true_value: 0.3345
    true_std: 0.0047
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3345
    sort_std: 0.0047
    is_best: false
  - model: GCN + Last FA
    model_key: gcn + last fa
    model_plain: GCN + Last FA
    value: 0.3332
    std: 0.0044
    paper_value: 0.3332
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 61
    true_value: 0.3332
    true_std: 0.0044
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3332
    sort_std: 0.0044
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.7995
    std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.7196
    std: 0.0069
    paper_value: 0.7196
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 49
    true_value: 0.7196
    true_std: 0.0069
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7196
    sort_std: 0.0069
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7149
    std: 0.0093
    paper_value: 0.7149
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 53
    true_value: 0.7149
    true_std: 0.0093
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7149
    sort_std: 0.0093
    is_best: false
  - model: R-GIN + Every FA
    model_key: r-gin + every fa
    model_plain: R-GIN + Every FA
    value: 0.7148
    std: 0.0088
    paper_value: 0.7148
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 54
    true_value: 0.7148
    true_std: 0.0088
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.0088
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.7021
    std: 0.0081
    paper_value: 0.7021
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 57
    true_value: 0.7021
    true_std: 0.0081
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7021
    sort_std: 0.0081
    is_best: false
  - model: R-GIN + Last FA
    model_key: r-gin + last fa
    model_plain: R-GIN + Last FA
    value: 0.6971
    std: 0.0103
    paper_value: 0.6971
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 59
    true_value: 0.6971
    true_std: 0.0103
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6971
    sort_std: 0.0103
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.6889
    std: 0.0087
    paper_value: 0.6889
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 60
    true_value: 0.6889
    true_std: 0.0087
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6889
    sort_std: 0.0087
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.6509
    std: 0.0093
    paper_value: 0.6509
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 63
    true_value: 0.6509
    true_std: 0.0093
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6509
    sort_std: 0.0093
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.6439
    std: 0.0091
    paper_value: 0.6439
    paper_std: 0.0091
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 64
    true_value: 0.6439
    true_std: 0.0091
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6439
    sort_std: 0.0091
    is_best: false
  - model: R-GIN + DIGL
    model_key: r-gin + digl
    model_plain: R-GIN + DIGL
    value: 0.6393
    std: 0.0095
    paper_value: 0.6393
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 65
    true_value: 0.6393
    true_std: 0.0095
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6393
    sort_std: 0.0095
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.4977
    std: 0.0082
    paper_value: 0.4977
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 66
    true_value: 0.4977
    true_std: 0.0082
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4977
    sort_std: 0.0082
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.4966
    std: 0.0086
    paper_value: 0.4966
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 67
    true_value: 0.4966
    true_std: 0.0086
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4966
    sort_std: 0.0086
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.494
    std: 0.009
    paper_value: 0.494
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 68
    true_value: 0.494
    true_std: 0.009
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.494
    sort_std: 0.009
    is_best: false
  - model: GCN + Last FA
    model_key: gcn + last fa
    model_plain: GCN + Last FA
    value: 0.4898
    std: 0.0095
    paper_value: 0.4898
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 69
    true_value: 0.4898
    true_std: 0.0095
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4898
    sort_std: 0.0095
    is_best: false
  - model: GCN + Every FA
    model_key: gcn + every fa
    model_plain: GCN + Every FA
    value: 0.4817
    std: 0.008
    paper_value: 0.4817
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 70
    true_value: 0.4817
    true_std: 0.008
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4817
    sort_std: 0.008
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: MUTAG
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.939
    std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.939
    sort_std: 0.04
    is_best: true
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.9263
    std: 0.0421
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: Jan 2019
    date_display: Jan 2019
    date_iso: 2019-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9263
    sort_std: 0.0421
    is_best: true
  - model: PS
    model_key: ps
    model_plain: PS
    value: 0.926
    std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.926
    sort_std: 0.042
    is_best: true
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.8615
    std: 0.0149
    paper_value: 0.8615
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 24
    true_value: 0.8615
    true_std: 0.0149
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8615
    sort_std: 0.0149
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.861
    std: 0.0176
    paper_value: 0.861
    paper_std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 25
    true_value: 0.861
    true_std: 0.0176
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.861
    sort_std: 0.0176
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.855
    std: 0.0147
    paper_value: 0.855
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 29
    true_value: 0.855
    true_std: 0.0147
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.855
    sort_std: 0.0147
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.8305
    std: 0.0144
    paper_value: 0.8305
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 44
    true_value: 0.8305
    true_std: 0.0144
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8305
    sort_std: 0.0144
    is_best: false
  - model: R-GIN + Every FA
    model_key: r-gin + every fa
    model_plain: R-GIN + Every FA
    value: 0.8305
    std: 0.0152
    paper_value: 0.8305
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 45
    true_value: 0.8305
    true_std: 0.0152
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8305
    sort_std: 0.0152
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.827
    std: 0.0178
    paper_value: 0.827
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 47
    true_value: 0.827
    true_std: 0.0178
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.0178
    is_best: false
  - model: R-GIN + DIGL
    model_key: r-gin + digl
    model_plain: R-GIN + DIGL
    value: 0.8145
    std: 0.0149
    paper_value: 0.8145
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 51
    true_value: 0.8145
    true_std: 0.0149
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8145
    sort_std: 0.0149
    is_best: false
  - model: R-GIN + Last FA
    model_key: r-gin + last fa
    model_plain: R-GIN + Last FA
    value: 0.806
    std: 0.0164
    paper_value: 0.806
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 52
    true_value: 0.806
    true_std: 0.0164
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.806
    sort_std: 0.0164
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.8
    std: 0.0157
    paper_value: 0.8
    paper_std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 53
    true_value: 0.8
    true_std: 0.0157
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.0157
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.797
    std: 0.0215
    paper_value: 0.797
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 54
    true_value: 0.797
    true_std: 0.0215
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.0215
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.7215
    std: 0.0244
    paper_value: 0.7215
    paper_std: 0.0244
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 63
    true_value: 0.7215
    true_std: 0.0244
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7215
    sort_std: 0.0244
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7105
    std: 0.0187
    paper_value: 0.7105
    paper_std: 0.0187
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 64
    true_value: 0.7105
    true_std: 0.0187
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7105
    sort_std: 0.0187
    is_best: false
  - model: GCN + Every FA
    model_key: gcn + every fa
    model_plain: GCN + Every FA
    value: 0.7045
    std: 0.0196
    paper_value: 0.7045
    paper_std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 65
    true_value: 0.7045
    true_std: 0.0196
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7045
    sort_std: 0.0196
    is_best: false
  - model: GCN + Last FA
    model_key: gcn + last fa
    model_plain: GCN + Last FA
    value: 0.7005
    std: 0.0203
    paper_value: 0.7005
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 66
    true_value: 0.7005
    true_std: 0.0203
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7005
    sort_std: 0.0203
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: REDDIT-BINARY
  rows:
  - model: PEs
    model_key: pes
    model_plain: PEs
    value: 0.945
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.918
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.918
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.016
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.9094
    std: 0.0047
    paper_value: 0.9094
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 5
    true_value: 0.9094
    true_std: 0.0047
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9094
    sort_std: 0.0047
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.9041
    std: 0.0041
    paper_value: 0.9041
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 6
    true_value: 0.9041
    true_std: 0.0041
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9041
    sort_std: 0.0041
    is_best: false
  - model: R-GIN + Last FA
    model_key: r-gin + last fa
    model_plain: R-GIN + Last FA
    value: 0.9
    std: 0.0065
    paper_value: 0.9
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 7
    true_value: 0.9
    true_std: 0.0065
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: 0.0065
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.8797
    std: 0.0056
    paper_value: 0.8797
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 12
    true_value: 0.8797
    true_std: 0.0056
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8797
    sort_std: 0.0056
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.8683
    std: 0.0052
    paper_value: 0.8683
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 15
    true_value: 0.8683
    true_std: 0.0052
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8683
    sort_std: 0.0052
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.8018
    std: 0.006
    paper_value: 0.8018
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 17
    true_value: 0.8018
    true_std: 0.006
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8018
    sort_std: 0.006
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.7604
    std: 0.0078
    paper_value: 0.7604
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 18
    true_value: 0.7604
    true_std: 0.0078
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7604
    sort_std: 0.0078
    is_best: false
  - model: R-GIN + DIGL
    model_key: r-gin + digl
    model_plain: R-GIN + DIGL
    value: 0.7443
    std: 0.0072
    paper_value: 0.7443
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 19
    true_value: 0.7443
    true_std: 0.0072
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7443
    sort_std: 0.0072
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.7033
    std: 0.0072
    paper_value: 0.7033
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 20
    true_value: 0.7033
    true_std: 0.0072
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7033
    sort_std: 0.0072
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.6862
    std: 0.0085
    paper_value: 0.6862
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 21
    true_value: 0.6862
    true_std: 0.0085
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6862
    sort_std: 0.0085
    is_best: false
  - model: GCN + Last FA
    model_key: gcn + last fa
    model_plain: GCN + Last FA
    value: 0.6849
    std: 0.0095
    paper_value: 0.6849
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 22
    true_value: 0.6849
    true_std: 0.0095
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6849
    sort_std: 0.0095
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.6826
    std: 0.011
    paper_value: 0.6826
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 23
    true_value: 0.6826
    true_std: 0.011
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6826
    sort_std: 0.011
    is_best: false
  - model: R-GIN + Every FA
    model_key: r-gin + every fa
    model_plain: R-GIN + Every FA
    value: 0.5686
    std: 0.0094
    paper_value: 0.5686
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 24
    true_value: 0.5686
    true_std: 0.0094
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5686
    sort_std: 0.0094
    is_best: false
  - model: GCN + Every FA
    model_key: gcn + every fa
    model_plain: GCN + Every FA
    value: 0.4849
    std: 0.0104
    paper_value: 0.4849
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 14, 2023
    date_display: Feb 2023
    date_iso: '2023-02-14'
    global_rank: 25
    true_value: 0.4849
    true_std: 0.0104
    value_gap_source_arxiv: '2302.06835'
    value_gap_source_title: Understanding Oversquashing in GNNs through the Lens of
      Effective Resistance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4849
    sort_std: 0.0104
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
main_figure: /figures/2302.06835/main_figure.png
---

