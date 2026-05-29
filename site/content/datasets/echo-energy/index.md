---
title: ECHO-Energy
slug: echo-energy
benchmark: ECHO Benchmark
task_type: graph_regression
description: ECHO energy propagation task — predicting energy distribution on physical
  graphs.
primary_metric: MAE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 196000
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 12
best_model:
  model: DE-LBP
  value: 0.085
  metric: MAE
  arxiv_id: '1603.05629'
  paper_title: Discriminative Embeddings of Latent Variable Models for Structured
    Data
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  - RMSE
  rows:
  - model: DE-LBP
    model_plain: DE-LBP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.085
    - null
    metric_stds:
    - null
    - null
  - model: DE-MF
    model_plain: DE-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0914
    - null
    metric_stds:
    - null
    - null
  - model: WL lv-6
    model_plain: WL lv-6
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0962
    - null
    metric_stds:
    - null
    - null
  - model: WL lv-3
    model_plain: WL lv-3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1431
    - null
    metric_stds:
    - null
    - null
  - model: Predict mean
    model_plain: Predict mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: https://github.com/Hanjun-Dai/graphnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.9864
    - null
    metric_stds:
    - null
    - null
  - model: Predict mean
    model_plain: Predict mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 2.4062
    metric_stds:
    - null
    - null
  - model: Weisfeiler-lehman Kernel, degree=3
    model_plain: Weisfeiler-lehman Kernel, degree=3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1367
    metric_stds:
    - null
    - null
  - model: Embedded Mean Field
    model_plain: Embedded Mean Field
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.125
    metric_stds:
    - null
    - null
  - model: Embedded Loopy BP
    model_plain: Embedded Loopy BP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1174
    metric_stds:
    - null
    - null
  - model: Neural Fingerprint
    model_plain: Neural Fingerprint
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1409
    metric_stds:
    - null
    - null
  - model: Weisfeiler Kernel NN
    model_plain: Weisfeiler Kernel NN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1058
    metric_stds:
    - null
    - null
  - model: Weisfeiler Kernel NN, gated lambda
    model_plain: Weisfeiler Kernel NN, gated lambda
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.09037'
    title: Deriving Neural Architectures from Sequence and Graph Kernels
    date: May 25, 2017
    date_iso: '2017-05-25'
    date_display: May 2017
    codebase_url: https://github.com/taolei87/icml17_knn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1043
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.085
    std: null
    model: DE-LBP
    arxiv_id: '1603.05629'
    title: Discriminative Embeddings of Latent Variable Models for Structured Data
    date: 2016-03
---

