---
title: D&D
slug: d-d
benchmark: TU Dortmund
task_type: graph_classification
description: Graph classification of proteins into enzymes and non-enzymes via D&D
  representation.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 1178
  avg_nodes: 284.3
  avg_edges: 715.7
  num_classes: 2
result_count: 148
best_model:
  model: Transformer
  value: 1.0
  metric: Accuracy
  arxiv_id: '2511.20406'
  paper_title: Short-Range Oversquashing
variants:
- slug: 10-fold-cv
  name: 10-fold CV
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
  - AUC
  - AUROC
  - MAE
  - MSE
  - Recall@10
  - Recall@100
  - Recall@1k
  rows:
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VRN Ensemble
    model_plain: VRN Ensemble
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9554
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVCNN
    model_plain: MVCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepSets + transformation
    model_plain: DeepSets + transformation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepSets
    model_plain: DeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.87
    - null
    - null
    - null
    - null
    - 0.0604
    - 0.285
    - 0.607
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE + CLIP/CLIP
    model_plain: SAGE + CLIP/CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3D GAN
    model_plain: 3D GAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VoxNet
    model_plain: VoxNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.831
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE + ViT/T5
    model_plain: SAGE + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8303
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Deep-Sets w. pooling only
    model_plain: Deep-Sets w. pooling only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE + DINOv2/T5
    model_plain: SAGE + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8299
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: g-U-Nets
    model_plain: g-U-Nets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8243
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2V with 1 DiffPool
    model_plain: S2V with 1 DiffPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8207
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MMGCN + DINOv2/T5
    model_plain: MMGCN + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MMGCN + ViT/T5
    model_plain: MMGCN + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8167
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MMGCN + CLIP/CLIP
    model_plain: MMGCN + CLIP/CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8161
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE + ImageBind/ImageBind
    model_plain: SAGE + ImageBind/ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool-NoLP
    model_plain: DiffPool-NoLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7998
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SortPool
    model_plain: SortPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL-OA
    model_plain: WL-OA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7904
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGC-DGCNN
    model_plain: PGC-DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7893
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2V
    model_plain: S2V
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7892
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + ImageBind/ImageBind
    model_plain: GCN + ImageBind/ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shortest-path
    model_plain: Shortest-path
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7886
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Jumping Knowledge
    model_plain: Jumping Knowledge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Full B12C1
    model_plain: Full B12C1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7818
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0202
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Full B8C1
    model_plain: Full B8C1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0369
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diverse B12C3
    model_plain: Diverse B12C3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7767
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0335
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepPano
    model_plain: DeepPano
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7764
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Repeat B12C3
    model_plain: Repeat B12C3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, augmentation
    model_plain: SAGPool_h, augmentation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3DShapeNets
    model_plain: 3DShapeNets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionSNN
    model_plain: UnionSNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0237
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07979'
    title: 'ASAP: Adaptive Structure Aware Pooling for Learning Hierarchical Graph
      Representations'
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/malllabiisc/ASAP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7687
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, parallel, M=2
    model_plain: SAGPool_h, parallel, M=2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7677
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7674
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0204
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, serial,2layers
    model_plain: SAGPool_h, serial,2layers
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7668
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ResGCN
    model_plain: ResGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7665
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0273
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAT + CLIP/CLIP
    model_plain: MGAT + CLIP/CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7648
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7645
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, SAGE
    model_plain: SAGPool_h, SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7628
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0106
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7627
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PSCN
    model_plain: PSCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7627
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MEWISPool
    model_plain: MEWISPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0259
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSNN
    model_plain: GraphSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0259
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, Cheb
    model_plain: SAGPool_h, Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7563
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0295
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7551
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0352
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPool_h, GAT
    model_plain: SAGPool_h, GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7549
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool-Det
    model_plain: DiffPool-Det
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAT + ViT/T5
    model_plain: MGAT + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7543
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7542
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: gPool_h
    model_plain: gPool_h
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7501
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TopK
    model_plain: TopK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07979'
    title: 'ASAP: Adaptive Structure Aware Pooling for Learning Hierarchical Graph
      Representations'
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/malllabiisc/ASAP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7501
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAT + DINOv2/T5
    model_plain: MGAT + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7498
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0123
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7485
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7484
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0263
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TwoHop(L4)
    model_plain: TwoHop(L4)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7453
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0524
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7425
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0376
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ECC
    model_plain: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1-WL
    model_plain: 1-WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: Jun 2018
    date_iso: 2018-06
    date_display: Jun 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7402
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionGraphSAGE
    model_plain: UnionGraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7385
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNJK
    model_plain: GCNJK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7316
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0512
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7258
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0304
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SortPool
    model_plain: SortPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7253
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0119
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionGatedGCN
    model_plain: UnionGatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP + CLIP/CLIP
    model_plain: MLP + CLIP/CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7229
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CurvGN
    model_plain: CurvGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0188
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNVIR(L8)
    model_plain: GCNVIR(L8)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7198
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0434
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Global-Attention
    model_plain: Global-Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07979'
    title: 'ASAP: Adaptive Structure Aware Pooling for Learning Hierarchical Graph
      Representations'
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/malllabiisc/ASAP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7138
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7127
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0268
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionGCN
    model_plain: UnionGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0498
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NestedGIN
    model_plain: NestedGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP + DINOv2/T5
    model_plain: MLP + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6883
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP + ViT/T5
    model_plain: MLP + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6782
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1904.08082'
    title: Self-Attention Graph Pooling
    date: Apr 17, 2019
    date_iso: '2019-04-17'
    date_display: Apr 2019
    codebase_url: https://github.com/inyeoplee77/SAGPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6695
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN(L8)
    model_plain: DGCNN(L8)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6163
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0533
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MMGCN + ImageBind/ImageBind
    model_plain: MMGCN + ImageBind/ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5875
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KNN graph-convolution
    model_plain: KNN graph-convolution
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KronRLS
    model_plain: KronRLS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.379
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimBoost
    model_plain: SimBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.282
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimCNN-DTA
    model_plain: SimCNN-DTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.319
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepDTA
    model_plain: DeepDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.261
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WideDTA
    model_plain: WideDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.886
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AttentionDTA
    model_plain: AttentionDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.216
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MATT-DTI
    model_plain: MATT-DTI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.227
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphDTA
    model_plain: GraphDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.258
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FusionDTA
    model_plain: FusionDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.22
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BiCompDTA
    model_plain: BiCompDTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.237
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PMN
    model_plain: PMN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16685'
    title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
      Protein Representation Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/HySonLab/Ligand_Generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.202
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 0.007
    - null
    - null
    - null
  - model: Frigate
    model_plain: Frigate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 3.547
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.2
    - null
    - null
    - null
    - null
  - model: STNN
    model_plain: STNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 5.633
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.18
    - null
    - null
    - null
    - null
  - model: DCRNN
    model_plain: DCRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 4.893
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.26
    - null
    - null
    - null
    - null
  - model: LocaleGN
    model_plain: LocaleGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 4.597
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.22
    - null
    - null
    - null
    - null
  - model: STGODE
    model_plain: STGODE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 4.693
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.19
    - null
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 5.712
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.33
    - null
    - null
    - null
    - null
  - model: GraphWavenet
    model_plain: GraphWavenet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08277'
    title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/idea-iitd/Frigate
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 5.308
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.3
    - null
    - null
    - null
    - null
  - model: Deep model
    model_plain: Deep model
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.925
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GW_ward
    model_plain: GW_ward
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.886
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OLO_ward
    model_plain: OLO_ward
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.892
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: R2E
    model_plain: R2E
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.83
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral_norm
    model_plain: Spectral_norm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.726
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MDS
    model_plain: MDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.763
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PCA
    model_plain: PCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.763
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Barycenter
    model_plain: Barycenter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.46
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Moment
    model_plain: Moment
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.557
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BEA_TSP
    model_plain: BEA_TSP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.852
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPIN
    model_plain: SPIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.12169'
    title: 'ReorderBench: A Benchmark for Matrix Reordering'
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.895
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8864
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9468
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9491
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.956
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGNs
    model_plain: DGNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9755
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0001
    - 0.002
    - 0.016
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bayes Set
    model_plain: Bayes Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0175
    - 0.125
    - 0.345
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: w2v Near
    model_plain: w2v Near
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0403
    - 0.167
    - 0.352
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NN-max
    model_plain: NN-max
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0472
    - 0.214
    - 0.47
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NN-sum-con
    model_plain: NN-sum-con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0487
    - 0.235
    - 0.539
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NN-max-con
    model_plain: NN-max-con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0472
    - 0.22
    - 0.518
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: generic framework to deal
    model_plain: generic framework to deal
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0554
    - 0.261
    - 0.555
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: R-PEs
    model_plain: R-PEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7224
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.003
    - null
    - null
    - null
    - null
    - null
  - model: B-PEs
    model_plain: B-PEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7122
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0042
    - null
    - null
    - null
    - null
    - null
  - model: SignNet
    model_plain: SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7227
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0097
    - null
    - null
    - null
    - null
    - null
  - model: SPE
    model_plain: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7253
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0066
    - null
    - null
    - null
    - null
    - null
  - model: BasisNet
    model_plain: BasisNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7166
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0005
    - null
    - null
    - null
    - null
    - null
  - model: PEG
    model_plain: PEG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7198
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0065
    - null
    - null
    - null
    - null
    - null
  - model: NoPE
    model_plain: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7168
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.011
    - null
    - null
    - null
    - null
    - null
  - model: SPE-8S
    model_plain: SPE-8S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7172
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0071
    - null
    - null
    - null
    - null
    - null
  - model: SE(3)-Transformer
    model_plain: SE(3)-Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0244
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TFN
    model_plain: TFN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0155
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Radial Field
    model_plain: Radial Field
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0104
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0071
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN-FA
    model_plain: GNN-FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0057
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN-Canonical
    model_plain: GNN-Canonical
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.0043
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer-Canonical
    model_plain: Transformer-Canonical
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.00508
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS+Transformer
    model_plain: GPS+Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.00401
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - 1.0e-05
    - null
    - null
    - null
  milestones:
  - value: 0.9554
    std: null
    model: VRN Ensemble
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: 2017-03
  - value: 1.0
    std: null
    model: Transformer
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: 2025-11
---

