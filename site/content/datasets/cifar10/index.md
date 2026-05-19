---
title: CIFAR10
slug: cifar10
benchmark: GNNBenchmark
task_type: graph_classification
description: Graph classification on CIFAR10 superpixel graphs (10 classes, 60k graphs).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: 60000
  avg_nodes: 117.6
  avg_edges: 941.2
  num_classes: 10
result_count: 119
best_model:
  model: GRASS
  value: 0.8375
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: Fixed 45k/5k/10k split.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: GRASS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8375
    metric_stds:
    - 0.00141
  - model: NeuralWalker
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.80027
    metric_stds:
    - 0.00185
  - model: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79067
    metric_stds:
    - 0.00269
  - model: PPGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7856
    metric_stds:
    - 0.007
  - model: MPNN + differential encoding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7782
    metric_stds:
    - 0.00091
  - model: GSM++ (MoT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7781
    metric_stds:
    - 0.0028
  - model: GSSC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.05815'
    title: What Can We Learn from State Space Models for Machine Learning on Graphs?
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77642
    metric_stds:
    - 0.00456
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77218
    metric_stds:
    - 0.00381
  - model: GRIT-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.77022
    metric_stds:
    - 0.0043
  - model: GSM++ (DFS)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7692
    metric_stds:
    - 0.0031
  - model: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76903
    metric_stds:
    - 0.00457
  - model: MPNN only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76823
    metric_stds:
    - 0.00219
  - model: GEAET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76634
    metric_stds:
    - 0.00427
  - model: GSM++ (BFS)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7659
    metric_stds:
    - 0.0024
  - model: GT + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76473
    metric_stds:
    - 0.00429
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76468
    metric_stds:
    - 0.00881
  - model: GRIT 2-QiQRW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76442
    metric_stds:
    - 0.0107
  - model: GatedGCN + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76395
    metric_stds:
    - 0.00186
  - model: GRIT 1-CQRW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76347
    metric_stds:
    - 0.00704
  - model: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.76246
    metric_stds:
    - 0.00954
  - model: GRIT (our run)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76198
    metric_stds:
    - 0.00744
  - model: GraphGPS + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7618
    metric_stds:
    - 0.00277
  - model: EdgeGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76127
    metric_stds:
    - 0.00402
  - model: GRIT-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75905
    metric_stds:
    - 0.00842
  - model: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.05815'
    title: What Can We Learn from State Space Models for Machine Learning on Graphs?
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7576
    metric_stds:
    - 0.0042
  - model: GMN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7576
    metric_stds:
    - 0.0042
  - model: GRIT-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7572
    metric_stds:
    - 0.00734
  - model: GraphGPS with k-MIP attention (k=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7565000000000001
    metric_stds:
    - 0.0044
  - model: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7537
    metric_stds:
    - 0.621
  - model: RandAlign + scaling (GatedGCN-8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75015
    metric_stds:
    - 0.00177
  - model: GPS_big+MoSE_S
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.0059
  - model: GPS_big+MoSE_Omega
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7473
    metric_stds:
    - 0.0064
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74696
    metric_stds:
    - 0.00125
  - model: GMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7444
    metric_stds:
    - 0.0009
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73961
    metric_stds:
    - 0.0033
  - model: Graph MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73961
    metric_stds:
    - 0.0033
  - model: TIGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73955
    metric_stds:
    - 0.0036
  - model: ARGNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    metric_stds:
    - 0.0015
  - model: CSA-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73897
    metric_stds:
    - 0.00524
  - model: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73885
    metric_stds:
    - 0.00348
  - model: Graph Mamba-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - 0.0034
  - model: Graph-Mamba
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - 0.0034
  - model: MOSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.0044
  - model: GPS_small+MoSE_Omega
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.0044
  - model: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7341
    metric_stds:
    - 0.0015
  - model: GPS_small+MoSE_S
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7334
    metric_stds:
    - 0.005
  - model: GPS + HOPE-WavePE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via - High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7301
    metric_stds:
    - 0.0081
  - model: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72838
    metric_stds:
    - 0.00417
  - model: CKGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72785
    metric_stds:
    - 0.00436
  - model: GPS-GCCM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72502
    metric_stds:
    - 0.0028699999999999997
  - model: Graph MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7246
    metric_stds:
    - 0.0036
  - model: GPS + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7244
    metric_stds:
    - 0.0048
  - model: GPS+EdgeRWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72417
    metric_stds:
    - 0.00221
  - model: SignNet DeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7237
    metric_stds:
    - 0.0034
  - model: LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7231
    metric_stds:
    - 0.0034
  - model: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7231
    metric_stds:
    - 0.0034
  - model: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7231
    metric_stds:
    - 0.0025
  - model: GPS + (RWSE/LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    metric_stds:
    - 0.0036
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72298
    metric_stds:
    - 0.00356
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72298
    metric_stds:
    - 0.00356
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7226
    metric_stds:
    - 0.0031
  - model: GPS w/ Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7226
    metric_stds:
    - 0.0031
  - model: GIN-AK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7219
    metric_stds:
    - 0.0013
  - model: PEG^LapEig
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    metric_stds:
    - 0.0046
  - model: GPS+AllPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7205
    metric_stds:
    - 0.0035
  - model: GPS+Consistency+Contrastive
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71976
    metric_stds:
    - 0.00321
  - model: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7196
    metric_stds:
    - 0.004
  - model: GatedGCN + SSFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71938
    metric_stds:
    - 0.0019
  - model: GPS+Diffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71931
    metric_stds:
    - 0.0034699999999999996
  - model: GPS-PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7182999999999999
    metric_stds:
    - 0.00218
  - model: GPS+Consistency
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7182999999999999
    metric_stds:
    - 0.00218
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via - High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7176
    metric_stds:
    - 0.0001
  - model: SignNet MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7174
    metric_stds:
    - 0.006
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7167
    metric_stds:
    - 0.0001
  - model: GatedGCN+PE-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7158
    metric_stds:
    - 0.0009
  - model: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural - Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7149
    metric_stds:
    - 0.0019
  - model: GPS + projection
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71455
    metric_stds:
    - 0.00513
  - model: GRIT-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71167
    metric_stds:
    - 0.01311
  - model: GPS + Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7067
    metric_stds:
    - 0.0033
  - model: S4G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7065
    metric_stds:
    - 0.0033
  - model: GatedGCN+PE-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    metric_stds:
    - 0.0022
  - model: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7048
    metric_stds:
    - 0.001
  - model: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7035
    metric_stds:
    - 0.0063
  - model: GatedGCN+PE+VN_G
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7028
    metric_stds:
    - 0.0038
  - model: GatedGCN+EdgeRWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7026
    metric_stds:
    - 0.00341
  - model: Eigenformer (feat.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.70194
    metric_stds:
    - null
  - model: GPS-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.70163
    metric_stds:
    - 0.00357
  - model: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69948
    metric_stds:
    - 0.00499
  - model: GatedGCN+GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69948
    metric_stds:
    - 0.00499
  - model: GAT + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6992
    metric_stds:
    - 0.00082
  - model: Graph-ViT + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6987
    metric_stds:
    - 0.0028
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69824
    metric_stds:
    - 0.00413
  - model: GatedGCN-8 w/o RandAlign
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69808
    metric_stds:
    - 0.00421
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6967
    metric_stds:
    - 0.004
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69592
    metric_stds:
    - 0.00287
  - model: GAT-8 + RandAlign (w/o scaling)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69158
    metric_stds:
    - 0.00438
  - model: CRaW1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69013
    metric_stds:
    - 0.00259
  - model: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69013
    metric_stds:
    - 0.00259
  - model: GCN+PE+VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68756
    metric_stds:
    - 0.00172
  - model: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68702
    metric_stds:
    - 0.00409
  - model: GCN + differential enc.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67373
    metric_stds:
    - 0.00415
  - model: Eigenformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67316
    metric_stds:
    - null
  - model: GatedGCN-16
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67312
    metric_stds:
    - 0.00311
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6731
    metric_stds:
    - 0.0031
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65767
    metric_stds:
    - 0.00308
  - model: Global attention + differential encoding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64468
    metric_stds:
    - 0.00537
  - model: GAT-8 w/o Lrn&Align
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64452
    metric_stds:
    - 0.00303
  - model: Cy2C-GNNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64285
    metric_stds:
    - 5.0e-05
  - model: GAT-16
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64223
    metric_stds:
    - 0.00455
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64223
    metric_stds:
    - 0.00455
  - model: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.59753
    metric_stds:
    - 0.00293
  - model: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.59175
    metric_stds:
    - 0.01593
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.56081
    metric_stds:
    - 0.00198
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5571
    metric_stds:
    - 0.00381
  - model: GCN + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.55275
    metric_stds:
    - 0.00165
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5526
    metric_stds:
    - 0.0153
  - model: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.54655
    metric_stds:
    - 0.00518
  - model: Global attention only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.45237
    metric_stds:
    - 0.01349
  - model: SPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.3722
    metric_stds:
    - 0.0827
  milestones:
  - value: 0.7246
    std: 0.0036
    model: Graph MLP-Mixer
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.76473
    std: 0.00429
    model: GT + HDSE
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.77642
    std: 0.00456
    model: GSSC
    arxiv_id: '2406.05815'
    title: What Can We Learn from State Space Models for Machine Learning on Graphs?
    date: 2024-06
  - value: 0.8375
    std: 0.00141
    model: GRASS
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: 2024-07
---

