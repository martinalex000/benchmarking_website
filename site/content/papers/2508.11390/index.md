---
title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature based
  Graph-to-Hypergraph Structural Lifting
arxiv_id: '2508.11390'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
abstract: Graph Neural Networks are highly eﬀective at learning from relational data,
  leveraging node and edge features while maintaining the symmetries inherent to graph
  structures. However, many real-world systems—such as social or biological networks—exhibit
  complex interactions that are more naturally represented by higher-order topological
  domains. The emerging field of Geometric and Topological Deep Learning addresses
  this challenge by introducing methods that utilize and benefit from higher-order
  structures. Central to TDL is the concept of lifting, which transforms data representations
  from basic graph forms to more expressive topologies before the application of GNN
  models for learning. In this work, we propose a structural lifting strategy using
  Forman-Ricci curvature, which defines an edge-based network characteristic based
  on Riemannian geometry. Curvature reveals local and global properties of a graph
  such as to identify a network’s backbones, i.e., coarse, structure-preserving graph
  geometries that form connections between major communities — most suitably represented
  as hyperedges to model information flows between clusters across large distances
  in the network. To this end, our approach provides a remedy to the problem of information
  distortion in message passing across long distances and graph bottlenecks—a phenomenon
  known in graph learning as over-squashing.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- UniGNN2
- UniGNN2 (Ric_F)
mrr: 0.0088
adjusted_mrr: 0.0088
mrr_dataset_count: 3
benchmark_categories:
- TU Dortmund
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id002
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7
    std: 0.03
    paper_value: 0.7
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.802
    true_std: 0.02
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10200000000000009
    value_note: ''
    paper_rank: 78
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.802
    sort_std: 0.02
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.71
    std: 0.04
    paper_value: 0.71
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 51
    true_value: 0.773
    true_std: 0.025
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06300000000000006
    value_note: ''
    paper_rank: 78
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.773
    sort_std: 0.025
    is_best: false
  - model: AST
    model_key: ast
    model_plain: AST
    value: 0.7
    std: 0.06
    paper_value: 0.7
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 79
    true_value: 0.7
    true_std: 0.06
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.06
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.68
    std: 0.09
    paper_value: 0.68
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 81
    true_value: 0.68
    true_std: 0.09
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.09
    is_best: false
  - model: UniGNN2
    model_key: unignn2
    model_plain: UniGNN2
    value: 0.67
    std: 0.09
    paper_value: 0.67
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 84
    true_value: 0.67
    true_std: 0.09
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.09
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
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
    global_rank: 3
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.69
    std: 0.04
    paper_value: 0.69
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
    true_value: 0.7634
    true_std: 0.0166
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07340000000000002
    value_note: ''
    paper_rank: 185
    rank_delta: 157
    rank_delta_abs: 157
    rank_delta_direction: worse
    sort_value: 0.7634
    sort_std: 0.0166
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.69
    std: 0.04
    paper_value: 0.69
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07000000000000006
    value_note: ''
    paper_rank: 185
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: UniGNN2
    model_key: unignn2
    model_plain: UniGNN2
    value: 0.69
    std: 0.06
    paper_value: 0.69
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 186
    true_value: 0.69
    true_std: 0.06
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 186
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.06
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.67
    std: 0.07
    paper_value: 0.67
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 191
    true_value: 0.67
    true_std: 0.07
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.07
    is_best: false
  - model: AST
    model_key: ast
    model_plain: AST
    value: 0.66
    std: 0.08
    paper_value: 0.66
    paper_std: 0.08
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 193
    true_value: 0.66
    true_std: 0.08
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.66
    sort_std: 0.08
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
    value: 0.77
    std: 0.17
    paper_value: 0.77
    paper_std: 0.17
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.9682
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19819999999999993
    value_note: ''
    paper_rank: 140
    rank_delta: 138
    rank_delta_abs: 138
    rank_delta_direction: worse
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.78
    std: 0.14
    paper_value: 0.78
    paper_std: 0.14
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18809999999999993
    value_note: ''
    paper_rank: 104
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.968
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
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
  - model: GCN (Ric_F)
    model_key: gcn (ric_f)
    model_plain: GCN (Ric_F)
    value: 0.79
    std: 0.13
    paper_value: 0.79
    paper_std: 0.13
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 67
    true_value: 0.79
    true_std: 0.13
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.13
    is_best: false
  - model: AST (Ric_F)
    model_key: ast (ric_f)
    model_plain: AST (Ric_F)
    value: 0.79
    std: 0.19
    paper_value: 0.79
    paper_std: 0.19
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 68
    true_value: 0.79
    true_std: 0.19
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.19
    is_best: true
  - model: AST
    model_key: ast
    model_plain: AST
    value: 0.78
    std: 0.2
    paper_value: 0.78
    paper_std: 0.2
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 108
    true_value: 0.78
    true_std: 0.2
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.2
    is_best: true
  - model: UniGNN2
    model_key: unignn2
    model_plain: UniGNN2
    value: 0.78
    std: 0.15
    paper_value: 0.78
    paper_std: 0.15
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 109
    true_value: 0.78
    true_std: 0.15
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.15
    is_best: false
  - model: EDGNN (Ric_F)
    model_key: edgnn (ric_f)
    model_plain: EDGNN (Ric_F)
    value: 0.78
    std: 0.16
    paper_value: 0.78
    paper_std: 0.16
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 110
    true_value: 0.78
    true_std: 0.16
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.16
    is_best: false
  - model: UniGNN2 (Ric_F)
    model_key: unignn2 (ric_f)
    model_plain: UniGNN2 (Ric_F)
    value: 0.78
    std: 0.16
    paper_value: 0.78
    paper_std: 0.16
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 111
    true_value: 0.78
    true_std: 0.16
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.16
    is_best: false
  - model: GAT (Ric_F)
    model_key: gat (ric_f)
    model_plain: GAT (Ric_F)
    value: 0.77
    std: 0.17
    paper_value: 0.77
    paper_std: 0.17
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 143
    true_value: 0.77
    true_std: 0.17
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.17
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.76
    std: 0.17
    paper_value: 0.76
    paper_std: 0.17
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 165
    true_value: 0.76
    true_std: 0.17
    value_gap_source_arxiv: '2508.11390'
    value_gap_source_title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci
      Curvature based Graph-to-Hypergraph Structural Lifting
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.17
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
- benchmark: OGB
  datasets:
  - *id003
main_figure: /figures/2508.11390/main_figure.png
---

