---
title: ESOL
slug: esol
benchmark: MoleculeNet
task_type: graph_regression
description: Aqueous solubility regression (log mol/L) on 1,128 molecules.
primary_metric: RMSE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats: null
result_count: 5
best_model:
  model: Neural FPs + neural net
  value: 0.52
  metric: RMSE
  arxiv_id: '1509.09292'
  paper_title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: RMSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - RMSE
  rows:
  - model: Neural FPs + neural net
    model_plain: Neural FPs + neural net
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.52
    metric_stds:
    - 0.07
  - model: Neural FPs + linear layer
    model_plain: Neural FPs + linear layer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    metric_stds:
    - 0.11
  - model: Circular FPs + neural net
    model_plain: Circular FPs + neural net
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.4
    metric_stds:
    - 0.13
  - model: Circular FPs + linear layer
    model_plain: Circular FPs + linear layer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.71
    metric_stds:
    - 0.13
  - model: Predict mean
    model_plain: Predict mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.29
    metric_stds:
    - 0.4
  milestones:
  - value: 0.52
    std: 0.07
    model: Neural FPs + neural net
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: 2015-09
---

