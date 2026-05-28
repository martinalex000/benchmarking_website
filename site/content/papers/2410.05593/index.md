---
title: When Graph Neural Networks Meet Dynamic Mode Decomposition
arxiv_id: '2410.05593'
source_url: ''
authors: []
published_date: Oct 2024
published_date_iso: 2024-10
abstract: Graph Neural Networks (GNNs) have emerged as fundamental tools for a wide
  range of prediction tasks on graph-structured data. Recent studies have drawn analogies
  between GNN feature propagation and diffusion processes, which can be interpreted
  as dynamical systems. In this paper, we delve deeper into this perspective by connecting
  the dynamics in GNNs to modern Koopman theory and its numerical method, Dynamic
  Mode Decomposition (DMD). We illustrate how DMD can estimate a low-rank, finite-dimensional
  linear operator based on multiple states of the system, effectively approximating
  potential nonlinear interactions between nodes in the graph. This approach allows
  us to capture complex dynamics within the graph accurately and efficiently. We theoretically
  establish a connection between the DMD-estimated operator and the original dynamic
  operator between system states. Building upon this foundation, we introduce a family
  of DMD-GNN models that effectively leverage the low-rank eigenfunctions provided
  by the DMD algorithm. We further discuss the potential of enhancing our approach
  by incorporating domain-specific constraints such as symmetry into the DMD computation,
  allowing the corresponding GNN models to respect known physical properties of the
  underlying system. Our work paves the path for applying advanced dynamical system
  analysis tools via GNNs. We validate our approach through extensive experiments
  on various learning tasks, including directed graphs, large-scale graphs, long-range
  interactions, and spatial-temporal graphs. We also empirically verify that our proposed
  models can serve as powerful encoders for link prediction tasks. The results demonstrate
  that our DMD-enhanced GNNs achieve state-of-the-art performance, highlighting the
  effectiveness of integrating DMD into GNN frameworks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- DMD-GCN
- DMD-SGC
- DMD++
- DMD-ACMP
mrr: 0.1541
adjusted_mrr: 0.1541
mrr_dataset_count: 9
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- OGB
- DualEquiNet RNA Benchmarks
task_categories:
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id008
  dataset: COCO-SP
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.4901
    std: null
    metric: F1
    higher_is_better: true
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
    sort_value: 0.4901
    sort_std: null
    is_best: true
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.4752
    std: 0.0032
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
    global_rank: 2
    sort_value: 0.4752
    sort_std: 0.0032
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.079
    std: 0.025
    paper_value: 0.079
    paper_std: 0.025
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19429999999999997
    value_note: ''
    paper_rank: 78
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.2733
    sort_std: 0.0041
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.091
    std: 0.009
    paper_value: 0.091
    paper_std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 74
    true_value: 0.091
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.091
    sort_std: 0.009
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.083
    std: 0.012
    paper_value: 0.083
    paper_std: 0.012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 77
    true_value: 0.083
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.083
    sort_std: 0.012
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.081
    std: 0.015
    paper_value: 0.081
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 78
    true_value: 0.081
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.081
    sort_std: 0.015
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.056
    std: 0.011
    paper_value: 0.056
    paper_std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 80
    true_value: 0.056
    true_std: 0.011
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.056
    sort_std: 0.011
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.044
    std: 0.015
    paper_value: 0.044
    paper_std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 81
    true_value: 0.044
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.015
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.031
    std: 0.016
    paper_value: 0.031
    paper_std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 84
    true_value: 0.0315
    true_std: 0.0031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.0315 within std
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0315
    sort_std: 0.0031
    is_best: false
  metric: F1
  higher_is_better: true
- &id010
  dataset: COVID
  rows:
  - model: DualEquiNet
    model_key: dualequinet
    model_plain: DualEquiNet
    value: 0.353
    std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.353
    sort_std: 0.006
    is_best: true
  - model: w/o CSIP
    model_key: w/o csip
    model_plain: w/o CSIP
    value: 0.356
    std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.356
    sort_std: 0.002
    is_best: true
  - model: w/o CSIP/Cross
    model_key: w/o csip/cross
    model_plain: w/o CSIP/Cross
    value: 0.356
    std: 0.013
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.356
    sort_std: 0.013
    is_best: true
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.76
    std: 0.025
    paper_value: 0.76
    paper_std: 0.025
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.76
    sort_std: 0.025
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.784
    std: 0.013
    paper_value: 0.784
    paper_std: 0.013
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.784
    sort_std: 0.013
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.805
    std: 0.067
    paper_value: 0.805
    paper_std: 0.067
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.805
    sort_std: 0.067
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.809
    std: 0.011
    paper_value: 0.809
    paper_std: 0.011
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.809
    sort_std: 0.011
    is_best: false
  - model: GAT-kNN
    model_key: gat-knn
    model_plain: GAT-kNN
    value: 0.861
    std: 0.045
    paper_value: 0.861
    paper_std: 0.045
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.861
    sort_std: 0.045
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.938
    std: 0.081
    paper_value: 0.938
    paper_std: 0.081
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.938
    sort_std: 0.081
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.956
    std: 0.029
    paper_value: 0.956
    paper_std: 0.029
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.956
    sort_std: 0.029
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.956
    std: 0.034
    paper_value: 0.956
    paper_std: 0.034
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.956
    sort_std: 0.034
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.991
    std: 0.078
    paper_value: 0.991
    paper_std: 0.078
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.991
    sort_std: 0.078
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 1.052
    std: 0.081
    paper_value: 1.052
    paper_std: 0.081
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 1.052
    sort_std: 0.081
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 1.271
    std: 0.073
    paper_value: 1.271
    paper_std: 0.073
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 1.271
    sort_std: 0.073
    is_best: false
  - model: GCN-kNN
    model_key: gcn-knn
    model_plain: GCN-kNN
    value: 1.475
    std: 0.028
    paper_value: 1.475
    paper_std: 0.028
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 1.475
    sort_std: 0.028
    is_best: false
  metric: RMSE
  higher_is_better: false
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
    value: 0.709
    std: 0.005
    paper_value: 0.709
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1049
    value_note: ''
    paper_rank: 129
    rank_delta: 117
    rank_delta_abs: 117
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.731
    std: 0.004
    paper_value: 0.731
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 16
    true_value: 0.809
    true_std: 0.0121
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07800000000000007
    value_note: ''
    paper_rank: 110
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.809
    sort_std: 0.0121
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.72
    std: 0.007
    paper_value: 0.72
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08520000000000005
    value_note: ''
    paper_rank: 122
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.759
    std: 0.012
    paper_value: 0.759
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.8012
    true_std: 0.0083
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042200000000000015
    value_note: ''
    paper_rank: 68
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0083
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.591
    std: 0.005
    paper_value: 0.591
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.7939
    true_std: 0.0138
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20290000000000008
    value_note: ''
    paper_rank: 203
    rank_delta: 172
    rank_delta_abs: 172
    rank_delta_direction: worse
    sort_value: 0.7939
    sort_std: 0.0138
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.759
    std: 0.006
    paper_value: 0.759
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.7933
    true_std: 0.0035
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0343
    value_note: ''
    paper_rank: 68
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0035
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.732
    std: 0.004
    paper_value: 0.732
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 110
    true_value: 0.732
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.004
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.73
    std: 0.021
    paper_value: 0.73
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 112
    true_value: 0.73
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.021
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.726
    std: 0.008
    paper_value: 0.726
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 114
    true_value: 0.726
    true_std: 0.008
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.008
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.714
    std: 0.026
    paper_value: 0.714
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 125
    true_value: 0.714
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.026
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.71
    std: 0.006
    paper_value: 0.71
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 129
    true_value: 0.71
    true_std: 0.006
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.006
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.708
    std: 0.011
    paper_value: 0.708
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 130
    true_value: 0.708
    true_std: 0.011
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.011
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.672
    std: 0.01
    paper_value: 0.672
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 134
    true_value: 0.7056
    true_std: 0.0058
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03359999999999996
    value_note: ''
    paper_rank: 151
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.7056
    sort_std: 0.0058
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.838
    std: 0.009
    paper_value: 0.838
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047700000000000076
    value_note: ''
    paper_rank: 115
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.83
    std: 0.007
    paper_value: 0.83
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05249999999999999
    value_note: ''
    paper_rank: 129
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.835
    std: 0.007
    paper_value: 0.835
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04500000000000004
    value_note: ''
    paper_rank: 118
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.834
    std: 0.005
    paper_value: 0.834
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    true_value: 0.8796
    true_std: 0.0037
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.045600000000000085
    value_note: ''
    paper_rank: 120
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.8796
    sort_std: 0.0037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.815
    std: 0.005
    paper_value: 0.815
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06280000000000008
    value_note: ''
    paper_rank: 147
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.551
    std: 0.013
    paper_value: 0.551
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 65
    true_value: 0.8709
    true_std: 0.0066
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.31989999999999996
    value_note: ''
    paper_rank: 294
    rank_delta: 229
    rank_delta_abs: 229
    rank_delta_direction: worse
    sort_value: 0.8709
    sort_std: 0.0066
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.841
    std: 0.004
    paper_value: 0.841
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 111
    true_value: 0.841
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.004
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.745
    std: 0.008
    paper_value: 0.745
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 117
    true_value: 0.836
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09099999999999997
    value_note: ''
    paper_rank: 203
    rank_delta: 86
    rank_delta_abs: 86
    rank_delta_direction: worse
    sort_value: 0.836
    sort_std: null
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.833
    std: 0.005
    paper_value: 0.833
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 123
    true_value: 0.833
    true_std: 0.005
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.833
    sort_std: 0.005
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.829
    std: 0.014
    paper_value: 0.829
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 130
    true_value: 0.829
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.829
    sort_std: 0.014
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.829
    std: 0.009
    paper_value: 0.829
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 131
    true_value: 0.829
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.829
    sort_std: 0.009
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.826
    std: 0.007
    paper_value: 0.826
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 134
    true_value: 0.826
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.007
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.823
    std: 0.003
    paper_value: 0.823
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 140
    true_value: 0.823
    true_std: 0.003
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.898
    std: 0.006
    paper_value: 0.898
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 8
    true_value: 0.918
    true_std: 0.0063
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 13
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.0063
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.914
    std: 0.017
    paper_value: 0.914
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.914
    true_std: 0.017
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.914
    sort_std: 0.017
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.85
    std: 0.052
    paper_value: 0.85
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.9136
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06359999999999999
    value_note: ''
    paper_rank: 21
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9136
    sort_std: 0.007
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    paper_value: 0.913
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.881
    std: 0.024
    paper_value: 0.881
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.881
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.881
    sort_std: 0.024
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.851
    std: 0.064
    paper_value: 0.851
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.8623
    true_std: 0.0471
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011299999999999977
    value_note: global 0.8623 within std
    paper_rank: 21
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8623
    sort_std: 0.0471
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.836
    std: 0.031
    paper_value: 0.836
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 23
    true_value: 0.836
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.836
    sort_std: 0.031
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.665
    std: 0.138
    paper_value: 0.665
    paper_std: 0.138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15959999999999996
    value_note: ''
    paper_rank: 81
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.8
    std: 0.019
    paper_value: 0.8
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 31
    true_value: 0.8
    true_std: 0.019
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.019
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.76
    std: 0.01
    paper_value: 0.76
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.756
    std: 0.032
    paper_value: 0.756
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 39
    true_value: 0.756
    true_std: 0.032
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.032
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.726
    std: 0.003
    paper_value: 0.726
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 50
    true_value: 0.726
    true_std: 0.003
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.003
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.714
    std: 0.012
    paper_value: 0.714
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 54
    true_value: 0.714
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.238
    std: 0.016
    paper_value: 0.238
    paper_std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.138
    value_note: ''
    paper_rank: 91
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.243
    std: 0.014
    paper_value: 0.243
    paper_std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 90
    true_value: 0.243
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.243
    sort_std: 0.014
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.241
    std: 0.017
    paper_value: 0.241
    paper_std: 0.017
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 91
    true_value: 0.241
    true_std: 0.017
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.241
    sort_std: 0.017
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.217
    std: 0.036
    paper_value: 0.217
    paper_std: 0.036
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 93
    true_value: 0.217
    true_std: 0.036
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.217
    sort_std: 0.036
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.216
    std: 0.039
    paper_value: 0.216
    paper_std: 0.039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 94
    true_value: 0.216
    true_std: 0.039
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.216
    sort_std: 0.039
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.152
    std: 0.024
    paper_value: 0.152
    paper_std: 0.024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 104
    true_value: 0.152
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.152
    sort_std: 0.024
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.114
    std: 0.023
    paper_value: 0.114
    paper_std: 0.023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 112
    true_value: 0.114
    true_std: 0.023
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.114
    sort_std: 0.023
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.714
    std: 0.004
    paper_value: 0.714
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.9476
    true_std: 0.001
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23360000000000003
    value_note: ''
    paper_rank: 153
    rank_delta: 150
    rank_delta_abs: 150
    rank_delta_direction: worse
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: ND
    model_key: nd
    model_plain: ND
    value: 0.9256
    std: 0.0071
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    sort_value: 0.9256
    sort_std: 0.0071
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.79
    std: 0.003
    paper_value: 0.79
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13239999999999996
    value_note: ''
    paper_rank: 123
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.785
    std: 0.003
    paper_value: 0.785
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1351
    value_note: ''
    paper_rank: 124
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.792
    std: 0.003
    paper_value: 0.792
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 34
    true_value: 0.895
    true_std: 0.004
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10299999999999998
    value_note: ''
    paper_rank: 121
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.004
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.798
    std: 0.008
    paper_value: 0.798
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 37
    true_value: 0.8934
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09539999999999993
    value_note: ''
    paper_rank: 117
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.8934
    sort_std: 0.0025
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.792
    std: 0.015
    paper_value: 0.792
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 55
    true_value: 0.8864
    true_std: 0.0009
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09439999999999993
    value_note: ''
    paper_rank: 121
    rank_delta: 66
    rank_delta_abs: 66
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.0009
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.79
    std: 0.003
    paper_value: 0.79
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 58
    true_value: 0.8843
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09429999999999994
    value_note: ''
    paper_rank: 123
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.8843
    sort_std: 0.0015
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.812
    std: 0.015
    paper_value: 0.812
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 114
    true_value: 0.812
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.015
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.799
    std: 0.007
    paper_value: 0.799
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 117
    true_value: 0.799
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.799
    sort_std: 0.007
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.794
    std: 0.004
    paper_value: 0.794
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 118
    true_value: 0.794
    true_std: 0.004
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.004
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.794
    std: 0.014
    paper_value: 0.794
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 119
    true_value: 0.794
    true_std: 0.014
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.014
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.793
    std: 0.009
    paper_value: 0.793
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 120
    true_value: 0.793
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.009
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.768
    std: 0.006
    paper_value: 0.768
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 126
    true_value: 0.7726
    true_std: 0.0034
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0045999999999999375
    value_note: global 0.7726 within std
    paper_rank: 127
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7726
    sort_std: 0.0034
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.759
    std: 0.062
    paper_value: 0.759
    paper_std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.9295
    true_std: 0.0131
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17049999999999998
    value_note: ''
    paper_rank: 86
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.9295
    sort_std: 0.0131
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.926
    std: 0.034
    paper_value: 0.926
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.926
    true_std: 0.034
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.926
    sort_std: 0.034
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.923
    std: 0.007
    paper_value: 0.923
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.923
    sort_std: 0.007
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.859
    std: 0.046
    paper_value: 0.859
    paper_std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.9189
    true_std: 0.0393
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059900000000000064
    value_note: ''
    paper_rank: 33
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.9189
    sort_std: 0.0393
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.839
    std: 0.007
    paper_value: 0.839
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 19
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07280000000000009
    value_note: ''
    paper_rank: 42
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9118
    sort_std: 0.007
    is_best: false
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.894
    std: 0.038
    paper_value: 0.894
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 21
    true_value: 0.894
    true_std: 0.038
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.038
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.842
    std: 0.026
    paper_value: 0.842
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 42
    true_value: 0.842
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.842
    sort_std: 0.026
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.757
    std: 0.01
    paper_value: 0.757
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07409999999999994
    value_note: ''
    paper_rank: 87
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.823
    std: 0.025
    paper_value: 0.823
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 52
    true_value: 0.823
    true_std: 0.025
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.025
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.814
    std: 0.035
    paper_value: 0.814
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 56
    true_value: 0.814
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.035
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.812
    std: 0.025
    paper_value: 0.812
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 59
    true_value: 0.812
    true_std: 0.025
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.025
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.788
    std: 0.009
    paper_value: 0.788
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.020199999999999996
    value_note: global 0.8082 within std
    paper_rank: 67
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.793
    std: 0.012
    paper_value: 0.793
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 65
    true_value: 0.793
    true_std: 0.012
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    paper_value: 0.919
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 1
    true_value: 0.919
    true_std: 0.026
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    paper_value: 0.918
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 2
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    paper_value: 0.901
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.901
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.028300000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9
    sort_std: 0.028300000000000002
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.899
    std: 0.03
    paper_value: 0.899
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.899
    true_std: 0.03
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.899
    sort_std: 0.03
    is_best: true
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8941
    std: 0.047400000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8941
    sort_std: 0.047400000000000005
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.894
    std: 0.022
    paper_value: 0.894
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.894
    true_std: 0.022
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.022
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8920999999999999
    std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.8920999999999999
    sort_std: 0.0384
    is_best: true
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.889
    std: 0.032
    paper_value: 0.889
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.889
    true_std: 0.032
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.889
    sort_std: 0.032
    is_best: true
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.886
    std: 0.021
    paper_value: 0.886
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.886
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.886
    sort_std: 0.021
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.879
    std: 0.042
    paper_value: 0.879
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 13
    true_value: 0.879
    true_std: 0.042
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.879
    sort_std: 0.042
    is_best: true
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.852
    std: 0.021
    paper_value: 0.852
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.852
    true_std: 0.021
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.852
    sort_std: 0.021
    is_best: false
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.83
    std: 0.018
    paper_value: 0.83
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 26
    true_value: 0.83
    true_std: 0.018
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.018
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.667
    std: 0.014
    paper_value: 0.667
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11929999999999996
    value_note: ''
    paper_rank: 106
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.71
    std: 0.046
    paper_value: 0.71
    paper_std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07169999999999999
    value_note: ''
    paper_rank: 94
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.648
    std: 0.052
    paper_value: 0.648
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 77
    true_value: 0.7568
    true_std: 0.0426
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10880000000000001
    value_note: ''
    paper_rank: 110
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7568
    sort_std: 0.0426
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.755
    std: 0.008
    paper_value: 0.755
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 4
    true_value: 0.755
    true_std: 0.008
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.008
    is_best: true
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.744
    std: 0.015
    paper_value: 0.744
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.744
    true_std: 0.015
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.744
    sort_std: 0.015
    is_best: true
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.741
    std: 0.023
    paper_value: 0.741
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.741
    true_std: 0.023
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.023
    is_best: true
  - model: DMD-SGC
    model_key: dmd-sgc
    model_plain: DMD-SGC
    value: 0.741
    std: 0.009
    paper_value: 0.741
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 10
    true_value: 0.741
    true_std: 0.009
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.009
    is_best: false
  - model: DMD-GCN
    model_key: dmd-gcn
    model_plain: DMD-GCN
    value: 0.739
    std: 0.028
    paper_value: 0.739
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.739
    true_std: 0.028
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.028
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.727
    std: 0.003
    paper_value: 0.727
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008299999999999974
    value_note: ''
    paper_rank: 34
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.72
    std: 0.005
    paper_value: 0.72
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013000000000000012
    value_note: ''
    paper_rank: 51
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.728
    std: 0.024
    paper_value: 0.728
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 29
    true_value: 0.728
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.024
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.706
    std: 0.016
    paper_value: 0.706
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 52
    true_value: 0.72
    true_std: 0.0016
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.014000000000000012
    value_note: global 0.7200 within std
    paper_rank: 75
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.72
    sort_std: 0.0016
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.703
    std: 0.025
    paper_value: 0.703
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 58
    true_value: 0.719
    true_std: 0.0025
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.016000000000000014
    value_note: global 0.7190 within std
    paper_rank: 77
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.719
    sort_std: 0.0025
    is_best: false
  - model: Framelets
    model_key: framelets
    model_plain: Framelets
    value: 0.719
    std: 0.002
    paper_value: 0.719
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 59
    true_value: 0.719
    true_std: 0.002
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.002
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.704
    std: 0.015
    paper_value: 0.704
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 75
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007000000000000006
    value_note: global 0.7110 within std
    paper_rank: 77
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.55
    std: 0.003
    paper_value: 0.55
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 91
    true_value: 0.666
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11599999999999999
    value_note: ''
    paper_rank: 101
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.666
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
- benchmark: OGB
  datasets:
  - *id009
- benchmark: DualEquiNet RNA Benchmarks
  datasets:
  - *id010
main_figure: /figures/2410.05593/main_figure.png
---

