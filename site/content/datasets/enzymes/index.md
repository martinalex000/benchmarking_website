---
title: ENZYMES
slug: enzymes
benchmark: TU Dortmund
task_type: graph_classification
description: TU Dortmund graph classification on 6 enzyme reaction classes (600 graphs,
  subset of BRENDA database).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 600
  avg_nodes: 32.6
  avg_edges: 62.1
  num_classes: 6
result_count: 183
best_model:
  model: C-M
  value: 0.802
  metric: Accuracy
  arxiv_id: '2301.10857'
  paper_title: arXiv:2301.10857
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
  rows:
  - model: C-M
    model_plain: C-M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.802
    metric_stds:
    - 0.009
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
    is_best: true
    metric_values:
    - 0.794
    metric_stds:
    - 0.008
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.785
    metric_stds:
    - 0.01
  - model: H2GCN
    model_plain: H2GCN
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
    is_best: true
    metric_values:
    - 0.78
    metric_stds:
    - 0.0489
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    metric_stds:
    - 0.011
  - model: Graphormer
    model_plain: Graphormer
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
    - 0.778
    metric_stds:
    - 0.009
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.012
  - model: OOD-GMixup
    model_plain: OOD-GMixup
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    metric_stds:
    - 0.004
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
    - 0.762
    metric_stds:
    - 0.01
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    metric_stds:
    - 0.015
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    metric_stds:
    - 0.018
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
    - 0.756
    metric_stds:
    - 0.011
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    metric_stds:
    - 0.021
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
    - 0.741
    metric_stds:
    - 0.014
  - model: GSO
    model_plain: GSO
    is_baseline: false
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
    is_best: true
    metric_values:
    - 0.735
    metric_stds:
    - 0.0639
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
    - 0.729
    metric_stds:
    - 0.0755
  - model: PGCN_n + DropNode
    model_plain: PGCN_n + DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    metric_stds:
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
    - 0.7017
    metric_stds:
    - 0.0558
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
    - 0.7
    metric_stds:
    - 0.035
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
    - 0.695
    metric_stds:
    - 0.0737
  - model: FL
    model_plain: FL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6949
    metric_stds:
    - 0.0181
  - model: MSA-AU
    model_plain: MSA-AU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.694
    metric_stds:
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
    - 0.6879
    metric_stds:
    - 0.0211
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
    - 0.6817
    metric_stds:
    - 0.057
  - model: FedSage
    model_plain: FedSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6795
    metric_stds:
    - 0.0187
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
    - 0.6783
    metric_stds:
    - 0.061
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
    - 0.6783
    metric_stds:
    - 0.0687
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
    - 0.6767
    metric_stds:
    - 0.0374
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
    - 0.6767
    metric_stds:
    - 0.0374
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
    - 0.675
    metric_stds:
    - 0.0642
  - model: Local
    model_plain: Local
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6691
    metric_stds:
    - 0.0284
  - model: MSA-AD
    model_plain: MSA-AD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.669
    metric_stds:
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
    - 0.6683
    metric_stds:
    - 0.0508
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
    - 0.665
    metric_stds:
    - 0.0691
  - model: GCN + 2FC
    model_plain: GCN + 2FC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6645
    metric_stds:
    - null
  - model: GCFL
    model_plain: GCFL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6631
    metric_stds:
    - 0.0236
  - model: FCN (2FC)
    model_plain: FCN (2FC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6617
    metric_stds:
    - null
  - model: PGCN_g+2FC
    model_plain: PGCN_g+2FC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6617
    metric_stds:
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
    - 0.6583
    metric_stds:
    - 0.0593
  - model: GCN-4
    model_plain: GCN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.046
  - model: GATED-GCN-4
    model_plain: GATED-GCN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    metric_stds:
    - 0.049
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
    - 0.6533
    metric_stds:
    - 0.0436
  - model: FedProx
    model_plain: FedProx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6518
    metric_stds:
    - 0.0201
  - model: FedAvg
    model_plain: FedAvg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6486
    metric_stds:
    - 0.0273
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
    - 0.6457
    metric_stds:
    - 0.0453
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
    - 0.645
    metric_stds:
    - 0.0592
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
    - 0.645
    metric_stds:
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
    - 0.645
    metric_stds:
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
    - 0.6397
    metric_stds:
    - 0.0251
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
    - 0.6351
    metric_stds:
    - 0.0264
  - model: MOSGSL
    model_plain: MOSGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    metric_stds:
    - 0.054
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
    - 0.6333
    metric_stds:
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
    - 0.6253
    metric_stds:
    - null
  - model: Diff-Pool (Soft Assign)
    model_plain: Diff-Pool (Soft Assign)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6253
    metric_stds:
    - null
  - model: FedPer
    model_plain: FedPer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.13009'
    title: My Publication Title --- Single Author
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yuetan031/FedStar
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6223
    metric_stds:
    - 0.0376
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
    - 0.6216
    metric_stds:
    - 0.0211
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
    - 0.6195
    metric_stds:
    - null
  - model: GCAPS-CNN
    model_plain: GCAPS-CNN
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
    - 0.6183
    metric_stds:
    - 0.0539
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
    - 0.6181
    metric_stds:
    - 0.0099
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
    - 0.611
    metric_stds:
    - null
  - model: CLIQUEPOOL
    model_plain: CLIQUEPOOL
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
    - 0.6071
    metric_stds:
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6033
    metric_stds:
    - 0.0661
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
    - 0.6018
    metric_stds:
    - 0.0243
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
    - 0.6015
    metric_stds:
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
    - 0.6013
    metric_stds:
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
    - 0.596
    metric_stds:
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
    - 0.591
    metric_stds:
    - 0.011
  - model: WL-OA
    model_plain: WL-OA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.589
    metric_stds:
    - 0.009
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
    - 0.5845
    metric_stds:
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
    - 0.5833
    metric_stds:
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
    - 0.5832
    metric_stds:
    - 0.0264
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
    - 0.5712
    metric_stds:
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
    - 0.57
    metric_stds:
    - 0.014
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
    - 0.566
    metric_stds:
    - 0.006
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
    - 0.566
    metric_stds:
    - 0.031
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
    - 0.565
    metric_stds:
    - 0.0713
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.555
    metric_stds:
    - 0.0511
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
    - 0.551
    metric_stds:
    - 0.016
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
    - 0.551
    metric_stds:
    - 0.22
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
    - 0.5467
    metric_stds:
    - 0.0999
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
    - 0.5467
    metric_stds:
    - 0.0567
  - model: T-RND
    model_plain: T-RND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.546
    metric_stds:
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
    - 0.5425
    metric_stds:
    - null
  - model: Diff-Pool (GraphSAGE)
    model_plain: Diff-Pool (GraphSAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5425
    metric_stds:
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
    - 0.5417
    metric_stds:
    - 0.0625
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.54
    metric_stds:
    - 0.0517
  - model: WL
    model_plain: WL
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
    - 0.5375
    metric_stds:
    - 0.0137
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
    - 0.5366
    metric_stds:
    - 0.0607
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
    - 0.535
    metric_stds:
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
    - 0.5343
    metric_stds:
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
    - 0.5343
    metric_stds:
    - 0.0091
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
    - 0.532
    metric_stds:
    - 0.006
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
    - 0.527
    metric_stds:
    - 0.232
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5267
    metric_stds:
    - 0.0754
  - model: GCN Baseline
    model_plain: GCN Baseline
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
    - 0.526
    metric_stds:
    - 0.014
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
    - 0.52
    metric_stds:
    - 0.0072
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.519
    metric_stds:
    - null
  - model: GAT-3-TOGL-1
    model_plain: GAT-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.515
    metric_stds:
    - 0.073
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
    - 0.51
    metric_stds:
    - 0.0729
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
    - 0.506
    metric_stds:
    - 0.021
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
    - 0.5017
    metric_stds:
    - null
  - model: GIN-4
    model_plain: GIN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5
    metric_stds:
    - 0.123
  - model: HGP-SL
    model_plain: HGP-SL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4967
    metric_stds:
    - 0.0942
  - model: JbDA
    model_plain: JbDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.494
    metric_stds:
    - null
  - model: Graph U-Net
    model_plain: Graph U-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4833
    metric_stds:
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
    - 0.477
    metric_stds:
    - 0.021
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4683
    metric_stds:
    - 0.0776
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
    - 0.468
    metric_stds:
    - 0.011
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
    - 0.4567
    metric_stds:
    - null
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4533
    metric_stds:
    - 0.0587
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
    - 0.45
    metric_stds:
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
    - 0.4399
    metric_stds:
    - 0.0423
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
    - 0.4383
    metric_stds:
    - 0.0516
  - model: GCN-3-TOGL-1
    model_plain: GCN-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.438
    metric_stds:
    - 0.079
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
    - 0.4366
    metric_stds:
    - 0.0339
  - model: MSA-Real
    model_plain: MSA-Real
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.435
    metric_stds:
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
    - 0.4333
    metric_stds:
    - 0.0288
  - model: VIBGSL
    model_plain: VIBGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.425
    metric_stds:
    - 0.0453
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
    - 0.4232
    metric_stds:
    - null
  - model: sp
    model_plain: sp
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
    - 0.4231
    metric_stds:
    - 0.0137
  - model: GAUG
    model_plain: GAUG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08897'
    title: Motif-driven Subgraph Structure Learning for Graph Classification
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4117
    metric_stds:
    - 0.0758
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
    - 0.4103
    metric_stds:
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
    - 0.4
    metric_stds:
    - 0.04
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
    - 0.3983
    metric_stds:
    - 0.0368
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
    - 0.392
    metric_stds:
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
    - 0.387
    metric_stds:
    - 0.014
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
    - 0.38
    metric_stds:
    - 0.06
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
    - 0.3799
    metric_stds:
    - 0.0371
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
    - 0.379
    metric_stds:
    - 0.018
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
    - 0.377
    metric_stds:
    - 0.015
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
    - 0.376
    metric_stds:
    - 0.009
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
    - 0.37
    metric_stds:
    - 0.05
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
    - 0.37
    metric_stds:
    - 0.05
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
    - 0.3577
    metric_stds:
    - 0.0593
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
    - 0.341
    metric_stds:
    - 0.017
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
    - 0.3316
    metric_stds:
    - 0.0321
  - model: GK
    model_plain: GK
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
    - 0.327
    metric_stds:
    - 0.012
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
    - 0.323
    metric_stds:
    - 0.017
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
    - 0.3216
    metric_stds:
    - 0.0387
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
    - 0.315
    metric_stds:
    - 0.018
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
    - 0.31
    metric_stds:
    - 0.03
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.307
    metric_stds:
    - 0.022
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
    - 0.2916
    metric_stds:
    - 0.0563
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
    - 0.29
    metric_stds:
    - 0.08
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
    - 0.2855
    metric_stds:
    - 0.002
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
    - 0.2817
    metric_stds:
    - 0.0076
  - model: GCN + FoSR
    model_plain: GCN + FoSR
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
    - 0.272
    metric_stds:
    - 0.011
  - model: GIN
    model_plain: GIN
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
    - 0.271
    metric_stds:
    - 0.016
  - model: end-to-end graph-level clustering method
    model_plain: end-to-end graph-level clustering method
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
    - 0.2708
    metric_stds:
    - 0.0149
  - model: GAT-4
    model_plain: GAT-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.268
    metric_stds:
    - 0.041
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    metric_stds:
    - 0.0428
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
    - 0.263
    metric_stds:
    - 0.012
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
    - 0.26
    metric_stds:
    - 0.02
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
    - 0.2566
    metric_stds:
    - 0.0157
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
    - 0.2528
    metric_stds:
    - 0.0028
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
    - 0.2465
    metric_stds:
    - 0.0044
  - model: RW
    model_plain: RW
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
    - 0.2416
    metric_stds:
    - 0.0164
  - model: GCN
    model_plain: GCN
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
    - 0.238
    metric_stds:
    - 0.013
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
    - 0.238
    metric_stds:
    - 0.012
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
    - 0.2375
    metric_stds:
    - 0.005
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2341
    metric_stds:
    - 0.0479
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2333
    metric_stds:
    - 0.0425
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
    - 0.2317
    metric_stds:
    - 0.0
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2267
    metric_stds:
    - 0.0478
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2233
    metric_stds:
    - 0.0501
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
    - 0.2217
    metric_stds:
    - 0.0
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
    - 0.2206
    metric_stds:
    - 0.0098
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
    - 0.22
    metric_stds:
    - 0.0
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
    - 0.2166
    metric_stds:
    - 0.0037
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.215
    metric_stds:
    - 0.045
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
    - 0.215
    metric_stds:
    - 0.0022
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
    - 0.215
    metric_stds:
    - 0.0
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2133
    metric_stds:
    - 0.0562
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
    - 0.21
    metric_stds:
    - 0.0
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
    - 0.2083
    metric_stds:
    - 0.0
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2067
    metric_stds:
    - 0.0549
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.205
    metric_stds:
    - 0.0402
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
    - 0.2
    metric_stds:
    - 0.0
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1933
    metric_stds:
    - 0.0761
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
    - 0.1707
    metric_stds:
    - 0.0013
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
    - 0.17
    metric_stds:
    - 0.0
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
    - 0.17
    metric_stds:
    - 0.0009
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
    - 0.1095
    metric_stds:
    - 0.0069
  milestones:
  - value: 0.6181
    std: 0.0099
    model: MLG
    arxiv_id: '1603.06186'
    title: arXiv:1603.06186
    date: 2016-03
  - value: 0.6333
    std: null
    model: S2V with 1 DiffPool
    arxiv_id: '1806.08804'
    title: Hierarchical Graph Representation Learning with Differentiable Pooling
    date: 2018-06
  - value: 0.7017
    std: 0.0558
    model: GFN
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: 2019-05
  - value: 0.705
    std: null
    model: PGCN_n + DropNode
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: 2020-08
  - value: 0.78
    std: 0.0489
    model: H2GCN
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: 2020-12
  - value: 0.802
    std: 0.009
    model: C-M
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: 2023-01
---

