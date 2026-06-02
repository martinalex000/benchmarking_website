---
title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating
  State Space Models'
arxiv_id: '2602.17893'
source_url: ''
authors: []
published_date: Feb 19, 2026
published_date_iso: '2026-02-19'
published_venue: ''
abstract: 'State space models (SSMs) have recently emerged for modeling long-range
  dependency in sequence data, with much simplified computational costs than modern
  alternatives, such as transformers. Advancing SMMs to graph structured data, especially
  for large graphs, is a significant challenge because SSMs are sequence models and
  the shear graph volumes make it very expensive to convert graphs as sequences for
  effective learning. In this paper, we propose COMBA to tackle large graph learning
  using state space models, with two key innovations: graph context gating and cross
  batch aggregation. Graph context refers to different hops of neighborhood for each
  node, and graph context gating allows COMBA to use such context to learn best control
  of neighbor aggregation. For each graph context, COMBA samples nodes as batches,
  and train a graph neural network (GNN), with information being aggregated cross
  batches, allowing COMBA to scale to large graphs. Our theoretical study asserts
  that cross-batch aggregation guarantees lower error than training GNN without aggregation.
  Experiments on benchmark networks demonstrate significant performance gains compared
  to baseline approaches. Code and benchmark datasets will be released for public
  access.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- COMBA
mrr: 0.0526
adjusted_mrr: 0.0526
mrr_dataset_count: 6
benchmark_categories:
- Heterophilic Graphs
- OGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: Amazon-ratings
  rows:
  - model: here instead
    model_key: here instead
    model_plain: here instead
    value: 0.909
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 15, 2015
    date_display: Jun 2015
    date_iso: '2015-06-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.909
    sort_std: null
    is_best: true
  - model: CT
    model_key: ct
    model_plain: CT
    value: 0.848
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 15, 2015
    date_display: Jun 2015
    date_iso: '2015-06-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.848
    sort_std: null
    is_best: false
  - model: WNN
    model_key: wnn
    model_plain: WNN
    value: 0.843
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 15, 2015
    date_display: Jun 2015
    date_iso: '2015-06-15'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.843
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.462
    std: 0.008
    paper_value: 0.462
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 6
    true_value: 0.8326
    true_std: 0.0051
    value_gap_source_arxiv: '2410.10320'
    value_gap_source_title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3706
    value_note: ''
    paper_rank: 54
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.8326
    sort_std: 0.0051
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.504
    std: 0.007
    paper_value: 0.504
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 39
    true_value: 0.5126
    true_std: 0.0072
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008599999999999941
    value_note: ''
    paper_rank: 43
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.5126
    sort_std: 0.0072
    is_best: false
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.507
    std: 0.0025
    paper_value: 0.507
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 41
    true_value: 0.507
    true_std: 0.0025
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.507
    sort_std: 0.0025
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.49
    std: 0.0036
    paper_value: 0.49
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 46
    true_value: 0.49
    true_std: 0.0036
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.0036
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.481
    std: 0.0071
    paper_value: 0.481
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 49
    true_value: 0.481
    true_std: 0.0071
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.481
    sort_std: 0.0071
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.476
    std: 0.0047
    paper_value: 0.476
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 51
    true_value: 0.476
    true_std: 0.0047
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: 0.0047
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9907
    std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 1, 2025
    date_display: Jul 2025
    date_iso: '2025-07-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9907
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 1, 2025
    date_display: Jul 2025
    date_iso: '2025-07-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 7, 2025
    date_display: Aug 2025
    date_iso: '2025-08-07'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.942
    std: 0.0039
    paper_value: 0.942
    paper_std: 0.0039
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 8
    true_value: 0.942
    true_std: 0.0039
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.942
    sort_std: 0.0039
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.927
    std: 0.0021
    paper_value: 0.927
    paper_std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 10
    true_value: 0.927
    true_std: 0.0021
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.927
    sort_std: 0.0021
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.905
    std: 0.0016
    paper_value: 0.905
    paper_std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 18
    true_value: 0.905
    true_std: 0.0016
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.905
    sort_std: 0.0016
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.903
    std: 0.0006
    paper_value: 0.903
    paper_std: 0.0006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 19
    true_value: 0.903
    true_std: 0.0006
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.903
    sort_std: 0.0006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.884
    std: 0.0046
    paper_value: 0.884
    paper_std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 21
    true_value: 0.8975
    true_std: 0.0052
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013499999999999956
    value_note: ''
    paper_rank: 23
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.8975
    sort_std: 0.0052
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.886
    std: 0.0024
    paper_value: 0.886
    paper_std: 0.0024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 23
    true_value: 0.886
    true_std: 0.0024
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.886
    sort_std: 0.0024
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Roman-empire
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9263
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 1, 2025
    date_display: Jul 2025
    date_iso: '2025-07-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9263
    sort_std: 0.005
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9255
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9255
    sort_std: 0.003
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.9203
    std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9203
    sort_std: 0.0085
    is_best: true
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.895
    std: 0.0038
    paper_value: 0.895
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: This paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 11
    true_value: 0.895
    true_std: 0.0038
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.895
    sort_std: 0.0038
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.869
    std: 0.0092
    paper_value: 0.869
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: This paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 19
    true_value: 0.869
    true_std: 0.0092
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.869
    sort_std: 0.0092
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.833
    std: 0.0079
    paper_value: 0.833
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Feng et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 27
    true_value: 0.833
    true_std: 0.0079
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.833
    sort_std: 0.0079
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.815
    std: 0.0042
    paper_value: 0.815
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 32
    true_value: 0.815
    true_std: 0.0042
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.815
    sort_std: 0.0042
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.8
    std: 0.0043
    paper_value: 0.8
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: This paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 35
    true_value: 0.8
    true_std: 0.0043
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.0043
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.795
    std: 0.0088
    paper_value: 0.795
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 37
    true_value: 0.795
    true_std: 0.0088
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.0088
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Tolokers
  rows:
  - model: GRAMA_GCNGCN
    model_key: grama_gcngcn
    model_plain: GRAMA_GCNGCN
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8566
    std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 7, 2025
    date_display: Aug 2025
    date_iso: '2025-08-07'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8566
    sort_std: 0.0101
    is_best: true
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.845
    std: 0.0009
    paper_value: 0.845
    paper_std: 0.0009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 16
    true_value: 0.845
    true_std: 0.0009
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.0009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.838
    std: 0.0034
    paper_value: 0.838
    paper_std: 0.0034
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 19
    true_value: 0.838
    true_std: 0.0034
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.834
    std: 0.0045
    paper_value: 0.834
    paper_std: 0.0045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 30
    true_value: 0.834
    true_std: 0.0045
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.834
    sort_std: 0.0045
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.832
    std: 0.009
    paper_value: 0.832
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 33
    true_value: 0.832
    true_std: 0.009
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.832
    sort_std: 0.009
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.803
    std: 0.0199
    paper_value: 0.803
    paper_std: 0.0199
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 40
    true_value: 0.803
    true_std: 0.0199
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.803
    sort_std: 0.0199
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.758
    std: 0.0056
    paper_value: 0.758
    paper_std: 0.0056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 53
    true_value: 0.758
    true_std: 0.0056
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.0056
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
  dataset: ogbn-arxiv
  rows:
  - model: KCoT
    model_key: kcot
    model_plain: KCoT
    value: 0.7925
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.24867'
    title: 'Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought
      Graph Learning'
    date: May 24, 2026
    date_display: May 2026
    date_iso: '2026-05-24'
    codebase_url: https://github.com/Uncnbb/KCoT
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7925
    sort_std: null
    is_best: true
  - model: TAPE + SimTeG
    model_key: tape + simteg
    model_plain: TAPE + SimTeG
    value: 0.7803
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.02565'
    title: 'SimTeG: A Frustratingly ple Approach Improves xtual raph Learning'
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/vermouthdky/SimTeG
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.7803
    sort_std: 0.0007
    is_best: false
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.7751
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.19211'
    title: 'Large Language Models Meet Graph Neural Networks: A Perspective of Graph
      Mining'
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7751
    sort_std: 0.0017
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.68
    std: 0.0044
    paper_value: 0.68
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 57
    true_value: 0.752
    true_std: 0.0003
    value_gap_source_arxiv: '2509.14863'
    value_gap_source_title: 'Exploring the Global-to-Local Attention Scheme in Graph
      Transformers: An Empirical Study'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07199999999999995
    value_note: ''
    paper_rank: 323
    rank_delta: 266
    rank_delta_abs: 266
    rank_delta_direction: worse
    sort_value: 0.752
    sort_std: 0.0003
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.686
    std: 0.0089
    paper_value: 0.686
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 188
    true_value: 0.7248
    true_std: 0.0
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038799999999999946
    value_note: ''
    paper_rank: 318
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.7248
    sort_std: 0.0
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.678
    std: 0.0076
    paper_value: 0.678
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 195
    true_value: 0.7239
    true_std: null
    value_gap_source_arxiv: '2502.19693'
    value_gap_source_title: Accurate and Scalable Graph Neural Networks via Message
      Invariance
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04589999999999994
    value_note: ''
    paper_rank: 326
    rank_delta: 131
    rank_delta_abs: 131
    rank_delta_direction: worse
    sort_value: 0.7239
    sort_std: null
    is_best: false
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.716
    std: 0.0037
    paper_value: 0.716
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 247
    true_value: 0.716
    true_std: 0.0037
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 247
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.716
    sort_std: 0.0037
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.696
    std: 0.0023
    paper_value: 0.696
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 274
    true_value: 0.7101
    true_std: 0.0013
    value_gap_source_arxiv: '2403.16358'
    value_gap_source_title: 'ChebMixer: Efficient Graph Representation Learning with
      MLP Mixer'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014100000000000001
    value_note: ''
    paper_rank: 305
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.7101
    sort_std: 0.0013
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.701
    std: 0.0065
    paper_value: 0.701
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Feng et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 294
    true_value: 0.701
    true_std: 0.0065
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.0065
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbn-products
  rows:
  - model: GTs
    model_key: gts
    model_plain: GTs
    value: 0.9037
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9037
    sort_std: 0.0005
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9017
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9017
    sort_std: 0.0016
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8909
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8909
    sort_std: 0.001
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.717
    std: 0.0053
    paper_value: 0.717
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 63
    true_value: 0.7962
    true_std: null
    value_gap_source_arxiv: '2502.19693'
    value_gap_source_title: Accurate and Scalable Graph Neural Networks via Message
      Invariance
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07920000000000005
    value_note: ''
    paper_rank: 122
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.7962
    sort_std: null
    is_best: false
  - model: COMBA
    model_key: comba
    model_plain: COMBA
    value: 0.735
    std: 0.01
    paper_value: 0.735
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 19, 2026
    date_display: Feb 2026
    date_iso: '2026-02-19'
    published_venue: null
    global_rank: 112
    true_value: 0.735
    true_std: 0.01
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.01
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: OGB
  datasets:
  - *id005
  - *id006
single_proposed_model: COMBA
---

