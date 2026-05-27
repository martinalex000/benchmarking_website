---
title: ': Frugal Spatio-temporal Forecasting on Road Networks'
arxiv_id: '2306.08277'
authors: []
published_date: Jun 2023
abstract: Modelling spatio-temporal processes on road networks is a task of growing importance. While
  significant progress has been made on developing spatio-temporal graph neural networks, existing works
  are built upon three assumptions that are not practical on real-world road networks. First, they assume
  sensing on every node of a road network. In reality, due to budget-constraints or sensor failures, all
  locations (nodes) may not be equipped with sensors. Second, they assume that sensing history is available
  at all installed sensors. This is unrealistic as well due to sensor failures, loss of packets during
  communication, etc. Finally, there is an assumption of static road networks. Connectivity within networks
  change due to road closures, constructions of new roads, etc. In this work, we develop to address all
  these shortcomings. is powered by a spatio-temporal that integrates positional, topological, and temporal
  information into rich inductive node representations. The joint fusion of this diverse information is
  made feasible through a novel combination of gated Lipschitz embeddings with. We prove that the proposed
  architecture is provably more expressive than message-passing used in state-of-the-art algorithms. The
  higher expressivity of naturally translates to superior empirical performance conducted on real-world
  network-constrained traffic data. In addition, is robust to frugal sensor deployment, changes in road
  network connectivity, and temporal irregularity in sensing.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- Ours
- Frigate
mrr: 0.0
results:
- &id001
  dataset: D&D
  rows:
  - model: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.093
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: Ours
    value: 3.547
    std: 0.2
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Frigate
    value: 3.547
    std: 0.2
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: OURS (without Gating)
    value: 3.734
    std: 0.18
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: OURS (without Lipschitz)
    value: 3.787
    std: 0.18
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: LocaleGN
    value: 4.597
    std: 0.22
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: STGODE
    value: 4.693
    std: 0.19
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DCRNN
    value: 4.893
    std: 0.26
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GraphWavenet
    value: 5.308
    std: 0.3
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: STNN
    value: 5.633
    std: 0.18
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: STGCN
    value: 5.712
    std: 0.33
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2306.08277/main_figure.png
---

