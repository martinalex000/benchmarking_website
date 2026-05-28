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
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- TRIGON
mrr: 0.2018
adjusted_mrr: 0.2018
mrr_dataset_count: 6
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 11
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
    paper_rank: 11
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
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
    paper_rank: 17
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
    std: 0.0060999999999999995
    paper_value: 0.6803
    paper_std: 0.0060999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.6803
    true_std: 0.0060999999999999995
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
    sort_value: 0.6803
    sort_std: 0.0060999999999999995
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.6798000000000001
    std: 0.004
    paper_value: 0.6798000000000001
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.6798000000000001
    true_std: 0.004
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
    sort_value: 0.6798000000000001
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 41
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
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6585
    sort_std: 0.0049
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 43
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
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0051
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 44
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
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0054
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.6507
    std: 0.0040999999999999995
    paper_value: 0.6507
    paper_std: 0.0040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 46
    true_value: 0.6507
    true_std: 0.0040999999999999995
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
    sort_value: 0.6507
    sort_std: 0.0040999999999999995
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 53
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
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6308
    sort_std: 0.0037
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 88
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
    paper_rank: 88
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
    std: 0.0060999999999999995
    paper_value: 0.2634
    paper_std: 0.0060999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 128
    true_value: 0.2634
    true_std: 0.0060999999999999995
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2634
    sort_std: 0.0060999999999999995
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
    paper_value: 0.9170999999999999
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.9170999999999999
    true_std: 0.0029
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
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
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
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: ANS-GT + HDSE
    model_key: ans-gt + hdse
    model_plain: ANS-GT + HDSE
    value: 0.8967
    std: 0.0039
    metric: Accuracy
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
    sort_value: 0.8967
    sort_std: 0.0039
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8957
    std: 0.0143
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
    global_rank: 5
    sort_value: 0.8957
    sort_std: 0.0143
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 29
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
    paper_rank: 29
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 43
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
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8794
    sort_std: 0.0026
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 44
    true_value: 0.879
    true_std: 0.007
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0018000000000000238
    value_note: global 0.8790 within std
    paper_rank: 50
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.007
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.8786
    std: 0.0028000000000000004
    paper_value: 0.8786
    paper_std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 46
    true_value: 0.8786
    true_std: 0.0028000000000000004
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
    sort_value: 0.8786
    sort_std: 0.0028000000000000004
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.8773000000000001
    std: 0.0025
    paper_value: 0.8773000000000001
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 49
    true_value: 0.8773000000000001
    true_std: 0.0025
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
    sort_value: 0.8773000000000001
    sort_std: 0.0025
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.8773000000000001
    std: 0.0031
    paper_value: 0.8773000000000001
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 50
    true_value: 0.8773000000000001
    true_std: 0.0031
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
    sort_value: 0.8773000000000001
    sort_std: 0.0031
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.8765000000000001
    std: 0.0024
    paper_value: 0.8765000000000001
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
    true_value: 0.8765000000000001
    true_std: 0.0024
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
    sort_value: 0.8765000000000001
    sort_std: 0.0024
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.8754000000000001
    std: 0.0025
    paper_value: 0.8754000000000001
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 58
    true_value: 0.8754000000000001
    true_std: 0.0025
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
    sort_value: 0.8754000000000001
    sort_std: 0.0025
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.2986
    std: 0.0028000000000000004
    paper_value: 0.2986
    paper_std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 147
    true_value: 0.8165
    true_std: null
    value_gap_source_arxiv: '2502.07364'
    value_gap_source_title: Effects of Dropout on Performance in Long-range Graph
      Learning Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5179
    value_note: ''
    paper_rank: 299
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.8165
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.6911
    std: 0.015300000000000001
    paper_value: 0.6911
    paper_std: 0.015300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 71
    true_value: 0.6911
    true_std: 0.015300000000000001
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6911
    sort_std: 0.015300000000000001
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 79
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
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6722
    sort_std: 0.0148
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 105
    true_value: 0.582
    true_std: 0.005
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13739999999999997
    value_note: ''
    paper_rank: 140
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.582
    sort_std: 0.005
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 110
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
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5731
    sort_std: 0.016
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.4681
    std: 0.015600000000000001
    paper_value: 0.4681
    paper_std: 0.015600000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 127
    true_value: 0.508
    true_std: 0.011
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03989999999999999
    value_note: ''
    paper_rank: 134
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.508
    sort_std: 0.011
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.47729999999999995
    std: 0.0151
    paper_value: 0.47729999999999995
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 131
    true_value: 0.47729999999999995
    true_std: 0.0151
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47729999999999995
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 132
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
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4757
    sort_std: 0.0152
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.46049999999999996
    std: 0.0149
    paper_value: 0.46049999999999996
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (HeteroGAT)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 136
    true_value: 0.46049999999999996
    true_std: 0.0149
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.46049999999999996
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 137
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
    paper_rank: 137
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
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 138
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
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4511
    sort_std: 0.0147
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.44780000000000003
    std: 0.014499999999999999
    paper_value: 0.44780000000000003
    paper_std: 0.014499999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (HeteroGCN)
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 140
    true_value: 0.44780000000000003
    true_std: 0.014499999999999999
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.44780000000000003
    sort_std: 0.014499999999999999
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    value: 0.741
    std: 0.0189
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
    global_rank: 3
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.6648000000000001
    std: 0.0034999999999999996
    paper_value: 0.6648000000000001
    paper_std: 0.0034999999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 12
    true_value: 0.6648000000000001
    true_std: 0.0034999999999999996
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
    sort_value: 0.6648000000000001
    sort_std: 0.0034999999999999996
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.6525
    std: 0.0026
    paper_value: 0.6525
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.6525
    true_std: 0.0026
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6525
    sort_std: 0.0026
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.5378000000000001
    std: 0.0046
    paper_value: 0.5378000000000001
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 30
    true_value: 0.5378000000000001
    true_std: 0.0046
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
    sort_value: 0.5378000000000001
    sort_std: 0.0046
    is_best: false
  - model: GTR
    model_key: gtr
    model_plain: GTR
    value: 0.5332
    std: 0.0044
    paper_value: 0.5332
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.5332
    true_std: 0.0044
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
    sort_value: 0.5332
    sort_std: 0.0044
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.5263
    std: 0.003
    paper_value: 0.5263
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 34
    true_value: 0.5263
    true_std: 0.003
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
    sort_value: 0.5263
    sort_std: 0.003
    is_best: false
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.513
    std: 0.0038
    paper_value: 0.513
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 39
    true_value: 0.513
    true_std: 0.0038
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
    sort_value: 0.513
    sort_std: 0.0038
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.5086999999999999
    std: 0.005600000000000001
    paper_value: 0.5086999999999999
    paper_std: 0.005600000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 40
    true_value: 0.5086999999999999
    true_std: 0.005600000000000001
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
    sort_value: 0.5086999999999999
    sort_std: 0.005600000000000001
    is_best: false
  - model: SRDF
    model_key: srdf
    model_plain: SRDF
    value: 0.4911
    std: 0.0028000000000000004
    paper_value: 0.4911
    paper_std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
    true_value: 0.4911
    true_std: 0.0028000000000000004
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
    sort_value: 0.4911
    sort_std: 0.0028000000000000004
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.4053
    std: 0.0029
    paper_value: 0.4053
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 76
    true_value: 0.4053
    true_std: 0.0029
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
    sort_value: 0.4053
    sort_std: 0.0029
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.2288
    std: 0.0042
    paper_value: 0.2288
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 112
    true_value: 0.2288
    true_std: 0.0042
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
    sort_value: 0.2288
    sort_std: 0.0042
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 87
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
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7574
    sort_std: 0.0161
    is_best: false
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.7045999999999999
    std: 0.0161
    paper_value: 0.7045999999999999
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 113
    true_value: 0.7045999999999999
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7045999999999999
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 116
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
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6956
    sort_std: 0.0171
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 140
    true_value: 0.62
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16049999999999998
    value_note: ''
    paper_rank: 168
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.62
    sort_std: 0.003
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 141
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
    paper_rank: 141
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 148
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
    paper_rank: 148
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
    std: 0.016399999999999998
    paper_value: 0.5718
    paper_std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 153
    true_value: 0.5718
    true_std: 0.016399999999999998
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5718
    sort_std: 0.016399999999999998
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 154
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
    paper_rank: 154
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 155
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
    paper_rank: 155
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 157
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
    paper_rank: 157
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 158
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
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5593
    sort_std: 0.0176
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Wisconsin
  rows:
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.7390000000000001
    std: 0.0161
    paper_value: 0.7390000000000001
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 90
    true_value: 0.7390000000000001
    true_std: 0.0161
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7390000000000001
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 95
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
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7098
    sort_std: 0.015
    is_best: false
  - model: JDR
    model_key: jdr
    model_plain: JDR
    value: 0.6787000000000001
    std: 0.016200000000000003
    paper_value: 0.6787000000000001
    paper_std: 0.016200000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 104
    true_value: 0.6787000000000001
    true_std: 0.016200000000000003
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
    sort_value: 0.6787000000000001
    sort_std: 0.016200000000000003
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 118
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
    paper_rank: 118
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 122
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
    paper_rank: 122
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 125
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
    paper_rank: 125
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 127
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
    paper_rank: 127
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 128
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
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5512
    sort_std: 0.0151
    is_best: false
  - model: Base (GAT)
    model_key: base (gat)
    model_plain: Base (GAT)
    value: 0.5357999999999999
    std: 0.0139
    paper_value: 0.5357999999999999
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 129
    true_value: 0.5357999999999999
    true_std: 0.0139
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
    sort_value: 0.5357999999999999
    sort_std: 0.0139
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 135
    true_value: 0.517
    true_std: 0.013
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000004
    value_note: ''
    paper_rank: 138
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.517
    sort_std: 0.013
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
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 139
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
    paper_rank: 139
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
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
single_proposed_model: TRIGON
main_figure: /figures/2508.19071/main_figure.png
---

