---
title: NCI1
slug: nci1
benchmark: TU Dortmund
task_type: graph_classification
description: Graph classification of chemical compounds screened for anti-cancer activity.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 4110
  avg_nodes: 29.87
  avg_edges: 32.3
  num_classes: 2
result_count: 287
best_model:
  model: MSA-AU
  value: 0.962
  metric: Accuracy
  arxiv_id: '2312.10943'
  paper_title: Model Stealing Attack against Graph Classification with Authenticity,
    Uncertainty and Diversity
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
  - ACC
  rows:
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
    is_best: true
    metric_values:
    - 0.962
    - null
    metric_stds:
    - null
    - null
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
    - 0.947
    - null
    metric_stds:
    - null
    - null
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
    - 0.912
    - null
    metric_stds:
    - null
    - null
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
    - 0.91
    - null
    metric_stds:
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
    - 0.874
    - null
    metric_stds:
    - 0.003
    - null
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
    - 0.873
    - null
    metric_stds:
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
    - 0.862
    - null
    metric_stds:
    - 0.004
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
    - 0.86
    - null
    metric_stds:
    - 0.018
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
    - 0.859
    - null
    metric_stds:
    - 0.001
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 0.858
    - null
    metric_stds:
    - 0.005
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
    - 0.8578
    - null
    metric_stds:
    - 0.0207
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
    - 0.8532
    - null
    metric_stds:
    - 0.0034
    - null
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
    - 0.8512
    - null
    metric_stds:
    - 0.0029
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
    - 0.851
    - null
    metric_stds:
    - 0.003
    - null
  - model: WL sp
    model_plain: WL sp
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
    - 0.8455
    - null
    metric_stds:
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
    - 0.845
    - null
    metric_stds:
    - 0.004
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
    metric_stds:
    - 0.001
    - null
  - model: WL edge
    model_plain: WL edge
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
    - 0.8437
    - null
    metric_stds:
    - null
    - null
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
    - 0.843
    - null
    metric_stds:
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
    - 0.842
    - null
    metric_stds:
    - 0.015
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
    is_best: false
    metric_values:
    - 0.84
    - null
    metric_stds:
    - 0.016
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
    is_best: false
    metric_values:
    - 0.8391
    - null
    metric_stds:
    - 0.0127
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
    - 0.838
    - null
    metric_stds:
    - 0.006
    - null
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
    is_best: false
    metric_values:
    - 0.8372
    - null
    metric_stds:
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
    - 0.8365
    - null
    metric_stds:
    - 0.0169
    - null
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
    is_best: false
    metric_values:
    - 0.8362
    - null
    metric_stds:
    - 0.0138
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
    is_best: false
    metric_values:
    - 0.836
    - null
    metric_stds:
    - 0.012
    - null
  - model: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8352
    - null
    metric_stds:
    - 0.0375
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
    is_best: false
    metric_values:
    - 0.835
    - null
    metric_stds:
    - 0.02
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
    - 0.835
    - null
    metric_stds:
    - 0.002
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
    - 0.8345
    - null
    metric_stds:
    - 0.0178
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
    - 0.834
    - null
    metric_stds:
    - 0.0123
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
    - 0.8307
    - null
    metric_stds:
    - 0.0154
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
    - 0.8304
    - null
    metric_stds:
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
    - 0.83
    - null
    metric_stds:
    - 0.0189
    - null
  - model: CoCN
    model_plain: CoCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8289
    - null
    metric_stds:
    - 0.0019
    - null
  - model: PG
    model_plain: PG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    metric_stds:
    - 0.013
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
    - 0.8277
    - null
    metric_stds:
    - 0.0149
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
    - 0.8272
    - null
    metric_stds:
    - 0.0171
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
    - 0.8271
    - null
    metric_stds:
    - 0.0164
    - null
  - model: SIN
    model_plain: SIN
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
    - 0.827
    - null
    metric_stds:
    - 0.021
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.827
    - null
    metric_stds:
    - 0.017
    - null
  - model: GRED (K=10)
    model_plain: GRED (K=10)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.826
    - null
    metric_stds:
    - 0.014
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
    - 0.8258
    - null
    metric_stds:
    - 0.0179
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
    - 0.825
    - null
    metric_stds:
    - 0.005
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
    - 0.8246
    - null
    metric_stds:
    - 0.0024
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
    - 0.824
    - null
    metric_stds:
    - 0.013
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
    - 0.8237
    - null
    metric_stds:
    - 0.0224
    - null
  - model: GraphTrans (large)
    model_plain: GraphTrans (large)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    - null
    metric_stds:
    - 0.026
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
    - 0.823
    - null
    metric_stds:
    - 0.026
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
    - 0.8224
    - null
    metric_stds:
    - 0.0124
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
    - 0.8221
    - null
    metric_stds:
    - 0.0042
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
    is_best: false
    metric_values:
    - 0.822
    - null
    metric_stds:
    - 0.014
    - null
  - model: WL subtree
    model_plain: WL subtree
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
    - 0.8219
    - null
    metric_stds:
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
    - 0.8219
    - null
    metric_stds:
    - 0.0018
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
    - 0.819
    - null
    metric_stds:
    - 0.004
    - null
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
    - 0.818
    - null
    metric_stds:
    - 0.009
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
    - 0.8161
    - null
    metric_stds:
    - 0.0178
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
    - 0.816
    - null
    metric_stds:
    - 0.001
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
    - 0.815
    - null
    metric_stds:
    - 0.011
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
    - 0.8146
    - null
    metric_stds:
    - 0.0151
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
    - 0.8143
    - null
    metric_stds:
    - 0.0165
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
    - 0.8139
    - null
    metric_stds:
    - 0.0192
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
    - 0.8131
    - null
    metric_stds:
    - 0.0022
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
    - 0.8129
    - null
    metric_stds:
    - 0.0122
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
    - 0.8113
    - null
    metric_stds:
    - 0.0043
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
    - 0.8112
    - null
    metric_stds:
    - 0.0128
    - null
  - model: novel message passing scheme
    model_plain: novel message passing scheme
    is_baseline: false
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
    - 0.8111
    - null
    metric_stds:
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
    - 0.811
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.81
    - null
    metric_stds:
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
    - 0.8098
    - null
    metric_stds:
    - 0.0196
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
    - 0.808
    - null
    metric_stds:
    - 0.004
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
    - 0.8079
    - null
    metric_stds:
    - 0.0124
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
    - 0.807
    - null
    metric_stds:
    - 0.013
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
    - 0.8067
    - null
    metric_stds:
    - 0.0116
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
    - 0.8064
    - null
    metric_stds:
    - 0.0246
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
    - 0.805
    - null
    metric_stds:
    - 0.019
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
    - 0.805
    - null
    metric_stds:
    - 0.019
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
    - 0.805
    - null
    metric_stds:
    - 0.0016
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8046
    - null
    metric_stds:
    - 0.0017
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
    - 0.8042
    - null
    metric_stds:
    - 0.0035
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
    - 0.804
    - null
    metric_stds:
    - 0.003
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
    - 0.804
    - null
    metric_stds:
    - 0.002
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
    - 0.8036
    - null
    metric_stds:
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8031
    - null
    metric_stds:
    - 0.0046
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
    - 0.8031
    - null
    metric_stds:
    - 0.0046
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
    - 0.803
    - null
    metric_stds:
    - 0.003
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
    - 0.8021
    - null
    metric_stds:
    - 0.0202
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    metric_stds:
    - 0.006
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
    - 0.802
    - null
    metric_stds:
    - 0.011
    - null
  - model: GraphTrans
    model_plain: GraphTrans
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
    - 0.8018
    - null
    metric_stds:
    - 0.0197
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
    - 0.8013
    - null
    metric_stds:
    - 0.0233
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
    - 0.8002
    - null
    metric_stds:
    - 0.0228
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.8
    - null
    metric_stds:
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
    - 0.7994
    - null
    metric_stds:
    - 0.0159
    - null
  - model: SGCL
    model_plain: SGCL
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
    - 0.7984
    - null
    metric_stds:
    - 0.0023
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
    - 0.7972
    - null
    metric_stds:
    - 0.0053
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
    - 0.7971
    - null
    metric_stds:
    - 0.0013
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
    - 0.796
    - null
    metric_stds:
    - 0.018
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
    - 0.7949
    - null
    metric_stds:
    - 0.0017
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
    - 0.794
    - null
    metric_stds:
    - 0.002
    - null
  - model: SEP
    model_plain: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7935
    - null
    metric_stds:
    - 0.0033
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
    - 0.7922
    - null
    metric_stds:
    - 0.0009
    - null
  - model: GraphTrans (small)
    model_plain: GraphTrans (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - 0.022
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
    - 0.792
    - null
    metric_stds:
    - 0.018
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
    - 0.791
    - null
    metric_stds:
    - 0.014
    - null
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
    - 0.7903
    - null
    metric_stds:
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
    - 0.7902
    - null
    metric_stds:
    - 0.0189
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
    - 0.79
    - null
    metric_stds:
    - 0.018
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
    - 0.789
    - null
    metric_stds:
    - 0.001
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
    - 0.789
    - null
    metric_stds:
    - 0.031
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
    - 0.7884
    - null
    metric_stds:
    - null
    - null
  - model: GIND
    model_plain: GIND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    metric_stds:
    - 0.017
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
    - 0.7878
    - null
    metric_stds:
    - 0.0109
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
    - 0.7876
    - null
    metric_stds:
    - 0.0061
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
    - 0.7871
    - null
    metric_stds:
    - 0.0218
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
    metric_stds:
    - 0.003
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
    - 0.7869
    - null
    metric_stds:
    - 0.0018
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
    - 0.7866
    - null
    metric_stds:
    - 0.0034
    - null
  - model: StructPool
    model_plain: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7864
    - null
    metric_stds:
    - 0.0153
    - null
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    metric_stds:
    - 0.019
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7856
    - null
    metric_stds:
    - 0.0026
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
    - 0.7852
    - null
    metric_stds:
    - 0.0017
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
    - 0.785
    - null
    metric_stds:
    - 0.023
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
    - 0.784
    - null
    metric_stds:
    - 0.025
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
    - 0.784
    - null
    metric_stds:
    - 0.021
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
    - 0.7835
    - null
    metric_stds:
    - 0.0155
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
    - 0.783
    - null
    metric_stds:
    - 0.003
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
    - 0.7823
    - null
    metric_stds:
    - 0.0131
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
    - 0.7821
    - null
    metric_stds:
    - 0.0258
    - null
  - model: SPN (K=10)
    model_plain: SPN (K=10)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    - null
    metric_stds:
    - 0.012
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
    - 0.7819
    - null
    metric_stds:
    - 0.0239
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
    - 0.7814
    - null
    metric_stds:
    - 0.0108
    - null
  - model: GCFExplainer
    model_plain: GCFExplainer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11695'
    title: Global Counterfactual Explainer for Graph Neural Networks
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/mertkosan/GCFExplainer
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7809
    - null
    metric_stds:
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
    - 0.7807
    - null
    metric_stds:
    - 0.0047
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
    - 0.78
    - null
    metric_stds:
    - 0.002
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
    - 0.7797
    - null
    metric_stds:
    - 0.0222
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
    - 0.7788
    - null
    metric_stds:
    - 0.0124
    - null
  - model: GraphCL
    model_plain: GraphCL
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
    - 0.7787
    - null
    metric_stds:
    - 0.0041
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
    - 0.7781
    - null
    metric_stds:
    - 0.0052
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
    - 0.778
    - null
    metric_stds:
    - 0.016
    - null
  - model: EGG
    model_plain: EGG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    - null
    metric_stds:
    - 0.0201
    - null
  - model: CGS
    model_plain: CGS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    metric_stds:
    - 0.02
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
    - 0.7754
    - null
    metric_stds:
    - 0.0224
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
    - 0.775
    - null
    metric_stds:
    - 0.023
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
    - 0.773
    - null
    metric_stds:
    - 0.0178
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
    - 0.772
    - null
    metric_stds:
    - 0.0022
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
    - 0.7713
    - null
    metric_stds:
    - 0.0149
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
    - 0.7696
    - null
    metric_stds:
    - 0.017
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
    - 0.7671
    - null
    metric_stds:
    - 0.0183
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    - null
    metric_stds:
    - 0.018
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
    - 0.7661
    - null
    metric_stds:
    - 0.0139
    - null
  - model: TwoHop
    model_plain: TwoHop
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
    - 0.7642
    - null
    metric_stds:
    - 0.0383
    - null
  - model: GCNFA
    model_plain: GCNFA
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
    - 0.7639
    - null
    metric_stds:
    - 0.0372
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
    - 0.7637
    - null
    metric_stds:
    - 0.0175
    - null
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7635
    - null
    metric_stds:
    - 0.0262
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
    - 0.7634
    - null
    metric_stds:
    - 0.0168
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
    - 0.7632
    - null
    metric_stds:
    - 0.0122
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
    - 0.762
    - null
    metric_stds:
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
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
    - 0.762
    - null
    metric_stds:
    - 0.0106
    - null
  - model: WL
    model_plain: WL
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
    - 0.7619
    - null
    metric_stds:
    - 0.0245
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
    - 0.7599
    - null
    metric_stds:
    - 0.0142
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
    - 0.7596
    - null
    metric_stds:
    - 0.0182
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
    - 0.7591
    - null
    metric_stds:
    - 0.0361
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
    - 0.7591
    - null
    metric_stds:
    - 0.0184
    - null
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
    - 0.759
    - null
    metric_stds:
    - null
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
    - 0.7584
    - null
    metric_stds:
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
    - 0.7581
    - null
    metric_stds:
    - 0.0268
    - null
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
    - 0.758
    - null
    metric_stds:
    - 0.018
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
    - 0.7574
    - null
    metric_stds:
    - 0.0147
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
    - 0.7533
    - null
    metric_stds:
    - 0.0215
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
    - 0.753
    - null
    metric_stds:
    - 0.0145
    - null
  - model: MVGRL
    model_plain: MVGRL
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
    - 0.7517
    - null
    metric_stds:
    - 0.007
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
    - 0.7511
    - null
    metric_stds:
    - 0.0345
    - null
  - model: GCN-1-TOGL-1 (static)
    model_plain: GCN-1-TOGL-1 (static)
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
    - 0.751
    - null
    metric_stds:
    - 0.012
    - null
  - model: rLap
    model_plain: rLap
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
    - 0.7506
    - null
    metric_stds:
    - 0.0165
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
    - 0.7503
    - null
    metric_stds:
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
    - 0.749
    - null
    metric_stds:
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
    - 0.7486
    - null
    metric_stds:
    - 0.0026
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
    - 0.7458
    - null
    metric_stds:
    - 0.0399
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
    - 0.7444
    - null
    metric_stds:
    - 0.0047
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
    - 0.744
    - null
    metric_stds:
    - 0.001
    - null
  - model: EdgeDroppingDegree
    model_plain: EdgeDroppingDegree
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
    - 0.744
    - null
    metric_stds:
    - 0.0165
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
    - 0.7436
    - null
    metric_stds:
    - 0.0024
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
    - 0.7417
    - null
    metric_stds:
    - 0.0289
    - null
  - model: DiffPool
    model_plain: DiffPool
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
    - 0.741
    - null
    metric_stds:
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
    - 0.7404
    - null
    metric_stds:
    - 0.0127
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
    - 0.7402
    - null
    metric_stds:
    - 0.0118
    - null
  - model: RandomWalkSubgraph
    model_plain: RandomWalkSubgraph
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
    - 0.7401
    - null
    metric_stds:
    - 0.0247
    - null
  - model: GCNFA(L8)
    model_plain: GCNFA(L8)
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
    - 0.7393
    - null
    metric_stds:
    - 0.0287
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
    - 0.7391
    - null
    metric_stds:
    - 0.0077
    - null
  - model: InfoGraph
    model_plain: InfoGraph
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
    - 0.7382
    - null
    metric_stds:
    - 0.0071
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
    - 0.737
    - null
    metric_stds:
    - 0.0255
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
    - 0.737
    - null
    metric_stds:
    - 0.002
    - null
  - model: AVG
    model_plain: AVG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    - null
    metric_stds:
    - 0.0255
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
    - 0.7366
    - null
    metric_stds:
    - 0.0169
    - null
  - model: NodeDropping
    model_plain: NodeDropping
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
    - 0.7365
    - null
    metric_stds:
    - 0.0261
    - null
  - model: PersLay
    model_plain: PersLay
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
    - 0.735
    - null
    metric_stds:
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    metric_stds:
    - 0.019
    - null
  - model: sp
    model_plain: sp
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
    - 0.7347
    - null
    metric_stds:
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
    - 0.7346
    - null
    metric_stds:
    - 0.0032
    - null
  - model: EdgeAddition
    model_plain: EdgeAddition
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
    - 0.7336
    - null
    metric_stds:
    - 0.0181
    - null
  - model: PPRDiffusion
    model_plain: PPRDiffusion
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
    - 0.7336
    - null
    metric_stds:
    - 0.0234
    - null
  - model: graph2vec
    model_plain: graph2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7322
    - null
    metric_stds:
    - 0.0181
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
    - 0.732
    - null
    metric_stds:
    - 0.001
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
    - 0.73
    - null
    metric_stds:
    - 0.003
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
    - 0.728
    - null
    metric_stds:
    - 0.015
    - null
  - model: EdgeDroppingEVC
    model_plain: EdgeDroppingEVC
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
    - 0.7265
    - null
    metric_stds:
    - 0.0232
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
    - 0.7241
    - null
    metric_stds:
    - 0.0018
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
    - 0.7212
    - null
    metric_stds:
    - null
    - null
  - model: MarkovDiffusion
    model_plain: MarkovDiffusion
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
    - 0.7183
    - null
    metric_stds:
    - 0.025
    - null
  - model: DiffPool
    model_plain: DiffPool
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
    - 0.7148
    - null
    metric_stds:
    - 0.0246
    - null
  - model: EdgeDroppingPR
    model_plain: EdgeDroppingPR
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
    - 0.7129
    - null
    metric_stds:
    - 0.0308
    - null
  - model: GFL
    model_plain: GFL
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
    - 0.712
    - null
    metric_stds:
    - 0.021
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.707
    - null
    metric_stds:
    - 0.0169
    - null
  - model: GCNVIR
    model_plain: GCNVIR
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
    - 0.7032
    - null
    metric_stds:
    - 0.0432
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
    - 0.7011
    - null
    metric_stds:
    - 0.0186
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    metric_stds:
    - 0.023
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
    - 0.7007
    - null
    metric_stds:
    - 0.0055
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
    - 0.6987
    - null
    metric_stds:
    - 0.0104
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
    - 0.6978
    - null
    metric_stds:
    - 0.0116
    - null
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
    - 0.6969
    - null
    metric_stds:
    - null
    - null
  - model: AD-GCL
    model_plain: AD-GCL
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
    - 0.6967
    - null
    metric_stds:
    - 0.0051
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
    - 0.6961
    - null
    metric_stds:
    - 0.0149
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
    - 0.6935
    - null
    metric_stds:
    - 0.0063
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
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
    - 0.6903
    - null
    metric_stds:
    - null
    - null
  - model: GEM
    model_plain: GEM
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
    - 0.6903
    - null
    metric_stds:
    - null
    - null
  - model: CF^2
    model_plain: CF^2
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
    - 0.6903
    - null
    metric_stds:
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
    - 0.6861
    - null
    metric_stds:
    - 0.0231
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
    - 0.686
    - null
    metric_stds:
    - 0.037
    - null
  - model: SortPool
    model_plain: SortPool
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
    - 0.6859
    - null
    metric_stds:
    - 0.0067
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
    - 0.6854
    - null
    metric_stds:
    - 0.0055
    - null
  - model: InfoGraph
    model_plain: InfoGraph
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
    - 0.6813
    - null
    metric_stds:
    - 0.0059
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
    - 0.6799
    - null
    metric_stds:
    - 0.0297
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
    - 0.6787
    - null
    metric_stds:
    - 0.004
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
    - 0.6786
    - null
    metric_stds:
    - 0.0141
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
    - 0.6772
    - null
    metric_stds:
    - 0.0228
    - null
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6702
    - null
    metric_stds:
    - 0.0225
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
    - 0.67
    - null
    metric_stds:
    - 0.006
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
    - 0.6692
    - null
    metric_stds:
    - 0.0021
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
    - 0.6684
    - null
    metric_stds:
    - 0.0045
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
    - 0.6637
    - null
    metric_stds:
    - 0.0274
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
    - 0.6612
    - null
    metric_stds:
    - 0.016
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
    - 0.6612
    - null
    metric_stds:
    - 0.016
    - null
  - model: Graphlet
    model_plain: Graphlet
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
    - 0.66
    - null
    metric_stds:
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.6546
    - null
    metric_stds:
    - 0.0112
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
    - 0.6502
    - null
    metric_stds:
    - 0.0166
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
    - 0.646
    - null
    metric_stds:
    - 0.0
    - null
  - model: p-rand walk
    model_plain: p-rand walk
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
    - 0.6434
    - null
    metric_stds:
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
    - 0.641
    - null
    metric_stds:
    - 0.004
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
    - 0.6298
    - null
    metric_stds:
    - 0.001
    - null
  - model: PANPool
    model_plain: PANPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6282
    - null
    metric_stds:
    - 0.0304
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
    - 0.626
    - null
    metric_stds:
    - null
    - null
  - model: GK
    model_plain: GK
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
    - 0.625
    - null
    metric_stds:
    - 0.003
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
    - 0.624
    - null
    metric_stds:
    - 0.003
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
    - 0.6239
    - null
    metric_stds:
    - 0.0968
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
    - 0.6235
    - null
    metric_stds:
    - 0.0028
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
    - 0.6198
    - null
    metric_stds:
    - 0.0198
    - null
  - model: R&G
    model_plain: R&G
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
    - 0.6186
    - null
    metric_stds:
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
    - 0.6161
    - null
    metric_stds:
    - 0.0322
    - null
  - model: Set2Set
    model_plain: Set2Set
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
    - 0.6104
    - null
    metric_stds:
    - 0.0269
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
    - 0.6075
    - null
    metric_stds:
    - 0.0189
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
    - 0.5805
    - null
    metric_stds:
    - 0.0436
    - null
  - model: DGCNN
    model_plain: DGCNN
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
    - 0.5661
    - null
    metric_stds:
    - 0.0104
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
    - 0.5658
    - null
    metric_stds:
    - 0.0212
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
    - 0.5644
    - null
    metric_stds:
    - 0.0677
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.55
    - null
    metric_stds:
    - 0.055
    - null
  - model: Node2Vec
    model_plain: Node2Vec
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
    - 0.5492
    - null
    metric_stds:
    - 0.0162
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
    - 0.545
    - null
    metric_stds:
    - 0.006
    - null
  - model: sub2vec
    model_plain: sub2vec
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
    - 0.5282
    - null
    metric_stds:
    - 0.0153
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
    - 0.5258
    - null
    metric_stds:
    - 0.0198
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
    - 0.4991
    - null
    metric_stds:
    - 0.0366
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
    - 0.4962
    - null
    metric_stds:
    - 0.0653
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
    - 0.492
    - null
    metric_stds:
    - 0.034
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
    - 0.4873
    - null
    metric_stds:
    - 0.0883
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
    - 0.4757
    - null
    metric_stds:
    - 0.0484
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
    - 0.3864
    - null
    metric_stds:
    - 0.1043
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
    - null
    - 0.5039
    metric_stds:
    - null
    - 0.0
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
    - null
    - 0.5226
    metric_stds:
    - null
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
    - null
    - 0.5047
    metric_stds:
    - null
    - 0.0029
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
    - null
    - 0.5438
    metric_stds:
    - null
    - 0.0185
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
    - null
    - 0.5467
    metric_stds:
    - null
    - 0.0193
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
    - null
    - 0.5537
    metric_stds:
    - null
    - 0.0168
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
    - null
    - 0.5629
    metric_stds:
    - null
    - 0.0224
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
    - null
    - 0.562
    metric_stds:
    - null
    - 0.0058
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
    - null
    - 0.563
    metric_stds:
    - null
    - 0.0085
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
    - null
    - 0.5636
    metric_stds:
    - null
    - 0.0231
  milestones:
  - value: 0.859
    std: 0.001
    model: WL
    arxiv_id: '1410.3314'
    title: Propagation Kernels
    date: 2014-10
  - value: 0.86
    std: 0.018
    model: WLK
    arxiv_id: '2209.08179'
    title: Cell Attention Networks
    date: 2022-09
  - value: 0.874
    std: 0.003
    model: ILLS
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: '2023-05-27'
  - value: 0.962
    std: null
    model: MSA-AU
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: 2023-12
---

