---
title: Towards Dynamic Message Passing on Graphs
arxiv_id: '2410.23686'
source_url: ''
authors: []
published_date: Oct 2024
published_date_iso: 2024-10
abstract: Message passing plays a vital role in graph neural networks (GNNs) for effective
  feature learning. However, the over-reliance on input topology diminishes the efficacy
  of message passing and restricts the ability of GNNs. Despite efforts to mitigate
  the reliance, existing study encounters message-passing bottlenecks or high computational
  expense problems, which invokes the demands for flexible message passing with low
  complexity. In this paper, we propose a novel dynamic message-passing mechanism
  for GNNs. It projects graph nodes and learnable pseudo nodes into a common space
  with measurable spatial relations between them. With nodes moving in the space,
  their evolving relations facilitate flexible pathway construction for a dynamic
  message-passing process. Associating pseudo nodes to input graphs with their measured
  relations, graph nodes can communicate with each other intermediately through pseudo
  nodes under linear complexity. We further develop a GNN model named based on our
  dynamic message-passing mechanism. employs a single recurrent layer to recursively
  generate the displacements of nodes and construct optimal dynamic pathways. Evaluation
  on eighteen benchmarks demonstrates the superior performance of over popular GNNs.
  successfully scales to large-scale benchmarks and requires significantly fewer parameters
  for graph classification with the shared recurrent layer.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- nsqure~
mrr: 0.1851
adjusted_mrr: 0.1851
mrr_dataset_count: 8
benchmark_categories:
- LRGB
- TU Dortmund
- OGB
- LINKX Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
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
    paper_value: 0.8672
    paper_std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 2
    true_value: 0.8672
    true_std: 0.0162
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    paper_value: 0.8615
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun 2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.8615
    true_std: 0.001
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8615
    std: 0.001
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
    global_rank: 4
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8059
    std: 0.0027
    paper_value: 0.8059
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf 2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021100000000000008
    value_note: ''
    paper_rank: 13
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.8213
    std: 0.0043
    paper_value: 0.8213
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying 2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.8213
    true_std: 0.0043
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8213
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.821
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.821
    sort_std: 0.009
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.8128
    std: 0.0015
    paper_value: 0.8128
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.8128
    true_std: 0.0015
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8128
    sort_std: 0.0015
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.809
    std: 0.008
    paper_value: 0.809
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.809
    true_std: 0.008
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.008
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.8074
    std: 0.0054
    paper_value: 0.8074
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.8074
    true_std: 0.0054
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8074
    sort_std: 0.0054
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7819
    std: 0.0063
    paper_value: 0.7819
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu* 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02399999999999991
    value_note: ''
    paper_rank: 20
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7803
    std: 0.0031
    paper_value: 0.7803
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.7803
    true_std: 0.0031
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7803
    sort_std: 0.0031
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7758
    std: 0.0085
    paper_value: 0.7758
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.7758
    true_std: 0.0085
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7758
    sort_std: 0.0085
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7727
    std: 0.0051
    paper_value: 0.7727
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan 2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 29
    true_value: 0.7727
    true_std: 0.0051
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7727
    sort_std: 0.0051
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.739
    std: 0.017
    paper_value: 0.739
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton 2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.739
    true_std: 0.017
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.017
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.726
    std: 0.0215
    paper_value: 0.726
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert 2016
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 57
    true_value: 0.726
    true_std: 0.0215
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.0215
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
    codebase_url: ''
    uses_external_data: false
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7995
    std: 0.0246
    paper_value: 0.7995
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.7995
    true_std: 0.0246
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.7829
    std: 0.0126
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
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.7829
    sort_std: 0.0126
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.7726
    std: 0.0027
    paper_value: 0.7726
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun_AllinARow_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.7726
    true_std: 0.0027
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7726
    sort_std: 0.0027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7326
    std: 0.0046
    paper_value: 0.7326
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03639999999999999
    value_note: ''
    paper_rank: 44
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.768
    std: 0.026
    paper_value: 0.768
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang_GoingDeeperPermutationSensitive_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 13
    true_value: 0.768
    true_std: 0.026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.026
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7278
    std: 0.0086
    paper_value: 0.7278
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu*_HowPowerfulAre_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0232
    value_note: global 0.7510 within std
    paper_rank: 53
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7412
    std: 0.0056
    paper_value: 0.7412
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_StructuralEntropyGuided_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.7412
    true_std: 0.0056
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7412
    sort_std: 0.0056
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7348
    std: 0.0076
    paper_value: 0.7348
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek_AccurateLearningGraph_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 43
    true_value: 0.7348
    true_std: 0.0076
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7348
    sort_std: 0.0076
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7314
    std: 0.007
    paper_value: 0.7314
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying_HierarchicalGraphRepresentation_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7314
    sort_std: 0.007
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7255
    std: 0.0128
    paper_value: 0.7255
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee_SelfAttentionGraphPooling_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 57
    true_value: 0.7255
    true_std: 0.0128
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7255
    sort_std: 0.0128
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7206
    std: 0.0064
    paper_value: 0.7206
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan_StructPoolStructuredGraph_2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 65
    true_value: 0.7206
    true_std: 0.0064
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7206
    sort_std: 0.0064
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7158
    std: 0.0095
    paper_value: 0.7158
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao_GraphUNets_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 75
    true_value: 0.7158
    true_std: 0.0095
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7158
    sort_std: 0.0095
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.71
    std: 0.0229
    paper_value: 0.71
    paper_std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert_LearningConvolutionalNeural_2016
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 85
    true_value: 0.71
    true_std: 0.0229
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.0229
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.688
    std: 0.045
    paper_value: 0.688
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton_InductiveRepresentationLearning_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 108
    true_value: 0.688
    true_std: 0.045
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.045
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.5153
    std: 0.0065
    paper_value: 0.5153
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_StructuralEntropyGuided_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.61
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0947
    value_note: ''
    paper_rank: 24
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.5731
    std: 0.0219
    paper_value: 0.5731
    paper_std: 0.0219
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.5731
    true_std: 0.0219
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5731
    sort_std: 0.0219
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.5632
    std: 0.0018
    paper_value: 0.5632
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun_AllinARow_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.5632
    true_std: 0.0018
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.5131
    std: 0.0072
    paper_value: 0.5131
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying_HierarchicalGraphRepresentation_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04690000000000005
    value_note: ''
    paper_rank: 24
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.532
    std: 0.036
    paper_value: 0.532
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang_GoingDeeperPermutationSensitive_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.532
    true_std: 0.036
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.532
    sort_std: 0.036
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5039
    std: 0.0041
    paper_value: 0.5039
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 21
    true_value: 0.523
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019100000000000006
    value_note: ''
    paper_rank: 35
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4813
    std: 0.0136
    paper_value: 0.4813
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu*_HowPowerfulAre_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041700000000000015
    value_note: ''
    paper_rank: 63
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.5066
    std: 0.0082
    paper_value: 0.5066
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek_AccurateLearningGraph_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 34
    true_value: 0.5066
    true_std: 0.0082
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5066
    sort_std: 0.0082
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.5023
    std: 0.0044
    paper_value: 0.5023
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee_SelfAttentionGraphPooling_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 37
    true_value: 0.5023
    true_std: 0.0044
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5023
    sort_std: 0.0044
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.5023
    std: 0.0053
    paper_value: 0.5023
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan_StructPoolStructuredGraph_2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 38
    true_value: 0.5023
    true_std: 0.0053
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5023
    sort_std: 0.0053
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.4859
    std: 0.0072
    paper_value: 0.4859
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao_GraphUNets_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 59
    true_value: 0.4859
    true_std: 0.0072
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4859
    sort_std: 0.0072
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.476
    std: 0.035
    paper_value: 0.476
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton_InductiveRepresentationLearning_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 67
    true_value: 0.476
    true_std: 0.035
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: 0.035
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.4523
    std: 0.0284
    paper_value: 0.4523
    paper_std: 0.0284
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert_LearningConvolutionalNeural_2016
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 71
    true_value: 0.4523
    true_std: 0.0284
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4523
    sort_std: 0.0284
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.8352
    std: 0.0375
    paper_value: 0.8352
    paper_std: 0.0375
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.8352
    true_std: 0.0375
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8352
    sort_std: 0.0375
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8289
    std: 0.0019
    paper_value: 0.8289
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun 2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 13
    true_value: 0.8289
    true_std: 0.0019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8289
    sort_std: 0.0019
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.828
    std: 0.013
    paper_value: 0.828
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 15
    true_value: 0.828
    true_std: 0.013
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.828
    sort_std: 0.013
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7662
    std: 0.018
    paper_value: 0.7662
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu* 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.060799999999999965
    value_note: ''
    paper_rank: 57
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.017
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7629
    std: 0.0179
    paper_value: 0.7629
    paper_std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf 2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 33
    true_value: 0.802
    true_std: 0.02
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.039100000000000024
    value_note: ''
    paper_rank: 63
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.802
    sort_std: 0.02
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7935
    std: 0.0033
    paper_value: 0.7935
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 38
    true_value: 0.7935
    true_std: 0.0033
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7935
    sort_std: 0.0033
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7864
    std: 0.0153
    paper_value: 0.7864
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan 2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 40
    true_value: 0.7864
    true_std: 0.0153
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7864
    sort_std: 0.0153
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.786
    std: 0.019
    paper_value: 0.786
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert 2016
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    true_value: 0.786
    true_std: 0.019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.019
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7382
    std: 0.0217
    paper_value: 0.7382
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton 2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 47
    true_value: 0.777
    true_std: 0.015
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03880000000000006
    value_note: ''
    paper_rank: 70
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.777
    sort_std: 0.015
    is_best: false
  - model: +pseudo node
    model_key: +pseudo node
    model_plain: +pseudo node
    value: 0.7708
    std: 0.0149
    paper_value: 0.7708
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: liu 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 52
    true_value: 0.7708
    true_std: 0.0149
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7708
    sort_std: 0.0149
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7662
    std: 0.0193
    paper_value: 0.7662
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying 2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 55
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0028000000000000247
    value_note: global 0.7690 within std
    paper_rank: 57
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7635
    std: 0.0262
    paper_value: 0.7635
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek 2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 63
    true_value: 0.7635
    true_std: 0.0262
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7635
    sort_std: 0.0262
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.6745
    std: 0.0111
    paper_value: 0.6745
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 82
    true_value: 0.6745
    true_std: 0.0111
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6745
    sort_std: 0.0111
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.6702
    std: 0.0225
    paper_value: 0.6702
    paper_std: 0.0225
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao 2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 83
    true_value: 0.6702
    true_std: 0.0225
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6702
    sort_std: 0.0225
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7753
    std: 0.0178
    paper_value: 0.7753
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.7753
    true_std: 0.0178
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7753
    sort_std: 0.0178
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.7686
    std: 0.0013
    paper_value: 0.7686
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun_AllinARow_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.7686
    true_std: 0.0013
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7686
    sort_std: 0.0013
    is_best: false
  - model: PG
    model_key: pg
    model_plain: PG
    value: 0.768
    std: 0.038
    paper_value: 0.768
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang_GoingDeeperPermutationSensitive_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 20
    true_value: 0.768
    true_std: 0.038
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.038
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7642
    std: 0.0039
    paper_value: 0.7642
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_StructuralEntropyGuided_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.7642
    true_std: 0.0039
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0039
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7562
    std: 0.0517
    paper_value: 0.7562
    paper_std: 0.0517
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying_HierarchicalGraphRepresentation_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.7625
    true_std: 0.01
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006299999999999972
    value_note: global 0.7625 within std
    paper_rank: 48
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.7625
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7384
    std: 0.0446
    paper_value: 0.7384
    paper_std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu*_HowPowerfulAre_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.023600000000000065
    value_note: global 0.7620 within std
    paper_rank: 99
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7324
    std: 0.0073
    paper_value: 0.7324
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.027599999999999958
    value_note: global 0.7600 within std
    paper_rank: 110
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7348
    std: 0.0566
    paper_value: 0.7348
    paper_std: 0.0566
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hamilton_InductiveRepresentationLearning_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 43
    true_value: 0.759
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0242
    value_note: global 0.7590 within std
    paper_rank: 104
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.032
    is_best: false
  - model: StructPool
    model_key: structpool
    model_plain: StructPool
    value: 0.7516
    std: 0.0086
    paper_value: 0.7516
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yuan_StructPoolStructuredGraph_2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 59
    true_value: 0.7516
    true_std: 0.0086
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7516
    sort_std: 0.0086
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7509
    std: 0.0059
    paper_value: 0.7509
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek_AccurateLearningGraph_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 66
    true_value: 0.7509
    true_std: 0.0059
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7509
    sort_std: 0.0059
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.75
    std: 0.0251
    paper_value: 0.75
    paper_std: 0.0251
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: niepert_LearningConvolutionalNeural_2016
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.75
    true_std: 0.0251
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0251
    is_best: false
  - model: +pseudo node
    model_key: +pseudo node
    model_plain: +pseudo node
    value: 0.7411
    std: 0.0412
    paper_value: 0.7411
    paper_std: 0.0412
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: liu_BoostingGraphStructure_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 89
    true_value: 0.7411
    true_std: 0.0412
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7411
    sort_std: 0.0412
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7156
    std: 0.0149
    paper_value: 0.7156
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lee_SelfAttentionGraphPooling_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 155
    true_value: 0.7156
    true_std: 0.0149
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7156
    sort_std: 0.0149
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7048
    std: 0.0101
    paper_value: 0.7048
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gao_GraphUNets_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 174
    true_value: 0.7048
    true_std: 0.0101
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7048
    sort_std: 0.0101
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    value: 0.3496
    std: null
    paper_value: 0.3496
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3357
    std: null
    paper_value: 0.3357
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09259999999999999
    value_note: ''
    paper_rank: 289
    rank_delta: 277
    rank_delta_abs: 277
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: null
    paper_value: 0.3547
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: null
    paper_value: 0.2481
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
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
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.2512
    std: null
    paper_value: 0.2512
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 156
    true_value: 0.2512
    true_std: null
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2512
    sort_std: null
    is_best: false
  - model: Drew-GIN
    model_key: drew-gin
    model_plain: Drew-GIN
    value: 0.2536
    std: null
    paper_value: 0.2536
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 176
    true_value: 0.2536
    true_std: null
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: null
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.2545
    std: null
    paper_value: 0.2545
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 181
    true_value: 0.254
    true_std: 0.0046
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.2540 within std
    paper_rank: 187
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.254
    sort_std: 0.0046
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2545
    std: null
    paper_value: 0.2545
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 189
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3471
    std: null
    paper_value: 0.3471
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: "Table \ref{tab:app-squashing}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 300
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id009
  dataset: arxiv-year
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.6603
    std: 0.002
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
    global_rank: 1
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
    date: May 29, 2024
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
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6462
    sort_std: 0.0101
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.5869
    std: 0.0042
    paper_value: 0.5869
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.5869
    true_std: 0.0042
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5869
    sort_std: 0.0042
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.56
    std: 0.0134
    paper_value: 0.56
    paper_std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lim_LargeScaleLearning_2021
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.56
    true_std: 0.0134
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
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
    sort_std: 0.0134
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4605
    std: 0.0051
    paper_value: 0.4605
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic_GraphAttentionNetworks_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 16
    true_value: 0.5027
    true_std: 0.002
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042200000000000015
    value_note: ''
    paper_rank: 20
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.5027
    sort_std: 0.002
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
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
    source_ref: zhu_HomophilyGraphNeural_2020
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.4909
    true_std: 0.001
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4909
    sort_std: 0.001
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
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.4602
    true_std: 0.0026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
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
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4434
    std: 0.0007
    paper_value: 0.4434
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.4434
    true_std: 0.0007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4434
    sort_std: 0.0007
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3815
    std: 0.0026
    paper_value: 0.3815
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger_PredictThenPropagate_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.3815
    true_std: 0.0026
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3815
    sort_std: 0.0026
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3768
    std: 0.003
    paper_value: 0.3768
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.3768
    true_std: 0.003
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3768
    sort_std: 0.003
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.3283
    std: 0.0013
    paper_value: 0.3283
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_SimplifyingGraphConvolutional_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 36
    true_value: 0.3283
    true_std: 0.0013
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3283
    sort_std: 0.0013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7263
    std: 0.0013
    paper_value: 0.7263
    paper_std: 0.0013
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_SGFormerSimplifyingEmpowering_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    sort_value: 0.7263
    sort_std: 0.0013
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7244
    std: 0.0028
    paper_value: 0.7244
    paper_std: 0.0028
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shirzad_ExphormerSparseTransformers_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    sort_value: 0.7244
    sort_std: 0.0028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7174
    std: 0.0029
    paper_value: 0.7174
    paper_std: 0.0029
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    sort_value: 0.7174
    sort_std: 0.0029
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7001
    std: 0.0065
    paper_value: 0.7001
    paper_std: 0.0065
    metric: accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.7001
    sort_std: 0.0065
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.6779
    std: 0.0027
    paper_value: 0.6779
    paper_std: 0.0027
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_SimplifyingGraphConvolutional_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 88
    sort_value: 0.6779
    sort_std: 0.0027
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6763
    std: 0.0023
    paper_value: 0.6763
    paper_std: 0.0023
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic_GraphAttentionNetworks_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    sort_value: 0.6763
    sort_std: 0.0023
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.599
    std: 0.0042
    paper_value: 0.599
    paper_std: 0.0042
    metric: accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_NodeFormerScalableGraph_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 89
    sort_value: 0.599
    sort_std: 0.0042
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ogbn-proteins
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7463
    std: 0.0124
    paper_value: 0.7463
    paper_std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic_GraphAttentionNetworks_2018
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 1
    true_value: 0.8501
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1038
    value_note: ''
    paper_rank: 18
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.8501
    sort_std: 0.0046
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8221
    std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8221
    sort_std: 0.0032
    is_best: false
  - model: HGODE
    model_key: hgode
    model_plain: HGODE
    value: 0.8124
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8124
    sort_std: 0.0063
    is_best: false
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.8034
    std: 0.0032
    metric: ROC-AUC
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
    sort_value: 0.8034
    sort_std: 0.0032
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7953
    std: 0.0038
    paper_value: 0.7953
    paper_std: 0.0038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_SGFormerSimplifyingEmpowering_2023
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.7992
    true_std: 0.0048
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039000000000000146
    value_note: global 0.7992 within std
    paper_rank: 6
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7992
    sort_std: 0.0048
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7955
    std: 0.0079
    paper_value: 0.7955
    paper_std: 0.0079
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.7955
    true_std: 0.0079
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7955
    sort_std: 0.0079
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7745
    std: 0.0115
    paper_value: 0.7745
    paper_std: 0.0115
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_NodeFormerScalableGraph_2022
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.7786
    true_std: 0.0084
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040999999999999925
    value_note: global 0.7786 within std
    paper_rank: 15
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7786
    sort_std: 0.0084
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7251
    std: 0.0035
    paper_value: 0.7251
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf_SemiSupervisedClassificationGraph_2017
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 16
    true_value: 0.7729
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047800000000000065
    value_note: ''
    paper_rank: 20
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7729
    sort_std: 0.0046
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.7031
    std: 0.0023
    paper_value: 0.7031
    paper_std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu_SimplifyingGraphConvolutional_2019
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.7031
    true_std: 0.0023
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7031
    sort_std: 0.0023
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
- benchmark: OGB
  datasets:
  - *id007
  - *id008
- benchmark: LINKX Benchmarks
  datasets:
  - *id009
single_proposed_model: nsqure~
main_figure: /figures/2410.23686/main_figure.png
---

