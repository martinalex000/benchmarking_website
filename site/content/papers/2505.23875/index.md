---
title: A Benchmark Dataset for Graph Regression with Homogeneous and Multi‑Relational
  Variants
arxiv_id: '2505.23875'
source_url: ''
authors: []
published_date: May 2025
published_date_iso: 2025-05
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
paper_type: method
proposed_models:
- PNA
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.11
    std: 0.0
    paper_value: 0.11
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.11
    sort_std: 0.0
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.14
    std: 0.01
    paper_value: 0.14
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 2
    sort_value: 0.14
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.14
    std: 0.01
    paper_value: 0.14
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 1
    sort_value: 0.14
    sort_std: 0.01
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.14
    std: 0.01
    paper_value: 0.14
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 16
    sort_value: 0.14
    sort_std: 0.01
    is_best: false
  - model: CodeBERT
    model_key: codebert
    model_plain: CodeBERT
    value: 0.15
    std: 0.08
    paper_value: 0.15
    paper_std: 0.08
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.15
    sort_std: 0.08
    is_best: true
  - model: Code2Vec
    model_key: code2vec
    model_plain: Code2Vec
    value: 0.15
    std: 0.01
    paper_value: 0.15
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.15
    sort_std: 0.01
    is_best: false
  - model: Cheb
    model_key: cheb
    model_plain: Cheb
    value: 0.15
    std: 0.01
    paper_value: 0.15
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.15
    sort_std: 0.01
    is_best: false
  - model: HeteroGAT
    model_key: heterogat
    model_plain: HeteroGAT
    value: 0.18
    std: 0.02
    paper_value: 0.18
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.18
    sort_std: 0.02
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
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
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.279
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.09008'
    title: City-Networks
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.279
    sort_std: 0.001
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
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
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.282
    sort_std: 0.03
    is_best: false
  - model: HeteroSage
    model_key: heterosage
    model_plain: HeteroSage
    value: 0.58
    std: 0.31
    paper_value: 0.58
    paper_std: 0.31
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: null
    sort_value: 0.58
    sort_std: 0.31
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

