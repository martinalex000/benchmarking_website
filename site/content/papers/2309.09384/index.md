---
title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
  Curvature
arxiv_id: '2309.09384'
source_url: ''
authors: []
published_date: Sep 17, 2023
published_date_iso: '2023-09-17'
published_venue: ''
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 30
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
    paper_rank: 30
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 31
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
    paper_rank: 31
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 32
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
    paper_rank: 32
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 33
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
    paper_rank: 33
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 34
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
    paper_rank: 34
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 36
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
    paper_rank: 36
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 37
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
    paper_rank: 37
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 38
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
    paper_rank: 38
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 40
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
    paper_rank: 40
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 41
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
    paper_rank: 41
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 45
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
    paper_rank: 45
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 22
    true_value: 0.9004
    true_std: null
    value_gap_source_arxiv: '2401.09125'
    value_gap_source_title: arXiv:2401.09125
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025399999999999978
    value_note: ''
    paper_rank: 137
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.9004
    sort_std: null
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 152
    true_value: 0.8705
    true_std: 0.0036
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07850000000000001
    value_note: ''
    paper_rank: 583
    rank_delta: 431
    rank_delta_abs: 431
    rank_delta_direction: worse
    sort_value: 0.8705
    sort_std: 0.0036
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 158
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
    paper_rank: 158
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 171
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
    paper_rank: 171
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 179
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
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8640000000000001
    sort_std: 0.021
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 610
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
    paper_rank: 610
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 616
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
    paper_rank: 616
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 619
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
    paper_rank: 619
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 649
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
    paper_rank: 649
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 660
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
    paper_rank: 660
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 675
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
    paper_rank: 675
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.914
    sort_std: 0.017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 57
    true_value: 0.792
    true_std: 0.063
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.295
    value_note: ''
    paper_rank: 211
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.792
    sort_std: 0.063
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 137
    true_value: 0.646
    true_std: 0.0208
    value_gap_source_arxiv: '2405.18581'
    value_gap_source_title: 'Unleashing the Potential of Text-attributed Graphs: Automatic
      Relation Decomposition via Large Language Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15300000000000002
    value_note: ''
    paper_rank: 213
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.646
    sort_std: 0.0208
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: MUTAG
  rows:
  - model: RC-Explainer
    model_key: rc-explainer
    model_plain: RC-Explainer
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_display: Apr 2022
    date_iso: 2022-04
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.983
    std: 0.025
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
    sort_value: 0.983
    sort_std: 0.025
    is_best: true
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.9805
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: Feb 2022
    date_display: Feb 2022
    date_iso: 2022-02
    codebase_url: https://github.com/chrisjtan/gnn_cff
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9805
    sort_std: null
    is_best: false
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 62
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16000000000000003
    value_note: ''
    paper_rank: 325
    rank_delta: 263
    rank_delta_abs: 263
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 109
    true_value: 0.872
    true_std: 0.0511
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15800000000000003
    value_note: ''
    paper_rank: 337
    rank_delta: 228
    rank_delta_abs: 228
    rank_delta_direction: worse
    sort_value: 0.872
    sort_std: 0.0511
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 39
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
    paper_rank: 39
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 40
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
    paper_rank: 40
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 41
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
    paper_rank: 41
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 42
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
    paper_rank: 42
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 43
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
    paper_rank: 43
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 45
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
    paper_rank: 45
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 46
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
    paper_rank: 46
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 49
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
    paper_rank: 49
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 50
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
    paper_rank: 50
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 51
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
    paper_rank: 51
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 53
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
    paper_rank: 53
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 8, 2024
    date_display: Oct 2024
    date_iso: '2024-10-08'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.031
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 205
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
    paper_rank: 205
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 207
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
    paper_rank: 207
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 208
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
    paper_rank: 208
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 230
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
    paper_rank: 230
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 231
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
    paper_rank: 231
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 232
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
    paper_rank: 232
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 233
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
    paper_rank: 233
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 238
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
    paper_rank: 238
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
    date: Sep 17, 2023
    date_display: Sep 2023
    date_iso: '2023-09-17'
    published_venue: null
    global_rank: 244
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
    paper_rank: 244
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
---

