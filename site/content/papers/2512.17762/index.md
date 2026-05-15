---
title: ECHO Benchmark
arxiv_id: '2512.17762'
authors: []
published_date: Dec 2025
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
proposed_models:
- GRIT
mrr: 0.0
results:
- &id001
  dataset: ECHO-Charge
  rows:
  - model: SWAN
    value: 6.109
    std: 0.103
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GPS
    value: 6.182
    std: 0.219
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: A-DGN
    value: 6.543
    std: 0.146
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GRIT
    value: 7.134
    std: 6.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GINE
    value: 7.176
    std: 0.371
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: PH-DGN
    value: 7.915
    std: 0.269
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GCN
    value: 8.421
    std: 0.512
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GCNII
    value: 8.829
    std: 0.021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: DRew
    value: 9.086
    std: 0.473
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GIN
    value: 10.784
    std: 0.059
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GraphCON
    value: 19.629
    std: 0.195
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: ECHO-Energy
  rows:
  - model: GPS
    value: 5.257
    std: 0.842
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: DRew
    value: 11.325
    std: 2.394
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: A-DGN
    value: 12.486
    std: 1.621
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: SWAN
    value: 12.629
    std: 1.157
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GCNII
    value: 13.235
    std: 2.63
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GraphCON
    value: 14.295
    std: 0.807
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: PH-DGN
    value: 16.08
    std: 1.123
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GINE
    value: 23.558
    std: 7.568
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GRIT
    value: 25.508
    std: 2.507
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GCN
    value: 28.112
    std: 1.239
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GIN
    value: 47.851
    std: 10.154
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: ECHO-Synth
  rows:
  - model: GRIT
    value: 1.014
    std: 0.046
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: SWAN
    value: 1.121
    std: 0.07
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: A-DGN
    value: 1.151
    std: 0.038
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: DRew
    value: 1.243
    std: 0.047
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: PH-DGN
    value: 1.627
    std: 0.398
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GIN
    value: 1.63
    std: 0.161
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GCNII
    value: 2.005
    std: 0.093
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GPS
    value: 2.16
    std: 0.098
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GraphCON
    value: 2.969
    std: 0.189
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GCN
    value: 3.832
    std: 0.262
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
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

