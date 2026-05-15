---
title: A Benchmark Dataset for Graph Regression with Homogeneous and Multi‑Relational
  Variants
arxiv_id: '2505.23875'
authors: []
published_date: May 2025
abstract: Graph‑level regression underpins many real‑world applications, yet public
  benchmarks remain heavily skewed toward molecular graphs and citation networks.
  This limited diversity hinders progress on models that must generalize across both
  homogeneous and heterogeneous graph structures. We introduce RelSC, a new graph‑regression
  dataset built from program graphs that combine syntactic and semantic information
  extracted from source code. Each graph is labelled with the execution‑time cost
  of the corresponding program, providing a continuous target variable that differs
  markedly from those found in existing benchmarks. RelSC is released in two complementary
  variants. supplies rich node features under a single (homogeneous) edge type, while
  preserves the original multi‑relational structure, connecting nodes through multiple
  edge types that encode distinct semantic relationships. Together, these variants
  let researchers probe how representation choice influences model behaviour. We evaluate
  a diverse set of graph neural network architectures on both variants of RelSC. The
  results reveal consistent performance differences between the homogeneous and multi-relational
  settings, emphasising the importance of structural representation. These findings
  demonstrate RelSC's value as a challenging and versatile benchmark for advancing
  graph regression methods.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- PNA
mrr: 0.0
results:
- &id001
  dataset: D&D
  rows:
  - model: PNA
    value: 0.11
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GCN
    value: 0.14
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GIN
    value: 0.14
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: false
  - model: GraphSAGE
    value: 0.14
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: CodeBERT
    value: 0.15
    std: 0.08
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: Code2Vec
    value: 0.15
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Cheb
    value: 0.15
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: HeteroGAT
    value: 0.18
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: MLP
    value: 0.279
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.09008'
    title: 'Towards Quantifying Long-Range Interactions in Graph Machine Learning:
      A Large Graph Dataset and a Measurement 0.8em'
    date: Mar 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: GATv2
    value: 0.282
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: HeteroSage
    value: 0.58
    std: 0.31
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
single_proposed_model: PNA
main_figure: /figures/2505.23875/main_figure.png
---

