---
title: Graph Inductive Biases in Transformers without Message Passing
arxiv_id: '2305.17589'
source_url: ''
authors: []
published_date: May 27, 2023
published_date_iso: '2023-05-27'
abstract: 'Transformers for graph data are increasingly widely studied and successful
  in numerous learning tasks. Graph inductive biases are crucial for Graph Transformers,
  and previous works incorporate them using message-passing modules and/or positional
  encodings. However, Graph Transformers that use message-passing inherit known issues
  of message-passing, and differ significantly from Transformers used in other domains,
  thus making transfer of research advances more difficult. On the other hand, Graph
  Transformers without message-passing often perform poorly on smaller datasets, where
  inductive biases are more crucial. To bridge this gap, we propose the Graph Inductive
  bias Transformer (GRIT) -- a new Graph Transformer that incorporates graph inductive
  biases without using message passing. GRIT is based on several architectural changes
  that are each theoretically and empirically justified, including: learned relative
  positional encodings initialized with random walk probabilities, a flexible attention
  mechanism that updates node and node-pair representations, and injection of degree
  information in each layer. We prove that GRIT is expressive -- it can express shortest
  path distances and various graph propagation matrices. GRIT achieves state-of-the-art
  empirical performance across a variety of graph datasets, thus showing the power
  that Graph Transformers without message-passing can deliver.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- ILLS
mrr: 0.4276
adjusted_mrr: 0.4276
mrr_dataset_count: 22
benchmark_categories:
- Classic
- TU Dortmund
- OGB
- Quantum Chemistry
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
- &id012
  dataset: AQSOL
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.49
    std: 0.01
    paper_value: 0.49
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.49
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.01
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.51
    std: 0.02
    paper_value: 0.51
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.51
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51
    sort_std: 0.02
    is_best: true
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.52
    std: 0.02
    paper_value: 0.52
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.52
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.02
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.53
    std: 0.02
    paper_value: 0.53
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.53
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.02
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.55
    std: 0.02
    paper_value: 0.55
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.55
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.55
    sort_std: 0.02
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.56
    std: 0.03
    paper_value: 0.56
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.58
    std: 0.02
    paper_value: 0.58
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.58
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.58
    sort_std: 0.02
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.59
    std: 0.02
    paper_value: 0.59
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.59
    true_std: 0.02
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.59
    sort_std: 0.02
    is_best: false
  - model: Ours(100K)
    model_key: ours(100k)
    model_plain: Ours(100K)
    value: 0.92
    std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_display: Jan 2022
    date_iso: 2022-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.92
    sort_std: 0.009
    is_best: false
  - model: GatedGCN-PE/E(500K)
    model_key: gatedgcn-pe/e(500k)
    model_plain: GatedGCN-PE/E(500K)
    value: 0.996
    std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_display: Jan 2022
    date_iso: 2022-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.996
    sort_std: 0.008
    is_best: false
  - model: PNA(100K)
    model_key: pna(100k)
    model_plain: PNA(100K)
    value: 1.083
    std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_display: Jan 2022
    date_iso: 2022-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 1.083
    sort_std: 0.011
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: Amazon-Computers
  rows:
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9228
    sort_std: 0.0039
    is_best: true
  - model: SGT
    model_key: sgt
    model_plain: SGT
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
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9226
    sort_std: 0.0018
    is_best: true
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
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9206
    sort_std: 0.0033
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.823
    std: 0.015
    paper_value: 0.823
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.9078
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0848000000000001
    value_note: ''
    paper_rank: 43
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.9078
    sort_std: 0.0013
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.828
    std: 0.014
    paper_value: 0.828
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.9018
    true_std: 0.0017
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07380000000000009
    value_note: ''
    paper_rank: 41
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.9018
    sort_std: 0.0017
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.012
    paper_value: 0.815
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.8965
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08150000000000002
    value_note: ''
    paper_rank: 43
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.8965
    sort_std: 0.0052
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.812
    std: 0.01
    paper_value: 0.812
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 32
    true_value: 0.8626
    true_std: 0.0056
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05059999999999998
    value_note: ''
    paper_rank: 43
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.8626
    sort_std: 0.0056
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.841
    std: 0.009
    paper_value: 0.841
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 38
    true_value: 0.841
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.009
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.835
    std: 0.013
    paper_value: 0.835
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 39
    true_value: 0.835
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.809
    std: 0.011
    paper_value: 0.809
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 44
    true_value: 0.809
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Amazon-Photo
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9537
    std: 0.0044
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
    sort_value: 0.9537
    sort_std: 0.0044
    is_best: true
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.9445
    std: 0.0045
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
    global_rank: 2
    sort_value: 0.9445
    sort_std: 0.0045
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.9435
    std: 0.0044
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
    global_rank: 3
    sort_value: 0.9435
    sort_std: 0.0044
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.831
    std: 0.005
    paper_value: 0.831
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.9432
    true_std: 0.0014
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11220000000000008
    value_note: ''
    paper_rank: 28
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.9432
    sort_std: 0.0014
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.835
    std: 0.006
    paper_value: 0.835
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.9387
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10370000000000001
    value_note: ''
    paper_rank: 28
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.9387
    sort_std: 0.0011
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.828
    std: 0.005
    paper_value: 0.828
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.927
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09900000000000009
    value_note: ''
    paper_rank: 28
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.927
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.839
    std: 0.004
    paper_value: 0.839
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 16
    true_value: 0.9211
    true_std: 0.0032
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08210000000000006
    value_note: ''
    paper_rank: 27
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9211
    sort_std: 0.0032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.821
    std: 0.004
    paper_value: 0.821
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 25
    true_value: 0.8916
    true_std: 0.0103
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0706
    value_note: ''
    paper_rank: 28
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8916
    sort_std: 0.0103
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.851
    std: 0.003
    paper_value: 0.851
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 26
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.842
    std: 0.003
    paper_value: 0.842
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 27
    true_value: 0.842
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id018
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.638
    std: 0.012
    paper_value: 0.638
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.826
    true_std: 0.022
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18799999999999994
    value_note: ''
    paper_rank: 53
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.022
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.649
    std: 0.013
    paper_value: 0.649
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.822
    true_std: 0.021
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17299999999999993
    value_note: ''
    paper_rank: 52
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.822
    sort_std: 0.021
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.661
    std: 0.009
    paper_value: 0.661
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 38
    true_value: 0.7473
    true_std: 0.0109
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08629999999999993
    value_note: ''
    paper_rank: 50
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.7473
    sort_std: 0.0109
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.645
    std: 0.015
    paper_value: 0.645
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 42
    true_value: 0.739
    true_std: 0.017
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09399999999999997
    value_note: ''
    paper_rank: 53
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.739
    sort_std: 0.017
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.674
    std: 0.008
    paper_value: 0.674
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 50
    true_value: 0.674
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.674
    sort_std: 0.008
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.655
    std: 0.01
    paper_value: 0.655
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 51
    true_value: 0.655
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.01
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.652
    std: 0.011
    paper_value: 0.652
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 52
    true_value: 0.652
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.652
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: CiteSeer
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.8285
    std: 0.0038
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8285
    sort_std: 0.0038
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.8114
    std: 0.0034
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8114
    sort_std: 0.0034
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.7741
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_display: May 2022
    date_iso: '2022-05-15'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7741
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.728
    std: 0.012
    paper_value: 0.728
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.7643
    true_std: 0.0131
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0363
    value_note: ''
    paper_rank: 41
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.7643
    sort_std: 0.0131
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.715
    std: 0.018
    paper_value: 0.715
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.7643
    true_std: 0.0119
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04930000000000001
    value_note: ''
    paper_rank: 50
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.7643
    sort_std: 0.0119
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.735
    std: 0.011
    paper_value: 0.735
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 26
    true_value: 0.759
    true_std: 0.0091
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02400000000000002
    value_note: ''
    paper_rank: 38
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.0091
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.758
    std: 0.008
    paper_value: 0.758
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 30
    true_value: 0.758
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.721
    std: 0.015
    paper_value: 0.721
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 32
    true_value: 0.7577
    true_std: 0.0096
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.036700000000000066
    value_note: ''
    paper_rank: 43
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.7577
    sort_std: 0.0096
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.742
    std: 0.009
    paper_value: 0.742
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 36
    true_value: 0.742
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.725
    std: 0.014
    paper_value: 0.725
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 42
    true_value: 0.7255
    true_std: 0.0178
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000500000000000056
    value_note: global 0.7255 within std
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7255
    sort_std: 0.0178
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9577
    sort_std: 0.0015
    is_best: true
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9575
    std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9575
    sort_std: 0.0009
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.848
    std: 0.005
    paper_value: 0.848
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.9449
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09689999999999999
    value_note: ''
    paper_rank: 32
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9449
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.842
    std: 0.006
    paper_value: 0.842
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.9361
    true_std: 0.0014
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09410000000000007
    value_note: ''
    paper_rank: 32
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.9361
    sort_std: 0.0014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.835
    std: 0.005
    paper_value: 0.835
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 16
    true_value: 0.9292
    true_std: 0.0012
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09420000000000006
    value_note: ''
    paper_rank: 33
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.9292
    sort_std: 0.0012
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.003
    paper_value: 0.862
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 30
    true_value: 0.862
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.851
    std: 0.004
    paper_value: 0.851
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 31
    true_value: 0.851
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.839
    std: 0.005
    paper_value: 0.839
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 33
    true_value: 0.839
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.831
    std: 0.004
    paper_value: 0.831
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 34
    true_value: 0.831
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.831
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Coauthor-Physics
  rows:
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9734
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9734
    sort_std: 0.0003
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9716
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9716
    sort_std: 0.0013
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.945
    std: 0.003
    paper_value: 0.945
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.945
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.945
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.941
    std: 0.003
    paper_value: 0.941
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.941
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.941
    sort_std: 0.003
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.938
    std: 0.004
    paper_value: 0.938
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.938
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.938
    sort_std: 0.004
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.935
    std: 0.004
    paper_value: 0.935
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.935
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.932
    std: 0.005
    paper_value: 0.932
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.932
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.932
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.93
    std: 0.005
    paper_value: 0.93
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.93
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.93
    sort_std: 0.005
    is_best: false
  - model: GS-mean
    model_key: gs-mean
    model_plain: GS-mean
    value: 0.93
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_display: Nov 2018
    date_iso: 2018-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.93
    sort_std: 0.008
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.928
    std: 0.006
    paper_value: 0.928
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.928
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.928
    sort_std: 0.006
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.925
    std: 0.007
    paper_value: 0.925
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.925
    true_std: 0.007
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.925
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Cora
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9285
    std: 0.0054
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
    sort_value: 0.9285
    sort_std: 0.0054
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9171
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9171
    sort_std: 0.0029
    is_best: false
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.825
    std: 0.006
    paper_value: 0.825
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 26
    true_value: 0.879
    true_std: 0.0173
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05400000000000005
    value_note: ''
    paper_rank: 69
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.0173
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.005
    paper_value: 0.815
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 29
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06280000000000008
    value_note: ''
    paper_rank: 77
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.828
    std: 0.007
    paper_value: 0.828
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 35
    true_value: 0.8759
    true_std: 0.0168
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047900000000000054
    value_note: ''
    paper_rank: 66
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.8759
    sort_std: 0.0168
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.83
    std: 0.008
    paper_value: 0.83
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 39
    true_value: 0.8711
    true_std: 0.0148
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041100000000000025
    value_note: ''
    paper_rank: 65
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.8711
    sort_std: 0.0148
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.842
    std: 0.003
    paper_value: 0.842
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 59
    true_value: 0.842
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.835
    std: 0.004
    paper_value: 0.835
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 62
    true_value: 0.835
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: VRN Ensemble
    model_key: vrn ensemble
    model_plain: VRN Ensemble
    value: 0.9554
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9554
    sort_std: null
    is_best: false
  - model: MVCNN
    model_key: mvcnn
    model_plain: MVCNN
    value: 0.901
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.801
    std: 0.011
    paper_value: 0.801
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.9
    true_std: null
    value_gap_source_arxiv: '2511.20406'
    value_gap_source_title: Short-Range Oversquashing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09899999999999998
    value_note: ''
    paper_rank: 21
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.825
    std: 0.008
    paper_value: 0.825
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.825
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.814
    std: 0.009
    paper_value: 0.814
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 19
    true_value: 0.814
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.798
    std: 0.013
    paper_value: 0.798
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 23
    true_value: 0.798
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.795
    std: 0.012
    paper_value: 0.795
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 24
    true_value: 0.795
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.012
    is_best: false
  - model: Jumping Knowledge
    model_key: jumping knowledge
    model_plain: Jumping Knowledge
    value: 0.788
    std: 0.014
    paper_value: 0.788
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 32
    true_value: 0.788
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.782
    std: 0.015
    paper_value: 0.782
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 33
    true_value: 0.782
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.015
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.775
    std: 0.018
    paper_value: 0.775
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 39
    true_value: 0.775
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.018
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id019
  dataset: ENZYMES
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.794
    std: 0.008
    paper_value: 0.794
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.794
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.008
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.778
    std: 0.009
    paper_value: 0.778
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.778
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.778
    sort_std: 0.009
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.762
    std: 0.01
    paper_value: 0.762
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.762
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.01
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.756
    std: 0.011
    paper_value: 0.756
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.756
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.011
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.741
    std: 0.014
    paper_value: 0.741
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.741
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.014
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.735
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.012
    is_best: false
  - model: GSO
    model_key: gso
    model_plain: GSO
    value: 0.735
    std: 0.0639
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.735
    sort_std: 0.0639
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.723
    std: 0.015
    paper_value: 0.723
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.723
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.015
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.718
    std: 0.018
    paper_value: 0.718
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.718
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.018
    is_best: false
  - model: UnionSNN
    model_key: unionsnn
    model_plain: UnionSNN
    value: 0.6817
    std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.6817
    sort_std: 0.057
    is_best: false
  - model: UnionGCN
    model_key: uniongcn
    model_plain: UnionGCN
    value: 0.6783
    std: 0.061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.6783
    sort_std: 0.061
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
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
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.006
    paper_value: 0.785
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.785
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.006
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.771
    std: 0.007
    paper_value: 0.771
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.771
    true_std: 0.007
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.007
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.762
    std: 0.008
    paper_value: 0.762
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.762
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.758
    std: 0.009
    paper_value: 0.758
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 17
    true_value: 0.758
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.722
    std: 0.015
    paper_value: 0.722
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.757
    true_std: 0.036
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03500000000000003
    value_note: global 0.7570 within std
    paper_rank: 46
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.757
    sort_std: 0.036
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.745
    std: 0.013
    paper_value: 0.745
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 21
    true_value: 0.755
    true_std: 0.04
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.7550 within std
    paper_rank: 27
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.04
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.741
    std: 0.011
    paper_value: 0.741
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 35
    true_value: 0.741
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.011
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 42
    true_value: 0.735
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id021
  dataset: IMDB-MULTI
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.724
    std: 0.009
    paper_value: 0.724
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.724
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.009
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.712
    std: 0.011
    paper_value: 0.712
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.712
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: 0.011
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.705
    std: 0.01
    paper_value: 0.705
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.705
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.01
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.701
    std: 0.014
    paper_value: 0.701
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.701
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.014
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.698
    std: 0.013
    paper_value: 0.698
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.698
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.698
    sort_std: 0.013
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.695
    std: 0.012
    paper_value: 0.695
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.695
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.682
    std: 0.015
    paper_value: 0.682
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.682
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.015
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.5731
    std: 0.0219
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
    global_rank: 8
    sort_value: 0.5731
    sort_std: 0.0219
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.5632
    std: 0.0018
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
    global_rank: 9
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.532
    std: 0.036
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
    global_rank: 10
    sort_value: 0.532
    sort_std: 0.036
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id017
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.83
    std: 0.02
    paper_value: 0.83
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06400000000000006
    value_note: ''
    paper_rank: 46
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: true
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.885
    std: 0.01
    paper_value: 0.885
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.885
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.885
    sort_std: 0.01
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.87
    std: 0.012
    paper_value: 0.87
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 22
    true_value: 0.87
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87
    sort_std: 0.012
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.86
    std: 0.015
    paper_value: 0.86
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 27
    true_value: 0.86
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.015
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.815
    std: 0.023
    paper_value: 0.815
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 30
    true_value: 0.851
    true_std: 0.076
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03600000000000003
    value_note: global 0.8510 within std
    paper_rank: 50
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.076
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.85
    std: 0.018
    paper_value: 0.85
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 31
    true_value: 0.85
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.018
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.84
    std: 0.022
    paper_value: 0.84
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 37
    true_value: 0.84
    true_std: 0.022
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.022
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.835
    std: 0.025
    paper_value: 0.835
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 41
    true_value: 0.835
    true_std: 0.025
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.825
    std: 0.021
    paper_value: 0.825
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 49
    true_value: 0.825
    true_std: 0.021
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: NCI1
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.874
    std: 0.003
    paper_value: 0.874
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.874
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.874
    sort_std: 0.003
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.862
    std: 0.004
    paper_value: 0.862
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.862
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.004
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.858
    std: 0.005
    paper_value: 0.858
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.858
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.851
    std: 0.003
    paper_value: 0.851
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.845
    std: 0.004
    paper_value: 0.845
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.838
    std: 0.006
    paper_value: 0.838
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.838
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: 0.006
    is_best: false
  - model: GSO
    model_key: gso
    model_plain: GSO
    value: 0.8362
    std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.8362
    sort_std: 0.0138
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.8352
    std: 0.0375
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
    global_rank: 8
    sort_value: 0.8352
    sort_std: 0.0375
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.832
    std: 0.005
    paper_value: 0.832
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.832
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.832
    sort_std: 0.005
    is_best: false
  - model: GCN^2
    model_key: gcn^2
    model_plain: GCN^2
    value: 0.83
    std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.83
    sort_std: 0.0189
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id027
  dataset: PCQM4Mv2
  rows:
  - model: GPS-medium
    model_key: gps-medium
    model_plain: GPS-medium
    value: 0.0858
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0858
    sort_std: null
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.0864
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0864
    sort_std: null
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.0872
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0872
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.119
    std: 0.001
    paper_value: 0.119
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.119
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.119
    sort_std: 0.001
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.121
    std: 0.001
    paper_value: 0.121
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.121
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.121
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.132
    std: 0.002
    paper_value: 0.132
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.1218
    true_std: null
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0102
    value_note: ''
    paper_rank: 21
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.1218
    sort_std: null
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.122
    std: 0.001
    paper_value: 0.122
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.122
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.122
    sort_std: 0.001
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.123
    std: 0.001
    paper_value: 0.123
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 17
    true_value: 0.123
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.123
    sort_std: 0.001
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.124
    std: 0.001
    paper_value: 0.124
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.124
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.124
    sort_std: 0.001
    is_best: false
  - model: PNA + RWSE
    model_key: pna + rwse
    model_plain: PNA + RWSE
    value: 0.125
    std: 0.001
    paper_value: 0.125
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 19
    true_value: 0.125
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.125
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.128
    std: 0.001
    paper_value: 0.128
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 21
    true_value: 0.128
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.128
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.135
    std: 0.003
    paper_value: 0.135
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 22
    true_value: 0.135
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.135
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.136
    std: 0.002
    paper_value: 0.136
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 23
    true_value: 0.136
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.136
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.138
    std: 0.004
    paper_value: 0.138
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 24
    true_value: 0.138
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.138
    sort_std: 0.004
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: PPI
  rows:
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.981
    std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.981
    sort_std: 0.004
    is_best: true
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.97
    std: 0.003
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.97
    sort_std: 0.003
    is_best: false
  - model: Stochastic-GCN
    model_key: stochastic-gcn
    model_plain: Stochastic-GCN
    value: 0.963
    std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.963
    sort_std: 0.01
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.942
    std: 0.001
    paper_value: 0.942
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.942
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.942
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.935
    std: 0.001
    paper_value: 0.935
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.935
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.001
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.933
    std: 0.002
    paper_value: 0.933
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.933
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.933
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.931
    std: 0.003
    paper_value: 0.931
    paper_std: 0.003
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.931
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.931
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.929
    std: 0.002
    paper_value: 0.929
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.929
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.929
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.928
    std: 0.001
    paper_value: 0.928
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.928
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.928
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.926
    std: 0.002
    paper_value: 0.926
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.926
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.926
    sort_std: 0.002
    is_best: false
  metric: F1
  higher_is_better: true
- &id014
  dataset: PROTEINS
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.802
    std: 0.009
    paper_value: 0.802
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.802
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.795
    std: 0.01
    paper_value: 0.795
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.795
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.01
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.791
    std: 0.011
    paper_value: 0.791
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.791
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.011
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.788
    std: 0.013
    paper_value: 0.788
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.788
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.013
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.785
    std: 0.012
    paper_value: 0.785
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.012
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.781
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.781
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.779
    std: 0.014
    paper_value: 0.779
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.779
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.014
    is_best: true
  - model: g-U-Nets
    model_key: g-u-nets
    model_plain: g-U-Nets
    value: 0.7768
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_display: May 2019
    date_iso: '2019-05-11'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.7768
    sort_std: null
    is_best: false
  - model: SE2P-C2
    model_key: se2p-c2
    model_plain: SE2P-C2
    value: 0.776
    std: 0.063
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
    global_rank: 9
    sort_value: 0.776
    sort_std: 0.063
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.772
    std: 0.015
    paper_value: 0.772
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: 0.018
    paper_value: 0.768
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.768
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.018
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: Flan-T5-large
    model_key: flan-t5-large
    model_plain: Flan-T5-large
    value: 0.9462
    std: 0.0013
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
    global_rank: 1
    sort_value: 0.9462
    sort_std: 0.0013
    is_best: true
  - model: Flan-T5-base
    model_key: flan-t5-base
    model_plain: Flan-T5-base
    value: 0.9445
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
    sort_value: 0.9445
    sort_std: 0.0012
    is_best: true
  - model: Llama-7b
    model_key: llama-7b
    model_plain: Llama-7b
    value: 0.9384
    std: 0.0025
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
    global_rank: 3
    sort_value: 0.9384
    sort_std: 0.0025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.812
    std: 0.005
    paper_value: 0.812
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.889
    true_std: 0.0032
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07699999999999996
    value_note: ''
    paper_rank: 30
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.889
    sort_std: 0.0032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.808
    std: 0.004
    paper_value: 0.808
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 17
    true_value: 0.8685
    true_std: 0.0011
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0605
    value_note: ''
    paper_rank: 30
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8685
    sort_std: 0.0011
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.815
    std: 0.006
    paper_value: 0.815
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 21
    true_value: 0.8328
    true_std: 0.0012
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017800000000000038
    value_note: ''
    paper_rank: 29
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.8328
    sort_std: 0.0012
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.825
    std: 0.003
    paper_value: 0.825
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 23
    true_value: 0.825
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.821
    std: 0.004
    paper_value: 0.821
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 25
    true_value: 0.821
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.004
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.818
    std: 0.005
    paper_value: 0.818
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 27
    true_value: 0.818
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.818
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id036
  dataset: QM9
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.025
    std: 0.001
    paper_value: 0.025
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.025
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.001
    is_best: true
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.026
    std: 0.001
    paper_value: 0.026
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.026
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.026
    sort_std: 0.001
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.028
    std: 0.001
    paper_value: 0.028
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.028
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.028
    sort_std: 0.001
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.033
    std: 0.001
    paper_value: 0.033
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.033
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.033
    sort_std: 0.001
    is_best: false
  - model: EquiBind
    model_key: equibind
    model_plain: EquiBind
    value: 0.045
    std: 0.002
    paper_value: 0.045
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.045
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.045
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.048
    std: 0.002
    paper_value: 0.048
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.048
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.048
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.051
    std: 0.002
    paper_value: 0.051
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.051
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.051
    sort_std: 0.002
    is_best: false
  - model: PPGN
    model_key: ppgn
    model_plain: PPGN
    value: 0.0512
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_display: Feb 2020
    date_iso: 2020-02
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.0512
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.056
    std: 0.003
    paper_value: 0.056
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.056
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.056
    sort_std: 0.003
    is_best: false
  - model: WL
    model_key: wl
    model_plain: WL
    value: 0.0567
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_display: Feb 2020
    date_iso: 2020-02
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.0567
    sort_std: null
    is_best: false
  - model: Deep LRP-1-3
    model_key: deep lrp-1-3
    model_plain: Deep LRP-1-3
    value: 0.0567
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_display: Feb 2020
    date_iso: 2020-02
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.0567
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id022
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
    value: 0.881
    std: 0.004
    paper_value: 0.881
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.918
    true_std: 0.01
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03700000000000003
    value_note: ''
    paper_rank: 11
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
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
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.911
    std: 0.018
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
    global_rank: 4
    sort_value: 0.911
    sort_std: 0.018
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.894
    std: 0.002
    paper_value: 0.894
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.894
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.889
    std: 0.002
    paper_value: 0.889
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.889
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.885
    std: 0.003
    paper_value: 0.885
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 11
    true_value: 0.885
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.885
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.878
    std: 0.003
    paper_value: 0.878
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.878
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.878
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.872
    std: 0.004
    paper_value: 0.872
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.872
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.872
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.865
    std: 0.005
    paper_value: 0.865
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 16
    true_value: 0.865
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.865
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id020
  dataset: REDDIT-MULTI-5K
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.871
    std: 0.002
    paper_value: 0.871
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.871
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.871
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.862
    std: 0.003
    paper_value: 0.862
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.862
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.856
    std: 0.002
    paper_value: 0.856
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.856
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.856
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.851
    std: 0.003
    paper_value: 0.851
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.848
    std: 0.004
    paper_value: 0.848
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.848
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.842
    std: 0.002
    paper_value: 0.842
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.842
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.835
    std: 0.003
    paper_value: 0.835
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.835
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.003
    is_best: false
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 0.606
    std: 0.003
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
    global_rank: 8
    sort_value: 0.606
    sort_std: 0.003
    is_best: false
  - model: SRF (RBF, AG)
    model_key: srf (rbf, ag)
    model_plain: SRF (RBF, AG)
    value: 0.6053
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 9
    sort_value: 0.6053
    sort_std: 0.0029
    is_best: false
  - model: SRF (L, AG)
    model_key: srf (l, ag)
    model_plain: SRF (L, AG)
    value: 0.6033
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 10
    sort_value: 0.6033
    sort_std: 0.0037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Reddit
  rows:
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.968
    std: 0.0
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.968
    sort_std: 0.0
    is_best: true
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.966
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_display: May 2019
    date_iso: 2019-05
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.966
    sort_std: null
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.966
    std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.966
    sort_std: 0.001
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.935
    std: 0.001
    paper_value: 0.935
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.954
    true_std: null
    value_gap_source_arxiv: '1905.07953'
    value_gap_source_title: 'Cluster-GCN: An Efficient Algorithm for Training Deep
      and Large Graph Convolutional Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018999999999999906
    value_note: ''
    paper_rank: 18
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.954
    sort_std: null
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.941
    std: 0.001
    paper_value: 0.941
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.941
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.941
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.938
    std: 0.001
    paper_value: 0.938
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.938
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.938
    sort_std: 0.001
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.937
    std: 0.001
    paper_value: 0.937
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 16
    true_value: 0.937
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.937
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.936
    std: 0.001
    paper_value: 0.936
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.936
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.936
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.934
    std: 0.002
    paper_value: 0.934
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 19
    true_value: 0.934
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.933
    std: 0.002
    paper_value: 0.933
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 20
    true_value: 0.933
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.933
    sort_std: 0.002
    is_best: false
  metric: F1
  higher_is_better: true
- &id009
  dataset: WikiCS
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
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8019
    std: 0.0041
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
    global_rank: 2
    sort_value: 0.8019
    sort_std: 0.0041
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.7901
    std: 0.0068
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
    global_rank: 3
    sort_value: 0.7901
    sort_std: 0.0068
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.789
    std: 0.01
    paper_value: 0.789
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.789
    true_std: 0.01
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.789
    sort_std: 0.01
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.752
    std: 0.014
    paper_value: 0.752
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.7887
    true_std: 0.0011
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.036699999999999955
    value_note: ''
    paper_rank: 17
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.7887
    sort_std: 0.0011
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.735
    std: 0.012
    paper_value: 0.735
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.7747
    true_std: 0.0085
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03970000000000007
    value_note: ''
    paper_rank: 19
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.7747
    sort_std: 0.0085
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.741
    std: 0.015
    paper_value: 0.741
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 16
    true_value: 0.7691
    true_std: 0.0082
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.028100000000000014
    value_note: ''
    paper_rank: 19
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7691
    sort_std: 0.0082
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.763
    std: 0.013
    paper_value: 0.763
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 17
    true_value: 0.763
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.013
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.745
    std: 0.016
    paper_value: 0.745
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 19
    true_value: 0.745
    true_std: 0.016
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.016
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.728
    std: 0.011
    paper_value: 0.728
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 20
    true_value: 0.728
    true_std: 0.011
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
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
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.278
    std: 0.006
    paper_value: 0.278
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.006
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.272
    value_note: ''
    paper_rank: 106
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.006
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.014
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
    global_rank: 3
    sort_value: 0.014
    sort_std: null
    is_best: false
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
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.296
    std: 0.005
    paper_value: 0.296
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27199999999999996
    value_note: ''
    paper_rank: 107
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.245
    std: 0.003
    paper_value: 0.245
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 31
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.178
    value_note: ''
    paper_rank: 106
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.067
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.285
    std: 0.004
    paper_value: 0.285
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 67
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.174
    value_note: ''
    paper_rank: 107
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.142
    std: 0.001
    paper_value: 0.142
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 81
    true_value: 0.142
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.142
    sort_std: 0.001
    is_best: false
  - model: DimeNet++ (large)
    model_key: dimenet++ (large)
    model_plain: DimeNet++ (large)
    value: 0.158
    std: 0.002
    paper_value: 0.158
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 89
    true_value: 0.158
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.158
    sort_std: 0.002
    is_best: false
  - model: PaiNN (large)
    model_key: painn (large)
    model_plain: PaiNN (large)
    value: 0.165
    std: 0.002
    paper_value: 0.165
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 91
    true_value: 0.165
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.165
    sort_std: 0.002
    is_best: false
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.172
    std: 0.002
    paper_value: 0.172
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 94
    true_value: 0.172
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.172
    sort_std: 0.002
    is_best: false
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.185
    std: 0.003
    paper_value: 0.185
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 97
    true_value: 0.185
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.185
    sort_std: 0.003
    is_best: false
  - model: SE(3)-Transformer
    model_key: se(3)-transformer
    model_plain: SE(3)-Transformer
    value: 0.188
    std: 0.003
    paper_value: 0.188
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 98
    true_value: 0.188
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.188
    sort_std: 0.003
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.195
    std: 0.004
    paper_value: 0.195
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 101
    true_value: 0.195
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.195
    sort_std: 0.004
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.198
    std: 0.002
    paper_value: 0.198
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 102
    true_value: 0.198
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.198
    sort_std: 0.002
    is_best: false
  - model: EquiBind
    model_key: equibind
    model_plain: EquiBind
    value: 0.21
    std: 0.005
    paper_value: 0.21
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 103
    true_value: 0.21
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.21
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id025
  dataset: ogbg-molhiv
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    paper_value: 0.862
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.862
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.002
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    paper_value: 0.858
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.858
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.002
    is_best: true
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.855
    std: 0.002
    paper_value: 0.855
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.855
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.855
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.853
    std: 0.003
    paper_value: 0.853
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.853
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.853
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.851
    std: 0.004
    paper_value: 0.851
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.851
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.848
    std: 0.003
    paper_value: 0.848
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.848
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.845
    std: 0.004
    paper_value: 0.845
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.842
    std: 0.005
    paper_value: 0.842
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.842
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.839
    std: 0.006
    paper_value: 0.839
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.8086
    std: 0.0056
    metric: ROC-AUC
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
    global_rank: 11
    sort_value: 0.8086
    sort_std: 0.0056
    is_best: false
  - model: EGT_Larger (30 layers) (pre-trained)
    model_key: egt_larger (30 layers) (pre-trained)
    model_plain: EGT_Larger (30 layers) (pre-trained)
    value: 0.806
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 110.8
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: true
    is_global_top: true
    global_rank: 12
    sort_value: 0.806
    sort_std: 0.0065
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id023
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    metric: AP
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
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.232
    std: 0.001
    paper_value: 0.232
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.3139
    true_std: 0.0032
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0819
    value_note: ''
    paper_rank: 37
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.3139
    sort_std: 0.0032
    is_best: false
  - model: Graphormer-FLAG
    model_key: graphormer-flag
    model_plain: Graphormer-FLAG
    value: 0.3139
    std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_display: Jun 2021
    date_iso: 2021-06
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3139
    sort_std: 0.0032
    is_best: false
  - model: GSO
    model_key: gso
    model_plain: GSO
    value: 0.3031
    std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.3031
    sort_std: 0.0026
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.225
    std: 0.002
    paper_value: 0.225
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 18
    true_value: 0.2838
    true_std: 0.0035
    value_gap_source_arxiv: '2110.07875'
    value_gap_source_title: Graph Neural Networks with Learnable Structural and Positional
      Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05879999999999999
    value_note: ''
    paper_rank: 42
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.2838
    sort_std: 0.0035
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.221
    std: 0.001
    paper_value: 0.221
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 24
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04929999999999998
    value_note: ''
    paper_rank: 43
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.213
    std: 0.002
    paper_value: 0.213
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 32
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02940000000000001
    value_note: ''
    paper_rank: 43
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.241
    std: 0.001
    paper_value: 0.241
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 33
    true_value: 0.241
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.241
    sort_std: 0.001
    is_best: false
  - model: MolFormer
    model_key: molformer
    model_plain: MolFormer
    value: 0.235
    std: 0.002
    paper_value: 0.235
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 34
    true_value: 0.235
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.235
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.215
    std: 0.003
    paper_value: 0.215
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 40
    true_value: 0.228
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013000000000000012
    value_note: ''
    paper_rank: 43
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.228
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.218
    std: 0.002
    paper_value: 0.218
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 42
    true_value: 0.227
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009000000000000008
    value_note: ''
    paper_rank: 43
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.227
    sort_std: 0.001
    is_best: false
  metric: AP
  higher_is_better: true
- &id034
  dataset: ogbl-biokg
  rows:
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.418
    std: null
    paper_value: 0.418
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.8095
    true_std: 0.0007
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3915
    value_note: ''
    paper_rank: 8
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8095
    sort_std: 0.0007
    is_best: true
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.395
    std: null
    paper_value: 0.395
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.8043
    true_std: 0.0003
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4093
    value_note: ''
    paper_rank: 8
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8043
    sort_std: 0.0003
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.432
    std: null
    paper_value: 0.432
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.7989
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36690000000000006
    value_note: ''
    paper_rank: 8
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.7989
    sort_std: 0.0004
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.365
    std: null
    paper_value: 0.365
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.7452
    true_std: 0.0004
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3802
    value_note: ''
    paper_rank: 8
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7452
    sort_std: 0.0004
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.512
    std: 0.003
    paper_value: 0.512
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.512
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.003
    is_best: false
  - model: GAIN
    model_key: gain
    model_plain: GAIN
    value: 0.485
    std: null
    paper_value: 0.485
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.485
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.485
    sort_std: null
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.468
    std: null
    paper_value: 0.468
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Vashishth et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.468
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.468
    sort_std: null
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.451
    std: null
    paper_value: 0.451
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Schlichtkrull et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.451
    true_std: null
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.451
    sort_std: null
    is_best: false
  metric: MRR
  higher_is_better: true
- &id030
  dataset: ogbl-citation2
  rows:
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.765
    std: 0.003
    paper_value: 0.765
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.8474
    true_std: 0.0021
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08240000000000003
    value_note: ''
    paper_rank: 14
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8474
    sort_std: 0.0021
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: 0.002
    paper_value: 0.768
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.826
    true_std: 0.0036
    value_gap_source_arxiv: '2005.00687'
    value_gap_source_title: 'Open Graph Benchmark: Datasets for Machine Learning on
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05799999999999994
    value_note: ''
    paper_rank: 14
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.0036
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.812
    std: 0.001
    paper_value: 0.812
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.812
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.001
    is_best: false
  - model: OpenGNN
    model_key: opengnn
    model_plain: OpenGNN
    value: 0.805
    std: 0.001
    paper_value: 0.805
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.805
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.001
    is_best: false
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    value: 0.8044
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_display: May 2020
    date_iso: 2020-05
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8044
    sort_std: 0.001
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.801
    std: 0.002
    paper_value: 0.801
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.801
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.801
    sort_std: 0.002
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.8004
    std: 0.0025
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_display: May 2020
    date_iso: 2020-05
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.8004
    sort_std: 0.0025
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.7985
    std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_display: May 2020
    date_iso: 2020-05
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.7985
    sort_std: 0.004
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.795
    std: 0.002
    paper_value: 0.795
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.795
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.792
    std: 0.003
    paper_value: 0.792
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.792
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.003
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.788
    std: 0.002
    paper_value: 0.788
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 11
    true_value: 0.788
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.785
    std: 0.002
    paper_value: 0.785
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.785
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.772
    std: 0.004
    paper_value: 0.772
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.772
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.77
    std: 0.003
    paper_value: 0.77
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.77
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.003
    is_best: false
  metric: MRR
  higher_is_better: true
- &id033
  dataset: ogbl-collab
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.002
    paper_value: 0.785
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.785
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.768
    std: 0.003
    paper_value: 0.768
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.768
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.762
    std: 0.002
    paper_value: 0.762
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.762
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.758
    std: 0.003
    paper_value: 0.758
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.758
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.751
    std: 0.004
    paper_value: 0.751
    paper_std: 0.004
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.751
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.745
    std: 0.003
    paper_value: 0.745
    paper_std: 0.003
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.745
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.736
    std: 0.002
    paper_value: 0.736
    paper_std: 0.002
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.736
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.002
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.497
    std: 0.0059
    metric: Hits@50
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
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.497
    sort_std: 0.0059
    is_best: false
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.491
    std: 0.0057
    metric: Hits@50
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
    global_rank: 9
    sort_value: 0.491
    sort_std: 0.0057
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4819
    std: 0.0094
    metric: Hits@50
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
    global_rank: 10
    sort_value: 0.4819
    sort_std: 0.0094
    is_best: false
  metric: Hits@50
  higher_is_better: true
- &id035
  dataset: ogbl-ddi
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.784
    std: 0.002
    paper_value: 0.784
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.784
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.771
    std: 0.003
    paper_value: 0.771
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.771
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.765
    std: 0.002
    paper_value: 0.765
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.765
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.752
    std: 0.003
    paper_value: 0.752
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.752
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.748
    std: 0.004
    paper_value: 0.748
    paper_std: 0.004
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.748
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.748
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.741
    std: 0.002
    paper_value: 0.741
    paper_std: 0.002
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.741
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.735
    std: 0.003
    paper_value: 0.735
    paper_std: 0.003
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.735
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.003
    is_best: false
  - model: Node2Vec
    model_key: node2vec
    model_plain: Node2Vec
    value: 0.2326
    std: 0.0209
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_display: May 2020
    date_iso: 2020-05
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.2326
    sort_std: 0.0209
    is_best: false
  - model: MatrixFactorization
    model_key: matrixfactorization
    model_plain: MatrixFactorization
    value: 0.1368
    std: 0.0475
    metric: Hits@20
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_display: May 2020
    date_iso: 2020-05
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.1368
    sort_std: 0.0475
    is_best: false
  metric: Hits@20
  higher_is_better: true
- &id026
  dataset: ogbl-wikikg2
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.7983
    std: 0.0042
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7983
    sort_std: 0.0042
    is_best: true
  - model: TCL
    model_key: tcl
    model_plain: TCL
    value: 0.7811
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7811
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.746
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.746
    sort_std: 0.001
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.482
    std: 0.0
    paper_value: 0.482
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.728
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.246
    value_note: ''
    paper_rank: 31
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.728
    sort_std: 0.003
    is_best: false
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.451
    std: 0.0
    paper_value: 0.451
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Trouillon et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.725
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27399999999999997
    value_note: ''
    paper_rank: 31
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.725
    sort_std: 0.003
    is_best: false
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.438
    std: 0.0
    paper_value: 0.438
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2014
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.721
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.283
    value_note: ''
    paper_rank: 31
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.721
    sort_std: 0.003
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.365
    std: 0.0
    paper_value: 0.365
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bordes et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.685
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.32000000000000006
    value_note: ''
    paper_rank: 35
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.685
    sort_std: 0.004
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.495
    std: 0.0
    paper_value: 0.495
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Schlichtkrull et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.678
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18300000000000005
    value_note: ''
    paper_rank: 31
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.678
    sort_std: 0.004
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.501
    std: 0.0
    paper_value: 0.501
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Vashishth et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.675
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17400000000000004
    value_note: ''
    paper_rank: 31
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.675
    sort_std: 0.004
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.538
    std: 0.002
    paper_value: 0.538
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 26
    true_value: 0.538
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.002
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.524
    std: 0.0
    paper_value: 0.524
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 29
    true_value: 0.524
    true_std: 0.0
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.524
    sort_std: 0.0
    is_best: false
  - model: HGT
    model_key: hgt
    model_plain: HGT
    value: 0.512
    std: 0.0
    paper_value: 0.512
    paper_std: 0.0
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 31
    true_value: 0.512
    true_std: 0.0
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.0
    is_best: false
  metric: MRR
  higher_is_better: true
- &id024
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
    paper_value: 0.752
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.752
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.002
    is_best: true
  - model: Flan-T5-large
    model_key: flan-t5-large
    model_plain: Flan-T5-large
    value: 0.7467
    std: 0.0008
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
    global_rank: 4
    sort_value: 0.7467
    sort_std: 0.0008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
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
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.745
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.003
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.742
    std: 0.002
    paper_value: 0.742
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: JK-Net
    model_key: jk-net
    model_plain: JK-Net
    value: 0.74
    std: 0.003
    paper_value: 0.74
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.74
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.735
    std: 0.004
    paper_value: 0.735
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 14
    true_value: 0.7391
    true_std: 0.0012
    value_gap_source_arxiv: '2106.07476'
    value_gap_source_title: Training Graph Neural Networks with 1000 Layers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0040999999999999925
    value_note: ''
    paper_rank: 18
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7391
    sort_std: 0.0012
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.738
    std: 0.004
    paper_value: 0.738
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 15
    true_value: 0.738
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.731
    std: 0.003
    paper_value: 0.731
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 21
    true_value: 0.731
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.728
    std: 0.005
    paper_value: 0.728
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 26
    true_value: 0.728
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.005
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.725
    std: 0.006
    paper_value: 0.725
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 31
    true_value: 0.725
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id031
  dataset: ogbn-mag
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.781
    std: 0.003
    paper_value: 0.781
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.781
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: 0.003
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.775
    std: 0.002
    paper_value: 0.775
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.775
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.772
    std: 0.003
    paper_value: 0.772
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.772
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.768
    std: 0.004
    paper_value: 0.768
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.768
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.761
    std: 0.003
    paper_value: 0.761
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.761
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.759
    std: 0.002
    paper_value: 0.759
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.759
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.753
    std: 0.002
    paper_value: 0.753
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.753
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.742
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: AP-GNN
    model_key: ap-gnn
    model_plain: AP-GNN
    value: 0.731
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.731
    sort_std: 0.002
    is_best: false
  - model: HGT
    model_key: hgt
    model_plain: HGT
    value: 0.725
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.725
    sort_std: 0.002
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id032
  dataset: ogbn-papers100M
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.782
    std: 0.001
    paper_value: 0.782
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.782
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.001
    is_best: true
  - model: GraphSAINT + RWSE
    model_key: graphsaint + rwse
    model_plain: GraphSAINT + RWSE
    value: 0.775
    std: 0.002
    paper_value: 0.775
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.775
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: Neighbor Sampling (NS)
    model_key: neighbor sampling (ns)
    model_plain: Neighbor Sampling (NS)
    value: 0.773
    std: 0.001
    paper_value: 0.773
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.773
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.001
    is_best: false
  - model: LADIES
    model_key: ladies
    model_plain: LADIES
    value: 0.771
    std: 0.002
    paper_value: 0.771
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zeng et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.771
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.002
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.768
    std: 0.003
    paper_value: 0.768
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.768
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.765
    std: 0.002
    paper_value: 0.765
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 6
    true_value: 0.765
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.765
    sort_std: 0.002
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.762
    std: 0.004
    paper_value: 0.762
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.004
    is_best: false
  - model: FastGCN
    model_key: fastgcn
    model_plain: FastGCN
    value: 0.759
    std: 0.005
    paper_value: 0.759
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.759
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.005
    is_best: false
  - model: SIGN(3,3,3)
    model_key: sign(3,3,3)
    model_plain: SIGN(3,3,3)
    value: 0.6511
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.6511
    sort_std: 0.0014
    is_best: false
  - model: SIGN(3,1,1)
    model_key: sign(3,1,1)
    model_plain: SIGN(3,1,1)
    value: 0.6439
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.6439
    sort_std: 0.0018
    is_best: false
  - model: SIGN(3,0,0)
    model_key: sign(3,0,0)
    model_plain: SIGN(3,0,0)
    value: 0.6428
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.6428
    sort_std: 0.0014
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id028
  dataset: ogbn-products
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.835
    std: 0.001
    paper_value: 0.835
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 1
    true_value: 0.835
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.001
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.83
    std: 0.001
    paper_value: 0.83
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 2
    true_value: 0.83
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.001
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.827
    std: 0.001
    paper_value: 0.827
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 3
    true_value: 0.827
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8262
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8262
    sort_std: 0.0039
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.826
    std: 0.001
    paper_value: 0.826
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 5
    true_value: 0.826
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.001
    is_best: false
  - model: UniMP
    model_key: unimp
    model_plain: UniMP
    value: 0.8256
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.475605
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_display: Sep 2020
    date_iso: 2020-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8256
    sort_std: 0.0031
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.825
    std: 0.001
    paper_value: 0.825
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 7
    true_value: 0.825
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.824
    std: 0.001
    paper_value: 0.824
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.824
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.823
    std: 0.001
    paper_value: 0.823
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.823
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.001
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.822
    std: 0.001
    paper_value: 0.822
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.822
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.001
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.82
    std: 0.0043
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
    global_rank: 11
    sort_value: 0.82
    sort_std: 0.0043
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id029
  dataset: ogbn-proteins
  rows:
  - model: RevGNN-Wide
    model_key: revgnn-wide
    model_plain: RevGNN-Wide
    value: 0.8824
    std: 0.0015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8824
    sort_std: 0.0015
    is_best: true
  - model: RevGNN-Deep
    model_key: revgnn-deep
    model_plain: RevGNN-Deep
    value: 0.8774
    std: 0.0013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8774
    sort_std: 0.0013
    is_best: false
  - model: UniMP+CEF
    model_key: unimp+cef
    model_plain: UniMP+CEF
    value: 0.8691
    std: 0.0018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.96
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_display: Jun 2021
    date_iso: '2021-06-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8691
    sort_std: 0.0018
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.821
    std: 0.002
    paper_value: 0.821
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 4
    true_value: 0.8682
    true_std: 0.0021
    value_gap_source_arxiv: '2106.07476'
    value_gap_source_title: Training Graph Neural Networks with 1000 Layers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_note: ''
    paper_rank: 11
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8682
    sort_std: 0.0021
    is_best: false
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.841
    std: 0.002
    paper_value: 0.841
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 8
    true_value: 0.841
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.002
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.835
    std: 0.001
    paper_value: 0.835
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 9
    true_value: 0.835
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.832
    std: 0.002
    paper_value: 0.832
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 10
    true_value: 0.832
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.832
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.824
    std: 0.003
    paper_value: 0.824
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 11
    true_value: 0.824
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: 0.003
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.818
    std: 0.004
    paper_value: 0.818
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
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 12
    true_value: 0.818
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.818
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.003
    paper_value: 0.815
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    global_rank: 13
    true_value: 0.815
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.815
    sort_std: 0.003
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
  - *id009
  - *id010
  - *id011
  - *id012
- benchmark: TU Dortmund
  datasets:
  - *id013
  - *id014
  - *id015
  - *id016
  - *id017
  - *id018
  - *id019
  - *id020
  - *id021
  - *id022
- benchmark: OGB
  datasets:
  - *id023
  - *id024
  - *id025
  - *id026
  - *id027
  - *id028
  - *id029
  - *id030
  - *id031
  - *id032
  - *id033
  - *id034
  - *id035
- benchmark: Quantum Chemistry
  datasets:
  - *id036
single_proposed_model: ILLS
main_figure: /figures/2305.17589/main_figure.png
---

