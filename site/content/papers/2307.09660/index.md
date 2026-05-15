---
title: Neural Priority Queues for Graph Neural Networks
arxiv_id: '2307.09660'
authors: []
published_date: '2023-07-18'
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
proposed_models:
- NPQ_W-P-SV
- NPQ_W
- NPQ_M
mrr: 0.0055
results:
- &id001
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: NPQ_W-P-SV
    value: 0.2589
    std: 0.0031
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 182
    is_best: false
  - model: NPQ_W
    value: 0.267
    std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 208
    is_best: false
  - model: NPQ_M
    value: 0.3037
    std: 0.054
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 237
    is_best: false
  - model: NPQ_M-P
    value: 0.3141
    std: 0.0049
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 247
    is_best: false
  - model: Baseline
    value: 0.353
    std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 274
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
main_figure: /figures/2307.09660/main_figure.png
---

