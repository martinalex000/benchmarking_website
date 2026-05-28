---
title: Hybrid Focal and Full-Range Attention Based Graph Transformers
arxiv_id: '2311.04653'
source_url: ''
authors: []
published_date: Nov 2023
published_date_iso: 2023-11
abstract: The paradigm of Transformers using the self-attention mechanism has manifested
  its advantage in learning graph-structured data. Yet, Graph Transformers are capable
  of modeling full range dependencies but are often deficient in extracting information
  from locality. A common practice is to utilize Message Passing Neural Networks (MPNNs)
  as an auxiliary to capture local information, which however are still inadequate
  for comprehending substructures. In this paper, we present a purely attention-based
  architecture, namely Focal and Full-Range Graph Transformer (FFGT), which can mitigate
  the loss of local information in learning global correlations. The core component
  of FFGT is a new mechanism of compound attention, which combines the conventional
  full-range attention with K-hop focal attention on ego-nets to aggregate both global
  and local information. Beyond the scope of canonical Transformers, the FFGT has
  the merit of being more substructure-aware. Our approach enhances the performance
  of existing Graph Transformers on various open datasets, while achieves compatible
  SOTA performance on several Long-Range Graph Benchmark (LRGB) datasets even with
  a vanilla transformer. We further examine influential factors on the optimal focal
  length of attention via introducing a novel synthetic dataset based on SBM-PATTERN.
  blue
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- VANILLA-FFGT
- GRPE-FFGT
- FFGT (FL=1)
mrr: 0.0043
adjusted_mrr: 0.0014
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- GNNBenchmark
- OGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
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
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.6252
    std: 0.0097
    paper_value: 0.6252
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 58
    true_value: 0.6252
    true_std: 0.0097
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6252
    sort_std: 0.0097
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.5562
    std: 0.0043
    paper_value: 0.5562
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 85
    true_value: 0.5562
    true_std: 0.0043
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5562
    sort_std: 0.0043
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.5465
    std: 0.015
    paper_value: 0.5465
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 89
    true_value: 0.5465
    true_std: 0.015
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5465
    sort_std: 0.015
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.3681
    std: 0.0169
    paper_value: 0.3681
    paper_std: 0.0169
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 90
    true_value: 0.5453
    true_std: 0.0136
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17720000000000002
    value_note: ''
    paper_rank: 127
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.5453
    sort_std: 0.0136
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7369
    std: 0.0148
    paper_value: 0.7369
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 26
    true_value: 0.8012
    true_std: 0.0124
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06430000000000002
    value_note: ''
    paper_rank: 103
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0124
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.7531
    std: 0.0132
    paper_value: 0.7531
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 81
    true_value: 0.7531
    true_std: 0.0132
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7531
    sort_std: 0.0132
    is_best: false
  - model: UniMP
    model_key: unimp
    model_plain: UniMP
    value: 0.75
    std: 0.0159
    paper_value: 0.75
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 89
    true_value: 0.75
    true_std: 0.0159
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0159
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.733
    std: 0.0148
    paper_value: 0.733
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 107
    true_value: 0.733
    true_std: 0.0148
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.0148
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.7259
    std: 0.014
    paper_value: 0.7259
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 116
    true_value: 0.7259
    true_std: 0.014
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7259
    sort_std: 0.014
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6963
    std: 0.0376
    paper_value: 0.6963
    paper_std: 0.0376
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 132
    true_value: 0.7064
    true_std: 0.0097
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010099999999999998
    value_note: global 0.7064 within std
    paper_rank: 138
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.7064
    sort_std: 0.0097
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8577
    std: 0.0135
    paper_value: 0.8577
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02429999999999999
    value_note: ''
    paper_rank: 90
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.8659
    std: 0.0083
    paper_value: 0.8659
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 82
    true_value: 0.8659
    true_std: 0.0083
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8659
    sort_std: 0.0083
    is_best: false
  - model: UniMP
    model_key: unimp
    model_plain: UniMP
    value: 0.8418
    std: 0.0139
    paper_value: 0.8418
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 110
    true_value: 0.8418
    true_std: 0.0139
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8418
    sort_std: 0.0139
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.8252
    std: 0.013
    paper_value: 0.8252
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 137
    true_value: 0.8252
    true_std: 0.013
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8252
    sort_std: 0.013
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.8191
    std: 0.0342
    paper_value: 0.8191
    paper_std: 0.0342
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 143
    true_value: 0.8191
    true_std: 0.0342
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8191
    sort_std: 0.0342
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.6771
    std: 0.0078
    paper_value: 0.6771
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 192
    true_value: 0.758
    true_std: 0.011
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08089999999999997
    value_note: ''
    paper_rank: 262
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.758
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: PATTERN
  rows:
  - model: GRIT (our run)
    model_key: grit (our run)
    model_plain: GRIT (our run)
    value: 0.90405
    std: 0.00232
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.90405
    sort_std: 0.00232
    is_best: true
  - model: GRIT 2-QiQRW
    model_key: grit 2-qiqrw
    model_plain: GRIT 2-QiQRW
    value: 0.90165
    std: 0.00446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.90165
    sort_std: 0.00446
    is_best: true
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.89752
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_display: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.89752
    sort_std: 0.0003
    is_best: false
  - model: FFGT (FL=1)
    model_key: ffgt (fl=1)
    model_plain: FFGT (FL=1)
    value: 0.874412
    std: 0.000709
    paper_value: 0.874412
    paper_std: 0.000709
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 11
    true_value: 0.874412
    true_std: 0.000709
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.874412
    sort_std: 0.000709
    is_best: false
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    value: 0.873625
    std: 0.000699
    paper_value: 0.873625
    paper_std: 0.000699
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 13
    true_value: 0.873625
    true_std: 0.000699
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.873625
    sort_std: 0.000699
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6942
    std: 0.0075
    paper_value: 0.6942
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 61
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027999999999999137
    value_note: global 0.6970 within std
    paper_rank: 74
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.6956
    std: 0.008
    paper_value: 0.6956
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 69
    true_value: 0.6956
    true_std: 0.008
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6956
    sort_std: 0.008
    is_best: false
  - model: VANILLA-FFGT
    model_key: vanilla-ffgt
    model_plain: VANILLA-FFGT
    value: 0.6914
    std: 0.004
    paper_value: 0.6914
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 81
    true_value: 0.6914
    true_std: 0.004
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6914
    sort_std: 0.004
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.6836
    std: 0.006
    paper_value: 0.6836
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 94
    true_value: 0.6836
    true_std: 0.006
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6836
    sort_std: 0.006
    is_best: false
  - model: MGT
    model_key: mgt
    model_plain: MGT
    value: 0.6817
    std: 0.0064
    paper_value: 0.6817
    paper_std: 0.0064
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 103
    true_value: 0.6817
    true_std: 0.0064
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6817
    sort_std: 0.0064
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.673
    std: 0.0078
    paper_value: 0.673
    paper_std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 123
    true_value: 0.673
    true_std: 0.0078
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.673
    sort_std: 0.0078
    is_best: false
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    value: 0.6648
    std: 0.0087
    paper_value: 0.6648
    paper_std: 0.0087
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 136
    true_value: 0.6648
    true_std: 0.0087
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6648
    sort_std: 0.0087
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 168
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: 0.0043
    paper_value: 0.6527
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
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
    paper_value: 0.2416
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 2
    true_value: 0.2416
    true_std: 0.0026
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: 0.0006
    paper_value: 0.3234
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08130000000000001
    value_note: ''
    paper_rank: 287
    rank_delta: 284
    rank_delta_abs: 284
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.2422
    sort_std: 0.0007
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
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
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
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.2436
    std: 0.0018
    paper_value: 0.2436
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 22
    true_value: 0.2436
    true_std: 0.0018
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2436
    sort_std: 0.0018
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2449
    std: 0.0016
    paper_value: 0.2449
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: MGT
    model_key: mgt
    model_plain: MGT
    value: 0.2453
    std: 0.0025
    paper_value: 0.2453
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 39
    true_value: 0.2453
    true_std: 0.0025
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2453
    sort_std: 0.0025
    is_best: false
  - model: VANILLA-FFGT
    model_key: vanilla-ffgt
    model_plain: VANILLA-FFGT
    value: 0.2456
    std: 0.0017
    paper_value: 0.2456
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 47
    true_value: 0.2456
    true_std: 0.0017
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2456
    sort_std: 0.0017
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.2498
    std: 0.0008
    paper_value: 0.2498
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 131
    true_value: 0.2498
    true_std: 0.0008
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2498
    sort_std: 0.0008
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.25
    std: 0.0012
    paper_value: 0.25
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    value: 0.25
    std: 0.0027
    paper_value: 0.25
    paper_std: 0.0027
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 142
    true_value: 0.25
    true_std: 0.0027
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0027
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0042
    paper_value: 0.2683
    paper_std: 0.0042
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
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
  metric: MAE
  higher_is_better: false
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
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 107
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.084
    std: 0.002
    paper_value: 0.084
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: frasca2022understanding
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 14
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.060000000000000005
    value_note: ''
    paper_rank: 154
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.085
    std: 0.005
    paper_value: 0.085
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: he2023generalization
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 159
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 98
    true_value: 0.069
    true_std: 0.008
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.0690 within std
    paper_rank: 107
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.069
    sort_std: 0.008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: kipf2016semi
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.291
    value_note: ''
    paper_rank: 285
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.226
    std: 0.014
    paper_value: 0.226
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: bresson2017residual
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 132
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14900000000000002
    value_note: ''
    paper_rank: 263
    rank_delta: 131
    rank_delta_abs: 131
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.093
    std: 0.004
    paper_value: 0.093
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 181
    true_value: 0.093
    true_std: 0.004
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.004
    is_best: false
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.093
    std: 0.004
    paper_value: 0.093
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 181
    true_value: 0.093
    true_std: 0.004
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.004
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.101
    std: 0.006
    paper_value: 0.101
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 183
    true_value: 0.094
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007000000000000006
    value_note: ''
    paper_rank: 186
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.094
    sort_std: 0.002
    is_best: false
  - model: MGT
    model_key: mgt
    model_plain: MGT
    value: 0.131
    std: 0.003
    paper_value: 0.131
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ngo2023multiresolution
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 221
    true_value: 0.131
    true_std: 0.003
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.131
    sort_std: 0.003
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 227
    true_value: 0.139
    true_std: 0.006
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 227
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.139
    sort_std: 0.006
    is_best: false
  - model: VANILLA-FFGT
    model_key: vanilla-ffgt
    model_plain: VANILLA-FFGT
    value: 0.14
    std: 0.005
    paper_value: 0.14
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 230
    true_value: 0.14
    true_std: 0.005
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.14
    sort_std: 0.005
    is_best: false
  - model: VANILLA-FFGT
    model_key: vanilla-ffgt
    model_plain: VANILLA-FFGT
    value: 0.14
    std: 0.005
    paper_value: 0.14
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 230
    true_value: 0.14
    true_std: 0.005
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.14
    sort_std: 0.005
    is_best: false
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    value: 0.156
    std: 0.006
    paper_value: 0.156
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
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 242
    true_value: 0.156
    true_std: 0.006
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.156
    sort_std: 0.006
    is_best: false
  metric: MAE
  higher_is_better: false
- &id008
  dataset: ogbg-molpcba
  rows:
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
    is_best: true
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
    value: 0.267
    std: 0.002
    paper_value: 0.267
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 3
    true_value: 0.3066
    true_std: 0.0013
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03959999999999997
    value_note: ''
    paper_rank: 44
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: LGI-GT
    model_key: lgi-gt
    model_plain: LGI-GT
    value: 0.304
    std: 0.0029
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
    global_rank: 4
    sort_value: 0.304
    sort_std: 0.0029
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 20
    true_value: 0.291
    true_std: 0.001
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2910 within std
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.291
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 21
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2902
    std: 0.001
    paper_value: 0.2902
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 23
    true_value: 0.2902
    true_std: 0.001
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2902
    sort_std: 0.001
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.2856
    std: 0.0039
    paper_value: 0.2856
    paper_std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 27
    true_value: 0.2856
    true_std: 0.0039
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2856
    sort_std: 0.0039
    is_best: false
  - model: VANILLA-FFGT
    model_key: vanilla-ffgt
    model_plain: VANILLA-FFGT
    value: 0.2779
    std: 0.0049
    paper_value: 0.2779
    paper_std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 35
    true_value: 0.2779
    true_std: 0.0049
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2779
    sort_std: 0.0049
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2765
    std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 37
    true_value: 0.2765
    true_std: 0.0042
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2765
    sort_std: 0.0042
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2424
    std: 0.0034
    paper_value: 0.2424
    paper_std: 0.0034
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 40
    true_value: 0.2721
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029700000000000004
    value_note: ''
    paper_rank: 50
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.2721
    sort_std: 0.0046
    is_best: false
  - model: VANILLA
    model_key: vanilla
    model_plain: VANILLA
    value: 0.2638
    std: 0.0058
    paper_value: 0.2638
    paper_std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 46
    true_value: 0.2638
    true_std: 0.0058
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2638
    sort_std: 0.0058
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
- benchmark: GNNBenchmark
  datasets:
  - *id007
- benchmark: OGB
  datasets:
  - *id008
main_figure: /figures/2311.04653/main_figure.png
---

