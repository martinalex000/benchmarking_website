---
title: 'Exphormer: Sparse Transformers for Graphs'
arxiv_id: '2303.06147'
source_url: ''
authors: []
published_date: Mar 10, 2023
published_date_iso: '2023-03-10'
abstract: 'Graph transformers have emerged as a promising architecture for a variety
  of graph learning and representation tasks. Despite their successes, though, it
  remains challenging to scale graph transformers to large graphs while maintaining
  accuracy competitive with message-passing networks. In this paper, we introduce
  Exphormer, a framework for building powerful and scalable graph transformers. Exphormer
  consists of a sparse attention mechanism based on two mechanisms: virtual global
  nodes and expander graphs, whose mathematical characteristics, such as spectral
  expansion, pseduorandomness, and sparsity, yield graph transformers with complexity
  only linear in the size of the graph, while allowing us to prove desirable theoretical
  properties of the resulting transformer models. We show that incorporating Exphormer
  into the recently-proposed GraphGPS framework produces models with competitive empirical
  results on a wide variety of graph datasets, including state-of-the-art results
  on three datasets. We also show that Exphormer can scale to datasets on larger graphs
  than shown in previous graph transformer architectures. Code can be found at \url{https://github.com/hamed1375/Exphormer}.'
codebase_url: https://github.com/hamed1375/Exphormer
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Exphormer
mrr: 0.2005
adjusted_mrr: 0.2005
mrr_dataset_count: 11
benchmark_categories:
- Classic
- LRGB
- OGB
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id011
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
    global_rank: 3
    sort_value: 0.79284
    sort_std: 0.00122
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.7923
    std: 0.00348
    paper_value: 0.7923
    paper_std: 0.00348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hussain 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 4
    true_value: 0.79232
    true_std: 0.00348
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.7923 within std
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79232
    sort_std: 0.00348
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7807
    std: 0.00037
    paper_value: 0.7807
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 9
    true_value: 0.7807
    true_std: 0.00037
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7807
    sort_std: 0.00037
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7802
    std: 0.0018
    paper_value: 0.7802
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 10
    true_value: 0.7802
    true_std: 0.0018
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7802
    sort_std: 0.0018
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
    value: 0.7786
    std: 0.00104
    paper_value: 0.7786
    paper_std: 0.00104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 13
    true_value: 0.7786
    true_std: 0.00104
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7786
    sort_std: 0.00104
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7669
    std: 0.0065
    paper_value: 0.7669
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 19
    true_value: 0.76691
    true_std: 0.0065
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.99999999995449e-06
    value_note: global 0.7669 within std
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76691
    sort_std: 0.0065
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
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 20
    true_value: 0.76082
    true_std: 0.00196
    value_gap_source_arxiv: '2108.03348'
    value_gap_source_title: Global Self-Attention as a Replacement for Graph Convolution
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022420000000000107
    value_note: ''
    paper_rank: 22
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.76082
    sort_std: 0.00196
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7059
    std: 0.00447
    paper_value: 0.7059
    paper_std: 0.00447
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 24
    true_value: 0.7059
    true_std: 0.00447
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7059
    sort_std: 0.00447
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.685
    std: 0.00976
    paper_value: 0.685
    paper_std: 0.00976
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 25
    true_value: 0.685
    true_std: 0.0097
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
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
    std: 0.01553
    paper_value: 0.6472
    paper_std: 0.01553
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 26
    true_value: 0.6472
    true_std: 0.0155
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6472
    sort_std: 0.0155
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: COCO-SP
  rows:
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.4483
    std: 0.0071
    metric: F1
    higher_is_better: true
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4483
    sort_std: 0.0071
    is_best: true
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.4387
    std: 0.0054
    metric: F1
    higher_is_better: true
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4387
    sort_std: 0.0054
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.4382
    std: 0.0101
    metric: F1
    higher_is_better: true
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3455
    std: 0.0009
    paper_value: 0.3455
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 7
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3412
    std: 0.0044
    paper_value: 0.3412
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 9
    true_value: 0.3412
    true_std: 0.0044
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3412
    sort_std: 0.0044
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2641
    std: 0.0045
    paper_value: 0.2641
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 13
    true_value: 0.2641
    true_std: 0.0045
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2641
    sort_std: 0.0045
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2618
    std: 0.0031
    paper_value: 0.2618
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 14
    true_value: 0.2618
    true_std: 0.0031
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2618
    sort_std: 0.0031
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2592
    std: 0.0158
    paper_value: 0.2592
    paper_std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 16
    true_value: 0.2592
    true_std: 0.0158
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2592
    sort_std: 0.0158
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.2574
    std: 0.0034
    paper_value: 0.2574
    paper_std: 0.0034
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 18
    true_value: 0.2574
    true_std: 0.0034
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
    sort_value: 0.2574
    sort_std: 0.0034
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2434
    std: 0.0156
    paper_value: 0.2434
    paper_std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 19
    true_value: 0.2434
    true_std: 0.0156
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2434
    sort_std: 0.0156
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1339
    std: 0.0044
    paper_value: 0.1339
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 24
    true_value: 0.1339
    true_std: 0.0044
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1339
    sort_std: 0.0044
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0841
    std: 0.001
    paper_value: 0.0841
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 37
    true_value: 0.0841
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0841
    sort_std: 0.001
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Coauthor-CS
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9589
    std: 0.0034
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9577
    std: 0.0015
    paper_value: 0.9577
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 2
    true_value: 0.9577
    true_std: 0.0015
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9577
    sort_std: 0.0015
    is_best: true
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9575
    std: 0.0009
    paper_value: 0.9575
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Nagphormer22
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 3
    true_value: 0.9575
    true_std: 0.0009
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9575
    sort_std: 0.0009
    is_best: true
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.9546
    std: 0.0033
    metric: Accuracy
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
    global_rank: 4
    sort_value: 0.9546
    sort_std: 0.0033
    is_best: true
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.9518
    std: 0.003
    metric: Accuracy
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
    global_rank: 5
    sort_value: 0.9518
    sort_std: 0.003
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.9451
    std: 0.0015
    paper_value: 0.9451
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 12
    true_value: 0.9451
    true_std: 0.0015
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9451
    sort_std: 0.0015
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9393
    std: 0.0012
    paper_value: 0.9393
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 14
    true_value: 0.9393
    true_std: 0.0012
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9393
    sort_std: 0.0012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Coauthor-Physics
  rows:
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9734
    std: 0.0003
    paper_value: 0.9734
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Nagphormer 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 1
    true_value: 0.9734
    true_std: 0.0003
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9734
    sort_std: 0.0003
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9716
    std: 0.0013
    paper_value: 0.9716
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 2
    true_value: 0.9716
    true_std: 0.0013
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9716
    sort_std: 0.0013
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.945
    std: 0.003
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
    sort_value: 0.945
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.941
    std: 0.003
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
    global_rank: 4
    sort_value: 0.941
    sort_std: 0.003
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.938
    std: 0.004
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
    global_rank: 5
    sort_value: 0.938
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    params_millions: 1.66
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.9817
    std: 0.00087
    paper_value: 0.9817
    paper_std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hussain 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 21
    true_value: 0.98173
    true_std: 0.00087
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.9817 within std
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98173
    sort_std: 0.00087
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9805
    std: 0.00126
    paper_value: 0.9805
    paper_std: 0.00126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 29
    true_value: 0.98051
    true_std: 0.00126
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.99999999995449e-06
    value_note: global 0.9805 within std
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98051
    sort_std: 0.00126
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.9794
    std: 0.0005
    paper_value: 0.9794
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönshoff 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 30
    true_value: 0.97944
    true_std: 0.0005
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 3.999999999992898e-05
    value_note: global 0.9794 within std
    paper_rank: 31
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.97944
    sort_std: 0.0005
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.9794
    std: 0.0012
    paper_value: 0.9794
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso 2020
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 32
    true_value: 0.9794
    true_std: 0.0012
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9794
    sort_std: 0.0012
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
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 36
    true_value: 0.9734
    true_std: 0.00143
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9734
    sort_std: 0.00143
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9649
    std: 0.00252
    paper_value: 0.9649
    paper_std: 0.00252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 39
    true_value: 0.9649
    true_std: 0.0025
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9649
    sort_std: 0.0025
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9554
    std: 0.00205
    paper_value: 0.9554
    paper_std: 0.00205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 41
    true_value: 0.9554
    true_std: 0.00205
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9554
    sort_std: 0.00205
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9071
    std: 0.00218
    paper_value: 0.9071
    paper_std: 0.00218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 43
    true_value: 0.9071
    true_std: 0.0021
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9071
    sort_std: 0.0021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: PATTERN
  rows:
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.8668
    std: 0.00034
    paper_value: 0.8668
    paper_std: 0.00034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Beaini 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 1
    true_value: 0.96
    true_std: 0.002
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09319999999999995
    value_note: ''
    paper_rank: 24
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
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
    std: 0.00088
    paper_value: 0.8557
    paper_std: 0.00088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    paper_rank: 36
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.92
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8539
    std: 0.00136
    paper_value: 0.8539
    paper_std: 0.00136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    paper_rank: 38
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.91
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7827
    std: 0.00186
    paper_value: 0.7827
    paper_std: 0.00186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 5
    true_value: 0.9
    true_std: 0.004
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11730000000000007
    value_note: ''
    paper_rank: 44
    rank_delta: 39
    rank_delta_abs: 39
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
    value: 0.7189
    std: 0.00334
    paper_value: 0.7189
    paper_std: 0.00334
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    paper_rank: 45
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.005
    is_best: false
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.87552
    std: 0.00123
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
    global_rank: 8
    sort_value: 0.87552
    sort_std: 0.00123
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
    source_ref: Zhao 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 13
    true_value: 0.8685
    true_std: 0.00057
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8685
    sort_std: 0.00057
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
    value: 0.8685
    std: 0.00037
    paper_value: 0.8685
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 14
    true_value: 0.8685
    true_std: 0.00037
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8685
    sort_std: 0.00037
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.8682
    std: 0.0002
    paper_value: 0.8682
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hussain 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 16
    true_value: 0.86821
    true_std: 0.0002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 1.0000000000065512e-05
    value_note: global 0.8682 within std
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86821
    sort_std: 0.0002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8674
    std: 0.00015
    paper_value: 0.8674
    paper_std: 0.00015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 19
    true_value: 0.8674
    true_std: 0.00015
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8674
    sort_std: 0.00015
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8669
    std: 0.00059
    paper_value: 0.8669
    paper_std: 0.00059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 23
    true_value: 0.8669
    true_std: 0.00059
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8669
    sort_std: 0.00059
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.8658
    std: 0.00037
    paper_value: 0.8658
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 29
    true_value: 0.86581
    true_std: 0.00037
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.99999999995449e-06
    value_note: global 0.8658 within std
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86581
    sort_std: 0.00037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    value: 0.3637
    std: 0.002
    paper_value: 0.3637
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 2
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
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
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.286725
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.3442
    sort_std: 0.0009
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.335
    std: 0.0003
    paper_value: 0.335
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 13
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3341
    std: 0.0006
    paper_value: 0.3341
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 14
    true_value: 0.3341
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3341
    sort_std: 0.0006
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3337
    std: 0.0006
    paper_value: 0.3337
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 16
    true_value: 0.3337
    true_std: 0.0006
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3337
    sort_std: 0.0006
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3242
    std: 0.0008
    paper_value: 0.3242
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 20
    true_value: 0.3242
    true_std: 0.0008
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3242
    sort_std: 0.0008
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GINE
    model_key: gine
    model_plain: GINE
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 23
    true_value: 0.318
    true_std: 0.0027
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.0027
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.3174
    std: 0.002
    paper_value: 0.3174
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 25
    true_value: 0.3174
    true_std: 0.002
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3174
    sort_std: 0.002
    is_best: false
  metric: MRR
  higher_is_better: true
- &id005
  dataset: PascalVOC-SP
  rows:
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.4561
    std: 0.0039
    metric: F1
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
    global_rank: 1
    sort_value: 0.4561
    sort_std: 0.0039
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.4352
    std: 0.003
    metric: F1
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
    global_rank: 2
    sort_value: 0.4352
    sort_std: 0.003
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.4191
    std: 0.0126
    metric: F1
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
    global_rank: 3
    sort_value: 0.4191
    sort_std: 0.0126
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3975
    std: 0.0037
    paper_value: 0.3975
    paper_std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 5
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3748
    std: 0.0109
    paper_value: 0.3748
    paper_std: 0.0109
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 7
    true_value: 0.3748
    true_std: 0.0109
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3748
    sort_std: 0.0109
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.3736
    std: 0.0158
    paper_value: 0.3736
    paper_std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 8
    true_value: 0.3736
    true_std: 0.0158
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3736
    sort_std: 0.0158
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.3724
    std: 0.0131
    paper_value: 0.3724
    paper_std: 0.0131
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 9
    true_value: 0.3724
    true_std: 0.0131
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3724
    sort_std: 0.0131
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.323
    std: 0.0039
    paper_value: 0.323
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 11
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3216
    std: 0.0027
    paper_value: 0.3216
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 12
    true_value: 0.3216
    true_std: 0.0027
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3216
    sort_std: 0.0027
    is_best: false
  - model: GPS (MPNN-only)
    model_key: gps (mpnn-only)
    model_plain: GPS (MPNN-only)
    value: 0.3016
    std: 0.0031
    paper_value: 0.3016
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 18
    true_value: 0.3016
    true_std: 0.0031
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3016
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2873
    std: 0.0219
    paper_value: 0.2873
    paper_std: 0.0219
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 19
    true_value: 0.2873
    true_std: 0.0219
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2873
    sort_std: 0.0219
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.286
    std: 0.0085
    paper_value: 0.286
    paper_std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 21
    true_value: 0.286
    true_std: 0.0085
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.0085
    is_best: false
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.2762
    std: 0.0069
    paper_value: 0.2762
    paper_std: 0.0069
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 23
    true_value: 0.2762
    true_std: 0.0069
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2762
    sort_std: 0.0069
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2694
    std: 0.0098
    paper_value: 0.2694
    paper_std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 24
    true_value: 0.2694
    true_std: 0.0098
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2694
    sort_std: 0.0098
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1268
    std: 0.006
    paper_value: 0.1268
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 36
    true_value: 0.1268
    true_std: 0.006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1268
    sort_std: 0.006
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1265
    std: 0.0076
    paper_value: 0.1265
    paper_std: 0.0076
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 37
    true_value: 0.1265
    true_std: 0.0076
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1265
    sort_std: 0.0076
    is_best: false
  metric: F1
  higher_is_better: true
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 54
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 53
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.6475
    std: 0.0056
    paper_value: 0.6475
    paper_std: 0.0056
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 59
    true_value: 0.6475
    true_std: 0.0056
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6475
    sort_std: 0.0056
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GPS (MPNN-only)
    model_key: gps (mpnn-only)
    model_plain: GPS (MPNN-only)
    value: 0.6159
    std: 0.0048
    paper_value: 0.6159
    paper_std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 73
    true_value: 0.6159
    true_std: 0.0048
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6159
    sort_std: 0.0048
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GPS+BigBird
    model_key: gps+bigbird
    model_plain: GPS+BigBird
    value: 0.5854
    std: 0.0079
    paper_value: 0.5854
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 79
    true_value: 0.5854
    true_std: 0.0079
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5854
    sort_std: 0.0079
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
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 45
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
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
  metric: MAE
  higher_is_better: false
- &id008
  dataset: ogbn-arxiv
  rows:
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: Llama-7b
    model_key: llama-7b
    model_plain: Llama-7b
    value: 0.757
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.757
    sort_std: 0.0012
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.752
    std: 0.002
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
    global_rank: 3
    sort_value: 0.752
    sort_std: 0.002
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7244
    std: 0.0028
    paper_value: 0.7244
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    global_rank: 34
    true_value: 0.7244
    true_std: 0.0028
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7244
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
- benchmark: OGB
  datasets:
  - *id008
- benchmark: GNNBenchmark
  datasets:
  - *id009
  - *id010
  - *id011
single_proposed_model: Exphormer
main_figure: /figures/2303.06147/main_figure.png
---

