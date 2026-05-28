---
title: ECHO Benchmark
arxiv_id: '2512.17762'
source_url: ''
authors: []
published_date: Dec 2025
published_date_iso: 2025-12
abstract: Effectively capturing long-range interactions remains a fundamental yet
  unresolved challenge in graph neural network (GNN) research, critical for applications
  across diverse fields of science. To systematically address this, we introduce ECHO
  (Evaluating Communication over long HOps), a novel benchmark specifically designed
  to rigorously assess the capabilities of GNNs in handling very long-range graph
  propagation. ECHO includes three synthetic graph tasks, namely single-source shortest
  paths, node eccentricity, and graph diameter, each constructed over diverse and
  structurally challenging topologies intentionally designed to introduce significant
  information bottlenecks. ECHO also includes two real-world datasets, ECHO-Charge
  and ECHO-Energy, which define chemically grounded benchmarks for predicting atomic
  partial charges and molecular total energies, respectively, with reference computations
  obtained at the density functional theory (DFT) level. Both tasks inherently depend
  on capturing complex long-range molecular interactions. Our extensive benchmarking
  of popular GNN architectures reveals clear performance gaps, emphasizing the difficulty
  of true long-range propagation and highlighting design choices capable of overcoming
  inherent limitations. ECHO thereby sets a new standard for evaluating long-range
  information propagation, also providing a compelling example for its need in AI
  for science.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GRIT
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- ECHO Benchmark
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: ECHO-Charge
  rows:
  - model: SWAN
    model_key: swan
    model_plain: SWAN
    value: 6.109
    std: 0.103
    paper_value: 6.109
    paper_std: 0.103
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
    global_rank: 1
    true_value: 6.109
    true_std: 0.103
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 6.109
    sort_std: 0.103
    is_best: true
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 6.182
    std: 0.219
    paper_value: 6.182
    paper_std: 0.219
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
    true_value: 6.182
    true_std: 0.219
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 6.182
    sort_std: 0.219
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 6.543
    std: 0.146
    paper_value: 6.543
    paper_std: 0.146
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
    true_value: 6.543
    true_std: 0.146
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 6.543
    sort_std: 0.146
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 7.134
    std: 6.09
    paper_value: 7.134
    paper_std: 6.09
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
    global_rank: 4
    true_value: 7.134
    true_std: 6.09
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 7.134
    sort_std: 6.09
    is_best: true
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 7.176
    std: 0.371
    paper_value: 7.176
    paper_std: 0.371
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
    global_rank: 5
    true_value: 7.176
    true_std: 0.371
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 7.176
    sort_std: 0.371
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 7.915
    std: 0.269
    paper_value: 7.915
    paper_std: 0.269
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
    global_rank: 6
    true_value: 7.915
    true_std: 0.269
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 7.915
    sort_std: 0.269
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 8.421
    std: 0.512
    paper_value: 8.421
    paper_std: 0.512
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
    global_rank: 7
    true_value: 8.421
    true_std: 0.512
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 8.421
    sort_std: 0.512
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 8.829
    std: 0.021
    paper_value: 8.829
    paper_std: 0.021
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
    global_rank: 8
    true_value: 8.829
    true_std: 0.021
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 8.829
    sort_std: 0.021
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 9.086
    std: 0.473
    paper_value: 9.086
    paper_std: 0.473
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
    global_rank: 9
    true_value: 9.086
    true_std: 0.473
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 9.086
    sort_std: 0.473
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 10.784
    std: 0.059
    paper_value: 10.784
    paper_std: 0.059
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
    global_rank: 10
    true_value: 10.784
    true_std: 0.059
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 10.784
    sort_std: 0.059
    is_best: false
  - model: GraphCON
    model_key: graphcon
    model_plain: GraphCON
    value: 19.629
    std: 0.195
    paper_value: 19.629
    paper_std: 0.195
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
    global_rank: 11
    true_value: 19.629
    true_std: 0.195
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 19.629
    sort_std: 0.195
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: ECHO-Energy
  rows:
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 5.257
    std: 0.842
    paper_value: 5.257
    paper_std: 0.842
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
    global_rank: 1
    true_value: 5.257
    true_std: 0.842
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 5.257
    sort_std: 0.842
    is_best: true
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 11.325
    std: 2.394
    paper_value: 11.325
    paper_std: 2.394
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
    true_value: 11.325
    true_std: 2.394
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 11.325
    sort_std: 2.394
    is_best: false
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 12.486
    std: 1.621
    paper_value: 12.486
    paper_std: 1.621
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
    true_value: 12.486
    true_std: 1.621
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 12.486
    sort_std: 1.621
    is_best: false
  - model: SWAN
    model_key: swan
    model_plain: SWAN
    value: 12.629
    std: 1.157
    paper_value: 12.629
    paper_std: 1.157
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
    global_rank: 4
    true_value: 12.629
    true_std: 1.157
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 12.629
    sort_std: 1.157
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 13.235
    std: 2.63
    paper_value: 13.235
    paper_std: 2.63
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
    global_rank: 5
    true_value: 13.235
    true_std: 2.63
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 13.235
    sort_std: 2.63
    is_best: false
  - model: GraphCON
    model_key: graphcon
    model_plain: GraphCON
    value: 14.295
    std: 0.807
    paper_value: 14.295
    paper_std: 0.807
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
    global_rank: 6
    true_value: 14.295
    true_std: 0.807
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 14.295
    sort_std: 0.807
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 16.08
    std: 1.123
    paper_value: 16.08
    paper_std: 1.123
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
    global_rank: 7
    true_value: 16.08
    true_std: 1.123
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 16.08
    sort_std: 1.123
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 23.558
    std: 7.568
    paper_value: 23.558
    paper_std: 7.568
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
    global_rank: 8
    true_value: 23.558
    true_std: 7.568
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 23.558
    sort_std: 7.568
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 25.508
    std: 2.507
    paper_value: 25.508
    paper_std: 2.507
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
    global_rank: 9
    true_value: 25.508
    true_std: 2.507
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 25.508
    sort_std: 2.507
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 28.112
    std: 1.239
    paper_value: 28.112
    paper_std: 1.239
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
    global_rank: 10
    true_value: 28.112
    true_std: 1.239
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 28.112
    sort_std: 1.239
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 47.851
    std: 10.154
    paper_value: 47.851
    paper_std: 10.154
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
    global_rank: 11
    true_value: 47.851
    true_std: 10.154
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 47.851
    sort_std: 10.154
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: ECHO-Synth
  rows:
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 1.014
    std: 0.046
    paper_value: 1.014
    paper_std: 0.046
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
    true_value: 1.014
    true_std: 0.046
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.014
    sort_std: 0.046
    is_best: true
  - model: SWAN
    model_key: swan
    model_plain: SWAN
    value: 1.121
    std: 0.07
    paper_value: 1.121
    paper_std: 0.07
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
    true_value: 1.121
    true_std: 0.07
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.121
    sort_std: 0.07
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 1.151
    std: 0.038
    paper_value: 1.151
    paper_std: 0.038
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
    true_value: 1.151
    true_std: 0.038
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.151
    sort_std: 0.038
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 1.243
    std: 0.047
    paper_value: 1.243
    paper_std: 0.047
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
    global_rank: 4
    true_value: 1.243
    true_std: 0.047
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.243
    sort_std: 0.047
    is_best: false
  - model: PH-DGN
    model_key: ph-dgn
    model_plain: PH-DGN
    value: 1.627
    std: 0.398
    paper_value: 1.627
    paper_std: 0.398
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
    global_rank: 5
    true_value: 1.627
    true_std: 0.398
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.627
    sort_std: 0.398
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 1.63
    std: 0.161
    paper_value: 1.63
    paper_std: 0.161
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
    global_rank: 6
    true_value: 1.63
    true_std: 0.161
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.63
    sort_std: 0.161
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 2.005
    std: 0.093
    paper_value: 2.005
    paper_std: 0.093
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
    global_rank: 7
    true_value: 2.005
    true_std: 0.093
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.005
    sort_std: 0.093
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 2.16
    std: 0.098
    paper_value: 2.16
    paper_std: 0.098
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
    global_rank: 8
    true_value: 2.16
    true_std: 0.098
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.16
    sort_std: 0.098
    is_best: false
  - model: GraphCON
    model_key: graphcon
    model_plain: GraphCON
    value: 2.969
    std: 0.189
    paper_value: 2.969
    paper_std: 0.189
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
    global_rank: 9
    true_value: 2.969
    true_std: 0.189
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.969
    sort_std: 0.189
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 3.832
    std: 0.262
    paper_value: 3.832
    paper_std: 0.262
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
    global_rank: 10
    true_value: 3.832
    true_std: 0.262
    value_gap_source_arxiv: '2512.17762'
    value_gap_source_title: ECHO Benchmark
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 3.832
    sort_std: 0.262
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: ECHO Benchmark
  datasets:
  - *id001
  - *id002
  - *id003
single_proposed_model: GRIT
main_figure: /figures/2512.17762/main_figure.png
---

