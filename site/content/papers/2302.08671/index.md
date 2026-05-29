---
title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
arxiv_id: '2302.08671'
source_url: ''
authors: []
published_date: Feb 2023
published_date_iso: 2023-02
abstract: In recent years, Graph Neural Networks (GNNs) have been popular in the graph
  classification task. Currently, shallow GNNs are more common due to the well-known
  over-smoothing problem facing deeper GNNs. However, they are sub-optimal without
  utilizing the information from distant nodes, i.e., the long-range dependencies.
  The mainstream methods in the graph classification task can extract the long-range
  dependencies either by designing the pooling operations or incorporating the higher-order
  neighbors, while they have evident drawbacks by modifying the original graph structure,
  which may result in information loss in graph structure learning. In this paper,
  by justifying the smaller influence of the over-smoothing problem in the graph classification
  task, we evoke the importance of stacking-based GNNs and then employ them to capture
  the long-range dependencies without modifying the original graph structure. To achieve
  this, two design needs are given for stacking-based GNNs, i.e., sufficient model
  depth and adaptive skip-connection schemes. By transforming the two design needs
  into designing data-specific inter-layer connections, we propose a novel approach
  with the help of neural architecture search (NAS), which is dubbed LRGNN (Long-Range
  Graph Neural Networks). Extensive experiments on five datasets show that the proposed
  LRGNN can achieve the best performance, and obtained data-specific GNNs with different
  depth and skip-connection schemes, which can better capture the long-range dependencies..
codebase_url: https://github.com/LARS-research/LRGNN
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: VRN Ensemble
    model_key: vrn ensemble
    model_plain: VRN Ensemble
    value: 0.9554
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9554
    sort_std: null
    is_best: false
  - model: MVCNN
    model_key: mvcnn
    model_plain: MVCNN
    value: 0.901
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7785
    std: 0.0353
    paper_value: 0.7785
    paper_std: 0.0353
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 20
    true_value: 0.8064
    true_std: null
    value_gap_source_arxiv: '1806.08804'
    value_gap_source_title: Hierarchical Graph Representation Learning with Differentiable
      Pooling
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.027900000000000036
    value_note: global 0.8064 within std
    paper_rank: 36
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8064
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7563
    std: 0.0295
    paper_value: 0.7563
    paper_std: 0.0295
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 33
    true_value: 0.782
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025700000000000056
    value_note: global 0.7820 within std
    paper_rank: 55
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.782
    sort_std: 0.015
    is_best: false
  - model: Full B12C1
    model_key: full b12c1
    model_plain: Full B12C1
    value: 0.7818
    std: 0.0202
    paper_value: 0.7818
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 34
    true_value: 0.7818
    true_std: 0.0202
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7818
    sort_std: 0.0202
    is_best: false
  - model: Full B8C1
    model_key: full b8c1
    model_plain: Full B8C1
    value: 0.7801
    std: 0.0369
    paper_value: 0.7801
    paper_std: 0.0369
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 36
    true_value: 0.7801
    true_std: 0.0369
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7801
    sort_std: 0.0369
    is_best: false
  - model: Diverse B12C3
    model_key: diverse b12c3
    model_plain: Diverse B12C3
    value: 0.7767
    std: 0.0335
    paper_value: 0.7767
    paper_std: 0.0335
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 37
    true_value: 0.7767
    true_std: 0.0335
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7767
    sort_std: 0.0335
    is_best: false
  - model: Repeat B12C3
    model_key: repeat b12c3
    model_plain: Repeat B12C3
    value: 0.7725
    std: 0.029
    paper_value: 0.7725
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 40
    true_value: 0.7725
    true_std: 0.029
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7725
    sort_std: 0.029
    is_best: false
  - model: ResGCN
    model_key: resgcn
    model_plain: ResGCN
    value: 0.7665
    std: 0.0273
    paper_value: 0.7665
    paper_std: 0.0273
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 48
    true_value: 0.7665
    true_std: 0.0273
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7665
    sort_std: 0.0273
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7052
    std: 0.0548
    paper_value: 0.7052
    paper_std: 0.0548
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 50
    true_value: 0.7645
    true_std: 0.0097
    value_gap_source_arxiv: '1904.08082'
    value_gap_source_title: Self-Attention Graph Pooling
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05929999999999991
    value_note: ''
    paper_rank: 74
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.7645
    sort_std: 0.0097
    is_best: false
  - model: TwoHop(L4)
    model_key: twohop(l4)
    model_plain: TwoHop(L4)
    value: 0.7453
    std: 0.0524
    paper_value: 0.7453
    paper_std: 0.0524
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 64
    true_value: 0.7453
    true_std: 0.0524
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7453
    sort_std: 0.0524
    is_best: false
  - model: GCNJK
    model_key: gcnjk
    model_plain: GCNJK
    value: 0.7316
    std: 0.0512
    paper_value: 0.7316
    paper_std: 0.0512
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 68
    true_value: 0.7316
    true_std: 0.0512
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7316
    sort_std: 0.0512
    is_best: false
  - model: GCNVIR(L8)
    model_key: gcnvir(l8)
    model_plain: GCNVIR(L8)
    value: 0.7198
    std: 0.0434
    paper_value: 0.7198
    paper_std: 0.0434
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 73
    true_value: 0.7198
    true_std: 0.0434
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7198
    sort_std: 0.0434
    is_best: false
  - model: DGCNN(L8)
    model_key: dgcnn(l8)
    model_plain: DGCNN(L8)
    value: 0.6163
    std: 0.0533
    paper_value: 0.6163
    paper_std: 0.0533
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 79
    true_value: 0.6163
    true_std: 0.0533
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6163
    sort_std: 0.0533
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: Full B8C1
    model_key: full b8c1
    model_plain: Full B8C1
    value: 0.762
    std: 0.0518
    paper_value: 0.762
    paper_std: 0.0518
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 11
    true_value: 0.762
    true_std: 0.0518
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.0518
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.738
    std: 0.0513
    paper_value: 0.738
    paper_std: 0.0513
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 18
    true_value: 0.757
    true_std: 0.036
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.019000000000000017
    value_note: global 0.7570 within std
    paper_rank: 36
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.757
    sort_std: 0.036
    is_best: false
  - model: Full B12C1
    model_key: full b12c1
    model_plain: Full B12C1
    value: 0.745
    std: 0.0331
    paper_value: 0.745
    paper_std: 0.0331
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 28
    true_value: 0.745
    true_std: 0.0331
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.0331
    is_best: false
  - model: GCNJK
    model_key: gcnjk
    model_plain: GCNJK
    value: 0.742
    std: 0.0376
    paper_value: 0.742
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
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 31
    true_value: 0.742
    true_std: 0.0376
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0376
    is_best: false
  - model: Repeat B12C3
    model_key: repeat b12c3
    model_plain: Repeat B12C3
    value: 0.742
    std: 0.0541
    paper_value: 0.742
    paper_std: 0.0541
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 32
    true_value: 0.742
    true_std: 0.0541
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0541
    is_best: false
  - model: Diverse B12C3
    model_key: diverse b12c3
    model_plain: Diverse B12C3
    value: 0.742
    std: 0.0335
    paper_value: 0.742
    paper_std: 0.0335
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 33
    true_value: 0.742
    true_std: 0.0335
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0335
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.74
    std: 0.0574
    paper_value: 0.74
    paper_std: 0.0574
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 36
    true_value: 0.74
    true_std: 0.0574
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.0574
    is_best: false
  - model: ResGCN
    model_key: resgcn
    model_plain: ResGCN
    value: 0.737
    std: 0.057
    paper_value: 0.737
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 39
    true_value: 0.737
    true_std: 0.057
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.057
    is_best: false
  - model: GCNFA
    model_key: gcnfa
    model_plain: GCNFA
    value: 0.736
    std: 0.0562
    paper_value: 0.736
    paper_std: 0.0562
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 41
    true_value: 0.736
    true_std: 0.0562
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.0562
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.734
    std: 0.0302
    paper_value: 0.734
    paper_std: 0.0302
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 44
    true_value: 0.734
    true_std: 0.0302
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.0302
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7227
    std: 0.0447
    paper_value: 0.7227
    paper_std: 0.0447
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 45
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008700000000000041
    value_note: global 0.7314 within std
    paper_rank: 46
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7314
    sort_std: 0.007
    is_best: false
  - model: TwoHop
    model_key: twohop
    model_plain: TwoHop
    value: 0.724
    std: 0.0561
    paper_value: 0.724
    paper_std: 0.0561
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 46
    true_value: 0.724
    true_std: 0.0561
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.724
    sort_std: 0.0561
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.717
    std: 0.0365
    paper_value: 0.717
    paper_std: 0.0365
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 50
    true_value: 0.717
    true_std: 0.0365
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.0365
    is_best: false
  - model: GCNVIR
    model_key: gcnvir
    model_plain: GCNVIR
    value: 0.715
    std: 0.049
    paper_value: 0.715
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 52
    true_value: 0.715
    true_std: 0.049
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.049
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7664
    std: 0.0104
    paper_value: 0.7664
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 9
    true_value: 0.832
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06559999999999999
    value_note: ''
    paper_rank: 40
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.005
    is_best: false
  - model: Full B8C1
    model_key: full b8c1
    model_plain: Full B8C1
    value: 0.8139
    std: 0.0192
    paper_value: 0.8139
    paper_std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 19
    true_value: 0.8139
    true_std: 0.0192
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8139
    sort_std: 0.0192
    is_best: false
  - model: Diverse B12C3
    model_key: diverse b12c3
    model_plain: Diverse B12C3
    value: 0.8098
    std: 0.0196
    paper_value: 0.8098
    paper_std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 21
    true_value: 0.8098
    true_std: 0.0196
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8098
    sort_std: 0.0196
    is_best: false
  - model: Repeat B12C3
    model_key: repeat b12c3
    model_plain: Repeat B12C3
    value: 0.8079
    std: 0.0124
    paper_value: 0.8079
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 22
    true_value: 0.8079
    true_std: 0.0124
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8079
    sort_std: 0.0124
    is_best: false
  - model: Full B12C1
    model_key: full b12c1
    model_plain: Full B12C1
    value: 0.8064
    std: 0.0246
    paper_value: 0.8064
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 23
    true_value: 0.8064
    true_std: 0.0246
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8064
    sort_std: 0.0246
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.8018
    std: 0.0197
    paper_value: 0.8018
    paper_std: 0.0197
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 25
    true_value: 0.8018
    true_std: 0.0197
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8018
    sort_std: 0.0197
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7148
    std: 0.0246
    paper_value: 0.7148
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 39
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.054200000000000026
    value_note: ''
    paper_rank: 55
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: ResGCN
    model_key: resgcn
    model_plain: ResGCN
    value: 0.7671
    std: 0.0183
    paper_value: 0.7671
    paper_std: 0.0183
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 40
    true_value: 0.7671
    true_std: 0.0183
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7671
    sort_std: 0.0183
    is_best: false
  - model: TwoHop
    model_key: twohop
    model_plain: TwoHop
    value: 0.7642
    std: 0.0383
    paper_value: 0.7642
    paper_std: 0.0383
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 41
    true_value: 0.7642
    true_std: 0.0383
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0383
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.7608
    std: 0.0103
    paper_value: 0.7608
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 42
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0031999999999999806
    value_note: global 0.7640 within std
    paper_rank: 46
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: GCNFA
    model_key: gcnfa
    model_plain: GCNFA
    value: 0.7639
    std: 0.0372
    paper_value: 0.7639
    paper_std: 0.0372
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 43
    true_value: 0.7639
    true_std: 0.0372
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7639
    sort_std: 0.0372
    is_best: false
  - model: GCNJK
    model_key: gcnjk
    model_plain: GCNJK
    value: 0.7591
    std: 0.0361
    paper_value: 0.7591
    paper_std: 0.0361
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 47
    true_value: 0.7591
    true_std: 0.0361
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7591
    sort_std: 0.0361
    is_best: false
  - model: TwoHop(L4)
    model_key: twohop(l4)
    model_plain: TwoHop(L4)
    value: 0.7533
    std: 0.0215
    paper_value: 0.7533
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Morris et al. 2019
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 48
    true_value: 0.7533
    true_std: 0.0215
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7533
    sort_std: 0.0215
    is_best: false
  - model: DGCNN(L8)
    model_key: dgcnn(l8)
    model_plain: DGCNN(L8)
    value: 0.7458
    std: 0.0399
    paper_value: 0.7458
    paper_std: 0.0399
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 50
    true_value: 0.7458
    true_std: 0.0399
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7458
    sort_std: 0.0399
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.6978
    std: 0.0226
    paper_value: 0.6978
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 52
    true_value: 0.741
    true_std: 0.008
    value_gap_source_arxiv: '2201.08821'
    value_gap_source_title: Representing Long-Range Context for Graph Neural Networks
      with Global Attention
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043200000000000016
    value_note: ''
    paper_rank: 60
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.008
    is_best: false
  - model: GCNFA(L8)
    model_key: gcnfa(l8)
    model_plain: GCNFA(L8)
    value: 0.7393
    std: 0.0287
    paper_value: 0.7393
    paper_std: 0.0287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 54
    true_value: 0.7393
    true_std: 0.0287
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7393
    sort_std: 0.0287
    is_best: false
  - model: GCNVIR
    model_key: gcnvir
    model_plain: GCNVIR
    value: 0.7032
    std: 0.0432
    paper_value: 0.7032
    paper_std: 0.0432
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 56
    true_value: 0.7032
    true_std: 0.0432
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7032
    sort_std: 0.0432
    is_best: false
  - model: GCNVIR(L8)
    model_key: gcnvir(l8)
    model_plain: GCNVIR(L8)
    value: 0.6799
    std: 0.0297
    paper_value: 0.6799
    paper_std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2020
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 61
    true_value: 0.6799
    true_std: 0.0297
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6799
    sort_std: 0.0297
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7511
    std: 0.0214
    paper_value: 0.7511
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 6
    true_value: 0.781
    true_std: null
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029900000000000038
    value_note: ''
    paper_rank: 46
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.781
    sort_std: null
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7511
    std: 0.0451
    paper_value: 0.7511
    paper_std: 0.0451
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 12
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02090000000000003
    value_note: global 0.7720 within std
    paper_rank: 46
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.7395
    std: 0.0304
    paper_value: 0.7395
    paper_std: 0.0304
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 26
    true_value: 0.7626
    true_std: null
    value_gap_source_arxiv: '1905.05178'
    value_gap_source_title: Graph U-Nets
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0230999999999999
    value_note: global 0.7626 within std
    paper_rank: 59
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7626
    sort_std: null
    is_best: false
  - model: Full B8C1
    model_key: full b8c1
    model_plain: Full B8C1
    value: 0.7539
    std: 0.044
    paper_value: 0.7539
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 39
    true_value: 0.7539
    true_std: 0.044
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7539
    sort_std: 0.044
    is_best: true
  - model: TwoHop
    model_key: twohop
    model_plain: TwoHop
    value: 0.753
    std: 0.0427
    paper_value: 0.753
    paper_std: 0.0427
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 40
    true_value: 0.753
    true_std: 0.0427
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.0427
    is_best: true
  - model: Repeat B12C3
    model_key: repeat b12c3
    model_plain: Repeat B12C3
    value: 0.753
    std: 0.0477
    paper_value: 0.753
    paper_std: 0.0477
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 41
    true_value: 0.753
    true_std: 0.0477
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.0477
    is_best: true
  - model: Full B12C1
    model_key: full b12c1
    model_plain: Full B12C1
    value: 0.7529
    std: 0.0451
    paper_value: 0.7529
    paper_std: 0.0451
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 42
    true_value: 0.7529
    true_std: 0.0451
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7529
    sort_std: 0.0451
    is_best: true
  - model: GCNJK
    model_key: gcnjk
    model_plain: GCNJK
    value: 0.7524
    std: 0.0415
    paper_value: 0.7524
    paper_std: 0.0415
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 44
    true_value: 0.7524
    true_std: 0.0415
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7524
    sort_std: 0.0415
    is_best: true
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.7512
    std: 0.0489
    paper_value: 0.7512
    paper_std: 0.0489
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 46
    true_value: 0.7512
    true_std: 0.0489
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7512
    sort_std: 0.0489
    is_best: true
  - model: ResGCN
    model_key: resgcn
    model_plain: ResGCN
    value: 0.7511
    std: 0.0322
    paper_value: 0.7511
    paper_std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 47
    true_value: 0.7511
    true_std: 0.0322
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7511
    sort_std: 0.0322
    is_best: false
  - model: Diverse B12C3
    model_key: diverse b12c3
    model_plain: Diverse B12C3
    value: 0.7493
    std: 0.0515
    paper_value: 0.7493
    paper_std: 0.0515
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 54
    true_value: 0.7493
    true_std: 0.0515
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7493
    sort_std: 0.0515
    is_best: true
  - model: GCNFA
    model_key: gcnfa
    model_plain: GCNFA
    value: 0.7431
    std: 0.0416
    paper_value: 0.7431
    paper_std: 0.0416
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 58
    true_value: 0.7431
    true_std: 0.0416
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7431
    sort_std: 0.0416
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7189
    std: 0.0403
    paper_value: 0.7189
    paper_std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 68
    true_value: 0.7189
    true_std: 0.0403
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7189
    sort_std: 0.0403
    is_best: false
  - model: GCNVIR
    model_key: gcnvir
    model_plain: GCNVIR
    value: 0.7108
    std: 0.0314
    paper_value: 0.7108
    paper_std: 0.0314
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    global_rank: 72
    true_value: 0.7108
    true_std: 0.0314
    value_gap_source_arxiv: '2302.08671'
    value_gap_source_title: Search to Capture Long-range Dependency with Stacking
      GNNs for Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7108
    sort_std: 0.0314
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
main_figure: /figures/2302.08671/main_figure.png
---

