---
title: Multiscale Neural Operators for Solving Time-Independent PDEs
arxiv_id: '2311.05964'
source_url: ''
authors: []
published_date: Nov 2023
published_date_iso: 2023-11
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
paper_type: method
proposed_models:
- BSMS
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- GraphBench
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: Flow
  rows:
  - model: U-Net
    model_key: u-net
    model_plain: U-Net
    value: 0.0064
    std: null
    paper_value: 0.0064
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Takamoto 2022
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.0064
    sort_std: null
    is_best: true
  - model: BSMS
    model_key: bsms
    model_plain: BSMS
    value: 0.00983
    std: 0.000818
    paper_value: 0.00983
    paper_std: 0.000818
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Gao 2019
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.00983
    sort_std: 0.000818
    is_best: false
  - model: FNO
    model_key: fno
    model_plain: FNO
    value: 0.012
    std: null
    paper_value: 0.012
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Takamoto 2022
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.012
    sort_std: null
    is_best: false
  - model: Perceiver IO + GNN
    model_key: perceiver io + gnn
    model_plain: Perceiver IO + GNN
    value: 0.0131
    std: 0.000219
    paper_value: 0.0131
    paper_std: 0.000219
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.0131
    sort_std: 0.000219
    is_best: false
  - model: Perceiver IO
    model_key: perceiver io
    model_plain: Perceiver IO
    value: 0.0141
    std: 0.00116
    paper_value: 0.0141
    paper_std: 0.00116
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Jaegle 2021
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.0141
    sort_std: 0.00116
    is_best: false
  - model: MGN + Tree
    model_key: mgn + tree
    model_plain: MGN + Tree
    value: 0.0413
    std: 0.0147
    paper_value: 0.0413
    paper_std: 0.0147
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.0413
    sort_std: 0.0147
    is_best: false
  - model: MGN
    model_key: mgn
    model_plain: MGN
    value: 0.0641
    std: 0.000523
    paper_value: 0.0641
    paper_std: 0.000523
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Pfaff 2020
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: null
    sort_value: 0.0641
    sort_std: 0.000523
    is_best: false
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
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
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.45
    sort_std: 0.06
    is_best: false
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
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
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.49
    sort_std: 0.02
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
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
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.73
    sort_std: 0.09
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

