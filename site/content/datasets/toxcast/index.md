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
result_count: 38
best_model:
  model: GraphGPS+LAC
  value: 0.737
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
    is_best: true
    metric_values:
    - 0.737
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
    - 0.663
    metric_stds:
    - 0.008
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
    - 0.659
    metric_stds:
    - 0.008
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
    - 0.659
    metric_stds:
    - 0.007
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
    - 0.656
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.648
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
    - 0.646
    metric_stds:
    - 0.006
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
    - 0.643
    metric_stds:
    - 0.002
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.642
    metric_stds:
    - 0.005
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
    - 0.642
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
    - 0.641
    metric_stds:
    - 0.003
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
    - 0.639
    metric_stds:
    - 0.002
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.006
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - 0.004
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
    - 0.639
    metric_stds:
    - 0.003
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.637
    metric_stds:
    - 0.006
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
    - 0.636
    metric_stds:
    - 0.004
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
    - 0.635
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
    - 0.634
    metric_stds:
    - 0.006
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.633
    metric_stds:
    - 0.005
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.633
    metric_stds:
    - 0.005
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.632
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.632
    metric_stds:
    - 0.007
  - model: GraphMVP
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
    - 0.631
    metric_stds:
    - 0.002
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.629
    metric_stds:
    - 0.005
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.007
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.003
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.627
    metric_stds:
    - 0.001
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.625
    metric_stds:
    - 0.004
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.625
    metric_stds:
    - 0.009
  - model: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.002
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.624
    metric_stds:
    - 0.006
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
    - 0.624
    metric_stds:
    - 0.006
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.623
    metric_stds:
    - 0.006
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
    - 0.622
    metric_stds:
    - 0.002
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
    - 0.584
    metric_stds:
    - 0.006
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
  - value: 0.737
    std: null
    model: GraphGPS+LAC
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: 2026-04
---

