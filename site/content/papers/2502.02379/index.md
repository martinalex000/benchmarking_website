---
title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
  Datasets'
arxiv_id: '2502.02379'
authors: []
published_date: '2025-02-04'
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
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- o
mrr: 0.0036
results:
- &id008
  dataset: COLLAB
  rows:
  - model: CoCN expanded
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: nsqure~
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: CoCN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GCN
    value: 0.827
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GAT
    value: 0.821
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GIN
    value: 0.797
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 14
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: PathNN-SP (K=2)
    value: 0.704
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SPN(k=5)
    value: 0.694
    std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.572
    std: 0.058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GCN
    value: 0.563
    std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GAT
    value: 0.47
    std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 22
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: IMDB-BINARY
  rows:
  - model: GPM
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: RUM
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: nsqure~
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GCN
    value: 0.732
    std: 0.033
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GIN
    value: 0.724
    std: 0.034
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: GAT
    value: 0.719
    std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 55
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: DMON
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SEP
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GCN
    value: 0.504
    std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.493
    std: 0.023
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GIN
    value: 0.475
    std: 0.047
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 20
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: MUTAG
  rows:
  - model: PR-MPNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: IPR-MPNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.767
    std: 0.14
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: GCN
    value: 0.718
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.707
    std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 104
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: NCI1
  rows:
  - model: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via - High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: CoCN expanded
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.846
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.769
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GCN
    value: 0.72
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GAT
    value: 0.562
    std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 40
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    value: 0.854
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: PR-MPNN
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.603
    std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: GAT
    value: 0.6
    std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GCN
    value: 0.597
    std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 37
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: QM9
  rows:
  - model: Mace
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
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: DropGIN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: ESA
    value: 0.02578744427174226
    std: 0.000867405321348238
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: cf
    value: 0.07
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: cg
    value: 0.39
    std: 0.05
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: o
    value: 0.6
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: eg
    value: 0.65
    std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: rg
    value: 0.93
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: rf
    value: 1.44
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 35
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GIN
    value: 0.474
    std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN
    value: 0.472
    std: 0.017
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT
    value: 0.422
    std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ESA (PE)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PST
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: o
    value: 0.8
    std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 275
    is_best: false
  - model: eg
    value: 0.98
    std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 278
    is_best: false
  - model: cg
    value: 1.31
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 280
    is_best: false
  - model: rg
    value: 1.39
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 281
    is_best: false
  - model: cf
    value: 1.4
    std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 282
    is_best: false
  - model: rf
    value: 1.48
    std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 283
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: ogbg-molhiv
  rows:
  - model: MLP
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GIN
    value: 0.968
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GCN
    value: 0.967
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: GAT
    value: 0.962
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: SigGate-GT
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
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: G1
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
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 6
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

