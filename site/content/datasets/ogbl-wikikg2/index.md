---
title: ogbl-wikikg2
slug: ogbl-wikikg2
benchmark: OGB
task_type: link_prediction
description: Knowledge graph link prediction on Wikidata (2.5M entities, 535 relations).
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats: null
result_count: 35
best_model:
  model: DyGFormer
  value: 0.7983
  metric: MRR
variants:
- slug: standard-split
  name: Standard split
  notes: 'Metric: MRR.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  metrics:
  - MRR
  rows:
  - model: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7983
    metric_stds:
    - 0.0042
  - model: TCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7811
    metric_stds:
    - 0.002
  - model: CAWN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.0
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7304
    metric_stds:
    - 0.006
  - model: TNCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.711
    metric_stds:
    - 0.007
  - model: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6893
    metric_stds:
    - 0.0053
  - model: CTAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6676
    metric_stds:
    - 0.0074
  - model: TGTalker (nbr = 2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.656
    metric_stds:
    - null
  - model: Qwen3-8B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.651
    metric_stds:
    - null
  - model: TGTalker (All components)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.649
    metric_stds:
    - null
  - model: Qwen2.5-7B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.648
    metric_stds:
    - null
  - model: TGTalker (w/o Background Set)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.648
    metric_stds:
    - null
  - model: TGTalker (w/o In Context Learning)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.645
    metric_stds:
    - null
  - model: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6305
    metric_stds:
    - 0.0169
  - model: CTAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.03783'
    title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
      An Information-Flow Centric Review'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.611
    metric_stds:
    - 0.011
  - model: Qwen3-1.7B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.607
    metric_stds:
    - null
  - model: Mistral-7B-v0.3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.604
    metric_stds:
    - null
  - model: Llama3-8B
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.604
    metric_stds:
    - null
  - model: EdgeBank_tw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    metric_stds:
    - null
  - model: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5994
    metric_stds:
    - 0.0163
  - model: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5975
    metric_stds:
    - 0.0039
  - model: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.03783'
    title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
      An Information-Flow Centric Review'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.577
    metric_stds:
    - 0.015
  - model: EdgeBank
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.525
    metric_stds:
    - null
  - model: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5191
    metric_stds:
    - 0.0195
  - model: EdgeBank_inf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.495
    metric_stds:
    - null
  - model: HTGN (UTG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.464
    metric_stds:
    - 0.005
  - model: GPT-4.1-mini
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.425
    metric_stds:
    - null
  - model: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.396
    metric_stds:
    - 0.06
  - model: GCLSTM (UTG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.374
    metric_stds:
    - 0.01
  - model: GCN (UTG)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.336
    metric_stds:
    - 0.009
  - model: TGTalker (w/o Temporal Neighbours)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.322
    metric_stds:
    - null
  - model: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.03783'
    title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
      An Information-Flow Centric Review'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.282
    metric_stds:
    - 0.022
  - model: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.03783'
    title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
      An Information-Flow Centric Review'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.263
    metric_stds:
    - 0.005
  - model: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.03783'
    title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
      An Information-Flow Centric Review'
    date: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.261
    metric_stds:
    - 0.123
  - model: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.118
    metric_stds:
    - 0.002
  - model: TGTalker (with no components)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.008
    metric_stds:
    - null
  milestones:
  - value: 0.7983
    std: 0.0042
    model: DyGFormer
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
---

