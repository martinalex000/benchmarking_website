---
title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
arxiv_id: '2302.08671'
source_url: ''
authors: []
published_date: Feb 17, 2023
published_date_iso: '2023-02-17'
published_venue: ''
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
    date: Nov 25, 2025
    date_display: Nov 2025
    date_iso: '2025-11-25'
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: DC-GSAT
    model_key: dc-gsat
    model_plain: DC-GSAT
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DC-SMGNN
    model_key: dc-smgnn
    model_plain: DC-SMGNN
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 73
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
    paper_rank: 128
    rank_delta: 55
    rank_delta_abs: 55
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 90
    true_value: 0.7912
    true_std: 0.0307
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03490000000000004
    value_note: ''
    paper_rank: 174
    rank_delta: 84
    rank_delta_abs: 84
    rank_delta_direction: worse
    sort_value: 0.7912
    sort_std: 0.0307
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 107
    true_value: 0.787
    true_std: 0.0229
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08179999999999998
    value_note: ''
    paper_rank: 244
    rank_delta: 137
    rank_delta_abs: 137
    rank_delta_direction: worse
    sort_value: 0.787
    sort_std: 0.0229
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 119
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
    paper_rank: 119
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 126
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
    paper_rank: 126
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 129
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
    paper_rank: 129
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 140
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
    paper_rank: 140
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 159
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
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7665
    sort_std: 0.0273
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 198
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
    paper_rank: 198
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 218
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
    paper_rank: 218
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 230
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
    paper_rank: 230
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 290
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
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6163
    sort_std: 0.0533
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: IMDB-BINARY
  rows:
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 1
    true_value: 0.834
    true_std: 0.049
    value_gap_source_arxiv: '2205.12245'
    value_gap_source_title: Asynchronous Neural Networks for Learning in Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09599999999999997
    value_note: ''
    paper_rank: 100
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
    sort_value: 0.834
    sort_std: 0.049
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.83
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.83
    sort_std: 0.032
    is_best: true
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
    global_rank: 3
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
    global_rank: 4
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 21
    true_value: 0.7704
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047699999999999965
    value_note: ''
    paper_rank: 155
    rank_delta: 134
    rank_delta_abs: 134
    rank_delta_direction: worse
    sort_value: 0.7704
    sort_std: null
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 26
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
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.0518
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 59
    true_value: 0.7503
    true_std: null
    value_gap_source_arxiv: '2104.05960'
    value_gap_source_title: Hierarchical Adaptive Pooling by Capturing High-order
      Dependency for Graph Representation Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01629999999999998
    value_note: global 0.7503 within std
    paper_rank: 114
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.7503
    sort_std: null
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 72
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
    paper_rank: 72
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 81
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
    paper_rank: 81
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 82
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
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.0541
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 83
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
    paper_rank: 83
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 95
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
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.0574
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 106
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
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.057
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 110
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
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.0562
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 150
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
    paper_rank: 150
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 160
    true_value: 0.7219
    true_std: 0.0197
    value_gap_source_arxiv: '2512.04530'
    value_gap_source_title: Explainable Graph Representation Learning via Graph Pattern
      Analysis
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.7219 within std
    paper_rank: 173
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.7219
    sort_std: 0.0197
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 180
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
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.049
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: NCI1
  rows:
  - model: MSA-AU
    model_key: msa-au
    model_plain: MSA-AU
    value: 0.962
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.962
    sort_std: null
    is_best: true
  - model: MSA-AD
    model_key: msa-ad
    model_plain: MSA-AD
    value: 0.947
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.947
    sort_std: null
    is_best: false
  - model: JbDA
    model_key: jbda
    model_plain: JbDA
    value: 0.912
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.912
    sort_std: null
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 23
    true_value: 0.8365
    true_std: 0.0169
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07010000000000005
    value_note: ''
    paper_rank: 139
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.8365
    sort_std: 0.0169
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 58
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
    paper_rank: 58
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 65
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
    paper_rank: 65
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 67
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
    paper_rank: 67
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 70
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
    paper_rank: 70
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 84
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
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8018
    sort_std: 0.0197
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 121
    true_value: 0.7823
    true_std: 0.0131
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021499999999999964
    value_note: ''
    paper_rank: 150
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.7823
    sort_std: 0.0131
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 137
    true_value: 0.7713
    true_std: 0.0149
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056499999999999995
    value_note: ''
    paper_rank: 188
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.7713
    sort_std: 0.0149
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 139
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
    paper_rank: 139
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 141
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
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0383
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 142
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
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7639
    sort_std: 0.0372
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 147
    true_value: 0.763
    true_std: 0.0153
    value_gap_source_arxiv: '2102.06986'
    value_gap_source_title: How Framelets Enhance Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06520000000000004
    value_note: ''
    paper_rank: 195
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.763
    sort_std: 0.0153
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 153
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
    paper_rank: 153
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 157
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
    paper_rank: 157
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 165
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
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7458
    sort_std: 0.0399
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 171
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
    paper_rank: 171
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 191
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
    paper_rank: 191
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 204
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
    paper_rank: 204
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
  - model: HGP-SL
    model_key: hgp-sl
    model_plain: HGP-SL
    value: 0.8491
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8491
    sort_std: 0.0162
    is_best: true
  - model: rLap
    model_key: rlap
    model_plain: rLap
    value: 0.8434
    std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8434
    sort_std: 0.0403
    is_best: true
  - model: HGP-SL_DEN
    model_key: hgp-sl_den
    model_plain: HGP-SL_DEN
    value: 0.8312
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8312
    sort_std: 0.0084
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 10
    true_value: 0.8172
    true_std: 0.0219
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09830000000000005
    value_note: ''
    paper_rank: 264
    rank_delta: 254
    rank_delta_abs: 254
    rank_delta_direction: worse
    sort_value: 0.8172
    sort_std: 0.0219
    is_best: true
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 23
    true_value: 0.7999
    true_std: 0.0044
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06040000000000001
    value_note: ''
    paper_rank: 209
    rank_delta: 186
    rank_delta_abs: 186
    rank_delta_direction: worse
    sort_value: 0.7999
    sort_std: 0.0044
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 24
    true_value: 0.799
    true_std: 0.0295
    value_gap_source_arxiv: '1911.05954'
    value_gap_source_title: Hierarchical Graph Pooling with Structure Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047900000000000054
    value_note: ''
    paper_rank: 154
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.799
    sort_std: 0.0295
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 67
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
    paper_rank: 154
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.772
    sort_std: 0.015
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 138
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
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7539
    sort_std: 0.044
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 141
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
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.0427
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 142
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
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.0477
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 146
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
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7529
    sort_std: 0.0451
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 149
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
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7524
    sort_std: 0.0415
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 154
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
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7512
    sort_std: 0.0489
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 155
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
    paper_rank: 155
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 167
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
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7493
    sort_std: 0.0515
    is_best: false
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 200
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
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7431
    sort_std: 0.0416
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
    date: Feb 17, 2023
    date_display: Feb 2023
    date_iso: '2023-02-17'
    published_venue: null
    global_rank: 282
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
    paper_rank: 282
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
---

