---
title: Unitary convolutions for learning on graphs and groups
arxiv_id: '2410.05499'
source_url: ''
authors: []
published_date: Oct 7, 2024
published_date_iso: '2024-10-07'
abstract: Data with geometric structure is ubiquitous in machine learning often arising
  from fundamental symmetries in a domain, such as permutation-invariance in graphs
  and translation-invariance in images. Group-convolutional architectures, which encode
  symmetries as inductive bias, have shown great success in applications, but can
  suffer from instabilities as their depth increases and often struggle to learn long
  range dependencies in data. For instance, graph neural networks experience instability
  due to the convergence of node representations (over-smoothing), which can occur
  after only a few iterations of message-passing, reducing their effectiveness in
  downstream tasks. Here, we propose and study unitary group convolutions, which allow
  for deeper networks that are more stable during training. The main focus of the
  paper are graph neural networks, where we show that unitary graph convolutions provably
  avoid over-smoothing. Our experimental results confirm that unitary graph convolutional
  networks achieve competitive performance on benchmark datasets compared to state-of-the-art
  graph neural networks. We complement our analysis of the graph domain with the study
  of general unitary convolutions and analyze their role in enhancing stability in
  general group convolutional architectures.
codebase_url: ''
extraction_model: Kimi-K2.6
has_results: true
paper_type: method
proposed_models:
- UniGCN
- Lie UniGCN
- Unitary GCN
- Lie Unitary GCN
- Wide Unitary GCN
mrr: 0.037
adjusted_mrr: 0.037
mrr_dataset_count: 6
benchmark_categories:
- Heterophilic Graphs
- LRGB
- TU Dortmund
- Heterogeneous Graph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id002
  dataset: Amazon-ratings
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.5592
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.5592
    sort_std: 0.0043
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.5534
    std: 0.0074
    paper_value: 0.5534
    paper_std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.5534
    sort_std: 0.0074
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5496
    std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.5496
    sort_std: 0.0222
    is_best: true
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5363
    std: 0.0039
    paper_value: 0.5363
    paper_std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 20
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: Lie Unitary GCN
    model_key: lie unitary gcn
    model_plain: Lie Unitary GCN
    value: 0.5235
    std: 0.0026
    paper_value: 0.5235
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.5235
    sort_std: 0.0026
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5117
    std: 0.0066
    paper_value: 0.5117
    paper_std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 43
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4909
    std: 0.0063
    paper_value: 0.4909
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 2
    sort_value: 0.4909
    sort_std: 0.0063
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.487
    std: 0.0063
    paper_value: 0.487
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 17
    sort_value: 0.487
    sort_std: 0.0063
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.313
    std: 0.011
    paper_value: 0.313
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.293
    value_note: ''
    paper_rank: 82
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.255
    std: 0.012
    paper_value: 0.255
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 17
    true_value: 0.563
    true_std: 0.036
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.30799999999999994
    value_note: ''
    paper_rank: 121
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.036
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.268
    std: 0.012
    paper_value: 0.268
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 27
    true_value: 0.495
    true_std: 0.089
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22699999999999998
    value_note: ''
    paper_rank: 117
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.495
    sort_std: 0.089
    is_best: false
  - model: Wide Unitary GCN
    model_key: wide unitary gcn
    model_plain: Wide Unitary GCN
    value: 0.421
    std: 0.015
    paper_value: 0.421
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 42
    true_value: 0.421
    true_std: 0.015
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.421
    sort_std: 0.015
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.415
    std: 0.016
    paper_value: 0.415
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 45
    true_value: 0.415
    true_std: 0.016
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.415
    sort_std: 0.016
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: IMDB
  rows:
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.7308
    std: 0.0124
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7308
    sort_std: 0.0124
    is_best: true
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.7205
    std: 0.0115
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7205
    sort_std: 0.0115
    is_best: true
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.7148
    std: 0.0103
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7148
    sort_std: 0.0103
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.69
    std: 0.01
    paper_value: 0.69
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.69
    sort_std: 0.01
    is_best: false
  - model: Wide Unitary GCN
    model_key: wide unitary gcn
    model_plain: Wide Unitary GCN
    value: 0.624
    std: 0.013
    paper_value: 0.624
    paper_std: 0.013
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.624
    sort_std: 0.013
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.612
    std: 0.014
    paper_value: 0.612
    paper_std: 0.014
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.612
    sort_std: 0.014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.493
    std: 0.008
    paper_value: 0.493
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.493
    sort_std: 0.008
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.47
    std: 0.011
    paper_value: 0.47
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.47
    sort_std: 0.011
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id008
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.98
    std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: Wide Unitary GCN
    model_key: wide unitary gcn
    model_plain: Wide Unitary GCN
    value: 0.871
    std: 0.035
    paper_value: 0.871
    paper_std: 0.035
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.871
    sort_std: 0.035
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.868
    std: 0.033
    paper_value: 0.868
    paper_std: 0.033
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: null
    sort_value: 0.868
    sort_std: 0.033
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.757
    std: 0.036
    paper_value: 0.757
    paper_std: 0.036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 28
    sort_value: 0.757
    sort_std: 0.036
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.688
    std: 0.024
    paper_value: 0.688
    paper_std: 0.024
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 22
    sort_value: 0.688
    sort_std: 0.024
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.685
    std: 0.028
    paper_value: 0.685
    paper_std: 0.028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 117
    sort_value: 0.685
    sort_std: 0.028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9906999999999999
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango<sub>GPS</sub>
    model_key: tango\textsubscript{gps}
    model_plain: TangoGPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
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
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8975
    std: 0.0052
    paper_value: 0.8975
    paper_std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 5
    true_value: 0.9786
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08110000000000006
    value_note: ''
    paper_rank: 76
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.9786
    sort_std: 0.0024
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9201
    std: 0.0068
    paper_value: 0.9201
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05719999999999992
    value_note: ''
    paper_rank: 50
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: Lie Unitary GCN
    model_key: lie unitary gcn
    model_plain: Lie Unitary GCN
    value: 0.9611
    std: 0.001
    paper_value: 0.9611
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 17
    true_value: 0.9611
    true_std: 0.001
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9611
    sort_std: 0.001
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.9427
    std: 0.0058
    paper_value: 0.9427
    paper_std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 28
    true_value: 0.9427
    true_std: 0.0058
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9427
    sort_std: 0.0058
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9351
    std: 0.0057
    paper_value: 0.9351
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 39
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9185
    std: 0.0076
    paper_value: 0.9185
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 52
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.854
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 1
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.807
    std: 0.039
    metric: Accuracy
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
    global_rank: 2
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.726
    std: 0.008
    paper_value: 0.726
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 28
    true_value: 0.7634
    true_std: 0.0166
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03739999999999999
    value_note: ''
    paper_rank: 132
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.7634
    sort_std: 0.0166
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.697
    std: 0.008
    paper_value: 0.697
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06500000000000006
    value_note: ''
    paper_rank: 181
    rank_delta: 149
    rank_delta_abs: 149
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.706
    std: 0.007
    paper_value: 0.706
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05400000000000005
    value_note: ''
    paper_rank: 171
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: Wide Unitary GCN
    model_key: wide unitary gcn
    model_plain: Wide Unitary GCN
    value: 0.756
    std: 0.01
    paper_value: 0.756
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 49
    true_value: 0.756
    true_std: 0.01
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.01
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.751
    std: 0.013
    paper_value: 0.751
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 65
    true_value: 0.751
    true_std: 0.013
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.4588
    std: 0.0079
    paper_value: 0.4588
    paper_std: 0.0079
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 6
    true_value: 0.4588
    true_std: 0.0079
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4588
    sort_std: 0.0079
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.444
    std: 0.0065
    paper_value: 0.444
    paper_std: 0.0065
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 9
    true_value: 0.444
    true_std: 0.0065
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.444
    sort_std: 0.0065
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.388
    std: 0.004
    paper_value: 0.388
    paper_std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0383
    value_note: ''
    paper_rank: 42
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.4263
    sort_std: 0.0057
    is_best: false
  - model: Lie UniGCN
    model_key: lie unigcn
    model_plain: Lie UniGCN
    value: 0.4005
    std: 0.0067
    paper_value: 0.4005
    paper_std: 0.0067
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 33
    true_value: 0.4005
    true_std: 0.0067
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4005
    sort_std: 0.0067
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.396
    std: 0.0027
    paper_value: 0.396
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015000000000000013
    value_note: global 0.3975 within std
    paper_rank: 37
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2078
    std: 0.0031
    paper_value: 0.2078
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1682
    value_note: ''
    paper_rank: 95
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: UniGCN
    model_key: unigcn
    model_plain: UniGCN
    value: 0.3516
    std: 0.007
    paper_value: 0.3516
    paper_std: 0.007
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 57
    true_value: 0.3516
    true_std: 0.007
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3516
    sort_std: 0.007
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.3314
    std: 0.0024
    paper_value: 0.3314
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 59
    true_value: 0.3314
    true_std: 0.0024
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3314
    sort_std: 0.0024
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2718
    std: 0.0054
    paper_value: 0.2718
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 80
    true_value: 0.2718
    true_std: 0.0054
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2718
    sort_std: 0.0054
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: Questions
  rows:
  - model: IM-CO-GNN(Σ,Σ)
    model_key: im-co-gnn(σ,σ)
    model_plain: IM-CO-GNN(Σ,Σ)
    value: 0.8049
    std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_display: May 2025
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.8049
    sort_std: 0.0092
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8039000000000001
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
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
    global_rank: 2
    sort_value: 0.8039000000000001
    sort_std: 0.0104
    is_best: true
  - model: Tango<sub>GatedGCN</sub>
    model_key: tango\textsubscript{gatedgcn}
    model_plain: TangoGatedGCN
    value: 0.8039
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    global_rank: 3
    sort_value: 0.8039
    sort_std: 0.0104
    is_best: true
  - model: Lie Unitary GCN
    model_key: lie unitary gcn
    model_plain: Lie Unitary GCN
    value: 0.8001
    std: 0.0043
    paper_value: 0.8001
    paper_std: 0.0043
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 8
    true_value: 0.8001
    true_std: 0.0043
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8001
    sort_std: 0.0043
    is_best: true
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.7921
    std: 0.0079
    paper_value: 0.7921
    paper_std: 0.0079
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 12
    true_value: 0.7921
    true_std: 0.0079
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7921
    sort_std: 0.0079
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7609
    std: 0.0127
    paper_value: 0.7609
    paper_std: 0.0127
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 13
    true_value: 0.7902
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029299999999999993
    value_note: ''
    paper_rank: 46
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7902
    sort_std: 0.006
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.7795
    std: 0.0068
    paper_value: 0.7795
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 23
    true_value: 0.7795000000000001
    true_std: 0.0068000000000000005
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795000000000001
    sort_std: 0.0068000000000000005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7743
    std: 0.012
    paper_value: 0.7743
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.7795 within std
    paper_rank: 31
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7795
    sort_std: 0.0051
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7644
    std: 0.0062
    paper_value: 0.7644
    paper_std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 46
    true_value: 0.7644
    true_std: 0.0062
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.0062
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Roman-empire
  rows:
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9292
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9292
    sort_std: 0.0036
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9266
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9266
    sort_std: 0.006
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9262999999999999
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9262999999999999
    sort_std: 0.005
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7369
    std: 0.0074
    paper_value: 0.7369
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17579999999999996
    value_note: ''
    paper_rank: 79
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8087
    std: 0.003
    paper_value: 0.8087
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09760000000000002
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.8721
    std: 0.0076
    paper_value: 0.8721
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 37
    true_value: 0.8721
    true_std: 0.0076
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8721
    sort_std: 0.0076
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8651
    std: 0.0073
    paper_value: 0.8651
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 44
    true_value: 0.8651000000000001
    true_std: 0.0073
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8651000000000001
    sort_std: 0.0073
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8574
    std: 0.0067
    paper_value: 0.8574
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 47
    true_value: 0.8574
    true_std: 0.0067
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8574
    sort_std: 0.0067
    is_best: false
  - model: Lie Unitary GCN
    model_key: lie unitary gcn
    model_plain: Lie Unitary GCN
    value: 0.855
    std: 0.0022
    paper_value: 0.855
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 50
    true_value: 0.855
    true_std: 0.0022
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.855
    sort_std: 0.0022
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA<sub>GCN</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMAGCN
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: Lie Unitary GCN
    model_key: lie unitary gcn
    model_plain: Lie Unitary GCN
    value: 0.8518
    std: 0.0043
    paper_value: 0.8518
    paper_std: 0.0043
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 17
    true_value: 0.8518
    true_std: 0.0043
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8518
    sort_std: 0.0043
    is_best: true
  - model: Unitary GCN
    model_key: unitary gcn
    model_plain: Unitary GCN
    value: 0.8483
    std: 0.0068
    paper_value: 0.8483
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 26
    true_value: 0.8483
    true_std: 0.0068
    value_gap_source_arxiv: '2410.05499'
    value_gap_source_title: Unitary convolutions for learning on graphs and groups
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8483
    sort_std: 0.0068
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8364
    std: 0.0067
    paper_value: 0.8364
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 44
    true_value: 0.838
    true_std: 0.0034
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.8380 within std
    paper_rank: 49
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.837
    std: 0.0047
    paper_value: 0.837
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 48
    true_value: 0.8370000000000001
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8370000000000001
    sort_std: 0.004699999999999999
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8323
    std: 0.0064
    paper_value: 0.8323
    paper_std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 55
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8243
    std: 0.0044
    paper_value: 0.8243
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    variant_inference_reason: ''
    date: Oct 7, 2024
    date_display: Oct 2024
    date_iso: '2024-10-07'
    global_rank: 61
    true_value: 0.8243
    true_std: 0.0044
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: LRGB
  datasets:
  - *id006
- benchmark: TU Dortmund
  datasets:
  - *id007
  - *id008
  - *id009
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id010
main_figure: /figures/2410.05499/main_figure.png
---

