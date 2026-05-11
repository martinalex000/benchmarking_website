---
title: 'GraphBench: Next-generation graph learning benchmarking'
arxiv_id: '2512.04475'
authors: []
published_date: Dec 2025
abstract: Machine learning on graphs has recently achieved impressive progress in
  various domains, including molecular property prediction and chip design. However,
  benchmarking practices remain fragmented, often relying on narrow, task-specific
  datasets and inconsistent evaluation protocols, which hampers reproducibility and
  broader progress. To address this, we introduce GraphBench, a comprehensive benchmarking
  suite that spans diverse domains and prediction tasks, including node-level, edge-level,
  graph-level, and generative settings. GraphBench provides standardized evaluation
  protocols -- with consistent dataset splits and performance metrics that account
  for out-of-distribution generalization -- as well as a unified hyperparameter tuning
  framework. Additionally, we benchmark GraphBench using message-passing neural networks
  and graph transformer models, providing principled baselines and establishing a
  reference performance. See www.graphbench.io for further details.
codebase_url: https://github.com/graphbench/package
extraction_model: glm-4.7
results:
- dataset: Cora
  is_multi_metric: true
  rows:
  - model: GCN
    metric_values:
    - 0.53
    - 0.53
    - 0.61
    metric_stds:
    - 0.06
    - 0.06
    - 0.07
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    is_best: true
  - model: GT
    metric_values:
    - 0.29
    - 0.29
    - 0.39
    metric_stds:
    - 0.03
    - 0.03
    - 0.05
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: true
  - model: GIN
    metric_values:
    - 0.44
    - 0.44
    - 0.54
    metric_stds:
    - 0.13
    - 0.13
    - 0.12
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: true
  - model: GAT
    metric_values:
    - 0.38
    - 0.38
    - 0.48
    metric_stds:
    - 0.05
    - 0.05
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: true
  metrics:
  - Efficiency
  - RSE
  - Voltage
  primary_metric: Accuracy
  higher_is_better: false
main_figure: /figures/2512.04475/main_figure.png
---

