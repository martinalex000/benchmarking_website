---
title: MUTAG
slug: mutag
benchmark: TU Dortmund
task_type: graph_classification
description: Graph classification of mutagenic aromatic and heteroaromatic nitro compounds
  (2 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 188
  avg_nodes: 17.93
  avg_edges: 19.79
  num_classes: 2
result_count: 452
best_model:
  model: RC-Explainer
  value: 0.986
  metric: Accuracy
  arxiv_id: '2204.11028'
  paper_title: Reinforced Causal Explainer for Graph Neural Networks
variants:
- slug: 10-fold-cv
  name: 10-fold CV
  notes: 10-fold cross-validation (average ± std reported).
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
  - Coverage
  rows:
  - model: RC-Explainer
    model_plain: RC-Explainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.986
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SVMs
    model_plain: SVMs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_iso: 2022-03
    date_display: Mar 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.983
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
  - model: Base (GCN)
    model_plain: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/chrisjtan/gnn_cff
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9805
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: novel SUbG rAph neural network
    model_plain: novel SUbG rAph neural network
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/RingBDStack/SUGAR
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9674
    - null
    - null
    metric_stds:
    - 0.0455
    - null
    - null
  - model: GCN (trained for XGNN)
    model_plain: GCN (trained for XGNN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.02587'
    title: 'XGNN: Towards Model-Level Explanations of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.963
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HAP
    model_plain: HAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9501
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Zhao et al.
    model_plain: Zhao et al.
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.95
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PXGL-GNN
    model_plain: PXGL-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9487
    - null
    - null
    metric_stds:
    - 0.0226
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
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9418
    - null
    - null
    metric_stds:
    - 0.0461
    - null
    - null
  - model: CAN
    model_plain: CAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.941
    - null
    - null
    metric_stds:
    - 0.048
    - null
    - null
  - model: MPNN
    model_plain: MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.939
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
  - model: MA-GCNN
    model_plain: MA-GCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/RingBDStack/SUGAR
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9389
    - null
    - null
    metric_stds:
    - 0.0524
    - null
    - null
  - model: PSAGNN
    model_plain: PSAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9324
    - null
    - null
    metric_stds:
    - 0.0251
    - null
    - null
  - model: CapsNets
    model_plain: CapsNets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9316
    - null
    - null
    metric_stds:
    - 0.061
    - null
    - null
  - model: LaplaceGNN
    model_plain: LaplaceGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9285
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: CIN
    model_plain: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.927
    - null
    - null
    metric_stds:
    - 0.061
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9265
    - null
    - null
    metric_stds:
    - 0.0153
    - null
    - null
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
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
    - 0.9263
    - null
    - null
    metric_stds:
    - 0.0421
    - null
    - null
  - model: PGOT
    model_plain: PGOT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9263
    - null
    - null
    metric_stds:
    - 0.0258
    - null
    - null
  - model: PS
    model_plain: PS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.926
    - null
    - null
    metric_stds:
    - 0.042
    - null
    - null
  - model: Graphormer-SPIS
    model_plain: Graphormer-SPIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9248
    - null
    - null
    metric_stds:
    - 0.0587
    - null
    - null
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.922
    - null
    - null
    metric_stds:
    - 0.075
    - null
    - null
  - model: FGSD
    model_plain: FGSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9212
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NEST
    model_plain: NEST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/RingBDStack/SUGAR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9185
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
  - model: FractalGCL
    model_plain: FractalGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9171
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: MFN (GCN)
    model_plain: MFN (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10434'
    title: Equivariant Matrix Function Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.915
    - null
    - null
    metric_stds:
    - 0.0735
    - null
    - null
  - model: ECL-GSR
    model_plain: ECL-GSR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9145
    - null
    - null
    metric_stds:
    - 0.0275
    - null
    - null
  - model: ICL
    model_plain: ICL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9134
    - null
    - null
    metric_stds:
    - 0.0219
    - null
    - null
  - model: novel masking-based evaluation strategy
    model_plain: novel masking-based evaluation strategy
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.91
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: TDA
    model_plain: TDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9099
    - null
    - null
    metric_stds:
    - 0.0664
    - null
    - null
  - model: GFN
    model_plain: GFN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9084
    - null
    - null
    metric_stds:
    - 0.0722
    - null
    - null
  - model: FGConv-Sum
    model_plain: FGConv-Sum
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.06922'
    title: Decimated Framelet System on Graphs and Fast $ $-Framelet Transforms
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/YuGuangWang/FGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.908
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9062
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.906
    - null
    - null
    metric_stds:
    - 0.087
    - null
    - null
  - model: WL sp
    model_plain: WL sp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9051
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
  - model: P-WL-C
    model_plain: P-WL-C
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9051
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
  - model: IGNN-Solver (AA)
    model_plain: IGNN-Solver (AA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.904
    - null
    - null
    metric_stds:
    - 0.057
    - null
    - null
  - model: WLK
    model_plain: WLK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.904
    - null
    - null
    metric_stds:
    - 0.057
    - null
    - null
  - model: WL subtree
    model_plain: WL subtree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.904
    - null
    - null
    metric_stds:
    - 0.057
    - null
    - null
  - model: Graphormer-Neighbor
    model_plain: Graphormer-Neighbor
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9035
    - null
    - null
    metric_stds:
    - 0.0701
    - null
    - null
  - model: RetGK
    model_plain: RetGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: RetGK_I
    model_plain: RetGK_I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: TopoGCL
    model_plain: TopoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9009
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
  - model: 0-MPNNs
    model_plain: 0-MPNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    metric_stds:
    - 0.051
    - null
    - null
  - model: GNTK
    model_plain: GNTK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    metric_stds:
    - 0.085
    - null
    - null
  - model: ORC
    model_plain: ORC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8997
    - null
    - null
    metric_stds:
    - 0.0365
    - null
    - null
  - model: PDF
    model_plain: PDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8991
    - null
    - null
    metric_stds:
    - 0.0435
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.899
    - null
    - null
    metric_stds:
    - 0.065
    - null
    - null
  - model: GFN-light
    model_plain: GFN-light
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8989
    - null
    - null
    metric_stds:
    - 0.0714
    - null
    - null
  - model: S2S-N2N-PP
    model_plain: S2S-N2N-PP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/RingBDStack/SUGAR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8986
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8972
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8971
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: MGCL
    model_plain: MGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8955
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: RGCL
    model_plain: RGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: SumPool
    model_plain: SumPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8947
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8945
    - null
    - null
    metric_stds:
    - 0.0614
    - null
    - null
  - model: ECC
    model_plain: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/RingBDStack/SUGAR
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8944
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN-0
    model_plain: GIN-0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8942
    - null
    - null
    metric_stds:
    - 0.0561
    - null
    - null
  - model: NGN
    model_plain: NGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: CGS
    model_plain: CGS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    metric_stds:
    - 0.056
    - null
    - null
  - model: GCN^2
    model_plain: GCN^2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8939
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.893
    - null
    - null
    metric_stds:
    - 0.067
    - null
    - null
  - model: GIND
    model_plain: GIND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.893
    - null
    - null
    metric_stds:
    - 0.074
    - null
    - null
  - model: S2GAE
    model_plain: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8927
    - null
    - null
    metric_stds:
    - 0.0153
    - null
    - null
  - model: GraphTrans (GIN)
    model_plain: GraphTrans (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8924
    - null
    - null
    metric_stds:
    - 0.0529
    - null
    - null
  - model: GCL
    model_plain: GCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8913
    - null
    - null
    metric_stds:
    - 0.0191
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8901
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8901
    - null
    - null
    metric_stds:
    - 0.0131
    - null
    - null
  - model: GIN-ε
    model_plain: GIN-ε
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8901
    - null
    - null
    metric_stds:
    - 0.0601
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.89
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: PSCN
    model_plain: PSCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8895
    - null
    - null
    metric_stds:
    - 0.0437
    - null
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8889
    - null
    - null
    metric_stds:
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
    - 0.8886
    - null
    - null
    metric_stds:
    - 0.0433
    - null
    - null
  - model: EMP
    model_plain: EMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8879
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
  - model: AGFormer(GCN)
    model_plain: AGFormer(GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8878
    - null
    - null
    metric_stds:
    - 0.0878
    - null
    - null
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    metric_stds:
    - 0.0185
    - null
    - null
  - model: AutoGCL
    model_plain: AutoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8864
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: ILSS
    model_plain: ILSS
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
    - 0.885
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: FDGNN
    model_plain: FDGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    metric_stds:
    - 0.038
    - null
    - null
  - model: PGIB_cont (MaxPool)
    model_plain: PGIB_cont (MaxPool)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    metric_stds:
    - 0.0634
    - null
    - null
  - model: GradGCL
    model_plain: GradGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8846
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
  - model: FGW
    model_plain: FGW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8842
    - null
    - null
    metric_stds:
    - 0.0567
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
    - 0.8833
    - null
    - null
    metric_stds:
    - 0.0388
    - null
    - null
  - model: WWLS
    model_plain: WWLS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    metric_stds:
    - 0.0123
    - null
    - null
  - model: CORE SP
    model_plain: CORE SP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8829
    - null
    - null
    metric_stds:
    - 0.0155
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8829
    - null
    - null
    metric_stds:
    - 0.0131
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8821
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8812
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
  - model: MLG
    model_plain: MLG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8794
    - null
    - null
    metric_stds:
    - 0.0161
    - null
    - null
  - model: AWL
    model_plain: AWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.879
    - null
    - null
    metric_stds:
    - 0.098
    - null
    - null
  - model: ifMixup
    model_plain: ifMixup
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.879
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: AWE
    model_plain: AWE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8787
    - null
    - null
    metric_stds:
    - 0.0976
    - null
    - null
  - model: gPool
    model_plain: gPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8772
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8767
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: RGCL
    model_plain: RGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8766
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
  - model: RU-GIN
    model_plain: RU-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8761
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: SubGNN
    model_plain: SubGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8752
    - null
    - null
    metric_stds:
    - 0.0237
    - null
    - null
  - model: rLap (GraphCL)
    model_plain: rLap (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.875
    - null
    - null
    metric_stds:
    - 0.0986
    - null
    - null
  - model: GTOT-Tuning
    model_plain: GTOT-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.875
    - null
    - null
    metric_stds:
    - 0.0694
    - null
    - null
  - model: DGK
    model_plain: DGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8744
    - null
    - null
    metric_stds:
    - 0.0272
    - null
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8735
    - null
    - null
    metric_stds:
    - 0.0102
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
    - 0.8731
    - null
    - null
    metric_stds:
    - 0.0529
    - null
    - null
  - model: FC-V
    model_plain: FC-V
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8731
    - null
    - null
    metric_stds:
    - 0.0066
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
    - 0.8725
    - null
    - null
    metric_stds:
    - 0.0628
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
    - 0.8722
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
  - model: DAGCN
    model_plain: DAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8722
    - null
    - null
    metric_stds:
    - 0.061
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.872
    - null
    - null
    metric_stds:
    - 0.0511
    - null
    - null
  - model: GPSE
    model_plain: GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8719
    - null
    - null
    metric_stds:
    - 0.0866
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
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
    - 0.87
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: CXPlain
    model_plain: CXPlain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.868
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8672
    - null
    - null
    metric_stds:
    - 0.0195
    - null
    - null
  - model: CapsGNN
    model_plain: CapsGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8667
    - null
    - null
    metric_stds:
    - 0.0688
    - null
    - null
  - model: PGIB (MaxPool)
    model_plain: PGIB (MaxPool)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.865
    - null
    - null
    metric_stds:
    - 0.0784
    - null
    - null
  - model: PGIB_cont (SumPool)
    model_plain: PGIB_cont (SumPool)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.865
    - null
    - null
    metric_stds:
    - 0.0743
    - null
    - null
  - model: GCC
    model_plain: GCC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8641
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: GLA
    model_plain: GLA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8632
    - null
    - null
    metric_stds:
    - 0.0125
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
    - 0.8623
    - null
    - null
    metric_stds:
    - 0.0882
    - null
    - null
  - model: SSGE
    model_plain: SSGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8621
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8615
    - null
    - null
    metric_stds:
    - 0.0149
    - null
    - null
  - model: G-Tuning
    model_plain: G-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8614
    - null
    - null
    metric_stds:
    - 0.055
    - null
    - null
  - model: GIN + GTR
    model_plain: GIN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    metric_stds:
    - 0.0176
    - null
    - null
  - model: k-GNN
    model_plain: k-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 123-gnn
    model_plain: 123-gnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Edge Dropping + EPA (GraphCL)
    model_plain: Edge Dropping + EPA (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.861
    - null
    - null
    metric_stds:
    - 0.053
    - null
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.86
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: MixupGraph
    model_plain: MixupGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: Node Dropping + EPA (GraphCL)
    model_plain: Node Dropping + EPA (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.86
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8583
    - null
    - null
    metric_stds:
    - 0.0166
    - null
    - null
  - model: sp
    model_plain: sp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: Oct 2014
    date_iso: 2014-10
    date_display: Oct 2014
    codebase_url: https://github.com/marionmari/propagation_kernels
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: labels
    model_plain: labels
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: Oct 2014
    date_iso: 2014-10
    date_display: Oct 2014
    codebase_url: https://github.com/marionmari/propagation_kernels
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: Edge Dropping + Vanilla (GraphCL)
    model_plain: Edge Dropping + Vanilla (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8567
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
  - model: Supervised GCN
    model_plain: Supervised GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8563
    - null
    - null
    metric_stds:
    - 0.0584
    - null
    - null
  - model: NodeSam + Vanilla
    model_plain: NodeSam + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.856
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
  - model: MP-HSM
    model_plain: MP-HSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.856
    - null
    - null
    metric_stds:
    - 0.053
    - null
    - null
  - model: GCN + GTR
    model_plain: GCN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    metric_stds:
    - 0.0147
    - null
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: Node Dropping + EPA (SimSiam)
    model_plain: Node Dropping + EPA (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    metric_stds:
    - 0.049
    - null
    - null
  - model: Edge Dropping + EPA (SimSiam)
    model_plain: Edge Dropping + EPA (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    metric_stds:
    - 0.051
    - null
    - null
  - model: PGIB_cont
    model_plain: PGIB_cont
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    metric_stds:
    - 0.0522
    - null
    - null
  - model: Graphormer-id
    model_plain: Graphormer-id
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8549
    - null
    - null
    metric_stds:
    - 0.0851
    - null
    - null
  - model: GH
    model_plain: GH
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: Oct 2014
    date_iso: 2014-10
    date_display: Oct 2014
    codebase_url: https://github.com/marionmari/propagation_kernels
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.854
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Attribute Masking + EPA (SimSiam)
    model_plain: Attribute Masking + EPA (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.854
    - null
    - null
    metric_stds:
    - 0.048
    - null
    - null
  - model: GraphAug
    model_plain: GraphAug
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.853
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: Mixup + EPA (GraphCL)
    model_plain: Mixup + EPA (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.852
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.852
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
  - model: MeanAttPool
    model_plain: MeanAttPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8506
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MeanPool
    model_plain: MeanPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8501
    - null
    - null
    metric_stds:
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
    - 0.85
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: Attribute Masking + EPA (GraphCL)
    model_plain: Attribute Masking + EPA (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    metric_stds:
    - 0.047
    - null
    - null
  - model: Mixup + Vanilla (GraphCL)
    model_plain: Mixup + Vanilla (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
  - model: PGIB
    model_plain: PGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    metric_stds:
    - 0.0707
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
    - 0.8473
    - null
    - null
    metric_stds:
    - 0.0473
    - null
    - null
  - model: Subgraph + EPA (SimSiam)
    model_plain: Subgraph + EPA (SimSiam)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.847
    - null
    - null
    metric_stds:
    - 0.052
    - null
    - null
  - model: Infomax
    model_plain: Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8468
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
  - model: DGLC
    model_plain: DGLC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8468
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
  - model: Subgraph + EPA (GraphCL)
    model_plain: Subgraph + EPA (GraphCL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.846
    - null
    - null
    metric_stds:
    - 0.037
    - null
    - null
  - model: BSS
    model_plain: BSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8456
    - null
    - null
    metric_stds:
    - 0.0552
    - null
    - null
  - model: PK
    model_plain: PK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: Oct 2014
    date_iso: 2014-10
    date_display: Oct 2014
    codebase_url: https://github.com/marionmari/propagation_kernels
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: SortPool
    model_plain: SortPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.844
    - null
    - null
    metric_stds:
    - 0.141
    - null
    - null
  - model: 1-WL_F (K3-K4)
    model_plain: 1-WL_F (K3-K4)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.843
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: Subgraph + Vanilla (GraphCL)
    model_plain: Subgraph + Vanilla (GraphCL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    metric_stds:
    - 0.038
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
    - 0.8409
    - null
    - null
    metric_stds:
    - 0.0842
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
    - 0.8406
    - null
    - null
    metric_stds:
    - 0.0662
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
    - 0.8404
    - null
    - null
    metric_stds:
    - 0.0409
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
    - 0.84
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: 1-WL_F (K3)
    model_plain: 1-WL_F (K3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: Oct 2014
    date_iso: 2014-10
    date_display: Oct 2014
    codebase_url: https://github.com/marionmari/propagation_kernels
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.0374
    - null
    - null
  - model: Attribute Masking + Vanilla (SimSiam)
    model_plain: Attribute Masking + Vanilla (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.048
    - null
    - null
  - model: DMP
    model_plain: DMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.086
    - null
    - null
  - model: DMoN
    model_plain: DMoN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.84
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: GIN+GIB
    model_plain: GIN+GIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    metric_stds:
    - 0.064
    - null
    - null
  - model: IGN
    model_plain: IGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    metric_stds:
    - 0.13
    - null
    - null
  - model: GIN+SIB
    model_plain: GIN+SIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    metric_stds:
    - 0.064
    - null
    - null
  - model: Subgraph + Vanilla (SimSiam)
    model_plain: Subgraph + Vanilla (SimSiam)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.838
    - null
    - null
    metric_stds:
    - 0.039
    - null
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8375
    - null
    - null
    metric_stds:
    - 0.085
    - null
    - null
  - model: RW
    model_plain: RW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8372
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: Random Walk
    model_plain: Random Walk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8371
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
  - model: 1-WL
    model_plain: 1-WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.837
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: Node Dropping + Vanilla (SimSiam)
    model_plain: Node Dropping + Vanilla (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    - null
    - null
    metric_stds:
    - 0.045
    - null
    - null
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8368
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8363
    - null
    - null
    metric_stds:
    - 0.0081
    - null
    - null
  - model: 1-WL_F (C3-C4)
    model_plain: 1-WL_F (C3-C4)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: Vanilla Tuning
    model_plain: Vanilla Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8345
    - null
    - null
    metric_stds:
    - 0.0571
    - null
    - null
  - model: GMTPool
    model_plain: GMTPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8344
    - null
    - null
    metric_stds:
    - 0.0133
    - null
    - null
  - model: SortPooling
    model_plain: SortPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8333
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: StructPool
    model_plain: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8333
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 1-WL_F (C3)
    model_plain: 1-WL_F (C3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.09802'
    title: Label-invariant Augmentation for Semi-Supervised Graph Classification
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8316
    - null
    - null
    metric_stds:
    - 0.0098
    - null
    - null
  - model: graph2vec
    model_plain: graph2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8315
    - null
    - null
    metric_stds:
    - 0.0925
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.831
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: R-GIN + None
    model_plain: R-GIN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8305
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
  - model: R-GIN + Every FA
    model_plain: R-GIN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8305
    - null
    - null
    metric_stds:
    - 0.0152
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
    - 0.8304
    - null
    - null
    metric_stds:
    - 0.087
    - null
    - null
  - model: Mixup + EPA (SimSiam)
    model_plain: Mixup + EPA (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    metric_stds:
    - 0.07
    - null
    - null
  - model: Diff
    model_plain: Diff
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
  - model: Mincut
    model_plain: Mincut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    metric_stds:
    - 0.07
    - null
    - null
  - model: TV
    model_plain: TV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.04236'
    title: Graph Pooling via Ricci Flow
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: L2_SP
    model_plain: L2_SP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8298
    - null
    - null
    metric_stds:
    - 0.0391
    - null
    - null
  - model: DELTA
    model_plain: DELTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8298
    - null
    - null
    metric_stds:
    - 0.0612
    - null
    - null
  - model: Feature Map
    model_plain: Feature Map
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8295
    - null
    - null
    metric_stds:
    - 0.078
    - null
    - null
  - model: WL edge
    model_plain: WL edge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8294
    - null
    - null
    metric_stds:
    - 0.0233
    - null
    - null
  - model: DropNode
    model_plain: DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: Mixup + Vanilla (SimSiam)
    model_plain: Mixup + Vanilla (SimSiam)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
  - model: Graph Transplant_EP (GIN)
    model_plain: Graph Transplant_EP (GIN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: Supervised
    model_plain: Supervised
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8289
    - null
    - null
    metric_stds:
    - 0.0616
    - null
    - null
  - model: GLN
    model_plain: GLN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8285
    - null
    - null
    metric_stds:
    - 0.1215
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8271
    - null
    - null
    metric_stds:
    - 0.0162
    - null
    - null
  - model: R-GIN + SDRF
    model_plain: R-GIN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    metric_stds:
    - 0.0178
    - null
    - null
  - model: No augmentation
    model_plain: No augmentation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8263
    - null
    - null
    metric_stds:
    - 0.0162
    - null
    - null
  - model: 1-WLOA
    model_plain: 1-WLOA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.826
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: L2xGin
    model_plain: L2xGin
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.14402'
    title: 'L2XGNN: Learning to Explain Graph Neural Networks'
    date: Sep 28, 2022
    date_iso: '2022-09-28'
    date_display: Sep 2022
    codebase_url: https://github.com/GiuseppeSerra93/L2XGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    metric_stds:
    - 0.078
    - null
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8247
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
  - model: EPIC
    model_plain: EPIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8244
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8244
    - null
    - null
    metric_stds:
    - 0.0129
    - null
    - null
  - model: StochNorm
    model_plain: StochNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.824
    - null
    - null
    metric_stds:
    - 0.0795
    - null
    - null
  - model: HoscPool
    model_plain: HoscPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: AttPool-global
    model_plain: AttPool-global
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8222
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Manifold-Mixup
    model_plain: Manifold-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: HGP-SL
    model_plain: HGP-SL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8215
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: StableSAGE
    model_plain: StableSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8212999999999999
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
  - model: M-Evolve
    model_plain: M-Evolve
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: SubG
    model_plain: SubG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: Graph Transplant_DP (GCS)
    model_plain: Graph Transplant_DP (GCS)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: UFGPool-Spectrum
    model_plain: UFGPool-Spectrum
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    metric_stds:
    - 0.0128
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/chentingpc/gfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: WLSK
    model_plain: WLSK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8205
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: Attribute Masking + Vanilla (GraphCL)
    model_plain: Attribute Masking + Vanilla (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    metric_stds:
    - 0.064
    - null
    - null
  - model: DropN
    model_plain: DropN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: PermE
    model_plain: PermE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GM-Mix
    model_plain: GM-Mix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8196
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: Vanilla
    model_plain: Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: MaskN
    model_plain: MaskN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.05639'
    title: 'Graph Transplant: Node Saliency-Guided Graph Mixup with Local Structure
      Preservation'
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    metric_stds:
    - 0.091
    - null
    - null
  - model: HP-2
    model_plain: HP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.817
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8167
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GK
    model_plain: GK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8166
    - null
    - null
    metric_stds:
    - 0.0211
    - null
    - null
  - model: UFGPool-Sum
    model_plain: UFGPool-Sum
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8159
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: rLap (BGRL)
    model_plain: rLap (BGRL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    - null
    metric_stds:
    - 0.0539
    - null
    - null
  - model: DGLC_d3
    model_plain: DGLC_d3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8148
    - null
    - null
    metric_stds:
    - 0.0231
    - null
    - null
  - model: R-GIN + DIGL
    model_plain: R-GIN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8145
    - null
    - null
    metric_stds:
    - 0.0149
    - null
    - null
  - model: StableGCN
    model_plain: StableGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8145
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: EdgePool
    model_plain: EdgePool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8141
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
  - model: GK(k=3)
    model_plain: GK(k=3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: L2xGcn_dsc
    model_plain: L2xGcn_dsc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.14402'
    title: 'L2XGNN: Learning to Explain Graph Neural Networks'
    date: Sep 28, 2022
    date_iso: '2022-09-28'
    date_display: Sep 2022
    codebase_url: https://github.com/GiuseppeSerra93/L2XGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    metric_stds:
    - 0.092
    - null
    - null
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.00547'
    title: 'Performance Heterogeneity in Graph Neural Networks: Lessons for Architecture
      Design and Preprocessing'
    date: Mar 1, 2025
    date_iso: '2025-03-01'
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: HGP-SL_DEN
    model_plain: HGP-SL_DEN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8107
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
  - model: SubMix
    model_plain: SubMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8099
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: COMPGCN-SymCL
    model_plain: COMPGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8088
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Set2Set
    model_plain: Set2Set
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8084
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8078
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
  - model: RWGK
    model_plain: RWGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.07521'
    title: 'AGFormer: Efficient Graph Representation with Anchor-Graph Transformer'
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8077
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.06922'
    title: Decimated Framelet System on Graphs and Fast $ $-Framelet Transforms
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/YuGuangWang/FGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8072
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SUM
    model_plain: SUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8069
    - null
    - null
    metric_stds:
    - 0.0326
    - null
    - null
  - model: R-GIN + Last FA
    model_plain: R-GIN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    metric_stds:
    - 0.0164
    - null
    - null
  - model: AttrMasking
    model_plain: AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.09344'
    title: 'ifMixup: Interpolating Graph Pair to Regularize Graph Classification'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: PatchGT-DeeperGCN
    model_plain: PatchGT-DeeperGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: G-Mixup
    model_plain: G-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DGLC_d2
    model_plain: DGLC_d2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    metric_stds:
    - 0.0234
    - null
    - null
  - model: PGIB (SumPool)
    model_plain: PGIB (SumPool)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19906'
    title: Interpretable Prototype-based Graph Information Bottleneck
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/sang-woo-seo/PGIB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    metric_stds:
    - 0.1039
    - null
    - null
  - model: 6 GNNs
    model_plain: 6 GNNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8042
    - null
    - null
    metric_stds:
    - 0.0207
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8041
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
  - model: PatchGT-GCN
    model_plain: PatchGT-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: MEAN
    model_plain: MEAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8037
    - null
    - null
    metric_stds:
    - 0.0244
    - null
    - null
  - model: VGAE-Tuning
    model_plain: VGAE-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8035
    - null
    - null
    metric_stds:
    - 0.0616
    - null
    - null
  - model: p--RW
    model_plain: p--RW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: Mar 2016
    date_iso: 2016-03
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8033
    - null
    - null
    metric_stds:
    - 0.0135
    - null
    - null
  - model: gPool
    model_plain: gPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    metric_stds:
    - 0.0154
    - null
    - null
  - model: Node Dropping + Vanilla (GraphCL)
    model_plain: Node Dropping + Vanilla (GraphCL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12657'
    title: Explanation-Preserving Augmentation for Semi-Supervised Graph Representation
      Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/realMoana/EPA-GRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8025
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
  - model: EigenPool
    model_plain: EigenPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8011
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    metric_stds:
    - 0.0157
    - null
    - null
  - model: DC-SMGNN
    model_plain: DC-SMGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GNN graph classifier
    model_plain: GNN graph classifier
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11695'
    title: Global Counterfactual Explainer for Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/mertkosan/GCFExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7995
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
  - model: HGP-SL_HOP
    model_plain: HGP-SL_HOP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7988
    - null
    - null
    metric_stds:
    - 0.0109
    - null
    - null
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7984
    - null
    - null
    metric_stds:
    - 0.0246
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7981
    - null
    - null
    metric_stds:
    - 0.0158
    - null
    - null
  - model: M-Mixup
    model_plain: M-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: HP-1
    model_plain: HP-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: L2xGsg
    model_plain: L2xGsg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.14402'
    title: 'L2XGNN: Learning to Explain Graph Neural Networks'
    date: Sep 28, 2022
    date_iso: '2022-09-28'
    date_display: Sep 2022
    codebase_url: https://github.com/GiuseppeSerra93/L2XGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    metric_stds:
    - 0.081
    - null
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7972
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GCN + DIGL
    model_plain: GCN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
  - model: EigenPooling
    model_plain: EigenPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7948999999999999
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
  - model: HGP-SL_NS
    model_plain: HGP-SL_NS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7942
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: CompGCN
    model_plain: CompGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7929
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RWK
    model_plain: RWK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/lrnzgiusti/can
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: RW
    model_plain: RW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: JOAO+KM
    model_plain: JOAO+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
  - model: GIN0
    model_plain: GIN0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7903
    - null
    - null
    metric_stds:
    - 0.005600000000000001
    - null
    - null
  - model: DC-GISST
    model_plain: DC-GISST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DC-GSAT
    model_plain: DC-GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7889
    - null
    - null
    metric_stds:
    - 0.0205
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7886
    - null
    - null
    metric_stds:
    - 0.0115
    - null
    - null
  - model: MAX
    model_plain: MAX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7883
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: Uniform MaskNF
    model_plain: Uniform MaskNF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7875
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
  - model: Uniform DropNode
    model_plain: Uniform DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: MinCutPool
    model_plain: MinCutPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GCN + selective rewiring approach
    model_plain: GCN + selective rewiring approach
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.00547'
    title: 'Performance Heterogeneity in Graph Neural Networks: Lessons for Architecture
      Design and Preprocessing'
    date: Mar 1, 2025
    date_iso: '2025-03-01'
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7835
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: AutoGCL
    model_plain: AutoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: NoPool
    model_plain: NoPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11513'
    title: Towards Faithful Class-level Self-explainability in Graph Neural Networks
      by Subgraph Dependencies
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/FanzhenLiu/GraphOracle
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
  - model: GISST
    model_plain: GISST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DC-DIR
    model_plain: DC-DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
  - model: InfoGraph+KM
    model_plain: InfoGraph+KM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7795
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
  - model: DGLC_d1
    model_plain: DGLC_d1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7795
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
  - model: Feat
    model_plain: Feat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7794
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Uniform Mixture
    model_plain: Uniform Mixture
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7778
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RW+KM
    model_plain: RW+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7766
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: RW+SC
    model_plain: RW+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7765
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: GCN+GIB
    model_plain: GCN+GIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    metric_stds:
    - 0.075
    - null
    - null
  - model: HaarPool
    model_plain: HaarPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    metric_stds:
    - 0.0894
    - null
    - null
  - model: GCN+SIB
    model_plain: GCN+SIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    metric_stds:
    - 0.075
    - null
    - null
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.16944'
    title: Exact Computation of Any-Order Shapley Interactions for Graph Neural Networks
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/FFmgll/GraphSHAP-IQ
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    metric_stds:
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
    - 0.7714
    - null
    - null
    metric_stds:
    - 0.0814
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
    - 0.7711
    - null
    - null
    metric_stds:
    - 0.1005
    - null
    - null
  - model: GraphCL+KM
    model_plain: GraphCL+KM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
  - model: Uniform PerturbEdge
    model_plain: Uniform PerturbEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13248'
    title: Automated Data Augmentations for Graph Classification
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.764
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: 3-layer GCN
    model_plain: 3-layer GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09078'
    title: 'Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis
      of GNN Explanation Methods'
    date: Jun 16, 2021
    date_iso: '2021-06-16'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7632
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ECC
    model_plain: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7611
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SP+KM
    model_plain: SP+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7606
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: GraphSAGE+GIB
    model_plain: GraphSAGE+GIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    - null
    metric_stds:
    - 0.074
    - null
    - null
  - model: PK
    model_plain: PK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
  - model: GraphSAGE+SIB
    model_plain: GraphSAGE+SIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    - null
    metric_stds:
    - 0.074
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
    - 0.7566
    - null
    - null
    metric_stds:
    - 0.0867
    - null
    - null
  - model: GAT+SIB+DropEdge
    model_plain: GAT+SIB+DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    - null
    - null
    metric_stds:
    - 0.085
    - null
    - null
  - model: EigenPool
    model_plain: EigenPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    metric_stds:
    - 0.027
    - null
    - null
  - model: L2xGsg_dsc
    model_plain: L2xGsg_dsc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.14402'
    title: 'L2XGNN: Learning to Explain Graph Neural Networks'
    date: Sep 28, 2022
    date_iso: '2022-09-28'
    date_display: Sep 2022
    codebase_url: https://github.com/GiuseppeSerra93/L2XGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    - null
    - null
    metric_stds:
    - 0.077
    - null
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7502
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT+GIB
    model_plain: GAT+GIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    - null
    - null
    metric_stds:
    - 0.097
    - null
    - null
  - model: GAT+SIB
    model_plain: GAT+SIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    - null
    - null
    metric_stds:
    - 0.097
    - null
    - null
  - model: L2xGcn
    model_plain: L2xGcn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.14402'
    title: 'L2XGNN: Learning to Explain Graph Neural Networks'
    date: Sep 28, 2022
    date_iso: '2022-09-28'
    date_display: Sep 2022
    codebase_url: https://github.com/GiuseppeSerra93/L2XGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    - null
    metric_stds:
    - 0.082
    - null
    - null
  - model: ASAPool
    model_plain: ASAPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    metric_stds:
    - 0.077
    - null
    - null
  - model: GAT + DropEdge
    model_plain: GAT + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.11155'
    title: Recognizing Predictive Substructures with Subgraph Information Bottleneck
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    metric_stds:
    - 0.081
    - null
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7412000000000001
    - null
    - null
    metric_stds:
    - 0.061900000000000004
    - null
    - null
  - model: WL+KM
    model_plain: WL+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7394
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: WL-OA+KM
    model_plain: WL-OA+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7394
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: GWF+SC
    model_plain: GWF+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7392
    - null
    - null
    metric_stds:
    - 0.043
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.16944'
    title: Exact Computation of Any-Order Shapley Interactions for Graph Neural Networks
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: https://github.com/FFmgll/GraphSHAP-IQ
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RDF2Vec-SymCL
    model_plain: RDF2Vec-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7353
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GAT + FoSR
    model_plain: GAT + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.00547'
    title: 'Performance Heterogeneity in Graph Neural Networks: Lessons for Architecture
      Design and Preprocessing'
    date: Mar 1, 2025
    date_iso: '2025-03-01'
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
  - model: WL+SC
    model_plain: WL+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7323
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GraphCL+SC
    model_plain: GraphCL+SC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7322
    - null
    - null
    metric_stds:
    - 0.0266
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7287
    - null
    - null
    metric_stds:
    - 0.0684
    - null
    - null
  - model: SP+SC
    model_plain: SP+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7287
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7263
    - null
    - null
    metric_stds:
    - 0.102
    - null
    - null
  - model: InfoGraph+SC
    model_plain: InfoGraph+SC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7258
    - null
    - null
    metric_stds:
    - 0.0483
    - null
    - null
  - model: RGCN-SymCL
    model_plain: RGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7235
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN-concat
    model_plain: GCN-concat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7222
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7221
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN + None
    model_plain: GCN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7215
    - null
    - null
    metric_stds:
    - 0.0244
    - null
    - null
  - model: AttPool
    model_plain: AttPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05563'
    title: Graph Information Bottleneck for Subgraph Recognition
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    metric_stds:
    - 0.086
    - null
    - null
  - model: RDF2Vec
    model_plain: RDF2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7206
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ContextPred
    model_plain: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7175
    - null
    - null
    metric_stds:
    - 0.0734
    - null
    - null
  - model: sp
    model_plain: sp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7163
    - null
    - null
    metric_stds:
    - 0.0219
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7105
    - null
    - null
    metric_stds:
    - 0.0187
    - null
    - null
  - model: FF-GCN
    model_plain: FF-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
  - model: JOAO+SC
    model_plain: JOAO+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7072
    - null
    - null
    metric_stds:
    - 0.0285
    - null
    - null
  - model: GCN + Every FA
    model_plain: GCN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7045
    - null
    - null
    metric_stds:
    - 0.0196
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.00547'
    title: 'Performance Heterogeneity in Graph Neural Networks: Lessons for Architecture
      Design and Preprocessing'
    date: Mar 1, 2025
    date_iso: '2025-03-01'
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
  - model: GCN + Last FA
    model_plain: GCN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7005
    - null
    - null
    metric_stds:
    - 0.0203
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6953
    - null
    - null
    metric_stds:
    - 0.0077
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6865
    - null
    - null
    metric_stds:
    - 0.0431
    - null
    - null
  - model: VIB-GSL
    model_plain: VIB-GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6863
    - null
    - null
    metric_stds:
    - 0.0515
    - null
    - null
  - model: adaptive class-specific thresholds
    model_plain: adaptive class-specific thresholds
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.16606'
    title: 'GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain
      Adaptation'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/luo-junyu/GALA
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: Top-k
    model_plain: Top-k
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6761
    - null
    - null
    metric_stds:
    - 0.0336
    - null
    - null
  - model: WL-OA+SC
    model_plain: WL-OA+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6755
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.674
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RDF2Vec
    model_plain: RDF2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.672
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GK+SC
    model_plain: GK+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6702
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GWF+KM
    model_plain: GWF+KM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6694
    - null
    - null
    metric_stds:
    - 0.0768
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.11356'
    title: Fractal Graph Contrastive Learning
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6649
    - null
    - null
    metric_stds:
    - 0.0228
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6261
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: sub2vec
    model_plain: sub2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.01000'
    title: 'InfoGraph: Unsupervised and Semi-supervised Graph-Level Representation
      Learning via Mutual Information Maximization'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6105
    - null
    - null
    metric_stds:
    - 0.158
    - null
    - null
  - model: Grad-CAM
    model_plain: Grad-CAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.608
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.607
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PGM-Explainer
    model_plain: PGM-Explainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.603
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: CoT
    model_plain: CoT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5875
    - null
    - null
    metric_stds:
    - 0.1542
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/aidos-lab/rings
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57
    - null
    - null
    metric_stds:
    - 0.176
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5681
    - null
    - null
    metric_stds:
    - 0.1293
    - null
    - null
  - model: SA
    model_plain: SA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.568
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5665
    - null
    - null
    metric_stds:
    - 0.0174
    - null
    - null
  - model: LT+SC
    model_plain: LT+SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.02369'
    title: Deep Graph-Level Clustering Using Pseudo-Label-Guided Mutual Information
      Maximization Network
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.566
    - null
    - null
    metric_stds:
    - 0.0488
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5544
    - null
    - null
    metric_stds:
    - 0.1256
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5492
    - null
    - null
    metric_stds:
    - 0.1709
    - null
    - null
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.20815'
    title: GNN Explanations that do not Explain and How to find Them
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: https://github.com/steveazzolin/gnn_deg_expl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.535
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: 3D InfoGraph
    model_plain: 3D InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5317
    - null
    - null
    metric_stds:
    - 0.1729
    - null
    - null
  - model: ProG
    model_plain: ProG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5199
    - null
    - null
    metric_stds:
    - 0.045
    - null
    - null
  - model: OGMM
    model_plain: OGMM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4562
    - null
    - null
    metric_stds:
    - 0.1867
    - null
    - null
  - model: Multi-GFKD
    model_plain: Multi-GFKD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4436
    - null
    - null
    metric_stds:
    - 0.0842
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4344
    - null
    - null
    metric_stds:
    - 0.1514
    - null
    - null
  - model: GIN-B
    model_plain: GIN-B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4203
    - null
    - null
    metric_stds:
    - 0.1249
    - null
    - null
  - model: Inverse-X
    model_plain: Inverse-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3875
    - null
    - null
    metric_stds:
    - 0.1791
    - null
    - null
  - model: Uni-Soup
    model_plain: Uni-Soup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.374
    - null
    - null
    metric_stds:
    - 0.1203
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3733
    - null
    - null
    metric_stds:
    - 0.1081
    - null
    - null
  - model: Ens-HighConf
    model_plain: Ens-HighConf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3234
    - null
    - null
    metric_stds:
    - 0.0794
    - null
    - null
  - model: GCN (bb.)
    model_plain: GCN (bb.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3203
    - null
    - null
    metric_stds:
    - 0.0979
    - null
    - null
  - model: Avg-PTM
    model_plain: Avg-PTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3148
    - null
    - null
    metric_stds:
    - 0.0288
    - null
    - null
  - model: Greedy-Soup
    model_plain: Greedy-Soup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3146
    - null
    - null
    metric_stds:
    - 0.0623
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3125
    - null
    - null
    metric_stds:
    - 0.08
    - null
    - null
  - model: Ens-Prob
    model_plain: Ens-Prob
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2984
    - null
    - null
    metric_stds:
    - 0.0565
    - null
    - null
  - model: GIN-AK+
    model_plain: GIN-AK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2891
    - null
    - null
    metric_stds:
    - 0.0602
    - null
    - null
  - model: GAT-B
    model_plain: GAT-B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2781
    - null
    - null
    metric_stds:
    - 0.0286
    - null
    - null
  - model: AD-GAT
    model_plain: AD-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.03674'
    title: Out-of-Distribution Graph Models Merging
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2688
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.108
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.088
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.089
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.107
    - null
    - null
  - model: Nested GIN
    model_plain: Nested GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.082
    - null
    - null
  - model: SEG-BERT
    model_plain: SEG-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.065
    - null
    - null
  - model: UGNN
    model_plain: UGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
  - model: DiffPool-NoLP
    model_plain: DiffPool-NoLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: EigenGCN
    model_plain: EigenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Graph U-Net
    model_plain: Graph U-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.873
    - null
    metric_stds:
    - null
    - 0.013
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.727
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.783
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ATT
    model_plain: ATT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.765
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Gradient
    model_plain: Gradient
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2011.04573'
    title: Parameterized Explainer for Graph Neural Network
    date: Nov 2020
    date_iso: 2020-11
    date_display: Nov 2020
    codebase_url: https://github.com/flyingdoog/PGExplainer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.653
    - null
    metric_stds:
    - null
    - null
    - null
  - model: RAGE
    model_plain: RAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.877
    - null
    metric_stds:
    - null
    - 0.016
    - null
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.826
    - null
    metric_stds:
    - null
    - 0.013
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.843
    - null
    metric_stds:
    - null
    - 0.015
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.874
    - null
    metric_stds:
    - null
    - 0.012
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.88
    - null
    metric_stds:
    - null
    - 0.013
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.875
    - null
    metric_stds:
    - null
    - 0.014
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.864
    - null
    metric_stds:
    - null
    - 0.011
    - null
  - model: VIB-GSL
    model_plain: VIB-GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.833
    - null
    metric_stds:
    - null
    - 0.014
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.14578'
    title: 'GOAt: Explaining Graph Neural Networks via Graph Output Attribution'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/sluxsr/GOAt
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.012
    metric_stds:
    - null
    - null
    - null
  - model: SubgraphX
    model_plain: SubgraphX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.14578'
    title: 'GOAt: Explaining Graph Neural Networks via Graph Output Attribution'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/sluxsr/GOAt
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.002
    metric_stds:
    - null
    - null
    - null
  - model: RCExplainer
    model_plain: RCExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.14578'
    title: 'GOAt: Explaining Graph Neural Networks via Graph Output Attribution'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/sluxsr/GOAt
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.004
    metric_stds:
    - null
    - null
    - null
  - model: GOAT
    model_plain: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.14578'
    title: 'GOAt: Explaining Graph Neural Networks via Graph Output Attribution'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/sluxsr/GOAt
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.035
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 0.858
    std: 0.002
    model: sp
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: 2014-10
  - value: 0.8794
    std: 0.0161
    model: MLG
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: 2016-03
  - value: 0.9263
    std: 0.0421
    model: PATCHY-SAN
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: 2019-01
  - value: 0.939
    std: 0.04
    model: MPNN
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: 2019-12
  - value: 0.963
    std: null
    model: GCN (trained for XGNN)
    arxiv_id: '2006.02587'
    title: 'XGNN: Towards Model-Level Explanations of Graph Neural Networks'
    date: 2020-06
  - value: 0.9674
    std: 0.0455
    model: novel SUbG rAph neural network
    arxiv_id: '2101.08170'
    title: 'SUGAR: Subgraph Neural Network with Reinforcement Pooling and Self-Supervised
      Mutual Information Mechanism'
    date: 2021-01
  - value: 0.9805
    std: null
    model: Base (GCN)
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: 2022-02
  - value: 0.983
    std: 0.025
    model: SVMs
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: 2022-03
  - value: 0.986
    std: null
    model: RC-Explainer
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: 2022-04
---

