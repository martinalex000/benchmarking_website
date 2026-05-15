---
title: PCQM-Contact
slug: pcqm-contact
benchmark: LRGB
task_type: link_prediction
description: Link prediction of spatial atom contacts in quantum chemistry molecules.
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats:
  num_graphs: 529434
  avg_nodes: 30.14
  avg_edges: 61.09
  num_classes: 1
result_count: 90
best_model:
  model: FloydNet
  value: 0.6143
  metric: MRR
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official split. Metric: MRR (Mean Reciprocal Rank). Also reported: Hits@1,
    Hits@3, Hits@10.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  metrics:
  - MRR
  - MAE
  rows:
  - model: FloydNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6143
    - null
    metric_stds:
    - null
    - null
  - model: ViT-PS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5341
    - null
    metric_stds:
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4707
    - null
    metric_stds:
    - 0.0007
    - null
  - model: GPS
    is_baseline: true
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
    - 0.4703
    - null
    metric_stds:
    - 0.0014
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.467
    - null
    metric_stds:
    - 0.0004
    - null
  - model: GIN
    is_baseline: true
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
    - 0.4617
    - null
    metric_stds:
    - 0.0005
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4526
    - null
    metric_stds:
    - 0.0006
    - null
  - model: CoCN exp.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3713
    - null
    metric_stds:
    - 0.0037
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3637
    - null
    metric_stds:
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
    - 0.3587
    - null
    metric_stds:
    - 0.0025
    - null
  - model: GPS & OGE-Aug
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3543
    - null
    metric_stds:
    - 0.0004
    - null
  - model: + ReHub
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: ': Linear Complexity Graph Transformers Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3534
    - null
    metric_stds:
    - 0.0014
    - null
  - model: + ReHub-FC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: ': Linear Complexity Graph Transformers Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3526
    - null
    metric_stds:
    - 0.0014
    - null
  - model: GECO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3526
    - null
    metric_stds:
    - 0.0016
    - null
  - model: GENs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    - null
    metric_stds:
    - 0.001
    - null
  - model: GENs+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.352
    - null
    metric_stds:
    - 0.001
    - null
  - model: IPR-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3516
    - null
    metric_stds:
    - 0.0102
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? - Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3509
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? - Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3498
    - null
    metric_stds:
    - 0.0005
    - null
  - model: GEN w/o EA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3496
    - null
    metric_stds:
    - 0.0016
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? - Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3495
    - null
    metric_stds:
    - 0.001
    - null
  - model: Cache-GNN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3488
    - null
    metric_stds:
    - 0.0008
    - null
  - model: GEN w/o HA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.348
    - null
    metric_stds:
    - 0.0007
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
    - 0.3459
    - null
    metric_stds:
    - 0.0005
    - null
  - model: M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.345
    - null
    metric_stds:
    - 0.0002
    - null
  - model: DRew
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3444
    - null
    metric_stds:
    - 0.0017
    - null
  - model: Drew-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3444
    - null
    metric_stds:
    - 0.0017
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
    - 0.3442
    - null
    metric_stds:
    - 0.0009
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
    - 0.3442
    - null
    metric_stds:
    - 0.0009
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3441
    - null
    metric_stds:
    - 0.0008
    - null
  - model: GENs+RWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.344
    - null
    metric_stds:
    - 0.0008
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
    - 0.3437
    - null
    metric_stds:
    - 0.0005
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3437
    - null
    metric_stds:
    - null
    - null
  - model: GQT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3427
    - null
    metric_stds:
    - 0.0012
    - null
  - model: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3425
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? - Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3424
    - null
    metric_stds:
    - 0.0007
    - null
  - model: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3414
    - null
    metric_stds:
    - 0.0006
    - null
  - model: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3408
    - null
    metric_stds:
    - 0.002
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
    - 0.3408
    - null
    metric_stds:
    - 0.0003
    - null
  - model: GPS+Hodge1Lap
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
    - 0.3407
    - null
    metric_stds:
    - 0.0004
    - null
  - model: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3404
    - null
    metric_stds:
    - 0.0005
    - null
  - model: Graph Mamba-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3395
    - null
    metric_stds:
    - 0.0013
    - null
  - model: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3395
    - null
    metric_stds:
    - 0.0013
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
    - 0.3391
    - null
    metric_stds:
    - 0.0002
    - null
  - model: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.339
    - null
    metric_stds:
    - 0.0027
    - null
  - model: Graph Diffuser
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
    - 0.3388
    - null
    metric_stds:
    - 0.0011
    - null
  - model: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3373
    - null
    metric_stds:
    - 0.0045
    - null
  - model: MAGNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3364
    - null
    metric_stds:
    - 0.0008
    - null
  - model: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    metric_stds:
    - 0.0003
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    metric_stds:
    - 0.0003
    - null
  - model: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    metric_stds:
    - 0.0003
    - null
  - model: GatedGCN+EdgeRWSE
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
    - 0.3342
    - null
    metric_stds:
    - 0.0008
    - null
  - model: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3341
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GPS w/ Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3337
    - null
    metric_stds:
    - 0.0006
    - null
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
    - 0.3337
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3337
    - null
    metric_stds:
    - null
    - null
  - model: GatedGCN+Hodge1Lap
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
    - 0.3336
    - null
    metric_stds:
    - 0.0004
    - null
  - model: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3319
    - null
    metric_stds:
    - 0.002
    - null
  - model: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3287
    - null
    metric_stds:
    - 0.002
    - null
  - model: LASER
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3275
    - null
    metric_stds:
    - 0.0011
    - null
  - model: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3272
    - null
    metric_stds:
    - 0.0008
    - null
  - model: + NeuralAtoms
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: ': Linear Complexity Graph Transformers Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3262
    - null
    metric_stds:
    - 0.001
    - null
  - model: GatedGCN + Neural Atoms
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.01276'
    title: 'Neural Atoms: Propagating Long-range - Interaction in Molecular Graphs
      through - Efficient Communication Channel'
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3262
    - null
    metric_stds:
    - 0.001
    - null
  - model: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3256
    - null
    metric_stds:
    - 0.0011
    - null
  - model: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3249
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3242
    - null
    metric_stds:
    - null
    - null
  - model: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3234
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3234
    - null
    metric_stds:
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3218
    - null
    metric_stds:
    - null
    - null
  - model: GIN
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
    - 0.318
    - null
    metric_stds:
    - 0.0027
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.318
    - null
    metric_stds:
    - null
    - null
  - model: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3174
    - null
    metric_stds:
    - 0.002
    - null
  - model: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3174
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3161
    - null
    metric_stds:
    - 0.0004
    - null
  - model: GCN2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: ': Linear Complexity Graph Transformers Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3161
    - null
    metric_stds:
    - 0.0004
    - null
  - model: GCN + Neural Atoms
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.01276'
    title: 'Neural Atoms: Propagating Long-range - Interaction in Molecular Graphs
      through - Efficient Communication Channel'
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3049
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3007
    - null
    metric_stds:
    - 0.0022
    - null
  - model: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2989
    - null
    metric_stds:
    - 0.0026
    - null
  - model: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2937
    - null
    metric_stds:
    - 0.0007
    - null
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2783
    - null
    metric_stds:
    - 0.0008
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2311.01276'
    title: 'Neural Atoms: Propagating Long-range - Interaction in Molecular Graphs
      through - Efficient Communication Channel'
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2329
    - null
    metric_stds:
    - 0.0009
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1949
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1944
    - null
    metric_stds:
    - 0.002
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1927
    - null
    metric_stds:
    - 0.001
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
    - 93.6
    metric_stds:
    - null
    - 0.5
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
    - 92.7
    metric_stds:
    - null
    - 0.9
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
    - 94.1
    metric_stds:
    - null
    - 0.6
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
    - 92.9
    metric_stds:
    - null
    - 0.6
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
    - 90.4
    metric_stds:
    - null
    - 0.3
  - model: SOTA (Range)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.0809
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.335
    std: 0.0003
    model: SAN+LapPE
    arxiv_id: '2206.08164'
    title: LRGB
    date: 2022-06
  - value: 0.5341
    std: null
    model: ViT-PS
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: 2023-06
  - value: 0.6143
    std: null
    model: FloydNet
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: 2026-01
---

