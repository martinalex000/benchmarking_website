---
title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
  Datasets'
arxiv_id: '2502.02379'
source_url: ''
authors: []
published_date: Feb 4, 2025
published_date_iso: '2025-02-04'
abstract: 'Benchmark datasets have proved pivotal to the success of graph learning,
  and good benchmark datasets are crucial to guide the development of the field. Recent
  research has highlighted problems with graph-learning datasets and benchmarking
  practices -- revealing, for example, that methods which ignore the graph structure
  can outperform graph-based approaches. Such findings raise two questions: (1) What
  makes a good graph-learning dataset, and (2) how can we evaluate dataset quality
  in graph learning? Our work addresses these questions. As the classic evaluation
  setup uses datasets to evaluate models, it does not apply to dataset evaluation.
  Hence, we start from first principles. Observing that graph-learning datasets uniquely
  combine two modes -- graph structure and node features --, we introduce Rings, a
  flexible and extensible mode-perturbation framework to assess the quality of graph-learning
  datasets based on dataset ablations -- i.e., quantifying differences between the
  original dataset and its perturbed representations. Within this framework, we propose
  two measures -- performance separability and mode complementarity -- as evaluation
  tools, each assessing the capacity of a graph dataset to benchmark the power and
  efficacy of graph-learning methods from a distinct angle. We demonstrate the utility
  of our framework for dataset evaluation via extensive experiments on graph-level
  tasks and derive actionable recommendations for improving the evaluation of graph-learning
  methods. Our work opens new research directions in data-centric graph learning,
  and it constitutes a step toward the systematic evaluation of evaluations.'
codebase_url: https://github.com/aidos-lab/rings
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id003
  dataset: MUTAG
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.939
    std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.939
    sort_std: 0.04
    is_best: true
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.9263
    std: 0.0421
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1901.00596'
    title: A Comprehensive Survey on Graph Neural Networks
    date: Jan 2019
    date_display: Jan 2019
    date_iso: 2019-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9263
    sort_std: 0.0421
    is_best: true
  - model: PS
    model_key: ps
    model_plain: PS
    value: 0.926
    std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_display: Dec 2019
    date_iso: 2019-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.926
    sort_std: 0.042
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.853
    std: 0.087
    paper_value: 0.853
    paper_std: 0.087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 9
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.041000000000000036
    value_note: global 0.8940 within std
    paper_rank: 29
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.736
    std: 0.102
    paper_value: 0.736
    paper_std: 0.102
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 41
    true_value: 0.835
    true_std: 0.025
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.09899999999999998
    value_note: global 0.8350 within std
    paper_rank: 61
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.835
    sort_std: 0.025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.744
    std: 0.099
    paper_value: 0.744
    paper_std: 0.099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 49
    true_value: 0.825
    true_std: 0.021
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.08099999999999996
    value_note: global 0.8250 within std
    paper_rank: 61
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.825
    sort_std: 0.021
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.57
    std: 0.176
    paper_value: 0.57
    paper_std: 0.176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 68
    true_value: 0.57
    true_std: 0.176
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.176
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: NCI1
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.874
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.874
    sort_std: 0.003
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.862
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.004
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.858
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.858
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.769
    std: 0.02
    paper_value: 0.769
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08199999999999996
    value_note: ''
    paper_rank: 38
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.55
    std: 0.055
    paper_value: 0.55
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 5
    true_value: 0.845
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.29499999999999993
    value_note: ''
    paper_rank: 65
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.845
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.717
    std: 0.025
    paper_value: 0.717
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 9
    true_value: 0.832
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11499999999999999
    value_note: ''
    paper_rank: 55
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.005
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.492
    std: 0.034
    paper_value: 0.492
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 66
    true_value: 0.492
    true_std: 0.034
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.492
    sort_std: 0.034
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PROTEINS
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.802
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.795
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.795
    sort_std: 0.01
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.791
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.791
    sort_std: 0.011
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.609
    std: 0.033
    paper_value: 0.609
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 5
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17600000000000005
    value_note: ''
    paper_rank: 80
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.612
    std: 0.052
    paper_value: 0.612
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 7
    true_value: 0.779
    true_std: 0.014
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16700000000000004
    value_note: ''
    paper_rank: 80
    rank_delta: 73
    rank_delta_abs: 73
    rank_delta_direction: worse
    sort_value: 0.779
    sort_std: 0.014
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.033
    paper_value: 0.593
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 12
    true_value: 0.772
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17900000000000005
    value_note: ''
    paper_rank: 82
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.582
    std: 0.049
    paper_value: 0.582
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 83
    true_value: 0.582
    true_std: 0.049
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.582
    sort_std: 0.049
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
main_figure: /figures/2502.02379/main_figure.png
---

