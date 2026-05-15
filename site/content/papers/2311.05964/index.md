---
title: Multiscale Neural Operators for Solving Time-Independent PDEs
arxiv_id: '2311.05964'
authors: []
published_date: Nov 2023
abstract: Time-independent Partial Differential Equations (PDEs) on large meshes pose
  significant challenges for data-driven neural PDE solvers. We introduce a novel
  graph rewiring technique to tackle some of these challenges, such as aggregating
  information across scales and on irregular meshes. Our proposed approach bridges
  distant nodes, enhancing the global interaction capabilities of GNNs. Our experiments
  on three datasets reveal that GNN-based methods set new performance standards for
  time-independent PDEs on irregular meshes. Finally, we show that our graph rewiring
  strategy boosts the performance of baseline methods, achieving state-of-the-art
  results in one of the tasks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- BSMS
mrr: 0.0
results:
- &id001
  dataset: Flow
  rows:
  - model: U-Net
    value: 0.0064
    std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Takamoto 2022
    global_rank: null
    is_best: true
  - model: BSMS
    value: 0.00983
    std: 0.000818
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Gao 2019
    global_rank: null
    is_best: false
  - model: FNO
    value: 0.012
    std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Takamoto 2022
    global_rank: null
    is_best: false
  - model: Perceiver IO + GNN
    value: 0.0131
    std: 0.000219
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Perceiver IO
    value: 0.0141
    std: 0.00116
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Jaegle 2021
    global_rank: null
    is_best: false
  - model: MGN + Tree
    value: 0.0413
    std: 0.0147
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGN
    value: 0.0641
    std: 0.000523
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Pfaff 2020
    global_rank: null
    is_best: false
  - model: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: GraphBench
  datasets:
  - *id001
single_proposed_model: BSMS
main_figure: /figures/2311.05964/main_figure.png
---

