---
title: 'Curve Your Attention: Mixed-Curvature Transformers for Graph Representation
  Learning'
arxiv_id: '2309.04082'
source_url: ''
authors: []
published_date: Sep 2023
published_date_iso: 2023-09
abstract: Real-world graphs naturally exhibit hierarchical or cyclical structures
  that are unfit for the typical Euclidean space. While there exist graph neural networks
  that leverage hyperbolic or spherical spaces to learn representations that embed
  such structures more accurately, these methods are confined under the message-passing
  paradigm, making the models vulnerable against side-effects such as oversmoothing
  and oversquashing. More recent work have proposed global attention-based graph Transformers
  that can easily model long-range interactions, but their extensions towards non-Euclidean
  geometry are yet unexplored. To bridge this gap, we propose Fully Product-Stereographic
  Transformer, a generalization of Transformers towards operating entirely on the
  product of constant curvature spaces. When combined with tokenized graph Transformers,
  our model can learn the curvature appropriate for the input graph in an end-to-end
  fashion, without the need of additional tuning on different curvature initializations.
  We also provide a kernelized approach to non-Euclidean attention, which enables
  our model to run in time and memory cost linear to the number of nodes and edges
  while respecting the underlying geometry. Experiments on graph reconstruction and
  node classification demonstrate the benefits of generalizing Transformers to the
  non-Euclidean domain.
codebase_url: ''
extraction_model: glm-4.7
has_results: true
paper_type: method
proposed_models:
- \modelname{}
- Proposed Model (denoted as \modelname{})
mrr: 0.0072
adjusted_mrr: 0.0024
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterophilic Graphs
- TU Dortmund
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id007
  dataset: Actor
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.4298
    std: 0.0148
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
    global_rank: 1
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.4215
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4193
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.3961
    std: 0.0054
    paper_value: 0.3961
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.3961
    sort_std: 0.0054
    is_best: false
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    value: 0.3961
    std: 0.0054
    paper_value: 0.3961
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.3961
    sort_std: 0.0054
    is_best: false
  - model: HAT
    model_key: hat
    model_plain: HAT
    value: 0.3834
    std: 0.0026
    paper_value: 0.3834
    paper_std: 0.0026
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.3834
    sort_std: 0.0026
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.3687
    std: 0.005
    paper_value: 0.3687
    paper_std: 0.005
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    sort_value: 0.3687
    sort_std: 0.005
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.3659
    std: 0.0089
    paper_value: 0.3659
    paper_std: 0.0089
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.3659
    sort_std: 0.0089
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.3362
    std: 0.0055
    paper_value: 0.3362
    paper_std: 0.0055
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 23
    sort_value: 0.3362
    sort_std: 0.0055
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.2909
    std: 0.0019
    paper_value: 0.2909
    paper_std: 0.0019
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.2909
    sort_std: 0.0019
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.2889
    std: 0.0016
    paper_value: 0.2889
    paper_std: 0.0016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 36
    sort_value: 0.2889
    sort_std: 0.0016
    is_best: false
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    value: 0.2818
    std: 0.0055
    paper_value: 0.2818
    paper_std: 0.0055
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.2818
    sort_std: 0.0055
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.2743
    std: 0.0023
    paper_value: 0.2743
    paper_std: 0.0023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 59
    sort_value: 0.2743
    sort_std: 0.0023
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.2714
    std: 0.0046
    paper_value: 0.2714
    paper_std: 0.0046
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 78
    sort_value: 0.2714
    sort_std: 0.0046
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2709
    std: 0.0036
    paper_value: 0.2709
    paper_std: 0.0036
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 66
    sort_value: 0.2709
    sort_std: 0.0036
    is_best: false
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    value: 0.2639
    std: 0.006
    paper_value: 0.2639
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.2639
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.7211
    std: 0.0038
    paper_value: 0.7211
    paper_std: 0.0038
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 66
    sort_value: 0.7211
    sort_std: 0.0038
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.717
    std: 0.0028
    paper_value: 0.717
    paper_std: 0.0028
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 19
    sort_value: 0.717
    sort_std: 0.0028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7138
    std: 0.0043
    paper_value: 0.7138
    paper_std: 0.0043
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 12
    sort_value: 0.7138
    sort_std: 0.0043
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.7123
    std: 0.0051
    paper_value: 0.7123
    paper_std: 0.0051
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7123
    sort_std: 0.0051
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7058
    std: 0.0042
    paper_value: 0.7058
    paper_std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 134
    sort_value: 0.7058
    sort_std: 0.0042
    is_best: false
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.7003
    std: 0.0071
    paper_value: 0.7003
    paper_std: 0.0071
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7003
    sort_std: 0.0071
    is_best: false
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    value: 0.7003
    std: 0.0071
    paper_value: 0.7003
    paper_std: 0.0071
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7003
    sort_std: 0.0071
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6992
    std: 0.0061
    paper_value: 0.6992
    paper_std: 0.0061
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 16
    sort_value: 0.6992
    sort_std: 0.0061
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.6982
    std: 0.0053
    paper_value: 0.6982
    paper_std: 0.0053
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 181
    sort_value: 0.6982
    sort_std: 0.0053
    is_best: false
  - model: HAT
    model_key: hat
    model_plain: HAT
    value: 0.6814
    std: 0.0053
    paper_value: 0.6814
    paper_std: 0.0053
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.6814
    sort_std: 0.0053
    is_best: false
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    value: 0.6615
    std: 0.0045
    paper_value: 0.6615
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.6615
    sort_std: 0.0045
    is_best: false
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    value: 0.5406
    std: 0.0445
    paper_value: 0.5406
    paper_std: 0.0445
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.5406
    sort_std: 0.0445
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5258
    std: 0.0197
    paper_value: 0.5258
    paper_std: 0.0197
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 31
    sort_value: 0.5258
    sort_std: 0.0197
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  is_multi_metric: true
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    metric_values:
    - 0.9170999999999999
    - null
    metric_stds:
    - 0.0029
    - null
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
    is_best: true
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: DR
    model_key: dr
    model_plain: DR
    metric_values:
    - 0.9139
    - null
    metric_stds:
    - 0.0024
    - null
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
    is_best: true
    sort_value: 0.9139
    sort_std: 0.0024
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: LLP
    model_key: llp
    model_plain: LLP
    metric_values:
    - 0.8995
    - null
    metric_stds:
    - 0.0201
    - null
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
    is_best: true
    sort_value: 0.8995
    sort_std: 0.0201
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
    - 0.8229
    - 0.8229
    metric_stds:
    - 0.0046
    - 0.0046
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8825
    sort_std: 0.0053
    true_value: 0.8825
    true_std: 0.0053
    paper_value: 0.8229
    paper_std: 0.0046
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059599999999999986
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 31
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    metric_values:
    - 0.8
    - 0.8
    metric_stds:
    - 0.0085
    - 0.0085
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8796
    sort_std: 0.0037
    true_value: 0.8796
    true_std: 0.0037
    paper_value: 0.8
    paper_std: 0.0085
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0796
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 41
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.804
    - 0.804
    metric_stds:
    - 0.0053
    - 0.0053
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8778
    sort_std: 0.0096
    true_value: 0.8778
    true_std: 0.0096
    paper_value: 0.804
    paper_std: 0.0053
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07379999999999998
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 48
  - model: MLP
    model_key: mlp
    model_plain: MLP
    metric_values:
    - 0.5244
    - 0.5244
    metric_stds:
    - 0.0108
    - 0.0108
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8709
    sort_std: 0.0066
    true_value: 0.8709
    true_std: 0.0066
    paper_value: 0.5244
    paper_std: 0.0108
    has_value_gap: true
    has_value_note: false
    value_gap: 0.34650000000000003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 65
  - model: SGC
    model_key: sgc
    model_plain: SGC
    metric_values:
    - 0.7968
    - 0.7968
    metric_stds:
    - 0.0065
    - 0.0065
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.866
    sort_std: 0.003
    true_value: 0.866
    true_std: 0.003
    paper_value: 0.7968
    paper_std: 0.0065
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06920000000000004
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 78
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    metric_values:
    - 0.7888
    - 0.7888
    metric_stds:
    - 0.0087
    - 0.0087
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.836
    sort_std: null
    true_value: 0.836
    true_std: null
    paper_value: 0.7888
    paper_std: 0.0087
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04720000000000002
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 117
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    metric_values:
    - 0.8232
    - 0.8232
    metric_stds:
    - 0.007
    - 0.007
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8232
    sort_std: 0.007
    true_value: 0.8232
    true_std: 0.007
    paper_value: 0.8232
    paper_std: 0.007
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 139
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    metric_values:
    - null
    - 0.8232
    metric_stds:
    - null
    - 0.007
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8232
    sort_std: 0.007
    true_value: null
    true_std: null
    paper_value: 0.8232
    paper_std: 0.007
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    metric_values:
    - 0.8142
    - 0.8142
    metric_stds:
    - 0.0079
    - 0.0079
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8142
    sort_std: 0.0079
    true_value: 0.8142
    true_std: 0.0079
    paper_value: 0.8142
    paper_std: 0.0079
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 148
  - model: HAT
    model_key: hat
    model_plain: HAT
    metric_values:
    - 0.7981
    - 0.7981
    metric_stds:
    - 0.0058
    - 0.0058
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7981
    sort_std: 0.0058
    true_value: 0.7981
    true_std: 0.0058
    paper_value: 0.7981
    paper_std: 0.0058
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 156
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    metric_values:
    - 0.7963
    - 0.7963
    metric_stds:
    - 0.0057
    - 0.0057
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7963
    sort_std: 0.0057
    true_value: 0.7963
    true_std: 0.0057
    paper_value: 0.7963
    paper_std: 0.0057
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 158
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    metric_values:
    - 0.793
    - 0.793
    metric_stds:
    - 0.0051
    - 0.0051
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.793
    sort_std: 0.0051
    true_value: 0.793
    true_std: 0.0051
    paper_value: 0.793
    paper_std: 0.0051
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 161
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    metric_values:
    - 0.737
    - 0.737
    metric_stds:
    - 0.0069
    - 0.0069
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.737
    sort_std: 0.0069
    true_value: 0.737
    true_std: 0.0069
    paper_value: 0.737
    paper_std: 0.0069
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 209
  metrics:
  - Accuracy
  - F1
  primary_metric: Accuracy
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
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.7216
    std: 0.0296
    paper_value: 0.7216
    paper_std: 0.0296
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7216
    sort_std: 0.0296
    is_best: false
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    value: 0.7216
    std: 0.0296
    paper_value: 0.7216
    paper_std: 0.0296
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7216
    sort_std: 0.0296
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.7162
    std: 0.0213
    paper_value: 0.7162
    paper_std: 0.0213
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7162
    sort_std: 0.0213
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7054
    std: 0.0201
    paper_value: 0.7054
    paper_std: 0.0201
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 54
    sort_value: 0.7054
    sort_std: 0.0201
    is_best: false
  - model: HAT
    model_key: hat
    model_plain: HAT
    value: 0.7054
    std: 0.0167
    paper_value: 0.7054
    paper_std: 0.0167
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7054
    sort_std: 0.0167
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5838
    std: 0.0404
    paper_value: 0.5838
    paper_std: 0.0404
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 11
    sort_value: 0.5838
    sort_std: 0.0404
    is_best: false
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    value: 0.5595
    std: 0.0285
    paper_value: 0.5595
    paper_std: 0.0285
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.5595
    sort_std: 0.0285
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.5568
    std: 0.018
    paper_value: 0.5568
    paper_std: 0.018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 18
    sort_value: 0.5568
    sort_std: 0.018
    is_best: false
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    value: 0.5568
    std: 0.0559
    paper_value: 0.5568
    paper_std: 0.0559
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.5568
    sort_std: 0.0559
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5514
    std: 0.018
    paper_value: 0.5514
    paper_std: 0.018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    sort_value: 0.5514
    sort_std: 0.018
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5297
    std: 0.0287
    paper_value: 0.5297
    paper_std: 0.0287
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.5297
    sort_std: 0.0287
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.527
    std: 0.0142
    paper_value: 0.527
    paper_std: 0.0142
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.527
    sort_std: 0.0142
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4784
    std: 0.0177
    paper_value: 0.4784
    paper_std: 0.0177
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 27
    sort_value: 0.4784
    sort_std: 0.0177
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: D&D
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
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
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
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
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
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
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.92
    std: null
    paper_value: 0.92
    paper_std: null
    metric: mAP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1 (graph_reconstruction)
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.92
    sort_std: null
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.8913
    std: null
    paper_value: 0.8913
    paper_std: null
    metric: mAP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1 (graph_reconstruction)
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.8913
    sort_std: null
    is_best: false
  metric: Accuracy
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
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.7893
    std: 0.0027
    paper_value: 0.7893
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7893
    sort_std: 0.0027
    is_best: false
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.7852
    std: 0.0058
    paper_value: 0.7852
    paper_std: 0.0058
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7852
    sort_std: 0.0058
    is_best: false
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    value: 0.7852
    std: 0.0058
    paper_value: 0.7852
    paper_std: 0.0058
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7852
    sort_std: 0.0058
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7837
    std: 0.0026
    paper_value: 0.7837
    paper_std: 0.0026
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 5
    sort_value: 0.7837
    sort_std: 0.0026
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7814
    std: 0.0031
    paper_value: 0.7814
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 6
    sort_value: 0.7814
    sort_std: 0.0031
    is_best: false
  - model: HAT
    model_key: hat
    model_plain: HAT
    value: 0.775
    std: 0.0042
    paper_value: 0.775
    paper_std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.775
    sort_std: 0.0042
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7731
    std: 0.0059
    paper_value: 0.7731
    paper_std: 0.0059
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 126
    sort_value: 0.7731
    sort_std: 0.0059
    is_best: false
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    value: 0.7713
    std: 0.0059
    paper_value: 0.7713
    paper_std: 0.0059
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.7713
    sort_std: 0.0059
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.7672
    std: 0.0086
    paper_value: 0.7672
    paper_std: 0.0086
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 57
    sort_value: 0.7672
    sort_std: 0.0086
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.7567
    std: 0.0099
    paper_value: 0.7567
    paper_std: 0.0099
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 34
    sort_value: 0.7567
    sort_std: 0.0099
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.7511
    std: 0.0127
    paper_value: 0.7511
    paper_std: 0.0127
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 104
    sort_value: 0.7511
    sort_std: 0.0127
    is_best: false
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    value: 0.6861
    std: 0.0305
    paper_value: 0.6861
    paper_std: 0.0305
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.6861
    sort_std: 0.0305
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6717
    std: 0.0091
    paper_value: 0.6717
    paper_std: 0.0091
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 3
    sort_value: 0.6717
    sort_std: 0.0091
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  is_multi_metric: true
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    metric_values:
    - 0.9656
    - null
    metric_stds:
    - 0.02
    - null
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
    is_best: true
    sort_value: 0.9656
    sort_std: 0.02
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    metric_values:
    - 0.9574
    - null
    metric_stds:
    - 0.0222
    - null
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
    is_best: true
    sort_value: 0.9574
    sort_std: 0.0222
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    metric_values:
    - 0.9475
    - null
    metric_stds:
    - 0.0309
    - null
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
    is_best: true
    sort_value: 0.9475
    sort_std: 0.0309
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: MLP
    model_key: mlp
    model_plain: MLP
    metric_values:
    - 0.7054
    - 0.7054
    metric_stds:
    - 0.03
    - 0.03
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.923
    sort_std: 0.007
    true_value: 0.923
    true_std: 0.007
    paper_value: 0.7054
    paper_std: 0.03
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21760000000000002
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 14
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    metric_values:
    - 0.5459
    - 0.5459
    metric_stds:
    - 0.0393
    - 0.0393
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9189
    sort_std: 0.0393
    true_value: 0.9189
    true_std: 0.0393
    paper_value: 0.5459
    paper_std: 0.0393
    has_value_gap: true
    has_value_note: false
    value_gap: 0.373
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: 17
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    metric_values:
    - null
    - 0.8919
    metric_stds:
    - null
    - 0.0237
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8919
    sort_std: 0.0237
    true_value: null
    true_std: null
    paper_value: 0.8919
    paper_std: 0.0237
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    metric_values:
    - 0.8919
    - null
    metric_stds:
    - 0.0237
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8919
    sort_std: 0.0237
    true_value: 0.8919
    true_std: 0.0237
    paper_value: 0.8919
    paper_std: 0.0237
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 22
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    metric_values:
    - 0.8865
    - 0.8865
    metric_stds:
    - 0.0206
    - 0.0206
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8865
    sort_std: 0.0206
    true_value: 0.8865
    true_std: 0.0206
    paper_value: 0.8865
    paper_std: 0.0206
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 27
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.5784
    - 0.5784
    metric_stds:
    - 0.0162
    - 0.0162
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8311
    sort_std: 0.032
    true_value: 0.8311
    true_std: 0.032
    paper_value: 0.5784
    paper_std: 0.0162
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2526999999999999
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 46
  - model: HAT
    model_key: hat
    model_plain: HAT
    metric_values:
    - 0.8216
    - 0.8216
    metric_stds:
    - 0.0252
    - 0.0252
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8216
    sort_std: 0.0252
    true_value: 0.8216
    true_std: 0.0252
    paper_value: 0.8216
    paper_std: 0.0252
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 54
  - model: GAT
    model_key: gat
    model_plain: GAT
    metric_values:
    - 0.5946
    - 0.5946
    metric_stds:
    - 0.0112
    - 0.0112
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8082
    sort_std: 0.0213
    true_value: 0.8082
    true_std: 0.0213
    paper_value: 0.5946
    paper_std: 0.0112
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2136
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 61
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    metric_values:
    - 0.6838
    - 0.6838
    metric_stds:
    - 0.0354
    - 0.0354
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.793
    sort_std: 0.012
    true_value: 0.793
    true_std: 0.012
    paper_value: 0.6838
    paper_std: 0.0354
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10920000000000007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 65
  - model: SGC
    model_key: sgc
    model_plain: SGC
    metric_values:
    - 0.5757
    - 0.5757
    metric_stds:
    - 0.0296
    - 0.0296
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5757
    sort_std: 0.0296
    true_value: 0.5757
    true_std: 0.0296
    paper_value: 0.5757
    paper_std: 0.0296
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 151
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    metric_values:
    - 0.5622
    - 0.5622
    metric_stds:
    - 0.0438
    - 0.0438
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5622
    sort_std: 0.0438
    true_value: 0.5622
    true_std: 0.0438
    paper_value: 0.5622
    paper_std: 0.0438
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 156
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    metric_values:
    - 0.5135
    - 0.5135
    metric_stds:
    - 0.0344
    - 0.0344
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5135
    sort_std: 0.0344
    true_value: 0.5135
    true_std: 0.0344
    paper_value: 0.5135
    paper_std: 0.0344
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 163
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    metric_values:
    - 0.5081
    - 0.5081
    metric_stds:
    - 0.036
    - 0.036
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5081
    sort_std: 0.036
    true_value: 0.5081
    true_std: 0.036
    paper_value: 0.5081
    paper_std: 0.036
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 164
  metrics:
  - Accuracy
  - F1
  primary_metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: \modelname{}
    model_key: \modelname{}
    model_plain: \modelname{}
    value: 0.836
    std: 0.0114
    paper_value: 0.836
    paper_std: 0.0114
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.836
    sort_std: 0.0114
    is_best: false
  - model: Proposed Model (denoted as \modelname{})
    model_key: proposed model (denoted as \modelname{})
    model_plain: Proposed Model (denoted as \modelname{})
    value: 0.836
    std: 0.0114
    paper_value: 0.836
    paper_std: 0.0114
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.836
    sort_std: 0.0114
    is_best: false
  - model: FPS-T
    model_key: fps-t
    model_plain: FPS-T
    value: 0.836
    std: 0.0114
    paper_value: 0.836
    paper_std: 0.0114
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.836
    sort_std: 0.0114
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.83
    std: 0.0065
    paper_value: 0.83
    paper_std: 0.0065
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.83
    sort_std: 0.0065
    is_best: false
  - model: HAT
    model_key: hat
    model_plain: HAT
    value: 0.818
    std: 0.0136
    paper_value: 0.818
    paper_std: 0.0136
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.818
    sort_std: 0.0136
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.812
    std: 0.0187
    paper_value: 0.812
    paper_std: 0.0187
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 2
    sort_value: 0.812
    sort_std: 0.0187
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.784
    std: 0.0052
    paper_value: 0.784
    paper_std: 0.0052
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 77
    sort_value: 0.784
    sort_std: 0.0052
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.556
    std: 0.0253
    paper_value: 0.556
    paper_std: 0.0253
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 13
    sort_value: 0.556
    sort_std: 0.0253
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.546
    std: 0.0268
    paper_value: 0.546
    paper_std: 0.0268
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.546
    sort_std: 0.0268
    is_best: false
  - model: \mathcal{Q}-GCN
    model_key: \mathcal{q}-gcn
    model_plain: \mathcal{Q}-GCN
    value: 0.528
    std: 0.022
    paper_value: 0.528
    paper_std: 0.022
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.528
    sort_std: 0.022
    is_best: false
  - model: Q-GCN
    model_key: q-gcn
    model_plain: Q-GCN
    value: 0.528
    std: 0.022
    paper_value: 0.528
    paper_std: 0.022
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.528
    sort_std: 0.022
    is_best: false
  - model: \kappa-GCN
    model_key: \kappa-gcn
    model_plain: \kappa-GCN
    value: 0.466
    std: 0.0241
    paper_value: 0.466
    paper_std: 0.0241
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.466
    sort_std: 0.0241
    is_best: false
  - model: κ-GCN
    model_key: κ-gcn
    model_plain: κ-GCN
    value: 0.466
    std: 0.0241
    paper_value: 0.466
    paper_std: 0.0241
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: null
    sort_value: 0.466
    sort_std: 0.0241
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.464
    std: 0.0201
    paper_value: 0.464
    paper_std: 0.0201
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 121
    sort_value: 0.464
    sort_std: 0.0201
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.462
    std: 0.023
    paper_value: 0.462
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
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 61
    sort_value: 0.462
    sort_std: 0.023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.454
    std: 0.0262
    paper_value: 0.454
    paper_std: 0.0262
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 53
    sort_value: 0.454
    sort_std: 0.0262
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
  - *id007
- benchmark: TU Dortmund
  datasets:
  - *id008
main_figure: /figures/2309.04082/main_figure.png
---

