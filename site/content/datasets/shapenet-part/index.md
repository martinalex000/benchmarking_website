---
title: ShapeNet-Part
slug: shapenet-part
benchmark: Other Graph Benchmarks
task_type: node_classification
description: '3D point cloud part segmentation on ShapeNet objects. Graph-based part
  label prediction on point cloud graphs (16 object categories, 50 part classes).

  '
primary_metric: F1
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 50
result_count: 12
best_model:
  model: DensePoint
  value: 0.842
  metric: F1
  arxiv_id: '2105.11016'
  paper_title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
variants:
- slug: standard-split
  name: Standard split
  notes: 'Metric: mean IoU / F1 across parts.'
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - Accuracy
  - mIoU
  rows:
  - model: DensePoint
    model_plain: DensePoint
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.842
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.842
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RS-CNN
    model_plain: RS-CNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PointNet
    model_plain: PointNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.852
    metric_stds:
    - null
    - null
    - null
  - model: dDGM
    model_plain: dDGM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.856
    metric_stds:
    - null
    - null
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.935
    - null
    metric_stds:
    - null
    - 0.002
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.928
    - null
    metric_stds:
    - null
    - 0.003
    - null
  - model: PointNet
    model_plain: PointNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.919
    - null
    metric_stds:
    - null
    - 0.005
    - null
  - model: PointCNN
    model_plain: PointCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.929
    - null
    metric_stds:
    - null
    - 0.003
    - null
  - model: PointTransformer
    model_plain: PointTransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.09231'
    title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical Convolutional Neural
      Network'
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.931
    - null
    metric_stds:
    - null
    - 0.002
    - null
  milestones:
  - value: 0.842
    std: null
    model: DensePoint
    arxiv_id: '2105.11016'
    title: Revisiting 2D Convolutional Neural Networks for Graph-based Applications
    date: 2021-05
---

