---
title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
arxiv_id: '2406.08993'
source_url: ''
authors: []
published_date: Jun 2024
published_date_iso: 2024-06
abstract: Graph Transformers (GTs) have recently emerged as popular alternatives to
  traditional message-passing Graph Neural Networks (GNNs), due to their theoretically
  superior expressiveness and impressive performance reported on standard node classification
  benchmarks, often significantly outperforming GNNs. In this paper, we conduct a
  thorough empirical analysis to reevaluate the performance of three classic GNN models
  (GCN, GAT, and GraphSAGE) against GTs. Our findings suggest that the previously
  reported superiority of GTs may have been overstated due to suboptimal hyperparameter
  configurations in GNNs. Remarkably, with slight hyperparameter tuning, these classic
  GNN models achieve state-of-the-art performance, matching or even exceeding that
  of recent GTs across 17 out of the 18 diverse datasets examined. Additionally, we
  conduct detailed ablation studies to investigate the influence of various GNN configurations—such
  as normalization, dropout, residual connections, and network depth—on node classification
  performance. Our study aims to promote a higher standard of empirical rigor in the
  field of graph machine learning, encouraging more accurate comparisons and evaluations
  of model capabilities. Our implementation is available at https://github.com/LUOyk1999/tunedGNN.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN* (-) Normalization
- GCN* (-) Dropout
- GraphSAGE* (-) Normalization
- GraphSAGE* (-) Dropout
- GCN* (-) Residual Connections
- GraphSAGE* (-) Residual Connections
- GAT* (-) Dropout
mrr: 0.0787
adjusted_mrr: 0.0524
mrr_dataset_count: 2
benchmark_categories:
- Classic
- Heterophilic Graphs
- OGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id006
  dataset: Amazon-Computers
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9409
    std: 0.0037
    paper_value: 0.9409
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 1
    true_value: 0.9409
    true_std: 0.0037
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9409
    sort_std: 0.0037
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9399
    std: 0.0012
    paper_value: 0.9399
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.9399
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9399
    sort_std: 0.0012
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9378
    std: 0.001
    paper_value: 0.9378
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.9378
    true_std: 0.001
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9378
    sort_std: 0.001
    is_best: true
  - model: GCN* (-) Dropout
    model_key: gcn* (-) dropout
    model_plain: GCN* (-) Dropout
    value: 0.9378
    std: 0.0026
    paper_value: 0.9378
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 4
    true_value: 0.9378
    true_std: 0.0026
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9378
    sort_std: 0.0026
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9325
    std: 0.0014
    paper_value: 0.9325
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.9325
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9325
    sort_std: 0.0014
    is_best: false
  - model: GraphSAGE* (-) Normalization
    model_key: graphsage* (-) normalization
    model_plain: GraphSAGE* (-) Normalization
    value: 0.9277
    std: 0.0063
    paper_value: 0.9277
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.9277
    true_std: 0.0063
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9277
    sort_std: 0.0063
    is_best: false
  - model: GCN* (-) Normalization
    model_key: gcn* (-) normalization
    model_plain: GCN* (-) Normalization
    value: 0.926
    std: 0.0014
    paper_value: 0.926
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.926
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.926
    sort_std: 0.0014
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9242
    std: 0.0066
    paper_value: 0.9242
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.9242
    true_std: 0.0066
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9242
    sort_std: 0.0066
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9229
    std: 0.0037
    paper_value: 0.9229
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 9
    true_value: 0.9229
    true_std: 0.0037
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9229
    sort_std: 0.0037
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9228
    std: 0.0039
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
    global_rank: 10
    sort_value: 0.9228
    sort_std: 0.0039
    is_best: false
  - model: M
    model_key: m
    model_plain: M
    value: 0.9226
    std: 0.0018
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.9226
    sort_std: 0.0018
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.9206
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.9206
    sort_std: 0.0033
    is_best: false
  - model: GraphSAGE* (-) Dropout
    model_key: graphsage* (-) dropout
    model_plain: GraphSAGE* (-) Dropout
    value: 0.9202
    std: 0.0035
    paper_value: 0.9202
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.9202
    true_std: 0.0035
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9202
    sort_std: 0.0035
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.918
    std: 0.0035
    paper_value: 0.918
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 15
    true_value: 0.918
    true_std: 0.0035
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.0035
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9179
    std: 0.0063
    paper_value: 0.9179
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.9179
    true_std: 0.0063
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9179
    sort_std: 0.0063
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9169
    std: 0.003
    paper_value: 0.9169
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.9169
    true_std: 0.003
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9169
    sort_std: 0.003
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8729
    std: 0.0058
    paper_value: 0.8729
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 31
    true_value: 0.8785
    true_std: 0.0024
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005599999999999938
    value_note: global 0.8785 within std
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8785
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Amazon-Photo
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9712
    std: 0.0024
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
    sort_value: 0.9712
    sort_std: 0.0024
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9678
    std: 0.0023
    paper_value: 0.9678
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.9678
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.966
    std: 0.0033
    paper_value: 0.966
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.966
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9657
    std: 0.0023
    paper_value: 0.9657
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 4
    true_value: 0.9657
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9657
    sort_std: 0.0023
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9614
    std: 0.0016
    paper_value: 0.9614
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.9614
    true_std: 0.0016
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9614
    sort_std: 0.0016
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.961
    std: 0.0046
    paper_value: 0.961
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.958
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.958
    sort_std: null
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9569
    std: 0.0039
    paper_value: 0.9569
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.9569
    true_std: 0.0039
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9569
    sort_std: 0.0039
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9558
    std: 0.0036
    paper_value: 0.9558
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 9
    true_value: 0.9558
    true_std: 0.0036
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
    sort_value: 0.9558
    sort_std: 0.0036
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9552
    std: 0.0052
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
    global_rank: 10
    sort_value: 0.9552
    sort_std: 0.0052
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9343
    std: 0.0056
    paper_value: 0.9343
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.9527
    true_std: 0.0022
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018399999999999972
    value_note: ''
    paper_rank: 30
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.9527
    sort_std: 0.0022
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9489
    std: 0.0014
    paper_value: 0.9489
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 18
    true_value: 0.9489
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9489
    sort_std: 0.0014
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9433
    std: 0.0021
    paper_value: 0.9433
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 24
    true_value: 0.9433
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9433
    sort_std: 0.0021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5554
    std: 0.0051
    paper_value: 0.5554
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
    paper_value: 0.554
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.554
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5496
    std: 0.0022
    paper_value: 0.5496
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 4
    true_value: 0.5496
    true_std: 0.0222
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5496
    sort_std: 0.0222
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.5458
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 5
    sort_value: 0.5458
    sort_std: 0.0036
    is_best: false
  - model: IM-CO-GNN(μ,μ)
    model_key: im-co-gnn(μ,μ)
    model_plain: IM-CO-GNN(μ,μ)
    value: 0.5443
    std: 0.0041
    metric: Accuracy
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
    global_rank: 6
    sort_value: 0.5443
    sort_std: 0.0041
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.5414
    std: 0.0062
    paper_value: 0.5414
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.5414
    true_std: 0.02
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5414
    sort_std: 0.02
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.538
    std: 0.006
    paper_value: 0.538
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.0
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.5327
    std: 0.0066
    paper_value: 0.5327
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 25
    true_value: 0.5327
    true_std: 0.0006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5327
    sort_std: 0.0006
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.5274
    true_std: 0.0083
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5274
    sort_std: 0.0083
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 77
    true_value: 0.4488
    true_std: 0.0034
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4488
    sort_std: 0.0034
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4379
    std: 0.0057
    paper_value: 0.4379
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 82
    true_value: 0.4386
    true_std: 0.0035
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006999999999999784
    value_note: global 0.4386 within std
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4386
    sort_std: 0.0035
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.3979
    std: 0.0077
    paper_value: 0.3979
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 91
    true_value: 0.3979
    true_std: 0.0077
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3979
    sort_std: 0.0077
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 93
    true_value: 0.3689
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3689
    sort_std: 0.0014
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3647
    std: 0.0023
    paper_value: 0.3647
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 94
    true_value: 0.3647
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3647
    sort_std: 0.0023
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: true
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
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
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.4061
    std: 0.0297
    paper_value: 0.4061
    paper_std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.7827
    true_std: 0.0128
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.37659999999999993
    value_note: ''
    paper_rank: 124
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.7827
    sort_std: 0.0128
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.259
    std: 0.0358
    paper_value: 0.259
    paper_std: 0.0358
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 23
    true_value: 0.7121
    true_std: 0.0184
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.45309999999999995
    value_note: ''
    paper_rank: 128
    rank_delta: 105
    rank_delta_abs: 105
    rank_delta_direction: worse
    sort_value: 0.7121
    sort_std: 0.0184
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3993
    std: 0.033
    paper_value: 0.3993
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 36
    true_value: 0.6748
    true_std: 0.004
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27549999999999997
    value_note: ''
    paper_rank: 125
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.6748
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4629
    std: 0.034
    paper_value: 0.4629
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18530000000000002
    value_note: ''
    paper_rank: 111
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4413
    std: 0.0417
    paper_value: 0.4413
    paper_std: 0.0417
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1977
    value_note: ''
    paper_rank: 117
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4481
    std: 0.0474
    paper_value: 0.4481
    paper_std: 0.0474
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 60
    true_value: 0.6215
    true_std: 0.0042
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17340000000000005
    value_note: ''
    paper_rank: 117
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.6215
    sort_std: 0.0042
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4521
    std: 0.0372
    paper_value: 0.4521
    paper_std: 0.0372
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 62
    true_value: 0.6144
    true_std: 0.0137
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16229999999999994
    value_note: ''
    paper_rank: 115
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.6144
    sort_std: 0.0137
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.2675
    std: 0.0364
    paper_value: 0.2675
    paper_std: 0.0364
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 64
    true_value: 0.612
    true_std: 0.0428
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3445
    value_note: ''
    paper_rank: 127
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.612
    sort_std: 0.0428
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4197
    std: 0.0318
    paper_value: 0.4197
    paper_std: 0.0318
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 70
    true_value: 0.6017
    true_std: 0.0139
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.182
    value_note: ''
    paper_rank: 121
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.6017
    sort_std: 0.0139
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3638
    std: 0.0385
    paper_value: 0.3638
    paper_std: 0.0385
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 84
    true_value: 0.5634
    true_std: 0.0111
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1996
    value_note: ''
    paper_rank: 127
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.5634
    sort_std: 0.0111
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.4155
    std: 0.0391
    paper_value: 0.4155
    paper_std: 0.0391
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 112
    true_value: 0.4607
    true_std: 0.0151
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04520000000000002
    value_note: ''
    paper_rank: 123
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.4607
    sort_std: 0.0151
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.33
    std: 0.0315
    paper_value: 0.33
    paper_std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 124
    true_value: 0.408
    true_std: 0.02
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07799999999999996
    value_note: ''
    paper_rank: 127
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.408
    sort_std: 0.02
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
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7219
    std: 0.0083
    paper_value: 0.7219
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.818
    true_std: 0.0076
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09609999999999996
    value_note: ''
    paper_rank: 121
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.818
    sort_std: 0.0076
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7314
    std: 0.0067
    paper_value: 0.7314
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0824999999999999
    value_note: ''
    paper_rank: 110
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7222
    std: 0.0084
    paper_value: 0.7222
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08300000000000007
    value_note: ''
    paper_rank: 120
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7059
    std: 0.0089
    paper_value: 0.7059
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 26
    true_value: 0.8012
    true_std: 0.0124
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09530000000000005
    value_note: ''
    paper_rank: 133
    rank_delta: 107
    rank_delta_abs: 107
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0124
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7272
    std: 0.0115
    paper_value: 0.7272
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 29
    true_value: 0.7962
    true_std: 0.0163
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06900000000000006
    value_note: ''
    paper_rank: 112
    rank_delta: 83
    rank_delta_abs: 83
    rank_delta_direction: worse
    sort_value: 0.7962
    sort_std: 0.0163
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7237
    std: 0.012
    paper_value: 0.7237
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 30
    true_value: 0.7956
    true_std: 0.011
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07189999999999996
    value_note: ''
    paper_rank: 118
    rank_delta: 88
    rank_delta_abs: 88
    rank_delta_direction: worse
    sort_value: 0.7956
    sort_std: 0.011
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7226
    std: 0.0055
    paper_value: 0.7226
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06969999999999998
    value_note: ''
    paper_rank: 120
    rank_delta: 86
    rank_delta_abs: 86
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7273
    std: 0.0123
    paper_value: 0.7273
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 47
    true_value: 0.7699
    true_std: 0.0112
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04260000000000008
    value_note: ''
    paper_rank: 112
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.7699
    sort_std: 0.0112
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7221
    std: 0.0129
    paper_value: 0.7221
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 50
    true_value: 0.7689
    true_std: 0.0119
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046800000000000064
    value_note: ''
    paper_rank: 120
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7689
    sort_std: 0.0119
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7185
    std: 0.0111
    paper_value: 0.7185
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 52
    true_value: 0.7683
    true_std: 0.0124
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.049799999999999955
    value_note: ''
    paper_rank: 122
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7683
    sort_std: 0.0124
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Coauthor-CS
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9638
    std: 0.0011
    paper_value: 0.9638
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 1
    true_value: 0.9638
    true_std: 0.0011
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9638
    sort_std: 0.0011
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9621
    std: 0.0014
    paper_value: 0.9621
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.9621
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9621
    sort_std: 0.0014
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9617
    std: 0.0006
    paper_value: 0.9617
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.9617
    true_std: 0.0006
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9617
    sort_std: 0.0006
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9592
    std: 0.0025
    paper_value: 0.9592
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 4
    true_value: 0.9592
    true_std: 0.0025
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9592
    sort_std: 0.0025
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9585
    std: 0.0016
    paper_value: 0.9585
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.9585
    true_std: 0.0016
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9585
    sort_std: 0.0016
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9571
    std: 0.0024
    paper_value: 0.9571
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.9571
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9571
    sort_std: 0.0024
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9569
    std: 0.0027
    paper_value: 0.9569
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.9569
    true_std: 0.0027
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9569
    sort_std: 0.0027
    is_best: false
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.9546
    sort_std: 0.0033
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9542
    std: 0.0019
    paper_value: 0.9542
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.9542
    true_std: 0.0019
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9542
    sort_std: 0.0019
    is_best: false
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.9518
    sort_std: 0.003
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9404
    std: 0.0021
    paper_value: 0.9404
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 19
    true_value: 0.9404
    true_std: 0.0021
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9404
    sort_std: 0.0021
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9381
    std: 0.0019
    paper_value: 0.9381
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 20
    true_value: 0.9381
    true_std: 0.0019
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9381
    sort_std: 0.0019
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Coauthor-Physics
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9831
    std: 0.0018
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
    global_rank: 1
    sort_value: 0.9831
    sort_std: 0.0018
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9718
    std: 0.0011
    paper_value: 0.9718
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.9808
    true_std: 0.0027
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009000000000000008
    value_note: ''
    paper_rank: 16
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.9808
    sort_std: 0.0027
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9675
    std: 0.0026
    paper_value: 0.9675
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.9796
    true_std: 0.0081
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0121
    value_note: ''
    paper_rank: 17
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.9796
    sort_std: 0.0081
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.9786
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 4
    sort_value: 0.9786
    sort_std: 0.0016
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9735
    std: 0.0012
    paper_value: 0.9735
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.9785
    true_std: 0.0026
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0050000000000000044
    value_note: ''
    paper_rank: 12
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.9785
    sort_std: 0.0026
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9725
    std: 0.0006
    paper_value: 0.9725
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.9782
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.005699999999999927
    value_note: ''
    paper_rank: 12
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.9782
    sort_std: 0.0028
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.9775
    std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 7
    sort_value: 0.9775
    sort_std: 0.0053
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9746
    std: 0.001
    paper_value: 0.9746
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.9774
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0028000000000000247
    value_note: global 0.9774 within std
    paper_rank: 11
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.9774
    sort_std: 0.0035
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9671
    std: 0.0015
    paper_value: 0.9671
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.976
    true_std: 0.0005
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008900000000000019
    value_note: ''
    paper_rank: 17
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.976
    sort_std: 0.0005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9719
    std: 0.0005
    paper_value: 0.9719
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 15
    true_value: 0.9719
    true_std: 0.0005
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9719
    sort_std: 0.0005
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9706
    std: 0.0013
    paper_value: 0.9706
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.9706
    true_std: 0.0013
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9706
    sort_std: 0.0013
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9648
    std: 0.0034
    paper_value: 0.9648
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 18
    true_value: 0.9648
    true_std: 0.0034
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9648
    sort_std: 0.0034
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9647
    std: 0.0016
    paper_value: 0.9647
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 19
    true_value: 0.9647
    true_std: 0.0016
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9647
    sort_std: 0.0016
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
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8273
    std: 0.0075
    paper_value: 0.8273
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059699999999999975
    value_note: ''
    paper_rank: 131
    rank_delta: 111
    rank_delta_abs: 111
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8446
    std: 0.0055
    paper_value: 0.8446
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.037899999999999934
    value_note: ''
    paper_rank: 107
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8092
    std: 0.0117
    paper_value: 0.8092
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07279999999999998
    value_note: ''
    paper_rank: 151
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8482
    std: 0.0085
    paper_value: 0.8482
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 37
    true_value: 0.8809999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03279999999999994
    value_note: ''
    paper_rank: 105
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8343
    std: 0.0089
    paper_value: 0.8343
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 45
    true_value: 0.879
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04469999999999996
    value_note: ''
    paper_rank: 120
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.851
    std: 0.0067
    paper_value: 0.851
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026800000000000046
    value_note: ''
    paper_rank: 101
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8388
    std: 0.0065
    paper_value: 0.8388
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.030200000000000116
    value_note: ''
    paper_rank: 112
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8387
    std: 0.0096
    paper_value: 0.8387
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 114
    true_value: 0.8387
    true_std: 0.0096
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8387
    sort_std: 0.0096
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8329
    std: 0.0136
    paper_value: 0.8329
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 124
    true_value: 0.8329
    true_std: 0.0136
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8329
    sort_std: 0.0136
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8326
    std: 0.0124
    paper_value: 0.8326
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 125
    true_value: 0.8326
    true_std: 0.0124
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8326
    sort_std: 0.0124
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
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
    value: 0.9786
    std: 0.0024
    paper_value: 0.9786
    paper_std: 0.0024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.9786
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9786
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9777
    std: 0.0062
    paper_value: 0.9777
    paper_std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.9777
    true_std: 0.0062
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9777
    sort_std: 0.0062
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9773
    std: 0.0073
    paper_value: 0.9773
    paper_std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9749
    std: 0.0048
    paper_value: 0.9749
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 10
    true_value: 0.9749
    true_std: 0.0048
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9749
    sort_std: 0.0048
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9142
    std: 0.0041
    paper_value: 0.9142
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 58
    true_value: 0.9142
    true_std: 0.0041
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9142
    sort_std: 0.0041
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9075
    std: 0.0089
    paper_value: 0.9075
    paper_std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 66
    true_value: 0.9075
    true_std: 0.0089
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9075
    sort_std: 0.0089
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 73
    true_value: 0.9008
    true_std: 0.007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9008
    sort_std: 0.007
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8971
    std: 0.0031
    paper_value: 0.8971
    paper_std: 0.0031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 77
    true_value: 0.8971
    true_std: 0.0031
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8971
    sort_std: 0.0031
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8771
    std: 0.0069
    paper_value: 0.8771
    paper_std: 0.0069
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 83
    true_value: 0.8771
    true_std: 0.0069
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8771
    sort_std: 0.0069
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 85
    true_value: 0.8624
    true_std: 0.0061
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8624
    sort_std: 0.0061
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.5203
    std: 0.0546
    paper_value: 0.5203
    paper_std: 0.0546
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 92
    true_value: 0.5203
    true_std: 0.0546
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5203
    sort_std: 0.0546
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 93
    true_value: 0.5108
    true_std: 0.0123
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5108
    sort_std: 0.0123
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8112
    std: 0.0052
    paper_value: 0.8112
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11119999999999997
    value_note: ''
    paper_rank: 114
    rank_delta: 109
    rank_delta_abs: 109
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8028
    std: 0.0064
    paper_value: 0.8028
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11730000000000007
    value_note: ''
    paper_rank: 116
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7935
    std: 0.0073
    paper_value: 0.7935
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 11
    true_value: 0.9068
    true_std: 0.0031
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11330000000000007
    value_note: ''
    paper_rank: 119
    rank_delta: 108
    rank_delta_abs: 108
    rank_delta_direction: worse
    sort_value: 0.9068
    sort_std: 0.0031
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8014
    std: 0.0106
    paper_value: 0.8014
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 27
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09560000000000002
    value_note: ''
    paper_rank: 116
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.806
    std: 0.0049
    paper_value: 0.806
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 26
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09099999999999997
    value_note: ''
    paper_rank: 116
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7967
    std: 0.0073
    paper_value: 0.7967
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 32
    true_value: 0.8952
    true_std: 0.0054
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09850000000000003
    value_note: ''
    paper_rank: 117
    rank_delta: 85
    rank_delta_abs: 85
    rank_delta_direction: worse
    sort_value: 0.8952
    sort_std: 0.0054
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7959
    std: 0.0092
    paper_value: 0.7959
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09729999999999994
    value_note: ''
    paper_rank: 117
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7994
    std: 0.0026
    paper_value: 0.7994
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 45
    true_value: 0.8894
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08999999999999997
    value_note: ''
    paper_rank: 116
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.8894
    sort_std: 0.0016
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7972
    std: 0.005
    paper_value: 0.7972
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08919999999999995
    value_note: ''
    paper_rank: 117
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8006
    std: 0.0067
    paper_value: 0.8006
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 92
    true_value: 0.8687
    true_std: 0.0024
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06810000000000005
    value_note: ''
    paper_rank: 116
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.8687
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7902
    std: 0.006
    paper_value: 0.7902
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 13
    true_value: 0.7902
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7902
    sort_std: 0.006
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7894
    std: 0.0078
    paper_value: 0.7894
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.7894
    true_std: 0.0078
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7894
    sort_std: 0.0078
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.7886
    true_std: 0.0092
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7886
    sort_std: 0.0092
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7795
    std: 0.0051
    paper_value: 0.7795
    paper_std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795
    sort_std: 0.0051
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7721
    std: 0.0128
    paper_value: 0.7721
    paper_std: 0.0128
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.7721
    true_std: 0.0128
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7721
    sort_std: 0.0128
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7502
    std: 0.0161
    paper_value: 0.7502
    paper_std: 0.0161
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 49
    true_value: 0.7502
    true_std: 0.0161
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7502
    sort_std: 0.0161
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7381
    std: 0.0059
    paper_value: 0.7381
    paper_std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 54
    true_value: 0.7381
    true_std: 0.0059
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7381
    sort_std: 0.0059
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7256
    std: 0.0133
    paper_value: 0.7256
    paper_std: 0.0133
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 55
    true_value: 0.7256
    true_std: 0.0133
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7256
    sort_std: 0.0133
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.6596
    std: 0.0195
    paper_value: 0.6596
    paper_std: 0.0195
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 60
    true_value: 0.6596
    true_std: 0.0195
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6596
    sort_std: 0.0195
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 61
    true_value: 0.6574
    true_std: 0.0119
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
    sort_value: 0.6574
    sort_std: 0.0119
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6359
    std: 0.0146
    paper_value: 0.6359
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 62
    true_value: 0.6359
    true_std: 0.0146
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6359
    sort_std: 0.0146
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 64
    true_value: 0.5548
    true_std: 0.0091
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5548
    sort_std: 0.0091
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id010
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
    paper_value: 0.9266
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.9266
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9252
    std: 0.005
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
    global_rank: 4
    sort_value: 0.9252
    sort_std: 0.005
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9127
    std: 0.002
    paper_value: 0.9127
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9106
    std: 0.0027
    paper_value: 0.9106
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 23
    true_value: 0.9106
    true_std: 0.0027
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9106
    sort_std: 0.0027
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9063
    std: 0.0014
    paper_value: 0.9063
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8272
    std: 0.0068
    paper_value: 0.8272
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 65
    true_value: 0.8272
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8272
    sort_std: 0.0008
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8001
    std: 0.0044
    paper_value: 0.8001
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 71
    true_value: 0.8001
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8001
    sort_std: 0.0044
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 74
    true_value: 0.7992
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7992
    sort_std: 0.0056
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7483
    std: 0.0081
    paper_value: 0.7483
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 78
    true_value: 0.7483
    true_std: 0.0081
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7483
    sort_std: 0.0081
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 80
    true_value: 0.717
    true_std: 0.0031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0685
    value_note: ''
    paper_rank: 86
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.717
    sort_std: 0.0031
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.6396
    std: 0.0062
    paper_value: 0.6396
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 88
    true_value: 0.6396
    true_std: 0.0062
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6396
    sort_std: 0.0062
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6011
    std: 0.0052
    paper_value: 0.6011
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 89
    true_value: 0.6363
    true_std: 0.023
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03520000000000001
    value_note: ''
    paper_rank: 90
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6363
    sort_std: 0.023
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 93
    true_value: 0.5963
    true_std: 0.0069
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5963
    sort_std: 0.0069
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
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
    value: 0.3592
    std: 0.0132
    paper_value: 0.3592
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 3
    true_value: 0.741
    true_std: 0.0189
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3818
    value_note: ''
    paper_rank: 99
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7298
    std: 0.0178
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
    global_rank: 4
    sort_value: 0.7298
    sort_std: 0.0178
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.3511
    std: 0.0124
    paper_value: 0.3511
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 23
    true_value: 0.6121
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26099999999999995
    value_note: ''
    paper_rank: 102
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.6121
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4501
    std: 0.0163
    paper_value: 0.4501
    paper_std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0842
    value_note: ''
    paper_rank: 49
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3895
    std: 0.0199
    paper_value: 0.3895
    paper_std: 0.0199
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11199999999999993
    value_note: ''
    paper_rank: 81
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.5015
    sort_std: 0.0192
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4265
    std: 0.0241
    paper_value: 0.4265
    paper_std: 0.0241
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 48
    true_value: 0.4582
    true_std: 0.0217
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031700000000000006
    value_note: ''
    paper_rank: 62
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.4582
    sort_std: 0.0217
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4197
    std: 0.0214
    paper_value: 0.4197
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 50
    true_value: 0.4498
    true_std: 0.0303
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03009999999999996
    value_note: global 0.4498 within std
    paper_rank: 68
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.4498
    sort_std: 0.0303
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4173
    std: 0.0207
    paper_value: 0.4173
    paper_std: 0.0207
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027600000000000013
    value_note: ''
    paper_rank: 68
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3889
    std: 0.0267
    paper_value: 0.3889
    paper_std: 0.0267
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 56
    true_value: 0.4342
    true_std: 0.0162
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04529999999999995
    value_note: ''
    paper_rank: 82
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.4342
    sort_std: 0.0162
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4078
    std: 0.0147
    paper_value: 0.4078
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008299999999999974
    value_note: global 0.4161 within std
    paper_rank: 73
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.41609999999999997
    sort_std: 0.0074
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3981
    std: 0.0228
    paper_value: 0.3981
    paper_std: 0.0228
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 77
    true_value: 0.3981
    true_std: 0.0228
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3981
    sort_std: 0.0228
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.351
    std: 0.0115
    paper_value: 0.351
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.044300000000000006
    value_note: ''
    paper_rank: 102
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.3953
    sort_std: 0.0088
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.3004
    std: 0.0203
    paper_value: 0.3004
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 82
    true_value: 0.389
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08860000000000001
    value_note: ''
    paper_rank: 109
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.389
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: WikiCS
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8557
    std: 0.0065
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
    global_rank: 1
    sort_value: 0.8557
    sort_std: 0.0065
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8515
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.8515
    sort_std: 0.0063
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8473
    std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.8473
    sort_std: 0.0059
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8026
    std: 0.0092
    paper_value: 0.8026
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.8362
    true_std: 0.0017
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033600000000000074
    value_note: ''
    paper_rank: 25
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.8362
    sort_std: 0.0017
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7792
    std: 0.0093
    paper_value: 0.7792
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.8341
    true_std: 0.0034
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05489999999999995
    value_note: ''
    paper_rank: 47
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.8341
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8107
    std: 0.0054
    paper_value: 0.8107
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 9
    true_value: 0.8322
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021500000000000075
    value_note: ''
    paper_rank: 15
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8322
    sort_std: 0.0078
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8005
    std: 0.0046
    paper_value: 0.8005
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 12
    true_value: 0.8271
    true_std: 0.0056
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026599999999999957
    value_note: ''
    paper_rank: 29
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.8271
    sort_std: 0.0056
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.803
    std: 0.0062
    paper_value: 0.803
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.8232
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020199999999999996
    value_note: ''
    paper_rank: 21
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8232
    sort_std: 0.0069
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7513
    std: 0.0093
    paper_value: 0.7513
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.8103
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05900000000000005
    value_note: ''
    paper_rank: 51
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.8103
    sort_std: 0.0094
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8069
    std: 0.0031
    paper_value: 0.8069
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 20
    true_value: 0.8069
    true_std: 0.0031
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8069
    sort_std: 0.0031
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7938
    std: 0.0062
    paper_value: 0.7938
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 36
    true_value: 0.7938
    true_std: 0.0082
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7938
    sort_std: 0.0082
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7866
    std: 0.0049
    paper_value: 0.7866
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 39
    true_value: 0.7926
    true_std: 0.0057
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006000000000000005
    value_note: ''
    paper_rank: 43
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7926
    sort_std: 0.0057
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7796
    std: 0.0063
    paper_value: 0.7796
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 47
    true_value: 0.7796
    true_std: 0.0003
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7796
    sort_std: 0.0003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7353
    std: 0.0012
    paper_value: 0.7353
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.734
    std: 0.0022
    paper_value: 0.734
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 15
    true_value: 0.734
    true_std: 0.0022
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.0022
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.733
    std: 0.0018
    paper_value: 0.733
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.73
    std: 0.0028
    paper_value: 0.73
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 26
    true_value: 0.73
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.0028
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7276
    std: 0.0033
    paper_value: 0.7276
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 31
    true_value: 0.7276
    true_std: 0.0033
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.0033
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7276
    std: 0.0029
    paper_value: 0.7276
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.7276
    true_std: 0.0029
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.0029
    is_best: false
  - model: GCN* (-) Residual Connections
    model_key: gcn* (-) residual connections
    model_plain: GCN* (-) Residual Connections
    value: 0.7247
    std: 0.0034
    paper_value: 0.7247
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 39
    true_value: 0.7247
    true_std: 0.0034
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7247
    sort_std: 0.0034
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7232
    std: 0.0036
    paper_value: 0.7232
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 41
    true_value: 0.7244
    true_std: 0.0028
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0012000000000000899
    value_note: global 0.7244 within std
    paper_rank: 44
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7244
    sort_std: 0.0028
    is_best: false
  - model: GraphSAGE* (-) Residual Connections
    model_key: graphsage* (-) residual connections
    model_plain: GraphSAGE* (-) Residual Connections
    value: 0.7222
    std: 0.0049
    paper_value: 0.7222
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 49
    true_value: 0.7222
    true_std: 0.0049
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7222
    sort_std: 0.0049
    is_best: false
  - model: GCN* (-) Dropout
    model_key: gcn* (-) dropout
    model_plain: GCN* (-) Dropout
    value: 0.7206
    std: 0.0013
    paper_value: 0.7206
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 50
    true_value: 0.7206
    true_std: 0.0013
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7206
    sort_std: 0.0013
    is_best: false
  - model: GAT* (-) Dropout
    model_key: gat* (-) dropout
    model_plain: GAT* (-) Dropout
    value: 0.7168
    std: 0.0032
    paper_value: 0.7168
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 65
    true_value: 0.7168
    true_std: 0.0032
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7168
    sort_std: 0.0032
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7088
    std: 0.0024
    paper_value: 0.7088
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 67
    true_value: 0.7152
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006399999999999961
    value_note: ''
    paper_rank: 75
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.7152
    sort_std: 0.0024
    is_best: false
  - model: GCN* (-) Normalization
    model_key: gcn* (-) normalization
    model_plain: GCN* (-) Normalization
    value: 0.7133
    std: 0.0029
    paper_value: 0.7133
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 69
    true_value: 0.7133
    true_std: 0.0029
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7133
    sort_std: 0.0029
    is_best: false
  - model: GraphSAGE* (-) Dropout
    model_key: graphsage* (-) dropout
    model_plain: GraphSAGE* (-) Dropout
    value: 0.713
    std: 0.0021
    paper_value: 0.713
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 70
    true_value: 0.713
    true_std: 0.0021
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.713
    sort_std: 0.0021
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7123
    std: 0.0059
    paper_value: 0.7123
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 71
    true_value: 0.7123
    true_std: 0.0059
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7123
    sort_std: 0.0059
    is_best: false
  - model: GraphSAGE* (-) Normalization
    model_key: graphsage* (-) normalization
    model_plain: GraphSAGE* (-) Normalization
    value: 0.7113
    std: 0.0027
    paper_value: 0.7113
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 73
    true_value: 0.7113
    true_std: 0.0027
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7113
    sort_std: 0.0027
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6778
    std: 0.0028
    paper_value: 0.6778
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 89
    true_value: 0.6778
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6778
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
  dataset: ogbn-proteins
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8501
    std: 0.0046
    paper_value: 0.8501
    paper_std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 1
    true_value: 0.8501
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8501
    sort_std: 0.0046
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8221
    std: 0.0032
    paper_value: 0.8221
    paper_std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 2
    true_value: 0.8221
    true_std: 0.0032
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8221
    sort_std: 0.0032
    is_best: false
  - model: HGODE
    model_key: hgode
    model_plain: HGODE
    value: 0.8124
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8124
    sort_std: 0.0063
    is_best: false
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.8034
    std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8034
    sort_std: 0.0032
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7992
    std: 0.0048
    paper_value: 0.7992
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 5
    true_value: 0.7992
    true_std: 0.0048
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7992
    sort_std: 0.0048
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7955
    std: 0.0079
    metric: ROC-AUC
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
    uses_external_data: null
    is_global_top: true
    global_rank: 6
    sort_value: 0.7955
    sort_std: 0.0079
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7953
    std: 0.0067
    paper_value: 0.7953
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 7
    true_value: 0.7953
    true_std: 0.0067
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7953
    sort_std: 0.0067
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7931
    std: 0.0042
    paper_value: 0.7931
    paper_std: 0.0042
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 11
    true_value: 0.7931
    true_std: 0.0042
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7931
    sort_std: 0.0042
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7786
    std: 0.0084
    paper_value: 0.7786
    paper_std: 0.0084
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.7786
    true_std: 0.0084
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7786
    sort_std: 0.0084
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7762
    std: 0.0033
    paper_value: 0.7762
    paper_std: 0.0033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 15
    true_value: 0.7762
    true_std: 0.0033
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7762
    sort_std: 0.0033
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7729
    std: 0.0046
    paper_value: 0.7729
    paper_std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 16
    true_value: 0.7729
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7729
    sort_std: 0.0046
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7715
    std: 0.0064
    paper_value: 0.7715
    paper_std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 17
    true_value: 0.7725
    true_std: 0.0042
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.7725 within std
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7725
    sort_std: 0.0042
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7217
    std: 0.0045
    paper_value: 0.7217
    paper_std: 0.0045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 21
    true_value: 0.7217
    true_std: 0.0045
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7217
    sort_std: 0.0045
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
- benchmark: Heterophilic Graphs
  datasets:
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
- benchmark: OGB
  datasets:
  - *id015
  - *id016
main_figure: /figures/2406.08993/main_figure.png
---

