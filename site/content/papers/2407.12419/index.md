---
title: Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range
  Graph Predictions
arxiv_id: '2407.12419'
source_url: ''
authors: []
published_date: Jul 17, 2024
published_date_iso: '2024-07-17'
abstract: The geometry of a graph is encoded in dynamical processes on the graph.
  Many graph neural network (GNN) architectures are inspired by such dynamical systems,
  typically based on the graph Laplacian. Here, we introduce Dirac--Bianconi GNNs
  (DBGNNs), which are based on the topological Dirac equation recently proposed by
  Bianconi. Based on the graph Laplacian, we demonstrate that DBGNNs explore the geometry
  of the graph in a fundamentally different way than conventional message passing
  neural networks (MPNNs). While regular MPNNs propagate features diffusively, analogous
  to the heat equation, DBGNNs allow for coherent long-range propagation. Experimental
  results showcase the superior performance of DBGNNs over existing conventional MPNNs
  for long-range predictions of power grid stability and peptide properties. This
  study highlights the effectiveness of DBGNNs in capturing intricate graph dynamics,
  providing notable advancements in GNN architectures.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- DBGNN
mrr: 0.0038
adjusted_mrr: 0.0013
mrr_dataset_count: 1
benchmark_categories:
- LRGB
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
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
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.508
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
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
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
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
    params_millions: 0.509
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
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
    params_millions: 0.476
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
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
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
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
    params_millions: 0.506
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 167
    true_value: 0.2529
    true_std: 0.0009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08279999999999998
    value_note: ''
    paper_rank: 289
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.2529
    sort_std: 0.0009
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
    params_millions: 0.5
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 188
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
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
    params_millions: 0.493
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 242
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
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: DBGNN
    model_key: dbgnn
    model_plain: DBGNN
    value: 0.2864
    std: 0.0046
    paper_value: 0.2864
    paper_std: 0.0046
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.127
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 262
    true_value: 0.2864
    true_std: 0.0046
    value_gap_source_arxiv: '2407.12419'
    value_gap_source_title: Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive
      Long-Range Graph Predictions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2864
    sort_std: 0.0046
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
    params_millions: 0.505
    table_ref: Table 1
    source_ref: dwivediLongRangeGraph2023
    variant_inference_reason: ''
    date: Jul 17, 2024
    date_display: Jul 2024
    date_iso: '2024-07-17'
    global_rank: 300
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
single_proposed_model: DBGNN
main_figure: /figures/2407.12419/main_figure.png
---

