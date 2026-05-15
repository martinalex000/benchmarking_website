---
title: MNIST
slug: mnist
benchmark: GNNBenchmark
task_type: graph_classification
description: Graph classification on MNIST superpixel graphs (10 digit classes, 70k
  graphs).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.GNNBenchmarkDataset.html
stats:
  num_graphs: 70000
  avg_nodes: 70.6
  avg_edges: 564.5
  num_classes: 10
result_count: 115
best_model:
  model: GRASS
  value: 0.98932
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: Fixed 55k/5k/10k split.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - AUROC
  - ECE
  - F1
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
    - 0.98932
    - null
    - null
    - null
    metric_stds:
    - 0.00076
    - null
    - null
    - null
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
    is_best: true
    metric_values:
    - 0.9884
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.98712
    - null
    - null
    - null
    metric_stds:
    - 0.00137
    - null
    - null
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.98692
    - null
    - null
    - null
    metric_stds:
    - 0.00079
    - null
    - null
    - null
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
    - 0.98614
    - null
    - null
    - null
    metric_stds:
    - 0.00096
    - null
    - null
    - null
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
    - 0.98558
    - null
    - null
    - null
    metric_stds:
    - 0.00057
    - null
    - null
    - null
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
    - 0.9855
    - null
    - null
    - null
    metric_stds:
    - 0.00039
    - null
    - null
    - null
  - model: Full Model
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
    - 0.98528
    - null
    - null
    - null
    metric_stds:
    - 0.00057
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.98513
    - null
    - null
    - null
    metric_stds:
    - 0.00086
    - null
    - null
    - null
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
    - 0.98512
    - null
    - null
    - null
    metric_stds:
    - 0.00033
    - null
    - null
    - null
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
    - 0.98492
    - null
    - null
    - null
    metric_stds:
    - 0.00051
    - null
    - null
    - null
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
    - 0.9848
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
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
    - 0.98473
    - null
    - null
    - null
    metric_stds:
    - 0.00095
    - null
    - null
    - null
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
    - 0.98432
    - null
    - null
    - null
    metric_stds:
    - 0.00059
    - null
    - null
    - null
  - model: Exphormer
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
    - 0.9843
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
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
    - 0.98424
    - null
    - null
    - null
    metric_stds:
    - 0.00124
    - null
    - null
    - null
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
    - 0.98423
    - null
    - null
    - null
    metric_stds:
    - 0.00155
    - null
    - null
    - null
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
    - 0.9842
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
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
    - 0.9842
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
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
    - 0.9839
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.98382
    - null
    - null
    - null
    metric_stds:
    - 0.00095
    - null
    - null
    - null
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
    - 0.98367
    - null
    - null
    - null
    metric_stds:
    - 0.00106
    - null
    - null
    - null
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
    - 0.98362
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
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
    - 0.9835
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
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
    - 0.9834
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98294
    - null
    - null
    - null
    metric_stds:
    - 0.00147
    - null
    - null
    - null
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
    - 0.9829
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.98285
    - null
    - null
    - null
    metric_stds:
    - 0.00103
    - null
    - null
    - null
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
    - 0.98285
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98269
    - null
    - null
    - null
    metric_stds:
    - 0.00078
    - null
    - null
    - null
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
    - 0.9826
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
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
    - 0.98247
    - null
    - null
    - null
    metric_stds:
    - 0.00018
    - null
    - null
    - null
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
    - 0.98245
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
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
    - 0.98236
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98231
    - null
    - null
    - null
    metric_stds:
    - 0.00197
    - null
    - null
    - null
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
    - 0.9823
    - null
    - null
    - null
    metric_stds:
    - 0.00133
    - null
    - null
    - null
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
    - 0.9822
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
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
    - 0.9821
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
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
    - 0.98204
    - null
    - null
    - null
    metric_stds:
    - 0.00048
    - null
    - null
    - null
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
    - 0.982
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
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
    - 0.98173
    - null
    - null
    - null
    metric_stds:
    - 0.00087
    - null
    - null
    - null
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
    - 0.9817
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
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
    - 0.98164
    - null
    - null
    - null
    metric_stds:
    - 0.00054
    - null
    - null
    - null
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
    - 0.9815
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
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
    - 0.9814
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
  - model: GPS (MoSE)
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
    - 0.98135
    - null
    - null
    - null
    metric_stds:
    - 2.0e-05
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98127
    - null
    - null
    - null
    metric_stds:
    - 0.00123
    - null
    - null
    - null
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
    - 0.9811799999999999
    - null
    - null
    - null
    metric_stds:
    - 0.0005600000000000001
    - null
    - null
    - null
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
    - 0.98114
    - null
    - null
    - null
    metric_stds:
    - 0.00183
    - null
    - null
    - null
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
    - 0.98114
    - null
    - null
    - null
    metric_stds:
    - 0.00183
    - null
    - null
    - null
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
    - 0.9811
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
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
    - 0.9811
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
  - model: GRIT 1-CQRW
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
    - 0.98108
    - null
    - null
    - null
    metric_stds:
    - 0.00111
    - null
    - null
    - null
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
    - 0.98108
    - null
    - null
    - null
    metric_stds:
    - 0.00111
    - null
    - null
    - null
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
    - 0.9808100000000001
    - null
    - null
    - null
    metric_stds:
    - 0.00241
    - null
    - null
    - null
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
    - 0.9808
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
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
    - 0.9808
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
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
    - 0.98069
    - null
    - null
    - null
    metric_stds:
    - 0.00115
    - null
    - null
    - null
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
    - 0.98051
    - null
    - null
    - null
    metric_stds:
    - 0.00126
    - null
    - null
    - null
  - model: GPS (base model)
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
    - 0.98051
    - null
    - null
    - null
    metric_stds:
    - 0.00126
    - null
    - null
    - null
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
    - 0.98051
    - null
    - null
    - null
    metric_stds:
    - 0.00126
    - null
    - null
    - null
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
    - 0.9805
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
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
    - 0.9805
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
  - model: GPS-DENS + LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.98
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
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
    - 0.97997
    - null
    - null
    - null
    metric_stds:
    - 0.00126
    - null
    - null
    - null
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
    - 0.97989
    - null
    - null
    - null
    metric_stds:
    - 0.00118
    - null
    - null
    - null
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
    - 0.97985
    - null
    - null
    - null
    metric_stds:
    - 0.00032
    - null
    - null
    - null
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
    - 0.97944
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
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
    - 0.97944
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
  - model: PNA
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
    - 0.9794
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
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
    - 0.97912
    - null
    - null
    - null
    metric_stds:
    - 0.00062
    - null
    - null
    - null
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
    - 0.9783
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GPS + LPE + G-$\Delta$UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.978
    - null
    - 0.022
    - null
    metric_stds:
    - 0.001
    - null
    - 0.001
    - null
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
    - 0.97772
    - null
    - null
    - null
    metric_stds:
    - 1.0e-05
    - null
    - null
    - null
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
    - 0.97564
    - null
    - null
    - null
    metric_stds:
    - 0.00146
    - null
    - null
    - null
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
    - 0.97553
    - null
    - null
    - null
    metric_stds:
    - 0.00034
    - null
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97422
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
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
    - 0.97422
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
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
    - 0.9734
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
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
    - 0.97312
    - null
    - null
    - null
    metric_stds:
    - 0.00097
    - null
    - null
    - null
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
    - 0.97163
    - null
    - null
    - null
    metric_stds:
    - 0.00154
    - null
    - null
    - null
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
    - 0.97142
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97
    - null
    - 0.026
    - null
    metric_stds:
    - 0.001
    - null
    - 0.001
    - null
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
    - 0.96977
    - null
    - null
    - null
    metric_stds:
    - 0.00021
    - null
    - null
    - null
  - model: GPS (Pretrained) + LPE + G-$\Delta$UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.967
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
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
    - 0.96544
    - null
    - null
    - null
    metric_stds:
    - 0.00615
    - null
    - null
    - null
  - model: GatedGCN-DENS + LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.965
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
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
    - 0.9649
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
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
    - 0.9637
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
  - model: GatedGCN-DENS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.963
    - null
    - null
    - null
    metric_stds:
    - 0.0002
    - null
    - null
    - null
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
    - 0.95535
    - null
    - null
    - null
    metric_stds:
    - 0.00205
    - null
    - null
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
    - 0.95461
    - null
    - null
    - null
    metric_stds:
    - 0.00613
    - null
    - null
    - null
  - model: GatedGCN-DENS + LPE + G-$\Delta$UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
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
    - 0.95075
    - null
    - null
    - null
    metric_stds:
    - 0.00961
    - null
    - null
    - null
  - model: GatedGCN + G-$\Delta$UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - 0.022
    - null
    metric_stds:
    - 0.008
    - null
    - 0.007
    - null
  - model: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - 0.036
    - null
    metric_stds:
    - 0.002
    - null
    - 0.003
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.947
    - null
    - 0.038
    - null
    metric_stds:
    - 0.002
    - null
    - 0.001
    - null
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
    - 0.90831
    - null
    - null
    - null
    metric_stds:
    - 0.00161
    - null
    - null
    - null
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
    - 0.90805
    - null
    - null
    - null
    metric_stds:
    - 0.00032
    - null
    - null
    - null
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
    - 0.90705
    - null
    - null
    - null
    metric_stds:
    - 0.00218
    - null
    - null
    - null
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
    - 0.90667
    - null
    - null
    - null
    metric_stds:
    - 0.00143
    - null
    - null
    - null
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
    - 0.90305
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
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
    - 0.8331
    - null
    - null
    - null
    metric_stds:
    - 0.0446
    - null
    - null
    - null
  - model: GT (no PE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9329000000000001
    metric_stds:
    - null
    - null
    - null
    - 0.0088
  - model: GDT (LPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9107999999999999
    metric_stds:
    - null
    - null
    - null
    - 0.0095
  - model: GDT (SPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9251999999999999
    metric_stds:
    - null
    - null
    - null
    - 0.0012
  - model: GDT (RWSE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9326000000000001
    metric_stds:
    - null
    - null
    - null
    - 0.0045000000000000005
  - model: GDT (RRWP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9604
    metric_stds:
    - null
    - null
    - null
    - 0.0091
  - model: VANILLA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.759
    - null
    - null
    metric_stds:
    - null
    - 0.006
    - null
    - null
  - model: G-$\Delta$UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.771
    - null
    - null
    metric_stds:
    - null
    - 0.002
    - null
    - null
  - model: Pretr. G-\Delta UQ
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.774
    - null
    - null
    metric_stds:
    - null
    - 0.016
    - null
    - null
  - model: GatedGCN Ensembling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.024
    - null
    metric_stds:
    - null
    - null
    - 0.001
    - null
  - model: GatedGCN + G-$\Delta$UQ Ensembling
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.017
    - null
    metric_stds:
    - null
    - null
    - 0.002
    - null
  - model: GPS + LPE Ensembling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.016
    - null
    metric_stds:
    - null
    - null
    - 0.001
    - null
  - model: GPS + LPE + G-$\Delta$UQ Ensembling
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.03350'
    title: Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural
      Networks
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.014
    - null
    metric_stds:
    - null
    - null
    - 0.0
    - null
  milestones:
  - value: 0.9835
    std: 0.001
    model: Graph MLP-Mixer
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.9855
    std: 0.00039
    model: Exphormer
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.98692
    std: 0.00079
    model: NeuralWalker
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: 2024-06
  - value: 0.98932
    std: 0.00076
    model: GRASS
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: 2024-07
---

