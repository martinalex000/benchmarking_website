---
title: Improving Compositional Generalization using Iterated Learning and Simplicial
  Embeddings
arxiv_id: '2310.18777'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: Compositional generalization, the ability of an agent to generalize to unseen
  combinations of latent factors, is easy for humans but hard for deep neural networks.
  A line of research in cognitive science has hypothesized a process, ``iterated learning,''
  to help explain how human language developed this ability; the theory rests on simultaneous
  pressures towards compressibility (when an ignorant agent learns from an informed
  one) and expressivity (when it uses the representation for downstream tasks). Inspired
  by this process, we propose to improve the compositional generalization of deep
  networks by using iterated learning on models with simplicial embeddings, which
  can approximately discretize representations. This approach is further motivated
  by an analysis of compositionality based on Kolmogorov complexity. We show that
  this combination of changes improves compositional generalization over other approaches,
  demonstrating these improvements both on vision tasks with well-understood latent
  factors and on real molecular graph prediction tasks where the latent structure
  is unknown.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- SEM-IL (GCN)
- SEM-IL
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- OGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: SEM-IL
    model_key: sem-il
    model_plain: SEM-IL
    value: 0.0312
    std: 0.008053
    paper_value: 0.0312
    paper_std: 0.008053
    metric: MSE
    higher_is_better: false
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
    global_rank: null
    sort_value: 0.0312
    sort_std: 0.008053
    is_best: true
  - model: SEM-only
    model_key: sem-only
    model_plain: SEM-only
    value: 0.04291
    std: 0.01005
    paper_value: 0.04291
    paper_std: 0.01005
    metric: MSE
    higher_is_better: false
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
    global_rank: null
    sort_value: 0.04291
    sort_std: 0.01005
    is_best: true
  - model: NIL-only
    model_key: nil-only
    model_plain: NIL-only
    value: 0.04338
    std: 0.01403
    paper_value: 0.04338
    paper_std: 0.01403
    metric: MSE
    higher_is_better: false
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
    global_rank: null
    sort_value: 0.04338
    sort_std: 0.01403
    is_best: true
  - model: Baseline
    model_key: baseline
    model_plain: Baseline
    value: 0.04542
    std: 0.01097
    paper_value: 0.04542
    paper_std: 0.01097
    metric: MSE
    higher_is_better: false
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
    global_rank: null
    sort_value: 0.04542
    sort_std: 0.01097
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.05
    sort_std: 0.021
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.093
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.093
    sort_std: null
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id004
  dataset: PCQM4Mv2
  rows:
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.0831
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0831
    sort_std: null
    is_best: true
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: GRIT 2-QiQRW
    model_key: grit 2-qiqrw
    model_plain: GRIT 2-QiQRW
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: SEM-IL (GCN)
    model_key: sem-il (gcn)
    model_plain: SEM-IL (GCN)
    value: 0.098
    std: 0.005
    paper_value: 0.098
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
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
    global_rank: 25
    true_value: 0.098
    true_std: 0.005
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.098
    sort_std: 0.005
    is_best: false
  - model: SEM-only (GCN)
    model_key: sem-only (gcn)
    model_plain: SEM-only (GCN)
    value: 0.106
    std: 0.004
    paper_value: 0.106
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
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
    global_rank: 26
    true_value: 0.106
    true_std: 0.004
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.106
    sort_std: 0.004
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.108
    std: 0.003
    paper_value: 0.108
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
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
    global_rank: 27
    true_value: 0.108
    true_std: 0.003
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
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
    value: 0.9682
    std: 0.0003
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
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9681
    std: 0.0003
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
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: SEM-IL (GCN)
    model_key: sem-il (gcn)
    model_plain: SEM-IL (GCN)
    value: 0.7861
    std: 0.0073
    paper_value: 0.7861
    paper_std: 0.0073
    metric: ROC-AUC
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
    global_rank: 86
    true_value: 0.7861
    true_std: 0.0073
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7861
    sort_std: 0.0073
    is_best: false
  - model: SEM-only (GCN)
    model_key: sem-only (gcn)
    model_plain: SEM-only (GCN)
    value: 0.7821
    std: 0.0078
    paper_value: 0.7821
    paper_std: 0.0078
    metric: ROC-AUC
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
    true_value: 0.7821
    true_std: 0.0078
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7821
    sort_std: 0.0078
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.7701
    std: 0.0094
    paper_value: 0.7701
    paper_std: 0.0094
    metric: ROC-AUC
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
    global_rank: 140
    true_value: 0.7701
    true_std: 0.0094
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7701
    sort_std: 0.0094
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: SEM-IL (GCN)
    model_key: sem-il (gcn)
    model_plain: SEM-IL (GCN)
    value: 0.2802
    std: 0.0061
    paper_value: 0.2802
    paper_std: 0.0061
    metric: AP
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
    global_rank: 32
    true_value: 0.2802
    true_std: 0.0061
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2802
    sort_std: 0.0061
    is_best: false
  - model: SEM-only (GCN)
    model_key: sem-only (gcn)
    model_plain: SEM-only (GCN)
    value: 0.2566
    std: 0.0047
    paper_value: 0.2566
    paper_std: 0.0047
    metric: AP
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
    true_value: 0.2566
    true_std: 0.0047
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2566
    sort_std: 0.0047
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.2291
    std: 0.004
    paper_value: 0.2291
    paper_std: 0.004
    metric: AP
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
    global_rank: 54
    true_value: 0.2291
    true_std: 0.004
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2291
    sort_std: 0.004
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
  - *id003
  - *id004
main_figure: /figures/2310.18777/main_figure.png
---

