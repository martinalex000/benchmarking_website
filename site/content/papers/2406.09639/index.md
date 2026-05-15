---
title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
  Graphs'
arxiv_id: '2406.09639'
authors: []
published_date: Jun 2024
abstract: Multi-relational temporal graphs are powerful tools for modeling real-world
  data, capturing the evolving and interconnected nature of entities over time. Recently,
  many novel models are proposed for ML on such graphs intensifying the need for robust
  evaluation and standardized benchmark datasets. However, the availability of such
  resources remains scarce and evaluation faces added complexity due to reproducibility
  issues in experimental protocols. To address these challenges, we introduce Temporal
  Graph Benchmark~2.0 ( ), a novel benchmarking framework tailored for evaluating
  methods for predicting future links on Temporal Knowledge Graphs and Temporal Heterogeneous
  Graphs with a focus on large-scale datasets, extending the Temporal Graph Benchmark.
  facilitates comprehensive evaluations by presenting eight novel datasets spanning
  five domains with up to 53 million edges. datasets are significantly larger than
  existing datasets in terms of number of nodes, edges, or timestamps. In addition,
  provides a reproducible and realistic evaluation pipeline for multi-relational temporal
  graphs. Through extensive experimentation, we observe that 1)~leveraging edge-type
  information is crucial to obtain high performance, 2)~simple heuristic baselines
  are often competitive with more complex methods, 3)~most methods fail to run on
  our largest datasets, highlighting the need for research on more scalable methods.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models: []
mrr: null
results:
- &id001
  dataset: SAT Solving
  rows:
  - model: CEN
    value: 0.612
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li et al. 2022
    global_rank: null
    is_best: true
  - model: RecB_train
    value: 0.605
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gastinger et al. 2024
    global_rank: null
    is_best: false
  - model: TLogic
    value: 0.595
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    global_rank: null
    is_best: false
  - model: RE-GCN
    value: 0.594
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li et al. 2021
    global_rank: null
    is_best: false
  - model: RecB_default
    value: 0.486
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gastinger et al. 2024
    global_rank: null
    is_best: false
  - model: EdgeBank_tw
    value: 0.353
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Poursafaei et al. 2022
    global_rank: null
    is_best: false
  - model: EdgeBank_inf
    value: 0.333
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Poursafaei et al. 2022
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GraphBench
  datasets:
  - *id001
main_figure: /figures/2406.09639/main_figure.png
---

