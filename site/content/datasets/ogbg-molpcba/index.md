---
title: ogbg-molpcba
slug: ogbg-molpcba
benchmark: OGB
task_type: graph_classification
description: Multi-label classification (128 tasks) on PubChem BioAssay.
primary_metric: AP
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBDataset.html
stats:
  num_graphs: 437929
  avg_nodes: 26.0
  avg_edges: 28.1
  num_classes: 128
<<<<<<< Updated upstream
result_count: 104
=======
result_count: 79
>>>>>>> Stashed changes
best_model:
  model: novel dynamic message-passing mechanism
  value: 0.339
  metric: AP
  arxiv_id: '2410.23686'
  paper_title: Towards Dynamic Message Passing on Graphs
variants:
- slug: standard-split
  name: Standard split
  notes: 'Scaffold split. Metric: AP (Average Precision).'
  is_standard: true
  primary_metric: AP
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - AP
  - ACC
  - Accuracy
  - ROC-AUC
  rows:
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
    - 0.339
    - null
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
    - null
  - model: Graphormer-FLAG
    model_plain: Graphormer-FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3139
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 119.529
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3139
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
  - model: GSO
    model_plain: GSO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
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
    - 0.3031
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
  - model: GINE-APPNP
    model_plain: GINE-APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.1
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
<<<<<<< Updated upstream
    - 0.3066
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
  - model: LGI-GT
    model_plain: LGI-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.304
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
  - model: CRaWI
    model_plain: CRaWI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2986
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
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
    is_best: false
    metric_values:
    - 0.2986
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: SigGate-GT
    model_plain: SigGate-GT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2984
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2981
    - null
    - 0.8258
    - null
    metric_stds:
    - 0.0024
    - null
    - 0.0055
    - null
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2972
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: EGT (pre-trained)
    model_plain: EGT (pre-trained)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.2961
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
  - model: GECO
    model_plain: GECO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2961
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
  - model: GPS+LapPE
    model_plain: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2939
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
  - model: GPS+Hodge1Lap
    model_plain: GPS+Hodge1Lap
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2937
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GPS+EdgeRWSE
    model_plain: GPS+EdgeRWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2934
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GNNAK+
    model_plain: GNNAK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
  - model: GIN-AK+
    model_plain: GIN-AK+
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
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.292
=======
    - 0.2979
>>>>>>> Stashed changes
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.2
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
    - 0.2979
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: PHC-GNN
    model_plain: PHC-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.7
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2947
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.7
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2917
    - null
    - null
    - null
    metric_stds:
<<<<<<< Updated upstream
    - 0.0027
    - null
    - null
    - null
  - model: GINE
    model_plain: GINE
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
    - 0.2917
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: GPSE + GPS
    model_plain: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2911
    - null
    - null
    - null
    metric_stds:
    - 0.0036
=======
    - 0.0015
>>>>>>> Stashed changes
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 9.745
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2907
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
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
    - 0.2907
    - 0.8015
    - null
    - null
    metric_stds:
    - 0.0028
    - 0.0033
    - null
    - null
  - model: GIN-VN (fine-tune)
    model_plain: GIN-VN (fine-tune)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 3.4
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2902
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
  - model: GPS+RWSE
    model_plain: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2888
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 6.7
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2885
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: MPNN +pseudo node
    model_plain: MPNN +pseudo node
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
    - 0.2848
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
  - model: DeeperGCN-VN+FLAG
    model_plain: DeeperGCN-VN+FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 5.6
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2842
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 5.6
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
    - 0.2842
    - 0.7712
    - null
    - null
    metric_stds:
    - 0.0043
    - 0.0071
    - null
    - null
  - model: PNA-LSPE
    model_plain: PNA-LSPE
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
    - 0.284
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
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
=======
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2838
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
  - model: PNA + MAP
    model_plain: PNA + MAP
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
=======
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.281
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: GCN SEM-IL
    model_plain: GCN SEM-IL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2802
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
  - model: DeeperGCN-VN
    model_plain: DeeperGCN-VN
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
    - 0.2781
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
<<<<<<< Updated upstream
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    params_millions: 0.509
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2765
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
  - model: GraphTrans
    model_plain: GraphTrans
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
    - 0.2761
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
  - model: GIN-VN
    model_plain: GIN-VN
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
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GCN +pseudo node
    model_plain: GCN +pseudo node
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
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
<<<<<<< Updated upstream
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    params_millions: 0.51
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2703
    - 0.6892
    - null
    - null
    metric_stds:
    - 0.0023
    - 0.01
    - null
    - null
  - model: GatedGCN + MAP
    model_plain: GatedGCN + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.268
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2661
    - null
    - 0.6892
    - null
    metric_stds:
    - 0.0017
    - null
    - 0.01
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.266
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.262
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GIN + FA
    model_plain: GIN + FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.02997'
    title: Expander Graph Propagation
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2595
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
  - model: GCN SEM-only
    model_plain: GCN SEM-only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2566
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
    - null
<<<<<<< Updated upstream
  - model: d-DRFWL(2) GNN
    model_plain: d-DRFWL(2) GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2538
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.2483
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
  - model: GCN+PE+VN
    model_plain: GCN+PE+VN
=======
  - model: GIN + master node
    model_plain: GIN + master node
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.02997'
    title: Expander Graph Propagation
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2527
    - null
    - 0.6916
    - null
    metric_stds:
    - 0.0064
    - null
    - 0.0154
    - null
<<<<<<< Updated upstream
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
=======
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
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
    - 0.2424
    - 0.6839
    - null
    - null
    metric_stds:
    - 0.0034
    - 0.0084
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
>>>>>>> Stashed changes
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
    - 0.241
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: MolFormer
    model_plain: MolFormer
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.235
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: ML
    model_plain: ML
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.235
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: ExpC
    model_plain: ExpC
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
    - 0.2342
    - 0.7976
    - null
    - null
    metric_stds:
    - 0.0029
    - 0.0072
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.233
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GIN + EGP
    model_plain: GIN + EGP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.02997'
    title: Expander Graph Propagation
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2329
    - null
    - 0.7027
    - null
    metric_stds:
    - 0.0019
    - null
    - 0.0159
    - null
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.232
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.231
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: AttentiveFP
    model_plain: AttentiveFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.23
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GCN Baseline
    model_plain: GCN Baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2291
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2291
    - null
    - 0.6839
    - null
    metric_stds:
    - 0.0037
    - null
    - 0.0084
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.229
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.228
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: Jumping Knowledge
    model_plain: Jumping Knowledge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.228
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.227
    - null
    - null
    - null
    metric_stds:
    - 0.001
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
    - 0.225
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.225
    - null
    - null
    - null
    metric_stds:
    - 0.001
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
    - 0.221
    - null
    - null
    - null
    metric_stds:
    - 0.001
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
    - 0.218
    - null
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.215
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
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
    - 0.213
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.202
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1931
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
  - model: HopFormer
    model_plain: HopFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1849
    - null
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
    - null
  - model: Graph-MLPMixer
    model_plain: Graph-MLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1386
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1012
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0973
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0968
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0953
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0933
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0785
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
  - model: GCN+virtual node
    model_plain: GCN+virtual node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7037
    - null
    metric_stds:
    - null
    - null
    - 0.0107
    - null
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7712
    - null
    metric_stds:
    - null
    - null
    - 0.0071
    - null
  - model: ExpC
    model_plain: ExpC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7976
    - null
    metric_stds:
    - null
    - null
    - 0.0072
    - null
  - model: K-Subtree SAT
    model_plain: K-Subtree SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7522
    - null
    metric_stds:
    - null
    - null
    - 0.0056
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8015
    - null
    metric_stds:
    - null
    - null
    - 0.0033
    - null
  - model: GCN+virtual node
    model_plain: GCN+virtual node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7037
    - null
    metric_stds:
    - null
    - null
    - 0.0107
    - null
  - model: GCN
    model_plain: GCN
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
    - null
    - null
    - null
    - 0.202
    metric_stds:
    - null
    - null
    - null
    - 0.0024
  - model: GIN
    model_plain: GIN
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
    - null
    - null
    - null
    - 0.2266
    metric_stds:
    - null
    - null
    - null
    - 0.0028
  - model: GCN-virtual
    model_plain: GCN-virtual
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
    - null
    - null
    - null
    - 0.2703
    metric_stds:
    - null
    - null
    - null
    - 0.0023
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
    - null
    - null
    - null
    - 0.1281
    metric_stds:
    - null
    - null
    - null
    - 0.0039
  - model: GraphTrans (GIN)
    model_plain: GraphTrans (GIN)
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
    - null
    - null
    - null
    - 0.2756
    metric_stds:
    - null
    - null
    - null
    - 0.0039
  - model: GraphTrans (GIN-Virtual)
    model_plain: GraphTrans (GIN-Virtual)
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
    - null
    - null
    - null
    - 0.2761
    metric_stds:
    - null
    - null
    - null
    - 0.0029
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
    - null
    - 0.801
    - null
    - null
    metric_stds:
    - null
    - 0.0052
    - null
    - null
  - model: KS-SAT
    model_plain: KS-SAT
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
    - null
    - 0.7522
    - null
    - null
    metric_stds:
    - null
    - 0.0056
    - null
    - null
  milestones:
<<<<<<< Updated upstream
  - value: 0.2986
    std: 0.0025
    model: CRaWl
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: 2021-02
  - value: 0.3141
    std: 0.0019
    model: GatedGCN + VN
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: 2024-05
=======
  - value: 0.2661
    std: 0.0017
    model: GIN
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
  - value: 0.3139
    std: 0.0032
    model: Graphormer-FLAG
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: 2021-06
  - value: 0.339
    std: 0.0073
    model: novel dynamic message-passing mechanism
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: 2024-10
>>>>>>> Stashed changes
---

