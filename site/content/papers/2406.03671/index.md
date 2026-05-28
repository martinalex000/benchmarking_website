---
title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
arxiv_id: '2406.03671'
source_url: ''
authors: []
published_date: Jun 6, 2024
published_date_iso: '2024-06-06'
abstract: Recent research in the field of graph neural network (GNN) has identified
  a critical issue known as "over-squashing," resulting from the bottleneck phenomenon
  in graph structures, which impedes the propagation of long-range information. Prior
  works have proposed a variety of graph rewiring concepts that aim at optimizing
  the spatial or spectral properties of graphs to promote the signal propagation.
  However, such approaches inevitably deteriorate the original graph topology, which
  may lead to a distortion of information flow. To address this, we introduce an expanded
  width-aware (PANDA) message passing, a new message passing paradigm where nodes
  with high centrality, a potential source of over-squashing, are selectively expanded
  in width to encapsulate the growing influx of signals from distant nodes. Experimental
  results show that our method outperforms existing rewiring methods, suggesting that
  selectively expanding the hidden state of nodes can be a compelling alternative
  to graph rewiring for addressing the over-squashing.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN + PANDA
- + PANDA
- PANDA-GCN (Degree)
- PANDA-GCN (Betweenness)
- PANDA-GCN (Closeness)
- PANDA-GCN (PageRank)
- PANDA-GCN (Load)
mrr: 0.0158
adjusted_mrr: 0.0158
mrr_dataset_count: 10
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id012
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8722
    sort_std: 0.0013
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.684
    std: 0.00452
    paper_value: 0.684
    paper_std: 0.00452
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 49
    true_value: 0.7332
    true_std: 0.00814
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04919999999999991
    value_note: ''
    paper_rank: 83
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.7332
    sort_std: 0.00814
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.72992
    std: 0.00384
    paper_value: 0.72992
    paper_std: 0.00384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 53
    true_value: 0.72992
    true_std: 0.00384
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72992
    sort_std: 0.00384
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.684
    std: 0.00452
    paper_value: 0.684
    paper_std: 0.00452
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 84
    true_value: 0.684
    true_std: 0.00452
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.684
    sort_std: 0.00452
    is_best: false
  - model: Closeness
    model_key: closeness
    model_plain: Closeness
    value: 0.684
    std: 0.00452
    paper_value: 0.684
    paper_std: 0.00452
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 85
    true_value: 0.684
    true_std: 0.00452
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.684
    sort_std: 0.00452
    is_best: false
  - model: Degree
    model_key: degree
    model_plain: Degree
    value: 0.68162
    std: 0.00471
    paper_value: 0.68162
    paper_std: 0.00471
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 86
    true_value: 0.68162
    true_std: 0.00471
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68162
    sort_std: 0.00471
    is_best: false
  - model: Betweenness
    model_key: betweenness
    model_plain: Betweenness
    value: 0.67844
    std: 0.00547
    paper_value: 0.67844
    paper_std: 0.00547
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 88
    true_value: 0.67844
    true_std: 0.00547
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67844
    sort_std: 0.00547
    is_best: false
  - model: Load
    model_key: load
    model_plain: Load
    value: 0.67802
    std: 0.00506
    paper_value: 0.67802
    paper_std: 0.00506
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 89
    true_value: 0.67802
    true_std: 0.00506
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67802
    sort_std: 0.00506
    is_best: false
  - model: PageRank
    model_key: pagerank
    model_plain: PageRank
    value: 0.6754
    std: 0.005
    paper_value: 0.6754
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 90
    true_value: 0.6754
    true_std: 0.005
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6754
    sort_std: 0.005
    is_best: false
  - model: + CT-Layer
    model_key: + ct-layer
    model_plain: + CT-Layer
    value: 0.52146
    std: 0.00415
    paper_value: 0.52146
    paper_std: 0.00415
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 94
    true_value: 0.52146
    true_std: 0.00415
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52146
    sort_std: 0.00415
    is_best: false
  - model: Every Layer FA
    model_key: every layer fa
    model_plain: Every Layer FA
    value: 0.51798
    std: 0.00419
    paper_value: 0.51798
    paper_std: 0.00419
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 95
    true_value: 0.51798
    true_std: 0.00419
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51798
    sort_std: 0.00419
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.33836
    std: 0.00584
    paper_value: 0.33836
    paper_std: 0.00584
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 96
    true_value: 0.33836
    true_std: 0.00584
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33836
    sort_std: 0.00584
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.33784
    std: 0.00488
    paper_value: 0.33784
    paper_std: 0.00488
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 97
    true_value: 0.33784
    true_std: 0.00488
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33784
    sort_std: 0.00488
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.33602
    std: 0.01047
    paper_value: 0.33602
    paper_std: 0.01047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 98
    true_value: 0.33602
    true_std: 0.01047
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33602
    sort_std: 0.01047
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.33448
    std: 0.00472
    paper_value: 0.33448
    paper_std: 0.00472
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 99
    true_value: 0.33448
    true_std: 0.00472
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33448
    sort_std: 0.00472
    is_best: false
  - model: Last Layer FA
    model_key: last layer fa
    model_plain: Last Layer FA
    value: 0.3332
    std: 0.00435
    paper_value: 0.3332
    paper_std: 0.00435
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 100
    true_value: 0.3332
    true_std: 0.00435
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3332
    sort_std: 0.00435
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.3305
    std: 0.004
    paper_value: 0.3305
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 101
    true_value: 0.3305
    true_std: 0.004
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3305
    sort_std: 0.004
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.1553
    std: 0.00294
    paper_value: 0.1553
    paper_std: 0.00294
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 102
    true_value: 0.1553
    true_std: 0.00294
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1553
    sort_std: 0.00294
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.753
    std: 0.003
    paper_value: 0.753
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 82
    true_value: 0.753
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.003
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.745
    std: 0.003
    paper_value: 0.745
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 95
    true_value: 0.745
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.003
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.738
    std: 0.002
    paper_value: 0.738
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 102
    true_value: 0.738
    true_std: 0.002
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.002
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.723
    std: 0.004
    paper_value: 0.723
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 106
    true_value: 0.735
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01200000000000001
    value_note: global 0.7350 within std
    paper_rank: 118
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.735
    sort_std: 0.02
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.726
    std: 0.003
    paper_value: 0.726
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 113
    true_value: 0.726
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.723
    std: 0.003
    paper_value: 0.723
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 119
    true_value: 0.723
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.832
    std: 0.002
    paper_value: 0.832
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 29
    true_value: 0.8831
    true_std: 0.0029
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.051100000000000034
    value_note: ''
    paper_rank: 126
    rank_delta: 97
    rank_delta_abs: 97
    rank_delta_direction: worse
    sort_value: 0.8831
    sort_std: 0.0029
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.859
    std: 0.003
    paper_value: 0.859
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 43
    true_value: 0.8794
    true_std: 0.0026
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020399999999999974
    value_note: ''
    paper_rank: 90
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.8794
    sort_std: 0.0026
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.875
    std: 0.002
    paper_value: 0.875
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 44
    true_value: 0.879
    true_std: 0.007
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040000000000000036
    value_note: global 0.8790 within std
    paper_rank: 58
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.007
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.87
    std: 0.003
    paper_value: 0.87
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 68
    true_value: 0.87
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.867
    std: 0.003
    paper_value: 0.867
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 76
    true_value: 0.867
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.867
    sort_std: 0.003
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.863
    std: 0.003
    paper_value: 0.863
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 86
    true_value: 0.864
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.8640 within std
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.864
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.445
    std: 0.012
    paper_value: 0.445
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 105
    true_value: 0.582
    true_std: 0.005
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13699999999999996
    value_note: ''
    paper_rank: 140
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.582
    sort_std: 0.005
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.422
    std: 0.015
    paper_value: 0.422
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 113
    true_value: 0.546
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12400000000000005
    value_note: ''
    paper_rank: 144
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.546
    sort_std: 0.004
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.508
    std: 0.011
    paper_value: 0.508
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 127
    true_value: 0.508
    true_std: 0.011
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.508
    sort_std: 0.011
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.475
    std: 0.014
    paper_value: 0.475
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 133
    true_value: 0.475
    true_std: 0.014
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.475
    sort_std: 0.014
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.415
    std: 0.018
    paper_value: 0.415
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 135
    true_value: 0.468
    true_std: 0.03
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05300000000000005
    value_note: ''
    paper_rank: 144
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.468
    sort_std: 0.03
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.402
    std: 0.016
    paper_value: 0.402
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 138
    true_value: 0.4511
    true_std: 0.0147
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04909999999999998
    value_note: ''
    paper_rank: 145
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.4511
    sort_std: 0.0147
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.355
    std: 0.012
    paper_value: 0.355
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 15
    true_value: 0.584
    true_std: 0.021
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22899999999999998
    value_note: ''
    paper_rank: 61
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.584
    sort_std: 0.021
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.28367
    std: 0.01174
    paper_value: 0.28367
    paper_std: 0.01174
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 22
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21933000000000002
    value_note: ''
    paper_rank: 109
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.35817
    std: 0.01094
    paper_value: 0.35817
    paper_std: 0.01094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 23
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14483000000000001
    value_note: ''
    paper_rank: 61
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.3155
    std: 0.0123
    paper_value: 0.3155
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 36
    true_value: 0.462
    true_std: 0.0141
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14650000000000002
    value_note: ''
    paper_rank: 81
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.462
    sort_std: 0.0141
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.35717
    std: 0.01198
    paper_value: 0.35717
    paper_std: 0.01198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 44
    true_value: 0.415
    true_std: 0.03063
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05782999999999999
    value_note: ''
    paper_rank: 61
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.415
    sort_std: 0.03063
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.338
    std: 0.00115
    paper_value: 0.338
    paper_std: 0.00115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 68
    true_value: 0.338
    true_std: 0.00115
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.338
    sort_std: 0.00115
    is_best: false
  - model: R-GCN + Every Layer FA
    model_key: r-gcn + every layer fa
    model_plain: R-GCN + Every Layer FA
    value: 0.334
    std: 0.01142
    paper_value: 0.334
    paper_std: 0.01142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 71
    true_value: 0.334
    true_std: 0.01142
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.334
    sort_std: 0.01142
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.3057
    std: 0.0142
    paper_value: 0.3057
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 79
    true_value: 0.3175
    true_std: 0.02466
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011799999999999977
    value_note: global 0.3175 within std
    paper_rank: 91
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.3175
    sort_std: 0.02466
    is_best: false
  - model: PANDA-GCN (PageRank)
    model_key: panda-gcn (pagerank)
    model_plain: PANDA-GCN (PageRank)
    value: 0.3155
    std: 0.0123
    paper_value: 0.3155
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 82
    true_value: 0.3155
    true_std: 0.0123
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3155
    sort_std: 0.0123
    is_best: false
  - model: PANDA-GCN (Degree)
    model_key: panda-gcn (degree)
    model_plain: PANDA-GCN (Degree)
    value: 0.31117
    std: 0.01258
    paper_value: 0.31117
    paper_std: 0.01258
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 84
    true_value: 0.31117
    true_std: 0.01258
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31117
    sort_std: 0.01258
    is_best: false
  - model: PANDA-GCN (Closeness)
    model_key: panda-gcn (closeness)
    model_plain: PANDA-GCN (Closeness)
    value: 0.29967
    std: 0.01231
    paper_value: 0.29967
    paper_std: 0.01231
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 94
    true_value: 0.29967
    true_std: 0.01231
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.29967
    sort_std: 0.01231
    is_best: false
  - model: PANDA-GCN (Betweenness)
    model_key: panda-gcn (betweenness)
    model_plain: PANDA-GCN (Betweenness)
    value: 0.296
    std: 0.01208
    paper_value: 0.296
    paper_std: 0.01208
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 97
    true_value: 0.296
    true_std: 0.01208
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.296
    sort_std: 0.01208
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.292
    std: 0.01367
    paper_value: 0.292
    paper_std: 0.01367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 99
    true_value: 0.292
    true_std: 0.013600000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.292
    sort_std: 0.013600000000000001
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.286
    std: 0.01186
    paper_value: 0.286
    paper_std: 0.01186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 104
    true_value: 0.286
    true_std: 0.01186
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.01186
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.286
    std: 0.01186
    paper_value: 0.286
    paper_std: 0.01186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 105
    true_value: 0.286
    true_std: 0.01186
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.01186
    is_best: false
  - model: Every Layer FA
    model_key: every layer fa
    model_plain: Every Layer FA
    value: 0.28383
    std: 0.01052
    paper_value: 0.28383
    paper_std: 0.01052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 109
    true_value: 0.28383
    true_std: 0.01052
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28383
    sort_std: 0.01052
    is_best: false
  - model: GCN + Last Layer FA
    model_key: gcn + last layer fa
    model_plain: GCN + Last Layer FA
    value: 0.28233
    std: 0.01138
    paper_value: 0.28233
    paper_std: 0.01138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 111
    true_value: 0.28233
    true_std: 0.01138
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28233
    sort_std: 0.01138
    is_best: false
  - model: PANDA-GCN (Load)
    model_key: panda-gcn (load)
    model_plain: PANDA-GCN (Load)
    value: 0.28167
    std: 0.0109
    paper_value: 0.28167
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 112
    true_value: 0.28167
    true_std: 0.0109
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28167
    sort_std: 0.0109
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.2752
    std: 0.0099
    paper_value: 0.2752
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 116
    true_value: 0.2752
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2752
    sort_std: 0.009899999999999999
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.25067
    std: 0.00994
    paper_value: 0.25067
    paper_std: 0.00994
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 123
    true_value: 0.25067
    true_std: 0.00994
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25067
    sort_std: 0.00994
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.16583
    std: 0.00907
    paper_value: 0.16583
    paper_std: 0.00907
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 129
    true_value: 0.16583
    true_std: 0.00907
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.16583
    sort_std: 0.00907
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    codebase_url: ''
    uses_external_data: false
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.713
    std: 0.015
    paper_value: 0.713
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 79
    true_value: 0.713
    true_std: 0.015
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.713
    sort_std: 0.015
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7128
    std: 0.0086
    paper_value: 0.7128
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 80
    true_value: 0.7128
    true_std: 0.0086
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7128
    sort_std: 0.0086
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.7121
    std: 0.00919
    paper_value: 0.7121
    paper_std: 0.00919
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 81
    true_value: 0.7121
    true_std: 0.00919
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7121
    sort_std: 0.00919
    is_best: false
  - model: GCN + Last Layer FA
    model_key: gcn + last layer fa
    model_plain: GCN + Last Layer FA
    value: 0.7091
    std: 0.00788
    paper_value: 0.7091
    paper_std: 0.00788
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 88
    true_value: 0.7091
    true_std: 0.00788
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7091
    sort_std: 0.00788
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.7018
    std: 0.00992
    paper_value: 0.7018
    paper_std: 0.00992
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 99
    true_value: 0.7018000000000001
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7018000000000001
    sort_std: 0.009899999999999999
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.6972
    std: 0.01152
    paper_value: 0.6972
    paper_std: 0.01152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 106
    true_value: 0.6972
    true_std: 0.01152
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6972
    sort_std: 0.01152
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.6376
    std: 0.01012
    paper_value: 0.6376
    paper_std: 0.01012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 109
    true_value: 0.6835
    true_std: 0.02346
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04590000000000005
    value_note: ''
    paper_rank: 129
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.6835
    sort_std: 0.02346
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.6439
    std: 0.00907
    paper_value: 0.6439
    paper_std: 0.00907
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 126
    true_value: 0.6439
    true_std: 0.00907
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6439
    sort_std: 0.00907
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.6376
    std: 0.01012
    paper_value: 0.6376
    paper_std: 0.01012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 130
    true_value: 0.6376
    true_std: 0.0101
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6376
    sort_std: 0.0101
    is_best: false
  - model: PANDA-GCN (PageRank)
    model_key: panda-gcn (pagerank)
    model_plain: PANDA-GCN (PageRank)
    value: 0.6376
    std: 0.01012
    paper_value: 0.6376
    paper_std: 0.01012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 131
    true_value: 0.6376
    true_std: 0.01012
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6376
    sort_std: 0.01012
    is_best: false
  - model: PANDA-GCN (Degree)
    model_key: panda-gcn (degree)
    model_plain: PANDA-GCN (Degree)
    value: 0.621
    std: 0.01043
    paper_value: 0.621
    paper_std: 0.01043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 134
    true_value: 0.621
    true_std: 0.01043
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.621
    sort_std: 0.01043
    is_best: false
  - model: PANDA-GCN (Closeness)
    model_key: panda-gcn (closeness)
    model_plain: PANDA-GCN (Closeness)
    value: 0.6116
    std: 0.00992
    paper_value: 0.6116
    paper_std: 0.00992
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 135
    true_value: 0.6116
    true_std: 0.00992
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6116
    sort_std: 0.00992
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.4992
    std: 0.0099
    paper_value: 0.4992
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 137
    true_value: 0.607
    true_std: 0.02079
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1078
    value_note: ''
    paper_rank: 156
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.607
    sort_std: 0.02079
    is_best: false
  - model: PANDA-GCN (Load)
    model_key: panda-gcn (load)
    model_plain: PANDA-GCN (Load)
    value: 0.5984
    std: 0.01153
    paper_value: 0.5984
    paper_std: 0.01153
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 139
    true_value: 0.5984
    true_std: 0.01153
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5984
    sort_std: 0.01153
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.4966
    std: 0.00864
    paper_value: 0.4966
    paper_std: 0.00864
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 140
    true_value: 0.5975
    true_std: 0.02357
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10090000000000005
    value_note: ''
    paper_rank: 159
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.5975
    sort_std: 0.02357
    is_best: false
  - model: PANDA-GCN (Betweenness)
    model_key: panda-gcn (betweenness)
    model_plain: PANDA-GCN (Betweenness)
    value: 0.5963
    std: 0.01152
    paper_value: 0.5963
    paper_std: 0.01152
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 142
    true_value: 0.5963
    true_std: 0.01152
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5963
    sort_std: 0.01152
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.494
    std: 0.00904
    paper_value: 0.494
    paper_std: 0.00904
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 143
    true_value: 0.59
    true_std: 0.02254
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09599999999999997
    value_note: ''
    paper_rank: 159
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.59
    sort_std: 0.02254
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.50012
    std: 0.00917
    paper_value: 0.50012
    paper_std: 0.00917
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 155
    true_value: 0.50012
    true_std: 0.00917
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.50012
    sort_std: 0.00917
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.5
    std: 0.00974
    paper_value: 0.5
    paper_std: 0.00974
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 156
    true_value: 0.5
    true_std: 0.00974
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5
    sort_std: 0.00974
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.4977
    std: 0.00817
    paper_value: 0.4977
    paper_std: 0.00817
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 158
    true_value: 0.49770000000000003
    true_std: 0.008100000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49770000000000003
    sort_std: 0.008100000000000001
    is_best: false
  - model: Every Layer FA
    model_key: every layer fa
    model_plain: Every Layer FA
    value: 0.4916
    std: 0.0087
    paper_value: 0.4916
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 160
    true_value: 0.4916
    true_std: 0.0087
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4916
    sort_std: 0.0087
    is_best: false
  - model: R-GCN + Every Layer FA
    model_key: r-gcn + every layer fa
    model_plain: R-GCN + Every Layer FA
    value: 0.4916
    std: 0.0087
    paper_value: 0.4916
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 161
    true_value: 0.4916
    true_std: 0.0087
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4916
    sort_std: 0.0087
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.76
    std: 0.00774
    paper_value: 0.76
    paper_std: 0.00774
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 37
    true_value: 0.76
    true_std: 0.00774
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.00774
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.76
    std: 0.00774
    paper_value: 0.76
    paper_std: 0.00774
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 40
    true_value: 0.76
    true_std: 0.00774
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.00774
    is_best: false
  - model: PANDA-GCN (Closeness)
    model_key: panda-gcn (closeness)
    model_plain: PANDA-GCN (Closeness)
    value: 0.76
    std: 0.00774
    paper_value: 0.76
    paper_std: 0.00774
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 41
    true_value: 0.76
    true_std: 0.00774
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.00774
    is_best: false
  - model: PANDA-GCN (Degree)
    model_key: panda-gcn (degree)
    model_plain: PANDA-GCN (Degree)
    value: 0.75375
    std: 0.008
    paper_value: 0.75375
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 52
    true_value: 0.75375
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75375
    sort_std: 0.008
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.75107
    std: 0.00817
    paper_value: 0.75107
    paper_std: 0.00817
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 63
    true_value: 0.75107
    true_std: 0.00817
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75107
    sort_std: 0.00817
    is_best: false
  - model: PANDA-GCN (Betweenness)
    model_key: panda-gcn (betweenness)
    model_plain: PANDA-GCN (Betweenness)
    value: 0.74589
    std: 0.00791
    paper_value: 0.74589
    paper_std: 0.00791
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 78
    true_value: 0.74589
    true_std: 0.00791
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74589
    sort_std: 0.00791
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.742
    std: 0.008
    paper_value: 0.742
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 83
    true_value: 0.742
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.008
    is_best: false
  - model: PANDA-GCN (Load)
    model_key: panda-gcn (load)
    model_plain: PANDA-GCN (Load)
    value: 0.74188
    std: 0.00814
    paper_value: 0.74188
    paper_std: 0.00814
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 88
    true_value: 0.74188
    true_std: 0.00814
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74188
    sort_std: 0.00814
    is_best: false
  - model: PANDA-GCN (PageRank)
    model_key: panda-gcn (pagerank)
    model_plain: PANDA-GCN (PageRank)
    value: 0.74098
    std: 0.00851
    paper_value: 0.74098
    paper_std: 0.00851
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 91
    true_value: 0.74098
    true_std: 0.00851
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74098
    sort_std: 0.00851
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.7342
    std: 0.00811
    paper_value: 0.7342
    paper_std: 0.00811
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 105
    true_value: 0.7342
    true_std: 0.008100000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7342
    sort_std: 0.008100000000000001
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.7313
    std: 0.0069
    paper_value: 0.7313
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 113
    true_value: 0.7313
    true_std: 0.0069
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7313
    sort_std: 0.0069
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.7259
    std: 0.0248
    paper_value: 0.7259
    paper_std: 0.0248
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 122
    true_value: 0.72991
    true_std: 0.01956
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004009999999999958
    value_note: global 0.7299 within std
    paper_rank: 133
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.72991
    sort_std: 0.01956
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7092
    std: 0.00792
    paper_value: 0.7092
    paper_std: 0.00792
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 124
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01980000000000004
    value_note: ''
    paper_rank: 167
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.69813
    std: 0.00792
    paper_value: 0.69813
    paper_std: 0.00792
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 125
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.030870000000000064
    value_note: ''
    paper_rank: 179
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.70759
    std: 0.00774
    paper_value: 0.70759
    paper_std: 0.00774
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 138
    true_value: 0.72321
    true_std: 0.0144
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.015619999999999967
    value_note: ''
    paper_rank: 171
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.72321
    sort_std: 0.0144
    is_best: false
  - model: GCN + Last Layer FA
    model_key: gcn + last layer fa
    model_plain: GCN + Last Layer FA
    value: 0.72304
    std: 0.00666
    paper_value: 0.72304
    paper_std: 0.00666
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 139
    true_value: 0.72304
    true_std: 0.00666
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72304
    sort_std: 0.00666
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.70982
    std: 0.00737
    paper_value: 0.70982
    paper_std: 0.00737
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 167
    true_value: 0.70982
    true_std: 0.00737
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70982
    sort_std: 0.00737
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.70804
    std: 0.00827
    paper_value: 0.70804
    paper_std: 0.00827
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 170
    true_value: 0.70804
    true_std: 0.00827
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70804
    sort_std: 0.00827
    is_best: false
  - model: R-GCN + Every Layer FA
    model_key: r-gcn + every layer fa
    model_plain: R-GCN + Every Layer FA
    value: 0.70375
    std: 0.0091
    paper_value: 0.70375
    paper_std: 0.0091
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 175
    true_value: 0.70375
    true_std: 0.0091
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70375
    sort_std: 0.0091
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.69518
    std: 0.00725
    paper_value: 0.69518
    paper_std: 0.00725
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 182
    true_value: 0.69518
    true_std: 0.00725
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69518
    sort_std: 0.00725
    is_best: false
  - model: GCN + CT-Layer
    model_key: gcn + ct-layer
    model_plain: GCN + CT-Layer
    value: 0.61107
    std: 0.01184
    paper_value: 0.61107
    paper_std: 0.01184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 197
    true_value: 0.61107
    true_std: 0.01184
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61107
    sort_std: 0.01184
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.554
    std: 0.016
    paper_value: 0.554
    paper_std: 0.016
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 244
    true_value: 0.6028
    true_std: 0.0031
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048799999999999955
    value_note: ''
    paper_rank: 286
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.6028
    sort_std: 0.0031
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.456
    std: 0.015
    paper_value: 0.456
    paper_std: 0.015
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 251
    true_value: 0.5993999999999999
    true_std: 0.0037
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14339999999999992
    value_note: ''
    paper_rank: 305
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.5993999999999999
    sort_std: 0.0037
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.439
    std: 0.016
    paper_value: 0.439
    paper_std: 0.016
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 257
    true_value: 0.5947
    true_std: 0.0126
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1557
    value_note: ''
    paper_rank: 307
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.5947
    sort_std: 0.0126
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.46
    std: 0.016
    paper_value: 0.46
    paper_std: 0.016
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 258
    true_value: 0.5947
    true_std: 0.0034999999999999996
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1347
    value_note: ''
    paper_rank: 304
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.5947
    sort_std: 0.0034999999999999996
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.442
    std: 0.015
    paper_value: 0.442
    paper_std: 0.015
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 262
    true_value: 0.593
    true_std: 0.0023
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15099999999999997
    value_note: ''
    paper_rank: 307
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.593
    sort_std: 0.0023
    is_best: false
  metric: AP
  higher_is_better: true
- &id008
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
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.3272
    std: 0.0001
    paper_value: 0.3272
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 288
    true_value: 0.3272
    true_std: 0.0001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 288
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3272
    sort_std: 0.0001
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.3473
    std: 0.0007
    paper_value: 0.3473
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 302
    true_value: 0.3473
    true_std: 0.0007
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 302
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3473
    sort_std: 0.0007
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.3478
    std: 0.0013
    paper_value: 0.3478
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 303
    true_value: 0.3478
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 303
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3478
    sort_std: 0.0013
    is_best: false
  - model: GCN
    model_key: gcn (none)
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
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 305
    true_value: 0.3496
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 305
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3496
    sort_std: 0.0013
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.3514
    std: 0.0009
    paper_value: 0.3514
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 308
    true_value: 0.3514
    true_std: 0.0009
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3514
    sort_std: 0.0009
    is_best: false
  metric: MAE
  higher_is_better: false
- &id013
  dataset: REDDIT-BINARY
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9199
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9199
    sort_std: 0.0159
    is_best: false
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.86785
    std: 0.01056
    paper_value: 0.86785
    paper_std: 0.01056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 12
    true_value: 0.86785
    true_std: 0.01056
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86785
    sort_std: 0.01056
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.8069
    std: 0.00721
    paper_value: 0.8069
    paper_std: 0.00721
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 22
    true_value: 0.8069
    true_std: 0.00721
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8069
    sort_std: 0.00721
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.8069
    std: 0.00721
    paper_value: 0.8069
    paper_std: 0.00721
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 21
    true_value: 0.8069
    true_std: 0.00721
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8069
    sort_std: 0.00721
    is_best: false
  - model: PANDA-GCN (Degree)
    model_key: panda-gcn (degree)
    model_plain: PANDA-GCN (Degree)
    value: 0.8069
    std: 0.00721
    paper_value: 0.8069
    paper_std: 0.00721
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 23
    true_value: 0.8069
    true_std: 0.00721
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8069
    sort_std: 0.00721
    is_best: false
  - model: PANDA-GCN (PageRank)
    model_key: panda-gcn (pagerank)
    model_plain: PANDA-GCN (PageRank)
    value: 0.8034
    std: 0.00826
    paper_value: 0.8034
    paper_std: 0.00826
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 24
    true_value: 0.8034
    true_std: 0.00826
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8034
    sort_std: 0.00826
    is_best: false
  - model: PANDA-GCN (Betweenness)
    model_key: panda-gcn (betweenness)
    model_plain: PANDA-GCN (Betweenness)
    value: 0.8
    std: 0.00659
    paper_value: 0.8
    paper_std: 0.00659
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 25
    true_value: 0.8
    true_std: 0.00659
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.00659
    is_best: false
  - model: PANDA-GCN (Closeness)
    model_key: panda-gcn (closeness)
    model_plain: PANDA-GCN (Closeness)
    value: 0.797
    std: 0.00664
    paper_value: 0.797
    paper_std: 0.00664
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 26
    true_value: 0.797
    true_std: 0.00664
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.00664
    is_best: false
  - model: PANDA-GCN (Load)
    model_key: panda-gcn (load)
    model_plain: PANDA-GCN (Load)
    value: 0.795
    std: 0.00732
    paper_value: 0.795
    paper_std: 0.00732
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 27
    true_value: 0.795
    true_std: 0.00732
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.00732
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.7033
    std: 0.00727
    paper_value: 0.7033
    paper_std: 0.00727
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 29
    true_value: 0.7033
    true_std: 0.00727
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7033
    sort_std: 0.00727
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.6899
    std: 0.0061
    paper_value: 0.6899
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 30
    true_value: 0.6899
    true_std: 0.0061
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6899
    sort_std: 0.0061
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.6862
    std: 0.00851
    paper_value: 0.6862
    paper_std: 0.00851
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 31
    true_value: 0.6862
    true_std: 0.00851
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6862
    sort_std: 0.00851
    is_best: false
  - model: Last Layer FA
    model_key: last layer fa
    model_plain: Last Layer FA
    value: 0.68485
    std: 0.00945
    paper_value: 0.68485
    paper_std: 0.00945
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 32
    true_value: 0.68485
    true_std: 0.00945
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68485
    sort_std: 0.00945
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.68255
    std: 0.01098
    paper_value: 0.68255
    paper_std: 0.01098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 33
    true_value: 0.68255
    true_std: 0.01098
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68255
    sort_std: 0.01098
    is_best: false
  - model: + CT-Layer
    model_key: + ct-layer
    model_plain: + CT-Layer
    value: 0.5158
    std: 0.01019
    paper_value: 0.5158
    paper_std: 0.01019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 34
    true_value: 0.5158
    true_std: 0.01019
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5158
    sort_std: 0.01019
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.4998
    std: 0.0068
    paper_value: 0.4998
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 37
    true_value: 0.4998
    true_std: 0.0068
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4998
    sort_std: 0.0068
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.4985
    std: 0.00653
    paper_value: 0.4985
    paper_std: 0.00653
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 38
    true_value: 0.4985
    true_std: 0.00653
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4985
    sort_std: 0.00653
    is_best: false
  - model: Every Layer FA
    model_key: every layer fa
    model_plain: Every Layer FA
    value: 0.4849
    std: 0.01044
    paper_value: 0.4849
    paper_std: 0.01044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 39
    true_value: 0.4849
    true_std: 0.01044
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4849
    sort_std: 0.01044
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7601
    sort_std: 0.019
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7531
    std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7531
    sort_std: 0.0192
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.741
    std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.425
    std: 0.019
    paper_value: 0.425
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 34
    true_value: 0.5263
    true_std: 0.003
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1013
    value_note: ''
    paper_rank: 63
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.5263
    sort_std: 0.003
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.431
    std: 0.009
    paper_value: 0.431
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 61
    true_value: 0.431
    true_std: 0.009
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.431
    sort_std: 0.009
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.426
    std: 0.028
    paper_value: 0.426
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 63
    true_value: 0.426
    true_std: 0.028
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.426
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.425
    std: 0.027
    paper_value: 0.425
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 65
    true_value: 0.425
    true_std: 0.027
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.425
    sort_std: 0.027
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.424
    std: 0.025
    paper_value: 0.424
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 66
    true_value: 0.424
    true_std: 0.025
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.424
    sort_std: 0.025
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.352
    std: 0.03
    paper_value: 0.352
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 76
    true_value: 0.4053
    true_std: 0.0029
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.053300000000000014
    value_note: ''
    paper_rank: 102
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.4053
    sort_std: 0.0029
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.439
    std: 0.016
    paper_value: 0.439
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 131
    true_value: 0.644
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20500000000000002
    value_note: ''
    paper_rank: 169
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.644
    sort_std: 0.004
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.536
    std: 0.015
    paper_value: 0.536
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 140
    true_value: 0.62
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08399999999999996
    value_note: ''
    paper_rank: 162
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.62
    sort_std: 0.003
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.46
    std: 0.016
    paper_value: 0.46
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 141
    true_value: 0.6135
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15350000000000003
    value_note: ''
    paper_rank: 168
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.6135
    sort_std: 0.0125
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.494
    std: 0.012
    paper_value: 0.494
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 155
    true_value: 0.563
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06899999999999995
    value_note: ''
    paper_rank: 165
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.0161
    is_best: false
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.554
    std: 0.016
    paper_value: 0.554
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 159
    true_value: 0.554
    true_std: 0.016
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.016
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.442
    std: 0.015
    paper_value: 0.442
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 169
    true_value: 0.442
    true_std: 0.015
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.442
    sort_std: 0.015
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: + PANDA
    model_key: + panda
    model_plain: + PANDA
    value: 0.582
    std: 0.014
    paper_value: 0.582
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 120
    true_value: 0.582
    true_std: 0.014
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.582
    sort_std: 0.014
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.483
    std: 0.013
    paper_value: 0.483
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 125
    true_value: 0.556
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07300000000000006
    value_note: ''
    paper_rank: 137
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.556
    sort_std: 0.0125
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.462
    std: 0.012
    paper_value: 0.462
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 126
    true_value: 0.555
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09300000000000003
    value_note: ''
    paper_rank: 139
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.555
    sort_std: 0.003
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.503
    std: 0.009
    paper_value: 0.503
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 127
    true_value: 0.5537
    true_std: 0.0147
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05069999999999997
    value_note: ''
    paper_rank: 136
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.5537
    sort_std: 0.0147
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.517
    std: 0.013
    paper_value: 0.517
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 135
    true_value: 0.517
    true_std: 0.013
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.517
    sort_std: 0.013
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.446
    std: 0.014
    paper_value: 0.446
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 6, 2024
    date_display: Jun 2024
    date_iso: '2024-06-06'
    global_rank: 140
    true_value: 0.446
    true_std: 0.014
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.446
    sort_std: 0.014
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: Heterophilic Graphs
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
- benchmark: TU Dortmund
  datasets:
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
main_figure: /figures/2406.03671/main_figure.png
---

