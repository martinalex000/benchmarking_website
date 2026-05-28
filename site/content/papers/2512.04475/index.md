---
title: GraphBench
arxiv_id: '2512.04475'
source_url: ''
authors: []
published_date: Dec 2025
published_date_iso: 2025-12
abstract: Machine learning on graphs has recently achieved impressive progress in
  various domains, including molecular property prediction and chip design. However,
  benchmarking practices remain fragmented, often relying on narrow, task-specific
  datasets and inconsistent evaluation protocols, which hampers reproducibility and
  broader progress. To address this, we introduce, a comprehensive benchmarking suite
  that spans diverse domains and prediction tasks, including node-level, edge-level,
  graph-level, and generative settings. provides standardized evaluation protocols---with
  consistent dataset splits and performance metrics that account for out-of-distribution
  generalization---as well as a unified hyperparameter tuning framework. Additionally,
  we benchmark using message-passing neural networks and graph transformer models,
  providing principled baselines and establishing a reference performance. See www.graphbench.io
  for further details.
codebase_url: https://github.com/graphbench/package
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GNN
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- GraphBench
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id006
  dataset: BA graph
  rows:
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.292
    std: 0.041
    paper_value: 0.292
    paper_std: 0.041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.292
    true_std: 0.041
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.292
    sort_std: 0.041
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.03481
    std: 0.034460000000000005
    paper_value: 0.03481
    paper_std: 0.034460000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.03481
    true_std: 0.034460000000000005
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.03481
    sort_std: 0.034460000000000005
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.02825
    std: 0.00949
    paper_value: 0.02825
    paper_std: 0.00949
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.02825
    true_std: 0.00949
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.02825
    sort_std: 0.00949
    is_best: false
  - model: DeepSets
    model_key: deepsets
    model_plain: DeepSets
    value: 0.023039999999999998
    std: 0.00262
    paper_value: 0.023039999999999998
    paper_std: 0.00262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 4
    true_value: 0.023039999999999998
    true_std: 0.00262
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.023039999999999998
    sort_std: 0.00262
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: BlueSky
  rows:
  - model: GNN
    model_key: gnn
    model_plain: GNN
    value: 0.768
    std: 0.002
    paper_value: 0.768
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.768
    true_std: 0.002
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.002
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.784
    std: 0.001
    paper_value: 0.784
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.784
    true_std: 0.001
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.001
    is_best: false
  - model: DeepSets
    model_key: deepsets
    model_plain: DeepSets
    value: 0.81
    std: 0.005
    paper_value: 0.81
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.81
    true_std: 0.005
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: Bridges
  rows:
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9921
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9921
    sort_std: 0.0009
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9831
    std: 0.0184
    paper_value: 0.9831
    paper_std: 0.0184
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.9831
    true_std: 0.0184
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9831
    sort_std: 0.0184
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9622
    std: 0.0077
    paper_value: 0.9622
    paper_std: 0.0077
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.9831
    true_std: 0.0184
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02089999999999992
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9831
    sort_std: 0.0184
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.968
    std: 0.0178
    paper_value: 0.968
    paper_std: 0.0178
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.9831
    true_std: 0.0184
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.015100000000000002
    value_note: global 0.9831 within std
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9831
    sort_std: 0.0184
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9269
    std: 0.0103
    paper_value: 0.9269
    paper_std: 0.0103
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.9269
    true_std: 0.0103
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9269
    sort_std: 0.0103
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8762
    std: 0.0258
    paper_value: 0.8762
    paper_std: 0.0258
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.9269
    true_std: 0.0103
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05069999999999997
    value_note: ''
    paper_rank: 4
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9269
    sort_std: 0.0103
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8897
    std: 0.0304
    paper_value: 0.8897
    paper_std: 0.0304
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.9269
    true_std: 0.0103
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0371999999999999
    value_note: ''
    paper_rank: 4
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9269
    sort_std: 0.0103
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.9176000000000001
    std: 0.0766
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9176000000000001
    sort_std: 0.0766
    is_best: true
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.8734000000000001
    std: 0.0397
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8734000000000001
    sort_std: 0.0397
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GT
    model_key: gt
    model_plain: GT
    metric_values:
    - 0.6743
    - 6.4833
    metric_stds:
    - 0.0038
    - 0.0869
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6743
    sort_std: 0.0038
    true_value: null
    true_std: null
    paper_value: 0.6743
    paper_std: 0.0038
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.6595
    - 9.5061
    metric_stds:
    - 0.0164
    - 0.1265
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6595
    sort_std: 0.0164
    true_value: null
    true_std: null
    paper_value: 0.6595
    paper_std: 0.0164
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 38
  metrics:
  - F1
  - MAE
  primary_metric: Accuracy
  higher_is_better: true
- &id012
  dataset: ER graph
  rows:
  - model: DeepSets
    model_key: deepsets
    model_plain: DeepSets
    value: 0.756
    std: 0.711
    paper_value: 0.756
    paper_std: 0.711
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.756
    true_std: 0.711
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.711
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.751
    std: 0.767
    paper_value: 0.751
    paper_std: 0.767
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.751
    true_std: 0.767
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.767
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.234
    std: 0.191
    paper_value: 0.234
    paper_std: 0.191
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.234
    true_std: 0.191
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.234
    sort_std: 0.191
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.06486
    std: 0.08101000000000001
    paper_value: 0.06486
    paper_std: 0.08101000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 4
    true_value: 0.06486
    true_std: 0.08101000000000001
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.06486
    sort_std: 0.08101000000000001
    is_best: true
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Electronic Circuits
  rows:
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.07
    std: 0.03
    paper_value: 0.07
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.07
    true_std: 0.03
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.07
    sort_std: 0.03
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.09
    std: 0.06
    paper_value: 0.09
    paper_std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.09
    true_std: 0.06
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.06
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.11
    std: 0.05
    paper_value: 0.11
    paper_std: 0.05
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.11
    true_std: 0.05
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.11
    sort_std: 0.05
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.13
    std: 0.07
    paper_value: 0.13
    paper_std: 0.07
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 4
    true_value: 0.13
    true_std: 0.07
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.13
    sort_std: 0.07
    is_best: true
  metric: MAE
  higher_is_better: false
- &id003
  dataset: Flow
  rows:
  - model: RRWP
    model_key: rrwp
    model_plain: RRWP
    value: 1.45
    std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.45
    sort_std: 0.06
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 1.49
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.49
    sort_std: 0.02
    is_best: true
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 1.73
    std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.73
    sort_std: 0.09
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 3.4387
    std: 0.0631
    paper_value: 3.4387
    paper_std: 0.0631
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.596
    std: 0.1707
    paper_value: 9.596
    paper_std: 0.1707
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 6.1573
    value_note: ''
    paper_rank: 9
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 9.5061
    std: 0.1265
    paper_value: 9.5061
    paper_std: 0.1265
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 3.4387
    true_std: 0.0631
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 6.0674
    value_note: ''
    paper_rank: 9
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 3.4387
    sort_std: 0.0631
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 4.2737
    std: 0.0646
    paper_value: 4.2737
    paper_std: 0.0646
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 9
    true_value: 4.2737
    true_std: 0.0646
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.2737
    sort_std: 0.0646
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 6.3786
    std: 0.4262
    paper_value: 6.3786
    paper_std: 0.4262
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 9
    true_value: 4.2737
    true_std: 0.0646
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.1048999999999998
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.2737
    sort_std: 0.0646
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 6.4833
    std: 0.0869
    paper_value: 6.4833
    paper_std: 0.0869
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 9
    true_value: 4.2737
    true_std: 0.0646
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 2.2096
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.2737
    sort_std: 0.0646
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: MST
  rows:
  - model: GDT (RRWP)
    model_key: gdt (rrwp)
    model_plain: GDT (RRWP)
    value: 0.9604
    std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9604
    sort_std: 0.0091
    is_best: true
  - model: GT (no PE)
    model_key: gt (no pe)
    model_plain: GT (no PE)
    value: 0.9329000000000001
    std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9329000000000001
    sort_std: 0.0088
    is_best: false
  - model: GDT (RWSE)
    model_key: gdt (rwse)
    model_plain: GDT (RWSE)
    value: 0.9326000000000001
    std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9326000000000001
    sort_std: 0.0045000000000000005
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8566
    std: 0.0068
    paper_value: 0.8566
    paper_std: 0.0068
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 6
    true_value: 0.8566
    true_std: 0.0068
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8566
    sort_std: 0.0068
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8504
    std: 0.0148
    paper_value: 0.8504
    paper_std: 0.0148
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 6
    true_value: 0.8566
    true_std: 0.0068
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006199999999999983
    value_note: global 0.8566 within std
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8566
    sort_std: 0.0068
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8421
    std: 0.0115
    paper_value: 0.8421
    paper_std: 0.0115
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 6
    true_value: 0.8566
    true_std: 0.0068
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014500000000000068
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8566
    sort_std: 0.0068
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6906
    std: 0.1655
    paper_value: 0.6906
    paper_std: 0.1655
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 0.7288
    true_std: 0.0894
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03820000000000001
    value_note: global 0.7288 within std
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7288
    sort_std: 0.0894
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7288
    std: 0.0894
    paper_value: 0.7288
    paper_std: 0.0894
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 0.7288
    true_std: 0.0894
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7288
    sort_std: 0.0894
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6107
    std: 0.2015
    paper_value: 0.6107
    paper_std: 0.2015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 7
    true_value: 0.7288
    true_std: 0.0894
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.11809999999999998
    value_note: global 0.7288 within std
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7288
    sort_std: 0.0894
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
  dataset: Max Clique
  rows:
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5407
    std: 0.0088
    paper_value: 0.5407
    paper_std: 0.0088
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.5407
    true_std: 0.0088
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5407
    sort_std: 0.0088
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.4859
    std: 0.0017
    paper_value: 0.4859
    paper_std: 0.0017
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.5407
    true_std: 0.0088
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05479999999999996
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5407
    sort_std: 0.0088
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.4868
    std: 0.0013
    paper_value: 0.4868
    paper_std: 0.0013
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.5407
    true_std: 0.0088
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05389999999999995
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5407
    sort_std: 0.0088
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4584
    std: 0.0101
    paper_value: 0.4584
    paper_std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.4584
    true_std: 0.0101
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4584
    sort_std: 0.0101
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3996
    std: 0.0852
    paper_value: 0.3996
    paper_std: 0.0852
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.4584
    true_std: 0.0101
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.05879999999999996
    value_note: global 0.4584 within std
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4584
    sort_std: 0.0101
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4102
    std: 0.082
    paper_value: 0.4102
    paper_std: 0.082
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.4584
    true_std: 0.0101
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.048199999999999965
    value_note: global 0.4584 within std
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4584
    sort_std: 0.0101
    is_best: false
  metric: F1
  higher_is_better: true
- &id008
  dataset: Max Matching
  rows:
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7527
    std: 0.0051
    paper_value: 0.7527
    paper_std: 0.0051
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.7527
    true_std: 0.0051
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7527
    sort_std: 0.0051
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6399
    std: 0.0231
    paper_value: 0.6399
    paper_std: 0.0231
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.7527
    true_std: 0.0051
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11280000000000001
    value_note: ''
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7527
    sort_std: 0.0051
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6595
    std: 0.0164
    paper_value: 0.6595
    paper_std: 0.0164
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.7527
    true_std: 0.0051
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09320000000000006
    value_note: ''
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7527
    sort_std: 0.0051
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.7402
    std: 0.0172
    paper_value: 0.7402
    paper_std: 0.0172
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.7402
    true_std: 0.0172
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7402
    sort_std: 0.0172
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.6915
    std: 0.009
    paper_value: 0.6915
    paper_std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.7402
    true_std: 0.0172
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048699999999999966
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7402
    sort_std: 0.0172
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.6743
    std: 0.0038
    paper_value: 0.6743
    paper_std: 0.0038
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.7402
    true_std: 0.0172
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06589999999999996
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7402
    sort_std: 0.0172
    is_best: true
  metric: F1
  higher_is_better: true
- &id013
  dataset: RB graph
  rows:
  - model: DeepSets
    model_key: deepsets
    model_plain: DeepSets
    value: 0.918
    std: 0.186
    paper_value: 0.918
    paper_std: 0.186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.918
    true_std: 0.186
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.186
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.491
    std: 0.099
    paper_value: 0.491
    paper_std: 0.099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.491
    true_std: 0.099
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.099
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.041120000000000004
    std: 0.023530000000000002
    paper_value: 0.041120000000000004
    paper_std: 0.023530000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 3
    true_value: 0.041120000000000004
    true_std: 0.023530000000000002
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.041120000000000004
    sort_std: 0.023530000000000002
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.01583
    std: 0.00052
    paper_value: 0.01583
    paper_std: 0.00052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 4
    true_value: 0.01583
    true_std: 0.00052
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.01583
    sort_std: 0.00052
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: SAT Solving
  is_multi_metric: true
  rows:
  - model: Multi-class Classification
    model_key: multi-class classification
    model_plain: Multi-class Classification
    metric_values:
    - null
    - 0.23
    metric_stds:
    - null
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.23
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.23
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: null
  - model: Pairwise Classification
    model_key: pairwise classification
    model_plain: Pairwise Classification
    metric_values:
    - null
    - 0.33
    metric_stds:
    - null
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.33
    sort_std: 0.01
    true_value: null
    true_std: null
    paper_value: 0.33
    paper_std: 0.01
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Pairwise Regression
    model_key: pairwise regression
    model_plain: Pairwise Regression
    metric_values:
    - null
    - 0.54
    metric_stds:
    - null
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.54
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.54
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Random Forest
    model_key: random forest
    model_plain: Random Forest
    metric_values:
    - 0.58
    - null
    metric_stds:
    - 0.0
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.58
    sort_std: 0.0
    true_value: null
    true_std: null
    paper_value: 0.58
    paper_std: 0.0
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    metric_values:
    - 0.63
    - null
    metric_stds:
    - 0.0
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.63
    sort_std: 0.0
    true_value: null
    true_std: null
    paper_value: 0.63
    paper_std: 0.0
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - RMSE
  - Gap Closed
  primary_metric: Accuracy
  higher_is_better: false
- &id009
  dataset: Steiner Trees
  rows:
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.6691
    std: 0.0112
    paper_value: 0.6691
    paper_std: 0.0112
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.6691
    true_std: 0.0112
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6691
    sort_std: 0.0112
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5672
    std: 0.079
    paper_value: 0.5672
    paper_std: 0.079
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.6691
    true_std: 0.0112
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10189999999999999
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6691
    sort_std: 0.0112
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5212
    std: 0.0219
    paper_value: 0.5212
    paper_std: 0.0219
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.6691
    true_std: 0.0112
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14790000000000003
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6691
    sort_std: 0.0112
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6691
    std: 0.0288
    paper_value: 0.6691
    paper_std: 0.0288
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.6691
    true_std: 0.0288
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6691
    sort_std: 0.0288
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5628
    std: 0.11
    paper_value: 0.5628
    paper_std: 0.11
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.6691
    true_std: 0.0288
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.10630000000000006
    value_note: global 0.6691 within std
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6691
    sort_std: 0.0288
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5516
    std: 0.2368
    paper_value: 0.5516
    paper_std: 0.2368
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.6691
    true_std: 0.0288
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: true
    value_gap: 0.11750000000000005
    value_note: global 0.6691 within std
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6691
    sort_std: 0.0288
    is_best: true
  metric: F1
  higher_is_better: true
- &id010
  dataset: Topological Sorting
  rows:
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1001
    std: 0.0089
    paper_value: 0.1001
    paper_std: 0.0089
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.1001
    true_std: 0.0089
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1001
    sort_std: 0.0089
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1537
    std: 0.0031
    paper_value: 0.1537
    paper_std: 0.0031
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.1001
    true_std: 0.0089
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05360000000000001
    value_note: ''
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1001
    sort_std: 0.0089
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1301
    std: 0.0046
    paper_value: 0.1301
    paper_std: 0.0046
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 1
    true_value: 0.1001
    true_std: 0.0089
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03
    value_note: ''
    paper_rank: 2
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1001
    sort_std: 0.0089
    is_best: true
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.116
    std: 0.0058
    paper_value: 0.116
    paper_std: 0.0058
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.116
    true_std: 0.0058
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.116
    sort_std: 0.0058
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.1305
    std: 0.0094
    paper_value: 0.1305
    paper_std: 0.0094
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.116
    true_std: 0.0058
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014499999999999999
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.116
    sort_std: 0.0058
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.1532
    std: 0.0214
    paper_value: 0.1532
    paper_std: 0.0214
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    global_rank: 2
    true_value: 0.116
    true_std: 0.0058
    value_gap_source_arxiv: '2512.04475'
    value_gap_source_title: GraphBench
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0372
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.116
    sort_std: 0.0058
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: GraphBench
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
single_proposed_model: GNN
main_figure: /figures/2512.04475/main_figure.png
---

