---
title: Cora-CA
slug: cora-ca
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: Cora co-authorship hypergraph node classification (7 subject classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1
  avg_nodes: null
  avg_edges: null
  num_classes: 7
result_count: 18
best_model:
  model: TriCL
  value: 0.8215
  metric: Accuracy
  arxiv_id: '2206.04739'
  paper_title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
    on Hypergraphs'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: TriCL
    model_plain: TriCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8215
    metric_stds:
    - 0.009
  - model: TriCL-N
    model_plain: TriCL-N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.82
    metric_stds:
    - 0.01
  - model: the use of group-level and membership-level contrast
    model_plain: the use of group-level and membership-level contrast
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8157
    metric_stds:
    - 0.011
  - model: S2-HHGR
    model_plain: S2-HHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7815
    metric_stds:
    - 0.011
  - model: UniGCN
    model_plain: UniGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    metric_stds:
    - 0.014
  - model: AllSet
    model_plain: AllSet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7694
    metric_stds:
    - 0.013
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7694
    metric_stds:
    - 0.011
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7659
    metric_stds:
    - 0.01
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7488
    metric_stds:
    - 0.016
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7452
    metric_stds:
    - 0.013
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7438
    metric_stds:
    - 0.012
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7366
    metric_stds:
    - 0.013
  - model: HyperConv
    model_plain: HyperConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7352
    metric_stds:
    - 0.01
  - model: Random-Init
    model_plain: Random-Init
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6627
    metric_stds:
    - 0.022
  - model: HyperSAGE
    model_plain: HyperSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6459
    metric_stds:
    - 0.043
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6405
    metric_stds:
    - 0.014
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6065
    metric_stds:
    - 0.092
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    metric_stds:
    - 0.021
  milestones:
  - value: 0.8215
    std: 0.009
    model: TriCL
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: 2022-06
---

