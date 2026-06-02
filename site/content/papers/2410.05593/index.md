---
title: When Graph Neural Networks Meet Dynamic Mode Decomposition
arxiv_id: '2410.05593'
source_url: ''
authors: []
published_date: Oct 8, 2024
published_date_iso: '2024-10-08'
published_venue: ''
abstract: Graph Neural Networks (GNNs) have emerged as fundamental tools for a wide
  range of prediction tasks on graph-structured data. Recent studies have drawn analogies
  between GNN feature propagation and diffusion processes, which can be interpreted
  as dynamical systems. In this paper, we delve deeper into this perspective by connecting
  the dynamics in GNNs to modern Koopman theory and its numerical method, Dynamic
  Mode Decomposition (DMD). We illustrate how DMD can estimate a low-rank, finite-dimensional
  linear operator based on multiple states of the system, effectively approximating
  potential nonlinear interactions between nodes in the graph. This approach allows
  us to capture complex dynamics within the graph accurately and efficiently. We theoretically
  establish a connection between the DMD-estimated operator and the original dynamic
  operator between system states. Building upon this foundation, we introduce a family
  of DMD-GNN models that effectively leverage the low-rank eigenfunctions provided
  by the DMD algorithm. We further discuss the potential of enhancing our approach
  by incorporating domain-specific constraints such as symmetry into the DMD computation,
  allowing the corresponding GNN models to respect known physical properties of the
  underlying system. Our work paves the path for applying advanced dynamical system
  analysis tools via GNNs. We validate our approach through extensive experiments
  on various learning tasks, including directed graphs, large-scale graphs, long-range
  interactions, and spatial-temporal graphs. We also empirically verify that our proposed
  models can serve as powerful encoders for link prediction tasks. The results demonstrate
  that our DMD-enhanced GNNs achieve state-of-the-art performance, highlighting the
  effectiveness of integrating DMD into GNN frameworks.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- DMD++
mrr: 0.1322
adjusted_mrr: 0.1322
mrr_dataset_count: 9
benchmark_categories:
- Classic
- Heterophilic Graphs
- OGB
- LRGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id009
  dataset: COCO-SP
  rows:
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.4483
    std: 0.0071
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 11, 2025
    date_display: Nov 2025
    date_iso: '2025-11-11'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4483
    sort_std: 0.0071
    is_best: true
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.4387
    std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 11, 2025
    date_display: Nov 2025
    date_iso: '2025-11-11'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4387
    sort_std: 0.0054
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.4382
    std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 11, 2025
    date_display: Nov 2025
    date_iso: '2025-11-11'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: true
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.091
    std: 0.009
    paper_value: 0.091
    paper_std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 39
    true_value: 0.091
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.091
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.079
    std: 0.025
    paper_value: 0.079
    paper_std: 0.025
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 42
    true_value: 0.0841
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005099999999999993
    value_note: global 0.0841 within std
    paper_rank: 44
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.0841
    sort_std: 0.001
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.083
    std: 0.012
    paper_value: 0.083
    paper_std: 0.012
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 43
    true_value: 0.083
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.083
    sort_std: 0.012
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.081
    std: 0.015
    paper_value: 0.081
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 44
    true_value: 0.081
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.081
    sort_std: 0.015
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.056
    std: 0.011
    paper_value: 0.056
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 46
    true_value: 0.056
    true_std: 0.011
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.056
    sort_std: 0.011
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.044
    std: 0.015
    paper_value: 0.044
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 47
    true_value: 0.044
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.015
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.031
    std: 0.016
    paper_value: 0.031
    paper_std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 48
    true_value: 0.031
    true_std: 0.016
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.031
    sort_std: 0.016
    is_best: false
  metric: F1
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
    value: 0.709
    std: 0.005
    paper_value: 0.709
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 3
    true_value: 0.88
    true_std: null
    value_gap_source_arxiv: '1805.07984'
    value_gap_source_title: Adversarial Attacks on Neural Networks for Graph Data
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17100000000000004
    value_note: ''
    paper_rank: 447
    rank_delta: 444
    rank_delta_abs: 444
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: null
    is_best: false
  - model: AdaptKry
    model_key: adaptkry
    model_plain: AdaptKry
    value: 0.8378
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8378
    sort_std: 0.0038
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.72
    std: 0.007
    paper_value: 0.72
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 8
    true_value: 0.8227
    true_std: 0.0068
    value_gap_source_arxiv: '2411.17676'
    value_gap_source_title: Instance-Aware Graph Prompt Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10270000000000001
    value_note: ''
    paper_rank: 364
    rank_delta: 356
    rank_delta_abs: 356
    rank_delta_direction: worse
    sort_value: 0.8227
    sort_std: 0.0068
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.759
    std: 0.012
    paper_value: 0.759
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 24
    true_value: 0.8033
    true_std: 0.0009
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.044300000000000006
    value_note: ''
    paper_rank: 120
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.8033
    sort_std: 0.0009
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.759
    std: 0.006
    paper_value: 0.759
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 36
    true_value: 0.7933
    true_std: 0.0084
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0343
    value_note: ''
    paper_rank: 120
    rank_delta: 84
    rank_delta_abs: 84
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0084
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.731
    std: 0.004
    paper_value: 0.731
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 66
    true_value: 0.7711
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040100000000000025
    value_note: ''
    paper_rank: 290
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7711
    sort_std: null
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.708
    std: 0.011
    paper_value: 0.708
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 96
    true_value: 0.7646
    true_std: 0.0177
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056599999999999984
    value_note: ''
    paper_rank: 455
    rank_delta: 359
    rank_delta_abs: 359
    rank_delta_direction: worse
    sort_value: 0.7646
    sort_std: 0.0177
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.591
    std: 0.005
    paper_value: 0.591
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 109
    true_value: 0.7618
    true_std: 0.007
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17080000000000006
    value_note: ''
    paper_rank: 706
    rank_delta: 597
    rank_delta_abs: 597
    rank_delta_direction: worse
    sort_value: 0.7618
    sort_std: 0.007
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.732
    std: 0.004
    paper_value: 0.732
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 282
    true_value: 0.732
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 282
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.004
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.672
    std: 0.01
    paper_value: 0.672
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 300
    true_value: 0.7303
    true_std: 0.0005
    value_gap_source_arxiv: '2407.11025'
    value_gap_source_title: Backdoor Graph Condensation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05829999999999991
    value_note: ''
    paper_rank: 581
    rank_delta: 281
    rank_delta_abs: 281
    rank_delta_direction: worse
    sort_value: 0.7303
    sort_std: 0.0005
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.73
    std: 0.021
    paper_value: 0.73
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 303
    true_value: 0.73
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 303
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.021
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.726
    std: 0.008
    paper_value: 0.726
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 336
    true_value: 0.726
    true_std: 0.008
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 336
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.008
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.714
    std: 0.026
    paper_value: 0.714
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 399
    true_value: 0.714
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 399
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.026
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.71
    std: 0.006
    paper_value: 0.71
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 439
    true_value: 0.71
    true_std: 0.006
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 439
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.006
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.005
    paper_value: 0.815
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 22
    true_value: 0.9004
    true_std: null
    value_gap_source_arxiv: '2401.09125'
    value_gap_source_title: arXiv:2401.09125
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08540000000000003
    value_note: ''
    paper_rank: 508
    rank_delta: 486
    rank_delta_abs: 486
    rank_delta_direction: worse
    sort_value: 0.9004
    sort_std: null
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.838
    std: 0.009
    paper_value: 0.838
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 40
    true_value: 0.8929
    true_std: 0.0036
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05490000000000006
    value_note: ''
    paper_rank: 316
    rank_delta: 276
    rank_delta_abs: 276
    rank_delta_direction: worse
    sort_value: 0.8929
    sort_std: 0.0036
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.835
    std: 0.007
    paper_value: 0.835
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 50
    true_value: 0.8904
    true_std: 0.015
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055400000000000005
    value_note: ''
    paper_rank: 354
    rank_delta: 304
    rank_delta_abs: 304
    rank_delta_direction: worse
    sort_value: 0.8904
    sort_std: 0.015
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.83
    std: 0.007
    paper_value: 0.83
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 54
    true_value: 0.8897
    true_std: null
    value_gap_source_arxiv: '2605.24867'
    value_gap_source_title: 'Clustering as Reasoning: A $k$-Means Interpretation of
      Chain-of-Thought Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059700000000000086
    value_note: ''
    paper_rank: 404
    rank_delta: 350
    rank_delta_abs: 350
    rank_delta_direction: worse
    sort_value: 0.8897
    sort_std: null
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.834
    std: 0.005
    paper_value: 0.834
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 89
    true_value: 0.8829
    true_std: 0.0018
    value_gap_source_arxiv: '2506.08871'
    value_gap_source_title: Adapting to Heterophilic Graph Data with Structure-Guided
      Neighbor Discovery
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048900000000000055
    value_note: ''
    paper_rank: 369
    rank_delta: 280
    rank_delta_abs: 280
    rank_delta_direction: worse
    sort_value: 0.8829
    sort_std: 0.0018
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.829
    std: 0.014
    paper_value: 0.829
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 145
    true_value: 0.8736
    true_std: 0.0096
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.044600000000000084
    value_note: ''
    paper_rank: 413
    rank_delta: 268
    rank_delta_abs: 268
    rank_delta_direction: worse
    sort_value: 0.8736
    sort_std: 0.0096
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.745
    std: 0.008
    paper_value: 0.745
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 208
    true_value: 0.8573
    true_std: 0.0065
    value_gap_source_arxiv: '2401.15569'
    value_gap_source_title: Efficient Tuning and Inference for Large Language Models
      on Textual Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11229999999999996
    value_note: ''
    paper_rank: 680
    rank_delta: 472
    rank_delta_abs: 472
    rank_delta_direction: worse
    sort_value: 0.8573
    sort_std: 0.0065
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.841
    std: 0.004
    paper_value: 0.841
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 296
    true_value: 0.841
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 296
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.004
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.833
    std: 0.005
    paper_value: 0.833
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 377
    true_value: 0.833
    true_std: 0.005
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 377
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.833
    sort_std: 0.005
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.829
    std: 0.009
    paper_value: 0.829
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 414
    true_value: 0.829
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 414
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.829
    sort_std: 0.009
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.826
    std: 0.007
    paper_value: 0.826
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 438
    true_value: 0.826
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 438
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.007
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.823
    std: 0.003
    paper_value: 0.823
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 455
    true_value: 0.823
    true_std: 0.003
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 455
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.551
    std: 0.013
    paper_value: 0.551
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 601
    true_value: 0.7877
    true_std: 0.0088
    value_gap_source_arxiv: '2407.11025'
    value_gap_source_title: Backdoor Graph Condensation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2366999999999999
    value_note: ''
    paper_rank: 873
    rank_delta: 272
    rank_delta_abs: 272
    rank_delta_direction: worse
    sort_value: 0.7877
    sort_std: 0.0088
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
    paper_value: 0.914
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 2
    true_value: 0.914
    true_std: 0.017
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.914
    sort_std: 0.017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    paper_value: 0.913
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 3
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.898
    std: 0.006
    paper_value: 0.898
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 4
    true_value: 0.898
    true_std: 0.006
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.898
    sort_std: 0.006
    is_best: false
  - model: Our (GCN) vs. GCN
    model_key: our (gcn) vs. gcn
    model_plain: Our (GCN) vs. GCN
    value: 0.8919
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 18, 2022
    date_display: Jul 2022
    date_iso: '2022-07-18'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8919
    sort_std: null
    is_best: false
  - model: Our (APPNP) vs. APPNP
    model_key: our (appnp) vs. appnp
    model_plain: Our (APPNP) vs. APPNP
    value: 0.8919
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 18, 2022
    date_display: Jul 2022
    date_iso: '2022-07-18'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8919
    sort_std: null
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.881
    std: 0.024
    paper_value: 0.881
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 7
    true_value: 0.881
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.881
    sort_std: 0.024
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.851
    std: 0.064
    paper_value: 0.851
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 21
    true_value: 0.851
    true_std: 0.064
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.064
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.85
    std: 0.052
    paper_value: 0.85
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 22
    true_value: 0.85
    true_std: 0.052
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.052
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.836
    std: 0.031
    paper_value: 0.836
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 29
    true_value: 0.836
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.836
    sort_std: 0.031
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.76
    std: 0.01
    paper_value: 0.76
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 41
    true_value: 0.819
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05899999999999994
    value_note: ''
    paper_rank: 76
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.819
    sort_std: 0.054
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.8
    std: 0.019
    paper_value: 0.8
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 53
    true_value: 0.8
    true_std: 0.019
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.019
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.665
    std: 0.138
    paper_value: 0.665
    paper_std: 0.138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 57
    true_value: 0.792
    true_std: 0.063
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.127
    value_note: global 0.7920 within std
    paper_rank: 128
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.792
    sort_std: 0.063
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.756
    std: 0.032
    paper_value: 0.756
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 78
    true_value: 0.756
    true_std: 0.032
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.032
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.726
    std: 0.003
    paper_value: 0.726
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 96
    true_value: 0.726
    true_std: 0.003
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.003
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.714
    std: 0.012
    paper_value: 0.714
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 103
    true_value: 0.714
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: PascalVOC-SP
  rows:
  - model: PGMs
    model_key: pgms
    model_plain: PGMs
    value: 0.806
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.00887'
    title: Factor Graph Neural Networks
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/andre-martins/AD3
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.806
    sort_std: null
    is_best: true
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.4561
    std: 0.0039
    metric: F1
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
    sort_value: 0.4561
    sort_std: 0.0039
    is_best: false
  - model: GTs
    model_key: gts
    model_plain: GTs
    value: 0.4375
    std: 0.0029
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4375
    sort_std: 0.0029
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.243
    std: 0.014
    paper_value: 0.243
    paper_std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 31
    true_value: 0.243
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.243
    sort_std: 0.014
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.241
    std: 0.017
    paper_value: 0.241
    paper_std: 0.017
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 32
    true_value: 0.241
    true_std: 0.017
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.241
    sort_std: 0.017
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.238
    std: 0.016
    paper_value: 0.238
    paper_std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 33
    true_value: 0.238
    true_std: 0.016
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.238
    sort_std: 0.016
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.217
    std: 0.036
    paper_value: 0.217
    paper_std: 0.036
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 34
    true_value: 0.217
    true_std: 0.036
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.217
    sort_std: 0.036
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.216
    std: 0.039
    paper_value: 0.216
    paper_std: 0.039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 35
    true_value: 0.216
    true_std: 0.039
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.216
    sort_std: 0.039
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.152
    std: 0.024
    paper_value: 0.152
    paper_std: 0.024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 44
    true_value: 0.152
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.152
    sort_std: 0.024
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.114
    std: 0.023
    paper_value: 0.114
    paper_std: 0.023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 52
    true_value: 0.114
    true_std: 0.023
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.114
    sort_std: 0.023
    is_best: false
  metric: F1
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.79
    std: 0.003
    paper_value: 0.79
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 29
    true_value: 0.9296
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13959999999999995
    value_note: ''
    paper_rank: 467
    rank_delta: 438
    rank_delta_abs: 438
    rank_delta_direction: worse
    sort_value: 0.9296
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.785
    std: 0.003
    paper_value: 0.785
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 31
    true_value: 0.9233
    true_std: null
    value_gap_source_arxiv: '2402.08170'
    value_gap_source_title: arXiv:2402.08170
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13829999999999998
    value_note: ''
    paper_rank: 512
    rank_delta: 481
    rank_delta_abs: 481
    rank_delta_direction: worse
    sort_value: 0.9233
    sort_std: null
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.792
    std: 0.003
    paper_value: 0.792
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 83
    true_value: 0.8967
    true_std: 0.003
    value_gap_source_arxiv: '2411.12330'
    value_gap_source_title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10470000000000002
    value_note: ''
    paper_rank: 445
    rank_delta: 362
    rank_delta_abs: 362
    rank_delta_direction: worse
    sort_value: 0.8967
    sort_std: 0.003
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.798
    std: 0.008
    paper_value: 0.798
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 90
    true_value: 0.895
    true_std: 0.004
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09699999999999998
    value_note: ''
    paper_rank: 381
    rank_delta: 291
    rank_delta_abs: 291
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.004
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.79
    std: 0.003
    paper_value: 0.79
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 93
    true_value: 0.894
    true_std: null
    value_gap_source_arxiv: '2206.14418'
    value_gap_source_title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10399999999999998
    value_note: ''
    paper_rank: 467
    rank_delta: 374
    rank_delta_abs: 374
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: null
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.792
    std: 0.015
    paper_value: 0.792
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 113
    true_value: 0.8902
    true_std: 0.0051
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09819999999999995
    value_note: ''
    paper_rank: 445
    rank_delta: 332
    rank_delta_abs: 332
    rank_delta_direction: worse
    sort_value: 0.8902
    sort_std: 0.0051
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.714
    std: 0.004
    paper_value: 0.714
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 174
    true_value: 0.8747
    true_std: 0.0014
    value_gap_source_arxiv: '2306.07608'
    value_gap_source_title: 'Finding the Missing-half: Graph Complementary Learning
      for Homophily-prone and Heterophily-prone Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16070000000000007
    value_note: ''
    paper_rank: 653
    rank_delta: 479
    rank_delta_abs: 479
    rank_delta_direction: worse
    sort_value: 0.8747
    sort_std: 0.0014
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.812
    std: 0.015
    paper_value: 0.812
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 322
    true_value: 0.812
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 322
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.015
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.799
    std: 0.007
    paper_value: 0.799
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 375
    true_value: 0.799
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 375
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.799
    sort_std: 0.007
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.794
    std: 0.004
    paper_value: 0.794
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 417
    true_value: 0.794
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 417
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.004
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.794
    std: 0.014
    paper_value: 0.794
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 418
    true_value: 0.794
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 418
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.014
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.793
    std: 0.009
    paper_value: 0.793
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 437
    true_value: 0.793
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 437
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.009
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.768
    std: 0.006
    paper_value: 0.768
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 504
    true_value: 0.786
    true_std: 0.007
    value_gap_source_arxiv: '2306.11264'
    value_gap_source_title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph
      Topology Refinement'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018000000000000016
    value_note: ''
    paper_rank: 579
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.786
    sort_std: 0.007
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.759
    std: 0.062
    paper_value: 0.759
    paper_std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 6
    true_value: 0.9292
    true_std: 0.0061
    value_gap_source_arxiv: '2202.04139'
    value_gap_source_title: Simplified Graph Convolution with Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17020000000000002
    value_note: ''
    paper_rank: 127
    rank_delta: 121
    rank_delta_abs: 121
    rank_delta_direction: worse
    sort_value: 0.9292
    sort_std: 0.0061
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.926
    std: 0.034
    paper_value: 0.926
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 9
    true_value: 0.926
    true_std: 0.034
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.926
    sort_std: 0.034
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.923
    std: 0.007
    paper_value: 0.923
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 11
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.923
    sort_std: 0.007
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.839
    std: 0.007
    paper_value: 0.839
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 15
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2202.04139'
    value_gap_source_title: Simplified Graph Convolution with Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07280000000000009
    value_note: ''
    paper_rank: 66
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.9118
    sort_std: 0.007
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.894
    std: 0.038
    paper_value: 0.894
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 21
    true_value: 0.894
    true_std: 0.038
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.038
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.859
    std: 0.046
    paper_value: 0.859
    paper_std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 41
    true_value: 0.859
    true_std: 0.046
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.859
    sort_std: 0.046
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.842
    std: 0.026
    paper_value: 0.842
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 61
    true_value: 0.842
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.026
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.823
    std: 0.025
    paper_value: 0.823
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 77
    true_value: 0.823
    true_std: 0.025
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.025
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.814
    std: 0.035
    paper_value: 0.814
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 88
    true_value: 0.814
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.035
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.812
    std: 0.025
    paper_value: 0.812
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 90
    true_value: 0.812
    true_std: 0.025
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.025
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.788
    std: 0.009
    paper_value: 0.788
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 99
    true_value: 0.798
    true_std: 0.043
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.7980 within std
    paper_rank: 106
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.043
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.793
    std: 0.012
    paper_value: 0.793
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 104
    true_value: 0.793
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.757
    std: 0.01
    paper_value: 0.757
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 108
    true_value: 0.784
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.027000000000000024
    value_note: global 0.7840 within std
    paper_rank: 129
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.784
    sort_std: 0.054
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
    paper_value: 0.919
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 2
    true_value: 0.919
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    paper_value: 0.918
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 3
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: FMLP-O
    model_key: fmlp-o
    model_plain: FMLP-O
    value: 0.906
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.906
    sort_std: 0.0012
    is_best: false
  - model: SpatUFG
    model_key: spatufg
    model_plain: SpatUFG
    value: 0.904
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.904
    sort_std: 0.0025
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    paper_value: 0.901
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 6
    true_value: 0.901
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.899
    std: 0.03
    paper_value: 0.899
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 8
    true_value: 0.899
    true_std: 0.03
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.899
    sort_std: 0.03
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.894
    std: 0.022
    paper_value: 0.894
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 10
    true_value: 0.894
    true_std: 0.022
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.022
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.889
    std: 0.032
    paper_value: 0.889
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 12
    true_value: 0.889
    true_std: 0.032
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.032
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.886
    std: 0.021
    paper_value: 0.886
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 15
    true_value: 0.886
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.886
    sort_std: 0.021
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.879
    std: 0.042
    paper_value: 0.879
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 25
    true_value: 0.879
    true_std: 0.042
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.879
    sort_std: 0.042
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.852
    std: 0.021
    paper_value: 0.852
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 52
    true_value: 0.852
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.852
    sort_std: 0.021
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.71
    std: 0.046
    paper_value: 0.71
    paper_std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 61
    true_value: 0.843
    true_std: 0.037
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.133
    value_note: ''
    paper_rank: 137
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.843
    sort_std: 0.037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.667
    std: 0.014
    paper_value: 0.667
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 72
    true_value: 0.831
    true_std: 0.032
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16399999999999992
    value_note: ''
    paper_rank: 147
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.831
    sort_std: 0.032
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.83
    std: 0.018
    paper_value: 0.83
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 73
    true_value: 0.83
    true_std: 0.018
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.018
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.648
    std: 0.052
    paper_value: 0.648
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 109
    true_value: 0.765
    true_std: 0.044
    value_gap_source_arxiv: '2409.08676'
    value_gap_source_title: 'Redesigning graph filter-based GNNs to relax the homophily
      assumption This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11699999999999999
    value_note: ''
    paper_rank: 152
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.765
    sort_std: 0.044
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: ogbn-arxiv
  rows:
  - model: KCoT
    model_key: kcot
    model_plain: KCoT
    value: 0.7925
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.24867'
    title: 'Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought
      Graph Learning'
    date: May 24, 2026
    date_display: May 2026
    date_iso: '2026-05-24'
    codebase_url: https://github.com/Uncnbb/KCoT
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7925
    sort_std: null
    is_best: true
  - model: TAPE + SimTeG
    model_key: tape + simteg
    model_plain: TAPE + SimTeG
    value: 0.7803
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.02565'
    title: 'SimTeG: A Frustratingly ple Approach Improves xtual raph Learning'
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/vermouthdky/SimTeG
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.7803
    sort_std: 0.0007
    is_best: false
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.7751
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.19211'
    title: 'Large Language Models Meet Graph Neural Networks: A Perspective of Graph
      Mining'
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7751
    sort_std: 0.0017
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.755
    std: 0.008
    paper_value: 0.755
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 49
    true_value: 0.755
    true_std: 0.008
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.727
    std: 0.003
    paper_value: 0.727
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 57
    true_value: 0.752
    true_std: 0.0003
    value_gap_source_arxiv: '2509.14863'
    value_gap_source_title: 'Exploring the Global-to-Local Attention Scheme in Graph
      Transformers: An Empirical Study'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025000000000000022
    value_note: ''
    paper_rank: 175
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.0003
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.744
    std: 0.015
    paper_value: 0.744
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 76
    true_value: 0.744
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.744
    sort_std: 0.015
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.72
    std: 0.005
    paper_value: 0.72
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 77
    true_value: 0.7439
    true_std: null
    value_gap_source_arxiv: '2603.01385'
    value_gap_source_title: Toward Graph-Tokenizing Large Language Models with Reconstructive
      Graph Instruction Tuning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023900000000000032
    value_note: ''
    paper_rank: 210
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.7439
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.703
    std: 0.025
    paper_value: 0.703
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 86
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.039000000000000035
    value_note: ''
    paper_rank: 290
    rank_delta: 204
    rank_delta_abs: 204
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.741
    std: 0.023
    paper_value: 0.741
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 92
    true_value: 0.741
    true_std: 0.023
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.023
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.741
    std: 0.009
    paper_value: 0.741
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 93
    true_value: 0.741
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.009
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.739
    std: 0.028
    paper_value: 0.739
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 106
    true_value: 0.739
    true_std: 0.028
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.028
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.728
    std: 0.024
    paper_value: 0.728
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 166
    true_value: 0.728
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.024
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.704
    std: 0.015
    paper_value: 0.704
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
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 211
    true_value: 0.72
    true_std: 0.0
    value_gap_source_arxiv: '2511.06443'
    value_gap_source_title: How Wide and How Deep? Mitigating Over-Squashing of GNNs
      via Channel Capacity Constrained Estimation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016000000000000014
    value_note: ''
    paper_rank: 289
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.72
    sort_std: 0.0
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.706
    std: 0.016
    paper_value: 0.706
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 220
    true_value: 0.7192
    true_std: 0.0032
    value_gap_source_arxiv: '2401.15569'
    value_gap_source_title: Efficient Tuning and Inference for Large Language Models
      on Textual Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01319999999999999
    value_note: global 0.7192 within std
    paper_rank: 282
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.7192
    sort_std: 0.0032
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.719
    std: 0.002
    paper_value: 0.719
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 221
    true_value: 0.719
    true_std: 0.002
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.002
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.55
    std: 0.003
    paper_value: 0.55
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    published_venue: null
    global_rank: 356
    true_value: 0.6291
    true_std: 0.006
    value_gap_source_arxiv: '2304.10668'
    value_gap_source_title: 'Train Your Own GNN Teacher: Graph-Aware Distillation
      on Textual Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07909999999999995
    value_note: ''
    paper_rank: 391
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.6291
    sort_std: 0.006
    is_best: false
  metric: Accuracy
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
  - *id005
  - *id006
- benchmark: OGB
  datasets:
  - *id007
- benchmark: LRGB
  datasets:
  - *id008
  - *id009
single_proposed_model: DMD++
---

