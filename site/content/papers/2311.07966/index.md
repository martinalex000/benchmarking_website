---
title: Higher-Order Expander Graph Propagation
arxiv_id: '2311.07966'
authors: []
published_date: Nov 2023
abstract: Graph neural networks operate on graph-structured data via exchanging messages
  along edges. One limitation of this message passing paradigm is the over-squashing
  problem. Over-squashing occurs when messages from a node's expanded receptive field
  are compressed into fixed-size vectors, potentially causing information loss. To
  address this issue, recent works have explored using expander graphs, which are
  highly-connected sparse graphs with low diameters, to perform message passing. However,
  current methods on expander graph propagation only consider pair-wise interactions,
  ignoring higher-order structures in complex data. To explore the benefits of capturing
  these higher-order correlations while still leveraging expander graphs, we introduce
  higher-order expander graph propagation. We propose two methods for constructing
  bipartite expanders and evaluate their performance on both synthetic and real-world
  datasets.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GIN + 3-Regular Bipartite Expander + Learned Features
mrr: 0.0455
results:
- &id002
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
    value: 0.9494
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: CodeT5-base + GFSA
    value: 0.9492
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: CodeT5-small
    value: 0.9436
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 60.0
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GIN + 3-Regular Bipartite Expander + Learned Features
    value: 0.1519
    std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: EGP
    value: 0.1497
    std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Deac et al. 2022
    global_rank: 23
    is_best: false
  - model: Plain GIN
    value: 0.1495
    std: 0.0023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    global_rank: 24
    is_best: false
  - model: GIN + 3-Regular Bipartite Expander + Summation
    value: 0.1254
    std: 0.0029
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 25
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GCN
    value: 0.9681
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: EGP
    value: 0.7934
    std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deac et al. 2022
    global_rank: 43
    is_best: false
  - model: k=3 Ramanujan Expander
    value: 0.7848
    std: 0.0135
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: GIN + PM_at (Summation-MLP)
    value: 0.7614
    std: 0.0056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 105
    is_best: false
  - model: Plain GIN
    value: 0.7558
    std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu et al. 2020
    global_rank: 113
    is_best: false
  - model: GIN + PM (Summation)
    value: 0.7538
    std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 114
    is_best: false
  - model: GIN + PM_sp (Summation-MLP)
    value: 0.7524
    std: 0.0206
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 117
    is_best: false
  - model: GIN + RM (Learn-Features)
    value: 0.7511
    std: 0.0133
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 121
    is_best: false
  - model: GIN + PM (Learnt)
    value: 0.7503
    std: 0.0201
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 122
    is_best: false
  - model: GIN + RM (Masking)
    value: 0.7439
    std: 0.0219
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 126
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
single_proposed_model: GIN + 3-Regular Bipartite Expander + Learned Features
main_figure: /figures/2311.07966/main_figure.png
---

