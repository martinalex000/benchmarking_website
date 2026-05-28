---
title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
arxiv_id: '2509.22100'
source_url: ''
authors: []
published_date: Sep 2025
published_date_iso: 2025-09
abstract: Graph Neural Networks (GNNs) have achieved remarkable success across a range
  of learning tasks. However, scaling GNNs to large graphs remains a significant challenge,
  especially for graph-level tasks. In this work, we introduce SHAKE-GNN, a novel
  scalable graph-level GNN framework based on a hierarchy of Kirchhoff Forests, a
  class of random spanning forests used to construct stochastic multi-resolution decompositions
  of graphs. SHAKE-GNN produces multi-scale representations, enabling flexible trade-offs
  between efficiency and performance. We introduce an improved, data-driven strategy
  for selecting the trade-off parameter and analyse the time-complexity of SHAKE-GNN.
  Experimental results on multiple large-scale graph classification benchmarks demonstrate
  that SHAKE-GNN achieves competitive performance while offering improved scalability.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Coarsened Graph
- S² GCN
- GCNs (Coarsened)
mrr: 0.0391
adjusted_mrr: 0.0391
mrr_dataset_count: 3
benchmark_categories:
- Classic
- TU Dortmund
- OGB
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id002
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
  - model: Original Graph
    model_key: original graph
    model_plain: Original Graph
    value: 0.752
    std: null
    paper_value: 0.752
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 35
    true_value: 0.752
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: null
    is_best: false
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.752
    std: null
    paper_value: 0.752
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 36
    true_value: 0.752
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: null
    is_best: false
  - model: Coarsened Graph
    model_key: coarsened graph
    model_plain: Coarsened Graph
    value: 0.739
    std: null
    paper_value: 0.739
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 45
    true_value: 0.739
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: REDDIT-MULTI-5K
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.606
    std: 0.003
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
    sort_value: 0.606
    sort_std: 0.003
    is_best: true
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
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
    global_rank: 2
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.569
    std: 0.02
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
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: Original Graph
    model_key: original graph
    model_plain: Original Graph
    value: 0.492
    std: null
    paper_value: 0.492
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 13
    true_value: 0.492
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.492
    sort_std: null
    is_best: false
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.492
    std: null
    paper_value: 0.492
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 14
    true_value: 0.492
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.492
    sort_std: null
    is_best: false
  - model: Coarsened Graph
    model_key: coarsened graph
    model_plain: Coarsened Graph
    value: 0.481
    std: null
    paper_value: 0.481
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 15
    true_value: 0.481
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.481
    sort_std: null
    is_best: false
  - model: GCNs (Coarsened)
    model_key: gcns (coarsened)
    model_plain: GCNs (Coarsened)
    value: 0.481
    std: null
    paper_value: 0.481
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 16
    true_value: 0.481
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.481
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: true
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  - model: Original Graph
    model_key: original graph
    model_plain: Original Graph
    value: 0.749
    std: null
    paper_value: 0.749
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.749
    sort_std: null
    is_best: false
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.749
    std: null
    paper_value: 0.749
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit (score=90)'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.749
    sort_std: null
    is_best: false
  - model: Coarsened Graph
    model_key: coarsened graph
    model_plain: Coarsened Graph
    value: 0.74
    std: null
    paper_value: 0.74
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.74
    sort_std: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id004
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9681
    std: 0.0003
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: Original Graph
    model_key: original graph
    model_plain: Original Graph
    value: 0.794
    std: null
    paper_value: 0.794
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 54
    true_value: 0.794
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: null
    is_best: false
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.794
    std: null
    paper_value: 0.794
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 55
    true_value: 0.794
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: null
    is_best: false
  - model: Coarsened Graph
    model_key: coarsened graph
    model_plain: Coarsened Graph
    value: 0.787
    std: null
    paper_value: 0.787
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 83
    true_value: 0.787
    true_std: null
    value_gap_source_arxiv: '2509.22100'
    value_gap_source_title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph
      Neural Network'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.787
    sort_std: null
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
  dataset: ogbg-molpcba
  rows:
  - model: Original Graph
    model_key: original graph
    model_plain: Original Graph
    value: 0.767
    std: null
    paper_value: 0.767
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.767
    sort_std: null
    is_best: true
  - model: S² GCN
    model_key: s² gcn
    model_plain: S² GCN
    value: 0.767
    std: null
    paper_value: 0.767
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=87)'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.767
    sort_std: null
    is_best: true
  - model: Coarsened Graph
    model_key: coarsened graph
    model_plain: Coarsened Graph
    value: 0.744
    std: null
    paper_value: 0.744
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: null
    sort_value: 0.744
    sort_std: null
    is_best: false
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
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
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
  - *id003
- benchmark: OGB
  datasets:
  - *id004
  - *id005
main_figure: /figures/2509.22100/main_figure.png
---

