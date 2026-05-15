---
title: Effects of Dropout on Performance in - Long-range Graph Learning Tasks
arxiv_id: '2502.07364'
authors: []
published_date: Feb 2025
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
proposed_models:
- DropSens
mrr: 0.0093
results:
- &id001
  dataset: Cora
  rows:
  - model: GPM
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
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: TRIGON
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: DR
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: DropSens
    value: 0.8498
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: this paper
    global_rank: 107
    is_best: false
  - model: DIGL (PPR)
    value: 0.8321
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    global_rank: 128
    is_best: false
  - model: SDRF
    value: 0.8276
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    global_rank: 88
    is_best: false
  - model: None
    value: 0.8189
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    global_rank: 81
    is_best: false
  - model: FA
    value: 0.8165
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1(a)
    source_ref: topping2022understanding
    global_rank: 149
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

