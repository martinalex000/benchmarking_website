---
title: Tox21
slug: tox21
benchmark: MoleculeNet
task_type: graph_classification
description: Multi-task toxicity prediction (12 tasks) on NCI Tox21 challenge compounds.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats:
  num_graphs: 7831
  avg_nodes: 18.6
  avg_edges: 38.6
  num_classes: 12
result_count: 77
best_model:
  model: HIMP
  value: 0.874
  metric: ROC-AUC
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  metrics:
  - ROC-AUC
  rows:
  - model: HIMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.874
    metric_stds:
    - 0.005
  - model: Ours(dual readout)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    metric_stds:
    - 0.008
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    metric_stds:
    - 0.009
  - model: ChemRL-GEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.849
    metric_stds:
    - 0.003
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.849
    metric_stds:
    - null
  - model: Ours(dual readout,VN, 567k)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.844
    metric_stds:
    - 0.006
  - model: Ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    metric_stds:
    - 0.003
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.84
    metric_stds:
    - 0.004
  - model: Kernel SVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    metric_stds:
    - 0.006
  - model: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    metric_stds:
    - 0.014
  - model: Logistic Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    metric_stds:
    - 0.015
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7851
    metric_stds:
    - 0.0077
  - model: MPNN + HOPE-WavePE
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
    - 0.78
    metric_stds:
    - 0.001
  - model: HOD-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7798999999999999
    metric_stds:
    - 0.0070999999999999995
  - model: HyMN (GIN, T=2) no CSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7782
    metric_stds:
    - 0.0059
  - model: HyMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7781999999999999
    metric_stds:
    - 0.0059
  - model: GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
    - null
  - model: GPSE augmented
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
    - 0.774
    metric_stds:
    - 0.008
  - model: Policy-Learn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7736
    metric_stds:
    - 0.006
  - model: POLICY-LEARN (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7736
    metric_stds:
    - 0.006
  - model: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    metric_stds:
    - 0.015
  - model: Mole-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.768
    metric_stds:
    - 0.005
  - model: SimSGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.768
    metric_stds:
    - 0.009
  - model: PretrainGNN
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    metric_stds:
    - 0.004
  - model: AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.767
    metric_stds:
    - 0.004
  - model: Self-supervised pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    metric_stds:
    - 0.004
  - model: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    metric_stds:
    - 0.0063
  - model: RANDOM (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    metric_stds:
    - 0.0089
  - model: LapPE augmented
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
    - 0.766
    metric_stds:
    - 0.003
  - model: GIN + Laplacian PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7659999999999999
    metric_stds:
    - null
  - model: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.763
    metric_stds:
    - 0.005
  - model: RWSE augmented
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
    - 0.763
    metric_stds:
    - 0.005
  - model: Full
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7625
    metric_stds:
    - 0.0112
  - model: AttentiveFP
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
    - 0.761
    metric_stds:
    - 0.005
  - model: BiScale-GTR (Molecule)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.761
    metric_stds:
    - 0.004
  - model: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7608
    metric_stds:
    - 0.0079
  - model: HyMN (GIN, T=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7607
    metric_stds:
    - 0.005
  - model: GraphFP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    metric_stds:
    - 0.005
  - model: D-MPNN
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
    - 0.759
    metric_stds:
    - 0.007
  - model: AllPSE augmented
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
    - 0.759
    metric_stds:
    - 0.01
  - model: N-GramXGB
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
    - 0.758
    metric_stds:
    - 0.009
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    metric_stds:
    - 0.003
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.004
  - model: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.007
  - model: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.005
  - model: MORE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.756
    metric_stds:
    - 0.005
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.755
    metric_stds:
    - 0.006
  - model: GIN_C (Vocab 200)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    metric_stds:
    - 0.004
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7529
    metric_stds:
    - 0.0069
  - model: Reconstr. GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7515000000000001
    metric_stds:
    - 0.013999999999999999
  - model: G-Contextual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.006
  - model: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.003
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7491
    metric_stds:
    - 0.0051
  - model: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    metric_stds:
    - 0.003
  - model: MGSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.749
    metric_stds:
    - 0.006
  - model: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    metric_stds:
    - 0.004
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    metric_stds:
    - 0.006
  - model: RWPT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: - Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7449
    metric_stds:
    - 0.014
  - model: N-GramRF
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
    - 0.743
    metric_stds:
    - 0.004
  - model: GROVERbase
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.743
    metric_stds:
    - 0.001
  - model: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    metric_stds:
    - 0.006
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    metric_stds:
    - 0.003
  - model: CP, alpha=0.1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.007
  - model: GraphFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.74
    metric_stds:
    - 0.007
  - model: GraphGPS+LAC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    metric_stds:
    - null
  - model: GraphFP_CP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    metric_stds:
    - 0.007
  - model: No pre-training
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
    - 0.74
    metric_stds:
    - 0.008
  - model: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    metric_stds:
    - 0.007
  - model: GraphLOG pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.739
    metric_stds:
    - 0.007
  - model: G-Motif
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    metric_stds:
    - 0.007
  - model: GROVER_large
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.001
  - model: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    metric_stds:
    - null
  - model: GraphLoG augmented
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
    - 0.732
    metric_stds:
    - 0.005
  - model: BiScale-GTR (Fragment)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.731
    metric_stds:
    - 0.009
  - model: GraphFP-JT_C
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    metric_stds:
    - 0.008
  - model: JOAOv2 pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.682
    metric_stds:
    - 0.008
  - model: InfoGraph pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.681
    metric_stds:
    - 0.006
  milestones:
  - value: 0.774
    std: 0.008
    model: GPSE augmented
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.874
    std: 0.005
    model: HIMP
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: 2023-10
---

