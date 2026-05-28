---
title: Non-Dissipative Graph Propagation for Non-Local Community Detection
arxiv_id: '2508.14097'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
abstract: Community detection in graphs aims to cluster nodes into meaningful groups,
  a task particularly challenging in heterophilic graphs, where nodes sharing similarities
  and membership to the same community are typically distantly connected. This is
  particularly evident when this task is tackled by graph neural networks, since they
  rely on an inherently local message passing scheme to learn the node representations
  that serve to cluster nodes into communities. In this work, we argue that the ability
  to propagate long-range information during message passing is key to effectively
  perform community detection in heterophilic graphs. To this end, we introduce the
  Unsupervised Antisymmetric Graph Neural Network (uAGNN), a novel unsupervised community
  detection approach leveraging non-dissipative dynamical systems to ensure stability
  and to propagate long-range information effectively. By employing antisymmetric
  weight matrices, uAGNN captures both local and global graph structures, overcoming
  the limitations posed by heterophilic scenarios. Extensive experiments across ten
  datasets demonstrate uAGNN's superior performance in high and medium heterophilic
  settings, where traditional methods fail to exploit long-range dependencies. These
  results highlight uAGNN's potential as a powerful tool for unsupervised community
  detection in diverse graph environments.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- uAGNN
mrr: 0.007
adjusted_mrr: 0.0023
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- GraphBench
- Hypergraph Benchmarks
- Heterogeneous Graph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id008
  dataset: AMAP
  rows:
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.67
    std: 0.1
    paper_value: 0.67
    paper_std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.67
    true_std: 0.1
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.1
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.65
    std: 0.07
    paper_value: 0.65
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.65
    true_std: 0.07
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.07
    is_best: true
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.61
    std: 0.16
    paper_value: 0.61
    paper_std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.61
    true_std: 0.16
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.16
    is_best: true
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.51
    std: 0.09
    paper_value: 0.51
    paper_std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.51
    true_std: 0.09
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51
    sort_std: 0.09
    is_best: true
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.48
    std: 0.1
    paper_value: 0.48
    paper_std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.48
    true_std: 0.1
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.1
    is_best: true
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.48
    std: 0.09
    paper_value: 0.48
    paper_std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.48
    true_std: 0.09
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.09
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.34
    std: 0.02
    paper_value: 0.34
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.34
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34
    sort_std: 0.02
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.34
    std: 0.06
    paper_value: 0.34
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.34
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34
    sort_std: 0.06
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.25
    std: 0.03
    paper_value: 0.25
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.25
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.03
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: Amazon-Computers
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9409
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9409
    sort_std: 0.0037
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9399
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9399
    sort_std: 0.0012
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9378
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9378
    sort_std: 0.001
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.67
    std: 0.1
    paper_value: 0.67
    paper_std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.67
    sort_std: 0.1
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.65
    std: 0.07
    paper_value: 0.65
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.65
    sort_std: 0.07
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.61
    std: 0.16
    paper_value: 0.61
    paper_std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.61
    sort_std: 0.16
    is_best: false
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.51
    std: 0.09
    paper_value: 0.51
    paper_std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.51
    sort_std: 0.09
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.48
    std: 0.1
    paper_value: 0.48
    paper_std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.48
    sort_std: 0.1
    is_best: false
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.48
    std: 0.09
    paper_value: 0.48
    paper_std: 0.09
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.48
    sort_std: 0.09
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.34
    std: 0.02
    paper_value: 0.34
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.34
    sort_std: 0.02
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.34
    std: 0.06
    paper_value: 0.34
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.34
    sort_std: 0.06
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.25
    std: 0.03
    paper_value: 0.25
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.25
    sort_std: 0.03
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: BAT
  rows:
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.65
    std: 0.05
    paper_value: 0.65
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.65
    true_std: 0.05
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.05
    is_best: true
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.54
    std: 0.1
    paper_value: 0.54
    paper_std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.54
    true_std: 0.1
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.54
    sort_std: 0.1
    is_best: true
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.53
    std: 0.03
    paper_value: 0.53
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.53
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.03
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.52
    std: 0.03
    paper_value: 0.52
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.52
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.03
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.46
    std: 0.04
    paper_value: 0.46
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.46
    true_std: 0.04
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.46
    sort_std: 0.04
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.44
    std: 0.06
    paper_value: 0.44
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.44
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.44
    sort_std: 0.06
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.38
    std: 0.07
    paper_value: 0.38
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.38
    true_std: 0.07
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.38
    sort_std: 0.07
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.36
    std: 0.06
    paper_value: 0.36
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.36
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.06
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.36
    std: 0.06
    paper_value: 0.36
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.36
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.06
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.63
    std: 0.01
    paper_value: 0.63
    paper_std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 99
    sort_value: 0.63
    sort_std: 0.01
    is_best: false
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.61
    std: 0.03
    paper_value: 0.61
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.61
    sort_std: 0.03
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.61
    std: 0.14
    paper_value: 0.61
    paper_std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.61
    sort_std: 0.14
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.6
    std: 0.02
    paper_value: 0.6
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.6
    sort_std: 0.02
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.58
    std: 0.02
    paper_value: 0.58
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.58
    sort_std: 0.02
    is_best: false
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.55
    std: 0.11
    paper_value: 0.55
    paper_std: 0.11
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.55
    sort_std: 0.11
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.5
    std: 0.07
    paper_value: 0.5
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 212
    sort_value: 0.5
    sort_std: 0.07
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.5
    std: 0.04
    paper_value: 0.5
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.5
    sort_std: 0.04
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.38
    std: 0.15
    paper_value: 0.38
    paper_std: 0.15
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 120
    sort_value: 0.38
    sort_std: 0.15
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.61
    std: 0.04
    paper_value: 0.61
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 228
    sort_value: 0.61
    sort_std: 0.04
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.58
    std: 0.08
    paper_value: 0.58
    paper_std: 0.08
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.58
    sort_std: 0.08
    is_best: false
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.54
    std: 0.03
    paper_value: 0.54
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.54
    sort_std: 0.03
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.54
    std: 0.03
    paper_value: 0.54
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.54
    sort_std: 0.03
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.54
    std: 0.14
    paper_value: 0.54
    paper_std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.54
    sort_std: 0.14
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.48
    std: 0.06
    paper_value: 0.48
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 288
    sort_value: 0.48
    sort_std: 0.06
    is_best: false
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.48
    std: 0.08
    paper_value: 0.48
    paper_std: 0.08
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.48
    sort_std: 0.08
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.39
    std: 0.05
    paper_value: 0.39
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 122
    sort_value: 0.39
    sort_std: 0.05
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.38
    std: 0.06
    paper_value: 0.38
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 236
    sort_value: 0.38
    sort_std: 0.06
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  is_multi_metric: true
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    metric_values:
    - 0.9525
    - null
    metric_stds:
    - 0.0155
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.9525
    sort_std: 0.0155
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    metric_values:
    - 0.9393
    - null
    metric_stds:
    - 0.0105
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.9393
    sort_std: 0.0105
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    metric_values:
    - 0.9377
    - null
    metric_stds:
    - 0.0217
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
    sort_value: 0.9377
    sort_std: 0.0217
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: DGI
    model_key: dgi
    model_plain: DGI
    metric_values:
    - 0.34
    - 0.06
    metric_stds:
    - 0.06
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.34
    sort_std: 0.06
    true_value: null
    true_std: null
    paper_value: 0.34
    paper_std: 0.06
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DMON
    model_key: dmon
    model_plain: DMON
    metric_values:
    - 0.34
    - 0.22
    metric_stds:
    - 0.05
    - 0.07
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.34
    sort_std: 0.05
    true_value: null
    true_std: null
    paper_value: 0.34
    paper_std: 0.05
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    metric_values:
    - 0.29
    - 0.27
    metric_stds:
    - 0.04
    - 0.07
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.29
    sort_std: 0.04
    true_value: null
    true_std: null
    paper_value: 0.29
    paper_std: 0.04
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    metric_values:
    - 0.27
    - 0.06
    metric_stds:
    - 0.05
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.27
    sort_std: 0.05
    true_value: null
    true_std: null
    paper_value: 0.27
    paper_std: 0.05
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    metric_values:
    - 0.25
    - 0.05
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.25
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.25
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    metric_values:
    - 0.25
    - 0.05
    metric_stds:
    - 0.02
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.25
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.25
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    metric_values:
    - 0.24
    - 0.05
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.24
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.24
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    metric_values:
    - 0.23
    - 0.03
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.23
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.23
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 63
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    metric_values:
    - 0.22
    - 0.08
    metric_stds:
    - 0.02
    - 0.03
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.22
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.22
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - F1
  - NMI
  primary_metric: Accuracy
  higher_is_better: true
- &id012
  dataset: DBLP
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    value: 0.9249
    std: 0.0035
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9249
    sort_std: 0.0035
    is_best: true
  - model: GTN
    model_key: gtn
    model_plain: GTN
    value: 0.9148
    std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9148
    sort_std: 0.0039
    is_best: false
  - model: HAN
    model_key: han
    model_plain: HAN
    value: 0.9147
    std: 0.0022
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9147
    sort_std: 0.0022
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.72
    std: 0.05
    paper_value: 0.72
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.72
    sort_std: 0.05
    is_best: false
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.71
    std: 0.14
    paper_value: 0.71
    paper_std: 0.14
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.71
    sort_std: 0.14
    is_best: false
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.64
    std: 0.07
    paper_value: 0.64
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.64
    sort_std: 0.07
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.6
    std: 0.11
    paper_value: 0.6
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
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    sort_value: 0.6
    sort_std: 0.11
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.55
    std: 0.07
    paper_value: 0.55
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.55
    sort_std: 0.07
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.5
    std: 0.07
    paper_value: 0.5
    paper_std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.5
    sort_std: 0.07
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.5
    std: 0.13
    paper_value: 0.5
    paper_std: 0.13
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.5
    sort_std: 0.13
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.45
    std: 0.06
    paper_value: 0.45
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.45
    sort_std: 0.06
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.42
    std: 0.21
    paper_value: 0.42
    paper_std: 0.21
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.42
    sort_std: 0.21
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id011
  dataset: EAT
  rows:
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.48
    std: 0.03
    paper_value: 0.48
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.48
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.03
    is_best: true
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.47
    std: 0.06
    paper_value: 0.47
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.47
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47
    sort_std: 0.06
    is_best: true
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.47
    std: 0.05
    paper_value: 0.47
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.47
    true_std: 0.05
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47
    sort_std: 0.05
    is_best: true
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.46
    std: 0.05
    paper_value: 0.46
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.46
    true_std: 0.05
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.46
    sort_std: 0.05
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.42
    std: 0.06
    paper_value: 0.42
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.42
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.42
    sort_std: 0.06
    is_best: true
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.41
    std: 0.02
    paper_value: 0.41
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.41
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41
    sort_std: 0.02
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.35
    std: 0.04
    paper_value: 0.35
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.35
    true_std: 0.04
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.34
    std: 0.03
    paper_value: 0.34
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.34
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34
    sort_std: 0.03
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.19
    std: 0.02
    paper_value: 0.19
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.19
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19
    sort_std: 0.02
    is_best: false
  metric: F1
  higher_is_better: true
- &id004
  dataset: Texas
  is_multi_metric: true
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    metric_values:
    - 0.9656
    - null
    metric_stds:
    - 0.02
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.9656
    sort_std: 0.02
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    metric_values:
    - 0.9574
    - null
    metric_stds:
    - 0.0222
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.9574
    sort_std: 0.0222
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    metric_values:
    - 0.9475
    - null
    metric_stds:
    - 0.0309
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
    sort_value: 0.9475
    sort_std: 0.0309
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    metric_values:
    - 0.35
    - 0.14
    metric_stds:
    - 0.05
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.35
    sort_std: 0.05
    true_value: null
    true_std: null
    paper_value: 0.35
    paper_std: 0.05
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DMON
    model_key: dmon
    model_plain: DMON
    metric_values:
    - 0.33
    - 0.21
    metric_stds:
    - 0.02
    - 0.04
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.33
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.33
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    metric_values:
    - 0.33
    - 0.22
    metric_stds:
    - 0.09
    - 0.07
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.33
    sort_std: 0.09
    true_value: null
    true_std: null
    paper_value: 0.33
    paper_std: 0.09
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: DGI
    model_key: dgi
    model_plain: DGI
    metric_values:
    - 0.31
    - 0.12
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.31
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.31
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    metric_values:
    - 0.29
    - 0.15
    metric_stds:
    - 0.08
    - 0.0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.29
    sort_std: 0.08
    true_value: null
    true_std: null
    paper_value: 0.29
    paper_std: 0.08
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    metric_values:
    - 0.29
    - 0.1
    metric_stds:
    - 0.02
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.29
    sort_std: 0.02
    true_value: null
    true_std: null
    paper_value: 0.29
    paper_std: 0.02
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    metric_values:
    - 0.24
    - 0.06
    metric_stds:
    - 0.03
    - 0.03
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.24
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.24
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    metric_values:
    - 0.24
    - 0.08
    metric_stds:
    - 0.03
    - 0.02
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.24
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.24
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    metric_values:
    - 0.21
    - 0.03
    metric_stds:
    - 0.03
    - 0.01
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.21
    sort_std: 0.03
    true_value: null
    true_std: null
    paper_value: 0.21
    paper_std: 0.03
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 81
  metrics:
  - F1
  - NMI
  primary_metric: Accuracy
  higher_is_better: true
- &id010
  dataset: UAT
  rows:
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.54
    std: 0.01
    paper_value: 0.54
    paper_std: 0.01
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2019
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.54
    true_std: 0.01
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.54
    sort_std: 0.01
    is_best: true
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.53
    std: 0.02
    paper_value: 0.53
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.53
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.02
    is_best: true
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.52
    std: 0.03
    paper_value: 0.52
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2019
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.52
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.03
    is_best: true
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.52
    std: 0.03
    paper_value: 0.52
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhu et al. 2020
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.52
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.03
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.49
    std: 0.04
    paper_value: 0.49
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tsitsulin et al. 2023
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 5
    true_value: 0.49
    true_std: 0.04
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.04
    is_best: true
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.49
    std: 0.04
    paper_value: 0.49
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hassani et al. 2020
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.49
    true_std: 0.04
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.04
    is_best: true
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.48
    std: 0.02
    paper_value: 0.48
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 7
    true_value: 0.48
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.02
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.44
    std: 0.03
    paper_value: 0.44
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qiu et al. 2022
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.44
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.44
    sort_std: 0.03
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.17
    std: 0.13
    paper_value: 0.17
    paper_std: 0.13
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.17
    true_std: 0.13
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.17
    sort_std: 0.13
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
  dataset: Weather Forecasting
  rows:
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.48
    std: 0.03
    paper_value: 0.48
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.48
    sort_std: 0.03
    is_best: true
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.47
    std: 0.06
    paper_value: 0.47
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.47
    sort_std: 0.06
    is_best: true
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.47
    std: 0.05
    paper_value: 0.47
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.47
    sort_std: 0.05
    is_best: true
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.46
    std: 0.05
    paper_value: 0.46
    paper_std: 0.05
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.46
    sort_std: 0.05
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.42
    std: 0.06
    paper_value: 0.42
    paper_std: 0.06
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.42
    sort_std: 0.06
    is_best: true
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.41
    std: 0.02
    paper_value: 0.41
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.41
    sort_std: 0.02
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.35
    std: 0.04
    paper_value: 0.35
    paper_std: 0.04
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.34
    std: 0.03
    paper_value: 0.34
    paper_std: 0.03
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.34
    sort_std: 0.03
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.19
    std: 0.02
    paper_value: 0.19
    paper_std: 0.02
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: null
    sort_value: 0.19
    sort_std: 0.02
    is_best: false
  metric: MAE
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.23
    std: 0.02
    paper_value: 0.23
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 52
    true_value: 0.7882
    true_std: 0.0655
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5582
    value_note: ''
    paper_rank: 148
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.7882
    sort_std: 0.0655
    is_best: false
  - model: uAGNN
    model_key: uagnn
    model_plain: uAGNN
    value: 0.43
    std: 0.06
    paper_value: 0.43
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 142
    true_value: 0.43
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.43
    sort_std: 0.06
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.39
    std: 0.03
    paper_value: 0.39
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 143
    true_value: 0.39
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.03
    is_best: false
  - model: GRACE
    model_key: grace
    model_plain: GRACE
    value: 0.29
    std: 0.01
    paper_value: 0.29
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 144
    true_value: 0.29
    true_std: 0.01
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.29
    sort_std: 0.01
    is_best: false
  - model: DAEGC
    model_key: daegc
    model_plain: DAEGC
    value: 0.28
    std: 0.02
    paper_value: 0.28
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 145
    true_value: 0.28
    true_std: 0.02
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28
    sort_std: 0.02
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.27
    std: 0.03
    paper_value: 0.27
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 146
    true_value: 0.27
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27
    sort_std: 0.03
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.25
    std: 0.05
    paper_value: 0.25
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 147
    true_value: 0.25
    true_std: 0.05
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.05
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.24
    std: 0.03
    paper_value: 0.24
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 148
    true_value: 0.24
    true_std: 0.03
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.24
    sort_std: 0.03
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.19
    std: 0.06
    paper_value: 0.19
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 149
    true_value: 0.19
    true_std: 0.06
    value_gap_source_arxiv: '2508.14097'
    value_gap_source_title: Non-Dissipative Graph Propagation for Non-Local Community
      Detection
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19
    sort_std: 0.06
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: GraphBench
  datasets:
  - *id007
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id012
single_proposed_model: uAGNN
main_figure: /figures/2508.14097/main_figure.png
---

