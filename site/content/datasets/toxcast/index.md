---
title: ToxCast
slug: toxcast
benchmark: MoleculeNet
task_type: graph_classification
description: Multi-task toxicological profile prediction (617 tasks) from the EPA
  ToxCast program.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats:
  num_graphs: 8597
  avg_nodes: 18.7
  avg_edges: 38.4
  num_classes: 617
result_count: 54
best_model:
  model: Ours(dual readout)
  value: 0.752
  metric: ROC-AUC
  arxiv_id: '2310.01704'
  paper_title: Transformers are efficient hierarchical chemical graph learners
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - ROC-AUC
  rows:
  - model: Ours(dual readout)
    model_plain: Ours(dual readout)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.752
    metric_stds:
    - 0.003
  - model: ChemRL-GEM
    model_plain: ChemRL-GEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.004
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    metric_stds:
    - 0.004
  - model: GraphGPS+LAC
    model_plain: GraphGPS+LAC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.002
  - model: Ours
    model_plain: Ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    metric_stds:
    - 0.001
  - model: HIMP
    model_plain: HIMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    metric_stds:
    - 0.004
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    metric_stds:
    - null
  - model: Kernel SVM
    model_plain: Kernel SVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    metric_stds:
    - 0.014
  - model: MPNN + HOPE-WavePE
    model_plain: MPNN + HOPE-WavePE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.669
    metric_stds:
    - 0.005
  - model: GPSE augmented
    model_plain: GPSE augmented
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    metric_stds:
    - 0.008
  - model: SimSGT
    model_plain: SimSGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.659
    metric_stds:
    - 0.008
  - model: LapPE augmented
    model_plain: LapPE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    metric_stds:
    - 0.007
  - model: PretrainGNN
    model_plain: PretrainGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.657
    metric_stds:
    - 0.006
  - model: RWSE augmented
    model_plain: RWSE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    metric_stds:
    - 0.003
  - model: D-MPNN
    model_plain: D-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.655
    metric_stds:
    - 0.003
  - model: GROVERbase
    model_plain: GROVERbase
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.654
    metric_stds:
    - 0.004
  - model: GROVER_large
    model_plain: GROVER_large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.653
    metric_stds:
    - 0.005
  - model: CP, alpha=0.1
    model_plain: CP, alpha=0.1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.648
    metric_stds:
    - 0.005
  - model: MORE
    model_plain: MORE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.646
    metric_stds:
    - 0.006
  - model: Mole-BERT
    model_plain: Mole-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.643
    metric_stds:
    - 0.002
  - model: AttrMasking
    model_plain: AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.642
    metric_stds:
    - 0.005
  - model: Self-supervised pre-trained
    model_plain: Self-supervised pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.642
    metric_stds:
    - 0.005
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.003
  - model: XGBoost
    model_plain: XGBoost
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    metric_stds:
    - 0.005
  - model: BiScale-GTR (Fragment)
    model_plain: BiScale-GTR (Fragment)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.002
  - model: ContextPred
    model_plain: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.006
  - model: GraphFP_CP
    model_plain: GraphFP_CP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.009
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.004
  - model: AllPSE augmented
    model_plain: AllPSE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.003
  - model: GIN_C (Vocab 200)
    model_plain: GIN_C (Vocab 200)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.637
    metric_stds:
    - 0.006
  - model: AttentiveFP
    model_plain: AttentiveFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    metric_stds:
    - 0.002
  - model: GraphLoG augmented
    model_plain: GraphLoG augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.636
    metric_stds:
    - 0.004
  - model: GraphLoG
    model_plain: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.635
    metric_stds:
    - 0.007
  - model: No pre-training
    model_plain: No pre-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.634
    metric_stds:
    - 0.006
  - model: MGSSL
    model_plain: MGSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.633
    metric_stds:
    - 0.005
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.633
    metric_stds:
    - 0.005
  - model: JOAOv2
    model_plain: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.632
    metric_stds:
    - 0.005
  - model: GraphFP
    model_plain: GraphFP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.632
    metric_stds:
    - 0.007
  - model: GraphMVP
    model_plain: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.631
    metric_stds:
    - 0.002
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.629
    metric_stds:
    - 0.005
  - model: G-Contextual
    model_plain: G-Contextual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.007
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.003
  - model: GraphMVP
    model_plain: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.627
    metric_stds:
    - 0.001
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.625
    metric_stds:
    - 0.004
  - model: GraphFP-JT_C
    model_plain: GraphFP-JT_C
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.625
    metric_stds:
    - 0.009
  - model: GraphLoG
    model_plain: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.002
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.006
  - model: GraphLOG pretrained
    model_plain: GraphLOG pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.006
  - model: G-Motif
    model_plain: G-Motif
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.623
    metric_stds:
    - 0.006
  - model: BiScale-GTR (Molecule)
    model_plain: BiScale-GTR (Molecule)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.622
    metric_stds:
    - 0.002
  - model: Logistic Regression
    model_plain: Logistic Regression
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    metric_stds:
    - 0.003
  - model: InfoGraph pretrained
    model_plain: InfoGraph pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.584
    metric_stds:
    - 0.006
  - model: JOAOv2 pre-trained
    model_plain: JOAOv2 pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.57
    metric_stds:
    - 0.005
  milestones:
  - value: 0.663
    std: 0.008
    model: GPSE augmented
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.752
    std: 0.003
    model: Ours(dual readout)
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: 2023-10
---

