---
title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
arxiv_id: '2508.19071'
source_url: ''
authors: []
published_date: Aug 26, 2025
published_date_iso: '2025-08-26'
published_venue: ''
abstract: Graph Neural Networks (GNNs) have emerged as the leading paradigm for learning
  over graph-structured data. However, their performance is limited by issues inherent
  to graph topology, most notably oversquashing and oversmoothing. Recent advances
  in graph rewiring aim to mitigate these limitations by modifying the graph topology
  to promote more effective information propagation. In this work, we introduce TRIGON,
  a novel framework that constructs enriched, non-planar triangulations by learning
  to select relevant triangles from multiple graph views. By jointly optimizing triangle
  selection and downstream classification performance, our method produces a rewired
  graph with markedly improved structural properties such as reduced diameter, increased
  spectral gap, and lower effective resistance compared to existing rewiring methods.
  Empirical results demonstrate that TRIGON outperforms state-of-the-art approaches
  on node classification tasks across a range of homophilic and heterophilic benchmarks.
codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- TRIGON
mrr: 0.0643
adjusted_mrr: 0.0643
mrr_dataset_count: 7
benchmark_categories:
- Classic
- Heterophilic Graphs
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id003
  dataset: Chameleon
  rows:
  - model: RUNG
    model_key: rung
    model_plain: RUNG
    value: 0.9773
    std: 0.0328
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9773
    sort_std: 0.0328
    is_best: true
  - model: DHGNN
    model_key: dhgnn
    model_plain: DHGNN
    value: 0.8011
    std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8011
    sort_std: 0.0173
    is_best: false
  - model: NDDGNN
    model_key: nddgnn
    model_plain: NDDGNN
    value: 0.7979
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7979
    sort_std: 0.0104
    is_best: false
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.7552
    std: 0.005
    paper_value: 0.7552
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 9
    true_value: 0.7552
    true_std: 0.005
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7552
    sort_std: 0.005
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7428
    std: 0.0048
    paper_value: 0.7428
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 15
    true_value: 0.7428
    true_std: 0.0048
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7428
    sort_std: 0.0048
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.6803
    std: 0.0061
    paper_value: 0.6803
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 57
    true_value: 0.6803
    true_std: 0.0061
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6803
    sort_std: 0.0061
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.6798
    std: 0.004
    paper_value: 0.6798
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 59
    true_value: 0.6798
    true_std: 0.004
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6798
    sort_std: 0.004
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.6585
    std: 0.0049
    paper_value: 0.6585
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 73
    true_value: 0.6585
    true_std: 0.0049
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6585
    sort_std: 0.0049
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.6535
    std: 0.0054
    paper_value: 0.6535
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 76
    true_value: 0.6535
    true_std: 0.0054
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0054
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.6535
    std: 0.0051
    paper_value: 0.6535
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 77
    true_value: 0.6535
    true_std: 0.0051
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0051
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.6507
    std: 0.0041
    paper_value: 0.6507
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (HeteroGAT)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 81
    true_value: 0.6507
    true_std: 0.0041
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6507
    sort_std: 0.0041
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.6308
    std: 0.0037
    paper_value: 0.6308
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 92
    true_value: 0.6308
    true_std: 0.0037
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6308
    sort_std: 0.0037
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.5482
    std: 0.0048
    paper_value: 0.5482
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 138
    true_value: 0.5482
    true_std: 0.0048
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5482
    sort_std: 0.0048
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.2634
    std: 0.0061
    paper_value: 0.2634
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 262
    true_value: 0.2634
    true_std: 0.0061
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2634
    sort_std: 0.0061
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.952
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.952
    sort_std: 0.002
    is_best: true
  - model: Policy-GNN
    model_key: policy-gnn
    model_plain: Policy-GNN
    value: 0.897
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_display: Jun 2020
    date_iso: 2020-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.897
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.88
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 21, 2018
    date_display: May 2018
    date_iso: '2018-05-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.88
    sort_std: null
    is_best: false
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.8285
    std: 0.0038
    paper_value: 0.8285
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 5
    true_value: 0.8285
    true_std: 0.0038
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8285
    sort_std: 0.0038
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.8114
    std: 0.0034
    paper_value: 0.8114
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 13
    true_value: 0.8114
    true_std: 0.0034
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8114
    sort_std: 0.0034
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.7649
    std: 0.0028
    paper_value: 0.7649
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 93
    true_value: 0.7649
    true_std: 0.0028
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7649
    sort_std: 0.0028
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.7643
    std: 0.0032
    paper_value: 0.7643
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 98
    true_value: 0.7643
    true_std: 0.0032
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7643
    sort_std: 0.0032
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.7634
    std: 0.0027
    paper_value: 0.7634
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 101
    true_value: 0.7634
    true_std: 0.0027
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7634
    sort_std: 0.0027
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.7622
    std: 0.0034
    paper_value: 0.7622
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 104
    true_value: 0.7622
    true_std: 0.0034
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7622
    sort_std: 0.0034
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.762
    std: 0.0027
    paper_value: 0.762
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 106
    true_value: 0.762
    true_std: 0.0027
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.0027
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.7612
    std: 0.0028
    paper_value: 0.7612
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 112
    true_value: 0.7612
    true_std: 0.0028
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7612
    sort_std: 0.0028
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.7609
    std: 0.0029
    paper_value: 0.7609
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 115
    true_value: 0.7609
    true_std: 0.0029
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609
    sort_std: 0.0029
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.7601
    std: 0.0025
    paper_value: 0.7601
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 119
    true_value: 0.7601
    true_std: 0.0025
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7601
    sort_std: 0.0025
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.2231
    std: 0.0034
    paper_value: 0.2231
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 807
    true_value: 0.2231
    true_std: 0.0034
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 807
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2231
    sort_std: 0.0034
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: Self-Explainable GNN
    model_key: self-explainable gnn
    model_plain: Self-Explainable GNN
    value: 0.977
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.977
    sort_std: 0.016
    is_best: true
  - model: GCN-K
    model_key: gcn-k
    model_plain: GCN-K
    value: 0.948
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.007
    is_best: false
  - model: KP-GIN
    model_key: kp-gin
    model_plain: KP-GIN
    value: 0.946
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 26, 2021
    date_display: Aug 2021
    date_iso: '2021-08-26'
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.946
    sort_std: 0.007
    is_best: false
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9171
    std: 0.0029
    paper_value: 0.9171
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 10
    true_value: 0.9171
    true_std: 0.0029
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9171
    sort_std: 0.0029
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    paper_value: 0.9139
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 12
    true_value: 0.9139
    true_std: 0.0024
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.8831
    std: 0.0029
    paper_value: 0.8831
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 88
    true_value: 0.8831
    true_std: 0.0029
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8831
    sort_std: 0.0029
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.8794
    std: 0.0026
    paper_value: 0.8794
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 107
    true_value: 0.8794
    true_std: 0.0026
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8794
    sort_std: 0.0026
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.8786
    std: 0.0028
    paper_value: 0.8786
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 111
    true_value: 0.8786
    true_std: 0.0028
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8786
    sort_std: 0.0028
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.8773
    std: 0.0025
    paper_value: 0.8773
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 122
    true_value: 0.8773
    true_std: 0.0025
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8773
    sort_std: 0.0025
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.8773
    std: 0.0031
    paper_value: 0.8773
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 123
    true_value: 0.8773
    true_std: 0.0031
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8773
    sort_std: 0.0031
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.8772
    std: 0.0027
    paper_value: 0.8772
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 124
    true_value: 0.8772
    true_std: 0.0027
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8772
    sort_std: 0.0027
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.8765
    std: 0.0024
    paper_value: 0.8765
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (HeteroGAT)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 132
    true_value: 0.8765
    true_std: 0.0024
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8765
    sort_std: 0.0024
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.8754
    std: 0.0025
    paper_value: 0.8754
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 137
    true_value: 0.8754
    true_std: 0.0025
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8754
    sort_std: 0.0025
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.2986
    std: 0.0028
    paper_value: 0.2986
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 945
    true_value: 0.2986
    true_std: 0.0028
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 945
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2986
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.938
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 28, 2023
    date_display: Feb 2023
    date_iso: '2023-02-28'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.938
    sort_std: 0.015
    is_best: true
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.914
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.914
    sort_std: 0.017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.6911
    std: 0.0153
    paper_value: 0.6911
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 117
    true_value: 0.6911
    true_std: 0.0153
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6911
    sort_std: 0.0153
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.6722
    std: 0.0148
    paper_value: 0.6722
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 125
    true_value: 0.6722
    true_std: 0.0148
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6722
    sort_std: 0.0148
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.5731
    std: 0.016
    paper_value: 0.5731
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 172
    true_value: 0.5731
    true_std: 0.016
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5731
    sort_std: 0.016
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.4773
    std: 0.0151
    paper_value: 0.4773
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 219
    true_value: 0.4773
    true_std: 0.0151
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4773
    sort_std: 0.0151
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.4757
    std: 0.0152
    paper_value: 0.4757
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 221
    true_value: 0.4757
    true_std: 0.0152
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4757
    sort_std: 0.0152
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.4681
    std: 0.0156
    paper_value: 0.4681
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 223
    true_value: 0.4681
    true_std: 0.0156
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4681
    sort_std: 0.0156
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.4605
    std: 0.0149
    paper_value: 0.4605
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 226
    true_value: 0.4605
    true_std: 0.0149
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 226
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4605
    sort_std: 0.0149
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.4533
    std: 0.0155
    paper_value: 0.4533
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 232
    true_value: 0.4533
    true_std: 0.0155
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 232
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4533
    sort_std: 0.0155
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.4511
    std: 0.0147
    paper_value: 0.4511
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 233
    true_value: 0.4511
    true_std: 0.0147
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4511
    sort_std: 0.0147
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.4478
    std: 0.0145
    paper_value: 0.4478
    paper_std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 235
    true_value: 0.4478
    true_std: 0.0145
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 235
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4478
    sort_std: 0.0145
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.4446
    std: 0.0137
    paper_value: 0.4446
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 237
    true_value: 0.4446
    true_std: 0.0137
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 237
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4446
    sort_std: 0.0137
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
    date: Jul 1, 2025
    date_display: Jul 2025
    date_iso: '2025-07-01'
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
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
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
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9203
    sort_std: 0.0085
    is_best: true
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.7123
    std: 0.0018
    paper_value: 0.7123
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 57
    true_value: 0.7123
    true_std: 0.0018
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7123
    sort_std: 0.0018
    is_best: false
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.6652
    std: 0.0013
    paper_value: 0.6652
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 70
    true_value: 0.6652
    true_std: 0.0013
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6652
    sort_std: 0.0013
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.6199
    std: 0.0014
    paper_value: 0.6199
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 84
    true_value: 0.6199
    true_std: 0.0014
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6199
    sort_std: 0.0014
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.5858
    std: 0.0014
    paper_value: 0.5858
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 86
    true_value: 0.5858
    true_std: 0.0014
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5858
    sort_std: 0.0014
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.5393
    std: 0.0014
    paper_value: 0.5393
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 87
    true_value: 0.5393
    true_std: 0.0014
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5393
    sort_std: 0.0014
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.5331
    std: 0.0023
    paper_value: 0.5331
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 88
    true_value: 0.5331
    true_std: 0.0023
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5331
    sort_std: 0.0023
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.5253
    std: 0.0013
    paper_value: 0.5253
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 91
    true_value: 0.5253
    true_std: 0.0013
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5253
    sort_std: 0.0013
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.5238
    std: 0.0021
    paper_value: 0.5238
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 92
    true_value: 0.5238
    true_std: 0.0021
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5238
    sort_std: 0.0021
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.5166
    std: 0.0017
    paper_value: 0.5166
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 94
    true_value: 0.5166
    true_std: 0.0017
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5166
    sort_std: 0.0017
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.4923
    std: 0.0033
    paper_value: 0.4923
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 95
    true_value: 0.4923
    true_std: 0.0033
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4923
    sort_std: 0.0033
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  rows:
  - model: DoG (ACM-GCN)
    model_key: dog (acm-gcn)
    model_plain: DoG (ACM-GCN)
    value: 0.966
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 16, 2025
    date_display: Mar 2025
    date_iso: '2025-03-16'
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.966
    sort_std: 0.021
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.951
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 16, 2025
    date_display: Mar 2025
    date_iso: '2025-03-16'
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.951
    sort_std: 0.032
    is_best: true
  - model: AD-MixHop
    model_key: ad-mixhop
    model_plain: AD-MixHop
    value: 0.9443
    std: 0.0256
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9443
    sort_std: 0.0256
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.7574
    std: 0.0161
    paper_value: 0.7574
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 129
    true_value: 0.7574
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7574
    sort_std: 0.0161
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7046
    std: 0.0161
    paper_value: 0.7046
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 150
    true_value: 0.7046
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7046
    sort_std: 0.0161
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.6956
    std: 0.0171
    paper_value: 0.6956
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 159
    true_value: 0.6956
    true_std: 0.0171
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6956
    sort_std: 0.0171
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.6135
    std: 0.0125
    paper_value: 0.6135
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 201
    true_value: 0.6135
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6135
    sort_std: 0.0125
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.5979
    std: 0.0171
    paper_value: 0.5979
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 215
    true_value: 0.5979
    true_std: 0.0171
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 215
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5979
    sort_std: 0.0171
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.5718
    std: 0.0164
    paper_value: 0.5718
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 231
    true_value: 0.5718
    true_std: 0.0164
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5718
    sort_std: 0.0164
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.5684
    std: 0.0161
    paper_value: 0.5684
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGAT
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 233
    true_value: 0.5684
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5684
    sort_std: 0.0161
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.563
    std: 0.0161
    paper_value: 0.563
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 234
    true_value: 0.563
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.563
    sort_std: 0.0161
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.5619
    std: 0.0161
    paper_value: 0.5619
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 236
    true_value: 0.5619
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 236
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5619
    sort_std: 0.0161
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.5593
    std: 0.0176
    paper_value: 0.5593
    paper_std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 239
    true_value: 0.5593
    true_std: 0.0176
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5593
    sort_std: 0.0176
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.4595
    std: 0.0158
    paper_value: 0.4595
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table HeteroGCN
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 261
    true_value: 0.4595
    true_std: 0.0158
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 261
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4595
    sort_std: 0.0158
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.937
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 28, 2023
    date_display: Feb 2023
    date_iso: '2023-02-28'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.937
    sort_std: 0.012
    is_best: true
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.739
    std: 0.0161
    paper_value: 0.739
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 124
    true_value: 0.739
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.0161
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7098
    std: 0.015
    paper_value: 0.7098
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 138
    true_value: 0.7098
    true_std: 0.015
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7098
    sort_std: 0.015
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.6787
    std: 0.0162
    paper_value: 0.6787
    paper_std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 145
    true_value: 0.6787
    true_std: 0.0162
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6787
    sort_std: 0.0162
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.5849
    std: 0.0123
    paper_value: 0.5849
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 180
    true_value: 0.5849
    true_std: 0.0123
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5849
    sort_std: 0.0123
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.5722
    std: 0.015
    paper_value: 0.5722
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 184
    true_value: 0.5722
    true_std: 0.015
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5722
    sort_std: 0.015
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.556
    std: 0.0125
    paper_value: 0.556
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 196
    true_value: 0.556
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.556
    sort_std: 0.0125
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.5537
    std: 0.0147
    paper_value: 0.5537
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 198
    true_value: 0.5537
    true_std: 0.0147
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5537
    sort_std: 0.0147
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.5512
    std: 0.0151
    paper_value: 0.5512
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 200
    true_value: 0.5512
    true_std: 0.0151
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5512
    sort_std: 0.0151
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.5358
    std: 0.0139
    paper_value: 0.5358
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 212
    true_value: 0.5358
    true_std: 0.0139
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5358
    sort_std: 0.0139
    is_best: false
  - model: DIGL
    model_key: digl
    model_plain: DIGL
    value: 0.469
    std: 0.0128
    paper_value: 0.469
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 240
    true_value: 0.469
    true_std: 0.0128
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.469
    sort_std: 0.0128
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.4677
    std: 0.0148
    paper_value: 0.4677
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 26, 2025
    date_display: Aug 2025
    date_iso: '2025-08-26'
    published_venue: null
    global_rank: 241
    true_value: 0.4677
    true_std: 0.0148
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 241
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4677
    sort_std: 0.0148
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
  - *id007
single_proposed_model: TRIGON
---

