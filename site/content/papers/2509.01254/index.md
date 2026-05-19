---
title: 'What Expressivity Theory Misses: - Message Passing Complexity for GNNs'
arxiv_id: '2509.01254'
authors: []
published_date: Sep 2025
abstract: 'Expressivity theory, characterizing which graphs a GNN can distinguish,
  has become the predominant framework for analyzing GNNs, with new models striving
  for higher expressivity. However, we argue that this focus is misguided: First,
  higher expressivity is not necessary for most real-world tasks as these tasks rarely
  require expressivity beyond the basic WL test. Second, expressivity theory''s binary
  characterization and idealized assumptions fail to reflect GNNs'' practical capabilities.
  To overcome these limitations, we propose Message Passing Complexity (): a continuous
  measure that quantifies the difficulty for a GNN architecture to solve a given task
  through message passing. captures practical limitations like over-squashing while
  preserving theoretical impossibility results from expressivity theory, effectively
  narrowing the gap between theory and practice. Through extensive validation on fundamental
  GNN tasks, we show that ''s theoretical predictions correlate with empirical performance,
  successfully explaining architectural successes and failures. Thereby, advances
  beyond expressivity theory to provide a more powerful and nuanced framework for
  understanding and improving GNN architectures.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- CIN
mrr: 0.1429
results:
- &id001
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: CIN
    value: 0.077
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: FragNet
    value: 0.078
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 126
    is_best: false
  - model: GSN
    value: 0.12
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 161
    is_best: false
  - model: GCN
    value: 0.37
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 115
    is_best: false
  - model: GraphSAGE
    value: 0.4
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 188
    is_best: false
  - model: GIN
    value: 0.53
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
single_proposed_model: CIN
main_figure: /figures/2509.01254/main_figure.png
---

