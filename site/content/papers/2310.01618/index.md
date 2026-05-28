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
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- PIGN + GCN
- PIGN + GAT
- PIGN + GraphSAGE
- PIGN with GCN
- PIGN with GAT
mrr: 0.0103
adjusted_mrr: 0.0034
mrr_dataset_count: 1
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
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10089999999999999
    value_note: ''
    paper_rank: 125
    rank_delta: 113
    rank_delta_abs: 113
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10620000000000007
    value_note: ''
    paper_rank: 138
    rank_delta: 119
    rank_delta_abs: 119
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 148
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
    paper_rank: 148
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 160
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
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.661
    sort_std: 0.017
    is_best: false
  - model: IterGNN with GCN
    model_key: itergnn with gcn
    model_plain: IterGNN with GCN
    value: 0.4991
    std: 0.0494
    paper_value: 0.4991
    paper_std: 0.0494
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 213
    true_value: 0.4991
    true_std: 0.0494
    value_gap_source_arxiv: '2310.01618'
    value_gap_source_title: 'Operator Learning Meets Numerical Analysis: Improving
      Neural Networks through Iterative Methods'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4991
    sort_std: 0.0494
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0784999999999999
    value_note: ''
    paper_rank: 151
    rank_delta: 120
    rank_delta_abs: 120
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06879999999999997
    value_note: ''
    paper_rank: 151
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 165
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
    paper_rank: 165
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 185
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
    paper_rank: 185
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 282
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
    paper_rank: 282
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
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
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
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.356
    sort_std: 0.0037
    is_best: false
  - model: GraphSAGE (w/o iterations)
    model_key: graphsage (w/o iterations)
    model_plain: GraphSAGE (w/o iterations)
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 73
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
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3015
    sort_std: 0.0032
    is_best: false
  - model: PIGN + GCN
    model_key: pign + gcn
    model_plain: PIGN + GCN
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 97
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
    paper_rank: 97
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 98
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
    paper_rank: 98
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 100
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
    paper_rank: 100
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 101
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
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1706
    sort_std: 0.0046
    is_best: false
  - model: GCN (w/o iterations)
    model_key: gcn (w/o iterations)
    model_plain: GCN (w/o iterations)
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
    source_ref: Kipf 2017
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 110
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
    paper_rank: 110
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
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 113
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
    paper_rank: 113
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

