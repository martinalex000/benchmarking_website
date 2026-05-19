---
title: Code
slug: code
benchmark: OGB
task_type: graph_classification
description: Code AST-level method name prediction (ogbg-code2). 143k Python snippets.
primary_metric: F1
higher_is_better: true
pyg_url: https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-code2
stats: null
result_count: 27
best_model:
  model: CodeT5-small + GFSA
  value: 0.9494
  metric: F1
variants:
- slug: standard-split
  name: Standard split
  notes: Project-based split.
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: CodeT5-small + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.9494
    metric_stds:
    - null
  - model: CodeT5-base + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9492
    metric_stds:
    - null
  - model: CodeT5-small
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 60.0
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9436
    metric_stds:
    - null
  - model: CodeT5-base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9431
    metric_stds:
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
    - 0.1957
    metric_stds:
    - 0.0025
  - model: LPE
    is_baseline: true
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
    - 0.1948
    metric_stds:
    - 0.0021
  - model: RRWP
    is_baseline: true
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
    - 0.1942
    metric_stds:
    - 0.001
  - model: RWSE
    is_baseline: true
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
    - 0.19390000000000002
    metric_stds:
    - 0.004699999999999999
  - model: K-Subtree SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.1937
    metric_stds:
    - 0.0028
  - model: SAT
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
    - 0.1937
    metric_stds:
    - 0.0028
  - model: SPE
    is_baseline: true
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
    - 0.1935
    metric_stds:
    - 0.0021
  - model: NoPE
    is_baseline: true
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
    - 0.19269999999999998
    metric_stds:
    - 0.002
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.1915
    metric_stds:
    - 0.002
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
    - 0.1896
    metric_stds:
    - 0.0024
  - model: GraphGPS
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
    - 0.1894
    metric_stds:
    - 0.0024
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
    - 0.1894
    metric_stds:
    - 0.0024
  - model: GraphTrans (GCN-Virtual)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.183
    metric_stds:
    - 0.0024
  - model: GraphTrans
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
    - 0.183
    metric_stds:
    - 0.0024
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
    - 0.1803
    metric_stds:
    - 0.0019
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
    - 0.1787
    metric_stds:
    - 0.0026
  - model: GT
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
    - 0.167
    metric_stds:
    - 0.0015
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
    - 0.1595
    metric_stds:
    - 0.0018
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
    - 0.1581
    metric_stds:
    - 0.0026
  - model: GIN + 3-Regular Bipartite Expander + Learned Features
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1519
    metric_stds:
    - 0.002
  - model: EGP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1497
    metric_stds:
    - 0.0015
  - model: Plain GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1495
    metric_stds:
    - 0.0023
  - model: GIN + 3-Regular Bipartite Expander + Summation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1254
    metric_stds:
    - 0.0029
  milestones:
  - value: 0.1519
    std: 0.002
    model: GIN + 3-Regular Bipartite Expander + Learned Features
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: 2023-11
  - value: 0.9494
    std: null
    model: CodeT5-small + GFSA
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: 2023-12
---

