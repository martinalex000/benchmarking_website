---
title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
  Curvature
arxiv_id: '2309.09384'
source_url: ''
authors: []
published_date: Sep 2023
published_date_iso: 2023-09
abstract: 'While Graph Neural Networks (GNNs) have been successfully leveraged for
  learning on graph-structured data across domains, several potential pitfalls have
  been described recently. Those include the inability to accurately leverage information
  encoded in long-range connections (over-squashing), as well as difficulties distinguishing
  the learned representations of nearby nodes with growing network depth (over-smoothing).
  An effective way to characterize both effects is discrete curvature: Long-range
  connections that underlie over-squashing effects have low curvature, whereas edges
  that contribute to over-smoothing have high curvature. This observation has given
  rise to rewiring techniques, which add or remove edges to mitigate over-smoothing
  and over-squashing. Several rewiring approaches utilizing graph characteristics,
  such as curvature or the spectrum of the graph Laplacian, have been proposed. However,
  existing methods, especially those based on curvature, often require expensive subroutines
  and careful hyperparameter tuning, which limits their applicability to large-scale
  graphs. Here we propose a rewiring technique based on Augmented Forman-Ricci curvature
  (AFRC), a scalable curvature notation, which can be computed in linear time. We
  prove that AFRC effectively characterizes over-smoothing and over-squashing effects
  in message-passing GNNs. We complement our theoretical results with experiments,
  which demonstrate that the proposed approach achieves state-of-the-art performance
  while significantly reducing the computational cost in comparison with other methods.
  Utilizing fundamental properties of discrete curvature, we propose effective heuristics
  for hyperparameters in curvature-based rewiring, which avoids expensive hyperparameter
  searches, further improving the scalability of the proposed approach.'
codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Classic
- TU Dortmund
- Heterophilic Graphs
- LRGB
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id006
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
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
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: true
  - model: GCN + AFR-3 (heuristic add)
    model_key: gcn + afr-3 (heuristic add)
    model_plain: GCN + AFR-3 (heuristic add)
    value: 0.133
    std: 0.021
    paper_value: 0.133
    paper_std: 0.021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_GIN_heuristic_add)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 26
    true_value: 0.133
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.133
    sort_std: 0.021
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.132
    std: 0.018
    paper_value: 0.132
    paper_std: 0.018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 27
    true_value: 0.132
    true_std: 0.018
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.132
    sort_std: 0.018
    is_best: false
  - model: GCN + BORF (heuristic add)
    model_key: gcn + borf (heuristic add)
    model_plain: GCN + BORF (heuristic add)
    value: 0.132
    std: 0.021
    paper_value: 0.132
    paper_std: 0.021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_GIN_heuristic_add)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 28
    true_value: 0.132
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.132
    sort_std: 0.021
    is_best: false
  - model: GCN + AFR-4
    model_key: gcn + afr-4
    model_plain: GCN + AFR-4
    value: 0.131
    std: 0.019
    paper_value: 0.131
    paper_std: 0.019
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 29
    true_value: 0.131
    true_std: 0.019
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.131
    sort_std: 0.019
    is_best: false
  - model: GIN + AFR-3
    model_key: gin + afr-3
    model_plain: GIN + AFR-3
    value: 0.129
    std: 0.018
    paper_value: 0.129
    paper_std: 0.018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 30
    true_value: 0.129
    true_std: 0.018
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.129
    sort_std: 0.018
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.102
    std: 0.015
    paper_value: 0.102
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 32
    true_value: 0.102
    true_std: 0.015
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.102
    sort_std: 0.015
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.093
    std: 0.014
    paper_value: 0.093
    paper_std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.093
    true_std: 0.014
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.014
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.093
    std: 0.016
    paper_value: 0.093
    paper_std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 34
    true_value: 0.093
    true_std: 0.016
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.016
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.088
    std: 0.015
    paper_value: 0.088
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 35
    true_value: 0.088
    true_std: 0.015
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.088
    sort_std: 0.015
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.085
    std: 0.01
    paper_value: 0.085
    paper_std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 36
    true_value: 0.085
    true_std: 0.01
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.01
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.078
    std: 0.004
    paper_value: 0.078
    paper_std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 38
    true_value: 0.078
    true_std: 0.004
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.078
    sort_std: 0.004
    is_best: false
  metric: F1
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.875
    std: 0.005
    paper_value: 0.875
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 29
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0028000000000000247
    value_note: global 0.8778 within std
    paper_rank: 36
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.8690000000000001
    std: 0.02
    paper_value: 0.8690000000000001
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    true_value: 0.8690000000000001
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8690000000000001
    sort_std: 0.02
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.866
    std: 0.008
    paper_value: 0.866
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 44
    true_value: 0.866
    true_std: 0.008
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.866
    sort_std: 0.008
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.8640000000000001
    std: 0.021
    paper_value: 0.8640000000000001
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 46
    true_value: 0.8640000000000001
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8640000000000001
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.792
    std: 0.006999999999999999
    paper_value: 0.792
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 50
    true_value: 0.8565
    true_std: 0.0226
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0645
    value_note: ''
    paper_rank: 84
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.8565
    sort_std: 0.0226
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.784
    std: 0.004
    paper_value: 0.784
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 90
    true_value: 0.784
    true_std: 0.004
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.004
    is_best: false
  - model: GIN + AFR-3
    model_key: gin + afr-3
    model_plain: GIN + AFR-3
    value: 0.7829999999999999
    std: 0.006
    paper_value: 0.7829999999999999
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 91
    true_value: 0.7829999999999999
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7829999999999999
    sort_std: 0.006
    is_best: false
  - model: GCN + AFR-4
    model_key: gcn + afr-4
    model_plain: GCN + AFR-4
    value: 0.7809999999999999
    std: 0.012
    paper_value: 0.7809999999999999
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 92
    true_value: 0.7809999999999999
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7809999999999999
    sort_std: 0.012
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.763
    std: 0.006
    paper_value: 0.763
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 96
    true_value: 0.763
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.006
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.757
    std: 0.009000000000000001
    paper_value: 0.757
    paper_std: 0.009000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 98
    true_value: 0.757
    true_std: 0.009000000000000001
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.009000000000000001
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.748
    std: 0.003
    paper_value: 0.748
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 105
    true_value: 0.748
    true_std: 0.003
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.748
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Cornell
  rows:
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.873
    std: 0.0453
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.873
    sort_std: 0.0453
    is_best: true
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.8649
    std: 0.0735
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8649
    sort_std: 0.0735
    is_best: true
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8568
    std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8568
    sort_std: 0.0663
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.49700000000000005
    std: 0.034
    paper_value: 0.49700000000000005
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 30
    true_value: 0.66
    true_std: null
    value_gap_source_arxiv: '1609.02907'
    value_gap_source_title: Semi-Supervised Classification with Graph Convolutional
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16299999999999998
    value_note: ''
    paper_rank: 44
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.66
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.493
    std: 0.011000000000000001
    paper_value: 0.493
    paper_std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 45
    true_value: 0.493
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.493
    sort_std: 0.011000000000000001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: MUTAG
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.939
    std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.939
    sort_std: 0.04
    is_best: true
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.9263
    std: 0.0421
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: Jan 2019
    date_display: Jan 2019
    date_iso: 2019-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9263
    sort_std: 0.0421
    is_best: true
  - model: PS
    model_key: ps
    model_plain: PS
    value: 0.926
    std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.926
    sort_std: 0.042
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.734
    std: 0.024
    paper_value: 0.734
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 9
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16000000000000003
    value_note: ''
    paper_rank: 61
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.714
    std: 0.022
    paper_value: 0.714
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 49
    true_value: 0.825
    true_std: 0.021
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11099999999999999
    value_note: ''
    paper_rank: 63
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.825
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: PascalVOC-SP
  rows:
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
    global_rank: 1
    sort_value: 0.4561
    sort_std: 0.0039
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.4352
    std: 0.003
    metric: F1
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
    global_rank: 2
    sort_value: 0.4352
    sort_std: 0.003
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.4191
    std: 0.0126
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
    global_rank: 3
    sort_value: 0.4191
    sort_std: 0.0126
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.163
    std: 0.021
    paper_value: 0.163
    paper_std: 0.021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 29
    true_value: 0.163
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.163
    sort_std: 0.021
    is_best: false
  - model: GIN + AFR-3
    model_key: gin + afr-3
    model_plain: GIN + AFR-3
    value: 0.162
    std: 0.02
    paper_value: 0.162
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 30
    true_value: 0.162
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.162
    sort_std: 0.02
    is_best: false
  - model: GCN + AFR-3 (heuristic add)
    model_key: gcn + afr-3 (heuristic add)
    model_plain: GCN + AFR-3 (heuristic add)
    value: 0.161
    std: 0.015
    paper_value: 0.161
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_GIN_graph_heur)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 31
    true_value: 0.161
    true_std: 0.015
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.161
    sort_std: 0.015
    is_best: false
  - model: GCN + AFR-4
    model_key: gcn + afr-4
    model_plain: GCN + AFR-4
    value: 0.159
    std: 0.019
    paper_value: 0.159
    paper_std: 0.019
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 32
    true_value: 0.159
    true_std: 0.019
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.159
    sort_std: 0.019
    is_best: false
  - model: GCN + BORF (heuristic add)
    model_key: gcn + borf (heuristic add)
    model_plain: GCN + BORF (heuristic add)
    value: 0.159
    std: 0.015
    paper_value: 0.159
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_GIN_graph_heur)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.159
    true_std: 0.015
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.159
    sort_std: 0.015
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.144
    std: 0.017
    paper_value: 0.144
    paper_std: 0.017
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 34
    true_value: 0.144
    true_std: 0.017
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.144
    sort_std: 0.017
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.138
    std: 0.013
    paper_value: 0.138
    paper_std: 0.013
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 35
    true_value: 0.138
    true_std: 0.013
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.138
    sort_std: 0.013
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.123
    std: 0.011
    paper_value: 0.123
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.123
    true_std: 0.011
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.123
    sort_std: 0.011
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.122
    std: 0.014
    paper_value: 0.122
    paper_std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GIN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 40
    true_value: 0.122
    true_std: 0.014
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.122
    sort_std: 0.014
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.117
    std: 0.009
    paper_value: 0.117
    paper_std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    true_value: 0.117
    true_std: 0.009
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.117
    sort_std: 0.009
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.104
    std: 0.006
    paper_value: 0.104
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (GCN_node_hyper)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 42
    true_value: 0.104
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.104
    sort_std: 0.006
    is_best: false
  metric: F1
  higher_is_better: true
- &id004
  dataset: Wisconsin
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.0283
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9
    sort_std: 0.0283
    is_best: true
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8941
    std: 0.0474
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8941
    sort_std: 0.0474
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8921
    std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8921
    sort_std: 0.0384
    is_best: true
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.544
    std: 0.013
    paper_value: 0.544
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    true_value: 0.544
    true_std: 0.013
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.544
    sort_std: 0.013
    is_best: false
  - model: GIN + AFR-3
    model_key: gin + afr-3
    model_plain: GIN + AFR-3
    value: 0.541
    std: 0.013
    paper_value: 0.541
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 38
    true_value: 0.541
    true_std: 0.013
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.541
    sort_std: 0.013
    is_best: false
  - model: GCN + AFR-4
    model_key: gcn + afr-4
    model_plain: GCN + AFR-4
    value: 0.539
    std: 0.012
    paper_value: 0.539
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.539
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.539
    sort_std: 0.012
    is_best: false
  - model: R-GIN + FoSR
    model_key: r-gin + fosr
    model_plain: R-GIN + FoSR
    value: 0.488
    std: 0.024
    paper_value: 0.488
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 46
    true_value: 0.488
    true_std: 0.024
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.488
    sort_std: 0.024
    is_best: false
  - model: R-GIN + SDRF
    model_key: r-gin + sdrf
    model_plain: R-GIN + SDRF
    value: 0.486
    std: 0.018
    paper_value: 0.486
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 47
    true_value: 0.486
    true_std: 0.018
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.486
    sort_std: 0.018
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.485
    std: 0.01
    paper_value: 0.485
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 48
    true_value: 0.485
    true_std: 0.01
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.485
    sort_std: 0.01
    is_best: false
  - model: R-GIN + None
    model_key: r-gin + none
    model_plain: R-GIN + None
    value: 0.485
    std: 0.021
    paper_value: 0.485
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 49
    true_value: 0.485
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.485
    sort_std: 0.021
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.471
    std: 0.01
    paper_value: 0.471
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 51
    true_value: 0.471
    true_std: 0.01
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.471
    sort_std: 0.01
    is_best: false
  - model: GCN + None
    model_key: gcn + none
    model_plain: GCN + None
    value: 0.446
    std: 0.029
    paper_value: 0.446
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 55
    true_value: 0.446
    true_std: 0.029
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.446
    sort_std: 0.029
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
- benchmark: Heterophilic Graphs
  datasets:
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
main_figure: /figures/2309.09384/main_figure.png
---

