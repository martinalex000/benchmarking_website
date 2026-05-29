---
title: Transformers over Directed Acyclic Graphs
arxiv_id: '2210.13148'
source_url: ''
authors: []
published_date: Oct 24, 2022
published_date_iso: '2022-10-24'
abstract: 'Transformer models have recently gained popularity in graph representation
  learning as they have the potential to learn complex relationships beyond the ones
  captured by regular graph neural networks. The main research question is how to
  inject the structural bias of graphs into the transformer architecture, and several
  proposals have been made for undirected molecular graphs and, recently, also for
  larger network graphs. In this paper, we study transformers over directed acyclic
  graphs (DAGs) and propose architecture adaptations tailored to DAGs: (1) An attention
  mechanism that is considerably more efficient than the regular quadratic complexity
  of transformers and at the same time faithfully captures the DAG structure, and
  (2) a positional encoding of the DAG''s partial order, complementing the former.
  We rigorously evaluate our approach over various types of tasks, ranging from classifying
  source code graphs to nodes in citation networks, and show that it is effective
  in two important aspects: in making graph transformers generally outperform graph
  neural networks tailored to DAGs and in improving SOTA graph transformer performance
  in terms of both quality and efficiency.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- DIFFormer
- DAG + DIFFORMER-a
mrr: 0.0328
adjusted_mrr: 0.0328
mrr_dataset_count: 3
benchmark_categories:
- Classic
- Other Graph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
  dataset: CiteSeer
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.8285
    std: 0.0038
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8285
    sort_std: 0.0038
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.8114
    std: 0.0034
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.757
    std: 0.003
    paper_value: 0.757
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 7
    true_value: 0.7665
    true_std: 0.0152
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009499999999999953
    value_note: global 0.7665 within std
    paper_rank: 32
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.7665
    sort_std: 0.0152
    is_best: false
  - model: DAG + DIFFORMER-a
    model_key: dag + difformer-a
    model_plain: DAG + DIFFORMER-a
    value: 0.762
    std: 0.004
    paper_value: 0.762
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 21
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.004
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.73
    std: 0.003
    paper_value: 0.73
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 34
    true_value: 0.752
    true_std: 0.0127
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02200000000000002
    value_note: ''
    paper_rank: 42
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.0127
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9171
    sort_std: 0.0029
    is_best: false
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.834
    std: 0.002
    paper_value: 0.834
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 37
    true_value: 0.8744
    true_std: 0.0137
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04039999999999999
    value_note: ''
    paper_rank: 66
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.8744
    sort_std: 0.0137
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.841
    std: 0.006
    paper_value: 0.841
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 44
    true_value: 0.8661
    true_std: 0.0304
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02510000000000001
    value_note: global 0.8661 within std
    paper_rank: 60
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8661
    sort_std: 0.0304
    is_best: false
  - model: DAG + DIFFORMER-a
    model_key: dag + difformer-a
    model_plain: DAG + DIFFORMER-a
    value: 0.851
    std: 0.007
    paper_value: 0.851
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 54
    true_value: 0.851
    true_std: 0.007
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: MalNet-Tiny
  rows:
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9422
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9422
    sort_std: 0.0024
    is_best: true
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.9406
    std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9406
    sort_std: 0.0064
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.9372
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9372
    sort_std: 0.0029
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9264
    std: 0.0078
    paper_value: 0.9264
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 11
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 4
    true_value: 0.935
    true_std: 0.0041
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008600000000000052
    value_note: ''
    paper_rank: 6
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.935
    sort_std: 0.0041
    is_best: false
  - model: DAG+GraphGPS
    model_key: dag+graphgps
    model_plain: DAG+GraphGPS
    value: 0.9345
    std: 0.0041
    paper_value: 0.9345
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 11
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 5
    true_value: 0.9345
    true_std: 0.0041
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9345
    sort_std: 0.0041
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: PubMed
  rows:
  - model: Flan-T5-large
    model_key: flan-t5-large
    model_plain: Flan-T5-large
    value: 0.9462
    std: 0.0013
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
    global_rank: 1
    sort_value: 0.9462
    sort_std: 0.0013
    is_best: true
  - model: Flan-T5-base
    model_key: flan-t5-base
    model_plain: Flan-T5-base
    value: 0.9445
    std: 0.0012
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
    global_rank: 2
    sort_value: 0.9445
    sort_std: 0.0012
    is_best: true
  - model: Llama-7b
    model_key: llama-7b
    model_plain: Llama-7b
    value: 0.9384
    std: 0.0025
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
    global_rank: 3
    sort_value: 0.9384
    sort_std: 0.0025
    is_best: false
  - model: DAG + DIFFORMER-a
    model_key: dag + difformer-a
    model_plain: DAG + DIFFORMER-a
    value: 0.816
    std: 0.005
    paper_value: 0.816
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 31
    true_value: 0.816
    true_std: 0.005
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.816
    sort_std: 0.005
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.815
    std: 0.004
    paper_value: 0.815
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 32
    true_value: 0.815
    true_std: 0.004
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.815
    sort_std: 0.004
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.805
    std: 0.012
    paper_value: 0.805
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 24, 2022
    date_display: Oct 2022
    date_iso: '2022-10-24'
    global_rank: 33
    true_value: 0.805
    true_std: 0.012
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Other Graph Benchmarks
  datasets:
  - *id004
main_figure: /figures/2210.13148/main_figure.png
---

