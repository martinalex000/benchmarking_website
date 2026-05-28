---
title: Effects of Dropout on Performance in Long-range Graph Learning Tasks
arxiv_id: '2502.07364'
source_url: ''
authors: []
published_date: Feb 2025
published_date_iso: 2025-02
abstract: 'Message Passing Neural Networks (MPNNs) are a class of Graph Neural Networks
  (GNNs) that propagate information across the graph via local neighborhoods. The
  scheme gives rise to two key challenges: over-smoothing and over-squashing. While
  several Dropout-style algorithms, such as DropEdge and DropMessage, have successfully
  addressed over-smoothing, their impact on over-squashing remains largely unexplored.
  This represents a critical gap in the literature, as failure to mitigate over-squashing
  would make these methods unsuitable for long-range tasks -- the intended use case
  of deep MPNNs. In this work, we study the aforementioned algorithms, and closely
  related edge-dropping algorithms -- DropNode, DropAgg and DropGNN -- in the context
  of over-squashing. We present theoretical results showing that DropEdge-variants
  reduce sensitivity between distant nodes, limiting their suitability for long-range
  tasks. To address this, we introduce DropSens, a sensitivity-aware variant of DropEdge
  that explicitly controls the proportion of information lost due to edge-dropping,
  thereby increasing sensitivity to distant nodes despite dropping the same number
  of edges. Our experiments on long-range synthetic and real-world datasets confirm
  the predicted limitations of existing edge-dropping and feature-dropping methods.
  Moreover, DropSens consistently outperforms graph rewiring techniques designed to
  mitigate over-squashing, suggesting that simple, targeted modifications can substantially
  improve a model''s ability to capture long-range interactions. Our conclusions highlight
  the need to re-evaluate and re-design existing methods for training deep GNNs, with
  a renewed focus on modelling long-range interactions.'
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- DropSens
mrr: 0.0095
adjusted_mrr: 0.0032
mrr_dataset_count: 1
benchmark_categories:
- Classic
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
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
  - model: None
    model_key: none
    model_plain: None
    value: 0.8189
    std: null
    paper_value: 0.8189
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 79
    true_value: 0.866
    true_std: 0.008
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04710000000000003
    value_note: ''
    paper_rank: 144
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.866
    sort_std: 0.008
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.8276
    std: null
    paper_value: 0.8276
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 86
    true_value: 0.864
    true_std: 0.021
    value_gap_source_arxiv: '2309.09384'
    value_gap_source_title: Mitigating Over-Smoothing and Over-Squashing using Augmentations
      of Forman-Ricci Curvature
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03639999999999999
    value_note: ''
    paper_rank: 131
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.864
    sort_std: 0.021
    is_best: false
  - model: DropSens
    model_key: dropsens
    model_plain: DropSens
    value: 0.8498
    std: null
    paper_value: 0.8498
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 105
    true_value: 0.8498
    true_std: null
    value_gap_source_arxiv: '2502.07364'
    value_gap_source_title: Effects of Dropout on Performance in Long-range Graph
      Learning Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8498
    sort_std: null
    is_best: false
  - model: DIGL (PPR)
    model_key: digl (ppr)
    model_plain: DIGL (PPR)
    value: 0.8321
    std: null
    paper_value: 0.8321
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 126
    true_value: 0.8321
    true_std: null
    value_gap_source_arxiv: '2502.07364'
    value_gap_source_title: Effects of Dropout on Performance in Long-range Graph
      Learning Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8321
    sort_std: null
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.8165
    std: null
    paper_value: 0.8165
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 147
    true_value: 0.8165
    true_std: null
    value_gap_source_arxiv: '2502.07364'
    value_gap_source_title: Effects of Dropout on Performance in Long-range Graph
      Learning Tasks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8165
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
single_proposed_model: DropSens
main_figure: /figures/2502.07364/main_figure.png
---

