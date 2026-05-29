---
title: 'Operator Learning Meets Numerical Analysis: Improving Neural Networks through
  Iterative Methods'
arxiv_id: '2310.01618'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: Deep neural networks, despite their success in numerous applications, often
  function without established theoretical foundations. In this paper, we bridge this
  gap by drawing parallels between deep learning and classical numerical analysis.
  By framing neural networks as operators with fixed points representing desired solutions,
  we develop a theoretical framework grounded in iterative methods for operator equations.
  Under defined conditions, we present convergence proofs based on fixed point theory.
  We demonstrate that popular architectures, such as diffusion models and AlphaFold,
  inherently employ iterative operator learning. Empirical assessments highlight that
  performing iterations through network operators improves performance. We also introduce
  an iterative graph neural network, PIGN, that further demonstrates benefits of iterations.
  Our work aims to enhance the understanding of deep learning by merging insights
  from numerical analysis, potentially guiding the design of future networks with
  clearer theoretical underpinnings and improved performance.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- PIGN
- PIGN + GAT
- PIGN + GraphSAGE
- PIGN with GCN
- PIGN with GAT
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Classic
- LRGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: CiteSeer
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.758
    std: 0.008
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
    sort_value: 0.758
    sort_std: 0.008
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.742
    std: 0.009
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
    sort_value: 0.742
    sort_std: 0.009
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.735
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
    sort_value: 0.735
    sort_std: 0.011
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.699
    std: 0.01
    paper_value: 0.699
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.728
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029000000000000026
    value_note: ''
    paper_rank: 7
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.728
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.713
    std: 0.006
    paper_value: 0.713
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.721
    true_std: 0.015
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.7210 within std
    paper_rank: 7
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.721
    sort_std: 0.015
    is_best: false
  - model: PIGN with GCN
    model_key: pign with gcn
    model_plain: PIGN with GCN
    value: 0.684
    std: 0.015
    paper_value: 0.684
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.684
    true_std: 0.015
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.684
    sort_std: 0.015
    is_best: false
  - model: PIGN with GAT
    model_key: pign with gat
    model_plain: PIGN with GAT
    value: 0.661
    std: 0.017
    paper_value: 0.661
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.661
    true_std: 0.017
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.661
    sort_std: 0.017
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.842
    std: 0.003
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
    global_rank: 1
    sort_value: 0.842
    sort_std: 0.003
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.835
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
    sort_value: 0.835
    sort_std: 0.004
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.804
    std: 0.011
    paper_value: 0.804
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.83
    true_std: 0.008
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025999999999999912
    value_note: ''
    paper_rank: 6
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.83
    sort_std: 0.008
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.828
    std: 0.007
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
    global_rank: 4
    sort_value: 0.828
    sort_std: 0.007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.809
    std: 0.006
    paper_value: 0.809
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.815
    true_std: 0.005
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005999999999999894
    value_note: global 0.8150 within std
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.815
    sort_std: 0.005
    is_best: false
  - model: PIGN with GAT
    model_key: pign with gat
    model_plain: PIGN with GAT
    value: 0.792
    std: 0.009
    paper_value: 0.792
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.792
    true_std: 0.009
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.009
    is_best: false
  - model: PIGN with GCN
    model_key: pign with gcn
    model_plain: PIGN with GCN
    value: 0.767
    std: 0.014
    paper_value: 0.767
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.767
    true_std: 0.014
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.014
    is_best: false
  - model: IterGNN with GCN
    model_key: itergnn with gcn
    model_plain: IterGNN with GCN
    value: 0.605
    std: 0.175
    paper_value: 0.605
    paper_std: 0.175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.605
    true_std: 0.175
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.175
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PascalVOC-SP
  rows:
  - model: PIGN + GraphSAGE
    model_key: pign + graphsage
    model_plain: PIGN + GraphSAGE
    value: 0.356
    std: 0.0037
    paper_value: 0.356
    paper_std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 1
    true_value: 0.356
    true_std: 0.0037
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.356
    sort_std: 0.0037
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3015
    std: 0.0032
    paper_value: 0.3015
    paper_std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 2
    true_value: 0.3015
    true_std: 0.0032
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3015
    sort_std: 0.0032
    is_best: false
  - model: PIGN
    model_key: pign
    model_plain: PIGN
    value: 0.1831
    std: 0.0038
    paper_value: 0.1831
    paper_std: 0.0038
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.1831
    true_std: 0.0038
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1831
    sort_std: 0.0038
    is_best: false
  - model: IterGNN + GraphSAGE
    model_key: itergnn + graphsage
    model_plain: IterGNN + GraphSAGE
    value: 0.1816
    std: 0.0014
    paper_value: 0.1816
    paper_std: 0.0014
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.1816
    true_std: 0.0014
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1816
    sort_std: 0.0014
    is_best: false
  - model: IterGNN + GCN
    model_key: itergnn + gcn
    model_plain: IterGNN + GCN
    value: 0.1736
    std: 0.0311
    paper_value: 0.1736
    paper_std: 0.0311
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.1736
    true_std: 0.0311
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1736
    sort_std: 0.0311
    is_best: false
  - model: PIGN + GAT
    model_key: pign + gat
    model_plain: PIGN + GAT
    value: 0.1706
    std: 0.0046
    paper_value: 0.1706
    paper_std: 0.0046
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.1706
    true_std: 0.0046
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1706
    sort_std: 0.0046
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.151
    std: 0.0029
    paper_value: 0.151
    paper_std: 0.0029
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.151
    true_std: 0.0029
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.151
    sort_std: 0.0029
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.1204
    std: 0.0127
    paper_value: 0.1204
    paper_std: 0.0127
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.1204
    true_std: 0.0127
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1204
    sort_std: 0.0127
    is_best: false
  - model: IterGNN + GAT
    model_key: itergnn + gat
    model_plain: IterGNN + GAT
    value: 0.1099
    std: 0.0459
    paper_value: 0.1099
    paper_std: 0.0459
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.1099
    true_std: 0.0459
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1099
    sort_std: 0.0459
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
main_figure: /figures/2310.01618/main_figure.png
---

