---
title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
arxiv_id: '2508.19071'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
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
mrr: 0.2715
adjusted_mrr: 0.2715
mrr_dataset_count: 7
benchmark_categories:
- Classic
- Heterophilic Graphs
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id004
  dataset: Chameleon
  rows:
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7971
    std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7971
    sort_std: 0.0126
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7827
    std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7827
    sort_std: 0.0128
    is_best: true
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.761
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_display: Jan 2021
    date_iso: 2021-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.761
    sort_std: null
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
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
    paper_rank: 4
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
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
    paper_rank: 7
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 15
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
    paper_rank: 15
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
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
    paper_rank: 16
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
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
    paper_rank: 17
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 18
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
    paper_rank: 18
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
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
    paper_rank: 19
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
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
    paper_rank: 20
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 21
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
    paper_rank: 21
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
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
    paper_rank: 28
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 69
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
    paper_rank: 69
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
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
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8285
    sort_std: 0.0038
    is_best: true
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
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
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: ALT
    model_key: alt
    model_plain: ALT
    value: 0.7688
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.7688
    sort_std: 0.012
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7682
    std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.07256'
    title: 'Graph homophily booster: Reimagining the role of discrete features in
      heterophilic graph learning'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: https://github.com/q-rz/ICLR26-GRAPHITE
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.7682
    sort_std: 0.0148
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
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
    paper_rank: 9
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
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
    paper_rank: 13
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
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
    paper_rank: 17
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
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
    paper_rank: 19
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
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
    paper_rank: 20
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 22
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
    paper_rank: 22
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 24
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
    paper_rank: 24
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 25
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
    paper_rank: 25
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 85
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
    paper_rank: 85
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
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
    paper_rank: 2
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
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
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: Flan-T5-base
    model_key: flan-t5-base
    model_plain: Flan-T5-base
    value: 0.9077
    std: 0.0052
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
    sort_value: 0.9077
    sort_std: 0.0052
    is_best: false
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8995
    sort_std: 0.0201
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
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
    paper_rank: 20
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 25
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
    paper_rank: 25
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
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
    paper_rank: 27
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 30
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
    paper_rank: 30
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 31
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
    paper_rank: 31
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
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
    paper_rank: 32
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
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
    paper_rank: 34
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
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
    paper_rank: 36
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 123
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
    paper_rank: 123
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
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.873
    std: 0.0453
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
    sort_value: 0.873
    sort_std: 0.0453
    is_best: true
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.8649
    std: 0.0735
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
    global_rank: 2
    sort_value: 0.8649
    sort_std: 0.0735
    is_best: true
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8568
    std: 0.0663
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
    global_rank: 3
    sort_value: 0.8568
    sort_std: 0.0663
    is_best: true
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 27
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
    paper_rank: 27
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
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
    paper_rank: 28
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
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
    paper_rank: 42
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 47
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
    paper_rank: 47
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 48
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
    paper_rank: 48
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 49
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
    paper_rank: 49
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 50
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
    paper_rank: 50
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 51
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
    paper_rank: 51
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
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
    paper_rank: 52
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 53
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
    paper_rank: 53
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 54
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
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4446
    sort_std: 0.0137
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
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
    paper_rank: 37
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 40
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
    paper_rank: 40
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 48
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
    paper_rank: 48
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 51
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
    paper_rank: 51
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
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
    paper_rank: 52
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 53
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
    paper_rank: 53
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 55
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
    paper_rank: 55
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 56
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
    paper_rank: 56
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 58
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
    paper_rank: 58
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 59
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
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4923
    sort_std: 0.0033
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8784
    std: 0.044
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
    sort_value: 0.8784
    sort_std: 0.044
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8757
    std: 0.0486
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
    global_rank: 2
    sort_value: 0.8757
    sort_std: 0.0486
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.873
    std: 0.0593
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
    global_rank: 3
    sort_value: 0.873
    sort_std: 0.0593
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 20
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
    paper_rank: 20
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 25
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
    paper_rank: 25
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
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
    paper_rank: 28
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
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
    paper_rank: 32
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
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
    paper_rank: 36
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
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
    paper_rank: 37
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
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
    paper_rank: 38
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 39
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
    paper_rank: 39
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 41
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
    paper_rank: 41
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
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
    paper_rank: 42
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 46
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
    paper_rank: 46
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
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.0283
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
    sort_value: 0.9
    sort_std: 0.0283
    is_best: true
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8941
    std: 0.0474
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
    global_rank: 2
    sort_value: 0.8941
    sort_std: 0.0474
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8921
    std: 0.0384
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
    global_rank: 3
    sort_value: 0.8921
    sort_std: 0.0384
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 26
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
    paper_rank: 26
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
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
    paper_rank: 28
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 30
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
    paper_rank: 30
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
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
    paper_rank: 32
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
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
    paper_rank: 33
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
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
    paper_rank: 34
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 35
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
    paper_rank: 35
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
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
    paper_rank: 36
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 40
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
    paper_rank: 40
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
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
    paper_rank: 52
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 53
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
    paper_rank: 53
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
main_figure: /figures/2508.19071/main_figure.png
---

