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
  nodes under linear complexity. We further develop a GNN model named $N^2$ based
  on our dynamic message-passing mechanism. $N^2$ employs a single recurrent layer
  to recursively generate the displacements of nodes and construct optimal dynamic
  pathways. Evaluation on eighteen benchmarks demonstrates the superior performance
  of $N^2$ over popular GNNs. $N^2$ successfully scales to large-scale benchmarks
  and requires significantly fewer parameters for graph classification with the shared
  recurrent layer.
codebase_url: https://github.com/sunjss/N2
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- novel dynamic message-passing mechanism
mrr: 0.4457
adjusted_mrr: 0.4457
mrr_dataset_count: 6
benchmark_categories:
- TU Dortmund
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id004
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 1
    true_value: 0.8672
    true_std: 0.0162
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 2
    true_value: 0.8615
    true_std: 0.001
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
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: SE2P-C3
    model_key: se2p-c3
    model_plain: SE2P-C3
    value: 0.835
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.835
    sort_std: 0.017
    is_best: true
  - model: SE2P-C2
    model_key: se2p-c2
    model_plain: SE2P-C2
    value: 0.833
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.833
    sort_std: 0.021
    is_best: true
  - model: SE2P-C4
    model_key: se2p-c4
    model_plain: SE2P-C4
    value: 0.828
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.828
    sort_std: 0.021
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.826
    true_std: 0.022
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.020100000000000007
    value_note: global 0.8260 within std
    paper_rank: 14
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.022
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
    source_ref: xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.822
    true_std: 0.021
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040099999999999913
    value_note: ''
    paper_rank: 21
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.822
    sort_std: 0.021
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.8213
    true_std: 0.0043
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
    sort_value: 0.8213
    sort_std: 0.0043
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.8128
    true_std: 0.0015
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.809
    true_std: 0.008
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 23
    true_value: 0.7758
    true_std: 0.0085
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 42
    true_value: 0.739
    true_std: 0.017
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.726
    true_std: 0.0215
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    variant_inference_reason: 'dataset: exact match'
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
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.785
    sort_std: 0.006
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
    source_ref: Sun et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.7726
    true_std: 0.0027
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
    sort_value: 0.7726
    sort_std: 0.0027
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
    source_ref: Huang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.768
    true_std: 0.026
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
    sort_value: 0.768
    sort_std: 0.026
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
    source_ref: Kipf et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.757
    true_std: 0.036
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.024399999999999977
    value_note: global 0.7570 within std
    paper_rank: 44
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.757
    sort_std: 0.036
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
    source_ref: Xu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 21
    true_value: 0.755
    true_std: 0.04
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.027200000000000002
    value_note: global 0.7550 within std
    paper_rank: 45
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.04
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
    source_ref: Wu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 34
    true_value: 0.7412
    true_std: 0.0056
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
    sort_value: 0.7412
    sort_std: 0.0056
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
    source_ref: Hamilton et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 42
    true_value: 0.735
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04700000000000004
    value_note: ''
    paper_rank: 60
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.735
    sort_std: 0.012
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
    source_ref: Baek et al.
    variant_inference_reason: 'dataset: exact match'
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
    source_ref: Lee et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 44
    true_value: 0.734
    true_std: 0.0302
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008499999999999952
    value_note: global 0.7340 within std
    paper_rank: 45
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.734
    sort_std: 0.0302
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
    source_ref: Ying et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 45
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7314
    sort_std: 0.007
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
    source_ref: Yuan et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 47
    true_value: 0.7206
    true_std: 0.0064
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
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
    source_ref: Gao et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 51
    true_value: 0.7158
    true_std: 0.0095
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
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
    source_ref: Niepert et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 55
    true_value: 0.71
    true_std: 0.0229
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.0229
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: IMDB-MULTI
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.724
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.724
    sort_std: 0.009
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.712
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.712
    sort_std: 0.011
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.705
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.705
    sort_std: 0.01
    is_best: true
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
    source_ref: xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.698
    true_std: 0.013
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21669999999999995
    value_note: ''
    paper_rank: 24
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.698
    sort_std: 0.013
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
    source_ref: hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.695
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21899999999999997
    value_note: ''
    paper_rank: 25
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.695
    sort_std: 0.012
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
    source_ref: kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.682
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17810000000000004
    value_note: ''
    paper_rank: 20
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.682
    sort_std: 0.015
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.5731
    true_std: 0.0219
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
    source_ref: sun 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.5632
    true_std: 0.0018
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
    sort_value: 0.5632
    sort_std: 0.0018
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
    source_ref: huang 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.532
    true_std: 0.036
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
    sort_value: 0.532
    sort_std: 0.036
    is_best: false
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
    source_ref: wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.5153
    true_std: 0.0065
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
    sort_value: 0.5153
    sort_std: 0.0065
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
    source_ref: ying 2018
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.5131
    true_std: 0.0072
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
    sort_value: 0.5131
    sort_std: 0.0072
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
    source_ref: baek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 20
    true_value: 0.5066
    true_std: 0.0082
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
    source_ref: lee 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 21
    true_value: 0.5023
    true_std: 0.0044
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
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
    source_ref: yuan 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.5023
    true_std: 0.0053
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
    source_ref: gao 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.4859
    true_std: 0.0072
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
    sort_value: 0.4859
    sort_std: 0.0072
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
    source_ref: niepert 2016
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 28
    true_value: 0.4523
    true_std: 0.0284
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4523
    sort_std: 0.0284
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: NCI1
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.874
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.874
    sort_std: 0.003
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.862
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.004
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.858
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.858
    sort_std: 0.005
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08479999999999999
    value_note: ''
    paper_rank: 40
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.838
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0998
    value_note: ''
    paper_rank: 54
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.006
    is_best: false
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    variant_inference_reason: 'dataset: exact match'
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.832
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06909999999999994
    value_note: ''
    paper_rank: 44
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.005
    is_best: false
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.8289
    true_std: 0.0019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.828
    true_std: 0.013
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
    sort_value: 0.828
    sort_std: 0.013
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 28
    true_value: 0.7935
    true_std: 0.0033
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.7864
    true_std: 0.0153
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.786
    true_std: 0.019
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
    sort_value: 0.786
    sort_std: 0.019
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 39
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0028000000000000247
    value_note: global 0.7690 within std
    paper_rank: 40
    rank_delta: 1
    rank_delta_abs: 1
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 44
    true_value: 0.7635
    true_std: 0.0262
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 52
    true_value: 0.741
    true_std: 0.008
    value_gap_source_arxiv: '2201.08821'
    value_gap_source_title: Representing Long-Range Context for Graph Neural Networks
      with Global Attention
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0665
    value_note: ''
    paper_rank: 61
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.008
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 62
    true_value: 0.6702
    true_std: 0.0225
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6702
    sort_std: 0.0225
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PROTEINS
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.802
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.795
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.795
    sort_std: 0.01
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.791
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.791
    sort_std: 0.011
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046600000000000086
    value_note: ''
    paper_rank: 61
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.781
    true_std: null
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.024800000000000044
    value_note: global 0.7810 within std
    paper_rank: 35
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.781
    sort_std: null
    is_best: true
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.7753
    true_std: 0.0178
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7753
    sort_std: 0.0178
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03959999999999997
    value_note: ''
    paper_rank: 64
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.772
    sort_std: 0.015
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.7686
    true_std: 0.0013
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
    sort_value: 0.7686
    sort_std: 0.0013
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.768
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03320000000000001
    value_note: global 0.7680 within std
    paper_rank: 63
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.768
    sort_std: 0.018
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 19
    true_value: 0.768
    true_std: 0.038
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.038
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.7642
    true_std: 0.0039
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
    sort_value: 0.7642
    sort_std: 0.0039
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 33
    true_value: 0.7589
    true_std: 0.0276
    value_gap_source_arxiv: '1901.00596'
    value_gap_source_title: A Comprehensive Survey on Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008900000000000019
    value_note: global 0.7589 within std
    paper_rank: 49
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.7589
    sort_std: 0.0276
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 45
    true_value: 0.7516
    true_std: 0.0086
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 48
    true_value: 0.7509
    true_std: 0.0059
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7509
    sort_std: 0.0059
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 68
    true_value: 0.7189
    true_std: 0.0403
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0032999999999999696
    value_note: global 0.7189 within std
    paper_rank: 70
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.7189
    sort_std: 0.0403
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.7048
    true_std: 0.0101
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
    sort_value: 0.7048
    sort_std: 0.0101
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    paper_value: 0.339
    paper_std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 1
    true_value: 0.339
    true_std: 0.0073
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.3139
    std: 0.0032
    paper_value: 0.3139
    paper_std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 119.529
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 2
    true_value: 0.3139
    true_std: 0.0032
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
    sort_value: 0.3139
    sort_std: 0.0032
    is_best: false
  - model: Graphormer-FLAG
    model_key: graphormer-flag
    model_plain: Graphormer-FLAG
    value: 0.3139
    std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_display: Jun 2021
    date_iso: 2021-06
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3139
    sort_std: 0.0032
    is_best: false
  - model: GSO
    model_key: gso
    model_plain: GSO
    value: 0.3031
    std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_display: May 2023
    date_iso: '2023-05-10'
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.3031
    sort_std: 0.0026
    is_best: false
  - model: GINE-APPNP
    model_key: gine-appnp
    model_plain: GINE-APPNP
    value: 0.2979
    std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.1
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_display: Jun 2021
    date_iso: 2021-06
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.2979
    sort_std: 0.003
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
    params_millions: 9.745
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.2907
    true_std: 0.0028
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
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: MPNN +pseudo node
    model_key: mpnn +pseudo node
    model_plain: MPNN +pseudo node
    value: 0.2848
    std: 0.0026
    paper_value: 0.2848
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cai 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.2848
    true_std: 0.0026
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
    sort_value: 0.2848
    sort_std: 0.0026
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2765
    std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 5.885
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.2765
    true_std: 0.0042
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
    sort_value: 0.2765
    sort_std: 0.0042
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.2761
    std: 0.0029
    paper_value: 0.2761
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cai 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 23
    true_value: 0.2761
    true_std: 0.0029
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2761
    sort_std: 0.0029
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2266
    std: 0.0028
    paper_value: 0.2266
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04369999999999999
    value_note: ''
    paper_rank: 42
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN +pseudo node
    model_key: gcn +pseudo node
    model_plain: GCN +pseudo node
    value: 0.2703
    std: 0.0023
    paper_value: 0.2703
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.2703
    true_std: 0.0023
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
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.202
    std: 0.0024
    paper_value: 0.202
    paper_std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04039999999999999
    value_note: ''
    paper_rank: 43
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: OGB
  datasets:
  - *id006
single_proposed_model: novel dynamic message-passing mechanism
main_figure: /figures/2410.23686/main_figure.png
---

