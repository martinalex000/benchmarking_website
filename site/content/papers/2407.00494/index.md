---
title: Graph Neural Networks Gone Hogwild
arxiv_id: '2407.00494'
source_url: ''
authors: []
published_date: Jul 2024
published_date_iso: 2024-07
abstract: Graph neural networks (GNNs) appear to be powerful tools to learn state
  representations for agents in distributed, decentralized multi-agent systems, but
  generate catastrophically incorrect predictions when nodes update asynchronously
  during inference. This failure under asynchrony effectively excludes these architectures
  from many potential applications where synchrony is difficult or impossible to enforce,
  e.g., robotic swarms or sensor networks. In this work we identify ``implicitly-defined''
  GNNs as a class of architectures which is provably robust to asynchronous ``hogwild''
  inference, adapting convergence guarantees from work in asynchronous and distributed
  optimization. We then propose a novel implicitly-defined GNN architecture, which
  we call an energy GNN. We show that this architecture outperforms other GNNs from
  this class on a variety of synthetic tasks inspired by multi-agent systems.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Energy GNN (edge-wise)
- Energy GNN + attention
mrr: 0.0107
adjusted_mrr: 0.0107
mrr_dataset_count: 3
benchmark_categories:
- Classic
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
- &id005
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
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
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
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
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.98
    std: 0.034
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
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: GCN* (5 layer, embedding dimension=64)
    model_key: gcn* (5 layer, embedding dimension=64)
    model_plain: GCN* (5 layer, embedding dimension=64)
    value: 0.894
    std: 0.056
    paper_value: 0.894
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gin
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 30
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: IGNN* (3 layer, embedding dimension=32)
    model_key: ignn* (3 layer, embedding dimension=32)
    model_plain: IGNN* (3 layer, embedding dimension=32)
    value: 0.893
    std: 0.067
    paper_value: 0.893
    paper_std: 0.067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ignn
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 32
    true_value: 0.893
    true_std: 0.067
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.893
    sort_std: 0.067
    is_best: true
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.876
    std: 0.034
    paper_value: 0.876
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 46
    true_value: 0.876
    true_std: 0.034
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.876
    sort_std: 0.034
    is_best: false
  - model: Energy GNN + attention
    model_key: energy gnn + attention
    model_plain: Energy GNN + attention
    value: 0.795
    std: 0.018
    paper_value: 0.795
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 108
    true_value: 0.795
    true_std: 0.018
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.018
    is_best: false
  - model: GSD GNN
    model_key: gsd gnn
    model_plain: GSD GNN
    value: 0.784
    std: 0.022
    paper_value: 0.784
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 119
    true_value: 0.784
    true_std: 0.022
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.022
    is_best: false
  - model: GCN (5 layer)
    model_key: gcn (5 layer)
    model_plain: GCN (5 layer)
    value: 0.78
    std: 0.014
    paper_value: 0.78
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 121
    true_value: 0.78
    true_std: 0.014
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.014
    is_best: false
  - model: GAT (5 layer)
    model_key: gat (5 layer)
    model_plain: GAT (5 layer)
    value: 0.761
    std: 0.015
    paper_value: 0.761
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 131
    true_value: 0.761
    true_std: 0.015
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.015
    is_best: false
  - model: IGNN (1 layer)
    model_key: ignn (1 layer)
    model_plain: IGNN (1 layer)
    value: 0.73
    std: 0.006
    paper_value: 0.73
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 147
    true_value: 0.73
    true_std: 0.006
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PPI
  rows:
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.989
    std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.989
    sort_std: 0.0012
    is_best: true
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.982
    std: 0.0025
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.982
    sort_std: 0.0025
    is_best: false
  - model: IGNN*
    model_key: ignn*
    model_plain: IGNN*
    value: 0.976
    std: null
    paper_value: 0.976
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: IGNN
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 3
    true_value: 0.976
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.973
    std: null
    paper_value: 0.973
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 4
    true_value: 0.973
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.973
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: null
    paper_value: 0.768
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 5
    true_value: 0.768
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
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
    sort_std: null
    is_best: false
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.762
    std: null
    paper_value: 0.762
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.762
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: null
    is_best: false
  - model: GCN (5 layer)
    model_key: gcn (5 layer)
    model_plain: GCN (5 layer)
    value: 0.762
    std: null
    paper_value: 0.762
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 7
    true_value: 0.762
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
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
    sort_std: null
    is_best: false
  - model: Energy GNN + attention
    model_key: energy gnn + attention
    model_plain: Energy GNN + attention
    value: 0.76
    std: null
    paper_value: 0.76
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 8
    true_value: 0.76
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: null
    is_best: false
  - model: GSD GNN
    model_key: gsd gnn
    model_plain: GSD GNN
    value: 0.76
    std: null
    paper_value: 0.76
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 9
    true_value: 0.76
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: null
    is_best: false
  - model: IGNN (1 layer)
    model_key: ignn (1 layer)
    model_plain: IGNN (1 layer)
    value: 0.755
    std: null
    paper_value: 0.755
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 10
    true_value: 0.755
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: null
    is_best: false
  - model: GAT (5 layer)
    model_key: gat (5 layer)
    model_plain: GAT (5 layer)
    value: 0.743
    std: null
    paper_value: 0.743
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 11
    true_value: 0.743
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.592
    std: null
    paper_value: 0.592
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: IGNN
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 12
    true_value: 0.592
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.592
    sort_std: null
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.462
    std: null
    paper_value: 0.462
    paper_std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: IGNN
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 13
    true_value: 0.462
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.462
    sort_std: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id004
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
  - model: IGNN* (3 layer, embedding dimension=32)
    model_key: ignn* (3 layer, embedding dimension=32)
    model_plain: IGNN* (3 layer, embedding dimension=32)
    value: 0.777
    std: 0.034
    paper_value: 0.777
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: IGNN
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 13
    true_value: 0.777
    true_std: 0.034
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.777
    sort_std: 0.034
    is_best: true
  - model: GCN* (5 layer, embedding dimension=64)
    model_key: gcn* (5 layer, embedding dimension=64)
    model_plain: GCN* (5 layer, embedding dimension=64)
    value: 0.762
    std: 0.019
    paper_value: 0.762
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GIN
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.762
    true_std: 0.019
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.019
    is_best: false
  - model: GCN (5 layer)
    model_key: gcn (5 layer)
    model_plain: GCN (5 layer)
    value: 0.737
    std: 0.005
    paper_value: 0.737
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 103
    true_value: 0.737
    true_std: 0.005
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.005
    is_best: false
  - model: GSD GNN
    model_key: gsd gnn
    model_plain: GSD GNN
    value: 0.728
    std: 0.008
    paper_value: 0.728
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 127
    true_value: 0.728
    true_std: 0.008
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.008
    is_best: false
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.725
    std: 0.003
    paper_value: 0.725
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 135
    true_value: 0.725
    true_std: 0.003
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.003
    is_best: false
  - model: Energy GNN + attention
    model_key: energy gnn + attention
    model_plain: Energy GNN + attention
    value: 0.725
    std: 0.005
    paper_value: 0.725
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 136
    true_value: 0.725
    true_std: 0.005
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.005
    is_best: false
  - model: IGNN (1 layer)
    model_key: ignn (1 layer)
    model_plain: IGNN (1 layer)
    value: 0.718
    std: 0.013
    paper_value: 0.718
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 150
    true_value: 0.718
    true_std: 0.013
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.013
    is_best: false
  - model: GAT (5 layer)
    model_key: gat (5 layer)
    model_plain: GAT (5 layer)
    value: 0.717
    std: 0.032
    paper_value: 0.717
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 154
    true_value: 0.717
    true_std: 0.032
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.032
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: Energy GNN + attention
    model_key: energy gnn + attention
    model_plain: Energy GNN + attention
    value: 0.381
    std: null
    paper_value: 0.381
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 312
    true_value: 0.381
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 312
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.381
    sort_std: null
    is_best: false
  - model: GCN (5 layer)
    model_key: gcn (5 layer)
    model_plain: GCN (5 layer)
    value: 0.362
    std: null
    paper_value: 0.362
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 315
    true_value: 0.362
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 315
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.362
    sort_std: null
    is_best: false
  - model: GAT (5 layer)
    model_key: gat (5 layer)
    model_plain: GAT (5 layer)
    value: 0.355
    std: null
    paper_value: 0.355
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 316
    true_value: 0.355
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 316
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.355
    sort_std: null
    is_best: false
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.348
    std: null
    paper_value: 0.348
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 317
    true_value: 0.348
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 317
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.348
    sort_std: null
    is_best: false
  - model: GSD GNN
    model_key: gsd gnn
    model_plain: GSD GNN
    value: 0.343
    std: null
    paper_value: 0.343
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 318
    true_value: 0.343
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 318
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.343
    sort_std: null
    is_best: false
  - model: IGNN (1 layer)
    model_key: ignn (1 layer)
    model_plain: IGNN (1 layer)
    value: 0.211
    std: null
    paper_value: 0.211
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 324
    true_value: 0.211
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 324
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.211
    sort_std: null
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
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
  - model: GAT (5 layer)
    model_key: gat (5 layer)
    model_plain: GAT (5 layer)
    value: 0.335
    std: null
    paper_value: 0.335
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 289
    true_value: 0.335
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 289
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: null
    is_best: false
  - model: GCN (5 layer)
    model_key: gcn (5 layer)
    model_plain: GCN (5 layer)
    value: 0.366
    std: null
    paper_value: 0.366
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 323
    true_value: 0.366
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 323
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.366
    sort_std: null
    is_best: false
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.367
    std: null
    paper_value: 0.367
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 324
    true_value: 0.367
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 324
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.367
    sort_std: null
    is_best: false
  - model: GSD GNN
    model_key: gsd gnn
    model_plain: GSD GNN
    value: 0.375
    std: null
    paper_value: 0.375
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 326
    true_value: 0.375
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 326
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.375
    sort_std: null
    is_best: false
  - model: Energy GNN + attention
    model_key: energy gnn + attention
    model_plain: Energy GNN + attention
    value: 0.402
    std: null
    paper_value: 0.402
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 332
    true_value: 0.402
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 332
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.402
    sort_std: null
    is_best: false
  - model: IGNN (1 layer)
    model_key: ignn (1 layer)
    model_plain: IGNN (1 layer)
    value: 0.426
    std: null
    paper_value: 0.426
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 333
    true_value: 0.426
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 333
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.426
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
  - *id005
main_figure: /figures/2407.00494/main_figure.png
---

