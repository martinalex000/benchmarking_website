---
title: REDDIT-BINARY
slug: reddit-binary
benchmark: TU Dortmund
task_type: graph_classification
description: Binary graph classification of Reddit discussion threads (question-answering
  vs. online discussion).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 2000
  avg_nodes: 429.63
  avg_edges: 497.75
  num_classes: 2
<<<<<<< Updated upstream
result_count: 42
=======
result_count: 27
>>>>>>> Stashed changes
best_model:
  model: PEs
  value: 0.945
  metric: Accuracy
  arxiv_id: '2502.01122'
  paper_title: Learning Efficient Positional Encodings with Graph Neural Networks
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
  - model: PEs
    model_plain: PEs
    is_baseline: false
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
    is_best: true
    metric_values:
    - 0.945
    metric_stds:
    - 0.004
<<<<<<< Updated upstream
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9275
    metric_stds:
    - 0.0216
=======
>>>>>>> Stashed changes
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.924
    metric_stds:
    - 0.025
  - model: WEGL
    model_plain: WEGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.92
    metric_stds:
    - 0.008
  - model: Graph-JEPA
    model_plain: Graph-JEPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9199
    metric_stds:
    - 0.0159
=======
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.918
    metric_stds:
    - 0.01
>>>>>>> Stashed changes
  - model: GIN + rand id
    model_plain: GIN + rand id
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
    - 0.918
    metric_stds:
    - 0.016
  - model: GSN with cliques
    model_plain: GSN with cliques
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
    - 0.911
    metric_stds:
    - 0.018
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
    - 0.9094
    metric_stds:
    - 0.0047
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
    - 0.9041
    metric_stds:
    - 0.0041
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
    - 0.9
    metric_stds:
    - 0.0065
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
    - 0.894
    metric_stds:
    - 0.002
  - model: SignNet-8S
    model_plain: SignNet-8S
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
    is_best: true
    metric_values:
    - 0.89
    metric_stds:
    - 0.052
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
    - 0.889
    metric_stds:
    - 0.002
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
    - 0.885
    metric_stds:
    - 0.003
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
    - 0.881
    metric_stds:
    - 0.004
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
    - 0.8797
    metric_stds:
    - 0.0056
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
    - 0.878
    metric_stds:
    - 0.003
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
    - 0.872
    metric_stds:
    - 0.004
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
    - 0.8683
    metric_stds:
<<<<<<< Updated upstream
    - 0.02
  - model: DMON
    model_plain: DMON
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
    - 0.85
    metric_stds:
    - 0.02
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
    - 0.85
    metric_stds:
    - 0.03
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    metric_stds:
    - 0.006
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8263
    metric_stds:
    - 0.0099
  - model: Kern. WL
    model_plain: Kern. WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    metric_stds:
    - 0.031
  - model: + PANDA
    model_plain: + PANDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8069
    metric_stds:
    - 0.00721
  - model: GCN + PANDA
    model_plain: GCN + PANDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8069
    metric_stds:
    - 0.00721
  - model: PANDA-GCN (Degree)
    model_plain: PANDA-GCN (Degree)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8069
    metric_stds:
    - 0.00721
  - model: PANDA-GCN (PageRank)
    model_plain: PANDA-GCN (PageRank)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8034
    metric_stds:
    - 0.00826
  - model: PANDA-GCN (Betweenness)
    model_plain: PANDA-GCN (Betweenness)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.00659
  - model: PANDA-GCN (Closeness)
    model_plain: PANDA-GCN (Closeness)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    metric_stds:
    - 0.00664
  - model: PANDA-GCN (Load)
    model_plain: PANDA-GCN (Load)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    metric_stds:
    - 0.00732
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7879
    metric_stds:
    - 0.0214
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7033
    metric_stds:
    - 0.00727
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6899
    metric_stds:
    - 0.0061
  - model: SDRF
    model_plain: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6862
    metric_stds:
    - 0.00851
  - model: Last Layer FA
    model_plain: Last Layer FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: Jun 6, 2024
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68485
    metric_stds:
    - 0.00945
=======
    - 0.0052
>>>>>>> Stashed changes
  - model: GCN
    model_plain: GCN
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
    - 0.865
    metric_stds:
    - 0.005
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
    - 0.8018
    metric_stds:
    - 0.006
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
    - 0.7604
    metric_stds:
    - 0.0078
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
    - 0.7443
    metric_stds:
    - 0.0072
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
    - 0.7033
    metric_stds:
    - 0.0072
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
    - 0.6862
    metric_stds:
    - 0.0085
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
    - 0.6849
    metric_stds:
    - 0.0095
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
    - 0.6826
    metric_stds:
    - 0.011
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
    - 0.5686
    metric_stds:
    - 0.0094
  - model: GCN
    model_plain: GCN
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
    - 0.5
    metric_stds:
    - 0.0
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
    - 0.4849
    metric_stds:
    - 0.0104
  milestones:
<<<<<<< Updated upstream
  - value: 0.9275
    std: 0.0216
    model: CRaWl
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: 2021-02
=======
  - value: 0.9094
    std: 0.0047
    model: R-GIN + FoSR
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: '2023-02-14'
>>>>>>> Stashed changes
  - value: 0.945
    std: 0.004
    model: PEs
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: 2025-02
---

