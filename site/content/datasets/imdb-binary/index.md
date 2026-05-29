---
title: IMDB-BINARY
slug: imdb-binary
benchmark: TU Dortmund
task_type: graph_classification
description: Binary graph classification of movie collaboration networks (action vs.
  romance).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 1000
  avg_nodes: 19.8
  avg_edges: 96.5
  num_classes: 2
result_count: 293
best_model:
  model: SVMs
  value: 0.83
  metric: Accuracy
  arxiv_id: '2203.07691'
  paper_title: Supervised Contrastive Learning with Structure Inference for Graph
    Classification
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
  rows:
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
    - 0.83
    metric_stds:
    - 0.032
  - model: GPM
    model_plain: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.8267
    metric_stds:
    - 0.0047
  - model: RUM
    model_plain: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.811
    metric_stds:
    - 0.045
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
    is_best: true
    metric_values:
    - 0.7995
    metric_stds:
    - 0.0246
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
    - 0.7904
    metric_stds:
    - null
  - model: GXN
    model_plain: GXN
    is_baseline: true
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
    - 0.786
    metric_stds:
    - 0.023
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
    - 0.785
    metric_stds:
    - 0.006
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7829
    metric_stds:
    - 0.0126
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7805
    metric_stds:
    - 0.01
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
    - 0.7802
    metric_stds:
    - null
  - model: sGIN
    model_plain: sGIN
    is_baseline: true
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
    - 0.779
    metric_stds:
    - 0.043
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7776
    metric_stds:
    - 0.0098
  - model: QGNN
    model_plain: QGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7756
    metric_stds:
    - 0.0245
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
    - 0.7735
    metric_stds:
    - 0.0232
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
    - 0.7726
    metric_stds:
    - 0.0027
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
    - 0.772
    metric_stds:
    - 0.0473
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
    - 0.771
    metric_stds:
    - 0.007
  - model: ESAN*
    model_plain: ESAN*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.026
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
    is_best: true
    metric_values:
    - 0.7705
    metric_stds:
    - 0.0345
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
    - 0.7704
    metric_stds:
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
    is_best: true
    metric_values:
    - 0.769
    metric_stds:
    - 0.036
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
    - 0.768
    metric_stds:
    - 0.026
  - model: SGN
    model_plain: SGN
    is_baseline: true
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
    - 0.765
    metric_stds:
    - 0.057
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
    - 0.763
    metric_stds:
    - 0.003
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
    is_best: true
    metric_values:
    - 0.762
    metric_stds:
    - 0.0518
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
    - 0.008
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
    - 0.762
    metric_stds:
    - 0.004
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
    - 0.762
    metric_stds:
    - 0.004
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
    - 0.761
    metric_stds:
    - 0.005
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
    - 0.7606
    metric_stds:
    - 0.0059
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
    - 0.7602
    metric_stds:
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    metric_stds:
    - 0.019
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
    - 0.76
    metric_stds:
    - 0.027
  - model: SE2P-C3
    model_plain: SE2P-C3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    metric_stds:
    - 0.034
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
    - 0.759
    metric_stds:
    - 0.002
  - model: AgentNet
    model_plain: AgentNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7588
    metric_stds:
    - 0.036
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
    - 0.758
    metric_stds:
    - 0.009
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
    - 0.7577
    metric_stds:
    - 0.0172
  - model: SE2P-C4
    model_plain: SE2P-C4
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.757
    metric_stds:
    - 0.048
  - model: DropGNN
    model_plain: DropGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.757
    metric_stds:
    - 0.042
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
    - 0.756
    metric_stds:
    - 0.0269
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
    - 0.756
    metric_stds:
    - 0.003
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
    - 0.755
    metric_stds:
    - 0.017
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
    - 0.755
    metric_stds:
    - 0.0225
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
    - 0.754
    metric_stds:
    - 0.02
  - model: WEGL
    model_plain: WEGL
    is_baseline: true
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
    - 0.754
    metric_stds:
    - 0.05
  - model: GCBM-E
    model_plain: GCBM-E
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    metric_stds:
    - 0.043
  - model: DropGCN
    model_plain: DropGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.753
    metric_stds:
    - 0.033
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
    - 0.753
    metric_stds:
    - 0.002
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
    - 0.753
    metric_stds:
    - 0.027
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    metric_stds:
    - 0.031
  - model: SE2P-C2
    model_plain: SE2P-C2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    metric_stds:
    - 0.029
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
    - 0.751
    metric_stds:
    - 0.009
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
    is_best: true
    metric_values:
    - 0.751
    metric_stds:
    - 0.051
  - model: GIN-0
    model_plain: GIN-0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.751
    metric_stds:
    - 0.051
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
    - 0.7508
    metric_stds:
    - 0.0031
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
    - 0.7503
    metric_stds:
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
    - 0.7501
    metric_stds:
    - null
  - model: GNN-AK
    model_plain: GNN-AK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.042
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
    - 0.748
    metric_stds:
    - 0.004
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
    - 0.748
    metric_stds:
    - 0.025
  - model: GRDL
    model_plain: GRDL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    metric_stds:
    - 0.02
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
    - 0.747
    metric_stds:
    - 0.008
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
    - 0.747
    metric_stds:
    - 0.0267
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
    - 0.7467
    metric_stds:
    - 0.0032
  - model: SE2P-C1
    model_plain: SE2P-C1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.037
  - model: AMP-RNN
    model_plain: AMP-RNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.036
  - model: GAWL
    model_plain: GAWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.047
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
    - 0.7453
    metric_stds:
    - 0.0257
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
    - 0.745
    metric_stds:
    - 0.0331
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
    is_best: true
    metric_values:
    - 0.745
    metric_stds:
    - 0.059
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
    - 0.745
    metric_stds:
    - 0.046
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
    - 0.745
    metric_stds:
    - 0.0289
  - model: 1-GIN (GFL)
    model_plain: 1-GIN (GFL)
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
    - 0.745
    metric_stds:
    - 0.046
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
    is_best: true
    metric_values:
    - 0.7445
    metric_stds:
    - 0.0583
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
    - 0.7444
    metric_stds:
    - 0.0045
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
    - 0.743
    metric_stds:
    - 0.036
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
    - 0.743
    metric_stds:
    - 0.0329
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
    - 0.742
    metric_stds:
    - 0.0376
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
    - 0.742
    metric_stds:
    - 0.0541
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
    - 0.742
    metric_stds:
    - 0.0335
  - model: 123-gnn
    model_plain: 123-gnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - null
  - model: MVGRL
    model_plain: MVGRL
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
    - 0.742
    metric_stds:
    - 0.007
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
    - 0.742
    metric_stds:
    - 0.047
  - model: M-GCL
    model_plain: M-GCL
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.007
  - model: GCBM
    model_plain: GCBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.041
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
    - 0.7412
    metric_stds:
    - 0.0056
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
    is_best: false
    metric_values:
    - 0.741
    metric_stds:
    - 0.0104
  - model: Pre-train (Reconstruct)
    model_plain: Pre-train (Reconstruct)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.13728'
    title: Pre-Training Graph Neural Networks for Generic Structural Feature Extraction
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.741
    metric_stds:
    - 0.014
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
    - 0.7406
    metric_stds:
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
    - 0.7402
    metric_stds:
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
    - 0.7401
    metric_stds:
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
    - 0.74
    metric_stds:
    - 0.0574
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
    - 0.74
    metric_stds:
    - 0.007
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
    - 0.74
    metric_stds:
    - 0.0452
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
    - 0.739
    metric_stds:
    - 0.0247
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
    - 0.7388
    metric_stds:
    - 0.0053
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
    - 0.7384
    metric_stds:
    - 0.0036
  - model: GCN-3-TOGL-1 (static - interaction)
    model_plain: GCN-3-TOGL-1 (static - interaction)
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
    - 0.738
    metric_stds:
    - 0.048
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
    - 0.738
    metric_stds:
    - 0.028
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
    - 0.738
    metric_stds:
    - 0.039
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
    - 0.738
    metric_stds:
    - 0.045
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
    - 0.737
    metric_stds:
    - 0.057
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
    is_best: true
    metric_values:
    - 0.737
    metric_stds:
    - 0.07
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
    is_best: true
    metric_values:
    - 0.737
    metric_stds:
    - 0.07
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7369
    metric_stds:
    - 0.0205
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
    - 0.736
    metric_stds:
    - 0.0562
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
    - 0.736
    metric_stds:
    - 0.004
  - model: Pre-train (Rank)
    model_plain: Pre-train (Rank)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.13728'
    title: Pre-Training Graph Neural Networks for Generic Structural Feature Extraction
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.736
    metric_stds:
    - 0.014
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
    - 0.7348
    metric_stds:
    - 0.0076
  - model: GMT
    model_plain: GMT
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.7348
    metric_stds:
    - 0.008
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
    - 0.734
    metric_stds:
    - 0.0463
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
    - 0.734
    metric_stds:
    - 0.047
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
    - 0.733
    metric_stds:
    - 0.012
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
    - 0.733
    metric_stds:
    - 0.0529
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
    - 0.7329
    metric_stds:
    - 0.0146
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
    - 0.732
    metric_stds:
    - 0.041
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
    - 0.732
    metric_stds:
    - 0.0325
  - model: TopER
    model_plain: TopER
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
    - 0.732
    metric_stds:
    - 0.0343
  - model: Pre-train (All Tasks)
    model_plain: Pre-train (All Tasks)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.13728'
    title: Pre-Training Graph Neural Networks for Generic Structural Feature Extraction
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.732
    metric_stds:
    - 0.008
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
    - 0.731
    metric_stds:
    - 0.004
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
    - 0.731
    metric_stds:
    - 0.0483
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
    - 0.731
    metric_stds:
    - 0.0318
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
    - 0.731
    metric_stds:
    - 0.003
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
    - 0.7304
    metric_stds:
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
    - 0.73
    metric_stds:
    - 0.009
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
    - 0.73
    metric_stds:
    - 0.0435
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
    - 0.73
    metric_stds:
    - 0.0429
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
    - 0.73
    metric_stds:
    - 0.041
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.0577
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.009
  - model: SUGAR
    model_plain: SUGAR
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.035
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
    - 0.729
    metric_stds:
    - 0.046
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
    - 0.729
    metric_stds:
    - 0.0305
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
    - 0.729
    metric_stds:
    - 0.0375
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
    - 0.729
    metric_stds:
    - 0.027
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
    - 0.729
    metric_stds:
    - 0.046
  - model: GraphTrail
    model_plain: GraphTrail
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    metric_stds:
    - 0.049
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
    - 0.728
    metric_stds:
    - 0.006
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
    - 0.728
    metric_stds:
    - 0.007
  - model: EdgePool
    model_plain: EdgePool
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
    - 0.728
    metric_stds:
    - 0.044
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
    - 0.728
    metric_stds:
    - 0.025
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
    - 0.728
    metric_stds:
    - 0.0248
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
    - 0.7262
    metric_stds:
    - 0.0059
  - model: WITTOPOPOOL
    model_plain: WITTOPOPOOL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    metric_stds:
    - 0.018
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
    - 0.725
    metric_stds:
    - 0.004
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
    - 0.725
    metric_stds:
    - 0.0264
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
    - 0.725
    metric_stds:
    - 0.0291
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
    - 0.724
    metric_stds:
    - 0.0561
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
    - 0.724
    metric_stds:
    - 0.045
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    metric_stds:
    - 0.036
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
    - 0.723
    metric_stds:
    - 0.006
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
    - 0.723
    metric_stds:
    - 0.0293
  - model: RetGK
    model_plain: RetGK
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.723
    metric_stds:
    - 0.006
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
    - 0.722
    metric_stds:
    - 0.047
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
    - 0.722
    metric_stds:
    - 0.039
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
    - 0.722
    metric_stds:
    - 0.0299
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
    - 0.722
    metric_stds:
    - 0.039
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.722
    metric_stds:
    - 0.009
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
    - 0.721
    metric_stds:
    - 0.0365
  - model: Pre-train (Cluster)
    model_plain: Pre-train (Cluster)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.13728'
    title: Pre-Training Graph Neural Networks for Generic Structural Feature Extraction
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.721
    metric_stds:
    - 0.013
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
    - 0.7206
    metric_stds:
    - 0.0064
  - model: IGN
    model_plain: IGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.055
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
    - 0.72
    metric_stds:
    - 0.006
  - model: GCC
    model_plain: GCC
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
    - 0.72
    metric_stds:
    - null
  - model: FWL
    model_plain: FWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.046
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
    - 0.7196
    metric_stds:
    - 0.0069
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
    - 0.719
    metric_stds:
    - 0.052
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
    - 0.719
    metric_stds:
    - 0.0259
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
    - 0.719
    metric_stds:
    - 0.052
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
    - 0.7188
    metric_stds:
    - 0.0077
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
    - 0.7185
    metric_stds:
    - 0.0084
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
    - 0.718
    metric_stds:
    - 0.0399
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
    - 0.717
    metric_stds:
    - 0.01
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
    - 0.7169
    metric_stds:
    - 0.034
  - model: GCAPS
    model_plain: GCAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7169
    metric_stds:
    - 0.034
  - model: GCN-3-TOGL-1 (interaction)
    model_plain: GCN-3-TOGL-1 (interaction)
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
    - 0.716
    metric_stds:
    - 0.021
  - model: WWL
    model_plain: WWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    metric_stds:
    - 0.038
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
    - 0.7158
    metric_stds:
    - 0.012
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
    - 0.715
    metric_stds:
    - 0.049
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
    - 0.715
    metric_stds:
    - 0.044
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
    - 0.7149
    metric_stds:
    - 0.0093
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
    - 0.7148
    metric_stds:
    - 0.0088
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
    - 0.713
    metric_stds:
    - 0.0471
  - model: IEGN
    model_plain: IEGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7127
    metric_stds:
    - 0.045
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
    - 0.712
    metric_stds:
    - 0.008
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
    - 0.712
    metric_stds:
    - 0.047
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
    - 0.712
    metric_stds:
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
    - 0.712
    metric_stds:
    - 0.0366
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
    - 0.712
    metric_stds:
    - 0.039
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
    - 0.711
    metric_stds:
    - 0.0054
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.711
    metric_stds:
    - 0.004
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
    - 0.71
    metric_stds:
    - 0.022
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
    - 0.71
    metric_stds:
    - 0.0229
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
    - 0.71
    metric_stds:
    - 0.041
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
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
    - 0.71
    metric_stds:
    - 0.022
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    metric_stds:
    - 0.04
  - model: DiffPool
    model_plain: DiffPool
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
    - 0.709
    metric_stds:
    - 0.053
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
    - 0.709
    metric_stds:
    - 0.0501
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
    - 0.709
    metric_stds:
    - 0.0354
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
    - 0.7083
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
    - 0.708
    metric_stds:
    - 0.08
  - model: MinCutPool
    model_plain: MinCutPool
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
    - 0.7077
    metric_stds:
    - 0.0489
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
    - 0.707
    metric_stds:
    - 0.008
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
    - 0.707
    metric_stds:
    - 0.007
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    metric_stds:
    - 0.023
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
    - 0.704
    metric_stds:
    - 0.0537
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.704
    metric_stds:
    - 0.042
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
    - 0.703
    metric_stds:
    - 0.014
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    metric_stds:
    - 0.009
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
    - 0.7021
    metric_stds:
    - 0.0081
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
    - 0.7021
    metric_stds:
    - 0.0308
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
    - 0.7003
    metric_stds:
    - 0.0086
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.70025
    metric_stds:
    - 0.05147
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
    - 0.7
    metric_stds:
    - 0.0335
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.013
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
    - 0.698
    metric_stds:
    - 0.0296
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
    - 0.6971
    metric_stds:
    - 0.0103
  - model: PH
    model_plain: PH
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
    - 0.695
    metric_stds:
    - 0.005
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
    - 0.694
    metric_stds:
    - 0.011
  - model: RePHINE
    model_plain: RePHINE
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
    - 0.694
    metric_stds:
    - 0.0378
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
    - 0.693
    metric_stds:
    - 0.0361
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
    - 0.69
    metric_stds:
    - 0.0427
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
    - 0.6889
    metric_stds:
    - 0.0087
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
    - 0.687
    metric_stds:
    - 0.0355
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
    - 0.686
    metric_stds:
    - 0.049
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
    - 0.685
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
    - 0.681
    metric_stds:
    - 0.009
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
    - 0.6802
    metric_stds:
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
    - 0.6794
    metric_stds:
    - 0.0077
  - model: GNN+T
    model_plain: GNN+T
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    metric_stds:
    - 0.035
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
    - 0.674
    metric_stds:
    - 0.0476
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
    - 0.6696
    metric_stds:
    - 0.0056
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
    - 0.6683
    metric_stds:
    - null
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
    - 0.6679
    metric_stds:
    - 0.0359
  - model: GLCC
    model_plain: GLCC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.665
    metric_stds:
    - null
  - model: WEGL
    model_plain: WEGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.664
    metric_stds:
    - 0.021
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    metric_stds:
    - 0.045
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6605
    metric_stds:
    - 0.06631
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
    - 0.6587
    metric_stds:
    - 0.0098
  - model: GCFExplainer
    model_plain: GCFExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    metric_stds:
    - 0.054
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
    - 0.6509
    metric_stds:
    - 0.0093
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
    - 0.65
    metric_stds:
    - 0.05
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.05
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.04
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
    - 0.649
    metric_stds:
    - 0.0554
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
    - 0.6439
    metric_stds:
    - 0.0091
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    metric_stds:
    - 0.06
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
    - 0.6393
    metric_stds:
    - 0.0095
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
    - 0.636
    metric_stds:
    - 0.042
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
    - 0.63
    metric_stds:
    - 0.08
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
    - 0.629
    metric_stds:
    - 0.0305
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.622
    metric_stds:
    - 0.04
  - model: OOD-GNN
    model_plain: OOD-GNN
    is_baseline: true
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
    - 0.5864
    metric_stds:
    - 0.033
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
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
    - 0.5844
    metric_stds:
    - 0.0849
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.583
    metric_stds:
    - 0.073
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.583
    metric_stds:
    - null
  - model: PGIB
    model_plain: PGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.57
    metric_stds:
    - 0.029
  - model: sp
    model_plain: sp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.567
    metric_stds:
    - null
  - model: Group DRO
    model_plain: Group DRO
    is_baseline: true
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
    - 0.5612
    metric_stds:
    - 0.0432
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.559
    metric_stds:
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
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
    - 0.5536
    metric_stds:
    - 0.0484
  - model: CAD
    model_plain: CAD
    is_baseline: true
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
    - 0.5531
    metric_stds:
    - 0.0525
  - model: RGCL
    model_plain: RGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.546
    metric_stds:
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
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
    - 0.5459
    metric_stds:
    - 0.0303
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.545
    metric_stds:
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.543
    metric_stds:
    - null
  - model: DropoutNode
    model_plain: DropoutNode
    is_baseline: true
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
    - 0.5423
    metric_stds:
    - 0.0492
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.54
    metric_stds:
    - 0.03
  - model: IB-IRM
    model_plain: IB-IRM
    is_baseline: true
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
    - 0.5391
    metric_stds:
    - 0.0432
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.538
    metric_stds:
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.53
    metric_stds:
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
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
    - 0.5278
    metric_stds:
    - 0.0692
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
    - 0.524
    metric_stds:
    - 0.072
  - model: ERM
    model_plain: ERM
    is_baseline: true
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
    - 0.5234
    metric_stds:
    - 0.0369
  - model: DropoutEdge
    model_plain: DropoutEdge
    is_baseline: true
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
    - 0.5232
    metric_stds:
    - 0.0313
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
    - 0.516
    metric_stds:
    - 0.01
  - model: SizeShiftReg
    model_plain: SizeShiftReg
    is_baseline: true
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
    - 0.5146
    metric_stds:
    - 0.0423
  - model: VGIB
    model_plain: VGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.508
    metric_stds:
    - 0.037
  - model: CuCo
    model_plain: CuCo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.507
    metric_stds:
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
    - 0.503
    metric_stds:
    - 0.01
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
    - 0.501
    metric_stds:
    - 0.009
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
    - 0.4977
    metric_stds:
    - 0.0082
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
    - 0.497
    metric_stds:
    - 0.01
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
    - 0.4966
    metric_stds:
    - 0.0086
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
    - 0.494
    metric_stds:
    - 0.009
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
    - 0.4898
    metric_stds:
    - 0.0095
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
    - 0.4817
    metric_stds:
    - 0.008
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
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
    - 0.4794
    metric_stds:
    - 0.0621
  - model: Top-K Pooling
    model_plain: Top-K Pooling
    is_baseline: true
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
    - 0.4784
    metric_stds:
    - 0.0996
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
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
    - 0.4642
    metric_stds:
    - 0.0453
  - model: Virtual Node
    model_plain: Virtual Node
    is_baseline: true
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
    - 0.4521
    metric_stds:
    - 0.0549
  - model: SAGPooling
    model_plain: SAGPooling
    is_baseline: true
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
    - 0.4425
    metric_stds:
    - 0.067
  milestones:
  - value: 0.769
    std: 0.036
    model: GNTK
    arxiv_id: '1905.04579'
    title: Are Powerful Graph Neural Nets Necessary? A Dissection on Graph Classification
    date: 2019-05
  - value: 0.7756
    std: 0.0245
    model: QGNN
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: 2020-08
  - value: 0.7904
    std: null
    model: HAP
    arxiv_id: '2104.05960'
    title: Hierarchical Adaptive Pooling by Capturing High-order Dependency for Graph
      Representation Learning
    date: 2021-04
  - value: 0.83
    std: 0.032
    model: SVMs
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: 2022-03
  - value: 0.834
    std: 0.049
    model: GCN
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: 2022-05
---

