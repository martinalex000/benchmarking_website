---
title: NCI1
slug: nci1
benchmark: TU Dortmund
task_type: graph_classification
description: Graph classification of chemical compounds screened for anti-cancer activity.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats: null
result_count: 86
best_model:
  model: Kern. WL
  value: 0.86
  metric: Accuracy
variants:
- slug: 10-fold-cv
  name: 10-fold CV
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: Kern. WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.86
    metric_stds:
    - 0.018
  - model: CoCN expanded
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
    is_best: true
    metric_values:
    - 0.8583
    metric_stds:
    - 0.0086
  - model: PR-MPNN (10-fold CV)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.846
    metric_stds:
    - 0.012
  - model: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.845
    metric_stds:
    - 0.024
  - model: CAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.836
    metric_stds:
    - 0.012
  - model: nsqure~
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8352
    metric_stds:
    - 0.0375
  - model: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.835
    metric_stds:
    - 0.023
  - model: AdaptMPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.06984'
    title: On the Stability of Multiset and Graph Neural Networks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8326
    metric_stds:
    - 0.0086
  - model: GIN + HOPE-WavePE
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
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.831
    metric_stds:
    - 0.019
  - model: Natural GN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.83
    metric_stds:
    - 0.019
  - model: CoCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8289
    metric_stds:
    - 0.0019
  - model: CoCN vanilla
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
    - 0.8289
    metric_stds:
    - 0.0019
  - model: PG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    metric_stds:
    - 0.013
  - model: PG-GNN
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
    - 0.828
    metric_stds:
    - 0.013
  - model: SortMPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.06984'
    title: On the Stability of Multiset and Graph Neural Networks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8275
    metric_stds:
    - 0.016
  - model: SIN
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
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.827
    metric_stds:
    - 0.021
  - model: PK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    metric_stds:
    - 0.005
  - model: PathNN
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
    is_best: true
    metric_values:
    - 0.823
    metric_stds:
    - 0.019
  - model: PathNN-SP (K=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.823
    metric_stds:
    - 0.019
  - model: PathNN-AP (K=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.823
    metric_stds:
    - 0.017
  - model: PPGNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    metric_stds:
    - 0.014
  - model: PR-MPNN (train/val/test)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    metric_stds:
    - 0.015
  - model: DropGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    metric_stds:
    - 0.026
  - model: CO-GNN($\Sigma$, $\Sigma$)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    metric_stds:
    - 0.011
  - model: BS-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8034
    metric_stds:
    - 0.0146
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2406.06984'
    title: On the Stability of Multiset and Graph Neural Networks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    metric_stds:
    - 0.02
  - model: BNPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.02
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.014
  - model: SPN (K=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.015
  - model: CO-GNN($\mu$, $\mu$)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    metric_stds:
    - 0.007
  - model: SEP
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
    - 0.7935
    metric_stds:
    - 0.0033
  - model: RBF-KAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7918999999999999
    metric_stds:
    - 0.0181
  - model: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7864
    metric_stds:
    - 0.0153
  - model: PATCHY-SAN
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
    - 0.786
    metric_stds:
    - 0.019
  - model: SPN(k=5)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    metric_stds:
    - 0.038
  - model: JBGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    metric_stds:
    - 0.03
  - model: HOSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    metric_stds:
    - 0.03
  - model: PathNN-P (K=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    metric_stds:
    - 0.016
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    metric_stds:
    - 0.025
  - model: SCCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7712
    metric_stds:
    - 0.0107
  - model: +pseudo node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7708
    metric_stds:
    - 0.0149
  - model: Graclus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    metric_stds:
    - 0.02
  - model: ECPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    metric_stds:
    - 0.03
  - model: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    metric_stds:
    - 0.019
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    metric_stds:
    - 0.018
  - model: GSPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.766
    metric_stds:
    - 0.019
  - model: BS-KAGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7646
    metric_stds:
    - 0.0366
  - model: ICGMM_f
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.764
    metric_stds:
    - 0.014
  - model: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.764
    metric_stds:
    - 0.017
  - model: HOPSE-G
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7636
    metric_stds:
    - 0.0175
  - model: GMT
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
    - 0.7635
    metric_stds:
    - 0.0262
  - model: HOPSE-M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7634
    metric_stds:
    - 0.014
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7629
    metric_stds:
    - 0.0179
  - model: CGMM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    date_iso: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    metric_stds:
    - 0.02
  - model: ECC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    metric_stds:
    - 0.014
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    metric_stds:
    - 0.018
  - model: GCCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7576
    metric_stds:
    - 0.0128
  - model: SCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.0104
  - model: GAT+PSEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7557
    metric_stds:
    - 0.006
  - model: CCCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7535
    metric_stds:
    - 0.015
  - model: KMIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.03
  - model: Eigen
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.03
  - model: GPSE + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.747
    metric_stds:
    - 0.0079
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.0073
  - model: CWN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.0206
  - model: --
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.03
  - model: TopK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.02
  - model: MinCut
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.03
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.03
  - model: IGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    metric_stds:
    - 0.015
  - model: RBF-KAGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7263
    metric_stds:
    - 0.04650000000000001
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.019
  - model: ASAP
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
    - 0.7148
    metric_stds:
    - 0.0042
  - model: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    metric_stds:
    - 0.006
  - model: AST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.06
  - model: SaNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.15405'
    title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
      Representations'
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6817
    metric_stds:
    - 0.0088
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    metric_stds:
    - 0.09
  - model: SAGPool
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
    - 0.6745
    metric_stds:
    - 0.0111
  - model: TopKPool
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
    - 0.6702
    metric_stds:
    - 0.0225
  - model: UniGNN2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    metric_stds:
    - 0.09
  - model: PathNet
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
    - 0.641
    metric_stds:
    - 0.023
  - model: PathNet (N=10, K=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.023
  - model: GK (k=3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.003
  - model: DiffPool
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
    - 0.6232
    metric_stds:
    - 0.019
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6042000000000001
    metric_stds:
    - 0.0821
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.601
    metric_stds:
    - 0.0463
  milestones:
  - value: 0.823
    std: 0.019
    model: PathNN-SP (K=2)
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
  - value: 0.86
    std: 0.018
    model: Kern. WL
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: 2023-10
---

