---
title: ogbn-products
slug: ogbn-products
benchmark: OGB
task_type: node_classification
description: Node classification on Amazon product co-purchase graph (47 categories).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBNodePropPredDataset.html
stats: null
result_count: 43
best_model:
  model: SAGE
  value: 0.9334
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: 'Sales-rank split. Metric: Accuracy.'
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9334
    metric_stds:
    - 0.0006
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9115
    metric_stds:
    - 0.0004
  - model: GLEM-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8736
    metric_stds:
    - 0.0007
  - model: GLEM-LM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8483
    metric_stds:
    - 0.0004
  - model: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8262
    metric_stds:
    - 0.0039
  - model: GCN/SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8251
    metric_stds:
    - 0.0053
  - model: QGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    metric_stds:
    - 0.0231
  - model: GOAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    metric_stds:
    - 0.0043
  - model: GOAT-local-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8117
    metric_stds:
    - 0.0012
  - model: S$^2$GAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    metric_stds:
    - 0.007
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8063
    metric_stds:
    - 0.007
  - model: GOAT-full-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7988
    metric_stds:
    - 0.002
  - model: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7982
    metric_stds:
    - 0.0007
  - model: LargeGT-full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7981
    metric_stds:
    - 0.0025
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    metric_stds:
    - 0.003
  - model: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7976
    metric_stds:
    - 0.0059
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.791
    metric_stds:
    - 0.0002
  - model: Fine-tuned Deberta-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7908
    metric_stds:
    - 0.0023
  - model: LargeGT-local
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7895
    metric_stds:
    - 0.008
  - model: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7868
    metric_stds:
    - 0.014
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7859
    metric_stds:
    - 0.0002
  - model: LLM Few-shot
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7775
    metric_stds:
    - 0.0106
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7758
    metric_stds:
    - 0.0047
  - model: e5-large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7749
    metric_stds:
    - 0.0029
  - model: GAT-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7738
    metric_stds:
    - 0.0059
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7662
    metric_stds:
    - 0.0093
  - model: text-ada-embedding-002
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7642
    metric_stds:
    - 0.0031
  - model: LLM Few-Shot with 2-hop info
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.76
    metric_stds:
    - 0.0282
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7564
    metric_stds:
    - 0.0021
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7528
    metric_stds:
    - 0.0004
  - model: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7527
    metric_stds:
    - 0.0005
  - model: LLM Zero-Shot with 2-hop info
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7525
    metric_stds:
    - 0.0353
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7355
    metric_stds:
    - 0.0021
  - model: LLM Few-shot with COT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7325
    metric_stds:
    - 0.0177
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7293
    metric_stds:
    - 0.0013
  - model: Sentence-BERT(MiniLM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7273
    metric_stds:
    - 0.0034
  - model: LLM Zero-shot with COT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7125
    metric_stds:
    - 0.0106
  - model: LLM Zero-shot
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7075
    metric_stds:
    - 0.0248
  - model: GOAT-global-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7028
    metric_stds:
    - 0.0195
  - model: Word2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6927
    metric_stds:
    - 0.0054
  - model: TF-IDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6442
    metric_stds:
    - 0.0018
  - model: GT-sparse-δ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6076
    metric_stds:
    - 0.0
  - model: Deberta-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0718
    metric_stds:
    - 0.0109
  milestones:
  - value: 0.8736
    std: 0.0007
    model: GLEM-GNN
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: 2023-07
  - value: 0.9334
    std: 0.0006
    model: SAGE
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: 2024-10
---

