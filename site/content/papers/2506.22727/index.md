---
title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
  Passing
arxiv_id: '2506.22727'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
abstract: Differential privacy (DP) has been integrated into graph neural networks
  (GNNs) to protect sensitive structural information, e.g., edges, nodes, and associated
  features across various applications. A prominent approach is to perturb the message-passing
  process, which forms the core of most GNN architectures. However, existing methods
  typically incur a privacy cost that grows linearly with the number of layers (e.g.,
  GAP published in Usenix Security'23), ultimately requiring excessive noise to maintain
  a reasonable privacy level. This limitation becomes particularly problematic when
  multi-layer GNNs, which have shown better performance than one-layer GNN, are used
  to process graph data with sensitive information. In this paper, we theoretically
  establish that the privacy budget converges with respect to the number of layers
  by applying privacy amplification techniques to the message-passing process, exploiting
  the contractive properties inherent to standard GNN operations. Motivated by this
  analysis, we propose a simple yet effective Contractive Graph Layer (CGL) that ensures
  the contractiveness required for theoretical guarantees while preserving model utility.
  Our framework, $ $, supports both training and inference, equipped with a contractive
  aggregation module, a privacy allocation module, and a privacy auditing module.
  Experimental evaluations demonstrate that $ $ significantly improves the privacy-utility
  trade-off and achieves superior performance in privacy auditing tasks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CARIBOU
- CARIBOU (EDP)
mrr: 0.0556
adjusted_mrr: 0.0556
mrr_dataset_count: 3
benchmark_categories:
- Classic
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
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
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.966
    std: 0.0033
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
    global_rank: 3
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.958
    std: null
    paper_value: 0.958
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.958
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.958
    sort_std: null
    is_best: false
  - model: GAP
    model_key: gap
    model_plain: GAP
    value: 0.93
    std: null
    paper_value: 0.93
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 32
    true_value: 0.93
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.93
    sort_std: null
    is_best: false
  - model: DPDGC
    model_key: dpdgc
    model_plain: DPDGC
    value: 0.925
    std: null
    paper_value: 0.925
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 35
    true_value: 0.925
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.925
    sort_std: null
    is_best: false
  - model: PertGraph
    model_key: pertgraph
    model_plain: PertGraph
    value: 0.824
    std: null
    paper_value: 0.824
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 46
    true_value: 0.824
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.824
    sort_std: null
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
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.851
    std: null
    paper_value: 0.851
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 102
    true_value: 0.851
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: null
    is_best: false
  - model: GAP
    model_key: gap
    model_plain: GAP
    value: 0.771
    std: null
    paper_value: 0.771
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 183
    true_value: 0.771
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: null
    is_best: false
  - model: DPDGC
    model_key: dpdgc
    model_plain: DPDGC
    value: 0.755
    std: null
    paper_value: 0.755
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 196
    true_value: 0.755
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: null
    is_best: false
  - model: PertGraph
    model_key: pertgraph
    model_plain: PertGraph
    value: 0.6
    std: null
    paper_value: 0.6
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 283
    true_value: 0.6
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 283
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: DPDGC
    model_key: dpdgc
    model_plain: DPDGC
    value: 0.883
    std: null
    paper_value: 0.883
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 61
    true_value: 0.883
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.883
    sort_std: null
    is_best: false
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.882
    std: null
    paper_value: 0.882
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 70
    true_value: 0.882
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.882
    sort_std: null
    is_best: false
  - model: GAP
    model_key: gap
    model_plain: GAP
    value: 0.874
    std: null
    paper_value: 0.874
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 84
    true_value: 0.874
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.874
    sort_std: null
    is_best: false
  - model: PertGraph
    model_key: pertgraph
    model_plain: PertGraph
    value: 0.85
    std: null
    paper_value: 0.85
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 101
    true_value: 0.85
    true_std: null
    value_gap_source_arxiv: '2506.22727'
    value_gap_source_title: Convergent Privacy Framework for Multi-layer GNNs through
      Contractive Message Passing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: CARIBOU (EDP)
    model_key: caribou (edp)
    model_plain: CARIBOU (EDP)
    value: 0.637
    std: null
    paper_value: 0.637
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.637
    sort_std: null
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
main_figure: /figures/2506.22727/main_figure.png
---

