---
title: 'TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous
  Graphs'
arxiv_id: '2406.09639'
source_url: ''
authors: []
published_date: Jun 2024
published_date_iso: 2024-06
abstract: Multi-relational temporal graphs are powerful tools for modeling real-world
  data, capturing the evolving and interconnected nature of entities over time. Recently,
  many novel models are proposed for ML on such graphs intensifying the need for robust
  evaluation and standardized benchmark datasets. However, the availability of such
  resources remains scarce and evaluation faces added complexity due to reproducibility
  issues in experimental protocols. To address these challenges, we introduce Temporal
  Graph Benchmark 2.0, a novel benchmarking framework tailored for evaluating methods
  for predicting future links on Temporal Knowledge Graphs and Temporal Heterogeneous
  Graphs with a focus on large-scale datasets, extending the Temporal Graph Benchmark.
  facilitates comprehensive evaluations by presenting eight novel datasets spanning
  five domains with up to 53 million edges. datasets are significantly larger than
  existing datasets in terms of number of nodes, edges, or timestamps. In addition,
  provides a reproducible and realistic evaluation pipeline for multi-relational temporal
  graphs. Through extensive experimentation, we observe that 1) leveraging edge-type
  information is crucial to obtain high performance, 2) simple heuristic baselines
  are often competitive with more complex methods, 3) most methods fail to run on
  our largest datasets, highlighting the need for research on more scalable methods.
codebase_url: ''
extraction_model: glm-4.7
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- GraphBench
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id001
  dataset: SAT Solving
  rows:
  - model: CEN
    model_key: cen
    model_plain: CEN
    value: 0.612
    std: 0.001
    paper_value: 0.612
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.612
    sort_std: 0.001
    is_best: true
  - model: RecB_train
    model_key: recb_train
    model_plain: RecB_train
    value: 0.605
    std: null
    paper_value: 0.605
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gastinger et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.605
    sort_std: null
    is_best: false
  - model: TLogic
    model_key: tlogic
    model_plain: TLogic
    value: 0.595
    std: 0.001
    paper_value: 0.595
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.595
    sort_std: 0.001
    is_best: false
  - model: RE-GCN
    model_key: re-gcn
    model_plain: RE-GCN
    value: 0.594
    std: 0.001
    paper_value: 0.594
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li et al. 2021
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.594
    sort_std: 0.001
    is_best: false
  - model: RecB_default
    model_key: recb_default
    model_plain: RecB_default
    value: 0.486
    std: null
    paper_value: 0.486
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gastinger et al. 2024
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.486
    sort_std: null
    is_best: false
  - model: EdgeBank_tw
    model_key: edgebank_tw
    model_plain: EdgeBank_tw
    value: 0.353
    std: null
    paper_value: 0.353
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Poursafaei et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.353
    sort_std: null
    is_best: false
  - model: EdgeBank_inf
    model_key: edgebank_inf
    model_plain: EdgeBank_inf
    value: 0.333
    std: null
    paper_value: 0.333
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Poursafaei et al. 2022
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.333
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GraphBench
  datasets:
  - *id001
main_figure: /figures/2406.09639/main_figure.png
---

