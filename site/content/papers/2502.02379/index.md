---
title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
  Datasets'
arxiv_id: '2502.02379'
source_url: ''
authors: []
published_date: '2025-02-04'
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
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- o
mrr: 0.0034
adjusted_mrr: 0.0011
mrr_dataset_count: 1
benchmark_categories:
- Classic
- TU Dortmund
- OGB
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id008
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8722
    sort_std: 0.0013
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.8672
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.827
    std: 0.009
    paper_value: 0.827
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.821
    std: 0.009
    paper_value: 0.821
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 7
    true_value: 0.821
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.797
    std: 0.021
    paper_value: 0.797
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008899999999999908
    value_note: global 0.8059 within std
    paper_rank: 15
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.572
    std: 0.058
    paper_value: 0.572
    paper_std: 0.058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03400000000000003
    value_note: global 0.6060 within std
    paper_rank: 16
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.563
    std: 0.036
    paper_value: 0.563
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 17
    true_value: 0.563
    true_std: 0.036
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.563
    sort_std: 0.036
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.47
    std: 0.054
    paper_value: 0.47
    paper_std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 26
    true_value: 0.495
    true_std: 0.089
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025000000000000022
    value_note: global 0.4950 within std
    paper_rank: 30
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.495
    sort_std: 0.089
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7995
    std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.732
    std: 0.033
    paper_value: 0.732
    paper_std: 0.033
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 12
    sort_value: 0.732
    sort_std: 0.033
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.724
    std: 0.034
    paper_value: 0.724
    paper_std: 0.034
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 25
    sort_value: 0.724
    sort_std: 0.034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.719
    std: 0.027
    paper_value: 0.719
    paper_std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 61
    sort_value: 0.719
    sort_std: 0.027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.504
    std: 0.021
    paper_value: 0.504
    paper_std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 21
    sort_value: 0.504
    sort_std: 0.021
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.493
    std: 0.023
    paper_value: 0.493
    paper_std: 0.023
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 54
    sort_value: 0.493
    sort_std: 0.023
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.475
    std: 0.047
    paper_value: 0.475
    paper_std: 0.047
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 22
    sort_value: 0.475
    sort_std: 0.047
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.98
    std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15700000000000003
    value_note: ''
    paper_rank: 137
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: null
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.041000000000000036
    value_note: global 0.8940 within std
    paper_rank: 62
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 113
    true_value: 0.7871
    true_std: 0.0751
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.051100000000000034
    value_note: global 0.7871 within std
    paper_rank: 142
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.7871
    sort_std: 0.0751
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 166
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
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.176
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.86
    sort_std: 0.018
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8583
    std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05799999999999994
    value_note: ''
    paper_rank: 50
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.017
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 30
    true_value: 0.802
    true_std: 0.02
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08500000000000008
    value_note: ''
    paper_rank: 72
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.802
    sort_std: 0.02
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 47
    true_value: 0.773
    true_std: 0.025
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22299999999999998
    value_note: ''
    paper_rank: 83
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.773
    sort_std: 0.025
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 84
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
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.492
    sort_std: 0.034
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PROTEINS
  is_multi_metric: true
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    metric_values:
    - 0.854
    - null
    metric_stds:
    - 0.044
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.854
    sort_std: 0.044
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    metric_values:
    - 0.807
    - null
    metric_stds:
    - 0.039
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.807
    sort_std: 0.039
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    metric_values:
    - 0.807
    - null
    metric_stds:
    - 0.039
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
    sort_value: 0.807
    sort_std: 0.039
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GAT
    model_key: gat
    model_plain: GAT
    metric_values:
    - 0.612
    - 0.6
    metric_stds:
    - 0.052
    - 0.015
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7634
    sort_std: 0.0166
    true_value: 0.7634
    true_std: 0.0166
    paper_value: 0.612
    paper_std: 0.052
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15139999999999998
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 28
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.609
    - 0.603
    metric_stds:
    - 0.033
    - 0.011
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.762
    sort_std: 0.028
    true_value: 0.762
    true_std: 0.028
    paper_value: 0.609
    paper_std: 0.033
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15300000000000002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_note: ''
    arxiv_id: ''
    title: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 32
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.593
    - 0.597
    metric_stds:
    - 0.033
    - 0.006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.76
    sort_std: 0.032
    true_value: 0.76
    true_std: 0.032
    paper_value: 0.593
    paper_std: 0.033
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16700000000000004
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 38
  - model: GPS
    model_key: gps
    model_plain: GPS
    metric_values:
    - 0.582
    - null
    metric_stds:
    - 0.049
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.582
    sort_std: 0.049
    true_value: 0.582
    true_std: 0.049
    paper_value: 0.582
    paper_std: 0.049
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 201
  metrics:
  - Accuracy
  - AUROC
  primary_metric: Accuracy
  higher_is_better: true
- &id011
  dataset: QM9
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.02
    sort_std: null
    is_best: true
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.023
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    is_best: false
  - model: cf
    model_key: cf
    model_plain: cf
    value: 0.07
    std: 0.01
    paper_value: 0.07
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 16
    true_value: 0.07
    true_std: 0.01
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.07
    sort_std: 0.01
    is_best: false
  - model: cg
    model_key: cg
    model_plain: cg
    value: 0.39
    std: 0.05
    paper_value: 0.39
    paper_std: 0.05
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 31
    true_value: 0.39
    true_std: 0.05
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.05
    is_best: false
  - model: o
    model_key: o
    model_plain: o
    value: 0.6
    std: 0.02
    paper_value: 0.6
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 43
    true_value: 0.6
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6
    sort_std: 0.02
    is_best: false
  - model: eg
    model_key: eg
    model_plain: eg
    value: 0.65
    std: 0.03
    paper_value: 0.65
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 45
    true_value: 0.65
    true_std: 0.03
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.03
    is_best: false
  - model: rg
    model_key: rg
    model_plain: rg
    value: 0.93
    std: 0.01
    paper_value: 0.93
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 52
    true_value: 0.93
    true_std: 0.01
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.93
    sort_std: 0.01
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 1.44
    std: 0.02
    paper_value: 1.44
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 56
    true_value: 1.44
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.44
    sort_std: 0.02
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: true
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.474
    std: 0.027
    paper_value: 0.474
    paper_std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: null
    sort_value: 0.474
    sort_std: 0.027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.472
    std: 0.017
    paper_value: 0.472
    paper_std: 0.017
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: null
    sort_value: 0.472
    sort_std: 0.017
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.422
    std: 0.021
    paper_value: 0.422
    paper_std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: null
    sort_value: 0.422
    sort_std: 0.021
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: o
    model_key: o
    model_plain: o
    value: 0.8
    std: 0.03
    paper_value: 0.8
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 290
    true_value: 0.8
    true_std: 0.03
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.03
    is_best: false
  - model: o
    model_key: o
    model_plain: o
    value: 0.8
    std: 0.03
    paper_value: 0.8
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 290
    true_value: 0.8
    true_std: 0.03
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.03
    is_best: false
  - model: eg
    model_key: eg
    model_plain: eg
    value: 0.98
    std: 0.03
    paper_value: 0.98
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 293
    true_value: 0.98
    true_std: 0.03
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 293
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98
    sort_std: 0.03
    is_best: false
  - model: eg
    model_key: eg
    model_plain: eg
    value: 0.98
    std: 0.03
    paper_value: 0.98
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 293
    true_value: 0.98
    true_std: 0.03
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 293
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98
    sort_std: 0.03
    is_best: false
  - model: cg
    model_key: cg
    model_plain: cg
    value: 1.31
    std: 0.02
    paper_value: 1.31
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 295
    true_value: 1.31
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 295
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.31
    sort_std: 0.02
    is_best: false
  - model: cg
    model_key: cg
    model_plain: cg
    value: 1.31
    std: 0.02
    paper_value: 1.31
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 295
    true_value: 1.31
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 295
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.31
    sort_std: 0.02
    is_best: false
  - model: rg
    model_key: rg
    model_plain: rg
    value: 1.39
    std: 0.02
    paper_value: 1.39
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 296
    true_value: 1.39
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 296
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.39
    sort_std: 0.02
    is_best: false
  - model: rg
    model_key: rg
    model_plain: rg
    value: 1.39
    std: 0.02
    paper_value: 1.39
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 296
    true_value: 1.39
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 296
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.39
    sort_std: 0.02
    is_best: false
  - model: cf
    model_key: cf
    model_plain: cf
    value: 1.4
    std: 0.02
    paper_value: 1.4
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 297
    true_value: 1.4
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 297
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.4
    sort_std: 0.02
    is_best: false
  - model: cf
    model_key: cf
    model_plain: cf
    value: 1.4
    std: 0.02
    paper_value: 1.4
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 297
    true_value: 1.4
    true_std: 0.02
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 297
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.4
    sort_std: 0.02
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 1.48
    std: 0.01
    paper_value: 1.48
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 298
    true_value: 1.48
    true_std: 0.01
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 298
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.48
    sort_std: 0.01
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 1.48
    std: 0.01
    paper_value: 1.48
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
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 298
    true_value: 1.48
    true_std: 0.01
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 298
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.48
    sort_std: 0.01
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.962
    std: 0.003
    paper_value: 0.962
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 2
    true_value: 0.9682
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006199999999999983
    value_note: ''
    paper_rank: 4
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.967
    std: 0.002
    paper_value: 0.967
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010999999999999899
    value_note: global 0.9681 within std
    paper_rank: 4
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.968
    std: 0.002
    paper_value: 0.968
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: G1
    model_key: g1
    model_plain: G1
    value: 0.8247
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8247
    sort_std: null
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: OGB
  datasets:
  - *id010
- benchmark: Quantum Chemistry
  datasets:
  - *id011
single_proposed_model: o
main_figure: /figures/2502.02379/main_figure.png
---

