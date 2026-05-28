---
title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
arxiv_id: '2501.09821'
source_url: ''
authors: []
published_date: Jan 2025
published_date_iso: 2025-01
abstract: We introduce BN-Pool, the first clustering-based pooling method for Graph
  Neural Networks that adaptively determines the number of supernodes in a coarsened
  graph. BN-Pool leverages a generative model based on a Bayesian nonparametric framework
  for partitioning graph nodes into an unbounded number of clusters. During training,
  the node-to-cluster assignments are learned by combining the supervised loss of
  the downstream task with an unsupervised auxiliary term, which encourages the reconstruction
  of the original graph topology while penalizing unnecessary proliferation of clusters.
  By automatically discovering the optimal coarsening level for each graph, BN-Pool
  preserves the performance of soft-clustering pooling methods while avoiding their
  typical redundancy by learning compact pooled graphs. The code is available at https://github.com/NGMLGroup/Bayesian-Nonparametric-Graph-Pooling.
codebase_url: ''
extraction_model: openai-gpt-oss-120b
has_results: true
paper_type: method
proposed_models:
- BNPool
- ECPool
- KMIS
mrr: 0.0185
adjusted_mrr: 0.0185
mrr_dataset_count: 9
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- OGB
- Heterogeneous Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
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
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7
    std: 0.02
    paper_value: 0.7
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 6
    true_value: 0.8213
    true_std: 0.0043
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12130000000000007
    value_note: ''
    paper_rank: 77
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.8213
    sort_std: 0.0043
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.72
    std: 0.03
    paper_value: 0.72
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 9
    true_value: 0.8128
    true_std: 0.0015
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0928
    value_note: ''
    paper_rank: 63
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.8128
    sort_std: 0.0015
    is_best: false
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.75
    std: 0.02
    paper_value: 0.75
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 37
    true_value: 0.75
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.02
    is_best: false
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.73
    std: 0.03
    paper_value: 0.73
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 51
    true_value: 0.73
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.03
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.73
    std: 0.02
    paper_value: 0.73
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 52
    true_value: 0.73
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.02
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.72
    std: 0.02
    paper_value: 0.72
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 67
    true_value: 0.72
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.02
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.72
    std: 0.03
    paper_value: 0.72
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 64
    true_value: 0.72
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.03
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.72
    std: 0.03
    paper_value: 0.72
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 65
    true_value: 0.72
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.03
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.72
    std: 0.02
    paper_value: 0.72
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 66
    true_value: 0.72
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.02
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.71
    std: 0.02
    paper_value: 0.71
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 76
    true_value: 0.71
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.02
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.7
    std: 0.02
    paper_value: 0.7
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 79
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.02
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.7
    std: 0.04
    paper_value: 0.7
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 78
    true_value: 0.7
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.04
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.68
    std: 0.02
    paper_value: 0.68
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 87
    true_value: 0.68
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
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
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.543
    std: 0.05
    paper_value: 0.543
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 211
    true_value: 0.543
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 211
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.543
    sort_std: 0.05
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.507
    std: 0.024
    paper_value: 0.507
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 212
    true_value: 0.507
    true_std: 0.024
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.507
    sort_std: 0.024
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.481
    std: 0.05
    paper_value: 0.481
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 215
    true_value: 0.481
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 215
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.481
    sort_std: 0.05
    is_best: false
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.479
    std: 0.017
    paper_value: 0.479
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 216
    true_value: 0.479
    true_std: 0.017
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 216
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.479
    sort_std: 0.017
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.379
    std: 0.014
    paper_value: 0.379
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
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 218
    true_value: 0.379
    true_std: 0.014
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.014
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
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.668
    std: 0.01
    paper_value: 0.668
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 266
    true_value: 0.668
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 266
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.668
    sort_std: 0.01
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.579
    std: 0.038
    paper_value: 0.579
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 288
    true_value: 0.579
    true_std: 0.038
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 288
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.579
    sort_std: 0.038
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.57
    std: 0.021
    paper_value: 0.57
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 293
    true_value: 0.57
    true_std: 0.021
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 293
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.554
    std: 0.024
    paper_value: 0.554
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 294
    true_value: 0.554
    true_std: 0.024
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.024
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.504
    std: 0.011
    paper_value: 0.504
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 297
    true_value: 0.504
    true_std: 0.011
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 297
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.504
    sort_std: 0.011
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: DBLP
  is_multi_metric: true
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    metric_values:
    - 0.9249
    - null
    metric_stds:
    - 0.0035
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.9249
    sort_std: 0.0035
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    metric_values:
    - 0.9182
    - null
    metric_stds:
    - 0.0027
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.9182
    sort_std: 0.0027
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GTN
    model_key: gtn
    model_plain: GTN
    metric_values:
    - 0.9148
    - null
    metric_stds:
    - 0.0039
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.9148
    sort_std: 0.0039
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    metric_values:
    - 0.752
    - 0.585
    metric_stds:
    - 0.007
    - 0.007
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.752
    sort_std: 0.007
    true_value: null
    true_std: null
    paper_value: 0.752
    paper_std: 0.007
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    metric_values:
    - 0.692
    - 0.525
    metric_stds:
    - 0.034
    - 0.039
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.692
    sort_std: 0.034
    true_value: null
    true_std: null
    paper_value: 0.692
    paper_std: 0.034
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    metric_values:
    - 0.686
    - 0.53
    metric_stds:
    - 0.018
    - 0.044
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.686
    sort_std: 0.018
    true_value: null
    true_std: null
    paper_value: 0.686
    paper_std: 0.018
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DMON
    model_key: dmon
    model_plain: DMON
    metric_values:
    - 0.637
    - 0.454
    metric_stds:
    - 0.032
    - 0.013
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.637
    sort_std: 0.032
    true_value: null
    true_std: null
    paper_value: 0.637
    paper_std: 0.032
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    metric_values:
    - 0.495
    - 0.574
    metric_stds:
    - 0.049
    - 0.0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.495
    sort_std: 0.049
    true_value: null
    true_std: null
    paper_value: 0.495
    paper_std: 0.049
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - ACC
  - COS
  primary_metric: Micro-F1
  higher_is_better: true
- &id008
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.36
    std: 0.07
    paper_value: 0.36
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 14
    true_value: 0.595
    true_std: 0.056
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.235
    value_note: ''
    paper_rank: 60
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.595
    sort_std: 0.056
    is_best: false
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.54
    std: 0.07
    paper_value: 0.54
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 18
    true_value: 0.54
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.54
    sort_std: 0.07
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.37
    std: 0.07
    paper_value: 0.37
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 48
    true_value: 0.4
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.030000000000000027
    value_note: global 0.4000 within std
    paper_rank: 58
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.4
    sort_std: 0.04
    is_best: false
  - model: SepPool
    model_key: seppool
    model_plain: SepPool
    value: 0.4
    std: 0.06
    paper_value: 0.4
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 47
    true_value: 0.4
    true_std: 0.06
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4
    sort_std: 0.06
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.39
    std: 0.06
    paper_value: 0.39
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 50
    true_value: 0.39
    true_std: 0.06
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.06
    is_best: false
  - model: EigenPool
    model_key: eigenpool
    model_plain: EigenPool
    value: 0.39
    std: 0.06
    paper_value: 0.39
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 51
    true_value: 0.39
    true_std: 0.06
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.06
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.34
    std: 0.09
    paper_value: 0.34
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 59
    true_value: 0.37
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02999999999999997
    value_note: global 0.3700 within std
    paper_rank: 67
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.37
    sort_std: 0.05
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.36
    std: 0.09
    paper_value: 0.36
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 61
    true_value: 0.36
    true_std: 0.09
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.09
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.35
    std: 0.08
    paper_value: 0.35
    paper_std: 0.08
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 65
    true_value: 0.35
    true_std: 0.08
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.08
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.33
    std: 0.13
    paper_value: 0.33
    paper_std: 0.13
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 72
    true_value: 0.33
    true_std: 0.13
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33
    sort_std: 0.13
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.33
    std: 0.07
    paper_value: 0.33
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 73
    true_value: 0.33
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33
    sort_std: 0.07
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.33
    std: 0.08
    paper_value: 0.33
    paper_std: 0.08
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 74
    true_value: 0.33
    true_std: 0.08
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33
    sort_std: 0.08
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.29
    std: 0.07
    paper_value: 0.29
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 100
    true_value: 0.29
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.29
    sort_std: 0.07
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    paper_value: 0.63
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 1
    true_value: 0.63
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    paper_value: 0.62
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 2
    true_value: 0.62
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.61
    std: 0.02
    paper_value: 0.61
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 3
    true_value: 0.61
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.61
    std: 0.02
    paper_value: 0.61
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 4
    true_value: 0.61
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.58
    std: 0.02
    paper_value: 0.58
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 5
    true_value: 0.58
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.58
    sort_std: 0.02
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.5731
    sort_std: 0.0219
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.5673
    std: 0.0036
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
    global_rank: 7
    sort_value: 0.5673
    sort_std: 0.0036
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.56
    std: 0.03
    paper_value: 0.56
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 10
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.56
    std: 0.03
    paper_value: 0.56
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 11
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.56
    std: 0.03
    paper_value: 0.56
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 12
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.51
    std: 0.02
    paper_value: 0.51
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 27
    true_value: 0.51
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51
    sort_std: 0.02
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.49
    std: 0.07
    paper_value: 0.49
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 52
    true_value: 0.49
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.07
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.48
    std: 0.02
    paper_value: 0.48
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 65
    true_value: 0.48
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.02
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.45
    std: 0.03
    paper_value: 0.45
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 72
    true_value: 0.45
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45
    sort_std: 0.03
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.14
    std: 0.12
    paper_value: 0.14
    paper_std: 0.12
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 79
    true_value: 0.14
    true_std: 0.12
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.14
    sort_std: 0.12
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.88
    std: 0.07
    paper_value: 0.88
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 44
    true_value: 0.88
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.88
    sort_std: 0.07
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.87
    std: 0.14
    paper_value: 0.87
    paper_std: 0.14
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 49
    true_value: 0.87
    true_std: 0.14
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87
    sort_std: 0.14
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.81
    std: 0.09
    paper_value: 0.81
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 61
    true_value: 0.8556
    true_std: 0.0109
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.045599999999999974
    value_note: global 0.8556 within std
    paper_rank: 94
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.8556
    sort_std: 0.0109
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.82
    std: 0.11
    paper_value: 0.82
    paper_std: 0.11
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 69
    true_value: 0.84
    true_std: 0.08
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.020000000000000018
    value_note: global 0.8400 within std
    paper_rank: 87
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.84
    sort_std: 0.08
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.84
    std: 0.12
    paper_value: 0.84
    paper_std: 0.12
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 68
    true_value: 0.84
    true_std: 0.12
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.12
    is_best: true
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.84
    std: 0.07
    paper_value: 0.84
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 70
    true_value: 0.84
    true_std: 0.07
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.07
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.81
    std: 0.12
    paper_value: 0.81
    paper_std: 0.12
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 78
    true_value: 0.83
    true_std: 0.07
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.019999999999999907
    value_note: global 0.8300 within std
    paper_rank: 94
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.83
    sort_std: 0.07
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.83
    std: 0.1
    paper_value: 0.83
    paper_std: 0.1
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 77
    true_value: 0.83
    true_std: 0.1
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.1
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.82
    std: 0.12
    paper_value: 0.82
    paper_std: 0.12
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 88
    true_value: 0.82
    true_std: 0.12
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.12
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.82
    std: 0.1
    paper_value: 0.82
    paper_std: 0.1
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 89
    true_value: 0.82
    true_std: 0.1
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.1
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.81
    std: 0.11
    paper_value: 0.81
    paper_std: 0.11
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 95
    true_value: 0.81
    true_std: 0.11
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.11
    is_best: false
  - model: EigenPool
    model_key: eigenpool
    model_plain: EigenPool
    value: 0.79
    std: 0.02
    paper_value: 0.79
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 115
    true_value: 0.79
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.02
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.78
    std: 0.13
    paper_value: 0.78
    paper_std: 0.13
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 120
    true_value: 0.78
    true_std: 0.13
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.13
    is_best: false
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.69
    std: 0.12
    paper_value: 0.69
    paper_std: 0.12
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 161
    true_value: 0.69
    true_std: 0.12
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.12
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
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
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.86
    sort_std: 0.018
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8583
    std: 0.0086
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
    global_rank: 3
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.8
    std: 0.02
    paper_value: 0.8
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 34
    true_value: 0.8
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.02
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.77
    std: 0.03
    paper_value: 0.77
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 38
    true_value: 0.7935
    true_std: 0.0033
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.023499999999999965
    value_note: global 0.7935 within std
    paper_rank: 52
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.7935
    sort_std: 0.0033
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 43
    true_value: 0.78
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 44
    true_value: 0.78
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.77
    std: 0.02
    paper_value: 0.77
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 53
    true_value: 0.77
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.02
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.77
    std: 0.03
    paper_value: 0.77
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 54
    true_value: 0.77
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.03
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.75
    std: 0.02
    paper_value: 0.75
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 55
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.019000000000000017
    value_note: global 0.7690 within std
    paper_rank: 65
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.75
    std: 0.03
    paper_value: 0.75
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 66
    true_value: 0.75
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.03
    is_best: false
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.75
    std: 0.03
    paper_value: 0.75
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 67
    true_value: 0.75
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.03
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.73
    std: 0.03
    paper_value: 0.73
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 74
    true_value: 0.73
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.03
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.73
    std: 0.03
    paper_value: 0.73
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 73
    true_value: 0.73
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.03
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.73
    std: 0.03
    paper_value: 0.73
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 71
    true_value: 0.73
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.03
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.73
    std: 0.02
    paper_value: 0.73
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 72
    true_value: 0.73
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.77
    std: 0.05
    paper_value: 0.77
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 16
    true_value: 0.77
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.05
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.73
    std: 0.07
    paper_value: 0.73
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 25
    true_value: 0.7642
    true_std: 0.0039
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03420000000000001
    value_note: global 0.7642 within std
    paper_rank: 117
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.7642
    sort_std: 0.0039
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.75
    std: 0.03
    paper_value: 0.75
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 31
    true_value: 0.7625
    true_std: 0.01
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.012499999999999956
    value_note: global 0.7625 within std
    paper_rank: 67
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.7625
    sort_std: 0.01
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.76
    std: 0.04
    paper_value: 0.76
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 39
    true_value: 0.76
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.04
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.75
    std: 0.05
    paper_value: 0.75
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 70
    true_value: 0.75
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.05
    is_best: false
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.75
    std: 0.04
    paper_value: 0.75
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 72
    true_value: 0.75
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.04
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.75
    std: 0.05
    paper_value: 0.75
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 71
    true_value: 0.75
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.05
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.74
    std: 0.05
    paper_value: 0.74
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 96
    true_value: 0.74
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.05
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.74
    std: 0.05
    paper_value: 0.74
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 97
    true_value: 0.74
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.05
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.73
    std: 0.04
    paper_value: 0.73
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 118
    true_value: 0.73
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.04
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.73
    std: 0.05
    paper_value: 0.73
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 119
    true_value: 0.73
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.05
    is_best: false
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.72
    std: 0.04
    paper_value: 0.72
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 145
    true_value: 0.72
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.04
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.71
    std: 0.04
    paper_value: 0.71
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 164
    true_value: 0.71
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.04
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.255
    std: 0.001
    paper_value: 0.255
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 192
    true_value: 0.255
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 192
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.255
    sort_std: 0.001
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.262
    std: 0.006
    paper_value: 0.262
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 221
    true_value: 0.262
    true_std: 0.006
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.262
    sort_std: 0.006
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.263
    std: 0.001
    paper_value: 0.263
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 226
    true_value: 0.263
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 226
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.263
    sort_std: 0.001
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.264
    std: 0.001
    paper_value: 0.264
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 230
    true_value: 0.264
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.264
    sort_std: 0.001
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.264
    std: 0.001
    paper_value: 0.264
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 229
    true_value: 0.264
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 229
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.264
    sort_std: 0.001
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.265
    std: 0.003
    paper_value: 0.265
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 235
    true_value: 0.265
    true_std: 0.003
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 235
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.265
    sort_std: 0.003
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.266
    std: 0.0
    paper_value: 0.266
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 238
    true_value: 0.266
    true_std: 0.0
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 238
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.266
    sort_std: 0.0
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.276
    std: 0.018
    paper_value: 0.276
    paper_std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 253
    true_value: 0.276
    true_std: 0.018
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 253
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.276
    sort_std: 0.018
    is_best: false
  - model: EigenPool
    model_key: eigenpool
    model_plain: EigenPool
    value: 0.276
    std: 0.002
    paper_value: 0.276
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 254
    true_value: 0.276
    true_std: 0.002
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 254
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.276
    sort_std: 0.002
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.28
    std: 0.001
    paper_value: 0.28
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 259
    true_value: 0.28
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 259
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28
    sort_std: 0.001
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.283
    std: 0.001
    paper_value: 0.283
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 260
    true_value: 0.283
    true_std: 0.001
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 260
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.283
    sort_std: 0.001
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.295
    std: 0.007
    paper_value: 0.295
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 265
    true_value: 0.295
    true_std: 0.007
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 265
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.295
    sort_std: 0.007
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.35
    std: 0.002
    paper_value: 0.35
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 307
    true_value: 0.35
    true_std: 0.002
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 307
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
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
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.813
    std: 0.005
    paper_value: 0.813
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
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 113
    true_value: 0.813
    true_std: 0.005
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.813
    sort_std: 0.005
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.613
    std: 0.002
    paper_value: 0.613
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 169
    true_value: 0.613
    true_std: 0.002
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.613
    sort_std: 0.002
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.596
    std: 0.014
    paper_value: 0.596
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
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 170
    true_value: 0.596
    true_std: 0.014
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.596
    sort_std: 0.014
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.558
    std: 0.038
    paper_value: 0.558
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 171
    true_value: 0.558
    true_std: 0.038
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.558
    sort_std: 0.038
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.524
    std: 0.007
    paper_value: 0.524
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 172
    true_value: 0.524
    true_std: 0.007
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.524
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Reddit
  rows:
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.91
    std: 0.02
    paper_value: 0.91
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.91
    sort_std: 0.02
    is_best: true
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.91
    std: 0.02
    paper_value: 0.91
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.91
    sort_std: 0.02
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.9
    std: 0.02
    paper_value: 0.9
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.02
    is_best: true
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.9
    std: 0.01
    paper_value: 0.9
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.01
    is_best: true
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.9
    std: 0.03
    paper_value: 0.9
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.03
    is_best: true
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.9
    std: 0.02
    paper_value: 0.9
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.02
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.9
    std: 0.01
    paper_value: 0.9
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.01
    is_best: true
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.9
    std: 0.02
    paper_value: 0.9
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.9
    sort_std: 0.02
    is_best: true
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.89
    std: 0.03
    paper_value: 0.89
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.89
    sort_std: 0.03
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.88
    std: 0.02
    paper_value: 0.88
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.88
    sort_std: 0.02
    is_best: true
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
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.87
    std: 0.02
    paper_value: 0.87
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.87
    sort_std: 0.02
    is_best: true
  - model: --
    model_key: --
    model_plain: --
    value: 0.86
    std: 0.01
    paper_value: 0.86
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.86
    sort_std: 0.01
    is_best: false
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
    is_best: false
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
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.77
    std: 0.02
    paper_value: 0.77
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: null
    sort_value: 0.77
    sort_std: 0.02
    is_best: false
  metric: F1
  higher_is_better: true
- &id012
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
  - model: BNPool
    model_key: bnpool
    model_plain: BNPool
    value: 0.78
    std: 0.01
    paper_value: 0.78
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 105
    true_value: 0.78
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.01
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.77
    std: 0.01
    paper_value: 0.77
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 141
    true_value: 0.77
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.01
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.76
    std: 0.01
    paper_value: 0.76
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 163
    true_value: 0.76
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.01
    is_best: false
  - model: TopK
    model_key: topk
    model_plain: TopK
    value: 0.76
    std: 0.01
    paper_value: 0.76
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 162
    true_value: 0.76
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.01
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.75
    std: 0.0
    paper_value: 0.75
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 187
    true_value: 0.75
    true_std: 0.0
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 187
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0
    is_best: false
  - model: --
    model_key: --
    model_plain: --
    value: 0.74
    std: 0.02
    paper_value: 0.74
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 192
    true_value: 0.74
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 192
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.02
    is_best: false
  - model: Graclus
    model_key: graclus
    model_plain: Graclus
    value: 0.74
    std: 0.03
    paper_value: 0.74
    paper_std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 193
    true_value: 0.74
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.03
    is_best: false
  - model: ECPool
    model_key: ecpool
    model_plain: ECPool
    value: 0.74
    std: 0.01
    paper_value: 0.74
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 194
    true_value: 0.74
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.01
    is_best: false
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.74
    std: 0.02
    paper_value: 0.74
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 195
    true_value: 0.74
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.02
    is_best: false
  - model: HOSC
    model_key: hosc
    model_plain: HOSC
    value: 0.74
    std: 0.02
    paper_value: 0.74
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 197
    true_value: 0.74
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.02
    is_best: false
  - model: EigenPool
    model_key: eigenpool
    model_plain: EigenPool
    value: 0.74
    std: 0.02
    paper_value: 0.74
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 196
    true_value: 0.74
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.02
    is_best: false
  - model: JBGNN
    model_key: jbgnn
    model_plain: JBGNN
    value: 0.73
    std: 0.02
    paper_value: 0.73
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 204
    true_value: 0.73
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.02
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7
    std: 0.04
    paper_value: 0.7
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    global_rank: 211
    true_value: 0.7
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 211
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.04
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
- benchmark: LRGB
  datasets:
  - *id005
- benchmark: TU Dortmund
  datasets:
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: OGB
  datasets:
  - *id012
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id013
main_figure: /figures/2501.09821/main_figure.png
---

