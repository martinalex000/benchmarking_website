---
title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
  Graph
arxiv_id: '2409.11504'
source_url: ''
authors: []
published_date: Sep 2024
published_date_iso: 2024-09
abstract: The ability of message-passing neural networks (MPNNs) to fit complex functions
  over graphs is limited as most graph convolutions amplify the same signal across
  all feature channels, a phenomenon known as rank collapse, and over-smoothing as
  a special case. Most approaches to mitigate over-smoothing extend common message-passing
  schemes, e.g., the graph convolutional network, by utilizing residual connections,
  gating mechanisms, normalization, or regularization techniques. Our work contrarily
  proposes to directly tackle the cause of this issue by modifying the message-passing
  scheme and exchanging different types of messages using multi-relational graphs.
  We identify a sufficient condition to ensure linearly independent node representations.
  As one instantion, we show that operating on multiple directed acyclic graphs always
  satisfies our condition and propose to obtain these by defining a strict partial
  ordering of the nodes. We conduct comprehensive experiments that confirm the benefits
  of operating on multi-relational graphs to achieve more informative node representations.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- MRS-GCN_DA (random)
- MRS-GCN_DA (Features)
- MRS-GCN_DA (PPR)
- MRS-GCN_DA (Degree)
- MRS-GCN_DA
- MRS-SAGE_DA
- MRS-GAT_DA
- MRS-GatedGCN_DA
- MRS-Dir-GCN_DA
mrr: 0.0035
adjusted_mrr: 0.0012
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- LINKX Benchmarks
task_categories:
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
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
    paper_value: 0.8017
    paper_std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 2
    true_value: 0.8017
    true_std: 0.0188
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7971
    std: 0.0126
    paper_value: 0.7971
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.7971
    true_std: 0.0126
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7971
    sort_std: 0.0126
    is_best: true
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.7888
    std: 0.0104
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
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    sort_value: 0.7888
    sort_std: 0.0104
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7827
    std: 0.0128
    paper_value: 0.7827
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.7827
    true_std: 0.0128
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7827
    sort_std: 0.0128
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.7476
    std: 0.022
    paper_value: 0.7476
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 10
    true_value: 0.7523
    true_std: 0.0172
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0046999999999999265
    value_note: global 0.7523 within std
    paper_rank: 12
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.7523
    sort_std: 0.0172
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.714
    std: 0.0238
    paper_value: 0.714
    paper_std: 0.0238
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.714
    true_std: 0.0238
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.0238
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.7121
    std: 0.0184
    paper_value: 0.7121
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.7121
    true_std: 0.0184
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7121
    sort_std: 0.0184
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6842
    std: 0.0138
    paper_value: 0.6842
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 25
    true_value: 0.6842
    true_std: 0.0138
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6842
    sort_std: 0.0138
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6482
    std: 0.0224
    paper_value: 0.6482
    paper_std: 0.0224
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 43
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.6285
    std: 0.029
    paper_value: 0.6285
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 48
    true_value: 0.6285
    true_std: 0.029
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6285
    sort_std: 0.029
    is_best: false
  - model: H_2GCN
    model_key: h_2gcn
    model_plain: H_2GCN
    value: 0.5939
    std: 0.0198
    paper_value: 0.5939
    paper_std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 67
    true_value: 0.5939
    true_std: 0.0198
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5939
    sort_std: 0.0198
    is_best: false
  - model: MagNet
    model_key: magnet
    model_plain: MagNet
    value: 0.5822
    std: 0.0287
    paper_value: 0.5822
    paper_std: 0.0287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 73
    true_value: 0.5822
    true_std: 0.0287
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5822
    sort_std: 0.0287
    is_best: false
  - model: DiGCN
    model_key: digcn
    model_plain: DiGCN
    value: 0.5224
    std: 0.0365
    paper_value: 0.5224
    paper_std: 0.0365
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 89
    true_value: 0.5224
    true_std: 0.0365
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5224
    sort_std: 0.0365
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.4621
    std: 0.0299
    paper_value: 0.4621
    paper_std: 0.0299
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 102
    true_value: 0.4636
    true_std: 0.0252
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015000000000000013
    value_note: global 0.4636 within std
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4636
    sort_std: 0.0252
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.9187
    std: 0.0042
    paper_value: 0.9187
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 11
    true_value: 0.9187
    true_std: 0.0042
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9187
    sort_std: 0.0042
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
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
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.9123
    std: 0.0032
    paper_value: 0.9123
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 21
    true_value: 0.9123
    true_std: 0.0032
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9123
    sort_std: 0.0032
    is_best: false
  - model: MagNet
    model_key: magnet
    model_plain: MagNet
    value: 0.8807
    std: 0.0027
    paper_value: 0.8807
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 35
    true_value: 0.8807
    true_std: 0.0027
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8807
    sort_std: 0.0027
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.8216
    std: 0.0078
    paper_value: 0.8216
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 66
    true_value: 0.8216
    true_std: 0.0078
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8216
    sort_std: 0.0078
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
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
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.6966
    std: 0.0062
    paper_value: 0.6966
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 83
    true_value: 0.6966
    true_std: 0.0062
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6966
    sort_std: 0.0062
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6494
    std: 0.0062
    paper_value: 0.6494
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 84
    true_value: 0.6619
    true_std: 0.0017
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012500000000000067
    value_note: ''
    paper_rank: 86
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.6619
    sort_std: 0.0017
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 87
    true_value: 0.6485
    true_std: 0.0027
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6485
    sort_std: 0.0027
    is_best: false
  - model: H_2GCN
    model_key: h_2gcn
    model_plain: H_2GCN
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 91
    true_value: 0.6011
    true_std: 0.0052
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6011
    sort_std: 0.0052
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
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
  - model: DiGCN
    model_key: digcn
    model_plain: DiGCN
    value: 0.5271
    std: 0.0032
    paper_value: 0.5271
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 95
    true_value: 0.5271
    true_std: 0.0032
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5271
    sort_std: 0.0032
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.3755
    std: 0.0036
    paper_value: 0.3755
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 103
    true_value: 0.3755
    true_std: 0.0036
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3755
    sort_std: 0.0036
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    paper_value: 0.7601
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 1
    true_value: 0.7601
    true_std: 0.019
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7601
    sort_std: 0.019
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7531
    std: 0.0192
    paper_value: 0.7531
    paper_std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 2
    true_value: 0.7531
    true_std: 0.0192
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7531
    sort_std: 0.0192
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.741
    std: 0.0189
    paper_value: 0.741
    paper_std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 3
    true_value: 0.741
    true_std: 0.0189
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7205
    std: 0.014
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
    global_rank: 4
    sort_value: 0.7205
    sort_std: 0.014
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.7191
    std: 0.0103
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
    global_rank: 5
    sort_value: 0.7191
    sort_std: 0.0103
    is_best: false
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.6998
    std: 0.0153
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
    global_rank: 6
    sort_value: 0.6998
    sort_std: 0.0153
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.674
    std: 0.0221
    paper_value: 0.674
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 8
    true_value: 0.6856
    true_std: 0.0133
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011599999999999944
    value_note: global 0.6856 within std
    paper_rank: 9
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6856
    sort_std: 0.0133
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.6426
    std: 0.0238
    paper_value: 0.6426
    paper_std: 0.0238
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 14
    true_value: 0.6426
    true_std: 0.0238
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6426
    sort_std: 0.0238
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6181
    std: 0.018
    paper_value: 0.6181
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 17
    true_value: 0.6181
    true_std: 0.018
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6181
    sort_std: 0.018
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.5788
    std: 0.0176
    paper_value: 0.5788
    paper_std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.5788
    true_std: 0.0176
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5788
    sort_std: 0.0176
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.5435
    std: 0.0087
    paper_value: 0.5435
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 24
    true_value: 0.5435
    true_std: 0.0087
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5435
    sort_std: 0.0087
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5343
    std: 0.0201
    paper_value: 0.5343
    paper_std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 26
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: MagNet
    model_key: magnet
    model_plain: MagNet
    value: 0.3901
    std: 0.0193
    paper_value: 0.3901
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 75
    true_value: 0.3901
    true_std: 0.0193
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3901
    sort_std: 0.0193
    is_best: false
  - model: H_2GCN
    model_key: h_2gcn
    model_plain: H_2GCN
    value: 0.379
    std: 0.0202
    paper_value: 0.379
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 82
    true_value: 0.379
    true_std: 0.0202
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.0202
    is_best: false
  - model: DiGCN
    model_key: digcn
    model_plain: DiGCN
    value: 0.3774
    std: 0.0154
    paper_value: 0.3774
    paper_std: 0.0154
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 86
    true_value: 0.3774
    true_std: 0.0154
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3774
    sort_std: 0.0154
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.2877
    std: 0.0156
    paper_value: 0.2877
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 90
    true_value: 0.366
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07829999999999998
    value_note: ''
    paper_rank: 101
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.366
    sort_std: 0.018000000000000002
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.123
    std: 0.004
    paper_value: 0.123
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057999999999999996
    value_note: ''
    paper_rank: 199
    rank_delta: 126
    rank_delta_abs: 126
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.155
    std: 0.003
    paper_value: 0.155
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 126
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.079
    value_note: ''
    paper_rank: 223
    rank_delta: 97
    rank_delta_abs: 97
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.099
    std: 0.011
    paper_value: 0.099
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 127
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022000000000000006
    value_note: ''
    paper_rank: 174
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.149
    std: 0.001
    paper_value: 0.149
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 135
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07136451037695209
    value_note: ''
    paper_rank: 218
    rank_delta: 83
    rank_delta_abs: 83
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: MRS-GatedGCN_DA
    model_key: mrs-gatedgcn_da
    model_plain: MRS-GatedGCN_DA
    value: 0.088
    std: 0.004
    paper_value: 0.088
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 161
    true_value: 0.088
    true_std: 0.004
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.088
    sort_std: 0.004
    is_best: false
  - model: MRS-GCN_DA
    model_key: mrs-gcn_da
    model_plain: MRS-GCN_DA
    value: 0.106
    std: 0.004
    paper_value: 0.106
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 181
    true_value: 0.106
    true_std: 0.004
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.106
    sort_std: 0.004
    is_best: false
  - model: MRS-SAGE_DA
    model_key: mrs-sage_da
    model_plain: MRS-SAGE_DA
    value: 0.106
    std: 0.002
    paper_value: 0.106
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 182
    true_value: 0.106
    true_std: 0.002
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.106
    sort_std: 0.002
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.123
    std: 0.002
    paper_value: 0.123
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 200
    true_value: 0.123
    true_std: 0.002
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.123
    sort_std: 0.002
    is_best: false
  - model: MRS-GAT_DA
    model_key: mrs-gat_da
    model_plain: MRS-GAT_DA
    value: 0.128
    std: 0.0
    paper_value: 0.128
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    variant_inference_reason: 'zinc: entry cue matched full'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 204
    true_value: 0.128
    true_std: 0.0
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.128
    sort_std: 0.0
    is_best: false
  - model: MRS-GCN_DA (Degree)
    model_key: mrs-gcn_da (degree)
    model_plain: MRS-GCN_DA (Degree)
    value: 0.318
    std: 0.031
    paper_value: 0.318
    paper_std: 0.031
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 262
    true_value: 0.318
    true_std: 0.031
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.031
    is_best: false
  - model: MRS-GCN_DA (PPR)
    model_key: mrs-gcn_da (ppr)
    model_plain: MRS-GCN_DA (PPR)
    value: 0.358
    std: 0.006
    paper_value: 0.358
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 268
    true_value: 0.358
    true_std: 0.006
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 268
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.358
    sort_std: 0.006
    is_best: false
  - model: MRS-GCN_DA (Features)
    model_key: mrs-gcn_da (features)
    model_plain: MRS-GCN_DA (Features)
    value: 0.39
    std: 0.004
    paper_value: 0.39
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 274
    true_value: 0.39
    true_std: 0.004
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 274
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.004
    is_best: false
  - model: MRS-GCN_DA (random)
    model_key: mrs-gcn_da (random)
    model_plain: MRS-GCN_DA (random)
    value: 0.623
    std: 0.003
    paper_value: 0.623
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 286
    true_value: 0.623
    true_std: 0.003
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.623
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: arxiv-year
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.6603
    std: 0.002
    paper_value: 0.6603
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 1
    true_value: 0.6603
    true_std: 0.002
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6603
    sort_std: 0.002
    is_best: true
  - model: S² DirGCN
    model_key: s² dirgcn
    model_plain: S² DirGCN
    value: 0.6495
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.6495
    sort_std: 0.0033
    is_best: false
  - model: FaberNet
    model_key: fabernet
    model_plain: FaberNet
    value: 0.6462
    std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6462
    sort_std: 0.0101
    is_best: false
  - model: DirGCN (tuned)
    model_key: dirgcn (tuned)
    model_plain: DirGCN (tuned)
    value: 0.6444
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.6444
    sort_std: 0.0027
    is_best: false
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.6408
    std: 0.003
    paper_value: 0.6408
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.6408
    true_std: 0.003
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6408
    sort_std: 0.003
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.633
    std: 0.0184
    paper_value: 0.633
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 7
    true_value: 0.633
    true_std: 0.0184
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.633
    sort_std: 0.0184
    is_best: false
  - model: MagNet
    model_key: magnet
    model_plain: MagNet
    value: 0.6029
    std: 0.0027
    paper_value: 0.6029
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 8
    true_value: 0.6029
    true_std: 0.0027
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6029
    sort_std: 0.0027
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.56
    std: 0.0017
    paper_value: 0.56
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 10
    true_value: 0.56
    true_std: 0.0134
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.0134
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.5479
    std: 0.0025
    paper_value: 0.5479
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 11
    true_value: 0.5479
    true_std: 0.0025
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5479
    sort_std: 0.0025
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.5047
    std: 0.0021
    paper_value: 0.5047
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 15
    true_value: 0.5047
    true_std: 0.0021
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5047
    sort_std: 0.0021
    is_best: false
  - model: H_2GCN
    model_key: h_2gcn
    model_plain: H_2GCN
    value: 0.4909
    std: 0.001
    paper_value: 0.4909
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.4909
    true_std: 0.001
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4909
    sort_std: 0.001
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.4737
    std: 0.0059
    paper_value: 0.4737
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.4737
    true_std: 0.0059
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4737
    sort_std: 0.0059
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4602
    std: 0.0026
    paper_value: 0.4602
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 22
    true_value: 0.4602
    true_std: 0.0026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4602
    sort_std: 0.0026
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.4507
    std: 0.0021
    paper_value: 0.4507
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 23
    true_value: 0.4507
    true_std: 0.0021
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4507
    sort_std: 0.0021
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.367
    std: 0.0021
    paper_value: 0.367
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 34
    true_value: 0.367
    true_std: 0.0021
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.367
    sort_std: 0.0021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: snap-patents
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7472
    std: 0.0005
    paper_value: 0.7472
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 1
    true_value: 0.7472
    true_std: 0.0005
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7472
    sort_std: 0.0005
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7395
    std: 0.0005
    paper_value: 0.7395
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 2
    true_value: 0.7395
    true_std: 0.0005
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7395
    sort_std: 0.0005
    is_best: false
  - model: LargeGT-full
    model_key: largegt-full
    model_plain: LargeGT-full
    value: 0.7021
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7021
    sort_std: 0.0012
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.695
    std: 0.0039
    paper_value: 0.695
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.695
    true_std: 0.0039
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.0039
    is_best: false
  - model: LargeGT-local
    model_key: largegt-local
    model_plain: LargeGT-local
    value: 0.6819
    std: 0.0311
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.6819
    sort_std: 0.0311
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.6507
    std: 0.0003
    paper_value: 0.6507
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.6507
    true_std: 0.0003
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6507
    sort_std: 0.0003
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.6209
    std: 0.0027
    paper_value: 0.6209
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 7
    true_value: 0.6209
    true_std: 0.0027
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6209
    sort_std: 0.0027
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6195
    std: 0.0012
    paper_value: 0.6195
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 8
    true_value: 0.6195
    true_std: 0.0012
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6195
    sort_std: 0.0012
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.6011
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.6011
    sort_std: 0.0005
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.5514
    std: 0.0016
    paper_value: 0.5514
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 10
    true_value: 0.5514
    true_std: 0.0016
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5514
    sort_std: 0.0016
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5102
    std: 0.0006
    paper_value: 0.5102
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 11
    true_value: 0.5102
    true_std: 0.0006
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5102
    sort_std: 0.0006
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.4019
    std: 0.0003
    paper_value: 0.4019
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.4019
    true_std: 0.0003
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4019
    sort_std: 0.0003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.3134
    std: 0.0005
    paper_value: 0.3134
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 22
    true_value: 0.3134
    true_std: 0.0005
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3134
    sort_std: 0.0005
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
- benchmark: LINKX Benchmarks
  datasets:
  - *id005
  - *id006
main_figure: /figures/2409.11504/main_figure.png
---

