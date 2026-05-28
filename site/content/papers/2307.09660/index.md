---
title: Neural Priority Queues for Graph Neural Networks
arxiv_id: '2307.09660'
source_url: ''
authors: []
published_date: Jul 18, 2023
published_date_iso: '2023-07-18'
abstract: Graph Neural Networks (GNNs) have shown considerable success in neural algorithmic
  reasoning. Many traditional algorithms make use of an explicit memory in the form
  of a data structure. However, there has been limited exploration on augmenting GNNs
  with external memory. In this paper, we present Neural Priority Queues, a differentiable
  analogue to algorithmic priority queues, for GNNs. We propose and motivate a desiderata
  for memory modules, and show that Neural PQs exhibit the desiderata, and reason
  about their use with algorithmic reasoning. This is further demonstrated by empirical
  results on the CLRS-30 dataset. Furthermore, we find the Neural PQs useful in capturing
  long-range interactions, as empirically shown on a dataset from the Long-Range Graph
  Benchmark.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- NPQ_W-P-SV
- NPQ_W
- NPQ_M
mrr: 0.0047
adjusted_mrr: 0.0016
mrr_dataset_count: 1
benchmark_categories:
- LRGB
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: NPQ_W-P-SV
    model_key: npq_w-p-sv
    model_plain: NPQ_W-P-SV
    value: 0.2589
    std: 0.0031
    paper_value: 0.2589
    paper_std: 0.0031
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 18, 2023
    date_display: Jul 2023
    date_iso: '2023-07-18'
    global_rank: 212
    true_value: 0.2589
    true_std: 0.0031
    value_gap_source_arxiv: '2307.09660'
    value_gap_source_title: Neural Priority Queues for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2589
    sort_std: 0.0031
    is_best: false
  - model: NPQ_W
    model_key: npq_w
    model_plain: NPQ_W
    value: 0.267
    std: 0.0009
    paper_value: 0.267
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 18, 2023
    date_display: Jul 2023
    date_iso: '2023-07-18'
    global_rank: 239
    true_value: 0.267
    true_std: 0.0009
    value_gap_source_arxiv: '2307.09660'
    value_gap_source_title: Neural Priority Queues for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.267
    sort_std: 0.0009
    is_best: false
  - model: NPQ_M
    model_key: npq_m
    model_plain: NPQ_M
    value: 0.3037
    std: 0.054
    paper_value: 0.3037
    paper_std: 0.054
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 18, 2023
    date_display: Jul 2023
    date_iso: '2023-07-18'
    global_rank: 272
    true_value: 0.3037
    true_std: 0.054
    value_gap_source_arxiv: '2307.09660'
    value_gap_source_title: Neural Priority Queues for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 272
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3037
    sort_std: 0.054
    is_best: false
  - model: NPQ_M-P
    model_key: npq_m-p
    model_plain: NPQ_M-P
    value: 0.3141
    std: 0.0049
    paper_value: 0.3141
    paper_std: 0.0049
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 18, 2023
    date_display: Jul 2023
    date_iso: '2023-07-18'
    global_rank: 282
    true_value: 0.3141
    true_std: 0.0049
    value_gap_source_arxiv: '2307.09660'
    value_gap_source_title: Neural Priority Queues for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 282
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3141
    sort_std: 0.0049
    is_best: false
  - model: Baseline
    model_key: baseline
    model_plain: Baseline
    value: 0.353
    std: 0.0019
    paper_value: 0.353
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 18, 2023
    date_display: Jul 2023
    date_iso: '2023-07-18'
    global_rank: 310
    true_value: 0.353
    true_std: 0.0019
    value_gap_source_arxiv: '2307.09660'
    value_gap_source_title: Neural Priority Queues for Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 310
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.353
    sort_std: 0.0019
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
main_figure: /figures/2307.09660/main_figure.png
---

