---
title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
arxiv_id: '2508.05070'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
abstract: We introduce Tango -- a dynamical systems inspired framework for graph representation
  learning that governs node feature evolution through a learned energy landscape
  and its associated descent dynamics. At the core of our approach is a learnable
  Lyapunov function over node embeddings, whose gradient defines an energy-reducing
  direction that guarantees convergence and stability. To enhance flexibility while
  preserving the benefits of energy-based dynamics, we incorporate a novel tangential
  component, learned via message passing, that evolves features while maintaining
  the energy value. This decomposition into orthogonal flows of energy gradient descent
  and tangential evolution yields a flexible form of graph dynamics, and enables effective
  signal propagation even in flat or ill-conditioned energy regions, that often appear
  in graph learning. Our method mitigates oversquashing and is compatible with different
  graph neural network backbones. Empirically, Tango achieves strong performance across
  a diverse set of node and graph classification and regression benchmarks, demonstrating
  the effectiveness of jointly learned energy functions and tangential flows for graph
  neural networks.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Tango_GatedGCN
- Tango_GPS
mrr: 0.1703
adjusted_mrr: 0.1703
mrr_dataset_count: 12
benchmark_categories:
- Classic
- Heterophilic Graphs
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
- &id003
  dataset: Amazon-ratings
  rows:
  - model: here instead
    model_key: here instead
    model_plain: here instead
    value: 0.909
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.909
    sort_std: null
    is_best: true
  - model: CT
    model_key: ct
    model_plain: CT
    value: 0.848
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.848
    sort_std: null
    is_best: false
  - model: WNN
    model_key: wnn
    model_plain: WNN
    value: 0.843
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.843
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.487
    std: 0.0063
    paper_value: 0.487
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.8326
    true_std: 0.0051
    value_gap_source_arxiv: '2410.10320'
    value_gap_source_title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3456
    value_note: ''
    paper_rank: 46
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.8326
    sort_std: 0.0051
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4909
    std: 0.0063
    paper_value: 0.4909
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 12
    true_value: 0.8016
    true_std: 0.0232
    value_gap_source_arxiv: '2410.10320'
    value_gap_source_title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3107
    value_note: ''
    paper_rank: 45
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.8016
    sort_std: 0.0232
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.5417
    std: 0.0037
    paper_value: 0.5417
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.5417
    true_std: 0.0037
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5417
    sort_std: 0.0037
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.5383
    std: 0.0032
    paper_value: 0.5383
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
    true_value: 0.5383
    true_std: 0.0032
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5383
    sort_std: 0.0032
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5363
    std: 0.0039
    paper_value: 0.5363
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
    true_value: 0.5363
    true_std: 0.0039
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.5351
    std: 0.0046
    paper_value: 0.5351
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
    true_value: 0.5351
    true_std: 0.0046
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5351
    sort_std: 0.0046
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.5274
    std: 0.0083
    paper_value: 0.5274
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
    true_value: 0.5274
    true_std: 0.0083
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5274
    sort_std: 0.0083
    is_best: false
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.526
    std: 0.0053
    paper_value: 0.526
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.526
    true_std: 0.0053
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.526
    sort_std: 0.0053
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.5218
    std: 0.008
    paper_value: 0.5218
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.5218
    true_std: 0.008
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5218
    sort_std: 0.008
    is_best: false
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.5128
    std: 0.0056
    paper_value: 0.5128
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.5128
    true_std: 0.0056
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5128
    sort_std: 0.0056
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.5126
    std: 0.0072
    paper_value: 0.5126
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 39
    true_value: 0.5126
    true_std: 0.0072
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5126
    sort_std: 0.0072
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5117
    std: 0.0066
    paper_value: 0.5117
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 40
    true_value: 0.5117
    true_std: 0.0066
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  - model: GPS_GCNI+Performer (RWSE)
    model_key: gps_gcni+performer (rwse)
    model_plain: GPS_GCNI+Performer (RWSE)
    value: 0.4992
    std: 0.0068
    paper_value: 0.4992
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 44
    true_value: 0.4992
    true_std: 0.0068
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4992
    sort_std: 0.0068
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.43
    std: 0.0032
    paper_value: 0.43
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 49
    true_value: 0.481
    true_std: 0.0071
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 76
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.481
    sort_std: 0.0071
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.4598
    std: 0.0071
    paper_value: 0.4598
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 56
    true_value: 0.4598
    true_std: 0.0071
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4598
    sort_std: 0.0071
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.4488
    std: 0.0034
    paper_value: 0.4488
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 63
    true_value: 0.4488
    true_std: 0.0034
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4488
    sort_std: 0.0034
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.4461
    std: 0.005
    paper_value: 0.4461
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 65
    true_value: 0.4461
    true_std: 0.005
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4461
    sort_std: 0.005
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4412
    std: 0.003
    paper_value: 0.4412
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 69
    true_value: 0.4412
    true_std: 0.003
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4412
    sort_std: 0.003
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.4355
    std: 0.0048
    paper_value: 0.4355
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 75
    true_value: 0.4355
    true_std: 0.0048
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4355
    sort_std: 0.0048
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.3689
    std: 0.0014
    paper_value: 0.3689
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 84
    true_value: 0.419
    true_std: 0.0067
    value_gap_source_arxiv: '2601.01207'
    value_gap_source_title: Sparse Bayesian Message Passing under Structural Uncertainty
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05009999999999998
    value_note: ''
    paper_rank: 89
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.419
    sort_std: 0.0067
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
    value: 0.72838
    std: 0.00417
    paper_value: 0.72838
    paper_std: 0.00417
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: beaini2021directional
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.92
    true_std: 0.007
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19162
    value_note: ''
    paper_rank: 21
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.92
    sort_std: 0.007
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7035
    std: 0.0063
    paper_value: 0.7035
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PNA
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.91
    true_std: 0.008
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20650000000000002
    value_note: ''
    paper_rank: 31
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.88
    std: 0.01
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
    global_rank: 7
    sort_value: 0.88
    sort_std: 0.01
    is_best: false
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.78068
    std: 0.00785
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
    sort_value: 0.78068
    sort_std: 0.00785
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.76468
    std: 0.00881
    paper_value: 0.76468
    paper_std: 0.00881
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 12
    true_value: 0.76468
    true_std: 0.00881
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76468
    sort_std: 0.00881
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.75783
    std: 0.00261
    paper_value: 0.75783
    paper_std: 0.00261
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.75783
    true_std: 0.00261
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75783
    sort_std: 0.00261
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.72298
    std: 0.00356
    paper_value: 0.72298
    paper_std: 0.00356
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022graphgps
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 23
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.7230 within std
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 26
    true_value: 0.7219
    true_std: 0.0013
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
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
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.70894
    std: 0.00329
    paper_value: 0.70894
    paper_std: 0.00329
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
    true_value: 0.70894
    true_std: 0.00329
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70894
    sort_std: 0.00329
    is_best: false
  - model: CRaW1
    model_key: craw1
    model_plain: CRaW1
    value: 0.69013
    std: 0.00259
    paper_value: 0.69013
    paper_std: 0.00259
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonnshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.69013
    true_std: 0.00259
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69013
    sort_std: 0.00259
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
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: gatedgcn
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
- &id012
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.80113
    std: 0.00138
    paper_value: 0.80113
    paper_std: 0.00138
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.80113
    true_std: 0.00138
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.80113
    sort_std: 0.00138
    is_best: true
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.80026
    std: 0.00277
    paper_value: 0.80026
    paper_std: 0.00277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.80026
    true_std: 0.00277
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.79571
    std: 0.00122
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
    global_rank: 4
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
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.79232
    true_std: 0.00348
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
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
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.78194
    std: 0.00307
    paper_value: 0.78194
    paper_std: 0.00307
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.78194
    true_std: 0.00307
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78194
    sort_std: 0.00307
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.78016
    std: 0.0018
    paper_value: 0.78016
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022graphgps
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
    true_value: 0.78016
    true_std: 0.0018
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78016
    sort_std: 0.0018
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.76691
    std: 0.0065
    paper_value: 0.76691
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
    true_value: 0.76691
    true_std: 0.0065
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
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
    source_ref: gatedgcn
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
- &id009
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
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.98197
    std: 0.0011
    paper_value: 0.98197
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
    true_value: 0.98197
    true_std: 0.0011
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98197
    sort_std: 0.0011
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
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.98108
    std: 0.00111
    paper_value: 0.98108
    paper_std: 0.00111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
    true_value: 0.98108
    true_std: 0.00111
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98108
    sort_std: 0.00111
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
    source_ref: PNA
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.981
    true_std: 0.002
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.9810 within std
    paper_rank: 38
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.981
    sort_std: 0.002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.98051
    std: 0.00126
    paper_value: 0.98051
    paper_std: 0.00126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022graphgps
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
    true_value: 0.98082
    true_std: 0.00114
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00031000000000003247
    value_note: global 0.9808 within std
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98082
    sort_std: 0.00114
    is_best: false
  - model: CRaW1
    model_key: craw1
    model_plain: CRaW1
    value: 0.97944
    std: 0.0005
    paper_value: 0.97944
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonnshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.97944
    true_std: 0.0005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.97944
    sort_std: 0.0005
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
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.97788
    std: 0.00105
    paper_value: 0.97788
    paper_std: 0.00105
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
    true_value: 0.97788
    true_std: 0.00105
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.97788
    sort_std: 0.00105
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
    source_ref: gatedgcn
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9907
    std: 0.0025
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
    global_rank: 1
    sort_value: 0.9907
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
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.9839
    std: 0.0054
    paper_value: 0.9839
    paper_std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.9839
    true_std: 0.0054
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.9832
    std: 0.0059
    paper_value: 0.9832
    paper_std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.9832
    true_std: 0.0059
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9832
    sort_std: 0.0059
    is_best: true
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.9735
    std: 0.0063
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
    global_rank: 5
    sort_value: 0.9735
    sort_std: 0.0063
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.9731
    std: 0.0041
    paper_value: 0.9731
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.9731
    true_std: 0.0041
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9731
    sort_std: 0.0041
    is_best: false
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.9509
    std: 0.0118
    paper_value: 0.9509
    paper_std: 0.0118
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.9509
    true_std: 0.0118
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9509
    sort_std: 0.0118
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.9229
    std: 0.0047
    paper_value: 0.9229
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 11
    true_value: 0.9229
    true_std: 0.0047
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9229
    sort_std: 0.0047
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.9201
    true_std: 0.0068
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9201
    sort_std: 0.0068
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
  - model: GPS_GCNI+Performer (RWSE)
    model_key: gps_gcni+performer (rwse)
    model_plain: GPS_GCNI+Performer (RWSE)
    value: 0.9108
    std: 0.0058
    paper_value: 0.9108
    paper_std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 15
    true_value: 0.9108
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9108
    sort_std: 0.0058
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.9085
    std: 0.0058
    paper_value: 0.9085
    paper_std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
    true_value: 0.9085
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9085
    sort_std: 0.0058
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9074
    std: 0.0053
    paper_value: 0.9074
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
    true_value: 0.9074
    true_std: 0.0053
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9074
    sort_std: 0.0053
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8754
    std: 0.0122
    paper_value: 0.8754
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 18
    true_value: 0.905
    true_std: 0.0016
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02960000000000007
    value_note: ''
    paper_rank: 24
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.905
    sort_std: 0.0016
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.8419
    std: 0.0066
    paper_value: 0.8419
    paper_std: 0.0066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
    true_value: 0.903
    true_std: 0.0006
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06110000000000004
    value_note: ''
    paper_rank: 37
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.903
    sort_std: 0.0006
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.9008
    std: 0.007
    paper_value: 0.9008
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
    true_value: 0.9008
    true_std: 0.007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9008
    sort_std: 0.007
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 21
    true_value: 0.8975
    true_std: 0.0052
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8975
    sort_std: 0.0052
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8966
    std: 0.004
    paper_value: 0.8966
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.8966
    true_std: 0.004
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8966
    sort_std: 0.004
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8817
    std: 0.0073
    paper_value: 0.8817
    paper_std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
    true_value: 0.8817
    true_std: 0.0073
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8817
    sort_std: 0.0073
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.8624
    std: 0.0061
    paper_value: 0.8624
    paper_std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
    true_value: 0.8624
    true_std: 0.0061
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8624
    sort_std: 0.0061
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.5108
    std: 0.0123
    paper_value: 0.5108
    paper_std: 0.0123
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
    true_value: 0.857
    true_std: 0.0127
    value_gap_source_arxiv: '2601.01207'
    value_gap_source_title: Sparse Bayesian Message Passing under Structural Uncertainty
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.34619999999999995
    value_note: ''
    paper_rank: 38
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.857
    sort_std: 0.0127
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8109
    std: 0.0102
    paper_value: 0.8109
    paper_std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.8109
    true_std: 0.0102
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8109
    sort_std: 0.0102
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id010
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
    source_ref: beaini2021directional
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    paper_rank: 29
    rank_delta: 28
    rank_delta_abs: 28
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
    source_ref: gatedgcn
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.87196
    std: 0.00076
    paper_value: 0.87196
    paper_std: 0.00076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 12
    true_value: 0.87196
    true_std: 0.00076
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87196
    sort_std: 0.00076
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.87182
    std: 0.00063
    paper_value: 0.87182
    paper_std: 0.00063
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.87182
    true_std: 0.00063
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87182
    sort_std: 0.00063
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
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.86685
    std: 0.00059
    paper_value: 0.86685
    paper_std: 0.00059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022graphgps
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 29
    true_value: 0.86688
    true_std: 0.00073
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.8669 within std
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86688
    sort_std: 0.00073
    is_best: false
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.86672
    std: 0.00071
    paper_value: 0.86672
    paper_std: 0.00071
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 31
    true_value: 0.86672
    true_std: 0.00071
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86672
    sort_std: 0.00071
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
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
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.86581
    true_std: 0.00037
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86581
    sort_std: 0.00037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: DRew-GCN +PE
    model_key: drew-gcn +pe
    model_plain: DRew-GCN +PE
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: DRew-GIN+LapPE
    model_key: drew-gin+lappe
    model_plain: DRew-GIN+LapPE
    value: 0.7126
    std: 0.0045
    paper_value: 0.7126
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 11
    true_value: 0.7126
    true_std: 0.0045
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7126
    sort_std: 0.0045
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.7071
    std: 0.0083
    paper_value: 0.7071
    paper_std: 0.0083
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 15
    true_value: 0.7071
    true_std: 0.0083
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7071
    sort_std: 0.0083
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.7021
    std: 0.0043
    paper_value: 0.7021
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
    true_value: 0.7021
    true_std: 0.0043
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7021
    sort_std: 0.0043
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 0.7012
    std: 0.0045
    paper_value: 0.7012
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 18
    true_value: 0.7012
    true_std: 0.0045
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7012
    sort_std: 0.0045
    is_best: false
  - model: DRew-GCN
    model_key: drew-gcn
    model_plain: DRew-GCN
    value: 0.694
    std: 0.0074
    paper_value: 0.694
    paper_std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
    true_value: 0.6996
    true_std: 0.0076
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005600000000000049
    value_note: global 0.6996 within std
    paper_rank: 27
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.6996
    sort_std: 0.0076
    is_best: false
  - model: DRew-GatedGCN+LapPE
    model_key: drew-gatedgcn+lappe
    model_plain: DRew-GatedGCN+LapPE
    value: 0.6977
    std: 0.0026
    paper_value: 0.6977
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.6977
    true_std: 0.0026
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6977
    sort_std: 0.0026
    is_best: false
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.6892
    std: 0.004
    paper_value: 0.6892
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 30
    true_value: 0.6892
    true_std: 0.004
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6892
    sort_std: 0.004
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
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
    paper_rank: 90
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.6843
    std: 0.0049
    paper_value: 0.6843
    paper_std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
    true_value: 0.6843
    true_std: 0.0049
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6843
    sort_std: 0.0049
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.683
    std: 0.0026
    paper_value: 0.683
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.683
    true_std: 0.0026
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.683
    sort_std: 0.0026
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 41
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
    paper_rank: 90
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.6765
    sort_std: 0.0047
    is_best: false
  - model: SWAN
    model_key: swan
    model_plain: SWAN
    value: 0.6751
    std: 0.0039
    paper_value: 0.6751
    paper_std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 43
    true_value: 0.6751
    true_std: 0.0039
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6751
    sort_std: 0.0039
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.6739
    std: 0.0087
    paper_value: 0.6739
    paper_std: 0.0087
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 44
    true_value: 0.6739
    true_std: 0.0087
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6739
    sort_std: 0.0087
    is_best: false
  - model: DRew-GatedGCN
    model_key: drew-gatedgcn
    model_plain: DRew-GatedGCN
    value: 0.6733
    std: 0.0094
    paper_value: 0.6733
    paper_std: 0.0094
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 45
    true_value: 0.6733
    true_std: 0.0094
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6733
    sort_std: 0.0094
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: MixHop-GCN
    model_key: mixhop-gcn
    model_plain: MixHop-GCN
    value: 0.6592
    std: 0.0036
    paper_value: 0.6592
    paper_std: 0.0036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 58
    true_value: 0.6592
    true_std: 0.0036
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6592
    sort_std: 0.0036
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 63
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.6535 within std
    paper_rank: 65
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 65
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: DIGL+MPNN
    model_key: digl+mpnn
    model_plain: DIGL+MPNN
    value: 0.6469
    std: 0.0019
    paper_value: 0.6469
    paper_std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 71
    true_value: 0.6469
    true_std: 0.0019
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6469
    sort_std: 0.0019
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 79
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 81
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GraphCON
    model_key: graphcon
    model_plain: GraphCON
    value: 0.6022
    std: 0.0068
    paper_value: 0.6022
    paper_std: 0.0068
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 89
    true_value: 0.6022
    true_std: 0.0068
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6022
    sort_std: 0.0068
    is_best: false
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 0.5975
    std: 0.0044
    paper_value: 0.5975
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 90
    true_value: 0.5975
    true_std: 0.0044
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5975
    sort_std: 0.0044
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.5789
    std: 0.0062
    paper_value: 0.5789
    paper_std: 0.0062
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 93
    true_value: 0.5789
    true_std: 0.0062
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5789
    sort_std: 0.0062
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 96
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
  higher_is_better: true
- &id007
  dataset: Peptides-struct
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.2422
    std: 0.0014
    paper_value: 0.2422
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.2422
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.2438
    std: 0.0014
    metric: MAE
    higher_is_better: false
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
    global_rank: 4
    sort_value: 0.2438
    sort_std: 0.0014
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.2451
    std: 0.0006
    paper_value: 0.2451
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 10
    true_value: 0.2451
    true_std: 0.0006
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2451
    sort_std: 0.0006
    is_best: false
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
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
    paper_rank: 105
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: GCN
    model_key: gcn (re-eval)
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 0.2465
    std: 0.002
    paper_value: 0.2465
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.2465
    true_std: 0.002
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2465
    sort_std: 0.002
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.2473
    std: 0.0025
    paper_value: 0.2473
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
    true_value: 0.2473
    true_std: 0.0025
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0025
    is_best: false
  - model: GINE
    model_key: gine (re-eval)
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 29
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
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
    paper_rank: 104
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn (re-eval)
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.2478
    std: 0.0016
    paper_value: 0.2478
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.2478
    true_std: 0.0016
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2478
    sort_std: 0.0016
    is_best: false
  - model: SWAN
    model_key: swan
    model_plain: SWAN
    value: 0.2485
    std: 0.0009
    paper_value: 0.2485
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 46
    true_value: 0.2485
    true_std: 0.0009
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2485
    sort_std: 0.0009
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 53
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: GraphGPS
    model_key: graphgps (re-eval)
    model_plain: GraphGPS
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 61
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 64
    true_value: 0.2529
    true_std: 0.0016
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
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: DRew-GatedGCN+LapPE
    model_key: drew-gatedgcn+lappe
    model_plain: DRew-GatedGCN+LapPE
    value: 0.2539
    std: 0.0007
    paper_value: 0.2539
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 70
    true_value: 0.2539
    true_std: 0.0007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2539
    sort_std: 0.0007
    is_best: false
  - model: DRew-GIN+LapPE
    model_key: drew-gin+lappe
    model_plain: DRew-GIN+LapPE
    value: 0.2606
    std: 0.0014
    paper_value: 0.2606
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 82
    true_value: 0.2606
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2606
    sort_std: 0.0014
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.2614
    std: 0.0023
    paper_value: 0.2614
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 83
    true_value: 0.2614
    true_std: 0.0023
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2614
    sort_std: 0.0023
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.2616
    std: 0.0018
    paper_value: 0.2616
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 84
    true_value: 0.2616
    true_std: 0.0018
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2616
    sort_std: 0.0018
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 88
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
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: DRew-GatedGCN
    model_key: drew-gatedgcn
    model_plain: DRew-GatedGCN
    value: 0.2699
    std: 0.0018
    paper_value: 0.2699
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 90
    true_value: 0.2699
    true_std: 0.0018
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2699
    sort_std: 0.0018
    is_best: false
  - model: DRew-GCN
    model_key: drew-gcn
    model_plain: DRew-GCN
    value: 0.2799
    std: 0.0016
    paper_value: 0.2799
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 95
    true_value: 0.2766
    true_std: 0.0019
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0032999999999999696
    value_note: ''
    paper_rank: 96
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.2766
    sort_std: 0.0019
    is_best: false
  - model: GraphCON
    model_key: graphcon
    model_plain: GraphCON
    value: 0.2778
    std: 0.0018
    paper_value: 0.2778
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 96
    true_value: 0.2778
    true_std: 0.0018
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2778
    sort_std: 0.0018
    is_best: false
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 0.2874
    std: 0.0021
    paper_value: 0.2874
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 99
    true_value: 0.2874
    true_std: 0.0021
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2874
    sort_std: 0.0021
    is_best: false
  - model: MixHop-GCN
    model_key: mixhop-gcn
    model_plain: MixHop-GCN
    value: 0.2921
    std: 0.0023
    paper_value: 0.2921
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 100
    true_value: 0.2921
    true_std: 0.0023
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2921
    sort_std: 0.0023
    is_best: false
  - model: DIGL+MPNN
    model_key: digl+mpnn
    model_plain: DIGL+MPNN
    value: 0.3173
    std: 0.0007
    paper_value: 0.3173
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 102
    true_value: 0.3173
    true_std: 0.0007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3173
    sort_std: 0.0007
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.3418
    std: 0.0015
    paper_value: 0.3418
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 104
    true_value: 0.3418
    true_std: 0.0015
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3418
    sort_std: 0.0015
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 105
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: Questions
  rows:
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8039
    std: 0.0104
    paper_value: 0.8039
    paper_std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.8039
    true_std: 0.0104
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.0104
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8032
    std: 0.0107
    paper_value: 0.8032
    paper_std: 0.0107
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.8032
    true_std: 0.0107
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8032
    sort_std: 0.0107
    is_best: true
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.8002
    std: 0.0086
    paper_value: 0.8002
    paper_std: 0.0086
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.8002
    true_std: 0.0086
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8002
    sort_std: 0.0086
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.7931
    std: 0.0122
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
    global_rank: 4
    sort_value: 0.7931
    sort_std: 0.0122
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7886
    std: 0.0092
    paper_value: 0.7886
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.7886
    true_std: 0.0092
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7886
    sort_std: 0.0092
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.7875
    std: 0.0109
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
    global_rank: 6
    sort_value: 0.7875
    sort_std: 0.0109
    is_best: true
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.7805
    std: 0.0093
    paper_value: 0.7805
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.7805
    true_std: 0.0093
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7805
    sort_std: 0.0093
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.7795
    true_std: 0.0068
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795
    sort_std: 0.0068
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.7743
    true_std: 0.012
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7743
    sort_std: 0.012
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7724
    std: 0.0126
    paper_value: 0.7724
    paper_std: 0.0126
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 10
    true_value: 0.7724
    true_std: 0.0126
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7724
    sort_std: 0.0126
    is_best: false
  - model: GPS_GCNI+Performer (RWSE)
    model_key: gps_gcni+performer (rwse)
    model_plain: GPS_GCNI+Performer (RWSE)
    value: 0.7714
    std: 0.0149
    paper_value: 0.7714
    paper_std: 0.0149
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 11
    true_value: 0.7714
    true_std: 0.0149
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7714
    sort_std: 0.0149
    is_best: false
  - model: GODM
    model_key: godm
    model_plain: GODM
    value: 0.7684
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.17679'
    title: Data Augmentation for Supervised Graph Outlier Detection via Latent Diffusion
      Models
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: https://pypi.org/project/godm
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.7684
    sort_std: null
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7661
    std: 0.0113
    paper_value: 0.7661
    paper_std: 0.0113
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.7661
    true_std: 0.0113
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7661
    sort_std: 0.0113
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.7654
    std: 0.0095
    paper_value: 0.7654
    paper_std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.7654
    true_std: 0.0095
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7654
    sort_std: 0.0095
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 15
    true_value: 0.7644
    true_std: 0.0062
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.0062
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
    true_value: 0.7609
    true_std: 0.0127
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609
    sort_std: 0.0127
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7576
    std: 0.0166
    paper_value: 0.7576
    paper_std: 0.0166
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
    true_value: 0.7576
    true_std: 0.0166
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7576
    sort_std: 0.0166
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.7447
    std: 0.0086
    paper_value: 0.7447
    paper_std: 0.0086
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.7447
    true_std: 0.0086
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7447
    sort_std: 0.0086
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7394
    std: 0.0106
    paper_value: 0.7394
    paper_std: 0.0106
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 23
    true_value: 0.7394
    true_std: 0.0106
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7394
    sort_std: 0.0106
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.7388
    std: 0.0116
    paper_value: 0.7388
    paper_std: 0.0116
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
    true_value: 0.7388
    true_std: 0.0116
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7388
    sort_std: 0.0116
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.6817
    std: 0.0153
    paper_value: 0.6817
    paper_std: 0.0153
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.6817
    true_std: 0.0153
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6817
    sort_std: 0.0153
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.6574
    std: 0.0119
    paper_value: 0.6574
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 40
    true_value: 0.6574
    true_std: 0.0119
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6574
    sort_std: 0.0119
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.5548
    std: 0.0091
    paper_value: 0.5548
    paper_std: 0.0091
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 48
    true_value: 0.5548
    true_std: 0.0091
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5548
    sort_std: 0.0091
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id002
  dataset: Roman-empire
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9263
    std: 0.005
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.9263
    sort_std: 0.005
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9255
    std: 0.003
    metric: Accuracy
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
    sort_value: 0.9255
    sort_std: 0.003
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.9203
    std: 0.0085
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
    global_rank: 3
    sort_value: 0.9203
    sort_std: 0.0085
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.9189
    std: 0.003
    paper_value: 0.9189
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.9189
    true_std: 0.003
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9189
    sort_std: 0.003
    is_best: true
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.9157
    std: 0.0032
    paper_value: 0.9157
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.9157
    true_std: 0.0032
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
    sort_value: 0.9157
    sort_std: 0.0032
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.9137
    std: 0.0035
    paper_value: 0.9137
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.9137
    true_std: 0.0035
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9137
    sort_std: 0.0035
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.9108
    std: 0.0057
    paper_value: 0.9108
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.9108
    true_std: 0.0057
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9108
    sort_std: 0.0057
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8903
    std: 0.0037
    paper_value: 0.8903
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.8903
    true_std: 0.0037
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8903
    sort_std: 0.0037
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.8732
    std: 0.0039
    paper_value: 0.8732
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
    true_value: 0.8732
    true_std: 0.0039
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8732
    sort_std: 0.0039
    is_best: false
  - model: GPS_GCNI+Performer (RWSE)
    model_key: gps_gcni+performer (rwse)
    model_plain: GPS_GCNI+Performer (RWSE)
    value: 0.8704
    std: 0.0058
    paper_value: 0.8704
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 18
    true_value: 0.8704
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8704
    sort_std: 0.0058
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 21
    true_value: 0.8651
    true_std: 0.0073
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8651
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
    true_value: 0.8574
    true_std: 0.0067
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8574
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7446
    std: 0.0054
    paper_value: 0.7446
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
    true_value: 0.833
    true_std: 0.0079
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08839999999999992
    value_note: ''
    paper_rank: 49
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.833
    sort_std: 0.0079
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.8087
    true_std: 0.003
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8087
    sort_std: 0.003
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7434
    std: 0.0077
    paper_value: 0.7434
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
    true_value: 0.8
    true_std: 0.0043
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056600000000000095
    value_note: ''
    paper_rank: 49
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.0043
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7992
    std: 0.0056
    paper_value: 0.7992
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.7992
    true_std: 0.0056
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7992
    sort_std: 0.0056
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
    true_value: 0.795
    true_std: 0.0088
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05810000000000004
    value_note: ''
    paper_rank: 51
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.795
    sort_std: 0.0088
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.7457
    std: 0.0047
    paper_value: 0.7457
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 49
    true_value: 0.7457
    true_std: 0.0047
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7457
    sort_std: 0.0047
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7159
    std: 0.0125
    paper_value: 0.7159
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 56
    true_value: 0.7159
    true_std: 0.0125
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7159
    sort_std: 0.0125
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.5963
    std: 0.0069
    paper_value: 0.5963
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 58
    true_value: 0.7117
    true_std: 0.012
    value_gap_source_arxiv: '2404.15354'
    value_gap_source_title: 'Polynomial Selection in Spectral Graph Neural Networks:
      An Error-Sum of Function Slices Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11539999999999995
    value_note: ''
    paper_rank: 85
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.7117
    sort_std: 0.012
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.7114
    std: 0.0042
    paper_value: 0.7114
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 59
    true_value: 0.7114
    true_std: 0.0042
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7114
    sort_std: 0.0042
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.6522
    std: 0.0056
    paper_value: 0.6522
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 78
    true_value: 0.6522
    true_std: 0.0056
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6522
    sort_std: 0.0056
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.6485
    std: 0.0027
    paper_value: 0.6485
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 79
    true_value: 0.6485
    true_std: 0.0027
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6485
    sort_std: 0.0027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA_GCNGCN
    model_key: grama_gcngcn
    model_plain: GRAMA_GCNGCN
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
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8566
    std: 0.0101
    paper_value: 0.8566
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.8566
    true_std: 0.0101
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8566
    sort_std: 0.0101
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.8555
    std: 0.0335
    metric: ROC-AUC
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
    global_rank: 4
    sort_value: 0.8555
    sort_std: 0.0335
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8551
    std: 0.0098
    paper_value: 0.8551
    paper_std: 0.0098
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.8551
    true_std: 0.0098
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8551
    sort_std: 0.0098
    is_best: true
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.8445
    std: 0.0117
    paper_value: 0.8445
    paper_std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
    true_value: 0.8445
    true_std: 0.0117
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8445
    sort_std: 0.0117
    is_best: true
  - model: GPS_GCNI+Performer (RWSE)
    model_key: gps_gcni+performer (rwse)
    model_plain: GPS_GCNI+Performer (RWSE)
    value: 0.8438
    std: 0.0091
    paper_value: 0.8438
    paper_std: 0.0091
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 18
    true_value: 0.8438
    true_std: 0.0091
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8438
    sort_std: 0.0091
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
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
    paper_rank: 24
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8377
    std: 0.0078
    paper_value: 0.8377
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
    true_value: 0.8377
    true_std: 0.0078
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8377
    sort_std: 0.0078
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 23
    true_value: 0.837
    true_std: 0.0047
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
    sort_value: 0.837
    sort_std: 0.0047
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7832
    std: 0.0095
    paper_value: 0.7832
    paper_std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 30
    true_value: 0.834
    true_std: 0.0045
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.050799999999999956
    value_note: ''
    paper_rank: 46
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.834
    sort_std: 0.0045
    is_best: false
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.8336
    std: 0.0089
    paper_value: 0.8336
    paper_std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 31
    true_value: 0.8336
    true_std: 0.0089
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8336
    sort_std: 0.0089
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7731
    std: 0.0114
    paper_value: 0.7731
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.832
    true_std: 0.009
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05889999999999995
    value_note: ''
    paper_rank: 48
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.009
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8311
    std: 0.0104
    paper_value: 0.8311
    paper_std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.8311
    true_std: 0.0104
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8311
    sort_std: 0.0104
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8276
    std: 0.0061
    paper_value: 0.8276
    paper_std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
    true_value: 0.8276
    true_std: 0.0061
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8276
    sort_std: 0.0061
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.8252
    std: 0.0092
    paper_value: 0.8252
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.8252
    true_std: 0.0092
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8252
    sort_std: 0.0092
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
    true_value: 0.8243
    true_std: 0.0044
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.8101
    std: 0.0067
    paper_value: 0.8101
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.8101
    true_std: 0.0067
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8101
    sort_std: 0.0067
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7775
    std: 0.0105
    paper_value: 0.7775
    paper_std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 47
    true_value: 0.7775
    true_std: 0.0105
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7775
    sort_std: 0.0105
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.7339
    std: 0.0117
    paper_value: 0.7339
    paper_std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 57
    true_value: 0.7339
    true_std: 0.0117
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7339
    sort_std: 0.0117
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.7294
    std: 0.0097
    paper_value: 0.7294
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 62
    true_value: 0.7294
    true_std: 0.0097
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7294
    sort_std: 0.0097
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.6866
    std: 0.0065
    paper_value: 0.6866
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 66
    true_value: 0.6866
    true_std: 0.0065
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6866
    sort_std: 0.0065
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
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
    source_ref: gatedgcn
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.059
    std: 0.002
    paper_value: 0.059
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.036
    value_note: ''
    paper_rank: 30
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.081
    std: 0.009
    paper_value: 0.081
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhang2023rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056
    value_note: ''
    paper_rank: 58
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022graphgps
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.062
    std: 0.005
    paper_value: 0.062
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.062
    true_std: 0.005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.062
    sort_std: 0.005
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PNA
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.121
    value_note: ''
    paper_rank: 122
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.067
    sort_std: 0.009
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
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: CRaW1
    model_key: craw1
    model_plain: CRaW1
    value: 0.085
    std: 0.004
    paper_value: 0.085
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonnshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 60
    true_value: 0.085
    true_std: 0.004
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.004
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
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
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
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.128
    std: 0.011
    paper_value: 0.128
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 89
    true_value: 0.128
    true_std: 0.011
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.128
    sort_std: 0.011
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
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
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 97
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 100
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.168
    std: 0.003
    paper_value: 0.168
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: beaini2021directional
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 119
    true_value: 0.168
    true_std: 0.003
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.168
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
- benchmark: GNNBenchmark
  datasets:
  - *id009
  - *id010
  - *id011
  - *id012
main_figure: /figures/2508.05070/main_figure.png
---

