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
  searches, further improving the scalability of the proposed approach. Code available
  at https://github.com/Weber-GeoML/AFRC_Rewiring'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN + BORF
- AFR-3
- AFR-4
- GCN (AFR-3)
- GIN (AFR-4)
- GCN with AFR-3
- GCN with BORF
- GIN with AFR-4
mrr: 0.0138
adjusted_mrr: 0.0138
mrr_dataset_count: 3
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
- Heterogeneous Graph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id009
  dataset: COCO-SP
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.4901
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4901
    sort_std: null
    is_best: true
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.4752
    std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4752
    sort_std: 0.0032
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.101
    std: 0.012
    paper_value: 0.101
    paper_std: 0.012
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 71
    true_value: 0.101
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.012
    is_best: false
  - model: AFR-3
    model_key: afr-3
    model_plain: AFR-3
    value: 0.101
    std: 0.011
    paper_value: 0.101
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 70
    true_value: 0.101
    true_std: 0.011
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.011
    is_best: false
  - model: AFR-4
    model_key: afr-4
    model_plain: AFR-4
    value: 0.098
    std: 0.011
    paper_value: 0.098
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 72
    true_value: 0.098
    true_std: 0.011
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.098
    sort_std: 0.011
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 73
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
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.014
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 76
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
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.01
    is_best: false
  - model: None
    model_key: none
    model_plain: None
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 79
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
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.078
    sort_std: 0.004
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: true
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.671
    std: 0.021
    paper_value: 0.671
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    true_value: 0.671
    true_std: 0.021
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
    sort_value: 0.671
    sort_std: 0.021
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.663
    std: 0.022
    paper_value: 0.663
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 38
    true_value: 0.663
    true_std: 0.022
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
    sort_value: 0.663
    sort_std: 0.022
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.659
    std: 0.022
    paper_value: 0.659
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 40
    true_value: 0.659
    true_std: 0.022
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
    sort_value: 0.659
    sort_std: 0.022
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.595
    std: 0.004
    paper_value: 0.595
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 71
    true_value: 0.595
    true_std: 0.004
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.004
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.593
    std: 0.019
    paper_value: 0.593
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 74
    true_value: 0.593
    true_std: 0.019
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.593
    sort_std: 0.019
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.591
    std: 0.014
    paper_value: 0.591
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 76
    true_value: 0.591
    true_std: 0.014
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.591
    sort_std: 0.014
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.588
    std: 0.023
    paper_value: 0.588
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 77
    true_value: 0.588
    true_std: 0.023
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.588
    sort_std: 0.023
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.587
    std: 0.023
    paper_value: 0.587
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 78
    true_value: 0.587
    true_std: 0.023
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.587
    sort_std: 0.023
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.571
    std: 0.022
    paper_value: 0.571
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 83
    true_value: 0.571
    true_std: 0.022
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.571
    sort_std: 0.022
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
  - model: AFR-3
    model_key: afr-3
    model_plain: AFR-3
    value: 0.7440000000000001
    std: 0.01
    paper_value: 0.7440000000000001
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 98
    true_value: 0.7440000000000001
    true_std: 0.01
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
    sort_value: 0.7440000000000001
    sort_std: 0.01
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.7340000000000001
    std: 0.006
    paper_value: 0.7340000000000001
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 102
    true_value: 0.738
    true_std: 0.002
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039999999999998925
    value_note: global 0.7380 within std
    paper_rank: 106
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.738
    sort_std: 0.002
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.735
    std: 0.02
    paper_value: 0.735
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 106
    true_value: 0.735
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.02
    is_best: false
  - model: AFR-4
    model_key: afr-4
    model_plain: AFR-4
    value: 0.733
    std: 0.006
    paper_value: 0.733
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 108
    true_value: 0.733
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.006
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.726
    std: 0.022000000000000002
    paper_value: 0.726
    paper_std: 0.022000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 113
    true_value: 0.726
    true_std: 0.003
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.003
    is_best: false
  - model: None
    model_key: none
    model_plain: None
    value: 0.7170000000000001
    std: 0.006999999999999999
    paper_value: 0.7170000000000001
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 123
    true_value: 0.7170000000000001
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7170000000000001
    sort_std: 0.006999999999999999
    is_best: false
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.6509999999999999
    std: 0.006999999999999999
    paper_value: 0.6509999999999999
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 169
    true_value: 0.6509999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6509999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.647
    std: 0.006
    paper_value: 0.647
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 170
    true_value: 0.647
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.647
    sort_std: 0.006
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.6459999999999999
    std: 0.006
    paper_value: 0.6459999999999999
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 171
    true_value: 0.6459999999999999
    true_std: 0.006
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
    sort_value: 0.6459999999999999
    sort_std: 0.006
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.616
    std: 0.006999999999999999
    paper_value: 0.616
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 188
    true_value: 0.616
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.616
    sort_std: 0.006999999999999999
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.606
    std: 0.008
    paper_value: 0.606
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 191
    true_value: 0.606
    true_std: 0.008
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.008
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.599
    std: 0.006
    paper_value: 0.599
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 202
    true_value: 0.599
    true_std: 0.006
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.599
    sort_std: 0.006
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
  - model: AFR-4
    model_key: afr-4
    model_plain: AFR-4
    value: 0.881
    std: 0.005
    paper_value: 0.881
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 36
    true_value: 0.881
    true_std: 0.005
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
    sort_value: 0.881
    sort_std: 0.005
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.869
    std: 0.02
    paper_value: 0.869
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 43
    true_value: 0.8794
    true_std: 0.0026
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010399999999999965
    value_note: global 0.8794 within std
    paper_rank: 71
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.8794
    sort_std: 0.0026
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.879
    std: 0.007
    paper_value: 0.879
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 44
    true_value: 0.879
    true_std: 0.007
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
    sort_value: 0.879
    sort_std: 0.007
    is_best: false
  - model: AFR-3
    model_key: afr-3
    model_plain: AFR-3
    value: 0.875
    std: 0.005
    paper_value: 0.875
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 59
    true_value: 0.875
    true_std: 0.005
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.875
    sort_std: 0.005
    is_best: false
  - model: None
    model_key: none
    model_plain: None
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
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 79
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
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.866
    sort_std: 0.008
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.864
    std: 0.021
    paper_value: 0.864
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 86
    true_value: 0.864
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.864
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.519
    std: 0.042
    paper_value: 0.519
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 124
    true_value: 0.519
    true_std: 0.042
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.519
    sort_std: 0.042
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.484
    std: 0.025
    paper_value: 0.484
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 129
    true_value: 0.484
    true_std: 0.025
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.484
    sort_std: 0.025
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.473
    std: 0.023
    paper_value: 0.473
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 134
    true_value: 0.473
    true_std: 0.023
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.473
    sort_std: 0.023
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.468
    std: 0.03
    paper_value: 0.468
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 135
    true_value: 0.468
    true_std: 0.03
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.468
    sort_std: 0.03
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.439
    std: 0.011
    paper_value: 0.439
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 143
    true_value: 0.439
    true_std: 0.011
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.439
    sort_std: 0.011
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.431
    std: 0.012
    paper_value: 0.431
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 144
    true_value: 0.431
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.431
    sort_std: 0.012
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.404
    std: 0.02
    paper_value: 0.404
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 145
    true_value: 0.404
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.404
    sort_std: 0.02
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.364
    std: 0.023
    paper_value: 0.364
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 147
    true_value: 0.364
    true_std: 0.023
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.364
    sort_std: 0.023
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.361
    std: 0.024
    paper_value: 0.361
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 148
    true_value: 0.361
    true_std: 0.024
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.361
    sort_std: 0.024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
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
  - model: GCN with AFR-3
    model_key: gcn with afr-3
    model_plain: GCN with AFR-3
    value: 0.376
    std: 0.012
    paper_value: 0.376
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 57
    true_value: 0.376
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.376
    sort_std: 0.012
    is_best: false
  - model: GIN with AFR-4
    model_key: gin with afr-4
    model_plain: GIN with AFR-4
    value: 0.321
    std: 0.014
    paper_value: 0.321
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 77
    true_value: 0.321
    true_std: 0.014
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.321
    sort_std: 0.014
    is_best: false
  - model: GCN with BORF
    model_key: gcn with borf
    model_plain: GCN with BORF
    value: 0.319
    std: 0.012
    paper_value: 0.319
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 78
    true_value: 0.319
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.319
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: IMDB
  rows:
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.7308
    std: 0.0124
    metric: Micro-F1
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
    sort_value: 0.7308
    sort_std: 0.0124
    is_best: true
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.7205
    std: 0.0115
    metric: Micro-F1
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
    sort_value: 0.7205
    sort_std: 0.0115
    is_best: true
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.7148
    std: 0.0103
    metric: Micro-F1
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
    sort_value: 0.7148
    sort_std: 0.0103
    is_best: true
  - model: GCN with AFR-3
    model_key: gcn with afr-3
    model_plain: GCN with AFR-3
    value: 0.689
    std: 0.011
    paper_value: 0.689
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.689
    sort_std: 0.011
    is_best: false
  - model: GIN with AFR-4
    model_key: gin with afr-4
    model_plain: GIN with AFR-4
    value: 0.678
    std: 0.012
    paper_value: 0.678
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.678
    sort_std: 0.012
    is_best: false
  - model: GCN with BORF
    model_key: gcn with borf
    model_plain: GCN with BORF
    value: 0.677
    std: 0.015
    paper_value: 0.677
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.677
    sort_std: 0.015
    is_best: false
  - model: GCN with NONE
    model_key: gcn with none
    model_plain: GCN with NONE
    value: 0.476
    std: 0.011
    paper_value: 0.476
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.476
    sort_std: 0.011
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id011
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
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.754
    std: 0.028
    paper_value: 0.754
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 42
    true_value: 0.8809999999999999
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1269999999999999
    value_note: ''
    paper_rank: 135
    rank_delta: 93
    rank_delta_abs: 93
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.027000000000000003
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.734
    std: 0.024
    paper_value: 0.734
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 145
    true_value: 0.734
    true_std: 0.024
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.024
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.627
    std: 0.021
    paper_value: 0.627
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 151
    true_value: 0.7215
    true_std: 0.024399999999999998
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09450000000000003
    value_note: ''
    paper_rank: 168
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.7215
    sort_std: 0.024399999999999998
    is_best: false
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.709
    std: 0.027
    paper_value: 0.709
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 156
    true_value: 0.709
    true_std: 0.027
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.709
    sort_std: 0.027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.723
    std: 0.012
    paper_value: 0.723
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 83
    true_value: 0.742
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019000000000000017
    value_note: ''
    paper_rank: 140
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.008
    is_best: false
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.73
    std: 0.015
    paper_value: 0.73
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 121
    true_value: 0.73
    true_std: 0.015
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.015
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.727
    std: 0.013
    paper_value: 0.727
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 130
    true_value: 0.727
    true_std: 0.013
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.013
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.596
    std: 0.009
    paper_value: 0.596
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 167
    true_value: 0.70982
    true_std: 0.00737
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11382000000000003
    value_note: ''
    paper_rank: 198
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.70982
    sort_std: 0.00737
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.593
    std: 0.008
    paper_value: 0.593
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 170
    true_value: 0.70804
    true_std: 0.00827
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11504000000000003
    value_note: ''
    paper_rank: 200
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.70804
    sort_std: 0.00827
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.144
    std: 0.014
    paper_value: 0.144
    paper_std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 105
    true_value: 0.144
    true_std: 0.014
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
    sort_value: 0.144
    sort_std: 0.014
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.141
    std: 0.011
    paper_value: 0.141
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 106
    true_value: 0.141
    true_std: 0.011
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.141
    sort_std: 0.011
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 107
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
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.138
    sort_std: 0.013
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 111
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
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.117
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 114
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
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.104
    sort_std: 0.006
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: AFR-3
    model_key: afr-3
    model_plain: AFR-3
    value: 0.448
    std: 0.028
    paper_value: 0.448
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.448
    sort_std: 0.028
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.443
    std: 0.028
    paper_value: 0.443
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 248
    sort_value: 0.443
    sort_std: 0.028
    is_best: false
  - model: AFR-4
    model_key: afr-4
    model_plain: AFR-4
    value: 0.436
    std: 0.025
    paper_value: 0.436
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.436
    sort_std: 0.025
    is_best: false
  - model: None
    model_key: none
    model_plain: None
    value: 0.405
    std: 0.021
    paper_value: 0.405
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.405
    sort_std: 0.021
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: GCN (AFR-3)
    model_key: gcn (afr-3)
    model_plain: GCN (AFR-3)
    value: 0.687
    std: 0.031
    paper_value: 0.687
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 117
    true_value: 0.687
    true_std: 0.031
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.687
    sort_std: 0.031
    is_best: false
  - model: GIN (AFR-4)
    model_key: gin (afr-4)
    model_plain: GIN (AFR-4)
    value: 0.638
    std: 0.038
    paper_value: 0.638
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 133
    true_value: 0.638
    true_std: 0.038
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.638
    sort_std: 0.038
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.623
    std: 0.02
    paper_value: 0.623
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 138
    true_value: 0.623
    true_std: 0.02
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.623
    sort_std: 0.02
    is_best: false
  - model: GIN-E
    model_key: gin-e (none)
    model_plain: GIN-E
    value: 0.538
    std: 0.03
    paper_value: 0.538
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 162
    true_value: 0.538
    true_std: 0.03
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.03
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.502
    std: 0.034
    paper_value: 0.502
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 165
    true_value: 0.502
    true_std: 0.034
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.502
    sort_std: 0.034
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.472
    std: 0.036
    paper_value: 0.472
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 167
    true_value: 0.472
    true_std: 0.036
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.472
    sort_std: 0.036
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.469
    std: 0.012
    paper_value: 0.469
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 168
    true_value: 0.469
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.469
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.441
    std: 0.005
    paper_value: 0.441
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 169
    true_value: 0.442
    true_std: 0.015
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.4420 within std
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.442
    sort_std: 0.015
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.436
    std: 0.012
    paper_value: 0.436
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 170
    true_value: 0.436
    true_std: 0.012
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.436
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
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
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 125
    true_value: 0.556
    true_std: 0.0125
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07100000000000006
    value_note: ''
    paper_rank: 136
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.556
    sort_std: 0.0125
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
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
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 126
    true_value: 0.555
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08400000000000007
    value_note: ''
    paper_rank: 138
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.555
    sort_std: 0.003
    is_best: false
  - model: BORF
    model_key: borf
    model_plain: BORF
    value: 0.465
    std: 0.026
    paper_value: 0.465
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 127
    true_value: 0.5537
    true_std: 0.0147
    value_gap_source_arxiv: '2508.19071'
    value_gap_source_title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08869999999999995
    value_note: ''
    paper_rank: 139
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.5537
    sort_std: 0.0147
    is_best: false
  - model: AFR-4
    model_key: afr-4
    model_plain: AFR-4
    value: 0.522
    std: 0.024
    paper_value: 0.522
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 134
    true_value: 0.522
    true_std: 0.024
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.522
    sort_std: 0.024
    is_best: false
  - model: AFR-3
    model_key: afr-3
    model_plain: AFR-3
    value: 0.473
    std: 0.024
    paper_value: 0.473
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 138
    true_value: 0.473
    true_std: 0.024
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.473
    sort_std: 0.024
    is_best: false
  - model: None
    model_key: none
    model_plain: None
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
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 141
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
    paper_rank: 141
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
  - *id002
- benchmark: Heterophilic Graphs
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
  - *id009
- benchmark: TU Dortmund
  datasets:
  - *id010
  - *id011
  - *id012
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id013
main_figure: /figures/2309.09384/main_figure.png
---

