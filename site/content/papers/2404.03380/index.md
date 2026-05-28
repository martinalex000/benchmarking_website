---
title: On the Theoretical Expressive Power and the Design Space of Higher-Order Graph
  Transformers
arxiv_id: '2404.03380'
source_url: ''
authors: []
published_date: '2024-04-04'
published_date_iso: '2024-04-04'
abstract: Graph transformers have recently received significant attention in graph
  learning, partly due to their ability to capture more global interaction via self-attention.
  Nevertheless, while higher-order graph neural networks have been reasonably well
  studied, the exploration of extending graph transformers to higher-order variants
  is just starting. Both theoretical understanding and empirical results are limited.
  In this paper, we provide a systematic study of the theoretical expressive power
  of order-$k$ graph transformers and sparse variants. We first show that, an order-$k$
  graph transformer without additional structural information is less expressive than
  the $k$-Weisfeiler Lehman ($k$-WL) test despite its high computational cost. We
  then explore strategies to both sparsify and enhance the higher-order graph transformers,
  aiming to improve both their efficiency and expressiveness. Indeed, sparsification
  based on neighborhood information can enhance the expressive power, as it provides
  additional information about input graph structures. In particular, we show that
  a natural neighborhood-based sparse order-$k$ transformer model is not only computationally
  efficient, but also expressive -- as expressive as $k$-WL test. We further study
  several other sparse graph attention models that are computationally efficient and
  provide their expressiveness analysis. Finally, we provide experimental results
  to show the effectiveness of the different sparsification strategies.
codebase_url: ''
extraction_model: glm-4.7
has_results: true
paper_type: method
proposed_models:
- A_2^LN
- A_2^LN+LapPE
- A_2^LN+RWSE
- AS_0:1+attn.bias+RWSE
- AS_0:1^SN
- A_2-Performer
- A_2^VT
- A_2^Ngbh
- A_2^LN+VT
- AS_0:1^SN+VS
- A_3(connected)
- $\mathcal {AS}_{0:1}$-dense+attn.bias
- \mathcal A_{2}^{\mathsf {LN}}
mrr: 0.0417
adjusted_mrr: 0.0139
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- GNNBenchmark
- OGB
- PyG Imported Datasets
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id009
  dataset: Alchemy
  rows:
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 0.087
    std: 0.001
    paper_value: 0.087
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_alchemy_rebuttal
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 2
    true_value: 0.087
    true_std: 0.001
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.087
    sort_std: 0.001
    is_best: true
  - model: GINE + OGE-Aug
    model_key: gine + oge-aug
    model_plain: GINE + OGE-Aug
    value: 0.087
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.087
    sort_std: 0.001
    is_best: true
  - model: \mathcal A_{2}^{\mathsf {VT}}
    model_key: \mathcal a_{2}^{\mathsf {vt}}
    model_plain: \mathcal A_{2}^{\mathsf {VT}}
    value: 0.09
    std: 0.001
    paper_value: 0.09
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_alchemy_rebuttal
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 3
    true_value: 0.09
    true_std: 0.001
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.001
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {Ngbh}}
    model_key: \mathcal a_{2}^{\mathsf {ngbh}}
    model_plain: \mathcal A_{2}^{\mathsf {Ngbh}}
    value: 0.094
    std: 0.001
    paper_value: 0.094
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_alchemy_rebuttal
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 4
    true_value: 0.094
    true_std: 0.001
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.001
    is_best: false
  - model: GIN + SPE (All)
    model_key: gin + spe (all)
    model_plain: GIN + SPE (All)
    value: 0.108
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.108
    sort_std: 0.001
    is_best: false
  - model: GIN + BasisNet (All)
    model_key: gin + basisnet (all)
    model_plain: GIN + BasisNet (All)
    value: 0.11
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.11
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.112
    std: 0.001
    paper_value: 0.112
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_alchemy_rebuttal
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 7
    true_value: 0.112
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.112
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id007
  dataset: CSL
  rows:
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AttendingGT
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 3
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: Transformer+RWSE
    model_key: transformer+rwse
    model_plain: Transformer+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AttendingGT
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 4
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2+LapPE
    model_key: a_2+lappe
    model_plain: A_2+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 5
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2+RWSE
    model_key: a_2+rwse
    model_plain: A_2+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 6
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2^LN
    model_key: a_2^ln
    model_plain: A_2^LN
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 7
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2^LN+LapPE
    model_key: a_2^ln+lappe
    model_plain: A_2^LN+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 8
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2^LN+RWSE
    model_key: a_2^ln+rwse
    model_plain: A_2^LN+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 9
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: AS_0:1+attn.bias+LapPE
    model_key: as_0:1+attn.bias+lappe
    model_plain: AS_0:1+attn.bias+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 10
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: AS_0:1+attn.bias+RWSE
    model_key: as_0:1+attn.bias+rwse
    model_plain: AS_0:1+attn.bias+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 11
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: AS_0:1^SN+LapPE
    model_key: as_0:1^sn+lappe
    model_plain: AS_0:1^SN+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 12
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: AS_0:1^SN+RWSE
    model_key: as_0:1^sn+rwse
    model_plain: AS_0:1^SN+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 13
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal A_{2}^{\mathsf {LN}}
    model_key: \mathcal a_{2}^{\mathsf {ln}}
    model_plain: \mathcal A_{2}^{\mathsf {LN}}
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 24
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 27
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal A_{2}+LapPE
    model_key: \mathcal a_{2}+lappe
    model_plain: \mathcal A_{2}+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 22
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal A_{2}+RWSE
    model_key: \mathcal a_{2}+rwse
    model_plain: \mathcal A_{2}+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 23
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal {AS}_{0:1}+attn.bias+LapPE
    model_key: \mathcal {as}_{0:1}+attn.bias+lappe
    model_plain: \mathcal {AS}_{0:1}+attn.bias+LapPE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 25
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: \mathcal {AS}_{0:1}+attn.bias+RWSE
    model_key: \mathcal {as}_{0:1}+attn.bias+rwse
    model_plain: \mathcal {AS}_{0:1}+attn.bias+RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 26
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_display: Jul 2023
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 14
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.9
    std: 0.0
    paper_value: 0.9
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AttendingGT
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 31
    true_value: 0.9
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: 0.0
    is_best: false
  - model: AS_0:1+attn.bias
    model_key: as_0:1+attn.bias
    model_plain: AS_0:1+attn.bias
    value: 0.3667
    std: 0.0
    paper_value: 0.3667
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 33
    true_value: 0.3667
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3667
    sort_std: 0.0
    is_best: false
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_key: $\mathcal {as}_{0:1}$-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    value: 0.3667
    std: 0.0
    paper_value: 0.3667
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 34
    true_value: 0.3667
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3667
    sort_std: 0.0
    is_best: false
  - model: AS_0:1^SN
    model_key: as_0:1^sn
    model_plain: AS_0:1^SN
    value: 0.2
    std: 0.0
    paper_value: 0.2
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 35
    true_value: 0.2
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2
    sort_std: 0.0
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AttendingGT
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 38
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AttendingGT
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 39
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  - model: A_2
    model_key: a_2
    model_plain: A_2
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 40
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  - model: \mathcal A_{2}
    model_key: \mathcal a_{2}
    model_plain: \mathcal A_{2}
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_edge_CSL
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 44
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5378
    std: 0.0307
    paper_value: 0.5378
    paper_std: 0.0307
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.28680000000000005
    value_note: ''
    paper_rank: 118
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: Transformer+DEG
    model_key: transformer+deg
    model_plain: Transformer+DEG
    value: 0.7189
    std: 0.0248
    paper_value: 0.7189
    paper_std: 0.0248
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 52
    true_value: 0.7189
    true_std: 0.0248
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7189
    sort_std: 0.0248
    is_best: false
  - model: Transformer+RWSE
    model_key: transformer+rwse
    model_plain: Transformer+RWSE
    value: 0.7081
    std: 0.0202
    paper_value: 0.7081
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 61
    true_value: 0.7081
    true_std: 0.0202
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7081
    sort_std: 0.0202
    is_best: false
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_key: $\mathcal {as}_{0:1}$-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    value: 0.7027
    std: 0.0296
    paper_value: 0.7027
    paper_std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 64
    true_value: 0.7027
    true_std: 0.0296
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0296
    is_best: false
  - model: AS0:1-dense+attn.bias
    model_key: as0:1-dense+attn.bias
    model_plain: AS0:1-dense+attn.bias
    value: 0.7027
    std: 0.0296
    paper_value: 0.7027
    paper_std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 67
    true_value: 0.7027
    true_std: 0.0296
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7027
    sort_std: 0.0296
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6946
    std: 0.0173
    paper_value: 0.6946
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 70
    true_value: 0.6946
    true_std: 0.0173
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6946
    sort_std: 0.0173
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.6838
    std: 0.0173
    paper_value: 0.6838
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 74
    true_value: 0.6838
    true_std: 0.0173
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6838
    sort_std: 0.0173
    is_best: false
  - model: Graphormer+attn.bias
    model_key: graphormer+attn.bias
    model_plain: Graphormer+attn.bias
    value: 0.6838
    std: 0.0173
    paper_value: 0.6838
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 75
    true_value: 0.6838
    true_std: 0.0173
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6838
    sort_std: 0.0173
    is_best: false
  - model: GPS(GCN+Transformer)+LapPE
    model_key: gps(gcn+transformer)+lappe
    model_plain: GPS(GCN+Transformer)+LapPE
    value: 0.6622
    std: 0.0387
    paper_value: 0.6622
    paper_std: 0.0387
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 82
    true_value: 0.6622
    true_std: 0.0387
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6622
    sort_std: 0.0387
    is_best: false
  - model: GPS(GCN+Transformer)+RWSE
    model_key: gps(gcn+transformer)+rwse
    model_plain: GPS(GCN+Transformer)+RWSE
    value: 0.6514
    std: 0.0573
    paper_value: 0.6514
    paper_std: 0.0573
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 89
    true_value: 0.6514
    true_std: 0.0573
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6514
    sort_std: 0.0573
    is_best: false
  - model: GPS(GCN+Transformer)+DEG
    model_key: gps(gcn+transformer)+deg
    model_plain: GPS(GCN+Transformer)+DEG
    value: 0.6405
    std: 0.0243
    paper_value: 0.6405
    paper_std: 0.0243
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 94
    true_value: 0.6405
    true_std: 0.0243
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6405
    sort_std: 0.0243
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.5622
    std: 0.0265
    paper_value: 0.5622
    paper_std: 0.0265
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 111
    true_value: 0.5703
    true_std: 0.0547
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008099999999999996
    value_note: global 0.5703 within std
    paper_rank: 112
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.5703
    sort_std: 0.0547
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.5378
    std: 0.0409
    paper_value: 0.5378
    paper_std: 0.0409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 119
    true_value: 0.5378
    true_std: 0.0409
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5378
    sort_std: 0.0409
    is_best: false
  - model: GCN (DEG)
    model_key: gcn (deg)
    model_plain: GCN (DEG)
    value: 0.5351
    std: 0.0265
    paper_value: 0.5351
    paper_std: 0.0265
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 120
    true_value: 0.5351
    true_std: 0.0265
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5351
    sort_std: 0.0265
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 259
    rank_delta: 250
    rank_delta_abs: 250
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 48
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 271
    rank_delta: 223
    rank_delta_abs: 223
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 141
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 286
    rank_delta: 145
    rank_delta_abs: 145
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 152
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 166
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: AS_0:1^SN+VS
    model_key: as_0:1^sn+vs
    model_plain: AS_0:1^SN+VS
    value: 0.6486
    std: 0.0063
    paper_value: 0.6486
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 182
    true_value: 0.6486
    true_std: 0.0063
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6486
    sort_std: 0.0063
    is_best: false
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 0.6486
    std: 0.0063
    paper_value: 0.6486
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 183
    true_value: 0.6486
    true_std: 0.0063
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6486
    sort_std: 0.0063
    is_best: false
  - model: AS_0:1+attn.bias+RWSE
    model_key: as_0:1+attn.bias+rwse
    model_plain: AS_0:1+attn.bias+RWSE
    value: 0.6445
    std: 0.0082
    paper_value: 0.6445
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 196
    true_value: 0.6445
    true_std: 0.0082
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6445
    sort_std: 0.0082
    is_best: false
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_key: $\mathcal {as}_{0:1}$-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    value: 0.6445
    std: 0.0082
    paper_value: 0.6445
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 197
    true_value: 0.6445
    true_std: 0.0082
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6445
    sort_std: 0.0082
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 198
    true_value: 0.644
    true_std: 0.008
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.6440 within std
    paper_rank: 199
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.644
    sort_std: 0.008
    is_best: false
  - model: A_2^Ngbh
    model_key: a_2^ngbh
    model_plain: A_2^Ngbh
    value: 0.6419
    std: 0.0108
    paper_value: 0.6419
    paper_std: 0.0108
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table crossatten_A12
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 206
    true_value: 0.6419
    true_std: 0.0108
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 206
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6419
    sort_std: 0.0108
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 210
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: A_3(connected)
    model_key: a_3(connected)
    model_plain: A_3(connected)
    value: 0.6329
    std: 0.0117
    paper_value: 0.6329
    paper_std: 0.0117
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table crossatten_A12
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 214
    true_value: 0.6329
    true_std: 0.0117
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 214
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6329
    sort_std: 0.0117
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 215
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 215
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: AS_0:1^SN
    model_key: as_0:1^sn
    model_plain: AS_0:1^SN
    value: 0.5876
    std: 0.0079
    paper_value: 0.5876
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 269
    true_value: 0.5876
    true_std: 0.0079
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 269
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5876
    sort_std: 0.0079
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
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
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 301
    rank_delta: 298
    rank_delta_abs: 298
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 294
    rank_delta: 282
    rank_delta_abs: 282
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 78
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 308
    rank_delta: 230
    rank_delta_abs: 230
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: AS_0:1+attn.bias+RWSE
    model_key: as_0:1+attn.bias+rwse
    model_plain: AS_0:1+attn.bias+RWSE
    value: 0.2486
    std: 0.0007
    paper_value: 0.2486
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 111
    true_value: 0.2486
    true_std: 0.0007
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2486
    sort_std: 0.0007
    is_best: false
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_key: $\mathcal {as}_{0:1}$-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    value: 0.2486
    std: 0.0007
    paper_value: 0.2486
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 112
    true_value: 0.2486
    true_std: 0.0007
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2486
    sort_std: 0.0007
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 132
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: AS_0:1^SN+VS
    model_key: as_0:1^sn+vs
    model_plain: AS_0:1^SN+VS
    value: 0.2524
    std: 0.0009
    paper_value: 0.2524
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 162
    true_value: 0.2524
    true_std: 0.0009
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2524
    sort_std: 0.0009
    is_best: false
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 0.2524
    std: 0.0009
    paper_value: 0.2524
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 163
    true_value: 0.2524
    true_std: 0.0009
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2524
    sort_std: 0.0009
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 165
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: A_3(connected)
    model_key: a_3(connected)
    model_plain: A_3(connected)
    value: 0.2529
    std: 0.0023
    paper_value: 0.2529
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0023
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0023
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2545
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 185
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 185
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: A_2^Ngbh
    model_key: a_2^ngbh
    model_plain: A_2^Ngbh
    value: 0.2612
    std: 0.0013
    paper_value: 0.2612
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 212
    true_value: 0.2612
    true_std: 0.0013
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2612
    sort_std: 0.0013
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 239
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: AS_0:1^SN
    model_key: as_0:1^sn
    model_plain: AS_0:1^SN
    value: 0.2703
    std: 0.0015
    paper_value: 0.2703
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 244
    true_value: 0.2703
    true_std: 0.0015
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 244
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0015
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6595
    std: 0.0367
    paper_value: 0.6595
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 44
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17159999999999997
    value_note: ''
    paper_rank: 122
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.7784
    std: 0.0108
    paper_value: 0.7784
    paper_std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 68
    true_value: 0.7784
    true_std: 0.0108
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.0108
    is_best: false
  - model: Transformer+RWSE
    model_key: transformer+rwse
    model_plain: Transformer+RWSE
    value: 0.7757
    std: 0.0124
    paper_value: 0.7757
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 71
    true_value: 0.7757
    true_std: 0.0124
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7757
    sort_std: 0.0124
    is_best: false
  - model: Transformer+DEG
    model_key: transformer+deg
    model_plain: Transformer+DEG
    value: 0.773
    std: 0.0132
    paper_value: 0.773
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 76
    true_value: 0.773
    true_std: 0.0132
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.0132
    is_best: false
  - model: AS_0:1+attn.bias+RWSE
    model_key: as_0:1+attn.bias+rwse
    model_plain: AS_0:1+attn.bias+RWSE
    value: 0.7684
    std: 0.0166
    paper_value: 0.7684
    paper_std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 79
    true_value: 0.7684
    true_std: 0.0166
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7684
    sort_std: 0.0166
    is_best: false
  - model: AS0:1-dense+attn.bias
    model_key: as0:1-dense+attn.bias
    model_plain: AS0:1-dense+attn.bias
    value: 0.7684
    std: 0.0166
    paper_value: 0.7684
    paper_std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 80
    true_value: 0.7684
    true_std: 0.0166
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7684
    sort_std: 0.0166
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.7676
    std: 0.0179
    paper_value: 0.7676
    paper_std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 81
    true_value: 0.7676
    true_std: 0.0179
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7676
    sort_std: 0.0179
    is_best: false
  - model: Graphormer+attn.bias
    model_key: graphormer+attn.bias
    model_plain: Graphormer+attn.bias
    value: 0.7622
    std: 0.0236
    paper_value: 0.7622
    paper_std: 0.0236
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 82
    true_value: 0.767
    true_std: 0.017
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0048000000000000265
    value_note: global 0.7670 within std
    paper_rank: 83
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.767
    sort_std: 0.017
    is_best: false
  - model: GPS(GCN+Transformer)+LapPE
    model_key: gps(gcn+transformer)+lappe
    model_plain: GPS(GCN+Transformer)+LapPE
    value: 0.7541
    std: 0.0146
    paper_value: 0.7541
    paper_std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 87
    true_value: 0.7541
    true_std: 0.0146
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7541
    sort_std: 0.0146
    is_best: false
  - model: GPS(GCN+Transformer)+RWSE
    model_key: gps(gcn+transformer)+rwse
    model_plain: GPS(GCN+Transformer)+RWSE
    value: 0.7351
    std: 0.0265
    paper_value: 0.7351
    paper_std: 0.0265
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 100
    true_value: 0.7351
    true_std: 0.0265
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7351
    sort_std: 0.0265
    is_best: false
  - model: GPS(GCN+Transformer)+DEG
    model_key: gps(gcn+transformer)+deg
    model_plain: GPS(GCN+Transformer)+DEG
    value: 0.7351
    std: 0.0359
    paper_value: 0.7351
    paper_std: 0.0359
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 101
    true_value: 0.7351
    true_std: 0.0359
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7351
    sort_std: 0.0359
    is_best: false
  - model: GCN (DEG)
    model_key: gcn (deg)
    model_plain: GCN (DEG)
    value: 0.6676
    std: 0.0272
    paper_value: 0.6676
    paper_std: 0.0272
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 120
    true_value: 0.6676
    true_std: 0.0272
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6676
    sort_std: 0.0272
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6595
    std: 0.0367
    paper_value: 0.6595
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 123
    true_value: 0.6595
    true_std: 0.0367
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6595
    sort_std: 0.0367
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.6297
    std: 0.0321
    paper_value: 0.6297
    paper_std: 0.0321
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 133
    true_value: 0.6297
    true_std: 0.0321
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6297
    sort_std: 0.0321
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: Transformer+RWSE
    model_key: transformer+rwse
    model_plain: Transformer+RWSE
    value: 0.802
    std: 0.0223
    paper_value: 0.802
    paper_std: 0.0223
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 42
    true_value: 0.802
    true_std: 0.0223
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.802
    sort_std: 0.0223
    is_best: false
  - model: Transformer+DEG
    model_key: transformer+deg
    model_plain: Transformer+DEG
    value: 0.798
    std: 0.009
    paper_value: 0.798
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 46
    true_value: 0.798
    true_std: 0.009
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6667
    std: 0.0263
    paper_value: 0.6667
    paper_std: 0.0263
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11960000000000004
    value_note: ''
    paper_rank: 106
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: GPS(GCN+Transformer)+RWSE
    model_key: gps(gcn+transformer)+rwse
    model_plain: GPS(GCN+Transformer)+RWSE
    value: 0.7804
    std: 0.0288
    paper_value: 0.7804
    paper_std: 0.0288
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 62
    true_value: 0.7804
    true_std: 0.0288
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7804
    sort_std: 0.0288
    is_best: false
  - model: Graphormer+attn.bias
    model_key: graphormer+attn.bias
    model_plain: Graphormer+attn.bias
    value: 0.7765
    std: 0.02
    paper_value: 0.7765
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 65
    true_value: 0.7765
    true_std: 0.02
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7765
    sort_std: 0.02
    is_best: false
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_key: $\mathcal {as}_{0:1}$-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    value: 0.7745
    std: 0.0098
    paper_value: 0.7745
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 67
    true_value: 0.7745
    true_std: 0.0098
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7745
    sort_std: 0.0098
    is_best: false
  - model: AS0:1-dense+attn.bias
    model_key: as0:1-dense+attn.bias
    model_plain: AS0:1-dense+attn.bias
    value: 0.7745
    std: 0.0098
    paper_value: 0.7745
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 68
    true_value: 0.7745
    true_std: 0.0098
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7745
    sort_std: 0.0098
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.7706
    std: 0.0197
    paper_value: 0.7706
    paper_std: 0.0197
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 69
    true_value: 0.7706
    true_std: 0.0197
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7706
    sort_std: 0.0197
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.7608
    std: 0.0192
    paper_value: 0.7608
    paper_std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 76
    true_value: 0.7608
    true_std: 0.0192
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7608
    sort_std: 0.0192
    is_best: false
  - model: GPS(GCN+Transformer)+DEG
    model_key: gps(gcn+transformer)+deg
    model_plain: GPS(GCN+Transformer)+DEG
    value: 0.7549
    std: 0.0423
    paper_value: 0.7549
    paper_std: 0.0423
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 78
    true_value: 0.7549
    true_std: 0.0423
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7549
    sort_std: 0.0423
    is_best: false
  - model: GPS(GCN+Transformer)+LapPE
    model_key: gps(gcn+transformer)+lappe
    model_plain: GPS(GCN+Transformer)+LapPE
    value: 0.7471
    std: 0.0297
    paper_value: 0.7471
    paper_std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 85
    true_value: 0.7471
    true_std: 0.0297
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7471
    sort_std: 0.0297
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.6941
    std: 0.0266
    paper_value: 0.6941
    paper_std: 0.0266
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 102
    true_value: 0.6941
    true_std: 0.0266
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6941
    sort_std: 0.0266
    is_best: false
  - model: GCN (DEG)
    model_key: gcn (deg)
    model_plain: GCN (DEG)
    value: 0.6726
    std: 0.0153
    paper_value: 0.6726
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 106
    true_value: 0.6726
    true_std: 0.0153
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6726
    sort_std: 0.0153
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6647
    std: 0.0137
    paper_value: 0.6647
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_node_heterophilic
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 107
    true_value: 0.6647
    true_std: 0.0137
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6647
    sort_std: 0.0137
    is_best: false
  metric: Accuracy
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: CWNetworks
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 140
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 140
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GPS
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 105
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
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
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 105
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Graphormer
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 203
    rank_delta: 185
    rank_delta_abs: 185
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 203
    rank_delta: 185
    rank_delta_abs: 185
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PNA
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13072978921109524
    value_note: ''
    paper_rank: 245
    rank_delta: 197
    rank_delta_abs: 197
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
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
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13072978921109524
    value_note: ''
    paper_rank: 245
    rank_delta: 197
    rank_delta_abs: 197
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.069
    std: 0.004
    paper_value: 0.069
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0040000000000000036
    value_note: ''
    paper_rank: 93
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: A_2^LN+VT
    model_key: a_2^ln+vt
    model_plain: A_2^LN+VT
    value: 0.069
    std: 0.005
    paper_value: 0.069
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
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 99
    true_value: 0.069
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.005
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {VT}}
    model_key: \mathcal a_{2}^{\mathsf {vt}}
    model_plain: \mathcal A_{2}^{\mathsf {VT}}
    value: 0.069
    std: 0.005
    paper_value: 0.069
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 102
    true_value: 0.069
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.005
    is_best: false
  - model: A2^LN+VT
    model_key: a2^ln+vt
    model_plain: A2^LN+VT
    value: 0.069
    std: 0.005
    paper_value: 0.069
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 103
    true_value: 0.069
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.005
    is_best: false
  - model: AS_0:1^SN+VS
    model_key: as_0:1^sn+vs
    model_plain: AS_0:1^SN+VS
    value: 0.073
    std: 0.004
    paper_value: 0.073
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 118
    true_value: 0.073
    true_std: 0.004
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.004
    is_best: false
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 0.073
    std: 0.004
    paper_value: 0.073
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 119
    true_value: 0.073
    true_std: 0.004
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.004
    is_best: false
  - model: AS0:1^SN+VS
    model_key: as0:1^sn+vs
    model_plain: AS0:1^SN+VS
    value: 0.073
    std: 0.004
    paper_value: 0.073
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 120
    true_value: 0.073
    true_std: 0.004
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.004
    is_best: false
  - model: A_2^Ngbh
    model_key: a_2^ngbh
    model_plain: A_2^Ngbh
    value: 0.075
    std: 0.005
    paper_value: 0.075
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
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 126
    true_value: 0.075
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.075
    sort_std: 0.005
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {Ngbh}}
    model_key: \mathcal a_{2}^{\mathsf {ngbh}}
    model_plain: \mathcal A_{2}^{\mathsf {Ngbh}}
    value: 0.075
    std: 0.005
    paper_value: 0.075
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 127
    true_value: 0.075
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.075
    sort_std: 0.005
    is_best: false
  - model: A2^Ngbh
    model_key: a2^ngbh
    model_plain: A2^Ngbh
    value: 0.075
    std: 0.005
    paper_value: 0.075
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 128
    true_value: 0.075
    true_std: 0.005
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.075
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GCN
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 129
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.291
    value_note: ''
    paper_rank: 278
    rank_delta: 149
    rank_delta_abs: 149
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 129
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.291
    value_note: ''
    paper_rank: 278
    rank_delta: 149
    rank_delta_abs: 149
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ResidualGatedGCN
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 130
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20499999999999996
    value_note: ''
    paper_rank: 263
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 130
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20499999999999996
    value_note: ''
    paper_rank: 263
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GAT
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 138
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 278
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 138
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 278
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GNNAK
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 143
    true_value: 0.08
    true_std: 0.001
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.001
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 143
    true_value: 0.08
    true_std: 0.001
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.001
    is_best: false
  - model: AS_0:1^SN
    model_key: as_0:1^sn
    model_plain: AS_0:1^SN
    value: 0.08
    std: 0.004
    paper_value: 0.08
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 144
    true_value: 0.08
    true_std: 0.004
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.004
    is_best: false
  - model: AS0:1^SN
    model_key: as0:1^sn
    model_plain: AS0:1^SN
    value: 0.08
    std: 0.004
    paper_value: 0.08
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 146
    true_value: 0.08
    true_std: 0.004
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.08
    sort_std: 0.004
    is_best: false
  - model: A_2^LN
    model_key: a_2^ln
    model_plain: A_2^LN
    value: 0.086
    std: 0.006
    paper_value: 0.086
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 160
    true_value: 0.086
    true_std: 0.006
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.086
    sort_std: 0.006
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {LN}}
    model_key: \mathcal a_{2}^{\mathsf {ln}}
    model_plain: \mathcal A_{2}^{\mathsf {LN}}
    value: 0.086
    std: 0.006
    paper_value: 0.086
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 162
    true_value: 0.086
    true_std: 0.006
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.086
    sort_std: 0.006
    is_best: false
  - model: A2^LN
    model_key: a2^ln
    model_plain: A2^LN
    value: 0.086
    std: 0.006
    paper_value: 0.086
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 163
    true_value: 0.086
    true_std: 0.006
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.086
    sort_std: 0.006
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.108
    std: 0.009
    paper_value: 0.108
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: EGT
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 190
    true_value: 0.108
    true_std: 0.009
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.009
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.108
    std: 0.009
    paper_value: 0.108
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 190
    true_value: 0.108
    true_std: 0.009
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.009
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: RethinkingGTLap
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 217
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 218
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 217
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 218
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: A_2-Performer
    model_key: a_2-performer
    model_plain: A_2-Performer
    value: 0.155
    std: 0.008
    paper_value: 0.155
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 231
    true_value: 0.155
    true_std: 0.008
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.155
    sort_std: 0.008
    is_best: false
  - model: A_2-Performer
    model_key: a_2-performer
    model_plain: A_2-Performer
    value: 0.155
    std: 0.008
    paper_value: 0.155
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 231
    true_value: 0.155
    true_std: 0.008
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.155
    sort_std: 0.008
    is_best: false
  - model: \mathcal A_{2}\text{-}Performer
    model_key: \mathcal a_{2}\text{-}performer
    model_plain: \mathcal A_{2}\text{-}Performer
    value: 0.155
    std: 0.008
    paper_value: 0.155
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 232
    true_value: 0.155
    true_std: 0.008
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 232
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.155
    sort_std: 0.008
    is_best: false
  - model: A_2^VT
    model_key: a_2^vt
    model_plain: A_2^VT
    value: 0.186
    std: 0.009
    paper_value: 0.186
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 244
    true_value: 0.186
    true_std: 0.009
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 244
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.186
    sort_std: 0.009
    is_best: false
  - model: A2^VT
    model_key: a2^vt
    model_plain: A2^VT
    value: 0.186
    std: 0.009
    paper_value: 0.186
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 245
    true_value: 0.186
    true_std: 0.009
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 245
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.186
    sort_std: 0.009
    is_best: false
  metric: MAE
  higher_is_better: false
- &id008
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 9
    true_value: 0.8094
    true_std: 0.0057
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.8039
    std: 0.009
    paper_value: 0.8039
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: GSN
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 19
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: A_2^Ngbh
    model_key: a_2^ngbh
    model_plain: A_2^Ngbh
    value: 0.7981
    std: 0.0097
    paper_value: 0.7981
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 37
    true_value: 0.7981
    true_std: 0.0097
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7981
    sort_std: 0.0097
    is_best: false
  - model: AS_0:1^SN+VS
    model_key: as_0:1^sn+vs
    model_plain: AS_0:1^SN+VS
    value: 0.7981
    std: 0.0114
    paper_value: 0.7981
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 38
    true_value: 0.7981
    true_std: 0.0114
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7981
    sort_std: 0.0114
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {Ngbh}}
    model_key: \mathcal a_{2}^{\mathsf {ngbh}}
    model_plain: \mathcal A_{2}^{\mathsf {Ngbh}}
    value: 0.7981
    std: 0.0097
    paper_value: 0.7981
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 39
    true_value: 0.7981
    true_std: 0.0097
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7981
    sort_std: 0.0097
    is_best: false
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_key: \mathcal {as}_{0:1}^{\mathsf {sn}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    value: 0.7981
    std: 0.0114
    paper_value: 0.7981
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 40
    true_value: 0.7981
    true_std: 0.0114
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7981
    sort_std: 0.0114
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.797
    std: 0.0097
    paper_value: 0.797
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: DGN
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 42
    true_value: 0.797
    true_std: 0.0097
    value_gap_source_arxiv: '2404.09774'
    value_gap_source_title: 'RandAlign: A Parameter-Free Method for Regularizing Graph
      Convolutional Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.797
    sort_std: 0.0097
    is_best: false
  - model: GIN-AK+
    model_key: gin-ak+
    model_plain: GIN-AK+
    value: 0.7961
    std: 0.0119
    paper_value: 0.7961
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 45
    true_value: 0.7961
    true_std: 0.0119
    value_gap_source_arxiv: '2404.09774'
    value_gap_source_title: 'RandAlign: A Parameter-Free Method for Regularizing Graph
      Convolutional Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7961
    sort_std: 0.0119
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7905
    std: 0.0132
    paper_value: 0.7905
    paper_std: 0.0132
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 58
    true_value: 0.7905
    true_std: 0.0132
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7905
    sort_std: 0.0132
    is_best: false
  - model: A_2^LN+VT
    model_key: a_2^ln+vt
    model_plain: A_2^LN+VT
    value: 0.7901
    std: 0.0082
    paper_value: 0.7901
    paper_std: 0.0082
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: ''
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 60
    true_value: 0.7901
    true_std: 0.0082
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7901
    sort_std: 0.0082
    is_best: false
  - model: \mathcal A_{2}^{\mathsf {VT}}
    model_key: \mathcal a_{2}^{\mathsf {vt}}
    model_plain: \mathcal A_{2}^{\mathsf {VT}}
    value: 0.7901
    std: 0.0082
    paper_value: 0.7901
    paper_std: 0.0082
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 61
    true_value: 0.7901
    true_std: 0.0082
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7901
    sort_std: 0.0082
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: GPS
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 70
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7785
    std: 0.247
    paper_value: 0.7785
    paper_std: 0.247
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 111
    true_value: 0.7785
    true_std: 0.247
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7785
    sort_std: 0.247
    is_best: true
  - model: GCN + virtual node
    model_key: gcn + virtual node
    model_plain: GCN + virtual node
    value: 0.7707
    std: 0.0149
    paper_value: 0.7707
    paper_std: 0.0149
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_ogb
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: '2024-04-04'
    date_display: Apr 2024
    date_iso: '2024-04-04'
    global_rank: 128
    true_value: 0.7707
    true_std: 0.0149
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7707
    sort_std: 0.0149
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
- benchmark: GNNBenchmark
  datasets:
  - *id007
- benchmark: OGB
  datasets:
  - *id008
- benchmark: PyG Imported Datasets
  datasets:
  - *id009
main_figure: /figures/2404.03380/main_figure.png
---

