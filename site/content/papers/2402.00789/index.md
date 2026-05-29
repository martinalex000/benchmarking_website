---
title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State
  Spaces'
arxiv_id: '2402.00789'
source_url: ''
authors: []
published_date: Feb 1, 2024
published_date_iso: '2024-02-01'
abstract: Attention mechanisms have been widely used to capture long-range dependencies
  among nodes in Graph Transformers. Bottlenecked by the quadratic computational cost,
  attention mechanisms fail to scale in large graphs. Recent improvements in computational
  efficiency are mainly achieved by attention sparsification with random or heuristic-based
  graph subsampling, which falls short in data-dependent context reasoning. State
  space models (SSMs), such as Mamba, have gained prominence for their effectiveness
  and efficiency in modeling long-range dependencies in sequential data. However,
  adapting SSMs to non-sequential graph data presents a notable challenge. In this
  work, we introduce Graph-Mamba, the first attempt to enhance long-range context
  modeling in graph networks by integrating a Mamba block with the input-dependent
  node selection mechanism. Specifically, we formulate graph-centric node prioritization
  and permutation strategies to enhance context-aware reasoning, leading to a substantial
  improvement in predictive performance. Extensive experiments on ten benchmark datasets
  demonstrate that Graph-Mamba outperforms state-of-the-art methods in long-range
  graph prediction tasks, with a fraction of the computational cost in both FLOPs
  and GPU memory consumption. The code and models are publicly available at https://github.com/bowang-lab/Graph-Mamba.
codebase_url: https://github.com/bowang-lab/Graph-Mamba
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Graph-Mamba
mrr: 0.0828
adjusted_mrr: 0.0828
mrr_dataset_count: 6
benchmark_categories:
- LRGB
- GNNBenchmark
- Other Graph Benchmarks
task_categories:
- graph_classification
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id004
  dataset: CIFAR10
  rows:
  - model: CNNs
    model_key: cnns
    model_plain: CNNs
    value: 0.93
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.93
    sort_std: 0.005
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.92
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.92
    sort_std: 0.007
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.91
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.91
    sort_std: 0.008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5571
    std: 0.0038
    paper_value: 0.5571
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 5
    true_value: 0.89
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3329
    value_note: ''
    paper_rank: 53
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5526
    std: 0.0152
    paper_value: 0.5526
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 6
    true_value: 0.89
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.33740000000000003
    value_note: ''
    paper_rank: 54
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.01
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7413
    std: 0.005
    paper_value: 0.7413
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 15
    true_value: 0.74696
    true_std: 0.00125
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.005659999999999998
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74696
    sort_std: 0.00125
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.737
    std: 0.0034
    paper_value: 0.737
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 21
    true_value: 0.737
    true_std: 0.0034
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.0034
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.7226
    std: 0.0031
    paper_value: 0.7226
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 25
    true_value: 0.7226
    true_std: 0.0031
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7226
    sort_std: 0.0031
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.7067
    std: 0.0033
    paper_value: 0.7067
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 30
    true_value: 0.7067
    true_std: 0.0033
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7067
    sort_std: 0.0033
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.7048
    std: 0.001
    paper_value: 0.7048
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 31
    true_value: 0.7048
    true_std: 0.001
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7048
    sort_std: 0.001
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6731
    std: 0.0031
    paper_value: 0.6731
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 41
    true_value: 0.67312
    true_std: 0.00311
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.6731 within std
    paper_rank: 42
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.67312
    sort_std: 0.00311
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.80113
    std: 0.00138
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.80113
    sort_std: 0.00138
    is_best: true
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.80026
    std: 0.00277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.80026
    sort_std: 0.00277
    is_best: true
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.7973
    std: 0.00189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7973
    sort_std: 0.00189
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.7829
    std: 0.0004
    paper_value: 0.7829
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 12
    true_value: 0.7829
    true_std: 0.0004
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7829
    sort_std: 0.0004
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7802
    std: 0.0011
    paper_value: 0.7802
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 14
    true_value: 0.78071
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005100000000000104
    value_note: global 0.7807 within std
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78071
    sort_std: 0.00037
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.7799
    std: 0.0017
    paper_value: 0.7799
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 17
    true_value: 0.7799
    true_std: 0.0017
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7799
    sort_std: 0.0017
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.7746
    std: 0.0002
    paper_value: 0.7746
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 20
    true_value: 0.7746
    true_std: 0.0002
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7746
    sort_std: 0.0002
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.768
    std: 0.0036
    paper_value: 0.768
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 23
    true_value: 0.768
    true_std: 0.0036
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
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
    sort_std: 0.0036
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7384
    std: 0.0032
    paper_value: 0.7384
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 25
    true_value: 0.76082
    true_std: 0.00196
    value_gap_source_arxiv: '2108.03348'
    value_gap_source_title: Global Self-Attention as a Replacement for Graph Convolution
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022420000000000107
    value_note: ''
    paper_rank: 27
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.76082
    sort_std: 0.00196
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.685
    std: 0.0097
    paper_value: 0.685
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 30
    true_value: 0.685
    true_std: 0.0097
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.685
    sort_std: 0.0097
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6472
    std: 0.0155
    paper_value: 0.6472
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 33
    true_value: 0.6472
    true_std: 0.0155
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6472
    sort_std: 0.0155
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: MNIST
  rows:
  - model: Classical CNN
    model_key: classical cnn
    model_plain: Classical CNN
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_display: Jun 2016
    date_iso: 2016-06
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: LeNet5
    model_key: lenet5
    model_plain: LeNet5
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_display: May 2017
    date_iso: 2017-05
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: CayleyNets
    model_key: cayleynets
    model_plain: CayleyNets
    value: 0.9918
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_display: May 2017
    date_iso: 2017-05
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9918
    sort_std: null
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9843
    std: 0.0004
    paper_value: 0.9843
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 8
    true_value: 0.9855
    true_std: 0.00039
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0012000000000000899
    value_note: ''
    paper_rank: 10
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.9855
    sort_std: 0.00039
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.9842
    std: 0.0008
    paper_value: 0.9842
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 11
    true_value: 0.9842
    true_std: 0.0008
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9842
    sort_std: 0.0008
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.9834
    std: 0.0003
    paper_value: 0.9834
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 14
    true_value: 0.9834
    true_std: 0.0003
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9834
    sort_std: 0.0003
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.9817
    std: 0.0001
    paper_value: 0.9817
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 26
    true_value: 0.9817
    true_std: 0.0001
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9817
    sort_std: 0.0001
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.9811
    std: 0.0011
    paper_value: 0.9811
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 31
    true_value: 0.9811
    true_std: 0.0011
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9811
    sort_std: 0.0011
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9649
    std: 0.0025
    paper_value: 0.9649
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 40
    true_value: 0.979
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014100000000000001
    value_note: ''
    paper_rank: 50
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.979
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9071
    std: 0.0021
    paper_value: 0.9071
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 41
    true_value: 0.978
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07089999999999996
    value_note: ''
    paper_rank: 56
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.978
    sort_std: 0.003
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.9734
    std: 0.0014
    paper_value: 0.9734
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 47
    true_value: 0.9734
    true_std: 0.00143
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9734
    sort_std: 0.00143
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: MalNet-Tiny
  rows:
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9422
    std: 0.0024
    paper_value: 0.9422
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 1
    true_value: 0.9422
    true_std: 0.0024
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9422
    sort_std: 0.0024
    is_best: true
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.9406
    std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9406
    sort_std: 0.0064
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.9372
    std: 0.0029
    metric: Accuracy
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
    sort_value: 0.9372
    sort_std: 0.0029
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.935
    std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 4
    sort_value: 0.935
    sort_std: 0.0041
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.934
    std: 0.0027
    paper_value: 0.934
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 6
    true_value: 0.934
    true_std: 0.0027
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.0027
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.9264
    std: 0.0078
    paper_value: 0.9264
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
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 7
    true_value: 0.9264
    true_std: 0.0078
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9264
    sort_std: 0.0078
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.9234
    std: 0.0034
    paper_value: 0.9234
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 8
    true_value: 0.9234
    true_std: 0.0034
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9234
    sort_std: 0.0034
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.9223
    std: 0.0065
    paper_value: 0.9223
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
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 9
    true_value: 0.9223
    true_std: 0.0065
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9223
    sort_std: 0.0065
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8898
    std: 0.0055
    paper_value: 0.8898
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 11
    true_value: 0.8898
    true_std: 0.0055
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8898
    sort_std: 0.0055
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.81
    std: null
    paper_value: 0.81
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 14
    true_value: 0.81
    true_std: null
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PATTERN
  rows:
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.96
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.96
    sort_std: 0.002
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.93
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.93
    sort_std: 0.002
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8557
    std: 0.0008
    paper_value: 0.8557
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 3
    true_value: 0.92
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06430000000000002
    value_note: ''
    paper_rank: 47
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.92
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8539
    std: 0.0013
    paper_value: 0.8539
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 4
    true_value: 0.91
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05610000000000004
    value_note: ''
    paper_rank: 49
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.91
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7189
    std: 0.0033
    paper_value: 0.7189
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 7
    true_value: 0.88
    true_std: 0.005
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16110000000000002
    value_note: ''
    paper_rank: 60
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.005
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.867
    std: 0.0003
    paper_value: 0.867
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 24
    true_value: 0.86742
    true_std: 0.00015
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00041999999999997595
    value_note: ''
    paper_rank: 27
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.86742
    sort_std: 0.00015
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.8671
    std: 0.0005
    paper_value: 0.8671
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 27
    true_value: 0.8671
    true_std: 0.0005
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8671
    sort_std: 0.0005
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.8664
    std: 0.0011
    paper_value: 0.8664
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 33
    true_value: 0.8664
    true_std: 0.0011
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8664
    sort_std: 0.0011
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.86
    std: 0.0014
    paper_value: 0.86
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 39
    true_value: 0.86
    true_std: 0.0014
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.0014
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.8334
    std: 0.0029
    paper_value: 0.8334
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 55
    true_value: 0.8334
    true_std: 0.0029
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8334
    sort_std: 0.0029
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PCQM-Contact
  rows:
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.5341
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.5341
    sort_std: null
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3587
    std: 0.0025
    paper_value: 0.3587
    paper_std: 0.0025
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 2
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0050000000000000044
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.345
    std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.345
    sort_std: 0.0002
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.3442
    std: 0.0009
    paper_value: 0.3442
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.287
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 4
    true_value: 0.3442
    true_std: 0.0009
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3442
    sort_std: 0.0009
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.3437
    std: 0.0005
    paper_value: 0.3437
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 5
    true_value: 0.3437
    true_std: 0.0005
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3437
    sort_std: 0.0005
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.3425
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.3425
    sort_std: 0.0006
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.3395
    std: 0.0013
    paper_value: 0.3395
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 9
    true_value: 0.3395
    true_std: 0.0013
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3395
    sort_std: 0.0013
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.3391
    std: 0.0002
    paper_value: 0.3391
    paper_std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 10
    true_value: 0.3391
    true_std: 0.0002
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3391
    sort_std: 0.0002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: 0.0006
    paper_value: 0.3234
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 21
    true_value: 0.3234
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3234
    sort_std: 0.0006
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: 0.0011
    paper_value: 0.3218
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 22
    true_value: 0.3218
    true_std: 0.0011
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3218
    sort_std: 0.0011
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.318
    std: 0.0027
    paper_value: 0.318
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Benchmark on Short to Medium-Range Graph Datasets)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    global_rank: 24
    true_value: 0.318
    true_std: 0.0027
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.0027
    is_best: false
  metric: MRR
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: GNNBenchmark
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: Other Graph Benchmarks
  datasets:
  - *id006
single_proposed_model: Graph-Mamba
main_figure: /figures/2402.00789/main_figure.png
---

