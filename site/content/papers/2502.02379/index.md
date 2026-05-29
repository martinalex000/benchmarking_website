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
- &id002
  dataset: MUTAG
  rows:
  - model: RC-Explainer
    model_key: rc-explainer
    model_plain: RC-Explainer
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_display: Apr 2022
    date_iso: 2022-04
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.983
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.983
    sort_std: 0.025
    is_best: true
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.9805
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: Feb 2022
    date_display: Feb 2022
    date_iso: 2022-02
    codebase_url: https://github.com/chrisjtan/gnn_cff
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9805
    sort_std: null
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
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    global_rank: 59
    true_value: 0.8945
    true_std: 0.0614
    value_gap_source_arxiv: '2506.20362'
    value_gap_source_title: Self-Supervised Graph Learning via Spectral Bootstrapping
      and Laplacian-Based Augmentations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15849999999999997
    value_note: ''
    paper_rank: 323
    rank_delta: 264
    rank_delta_abs: 264
    rank_delta_direction: worse
    sort_value: 0.8945
    sort_std: 0.0614
    is_best: false
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
    global_rank: 62
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '1912.06058'
    value_gap_source_title: Coloring graph neural networks for node disambiguation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.041000000000000036
    value_note: global 0.8940 within std
    paper_rank: 144
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
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
    global_rank: 109
    true_value: 0.872
    true_std: 0.0511
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.128
    value_note: ''
    paper_rank: 317
    rank_delta: 208
    rank_delta_abs: 208
    rank_delta_direction: worse
    sort_value: 0.872
    sort_std: 0.0511
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
    global_rank: 358
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
    paper_rank: 358
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.176
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: NCI1
  rows:
  - model: MSA-AU
    model_key: msa-au
    model_plain: MSA-AU
    value: 0.962
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.962
    sort_std: null
    is_best: true
  - model: MSA-AD
    model_key: msa-ad
    model_plain: MSA-AD
    value: 0.947
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.947
    sort_std: null
    is_best: false
  - model: JbDA
    model_key: jbda
    model_plain: JbDA
    value: 0.912
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10943'
    title: Model Stealing Attack against Graph Classification with Authenticity, Uncertainty
      and Diversity
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.912
    sort_std: null
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
    global_rank: 13
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
    paper_rank: 138
    rank_delta: 125
    rank_delta_abs: 125
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
    global_rank: 15
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
    paper_rank: 225
    rank_delta: 210
    rank_delta_abs: 210
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
    global_rank: 23
    true_value: 0.8365
    true_std: 0.0169
    value_gap_source_arxiv: '1905.04579'
    value_gap_source_title: Are Powerful Graph Neural Nets Necessary? A Dissection
      on Graph Classification
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11950000000000005
    value_note: ''
    paper_rank: 188
    rank_delta: 165
    rank_delta_abs: 165
    rank_delta_direction: worse
    sort_value: 0.8365
    sort_std: 0.0169
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
    global_rank: 232
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
    paper_rank: 232
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
  - model: HGP-SL
    model_key: hgp-sl
    model_plain: HGP-SL
    value: 0.8491
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8491
    sort_std: 0.0162
    is_best: true
  - model: rLap
    model_key: rlap
    model_plain: rLap
    value: 0.8434
    std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8434
    sort_std: 0.0403
    is_best: true
  - model: HGP-SL_DEN
    model_key: hgp-sl_den
    model_plain: HGP-SL_DEN
    value: 0.8312
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8312
    sort_std: 0.0084
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
    global_rank: 38
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
    paper_rank: 331
    rank_delta: 293
    rank_delta_abs: 293
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
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
    global_rank: 47
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
    paper_rank: 330
    rank_delta: 283
    rank_delta_abs: 283
    rank_delta_direction: worse
    sort_value: 0.779
    sort_std: 0.014
    is_best: false
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
    global_rank: 67
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
    paper_rank: 337
    rank_delta: 270
    rank_delta_abs: 270
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
    global_rank: 340
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
    paper_rank: 340
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

