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
mrr: 0.0068
adjusted_mrr: 0.0068
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
    date: May 2018
    date_display: May 2018
    date_iso: 2018-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.88
    sort_std: null
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
    global_rank: 26
    true_value: 0.8028
    true_std: 0.0057
    value_gap_source_arxiv: '2402.15183'
    value_gap_source_title: 'GraphEdit: Large Language Models for Graph Structure
      Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07279999999999998
    value_note: ''
    paper_rank: 302
    rank_delta: 276
    rank_delta_abs: 276
    rank_delta_direction: worse
    sort_value: 0.8028
    sort_std: 0.0057
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
    global_rank: 86
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
    paper_rank: 135
    rank_delta: 49
    rank_delta_abs: 49
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
    global_rank: 107
    true_value: 0.762
    true_std: 0.004
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.004
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
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
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
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
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
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.946
    sort_std: 0.007
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
    global_rank: 71
    true_value: 0.8856
    true_std: 0.0101
    value_gap_source_arxiv: '2410.12096'
    value_gap_source_title: Bridging Large Language Models and Graph Structure Learning
      Models for Robust Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05160000000000009
    value_note: ''
    paper_rank: 369
    rank_delta: 298
    rank_delta_abs: 298
    rank_delta_direction: worse
    sort_value: 0.8856
    sort_std: 0.0101
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
    global_rank: 170
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
    paper_rank: 294
    rank_delta: 124
    rank_delta_abs: 124
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
    global_rank: 237
    true_value: 0.851
    true_std: 0.007
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 237
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
- &id003
  dataset: PubMed
  rows:
  - model: AIO
    model_key: aio
    model_plain: AIO
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.96
    std: 0.001
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
    global_rank: 2
    sort_value: 0.96
    sort_std: 0.001
    is_best: false
  - model: SAGN
    model_key: sagn
    model_plain: SAGN
    value: 0.9517
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
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
    global_rank: 6
    true_value: 0.9490000000000001
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13400000000000012
    value_note: ''
    paper_rank: 311
    rank_delta: 305
    rank_delta_abs: 305
    rank_delta_direction: worse
    sort_value: 0.9490000000000001
    sort_std: null
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
    global_rank: 310
    true_value: 0.816
    true_std: 0.005
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 310
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.816
    sort_std: 0.005
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
    global_rank: 343
    true_value: 0.805
    true_std: 0.012
    value_gap_source_arxiv: '2210.13148'
    value_gap_source_title: Transformers over Directed Acyclic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 343
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

