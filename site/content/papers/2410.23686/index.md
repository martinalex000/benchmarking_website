---
title: Towards Dynamic Message Passing on Graphs
arxiv_id: '2410.23686'
source_url: ''
authors: []
published_date: Oct 31, 2024
published_date_iso: '2024-10-31'
published_venue: ''
abstract: Message passing plays a vital role in graph neural networks (GNNs) for effective
  feature learning. However, the over-reliance on input topology diminishes the efficacy
  of message passing and restricts the ability of GNNs. Despite efforts to mitigate
  the reliance, existing study encounters message-passing bottlenecks or high computational
  expense problems, which invokes the demands for flexible message passing with low
  complexity. In this paper, we propose a novel dynamic message-passing mechanism
  for GNNs. It projects graph nodes and learnable pseudo nodes into a common space
  with measurable spatial relations between them. With nodes moving in the space,
  their evolving relations facilitate flexible pathway construction for a dynamic
  message-passing process. Associating pseudo nodes to input graphs with their measured
  relations, graph nodes can communicate with each other intermediately through pseudo
  nodes under linear complexity. We further develop a GNN model named $N^2$ based
  on our dynamic message-passing mechanism. $N^2$ employs a single recurrent layer
  to recursively generate the displacements of nodes and construct optimal dynamic
  pathways. Evaluation on eighteen benchmarks demonstrates the superior performance
  of $N^2$ over popular GNNs. $N^2$ successfully scales to large-scale benchmarks
  and requires significantly fewer parameters for graph classification with the shared
  recurrent layer.
codebase_url: https://github.com/sunjss/N2
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- novel dynamic message-passing mechanism
mrr: 0.3968
adjusted_mrr: 0.3968
mrr_dataset_count: 6
benchmark_categories:
- TU Dortmund
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id004
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.8672
    std: 0.0162
    paper_value: 0.8672
    paper_std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 1
    true_value: 0.8672
    true_std: 0.0162
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    paper_value: 0.8615
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 2
    true_value: 0.8615
    true_std: 0.001
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: PXGL-GNN
    model_key: pxgl-gnn
    model_plain: PXGL-GNN
    value: 0.8396
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8396
    sort_std: 0.0159
    is_best: true
  - model: GFL-att
    model_key: gfl-att
    model_plain: GFL-att
    value: 0.8379
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_display: Oct 2019
    date_iso: 2019-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8379
    sort_std: 0.0039
    is_best: false
  - model: GNTK
    model_key: gntk
    model_plain: GNTK
    value: 0.836
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_display: May 2019
    date_iso: 2019-05
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.836
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8059
    std: 0.0027
    paper_value: 0.8059
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 16
    true_value: 0.826
    true_std: 0.022
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.020100000000000007
    value_note: global 0.8260 within std
    paper_rank: 70
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.022
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7819
    std: 0.0063
    paper_value: 0.7819
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 21
    true_value: 0.822
    true_std: 0.021
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040099999999999913
    value_note: ''
    paper_rank: 102
    rank_delta: 81
    rank_delta_abs: 81
    rank_delta_direction: worse
    sort_value: 0.822
    sort_std: 0.021
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.8213
    std: 0.0043
    paper_value: 0.8213
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying 2018
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 22
    true_value: 0.8213
    true_std: 0.0043
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8213
    sort_std: 0.0043
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.8128
    std: 0.0015
    paper_value: 0.8128
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 44
    true_value: 0.813
    true_std: 0.002
    value_gap_source_arxiv: '2603.02025'
    value_gap_source_title: arXiv:2603.02025
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00019999999999997797
    value_note: global 0.8130 within std
    paper_rank: 46
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.813
    sort_std: 0.002
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7758
    std: 0.0085
    paper_value: 0.7758
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 52
    true_value: 0.8118
    true_std: 0.0089
    value_gap_source_arxiv: '2205.15068'
    value_gap_source_title: Embedding Graphs on Grassmann Manifold
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03599999999999992
    value_note: ''
    paper_rank: 111
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.8118
    sort_std: 0.0089
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.809
    std: 0.008
    paper_value: 0.809
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 55
    true_value: 0.809
    true_std: 0.008
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.008
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.8074
    std: 0.0054
    paper_value: 0.8074
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 62
    true_value: 0.8074
    true_std: 0.0054
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8074
    sort_std: 0.0054
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.739
    std: 0.017
    paper_value: 0.739
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 88
    true_value: 0.797
    true_std: 0.017
    value_gap_source_arxiv: '2008.05089'
    value_gap_source_title: Quaternion Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05800000000000005
    value_note: ''
    paper_rank: 143
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.797
    sort_std: 0.017
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7803
    std: 0.0031
    paper_value: 0.7803
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 92
    true_value: 0.7926
    true_std: 0.0537
    value_gap_source_arxiv: '2205.15068'
    value_gap_source_title: Embedding Graphs on Grassmann Manifold
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.012299999999999978
    value_note: global 0.7926 within std
    paper_rank: 103
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.7926
    sort_std: 0.0537
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7727
    std: 0.0051
    paper_value: 0.7727
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 121
    true_value: 0.7727
    true_std: 0.0051
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7727
    sort_std: 0.0051
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.726
    std: 0.0215
    paper_value: 0.726
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert 2016
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 153
    true_value: 0.726
    true_std: 0.0215
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.0215
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: IMDB-BINARY
  rows:
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7326
    std: 0.0046
    paper_value: 0.7326
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 1
    true_value: 0.834
    true_std: 0.049
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10139999999999993
    value_note: ''
    paper_rank: 117
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.834
    sort_std: 0.049
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.83
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.83
    sort_std: 0.032
    is_best: true
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
    global_rank: 3
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
    global_rank: 4
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.7995
    std: 0.0246
    paper_value: 0.7995
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 5
    true_value: 0.7995
    true_std: 0.0246
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.7726
    std: 0.0027
    paper_value: 0.7726
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 16
    true_value: 0.7726
    true_std: 0.0027
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7726
    sort_std: 0.0027
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7314
    std: 0.007
    paper_value: 0.7314
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 21
    true_value: 0.7704
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038999999999999924
    value_note: ''
    paper_rank: 121
    rank_delta: 100
    rank_delta_abs: 100
    rank_delta_direction: worse
    sort_value: 0.7704
    sort_std: null
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.768
    std: 0.026
    paper_value: 0.768
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 23
    true_value: 0.768
    true_std: 0.026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.026
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7278
    std: 0.0086
    paper_value: 0.7278
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 27
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2110.09344'
    value_gap_source_title: 'ifMixup: Interpolating Graph Pair to Regularize Graph
      Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03420000000000001
    value_note: ''
    paper_rank: 143
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.688
    std: 0.045
    paper_value: 0.688
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 35
    true_value: 0.76
    true_std: 0.033
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07200000000000006
    value_note: ''
    paper_rank: 217
    rank_delta: 182
    rank_delta_abs: 182
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.033
    is_best: true
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7255
    std: 0.0128
    paper_value: 0.7255
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 59
    true_value: 0.7503
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.024799999999999933
    value_note: ''
    paper_rank: 146
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.7503
    sort_std: null
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7158
    std: 0.0095
    paper_value: 0.7158
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 65
    true_value: 0.747
    true_std: 0.0267
    value_gap_source_arxiv: '2406.08897'
    value_gap_source_title: Motif-driven Subgraph Structure Learning for Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031200000000000006
    value_note: ''
    paper_rank: 178
    rank_delta: 113
    rank_delta_abs: 113
    rank_delta_direction: worse
    sort_value: 0.747
    sort_std: 0.0267
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7412
    std: 0.0056
    paper_value: 0.7412
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 89
    true_value: 0.7412
    true_std: 0.0056
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7412
    sort_std: 0.0056
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7206
    std: 0.0064
    paper_value: 0.7206
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yuan et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 92
    true_value: 0.7406
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 162
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7406
    sort_std: null
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7348
    std: 0.0076
    paper_value: 0.7348
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 113
    true_value: 0.735
    true_std: 0.008
    value_gap_source_arxiv: '2603.02025'
    value_gap_source_title: arXiv:2603.02025
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00019999999999997797
    value_note: global 0.7350 within std
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.008
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.71
    std: 0.0229
    paper_value: 0.71
    paper_std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 193
    true_value: 0.71
    true_std: 0.0229
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.0229
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: IMDB-MULTI
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.724
    std: 0.009
    metric: Accuracy
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
    sort_value: 0.724
    sort_std: 0.009
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.712
    std: 0.011
    metric: Accuracy
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
    sort_value: 0.712
    sort_std: 0.011
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.705
    std: 0.01
    metric: Accuracy
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
    sort_value: 0.705
    sort_std: 0.01
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4813
    std: 0.0136
    paper_value: 0.4813
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 5
    true_value: 0.698
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21669999999999995
    value_note: ''
    paper_rank: 111
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.698
    sort_std: 0.013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.476
    std: 0.035
    paper_value: 0.476
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 6
    true_value: 0.695
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21899999999999997
    value_note: ''
    paper_rank: 115
    rank_delta: 109
    rank_delta_abs: 109
    rank_delta_direction: worse
    sort_value: 0.695
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5039
    std: 0.0041
    paper_value: 0.5039
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 7
    true_value: 0.682
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17810000000000004
    value_note: ''
    paper_rank: 76
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.682
    sort_std: 0.015
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.5731
    std: 0.0219
    paper_value: 0.5731
    paper_std: 0.0219
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 8
    true_value: 0.5731
    true_std: 0.0219
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5731
    sort_std: 0.0219
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.5632
    std: 0.0018
    paper_value: 0.5632
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 9
    true_value: 0.5632
    true_std: 0.0018
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.5023
    std: 0.0053
    paper_value: 0.5023
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 17
    true_value: 0.5333
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031000000000000028
    value_note: ''
    paper_rank: 78
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.5333
    sort_std: null
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.532
    std: 0.036
    paper_value: 0.532
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 18
    true_value: 0.532
    true_std: 0.036
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.532
    sort_std: 0.036
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.5131
    std: 0.0072
    paper_value: 0.5131
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying 2018
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 38
    true_value: 0.5203
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007199999999999984
    value_note: global 0.5203 within std
    paper_rank: 54
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.5203
    sort_std: null
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.5153
    std: 0.0065
    paper_value: 0.5153
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 49
    true_value: 0.5153
    true_std: 0.0065
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5153
    sort_std: 0.0065
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.5066
    std: 0.0082
    paper_value: 0.5066
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 68
    true_value: 0.507
    true_std: 0.008
    value_gap_source_arxiv: '2603.02025'
    value_gap_source_title: arXiv:2603.02025
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00039999999999995595
    value_note: global 0.5070 within std
    paper_rank: 70
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.507
    sort_std: 0.008
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.5023
    std: 0.0044
    paper_value: 0.5023
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 79
    true_value: 0.5023
    true_std: 0.0044
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5023
    sort_std: 0.0044
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.4859
    std: 0.0072
    paper_value: 0.4859
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 82
    true_value: 0.4993
    true_std: 0.0313
    value_gap_source_arxiv: '2406.08897'
    value_gap_source_title: Motif-driven Subgraph Structure Learning for Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.013400000000000023
    value_note: global 0.4993 within std
    paper_rank: 106
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.4993
    sort_std: 0.0313
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.4523
    std: 0.0284
    paper_value: 0.4523
    paper_std: 0.0284
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert 2016
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 126
    true_value: 0.4523
    true_std: 0.0284
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4523
    sort_std: 0.0284
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: NCI1
  rows:
  - model: MSA-AU
    model_key: msa-au
    model_plain: MSA-AU
    value: 0.962
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.962
    sort_std: null
    is_best: true
  - model: MSA-AD
    model_key: msa-ad
    model_plain: MSA-AD
    value: 0.947
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.947
    sort_std: null
    is_best: false
  - model: JbDA
    model_key: jbda
    model_plain: JbDA
    value: 0.912
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.912
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7662
    std: 0.018
    paper_value: 0.7662
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 13
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08479999999999999
    value_note: ''
    paper_rank: 139
    rank_delta: 126
    rank_delta_abs: 126
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7382
    std: 0.0217
    paper_value: 0.7382
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 21
    true_value: 0.838
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0998
    value_note: ''
    paper_rank: 172
    rank_delta: 151
    rank_delta_abs: 151
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7629
    std: 0.0179
    paper_value: 0.7629
    paper_std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 23
    true_value: 0.8365
    true_std: 0.0169
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0736
    value_note: ''
    paper_rank: 147
    rank_delta: 124
    rank_delta_abs: 124
    rank_delta_direction: worse
    sort_value: 0.8365
    sort_std: 0.0169
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.8352
    std: 0.0375
    paper_value: 0.8352
    paper_std: 0.0375
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 26
    true_value: 0.8352
    true_std: 0.0375
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8352
    sort_std: 0.0375
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8289
    std: 0.0019
    paper_value: 0.8289
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 34
    true_value: 0.8289
    true_std: 0.0019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8289
    sort_std: 0.0019
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.828
    std: 0.013
    paper_value: 0.828
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 35
    true_value: 0.828
    true_std: 0.013
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.828
    sort_std: 0.013
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7935
    std: 0.0033
    paper_value: 0.7935
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 94
    true_value: 0.7935
    true_std: 0.0033
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7935
    sort_std: 0.0033
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7864
    std: 0.0153
    paper_value: 0.7864
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 114
    true_value: 0.7864
    true_std: 0.0153
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7864
    sort_std: 0.0153
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.786
    std: 0.019
    paper_value: 0.786
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 115
    true_value: 0.786
    true_std: 0.019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.019
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7662
    std: 0.0193
    paper_value: 0.7662
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 137
    true_value: 0.7713
    true_std: 0.0149
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005099999999999993
    value_note: global 0.7713 within std
    paper_rank: 139
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.7713
    sort_std: 0.0149
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7635
    std: 0.0262
    paper_value: 0.7635
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 144
    true_value: 0.7635
    true_std: 0.0262
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7635
    sort_std: 0.0262
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.6745
    std: 0.0111
    paper_value: 0.6745
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 147
    true_value: 0.763
    true_std: 0.0153
    value_gap_source_arxiv: '2102.06986'
    value_gap_source_title: How Framelets Enhance Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08850000000000002
    value_note: ''
    paper_rank: 205
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.763
    sort_std: 0.0153
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.6702
    std: 0.0225
    paper_value: 0.6702
    paper_std: 0.0225
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 160
    true_value: 0.7511
    true_std: 0.0345
    value_gap_source_arxiv: '2102.06986'
    value_gap_source_title: How Framelets Enhance Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08089999999999997
    value_note: ''
    paper_rank: 205
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.7511
    sort_std: 0.0345
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PROTEINS
  rows:
  - model: HGP-SL
    model_key: hgp-sl
    model_plain: HGP-SL
    value: 0.8491
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8491
    sort_std: 0.0162
    is_best: true
  - model: rLap
    model_key: rlap
    model_plain: rLap
    value: 0.8434
    std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8434
    sort_std: 0.0403
    is_best: true
  - model: HGP-SL_DEN
    model_key: hgp-sl_den
    model_plain: HGP-SL_DEN
    value: 0.8312
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8312
    sort_std: 0.0084
    is_best: true
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7156
    std: 0.0149
    paper_value: 0.7156
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
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 10
    true_value: 0.8172
    true_std: 0.0219
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10160000000000002
    value_note: ''
    paper_rank: 272
    rank_delta: 262
    rank_delta_abs: 262
    rank_delta_direction: worse
    sort_value: 0.8172
    sort_std: 0.0219
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7562
    std: 0.0517
    paper_value: 0.7562
    paper_std: 0.0517
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 24
    true_value: 0.799
    true_std: 0.0295
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.04280000000000006
    value_note: global 0.7990 within std
    paper_rank: 129
    rank_delta: 105
    rank_delta_abs: 105
    rank_delta_direction: worse
    sort_value: 0.799
    sort_std: 0.0295
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7384
    std: 0.0446
    paper_value: 0.7384
    paper_std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 38
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046600000000000086
    value_note: ''
    paper_rank: 213
    rank_delta: 175
    rank_delta_abs: 175
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.7753
    std: 0.0178
    paper_value: 0.7753
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 57
    true_value: 0.7753
    true_std: 0.0178
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7753
    sort_std: 0.0178
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7324
    std: 0.0073
    paper_value: 0.7324
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 67
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03959999999999997
    value_note: ''
    paper_rank: 229
    rank_delta: 162
    rank_delta_abs: 162
    rank_delta_direction: worse
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.7686
    std: 0.0013
    paper_value: 0.7686
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 78
    true_value: 0.7686
    true_std: 0.0013
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7686
    sort_std: 0.0013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7348
    std: 0.0566
    paper_value: 0.7348
    paper_std: 0.0566
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 79
    true_value: 0.768
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03320000000000001
    value_note: global 0.7680 within std
    paper_rank: 222
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.768
    sort_std: 0.018
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.768
    std: 0.038
    paper_value: 0.768
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 80
    true_value: 0.768
    true_std: 0.038
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.038
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7642
    std: 0.0039
    paper_value: 0.7642
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
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 97
    true_value: 0.7642
    true_std: 0.0039
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0039
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.75
    std: 0.0251
    paper_value: 0.75
    paper_std: 0.0251
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 118
    true_value: 0.759
    true_std: 0.028
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009000000000000008
    value_note: global 0.7590 within std
    paper_rank: 158
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.028
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7516
    std: 0.0086
    paper_value: 0.7516
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
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 152
    true_value: 0.7516
    true_std: 0.0086
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7516
    sort_std: 0.0086
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7509
    std: 0.0059
    paper_value: 0.7509
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 156
    true_value: 0.751
    true_std: 0.006
    value_gap_source_arxiv: '2203.07691'
    value_gap_source_title: Supervised Contrastive Learning with Structure Inference
      for Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.7510 within std
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.006
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7048
    std: 0.0101
    paper_value: 0.7048
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 223
    true_value: 0.7348
    true_std: 0.0357
    value_gap_source_arxiv: '2102.06986'
    value_gap_source_title: How Framelets Enhance Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.030000000000000027
    value_note: global 0.7348 within std
    paper_rank: 289
    rank_delta: 66
    rank_delta_abs: 66
    rank_delta_direction: worse
    sort_value: 0.7348
    sort_std: 0.0357
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    paper_value: 0.339
    paper_std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 1
    true_value: 0.339
    true_std: 0.0073
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    value: 0.3174
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3174
    sort_std: null
    is_best: false
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    value: 0.3167
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.3167
    sort_std: 0.0031
    is_best: false
  - model: TGT-At (+RDKit)
    model_key: tgt-at (+rdkit)
    model_plain: TGT-At (+RDKit)
    value: 0.3144
    std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 4
    sort_value: 0.3144
    sort_std: 0.0029
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.3139
    std: 0.0032
    paper_value: 0.3139
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 5
    true_value: 0.314
    true_std: null
    value_gap_source_arxiv: '2207.08806'
    value_gap_source_title: Unified 2D and 3D Pre-Training of Molecular Representations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.3140 within std
    paper_rank: 6
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.314
    sort_std: null
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 17
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: MPNN +pseudo node
    model_key: mpnn +pseudo node
    model_plain: MPNN +pseudo node
    value: 0.2848
    std: 0.0026
    paper_value: 0.2848
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cai 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 23
    true_value: 0.2848
    true_std: 0.0026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2848
    sort_std: 0.0026
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2765
    std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 32
    true_value: 0.2765
    true_std: 0.0042
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2765
    sort_std: 0.0042
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.2761
    std: 0.0029
    paper_value: 0.2761
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cai 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 33
    true_value: 0.2761
    true_std: 0.0029
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2761
    sort_std: 0.0029
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2266
    std: 0.0028
    paper_value: 0.2266
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 35
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04369999999999999
    value_note: ''
    paper_rank: 58
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN +pseudo node
    model_key: gcn +pseudo node
    model_plain: GCN +pseudo node
    value: 0.2703
    std: 0.0023
    paper_value: 0.2703
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 36
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.202
    std: 0.0024
    paper_value: 0.202
    paper_std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    published_venue: null
    global_rank: 46
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04039999999999999
    value_note: ''
    paper_rank: 59
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: OGB
  datasets:
  - *id006
single_proposed_model: novel dynamic message-passing mechanism
---

