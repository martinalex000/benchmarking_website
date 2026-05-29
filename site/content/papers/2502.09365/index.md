---
title: Simple Path Structural Encoding for Graph Transformers
arxiv_id: '2502.09365'
source_url: ''
authors: []
published_date: Feb 13, 2025
published_date_iso: '2025-02-13'
abstract: Graph transformers extend global self-attention to graph-structured data,
  achieving notable success in graph learning. Recently, random walk structural encoding
  (RWSE) has been found to further enhance their predictive power by encoding both
  structural and positional information into the edge representation. However, RWSE
  cannot always distinguish between edges that belong to different local graph patterns,
  which reduces its ability to capture the full structural complexity of graphs. This
  work introduces Simple Path Structural Encoding (SPSE), a novel method that utilizes
  simple path counts for edge encoding. We show theoretically and experimentally that
  SPSE overcomes the limitations of RWSE, providing a richer representation of graph
  structures, particularly for capturing local cyclic patterns. To make SPSE computationally
  tractable, we propose an efficient approximate algorithm for simple path counting.
  SPSE demonstrates significant performance improvements over RWSE on various benchmarks,
  including molecular and long-range graph datasets, achieving statistically significant
  gains in discriminative tasks. These results pose SPSE as a powerful edge encoding
  alternative for enhancing the expressivity of graph transformers.
codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Graphormer
- Graph-ViT
mrr: 0.0662
adjusted_mrr: 0.0442
mrr_dataset_count: 2
benchmark_categories:
- Classic
- OGB
- LRGB
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id007
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.64223
    std: 0.00455
    paper_value: 0.64223
    paper_std: 0.00455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 4
    true_value: 0.9
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25777000000000005
    value_note: ''
    paper_rank: 47
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5571
    std: 0.00381
    paper_value: 0.5571
    paper_std: 0.00381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
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
    value: 0.55255
    std: 0.01527
    paper_value: 0.55255
    paper_std: 0.01527
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 6
    true_value: 0.89
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.33745
    value_note: ''
    paper_rank: 54
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.01
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.77022
    std: 0.0043
    paper_value: 0.77022
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 10
    true_value: 0.77022
    true_std: 0.0043
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77022
    sort_std: 0.0043
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.76246
    std: 0.00954
    paper_value: 0.76246
    paper_std: 0.00954
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 13
    true_value: 0.76246
    true_std: 0.00954
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76246
    sort_std: 0.00954
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.74696
    std: 0.00125
    paper_value: 0.74696
    paper_std: 0.00125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 15
    true_value: 0.74696
    true_std: 0.00125
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74696
    sort_std: 0.00125
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.73961
    std: 0.0033
    paper_value: 0.73961
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 16
    true_value: 0.73961
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73961
    sort_std: 0.0033
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.73897
    std: 0.00524
    paper_value: 0.73897
    paper_std: 0.00524
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 18
    true_value: 0.73897
    true_std: 0.00524
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73897
    sort_std: 0.00524
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.73885
    std: 0.00348
    paper_value: 0.73885
    paper_std: 0.00348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 19
    true_value: 0.73885
    true_std: 0.00348
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73885
    sort_std: 0.00348
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.72097
    std: 0.00475
    paper_value: 0.72097
    paper_std: 0.00475
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 23
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020299999999999763
    value_note: global 0.7230 within std
    paper_rank: 27
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.723
    sort_std: 0.0036
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.7219
    std: 0.0013
    paper_value: 0.7219
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
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 26
    true_value: 0.7219
    true_std: 0.0013
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7219
    sort_std: 0.0013
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.72114
    std: 0.00462
    paper_value: 0.72114
    paper_std: 0.00462
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 27
    true_value: 0.72114
    true_std: 0.00462
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72114
    sort_std: 0.00462
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.68702
    std: 0.00409
    paper_value: 0.68702
    paper_std: 0.00409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 37
    true_value: 0.68702
    true_std: 0.00409
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68702
    sort_std: 0.00409
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.67312
    std: 0.00311
    paper_value: 0.67312
    paper_std: 0.00311
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 41
    true_value: 0.67312
    true_std: 0.00311
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67312
    sort_std: 0.00311
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
    paper_value: 0.7973
    paper_std: 0.00189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 3
    true_value: 0.7973
    true_std: 0.00189
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7973
    sort_std: 0.00189
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.79571
    std: 0.00122
    paper_value: 0.79571
    paper_std: 0.00122
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 4
    true_value: 0.79571
    true_std: 0.00122
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79571
    sort_std: 0.00122
    is_best: false
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.79284
    std: 0.00122
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
    global_rank: 5
    sort_value: 0.79284
    sort_std: 0.00122
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.79232
    std: 0.00348
    paper_value: 0.79232
    paper_std: 0.00348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 6
    true_value: 0.79232
    true_std: 0.00348
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79232
    sort_std: 0.00348
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.79071
    std: 0.0012
    paper_value: 0.79071
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 8
    true_value: 0.79071
    true_std: 0.0012
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79071
    sort_std: 0.0012
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.7894
    std: 0.00132
    paper_value: 0.7894
    paper_std: 0.00132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 9
    true_value: 0.7894
    true_std: 0.00132
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7894
    sort_std: 0.00132
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.7844
    std: 0.00177
    paper_value: 0.7844
    paper_std: 0.00177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 11
    true_value: 0.7844
    true_std: 0.00177
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7844
    sort_std: 0.00177
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.78071
    std: 0.00037
    paper_value: 0.78071
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 14
    true_value: 0.78071
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78071
    sort_std: 0.00037
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.77969
    std: 0.00161
    paper_value: 0.77969
    paper_std: 0.00161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 16
    true_value: 0.78016
    true_std: 0.0018
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00046999999999997044
    value_note: global 0.7802 within std
    paper_rank: 17
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.78016
    sort_std: 0.0018
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7384
    std: 0.00326
    paper_value: 0.7384
    paper_std: 0.00326
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.70587
    std: 0.00447
    paper_value: 0.70587
    paper_std: 0.00447
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 29
    true_value: 0.7059
    true_std: 0.00447
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.7059 within std
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7059
    sort_std: 0.00447
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.68498
    std: 0.00976
    paper_value: 0.68498
    paper_std: 0.00976
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 30
    true_value: 0.685
    true_std: 0.0097
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.6850 within std
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
    value: 0.64716
    std: 0.01553
    paper_value: 0.64716
    paper_std: 0.01553
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 33
    true_value: 0.6472
    true_std: 0.0155
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 4.0000000000040004e-05
    value_note: global 0.6472 within std
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6472
    sort_std: 0.0155
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    value: 0.9855
    std: 0.00039
    paper_value: 0.9855
    paper_std: 0.00039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 8
    true_value: 0.9855
    true_std: 0.00039
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9855
    sort_std: 0.00039
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.98294
    std: 0.00147
    paper_value: 0.98294
    paper_std: 0.00147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 15
    true_value: 0.98294
    true_std: 0.00147
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98294
    sort_std: 0.00147
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.98269
    std: 0.00078
    paper_value: 0.98269
    paper_std: 0.00078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 16
    true_value: 0.98269
    true_std: 0.00078
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98269
    sort_std: 0.00078
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.98231
    std: 0.00197
    paper_value: 0.98231
    paper_std: 0.00197
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 19
    true_value: 0.98231
    true_std: 0.00197
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98231
    sort_std: 0.00197
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.97422
    std: 0.0011
    paper_value: 0.97422
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 20
    true_value: 0.982
    true_std: 0.0005
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007780000000000009
    value_note: ''
    paper_rank: 44
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.982
    sort_std: 0.0005
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.98173
    std: 0.00087
    paper_value: 0.98173
    paper_std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 25
    true_value: 0.98173
    true_std: 0.00087
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98173
    sort_std: 0.00087
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.98127
    std: 0.00123
    paper_value: 0.98127
    paper_std: 0.00123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 29
    true_value: 0.98127
    true_std: 0.00123
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98127
    sort_std: 0.00123
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.98105
    std: 0.00158
    paper_value: 0.98105
    paper_std: 0.00158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 33
    true_value: 0.98105
    true_std: 0.00158
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98105
    sort_std: 0.00158
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.98064
    std: 0.00157
    paper_value: 0.98064
    paper_std: 0.00157
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 35
    true_value: 0.98082
    true_std: 0.00114
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000180000000000069
    value_note: global 0.9808 within std
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98082
    sort_std: 0.00114
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.96485
    std: 0.00252
    paper_value: 0.96485
    paper_std: 0.00252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 40
    true_value: 0.979
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014149999999999996
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
    value: 0.90705
    std: 0.00218
    paper_value: 0.90705
    paper_std: 0.00218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 41
    true_value: 0.978
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07094999999999996
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
    std: 0.00143
    paper_value: 0.9734
    paper_std: 0.00143
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.95535
    std: 0.00205
    paper_value: 0.95535
    paper_std: 0.00205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 48
    true_value: 0.972
    true_std: 0.005
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016649999999999943
    value_note: ''
    paper_rank: 52
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.972
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    value: 0.85568
    std: 0.00088
    paper_value: 0.85568
    paper_std: 0.00088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 3
    true_value: 0.92
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06432000000000004
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
    value: 0.85387
    std: 0.00136
    paper_value: 0.85387
    paper_std: 0.00136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 4
    true_value: 0.91
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05613000000000001
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
    value: 0.78271
    std: 0.00186
    paper_value: 0.78271
    paper_std: 0.00186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 5
    true_value: 0.9
    true_std: 0.004
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11729
    value_note: ''
    paper_rank: 57
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.89
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
    global_rank: 6
    sort_value: 0.89
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.71892
    std: 0.00334
    paper_value: 0.71892
    paper_std: 0.00334
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 7
    true_value: 0.88
    true_std: 0.005
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16108
    value_note: ''
    paper_rank: 60
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.005
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.87235
    std: 0.0004
    paper_value: 0.87235
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 10
    true_value: 0.87235
    true_std: 0.0004
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87235
    sort_std: 0.0004
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.87229
    std: 0.00056
    paper_value: 0.87229
    paper_std: 0.00056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 11
    true_value: 0.87229
    true_std: 0.00056
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87229
    sort_std: 0.00056
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.87064
    std: 0.00052
    paper_value: 0.87064
    paper_std: 0.00052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 14
    true_value: 0.87064
    true_std: 0.00052
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87064
    sort_std: 0.00052
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.87008
    std: 0.00062
    paper_value: 0.87008
    paper_std: 0.00062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 15
    true_value: 0.87008
    true_std: 0.00062
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87008
    sort_std: 0.00062
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.8685
    std: 0.00057
    paper_value: 0.8685
    paper_std: 0.00057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 17
    true_value: 0.8685
    true_std: 0.00057
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8685
    sort_std: 0.00057
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.86834
    std: 0.00025
    paper_value: 0.86834
    paper_std: 0.00025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 20
    true_value: 0.86834
    true_std: 0.00025
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86834
    sort_std: 0.00025
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.86821
    std: 0.0002
    paper_value: 0.86821
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 21
    true_value: 0.86821
    true_std: 0.0002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86821
    sort_std: 0.0002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.86742
    std: 0.00015
    paper_value: 0.86742
    paper_std: 0.00015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 24
    true_value: 0.86742
    true_std: 0.00015
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86742
    sort_std: 0.00015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.86688
    std: 0.00073
    paper_value: 0.86688
    paper_std: 0.00073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 29
    true_value: 0.86688
    true_std: 0.00073
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86688
    sort_std: 0.00073
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.86581
    std: 0.00037
    paper_value: 0.86581
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 35
    true_value: 0.86581
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86581
    sort_std: 0.00037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: PCQM4Mv2
  rows:
  - model: DeMol
    model_key: demol
    model_plain: DeMol
    value: 0.0603
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0603
    sort_std: null
    is_best: true
  - model: TGT-At
    model_key: tgt-at
    model_plain: TGT-At
    value: 0.0671
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0671
    sort_std: null
    is_best: false
  - model: Unimol+
    model_key: unimol+
    model_plain: Unimol+
    value: 0.0693
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0693
    sort_std: null
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.0942
    std: null
    paper_value: 0.0942
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 5
    true_value: 0.0755
    true_std: null
    value_gap_source_arxiv: '2212.02229'
    value_gap_source_title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular
      Property Prediction'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01870000000000001
    value_note: ''
    paper_rank: 33
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.0755
    sort_std: null
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.0831
    std: null
    paper_value: 0.0831
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 9
    true_value: 0.0831
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0831
    sort_std: null
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.0838
    std: null
    paper_value: 0.0838
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 10
    true_value: 0.0838
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.0864
    std: null
    paper_value: 0.0864
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 18
    true_value: 0.0864
    true_std: null
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0864
    sort_std: null
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.0911
    std: null
    paper_value: 0.0911
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 28
    true_value: 0.0911
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0911
    sort_std: null
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.0918
    std: null
    paper_value: 0.0918
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 29
    true_value: 0.0918
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0918
    sort_std: null
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.0934
    std: null
    paper_value: 0.0934
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 31
    true_value: 0.0934
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0934
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1195
    std: null
    paper_value: 0.1195
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 47
    true_value: 0.1195
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1195
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1379
    std: null
    paper_value: 0.1379
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 55
    true_value: 0.135
    true_std: 0.002
    value_gap_source_arxiv: '2107.09422'
    value_gap_source_title: Large-scale graph representation learning with very deep
      GNNs and self-supervision
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.002899999999999986
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.135
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
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
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 0.725
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.0023
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 5
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.697
    std: 0.008
    paper_value: 0.697
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 26
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.6945
    std: 0.0113
    paper_value: 0.6945
    paper_std: 0.0113
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 27
    true_value: 0.6945
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6945
    sort_std: 0.0113
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.6803
    std: 0.0085
    paper_value: 0.6803
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 40
    true_value: 0.6803
    true_std: 0.0085
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6803
    sort_std: 0.0085
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
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 53
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
    paper_rank: 96
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.6608
    std: 0.0063
    paper_value: 0.6608
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 55
    true_value: 0.6608
    true_std: 0.0063
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6608
    sort_std: 0.0063
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.6605
    std: 0.0096
    paper_value: 0.6605
    paper_std: 0.0096
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 56
    true_value: 0.6605
    true_std: 0.0096
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6605
    sort_std: 0.0096
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6601
    std: 0.0061
    paper_value: 0.6601
    paper_std: 0.0061
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 57
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6601
    sort_std: 0.0061
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 61
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
    paper_rank: 75
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6562
    sort_std: 0.0075
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 68
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
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.6513
    std: 0.0061
    paper_value: 0.6513
    paper_std: 0.0061
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 69
    true_value: 0.6513
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6513
    sort_std: 0.0061
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
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
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 6
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.002599999999999991
    value_note: ''
    paper_rank: 29
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: true
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.2449
    std: 0.0018
    paper_value: 0.2449
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 7
    true_value: 0.2449
    true_std: 0.0018
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0018
    is_best: true
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
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 26
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
    paper_rank: 105
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.248
    std: 0.0025
    paper_value: 0.248
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 41
    true_value: 0.248
    true_std: 0.0025
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.248
    sort_std: 0.0025
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
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 42
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
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.2482
    std: 0.0019
    paper_value: 0.2482
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 43
    true_value: 0.2482
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2482
    sort_std: 0.0019
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.2486
    std: 0.0012
    paper_value: 0.2486
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
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 47
    true_value: 0.2486
    true_std: 0.0012
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2486
    sort_std: 0.0012
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2509
    std: 0.0017
    paper_value: 0.2509
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 50
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 59
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.2506
    std: 0.001
    paper_value: 0.2506
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
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 59
    true_value: 0.2506
    true_std: 0.001
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.001
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 66
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 73
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 1
    true_value: 0.004
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27799999999999997
    value_note: ''
    paper_rank: 135
    rank_delta: 134
    rank_delta_abs: 134
    rank_delta_direction: worse
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.006
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.006
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.526
    std: 0.051
    paper_value: 0.526
    paper_std: 0.051
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.512
    value_note: ''
    paper_rank: 152
    rank_delta: 149
    rank_delta_abs: 149
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: true
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
    params_millions: 0.5
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
    is_best: true
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 11
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.34299999999999997
    value_note: ''
    paper_rank: 144
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 13
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 87
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.003
    paper_value: 0.07
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
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 16
    true_value: 0.0262
    true_std: 0.0025
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043800000000000006
    value_note: ''
    paper_rank: 49
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.0262
    sort_std: 0.0025
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.073
    std: 0.001
    paper_value: 0.073
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 24
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03799999999999999
    value_note: ''
    paper_rank: 51
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.059
    std: 0.001
    paper_value: 0.059
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 32
    true_value: 0.059
    true_std: 0.001
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.059
    sort_std: 0.001
    is_best: false
  - model: CSA-SPSE
    model_key: csa-spse
    model_plain: CSA-SPSE
    value: 0.061
    std: 0.003
    paper_value: 0.061
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 33
    true_value: 0.061
    true_std: 0.003
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.061
    sort_std: 0.003
    is_best: false
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.065
    std: 0.005
    paper_value: 0.065
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 39
    true_value: 0.065
    true_std: 0.005
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.065
    sort_std: 0.005
    is_best: false
  - model: GPS + GPSE
    model_key: gps + gpse
    model_plain: GPS + GPSE
    value: 0.068
    std: 0.003
    paper_value: 0.068
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 44
    true_value: 0.068
    true_std: 0.003
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.068
    sort_std: 0.003
    is_best: false
  - model: CSA-RWSE
    model_key: csa-rwse
    model_plain: CSA-RWSE
    value: 0.069
    std: 0.003
    paper_value: 0.069
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 46
    true_value: 0.069
    true_std: 0.003
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.003
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 58
    true_value: 0.08
    true_std: 0.001
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.001
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.108
    std: 0.009
    paper_value: 0.108
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
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 79
    true_value: 0.108
    true_std: 0.009
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 80
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.273
    value_note: ''
    paper_rank: 147
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    global_rank: 101
    true_value: 0.139
    true_std: 0.006
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.139
    sort_std: 0.006
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
  - *id004
- benchmark: GNNBenchmark
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
main_figure: /figures/2502.09365/main_figure.png
---

