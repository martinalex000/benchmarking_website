---
title: Size Transferability of Graph Transformers with Convolutional Positional Encodings
arxiv_id: '2602.15239'
source_url: ''
authors: []
published_date: Feb 2026
published_date_iso: 2026-02
abstract: Transformers have achieved remarkable success across domains, motivating
  the rise of Graph Transformers (GTs) as attention-based architectures for graph-structured
  data. A key design choice in GTs is the use of Graph Neural Network (GNN)-based
  positional encodings to incorporate structural information. In this work, we study
  GTs through the lens of manifold limit models for graph sequences and establish
  a theoretical connection between GTs with GNN positional encodings and Manifold
  Neural Networks (MNNs). Building on transferability results for GNNs under manifold
  convergence, we show that GTs inherit transferability guarantees from their positional
  encodings. In particular, GTs trained on small graphs provably generalize to larger
  graphs under mild assumptions. We complement our theory with extensive experiments
  on standard graph benchmarks, demonstrating that GTs exhibit scalable behavior on
  par with GNNs. To further show the efficiency in a real-world scenario, we implement
  GTs for shortest path distance estimation over terrains to better illustrate the
  efficiency of the transferable GTs. Our results provide new insights into the understanding
  of GTs and suggest practical directions for efficient training of GTs in large-scale
  settings.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GT + Mask + RPEARL
mrr: 0.0667
adjusted_mrr: 0.0222
mrr_dataset_count: 1
benchmark_categories:
- LINKX Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id001
  dataset: snap-patents
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7472
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7472
    sort_std: 0.0005
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7395
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7395
    sort_std: 0.0005
    is_best: false
  - model: LargeGT-full
    model_key: largegt-full
    model_plain: LargeGT-full
    value: 0.7021
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7021
    sort_std: 0.0012
    is_best: false
  - model: GT + Mask + RPEARL
    model_key: gt + mask + rpearl
    model_plain: GT + Mask + RPEARL
    value: 0.46549999999999997
    std: null
    paper_value: 0.46549999999999997
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 15
    true_value: 0.46549999999999997
    true_std: null
    value_gap_source_arxiv: '2602.15239'
    value_gap_source_title: Size Transferability of Graph Transformers with Convolutional
      Positional Encodings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.46549999999999997
    sort_std: null
    is_best: false
  - model: GT + Mask
    model_key: gt + mask
    model_plain: GT + Mask
    value: 0.3969
    std: null
    paper_value: 0.3969
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 20
    true_value: 0.3969
    true_std: null
    value_gap_source_arxiv: '2602.15239'
    value_gap_source_title: Size Transferability of Graph Transformers with Convolutional
      Positional Encodings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3969
    sort_std: null
    is_best: false
  - model: GT + RPEARL
    model_key: gt + rpearl
    model_plain: GT + RPEARL
    value: 0.34630000000000005
    std: null
    paper_value: 0.34630000000000005
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 21
    true_value: 0.34630000000000005
    true_std: null
    value_gap_source_arxiv: '2602.15239'
    value_gap_source_title: Size Transferability of Graph Transformers with Convolutional
      Positional Encodings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34630000000000005
    sort_std: null
    is_best: false
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.31329999999999997
    std: null
    paper_value: 0.31329999999999997
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 23
    true_value: 0.31329999999999997
    true_std: null
    value_gap_source_arxiv: '2602.15239'
    value_gap_source_title: Size Transferability of Graph Transformers with Convolutional
      Positional Encodings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31329999999999997
    sort_std: null
    is_best: false
  - model: GT + Mask + RE
    model_key: gt + mask + re
    model_plain: GT + Mask + RE
    value: 0.31010000000000004
    std: null
    paper_value: 0.31010000000000004
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 24
    true_value: 0.31010000000000004
    true_std: null
    value_gap_source_arxiv: '2602.15239'
    value_gap_source_title: Size Transferability of Graph Transformers with Convolutional
      Positional Encodings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31010000000000004
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: LINKX Benchmarks
  datasets:
  - *id001
single_proposed_model: GT + Mask + RPEARL
main_figure: /figures/2602.15239/main_figure.png
---

