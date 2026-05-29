---
title: PubMed
slug: pubmed
benchmark: Classic
task_type: node_classification
description: Citation network node classification (3 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 3
result_count: 1101
best_model:
  model: AIO
  value: 0.986
  metric: Accuracy
  arxiv_id: '2510.22555'
  paper_title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
variants:
- slug: planetoid-split
  name: Planetoid split
  notes: Yang et al. 2016 fixed split.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - AP
  - AUC
  - AUC-ROC
  - AUROC
  - F1
  - F1-micro
  - Ma-F1
  - Macro-F1
  - Mi-F1
  - Micro-F1
  - MicroF1
  - NMI
  rows:
  - model: AIO
    model_plain: AIO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.986
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-VAE/VGAE
    model_plain: S-VAE/VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGN
    model_plain: SAGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9517
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA-ND-7B
    model_plain: LLaGA-ND-7B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9503
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA-HO-7B
    model_plain: LLaGA-HO-7B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9503
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007000000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9490000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9487000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + LLM-based A-D
    model_plain: GCN + LLM-based A-D
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9475
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN + LLM-based LPA
    model_plain: TAPE_GCN + LLM-based LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9475
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN + LLM-based A-D
    model_plain: TAPE_GCN + LLM-based A-D
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9472
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + LLM-based LPA
    model_plain: GCN + LLM-based LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9469
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Flan-T5-large
    model_plain: Flan-T5-large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9462
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN-LPA
    model_plain: TAPE_GCN-LPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9461
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-LPA_DeBERTa
    model_plain: GCN-LPA_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Flan-T5-base
    model_plain: Flan-T5-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9445
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA-HO-7B(General)
    model_plain: LLaGA-HO-7B(General)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9445
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEdit
    model_plain: GraphEdit
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9409
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G-Prompt
    model_plain: G-Prompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.939
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Llama-7b
    model_plain: Llama-7b
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9384
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09078'
    title: 'Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis
      of GNN Explanation Methods'
    date: Jun 16, 2021
    date_iso: '2021-06-16'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9377
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9342
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LangGSL (LM)
    model_plain: LangGSL (LM)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9337
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LangGSL (GSLM)
    model_plain: LangGSL (GSLM)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9321
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GCN
    model_plain: TAPE_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9319
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE_GAT
    model_plain: TAPE_GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9316
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0115
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_DeBERTa
    model_plain: GCN_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9314
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT_DeBERTa
    model_plain: GAT_DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9312
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEdit-con
    model_plain: GraphEdit-con
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9312
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA-ND-7B(General)
    model_plain: LLaGA-ND-7B(General)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9242
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9233
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LangGSL
    model_plain: LangGSL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9214
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0131
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Policy-GNN
    model_plain: Policy-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AdaptKry
    model_plain: AdaptKry
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Snowball-V3
    model_plain: Snowball-V3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9096
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G2T-LimiX (FT)
    model_plain: G2T-LimiX (FT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EvenNet
    model_plain: EvenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Adapt
    model_plain: Adapt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.906
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAM-GT
    model_plain: DAM-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLM-incorporated
    model_plain: LLM-incorporated
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniMP + TAGs (8b)
    model_plain: UniMP + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLM-free
    model_plain: LLM-free
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPFN (ICL)
    model_plain: GraphPFN (ICL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPFN (FT)
    model_plain: GraphPFN (FT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OptBasisGNN
    model_plain: OptBasisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.903
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE
    model_plain: AD-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop_fast
    model_plain: AD-MixHop_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeBERTa
    model_plain: DeBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.902
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT +CAP
    model_plain: GAT +CAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + Vanilla
    model_plain: GAT + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-MixHop
    model_plain: AD-MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN + TAGs (8b)
    model_plain: HAN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0141
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PDE-Log
    model_plain: PDE-Log
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GaLGuard
    model_plain: GaLGuard
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.04894'
    title: Adversarial Attacks and Defenses on Graph-aware Large Language Models (LLMs)
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.9
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8998
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PDE-Expn
    model_plain: PDE-Expn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8992
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniMP
    model_plain: UniMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8992
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + FLAG
    model_plain: GraphSAGE + FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8991
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN*_SAGE
    model_plain: UDGNN*_SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8988
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-4o
    model_plain: GPT-4o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8985
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN_GCN
    model_plain: UDGNN_GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8985
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UDGNN*_GAT
    model_plain: UDGNN*_GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8978
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8977
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN + TAGs (70b)
    model_plain: HAN + TAGs (70b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8977
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8977
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoarFormer
    model_plain: CoarFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8975
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: simple GNN model (3-hop)
    model_plain: simple GNN model (3-hop)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8975
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8975
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LSGNN
    model_plain: LSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8973
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.897
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.897
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NewtonNet
    model_plain: NewtonNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8968
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8968
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN + TAGs (8b)
    model_plain: RGCN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8968
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN + TAGs (8b)
    model_plain: GIN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8968
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8962
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAFF
    model_plain: GRAFF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8959999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN-2
    model_plain: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8959
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + FLAG
    model_plain: GAT + FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8956
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8955
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SeHGNN + TAGs (8b)
    model_plain: SeHGNN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.895
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8949
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8947
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN-1
    model_plain: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLMs (2-layer)
    model_plain: LLMs (2-layer)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OptBasis
    model_plain: OptBasis
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8938
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFL-mean
    model_plain: GFL-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8936
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN
    model_plain: AD-DirGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8935
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE + Vanilla
    model_plain: GraphSAGE + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8932
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8931
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8929
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8926
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GATv2
    model_plain: AD-GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8926
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8925
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: novel graph MLP mixer
    model_plain: novel graph MLP mixer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8922
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIND
    model_plain: GIND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8922
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8922
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G2T-LimiX (ICL)
    model_plain: G2T-LimiX (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPNet
    model_plain: GPNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8912
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8909
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby+JK
    model_plain: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8907
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-DirGNN_fast
    model_plain: AD-DirGNN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8907
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8905
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8902
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8902
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SANE-hete
    model_plain: SANE-hete
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE
    model_plain: AD-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8896
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFL-att
    model_plain: GFL-att
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8896
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + FLAG
    model_plain: GCN + FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8892
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.889
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE_fast
    model_plain: AD-GraphSAGE_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8888
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8881
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.888
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8877
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8875
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8868
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-I-s
    model_plain: Geom-GCN-I-s
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LRGNN
    model_plain: LRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8865
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8864
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM
    model_plain: DGM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.886
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ES-MLP
    model_plain: ES-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8853
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8852
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RvGAT
    model_plain: RvGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IncGCN
    model_plain: IncGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8848
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8845
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MAML
    model_plain: MAML
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8844
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-I-g
    model_plain: Geom-GCN-I-g
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8844
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-JKNet
    model_plain: GCN-JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8841
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN_fast
    model_plain: AD-GCN_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8841
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (d=8)
    model_plain: DGM (d=8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (0 layers)
    model_plain: DGM (0 layers)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00537
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8839
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8839
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Global
    model_plain: Global
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8838
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OrderedGNN
    model_plain: OrderedGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8831
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8827
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT_fast
    model_plain: AD-GAT_fast
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FGSSL
    model_plain: FGSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8824
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (d=6)
    model_plain: DGM (d=6)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00601
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14855'
    title: 'CAP: Co-Adversarial Perturbation on Weights and Features for Improving
      Generalization of Graph Neural Networks'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8814
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8813
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAG-LimiX (ICL, E)
    model_plain: TAG-LimiX (ICL, E)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8809
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Whole Dataset
    model_plain: Whole Dataset
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN-IP
    model_plain: Geom-GCN-IP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SeHGNN
    model_plain: SeHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtoNet
    model_plain: ProtoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.879
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimMLP
    model_plain: SimMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SANE
    model_plain: SANE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8782
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (d=2)
    model_plain: DGM (d=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00531
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.14996'
    title: 'All Against Some: Efficient Integration of Large Language Models for Message
      Passing in Graph Neural Networks'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAG-TabPFNv2 (ICL, E)
    model_plain: TAG-TabPFNv2 (ICL, E)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.878
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BeltramiGuard
    model_plain: BeltramiGuard
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FedSage
    model_plain: FedSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.877
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8766
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    is_best: false
    metric_values:
    - 0.8765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (Euclidean)
    model_plain: DGM (Euclidean)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (d=4)
    model_plain: DGM (d=4)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (1 layer)
    model_plain: DGM (1 layer)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (GCN)
    model_plain: DGM (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.876
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEGSL
    model_plain: SEGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8753
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (MLP)
    model_plain: DGM (MLP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.875
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8747
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (EdgeConv)
    model_plain: DGM (EdgeConv)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.874
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00574
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PPRGo
    model_plain: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GAT
    model_plain: AD-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8737
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8734999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pro-GNN-fs
    model_plain: Pro-GNN-fs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: notations and formally define the problem
    model_plain: notations and formally define the problem
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8726
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.872
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WSGNN
    model_plain: WSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
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
    - 0.8713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.871
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.871
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-Jaccard
    model_plain: GCN-Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8704
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Beltrami
    model_plain: Beltrami
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperGRL
    model_plain: HyperGRL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8689
    - null
    - null
    - 0.9875
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8685
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8685
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Str-GCL
    model_plain: Str-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (GAT)
    model_plain: DGM (GAT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.868
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00914
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE + PiNGDA
    model_plain: GRACE + PiNGDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8679
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8668
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8665
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (Hyperbolic)
    model_plain: DGM (Hyperbolic)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00952
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCat
    model_plain: GCat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.865
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.15354'
    title: 'Polynomial Selection in Spectral Graph Neural Networks: An Error-Sum of
      Function Slices Approach'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: https://github.com/vasile-paskardlgm/TFGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8636
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLR
    model_plain: GLR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8635
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8634
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.863
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07608'
    title: 'Finding the Missing-half: Graph Complementary Learning for Homophily-prone
      and Heterophily-prone Graphs'
    date: Jun 13, 2023
    date_iso: '2023-06-13'
    date_display: Jun 2023
    codebase_url: https://github.com/zyzisastudyreallyhardguy/GOAL-Graph-Complementary-Learning
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8621
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLM4RGNN
    model_plain: LLM4RGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8621
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIB-Bern
    model_plain: GIB-Bern
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.12811'
    title: Graph Information Bottleneck
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.862
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0654
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8616
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8608
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8607
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8604
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIC
    model_plain: GIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8599
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8598
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8595
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.859
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOUDA
    model_plain: GOUDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8582
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8574
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PaGCL
    model_plain: PaGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8573
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Matchingnet
    model_plain: Matchingnet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8565
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    model_plain: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8561
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.856
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SP-AGCL
    model_plain: SP-AGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AT
    model_plain: AT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.855
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8545
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEdit
    model_plain: GraphEdit
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8538
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC-v2
    model_plain: SGC-v2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8536
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8531
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8531
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FedAvg
    model_plain: FedAvg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8529
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SLAPS
    model_plain: SLAPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8521
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FedProx
    model_plain: FedProx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8521
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeoMix (EXPHORMER)
    model_plain: GeoMix (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.852
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.852
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8519
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TADA (EXPHORMER)
    model_plain: TADA (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIB-Cat
    model_plain: GIB-Cat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.12811'
    title: Graph Information Bottleneck
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8507
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8505
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FLAG (EXPHORMER)
    model_plain: FLAG (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMix (EXPHORMER)
    model_plain: GraphMix (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8495
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GASSL
    model_plain: GASSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8491
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NODEDUP (EXPHORMER)
    model_plain: NODEDUP (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.849
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGGD (EXPHORMER)
    model_plain: LGGD (EXPHORMER)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNGuard
    model_plain: GNNGuard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8475
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8473
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sp^2GCL + PiNGDA
    model_plain: Sp^2GCL + PiNGDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8473
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-X
    model_plain: Logistic Reg.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.847
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8468
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8466
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (EXPHORMER)
    model_plain: DoG (EXPHORMER)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.846
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8456
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACEIS
    model_plain: GRACEIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8455
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAUG
    model_plain: GAUG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15183'
    title: 'GraphEdit: Large Language Models for Graph Structure Learning'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/HKUDS/GraphEdit
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8448
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FedOpt
    model_plain: FedOpt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8439
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8437
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DFNet
    model_plain: DFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.843
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Patton
    model_plain: Patton
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8428
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL
    model_plain: TriCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8426
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SP^2GCL
    model_plain: SP^2GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8426
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8423
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8422
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8421
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGM (ID)
    model_plain: DGM (ID)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04999'
    title: Differentiable Graph Module (DGM) for Graph Convolutional Networks
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/lcosmo/DGM_pytorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.842
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.00165
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.842
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT
    model_plain: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/sunshy-1/LLM4GraphTopology
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8419
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ASGC
    model_plain: ASGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8417
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8412
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8408
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGCN
    model_plain: UniGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8408
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8403
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8402
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAT-I-SC
    model_plain: CAT-I-SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8402
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8396
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8394
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SelfTask-GNN
    model_plain: SelfTask-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8392
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8388
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0077
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8383
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Local
    model_plain: Local
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18937'
    title: Federated Graph Semantic and Structural Learning
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/GuanchengWan/FGSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8381
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAIL
    model_plain: SAIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.838
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSF-GPR-I
    model_plain: DSF-GPR-I
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.09041'
    title: Graph Neural Networks with Diverse Spectral Filtering
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jingweio/DSF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8374
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TriCL-N
    model_plain: TriCL-N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8368
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8367
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAT-I-MF
    model_plain: CAT-I-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.836
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8352
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVD
    model_plain: GCN-SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.10203'
    title: Graph Structure Learning for Robust Graph Neural Networks
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/ChandlerBang/Pro-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NWR-GAE full
    model_plain: NWR-GAE full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NWR-GAE
    model_plain: NWR-GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperConv
    model_plain: HyperConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8342
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond STABLE_G
    model_plain: GCond STABLE_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.8331
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.09041'
    title: Graph Neural Networks with Diverse Spectral Filtering
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/jingweio/DSF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.833
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SNAG
    model_plain: SNAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GraphMAE)
    model_plain: DoG (GraphMAE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.832
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: All-Graph-Finetune (AGF)
    model_plain: All-Graph-Finetune (AGF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8306
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL-Anch
    model_plain: IDGL-Anch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGCN_n + DropNode
    model_plain: PGCN_n + DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8298
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MUSE
    model_plain: MUSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AllSet
    model_plain: AllSet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8285
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GCN)
    model_plain: DoG (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (GGD)
    model_plain: DoG (GGD)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8278
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_n + DropNode
    model_plain: GCN_n + DropNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.827
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8263
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8262
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8259
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-k-Lap
    model_plain: GAT-k-Lap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8256
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ALT-OPT
    model_plain: ALT-OPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: simple Teacher-Free Graph Self-Distillation (TGS) framework
    model_plain: simple Teacher-Free Graph Self-Distillation (TGS) framework
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03483'
    title: A Teacher-Free Graph Knowledge Distillation Framework with Dual Self-Distillation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/LirongWu/TGS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8242
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE-MLP
    model_plain: GRACE-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.824
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8239
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0488
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + PCL
    model_plain: GCN + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8232
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8228
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.822
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM Jaccard
    model_plain: GCDM Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM - GSL
    model_plain: GCDM - GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + PCL
    model_plain: GAT + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8214
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2-HHGR
    model_plain: S2-HHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8213
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.821
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Local-GCL
    model_plain: Local-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.08048'
    title: Towards Understanding the Generalization of Graph Neural Networks
    date: May 14, 2023
    date_iso: '2023-05-14'
    date_display: May 2023
    codebase_url: https://github.com/jianhao2016/GPRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM Plain
    model_plain: GCDM Plain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL-LR-Attention
    model_plain: GCL-LR-Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diffusion-A
    model_plain: Diffusion-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8198
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8196
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-NetMF
    model_plain: GAT-NetMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAT-GAE
    model_plain: HAT-GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8188
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP for adjacency matrix only
    model_plain: MLP for adjacency matrix only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8187
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.02534'
    title: 'MGAE: Masked Autoencoders for Self-Supervised Learning on Graphs'
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8185
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0101
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DoG (MVGRL)
    model_plain: DoG (MVGRL)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMNN
    model_plain: GMNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Grain(ball-D)
    model_plain: Grain(ball-D)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-GNN
    model_plain: GLEM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8172
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SuperGAT
    model_plain: SuperGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.817
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAG + DIFFORMER-a
    model_plain: DAG + DIFFORMER-a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UGCL
    model_plain: UGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond + GSL
    model_plain: GCond + GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.815
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: struc2vec
    model_plain: struc2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8149
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MAGNA
    model_plain: MAGNA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond Plain
    model_plain: GCond Plain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.814
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GGD
    model_plain: GGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDEM + STABLE_G
    model_plain: GDEM + STABLE_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + SSL
    model_plain: GCN + SSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.02380'
    title: Self-supervised Training of Graph Convolutional Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8123
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KNN w/ sp.-A
    model_plain: KNN w/ sp.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8121
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGMLP
    model_plain: DGMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMD-ACMP
    model_plain: DMD-ACMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IPGDN
    model_plain: IPGDN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GCN
    model_plain: AD-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARIEL
    model_plain: ARIEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13854'
    title: arXiv:2306.13854
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/yeonjun-in/torch-SP-AGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8102
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0148
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATNE
    model_plain: GATNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8101
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-Jaccard
    model_plain: GCN-Jaccard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCL-LRR
    model_plain: GCL-LRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ECL-GSR
    model_plain: ECL-GSR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8091
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.809
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimP-GCN
    model_plain: SimP-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.808
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3-CL
    model_plain: S^3-CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Grain(NN-D)
    model_plain: Grain(NN-D)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S3-CL
    model_plain: S3-CL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8073
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ESC-GNN
    model_plain: ESC-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.807
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.807
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GBP
    model_plain: GBP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN_kNN
    model_plain: GCN_kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.806
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Logistic Reg.-A
    model_plain: Logistic Reg.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ada-Ugnn
    model_plain: Ada-Ugnn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ELU-GCN
    model_plain: ELU-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.13148'
    title: Transformers over Directed Acyclic Graphs
    date: Oct 24, 2022
    date_iso: '2022-10-24'
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-mean
    model_plain: NAFS-mean
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBM
    model_plain: SBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13060'
    title: Graph Attention Retrospective
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.11430'
    title: Independence Promoted Graph Disentangled Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphHeat
    model_plain: GraphHeat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.16002'
    title: Graph Convolutional Networks using Heat Kernel for Semi-supervised Learning
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.805
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-max
    model_plain: NAFS-max
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM kNN
    model_plain: GCDM kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ADGCN-R
    model_plain: ADGCN-R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.804
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HGRL
    model_plain: HGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAFS-concat
    model_plain: NAFS-concat
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVD
    model_plain: GCN-SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM SVD
    model_plain: GCDM SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.13200'
    title: 'RobGC: Towards Robust Graph Condensation'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/XYGaoG/RobGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGD-GCN
    model_plain: LGD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.16026'
    title: 'MUSE: Multi-View Contrastive Learning for Heterophilic Graphs'
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KNN w/ sp.-X
    model_plain: KNN w/ sp.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoATA
    model_plain: CoATA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CG^3
    model_plain: CG^3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeoMix
    model_plain: GeoMix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-Deep
    model_plain: GAT-Deep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MERIT
    model_plain: MERIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PushNet-TPP
    model_plain: PushNet-TPP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.801
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0133
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DualGCN
    model_plain: DualGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PPRGo
    model_plain: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-Explainable GNN
    model_plain: Self-Explainable GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARIEL
    model_plain: ARIEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CRGNN
    model_plain: CRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGCL
    model_plain: SGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7998
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAI
    model_plain: NAI
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.00495'
    title: Efficient Graph Neural Network Inference at Large Scale
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7997
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7997
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGCN
    model_plain: DAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7995
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDE-rk2
    model_plain: GCDE-rk2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^2GC
    model_plain: S^2GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMD++
    model_plain: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UFGConv-S
    model_plain: UFGConv-S
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW
    model_plain: GraphGLOW
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMLP-O
    model_plain: FMLP-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.799
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-GraphPart
    model_plain: DA-GraphPart
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7989
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7988
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE
    model_plain: TAPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN + PCL
    model_plain: GIN + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7983
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H-GCN
    model_plain: H-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDC_PPR
    model_plain: GDC_PPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN (MXNet)
    model_plain: TAGCN (MXNet)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP (MXNet)
    model_plain: APPNP (MXNet)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CGPN
    model_plain: CGPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PushNet
    model_plain: PushNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0139
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.03147'
    title: Learning Conjoint Attentions for Graph Neural Nets
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7978
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FOSSIL
    model_plain: FOSSIL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7976
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UFG
    model_plain: UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N-GCN_a
    model_plain: N-GCN_a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N-GCN_fc
    model_plain: N-GCN_fc
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDC_HK
    model_plain: GDC_HK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06443'
    title: How Wide and How Deep? Mitigating Over-Squashing of GNNs via Channel Capacity
      Constrained Estimation
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/pixelhero98/C3E
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP Paper
    model_plain: APPNP Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph-MLP
    model_plain: Graph-MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: g-U-Nets
    model_plain: g-U-Nets
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.05178'
    title: Graph U-Nets
    date: May 11, 2019
    date_iso: '2019-05-11'
    date_display: May 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Snowball
    model_plain: Snowball
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diff-GCN
    model_plain: Diff-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPR
    model_plain: GPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN + DropEdge
    model_plain: GCN + DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph U-Net
    model_plain: Graph U-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.06127'
    title: 'Reinforcement learning on graphs: A survey'
    date: Apr 2022
    date_iso: 2022-04
    date_display: Apr 2022
    codebase_url: https://github.com/neunms/Reinforcement-learning-on-graphs-A-survey
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-GCN
    model_plain: Shift-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNNs
    model_plain: DNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EP-B
    model_plain: EP-B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPAGAN
    model_plain: SPAGAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.03464'
    title: 'SPAGAN: Shortest Path Graph Attention Network'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/ihollywhy/SPAGAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN
    model_plain: LGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDE-rk4 (4)
    model_plain: GCDE-rk4 (4)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN_sub
    model_plain: LGCN_sub
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN_whole
    model_plain: LGCN_whole
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Incep(Drop)
    model_plain: Incep(Drop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGWNN_wide
    model_plain: LGWNN_wide
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperSAGE
    model_plain: HyperSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7949
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet + PCL
    model_plain: ChebNet + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7948
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Framelets
    model_plain: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMD-SGC
    model_plain: DMD-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EE-UFG
    model_plain: EE-UFG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_knn
    model_plain: GraphGLOW_knn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pro-GNN
    model_plain: Pro-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NS-SAGE
    model_plain: NS-SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpatUFG
    model_plain: SpatUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj.
    model_plain: GB-GNN Adj.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN SAMME.R
    model_plain: GB-GNN SAMME.R
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN SAMME.R + Fine Tuning
    model_plain: GB-GNN SAMME.R + Fine Tuning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II
    model_plain: GB-GNN-II
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN Paper
    model_plain: TAGCN Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGCN DGL PyTorch
    model_plain: TAGCN DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08480'
    title: Eliciting Structural and Semantic Global Knowledge in Unsupervised Graph
      Contrastive Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/kaize0409/S-3-CL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PSAGNN
    model_plain: PSAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7939
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7938
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOPE (FT)
    model_plain: GCOPE (FT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7935
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph-Bert
    model_plain: Graph-Bert
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMD-GCN
    model_plain: DMD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: linear Snowball
    model_plain: linear Snowball
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAPHITE
    model_plain: GRAPHITE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.10459'
    title: 'Graphite: Iterative Generative Modeling of Graphs'
    date: Mar 28, 2018
    date_iso: '2018-03-28'
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DCNN (our implementation)
    model_plain: DCNN (our implementation)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HANet
    model_plain: HANet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1907.04786'
    title: Fast Haar Transforms for Graph Neural Networks
    date: Jul 2019
    date_iso: 2019-07
    date_display: Jul 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP DGL PyTorch
    model_plain: APPNP DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAuG-O
    model_plain: GAuG-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KCG
    model_plain: KCG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.793
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEGSL
    model_plain: SEGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7926
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoGCL
    model_plain: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Snowball
    model_plain: Snowball
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LoopyNet
    model_plain: LoopyNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.05140'
    title: 'Graph-Bert: Only Attention is Needed for Learning Graph Representations'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/jwzhanggy/Graph-Bert
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SuperGAT
    model_plain: SuperGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Partially absorbing
    model_plain: Partially absorbing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.13060'
    title: Graph Attention Retrospective
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JKNet(Drop)
    model_plain: JKNet(Drop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II + Fine Tuning L=1
    model_plain: GB-GNN-II + Fine Tuning L=1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN II + FT
    model_plain: GB-GNN II + FT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN DGL TensorFlow
    model_plain: GCN DGL TensorFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TIFA-GCL
    model_plain: TIFA-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAM
    model_plain: GAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-LM
    model_plain: GLEM-LM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEMLLM
    model_plain: GLEMLLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-RIM
    model_plain: DA-RIM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7917
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22299'
    title: 'CoATA: Effective Co-Augmentation of Topology and Attribute for Graph Neural
      Networks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7916
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N.S.-GCN
    model_plain: N.S.-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7914
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + SSL
    model_plain: GAT + SSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.02380'
    title: Self-supervised Training of Graph Convolutional Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7914
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ParetoGNN + GraphPatcher
    model_plain: ParetoGNN + GraphPatcher
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.00800'
    title: 'GraphPatcher: Mitigating Degree Bias for Graph Neural Networks via Test-time
      Augmentation'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/jumxglhf/GraphPatcher
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7911
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN KTA
    model_plain: GB-GNN KTA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AF-GCL
    model_plain: AF-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AERO-GNN
    model_plain: AERO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FOSSIL v2
    model_plain: FOSSIL v2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7909
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MUSE
    model_plain: MUSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7908
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Renormalization trick
    model_plain: Renormalization trick
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CNNs
    model_plain: CNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: StochasticGCN
    model_plain: StochasticGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LGCN_sub-GCN
    model_plain: LGCN_sub-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N-SAGE_a
    model_plain: N-SAGE_a
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Convolutional Network
    model_plain: Graph Convolutional Network
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Attention Network
    model_plain: Graph Attention Network
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Variance Reduction
    model_plain: Variance Reduction
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.08150'
    title: Hypergraph Convolution and Hypergraph Attention
    date: Jan 2019
    date_iso: 2019-01
    date_display: Jan 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUFG
    model_plain: SUFG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^2GC
    model_plain: S^2GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RTGNN
    model_plain: RTGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SFA
    model_plain: SFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFSA
    model_plain: GFSA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj. + Fine Tuning
    model_plain: GB-GNN Adj. + Fine Tuning
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN Adj. + FT
    model_plain: GB-GNN Adj. + FT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC Paper
    model_plain: SGC Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN Paper
    model_plain: GCN Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE DGL MXNet
    model_plain: GraphSAGE DGL MXNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-ppr
    model_plain: GAT-ppr
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-GAT
    model_plain: Shift-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7898
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7892
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPart
    model_plain: GraphPart
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN (rand. splits)
    model_plain: GCN (rand. splits)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLN
    model_plain: GLN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII_16
    model_plain: GCNII_16
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphArm
    model_plain: GraphArm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.789
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-GraphPart-W
    model_plain: PS-GraphPart-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-FeatProp
    model_plain: PS-FeatProp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7884
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0105
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7881
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PTDNet-GCN
    model_plain: PTDNet-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7881
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VEPM
    model_plain: VEPM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_at
    model_plain: GraphGLOW_at
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KP-GIN
    model_plain: KP-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random Policy
    model_plain: Random Policy
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN+GDC
    model_plain: GCN+GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_cos
    model_plain: GraphGLOW_cos
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RCL
    model_plain: RCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.12096'
    title: Bridging Large Language Models and Graph Structure Learning Models for
      Robust Representation Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ResGCN
    model_plain: ResGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00955'
    title: Evaluating Deep Graph Neural Networks
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDC
    model_plain: GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coteaching+
    model_plain: Coteaching+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CP
    model_plain: CP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-II L=0
    model_plain: GB-GNN-II L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT DGL PyTorch
    model_plain: GAT DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GWNN
    model_plain: GWNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PDTNet
    model_plain: PDTNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TED-GCN
    model_plain: TED-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BAGCN
    model_plain: BAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7854
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.00797'
    title: Beyond Low-frequency Information in Graph Convolutional Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDE-dpr5 (158)
    model_plain: GCDE-dpr5 (158)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07532'
    title: Graph Neural Ordinary Differential Equations
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: N-SAGE_fc
    model_plain: N-SAGE_fc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC DGL
    model_plain: SGC DGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT (TensorFlow)
    model_plain: GAT (TensorFlow)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GeniePath
    model_plain: GeniePath
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.03464'
    title: 'SPAGAN: Shortest Path Graph Attention Network'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/ihollywhy/SPAGAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT^3
    model_plain: GAT^3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.03464'
    title: 'SPAGAN: Shortest Path Graph Attention Network'
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/ihollywhy/SPAGAN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE + GraphPatcher
    model_plain: GRACE + GraphPatcher
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.00800'
    title: 'GraphPatcher: Mitigating Degree Bias for Graph Neural Networks via Test-time
      Augmentation'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/jumxglhf/GraphPatcher
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7848999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGCN_n
    model_plain: PGCN_n
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.12578'
    title: Graph Convolutional Neural Networks with Node Transition Probability-based
      Message Passing and DropNode Regularization
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ParetoGNN
    model_plain: ParetoGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.00800'
    title: 'GraphPatcher: Mitigating Degree Bias for Graph Neural Networks via Test-time
      Augmentation'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/jumxglhf/GraphPatcher
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7831999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LNet
    model_plain: LNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LanczosNet
    model_plain: LanczosNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.05767'
    title: Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE DGL PyTorch
    model_plain: GraphSAGE DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree
    model_plain: Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Self-training
    model_plain: Self-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANRMAB
    model_plain: ANRMAB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.00219'
    title: 'Grain: Improving Data Efficiency of Graph Neural Networks via Diversified
      Influence Maximization'
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/zwt233/Grain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ERASE
    model_plain: ERASE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7816
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AdaLNet
    model_plain: AdaLNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AD-GraphSAGE
    model_plain: AD-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.19382'
    title: Causal invariant geographic network representations with feature and structural
      distribution shifts
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.781
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSR
    model_plain: GSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7809
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGSR
    model_plain: SGSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7809
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI + GraphPatcher
    model_plain: DGI + GraphPatcher
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.00800'
    title: 'GraphPatcher: Mitigating Degree Bias for Graph Neural Networks via Test-time
      Augmentation'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/jumxglhf/GraphPatcher
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7804000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7802
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UnionNET
    model_plain: UnionNET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MERIT
    model_plain: MERIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sel-Cl
    model_plain: Sel-Cl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Jo-SRC
    model_plain: Jo-SRC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HONGAT
    model_plain: HONGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.09600'
    title: Graph Contrastive Learning with Low-Rank Regularization and Low-Rank Attention
      for Noisy Node Classification
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/Statistical-Deep-Learning/GCL-LR-Attention
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-KTA L=0
    model_plain: GB-GNN-KTA L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN DGL PyTorch
    model_plain: GCN DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-RIM-W
    model_plain: DA-RIM-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7794
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GB-GNN-Adj L=0
    model_plain: GB-GNN-Adj L=0
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7788
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FSM-IRL
    model_plain: FSM-IRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.19382'
    title: Causal invariant geographic network representations with feature and structural
      distribution shifts
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7783
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1st-order term only
    model_plain: 1st-order term only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.778
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APL
    model_plain: APL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7779
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0116
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCE
    model_plain: GCE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7779
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0143
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-GCN
    model_plain: GraphSAGE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.19382'
    title: Causal invariant geographic network representations with feature and structural
      distribution shifts
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Co-Dis
    model_plain: Co-Dis
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7764
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0234
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE (our implementation)
    model_plain: SAGE (our implementation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DS-GNN
    model_plain: DS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-GAT
    model_plain: JK-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0225
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HSIC-C-GraphSAGE
    model_plain: HSIC-C-GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.19382'
    title: Causal invariant geographic network representations with feature and structural
      distribution shifts
    date: Mar 2025
    date_iso: 2025-03
    date_display: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7753
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PushNet-PTP
    model_plain: PushNet-PTP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0205
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1st-order model
    model_plain: 1st-order model
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Forward
    model_plain: Forward
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04714'
    title: 'NRGNN: Learning a Label Noise-Resistant Graph Neural Network on Sparsely
      and Noisily Labeled Graphs'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/EnyanDai/NRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UFGConvS
    model_plain: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.01660'
    title: Graph Neural Networks With Lifting-based Adaptive Graph Wavelets
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Single parameter
    model_plain: Single parameter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-mean
    model_plain: GS-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphTrans_UltrasSmall
    model_plain: GraphTrans_UltrasSmall
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-K
    model_plain: GCN-K
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(N2V, l=1)
    model_plain: GZoom(N2V, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NOSMOG
    model_plain: NOSMOG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7734
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0236
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-GCN
    model_plain: FS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CE
    model_plain: CE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-DVAT
    model_plain: GCN-DVAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGLOW_dp
    model_plain: GraphGLOW_dp
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.11264'
    title: 'GraphGLOW: Open-World Graph Structure Learning for Cross-Graph Topology
      Refinement'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/WtaoZhao/GraphGLOW
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GC-RWCS
    model_plain: GC-RWCS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.05057'
    title: Towards More Practical Adversarial Attacks on Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/Mark12Ding/GNN-Practical-Attack
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNJK
    model_plain: GCNJK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7723
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0201
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-SVAT
    model_plain: GCN-SVAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.02174'
    title: 'Break the Ceiling: Stronger Multi-scale Deep Graph Convolutional Networks'
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: https://github.com/PwnerHarry/Stronger_GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(DW, l=1)
    model_plain: GZoom(DW, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI DGL TensorFlow
    model_plain: DGI DGL TensorFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.772
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0178
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FeatProp
    model_plain: FeatProp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(DGI, l=2)
    model_plain: GZoom(DGI, l=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11689'
    title: Self-Supervised Graph Representation Learning via Topology Transformations
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/gyshgx868/topo-ter
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ortho-GCN
    model_plain: Ortho-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PTDNet
    model_plain: PTDNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09755'
    title: Finding Heterophilic Neighbors via Confidence-based Subgraph Matching for
      Semi-supervised Node Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT
    model_plain: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7689
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LM (appr.)
    model_plain: LM (appr.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (64)
    model_plain: LADIES (64)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI Paper
    model_plain: DGI Paper
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN+T
    model_plain: GNN+T
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7672
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0112
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_iso: '2013-12-21'
    date_display: Dec 2013
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-meanpool
    model_plain: GS-meanpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: C&S
    model_plain: C&S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08583'
    title: arXiv:2206.08583
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/PKU-DAIR/NAFS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC+DGCN
    model_plain: SGC+DGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PolyGCL
    model_plain: PolyGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7639
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7631
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.763
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet (DGL PyTorch)
    model_plain: MoNet (DGL PyTorch)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.763
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12063'
    title: 'HAT-GAE: Self-Supervised Graph Auto-encoders with Hierarchical Adaptive
      Masking and Trainable Corruption'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7629
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7627
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RIM
    model_plain: RIM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7622
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RiemannGFM
    model_plain: RiemannGFM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GS-maxpool
    model_plain: GS-maxpool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAny
    model_plain: GraphAny
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI DGL PyTorch
    model_plain: DGI DGL PyTorch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Diffusion-X
    model_plain: Diffusion-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7602
    - null
    - null
    - 0.9747
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Text-Embedding-3-Large
    model_plain: Text-Embedding-3-Large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7596
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (512)
    model_plain: LADIES (512)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom_F+MILE(DW)
    model_plain: GZoom_F+MILE(DW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7587
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC+Cheb
    model_plain: GSC+Cheb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7575
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PI-GNN
    model_plain: PI-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7563
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7561
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.756
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLNN
    model_plain: GLNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7559
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0246
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LM
    model_plain: LM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7555
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RobustGCN
    model_plain: RobustGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.07754'
    title: On the Robustness of Graph Neural Diffusion to Topology Perturbations
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/zknus/Robustness-of-Graph-Neural-Diffusion
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7555
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7532
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.753
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FMLP-S
    model_plain: FMLP-S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MCR^2
    model_plain: MCR^2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.08852'
    title: 'ERASE: Error-Resilient Representation Learning on Graphs for Label Noise
      Tolerance'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/eraseai/erase
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7503
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Degree-W
    model_plain: PS-Degree-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7483
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MoNet (MXNet)
    model_plain: MoNet (MXNet)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.08550'
    title: Optimization and Generalization Analysis of Transduction through Gradient
      Boosting and Application to Multi-scale Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/delta2323/GB-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOFA
    model_plain: GOFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7476
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ENGINE
    model_plain: ENGINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7474
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7468
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphText
    model_plain: GraphText
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7464
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLM2Vec
    model_plain: LLM2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7457
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7455
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-RIM-W
    model_plain: PS-RIM-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7452
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Density-W
    model_plain: PS-Density-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: C-Density
    model_plain: C-Density
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7443
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Chebyshev
    model_plain: Chebyshev
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1808.03965'
    title: Large-Scale Learnable Graph Convolutional Networks
    date: Aug 2018
    date_iso: 2018-08
    date_display: Aug 2018
    codebase_url: https://github.com/divelab/lgcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (8192)
    model_plain: FastGCN (8192)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby
    model_plain: Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.14332'
    title: Multi-hop Attention Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/xjtuwgt/GNN-MAGNA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(DGI, l=1)
    model_plain: MILE(DGI, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Shift-MLP
    model_plain: Shift-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.744
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-NN
    model_plain: K-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7433
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk + Features
    model_plain: DeepWalk + Features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-AGE
    model_plain: DA-AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.07295'
    title: Adversarial Graph Disentanglement with Component-specific Aggregation
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/SsGood/ADGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPT-Mix-7B
    model_plain: GraphGPT-Mix-7B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7415999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7415
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Degree
    model_plain: DA-Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7411
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CDC
    model_plain: CDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random-W
    model_plain: Random-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7392
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ICA
    model_plain: ICA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bruna et al.
    model_plain: Bruna et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral
    model_plain: Spectral
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.06986'
    title: How Framelets Enhance Graph Neural Networks
    date: Feb 13, 2021
    date_iso: '2021-02-13'
    date_display: Feb 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.739
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Chebyshev filter (K=3)
    model_plain: Chebyshev filter (K=3)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Pagerank
    model_plain: DA-Pagerank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.7347
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-Density
    model_plain: DA-Density
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7339
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Random-W
    model_plain: PS-Random-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7331
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0165
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.04051'
    title: 'Graph-MLP: Node Classification without Message Passing in Graph'
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPS
    model_plain: GPS
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
    - 0.7327
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0184
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7327
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP-K
    model_plain: MLP-K
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP + PCL
    model_plain: MLP + PCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.09532'
    title: Pseudo Contrastive Learning for Graph-based Semi-supervised Learning
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Density-W
    model_plain: Density-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UGBA
    model_plain: UGBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7298
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0215
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bt.FP
    model_plain: Bt.FP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7294
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7293
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RobustGCN
    model_plain: RobustGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7291
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom_F+MILE(N2V)
    model_plain: GZoom_F+MILE(N2V)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter
    model_plain: GraphAdapter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7275
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LabelProp NL
    model_plain: LabelProp NL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: Dec 2018
    date_iso: 2018-12
    date_display: Dec 2018
    codebase_url: https://github.com/Hanjun-Dai/steady_state_embedding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoBFormer
    model_plain: CoBFormer
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
    - 0.7203
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0133
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Transformer + CAR
    model_plain: Transformer + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBA
    model_plain: SBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GTA
    model_plain: GTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DPGBA
    model_plain: DPGBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Full-Batch
    model_plain: Full-Batch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.16002'
    title: Graph Convolutional Networks using Heat Kernel for Semi-supervised Learning
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.717
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.715
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0297
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Multi-layer perceptron
    model_plain: Multi-layer perceptron
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC
    model_plain: S^3GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBert + NA
    model_plain: SBert + NA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7126
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InstructGLM
    model_plain: InstructGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7126
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RoBERTa (355M)
    model_plain: RoBERTa (355M)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7121
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT + CAR
    model_plain: GAT + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Label Propagation
    model_plain: Label Propagation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CP-GBA
    model_plain: CP-GBA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HARP(DW)
    model_plain: HARP(DW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.706
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BNLL
    model_plain: BNLL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UniGLM
    model_plain: UniGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OpenGraph (ICL)
    model_plain: OpenGraph (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0267
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HARP(N2V)
    model_plain: HARP(N2V)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.701
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6998
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
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
    - 0.6987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Feat
    model_plain: Feat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph scattering
    model_plain: Graph scattering
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGC
    model_plain: AGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6978
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SpecFormer
    model_plain: SpecFormer
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
    - 0.6973
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6954
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
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
    - 0.6953
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: METIS
    model_plain: METIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.693
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FS-MLP
    model_plain: FS-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.08025'
    title: 'GraphCL: Contrastive Self-Supervised Learning of Graph Representations'
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.69
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pagerank
    model_plain: Pagerank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6886
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree-W
    model_plain: Degree-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6824
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-Pagerank-W
    model_plain: PS-Pagerank-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6823
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCGC
    model_plain: CCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Degree
    model_plain: Degree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.674
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.20885'
    title: A Fused Gromov-Wasserstein Approach to Subgraph Contrastive Learning
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/sangaram/FOSSIL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNNGuard
    model_plain: GNNGuard
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6645
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6623
    - null
    - null
    - 0.9314
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Convolutional Network
    model_plain: Graph Convolutional Network
    is_baseline: false
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
    - 0.66
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sent-BERT (22M)
    model_plain: Sent-BERT (22M)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6593
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EvenNet
    model_plain: EvenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6591
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DA-AGE-W
    model_plain: DA-AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6585
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6568
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.12931'
    title: Demystifying Graph Convolution with a Simple Concatenation
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://bitbucket.org/gconcat2021/graph-concatenation
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6554
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6548
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6535
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005600000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AnyGraph (ICL)
    model_plain: AnyGraph (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6531
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.8 (99.48%)
    model_plain: k-means+EGG 0.8 (99.48%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6521
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0135
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6469
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0232
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(DW, l=1)
    model_plain: MILE(DW, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.645
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoT
    model_plain: CoT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6443
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0996
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TS-GNN (ICL)
    model_plain: TS-GNN (ICL)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.21489'
    title: 'GraphPFN: A Prior-Data Fitted Graph Foundation Model'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: https://github.com/yandex-research/graphpfn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6441
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0511
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGE-W
    model_plain: AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.643
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LogReg
    model_plain: LogReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6408
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PS-AGE-W
    model_plain: PS-AGE-W
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.04668'
    title: Label-free Node Classification on Graphs with Large Language Models (LLMs)
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/CurryTang/LLMGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NoisyGCN
    model_plain: NoisyGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6378
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BERT (110M)
    model_plain: BERT (110M)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6369
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.2 (64.98%)
    model_plain: k-means+EGG 0.2 (64.98%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6339
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IA-GPL
    model_plain: IA-GPL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6333
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6332
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.011899999999999999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6311
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProG
    model_plain: ProG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6307
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1196
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: k-means+EGG 0.5 (97.18%)
    model_plain: k-means+EGG 0.5 (97.18%)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15068'
    title: Embedding Graphs on Grassmann Manifold
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/conf20/Egg
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0228
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred SpikingGPF
    model_plain: EdgePred SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TSVM
    model_plain: TSVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.622
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.17185'
    title: 'Robustness in Text-Attributed Graph Learning: Insights, Trade-offs, and
      New Defenses'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/Leirunlin/TGRB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6194
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6186
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MILE(N2V, l=1)
    model_plain: MILE(N2V, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.618
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE SpikingGPF
    model_plain: GraphMAE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0509
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGA
    model_plain: TAGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.616
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL SpikingGPF
    model_plain: GraphCL SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6152
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0667
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE SpikingGPF
    model_plain: SimGRACE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0417
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL GPF
    model_plain: GraphCL GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0549
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAGA-rw
    model_plain: TAGA-rw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.599
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF
    model_plain: GraphMAE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5947
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred GPF-plus
    model_plain: EdgePred GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5929
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0562
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF-plus
    model_plain: SimGRACE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5897
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0431
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE GPF-plus
    model_plain: GraphMAE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5879
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.037
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OpenGraph
    model_plain: OpenGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.03251'
    title: 'RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/RiemannGraph/RiemannGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.584
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGE
    model_plain: ARGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5822
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred GPF
    model_plain: EdgePred GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5822
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE Fine-Tuning
    model_plain: GraphMAE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5803
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0516
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE GPF
    model_plain: SimGRACE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5796
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0507
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred Fine-Tuning
    model_plain: EdgePred Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5786
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0556
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL GPF-plus
    model_plain: GraphCL GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5776
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G2P2
    model_plain: G2P2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5732
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1099
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL Fine-Tuning
    model_plain: GraphCL Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5642
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0384
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graver
    model_plain: Graver
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.553
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0303
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE Fine-Tuning
    model_plain: SimGRACE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5524
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0492
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAL CausalGAT
    model_plain: CAL CausalGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.55
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Non-transfer-GCN
    model_plain: Non-transfer-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5487
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE All-in-One
    model_plain: SimGRACE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5311
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0428
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5246
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE All-in-One
    model_plain: GraphMAE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5237
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0624
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5218
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EdgePred All-in-One
    model_plain: EdgePred All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5216
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0645
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5192
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL All-in-One
    model_plain: GraphCL All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5177
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0617
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5143
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0398
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProNoG
    model_plain: ProNoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5135
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MDGPT
    model_plain: MDGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5103
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0332
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0888
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node features (SVM)
    model_plain: Node features (SVM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.08414'
    title: 'Scattering GCN: Overcoming Oversmoothness in Graph Convolutional Networks'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: http://github.com/dms-net/scatteringGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.499
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.491
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0542
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4855
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0601
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4823
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PLM
    model_plain: PLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.475
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3D InfoGraph
    model_plain: 3D InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.08092'
    title: 'GCoT: Chain-of-Thought Prompt Learning for Graphs'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4746
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1219
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNGR
    model_plain: DNGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4535
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4475
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0467
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4433
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0488
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4389
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4388
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.438
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4294
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.425
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4197
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0548
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: E5
    model_plain: E5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4189
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0483
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sent-BERT
    model_plain: Sent-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4171
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCC
    model_plain: GCC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4166
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0327
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN (bb.)
    model_plain: GCN (bb.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSSL
    model_plain: DSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.05592'
    title: 'Graver: Generative Graph Vocabularies for Robust Graph Foundation Models
      Fine-tuning'
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: https://github.com/RingBDStack/GRAVER
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0629
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RolX
    model_plain: RolX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3985
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0233
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Spectral
    model_plain: Spectral
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.01210'
    title: Attributed Graph Clustering via Adaptive Graph Convolution
    date: Jun 2019
    date_iso: 2019-06
    date_display: Jun 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3974
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (512)
    model_plain: FastGCN (512)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.393
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.092
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (64)
    model_plain: FastGCN (64)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.385
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3787
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.368
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3656
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GOttack
    model_plain: GOttack
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3587
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0342
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FGA
    model_plain: FGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.356
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0314
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMoN
    model_plain: DMoN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.351
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3479
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGA
    model_plain: SGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3427
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0427
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGD
    model_plain: PGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3413
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0366
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NETTACK
    model_plain: NETTACK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3373
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0337
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.335
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PR-BCD (NA)
    model_plain: PR-BCD (NA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.296
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0304
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2818
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.11235'
    title: 'ZeroG: Investigating Cross-dataset Zero-shot Transferability in Graphs'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/NineAbyss/ZeroG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.2733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.251
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphWave
    model_plain: GraphWave
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2096
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0235
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: L1D-RND
    model_plain: L1D-RND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1093
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0301
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.0756
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.895
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AMEN
    model_plain: AMEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Radar
    model_plain: Radar
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6233
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANOMALOUS
    model_plain: ANOMALOUS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7316
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DOMINANT
    model_plain: DOMINANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6962
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CoLA
    model_plain: CoLA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.00113'
    title: Anomaly Detection on Attributed Networks via Contrastive Self-Supervised
      Learning
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.9512
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGE
    model_plain: ARGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.837
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSGC
    model_plain: DSGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.844
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.857
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIC
    model_plain: GIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.859
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.864
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FeatWalk
    model_plain: FeatWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.843
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAN
    model_plain: CAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.841
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CONN
    model_plain: CONN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.866
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7558
    - null
    - 0.7837
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7606
    - null
    - 0.7884
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7566
    - null
    - 0.784
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7585
    - null
    - 0.7853
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7601
    - null
    - 0.7855
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Simple-HGN
    model_plain: Simple-HGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7617
    - null
    - 0.7888
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HINormer
    model_plain: HINormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.766
    - null
    - 0.7935
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7644
    - null
    - 0.7953
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S2GCN
    model_plain: S2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7667
    - null
    - 0.7956
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GBP
    model_plain: GBP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7913
    - null
    - 0.8056
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAMLP
    model_plain: GAMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7615
    - null
    - 0.7911
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7646
    - null
    - 0.7924
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LazyGNN
    model_plain: LazyGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7703
    - null
    - 0.7992
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NARS
    model_plain: NARS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7582
    - null
    - 0.7882
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SeHGNN
    model_plain: SeHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.777
    - null
    - 0.7971
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RpHGNN
    model_plain: RpHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7932
    - null
    - 0.8058
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TOP
    model_plain: TOP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7935
    - null
    - 0.806
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ScaleGNN_b
    model_plain: ScaleGNN_b
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.15920'
    title: 'ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order
      Neighboring Feature Fusion'
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/lx970414/ScaleGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8067
    - null
    - 0.8211
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SC
    model_plain: SC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.183
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.002
  - model: MSC
    model_plain: MSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.002
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.098
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
  - model: MinCutPool
    model_plain: MinCutPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.214
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.066
  - model: HP-1
    model_plain: HP-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.23
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.071
  - model: HP-2
    model_plain: HP-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.215
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.073
  - model: HoscPool
    model_plain: HoscPool
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.26
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.054
  - model: MF
    model_plain: MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9306
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.982
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9887
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9777
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BUDDY
    model_plain: BUDDY
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.982
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Neo-GNN
    model_plain: Neo-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9871
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NCN
    model_plain: NCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9898
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NCNC
    model_plain: NCNC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9914
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NBFNet
    model_plain: NBFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9834
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PEG
    model_plain: PEG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.24062'
    title: Energy-Balanced Hyperspherical Graph Representation Learning via Structural
      Binding and Entropic Dispersion
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/chenrui0127/HyperGRL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Katz Index
    model_plain: Katz Index
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.856
    - null
    - null
    - 0.757
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Personalized PageRank
    model_plain: Personalized PageRank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.86
    - null
    - null
    - 0.763
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimRank
    model_plain: SimRank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.829
    - null
    - null
    - 0.743
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.841
    - null
    - null
    - 0.844
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINE
    model_plain: LINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.914
    - null
    - null
    - 0.891
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.947
    - null
    - null
    - 0.944
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-VGAE
    model_plain: S-VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.96
    - null
    - null
    - 0.96
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEAL
    model_plain: SEAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.979
    - null
    - null
    - 0.978
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TLC-GNN
    model_plain: TLC-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.968
    - null
    - null
    - 0.97
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NBFNet
    model_plain: NBFNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.982
    - null
    - null
    - 0.983
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: KnowFormer
    model_plain: KnowFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.12865'
    title: arXiv:2409.12865
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/jnanliu/KnowFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.988
    - null
    - null
    - 0.987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.03
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.02
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
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.23
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.04
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
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.18
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.04
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
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.21
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.03
  - model: ORC-Pool
    model_plain: ORC-Pool
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
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.24
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.04
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.1802
    - null
    - 0.2046
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0198
    - null
    - 0.0239
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.1543
    - null
    - 0.2488
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0241
    - null
    - 0.0227
    - null
    - null
  - model: DisenHAN
    model_plain: DisenHAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4171
    - null
    - 0.5093
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0443
    - null
    - 0.0425
    - null
    - null
  - model: HetGNN
    model_plain: HetGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2186
    - null
    - 0.2993
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0321
    - null
    - 0.0351
    - null
    - null
  - model: HGT
    model_plain: HGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.475
    - null
    - 0.5186
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0634
    - null
    - 0.0485
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0984
    - null
    - 0.2116
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0169
    - null
    - 0.02
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2489
    - null
    - 0.3465
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0847
    - null
    - 0.0571
    - null
    - null
  - model: SimpleHGN
    model_plain: SimpleHGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4293
    - null
    - 0.4926
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0401
    - null
    - 0.0332
    - null
    - null
  - model: space4HGNN
    model_plain: space4HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4553
    - null
    - 0.4976
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0464
    - null
    - 0.0392
    - null
    - null
  - model: SlotGAT
    model_plain: SlotGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.01927'
    title: arXiv:2405.01927
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4779
    - null
    - 0.5325
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0356
    - null
    - 0.034
    - null
    - null
  - model: wvRN-IC
    model_plain: wvRN-IC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.826
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: wvRN-RL
    model_plain: wvRN-RL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.824
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SL-LR
    model_plain: SL-LR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.882
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HWN-noRel
    model_plain: HWN-noRel
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.879
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-FNN
    model_plain: CLN-FNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.894
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-HWN-full
    model_plain: CLN-HWN-full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.898
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-HWN-mini
    model_plain: CLN-HWN-mini
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.898
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.79
    std: 0.017
    model: CNNs
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: '2013-12-21'
  - value: 0.797
    std: 0.003
    model: N-GCN_a
    arxiv_id: '1802.08888'
    title: 'N-GCN: Multi-scale Graph Convolution for Semi-supervised Node Classification'
    date: 2018-02
  - value: 0.8
    std: null
    model: DGCNN
    arxiv_id: '1812.04202'
    title: 'Deep Learning on Graphs: A Survey'
    date: 2018-12
  - value: 0.8937
    std: 0.0041
    model: GFL-mean
    arxiv_id: '1910.03053'
    title: Graph Few-shot Learning via Knowledge Transfer
    date: 2019-10
  - value: 0.921
    std: 0.022
    model: Policy-GNN
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: 2020-06
  - value: 0.9377
    std: null
    model: GraphSAGE
    arxiv_id: '2106.09078'
    title: 'Probing GNN Explainers: A Rigorous Theoretical and Empirical Analysis
      of GNN Explanation Methods'
    date: '2021-06-16'
  - value: 0.9462
    std: 0.0013
    model: Flan-T5-large
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: 2023-08
  - value: 0.9475
    std: 0.0036
    model: GCN + LLM-based A-D
    arxiv_id: '2311.14324'
    title: Large Language Models as Topological Structure Enhancers for Text-Attributed
      Graphs
    date: 2023-11
  - value: 0.9517
    std: null
    model: SAGN
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: 2024-02
  - value: 0.96
    std: 0.001
    model: S-VAE/VGAE
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: 2024-07
  - value: 0.986
    std: null
    model: AIO
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: 2025-10
---

