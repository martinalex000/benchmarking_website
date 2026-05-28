---
title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
arxiv_id: '2406.16321'
source_url: ''
authors: []
published_date: Jun 2024
published_date_iso: 2024-06
abstract: Graph machine learning has made significant strides in recent years, yet
  the integration of visual information with graph structure and its potential for
  improving performance in downstream tasks remains an underexplored area. To address
  this critical gap, we introduce the Multimodal Graph Benchmark, a pioneering benchmark
  that incorporates both visual and textual information into graph learning tasks.
  extends beyond existing text-attributed graph benchmarks, offering a more comprehensive
  evaluation framework for multimodal graph learning. Our benchmark comprises seven
  diverse datasets of varying scales (ranging from thousands to millions of edges),
  designed to assess algorithms across different tasks in real-world scenarios. These
  datasets feature rich multimodal node attributes, including visual data, which enables
  a more holistic evaluation of various graph learning frameworks in complex, multimodal
  environments. To support advancements in this emerging field, we provide an extensive
  empirical study on various graph learning frameworks when presented with features
  from multiple modalities, particularly emphasizing the impact of visual information.
  This study offers valuable insights into the challenges and opportunities of integrating
  visual data into graph learning.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Classic
- TU Dortmund
- Hypergraph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
  dataset: AMAP
  rows:
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.67
    std: 0.1
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.67
    sort_std: 0.1
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.65
    std: 0.07
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.65
    sort_std: 0.07
    is_best: true
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.61
    std: 0.16
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.16
    is_best: true
  - model: SAGE + ImageBind
    model_key: sage + imagebind
    model_plain: SAGE + ImageBind
    value: 0.252
    std: 0.0009
    paper_value: 0.252
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.252
    sort_std: 0.0009
    is_best: false
  - model: MMGCN + ImageBind
    model_key: mmgcn + imagebind
    model_plain: MMGCN + ImageBind
    value: 0.2472
    std: 0.0019
    paper_value: 0.2472
    paper_std: 0.0019
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2472
    sort_std: 0.0019
    is_best: false
  - model: SAGE + CLIP
    model_key: sage + clip
    model_plain: SAGE + CLIP
    value: 0.2458
    std: 0.0018
    paper_value: 0.2458
    paper_std: 0.0018
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2458
    sort_std: 0.0018
    is_best: false
  - model: BUDDY + ImageBind
    model_key: buddy + imagebind
    model_plain: BUDDY + ImageBind
    value: 0.2435
    std: 0.0024
    paper_value: 0.2435
    paper_std: 0.0024
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2435
    sort_std: 0.0024
    is_best: false
  - model: BUDDY + CLIP
    model_key: buddy + clip
    model_plain: BUDDY + CLIP
    value: 0.2344
    std: 0.0026
    paper_value: 0.2344
    paper_std: 0.0026
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2344
    sort_std: 0.0026
    is_best: false
  - model: SAGE + ViT/T5
    model_key: sage + vit/t5
    model_plain: SAGE + ViT/T5
    value: 0.2311
    std: 0.0005
    paper_value: 0.2311
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2311
    sort_std: 0.0005
    is_best: false
  - model: SAGE + DINOv2/T5
    model_key: sage + dinov2/t5
    model_plain: SAGE + DINOv2/T5
    value: 0.2298
    std: 0.0001
    paper_value: 0.2298
    paper_std: 0.0001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2298
    sort_std: 0.0001
    is_best: false
  - model: BUDDY + DINOv2/T5
    model_key: buddy + dinov2/t5
    model_plain: BUDDY + DINOv2/T5
    value: 0.2295
    std: 0.0006
    paper_value: 0.2295
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2295
    sort_std: 0.0006
    is_best: false
  - model: BUDDY + ViT/T5
    model_key: buddy + vit/t5
    model_plain: BUDDY + ViT/T5
    value: 0.2282
    std: 0.0019
    paper_value: 0.2282
    paper_std: 0.0019
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2282
    sort_std: 0.0019
    is_best: false
  - model: GCN + ImageBind
    model_key: gcn + imagebind
    model_plain: GCN + ImageBind
    value: 0.2281
    std: 0.0003
    paper_value: 0.2281
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2281
    sort_std: 0.0003
    is_best: false
  - model: MMGCN + CLIP
    model_key: mmgcn + clip
    model_plain: MMGCN + CLIP
    value: 0.2228
    std: 0.0005
    paper_value: 0.2228
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2228
    sort_std: 0.0005
    is_best: false
  - model: MLP + ImageBind
    model_key: mlp + imagebind
    model_plain: MLP + ImageBind
    value: 0.2218
    std: 0.0002
    paper_value: 0.2218
    paper_std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2218
    sort_std: 0.0002
    is_best: false
  - model: MGAT + ImageBind
    model_key: mgat + imagebind
    model_plain: MGAT + ImageBind
    value: 0.2213
    std: 0.0027
    paper_value: 0.2213
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2213
    sort_std: 0.0027
    is_best: false
  - model: MMGCN + ViT/T5
    model_key: mmgcn + vit/t5
    model_plain: MMGCN + ViT/T5
    value: 0.216
    std: 0.0005
    paper_value: 0.216
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.216
    sort_std: 0.0005
    is_best: false
  - model: MGAT + DINOv2/T5
    model_key: mgat + dinov2/t5
    model_plain: MGAT + DINOv2/T5
    value: 0.2142
    std: 0.0013
    paper_value: 0.2142
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2142
    sort_std: 0.0013
    is_best: false
  - model: MGAT + CLIP
    model_key: mgat + clip
    model_plain: MGAT + CLIP
    value: 0.2138
    std: 0.0023
    paper_value: 0.2138
    paper_std: 0.0023
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2138
    sort_std: 0.0023
    is_best: false
  - model: MMGCN + DINOv2/T5
    model_key: mmgcn + dinov2/t5
    model_plain: MMGCN + DINOv2/T5
    value: 0.2119
    std: 0.0008
    paper_value: 0.2119
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2119
    sort_std: 0.0008
    is_best: false
  - model: MLP + CLIP
    model_key: mlp + clip
    model_plain: MLP + CLIP
    value: 0.211
    std: 0.0004
    paper_value: 0.211
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.211
    sort_std: 0.0004
    is_best: false
  - model: MGAT + ViT/T5
    model_key: mgat + vit/t5
    model_plain: MGAT + ViT/T5
    value: 0.2059
    std: 0.0041
    paper_value: 0.2059
    paper_std: 0.0041
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2059
    sort_std: 0.0041
    is_best: false
  - model: MLP + ViT/T5
    model_key: mlp + vit/t5
    model_plain: MLP + ViT/T5
    value: 0.1765
    std: 0.0006
    paper_value: 0.1765
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.1765
    sort_std: 0.0006
    is_best: false
  - model: MLP + DINOv2/T5
    model_key: mlp + dinov2/t5
    model_plain: MLP + DINOv2/T5
    value: 0.1753
    std: 0.0011
    paper_value: 0.1753
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.1753
    sort_std: 0.0011
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Amazon-Photo
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9712
    std: 0.0024
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.9712
    sort_std: 0.0024
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9678
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.966
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: SAGE + ImageBind
    model_key: sage + imagebind
    model_plain: SAGE + ImageBind
    value: 0.3432
    std: 0.0011
    paper_value: 0.3432
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3432
    sort_std: 0.0011
    is_best: false
  - model: SAGE + CLIP
    model_key: sage + clip
    model_plain: SAGE + CLIP
    value: 0.3383
    std: 0.0008
    paper_value: 0.3383
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3383
    sort_std: 0.0008
    is_best: false
  - model: BUDDY + ImageBind
    model_key: buddy + imagebind
    model_plain: BUDDY + ImageBind
    value: 0.3302
    std: 0.0044
    paper_value: 0.3302
    paper_std: 0.0044
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3302
    sort_std: 0.0044
    is_best: false
  - model: SAGE + DINOv2/T5
    model_key: sage + dinov2/t5
    model_plain: SAGE + DINOv2/T5
    value: 0.322
    std: 0.0012
    paper_value: 0.322
    paper_std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.322
    sort_std: 0.0012
    is_best: false
  - model: SAGE + ViT/T5
    model_key: sage + vit/t5
    model_plain: SAGE + ViT/T5
    value: 0.3201
    std: 0.001
    paper_value: 0.3201
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3201
    sort_std: 0.001
    is_best: false
  - model: MMGCN + ImageBind
    model_key: mmgcn + imagebind
    model_plain: MMGCN + ImageBind
    value: 0.3174
    std: 0.0021
    paper_value: 0.3174
    paper_std: 0.0021
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3174
    sort_std: 0.0021
    is_best: false
  - model: GCN + ImageBind
    model_key: gcn + imagebind
    model_plain: GCN + ImageBind
    value: 0.3167
    std: 0.0009
    paper_value: 0.3167
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3167
    sort_std: 0.0009
    is_best: false
  - model: BUDDY + CLIP
    model_key: buddy + clip
    model_plain: BUDDY + CLIP
    value: 0.3155
    std: 0.0013
    paper_value: 0.3155
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3155
    sort_std: 0.0013
    is_best: false
  - model: MMGCN + CLIP
    model_key: mmgcn + clip
    model_plain: MMGCN + CLIP
    value: 0.3138
    std: 0.0008
    paper_value: 0.3138
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3138
    sort_std: 0.0008
    is_best: false
  - model: MMGCN + ViT/T5
    model_key: mmgcn + vit/t5
    model_plain: MMGCN + ViT/T5
    value: 0.3083
    std: 0.0007
    paper_value: 0.3083
    paper_std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3083
    sort_std: 0.0007
    is_best: false
  - model: MLP + ImageBind
    model_key: mlp + imagebind
    model_plain: MLP + ImageBind
    value: 0.3045
    std: 0.0014
    paper_value: 0.3045
    paper_std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3045
    sort_std: 0.0014
    is_best: false
  - model: MMGCN + DINOv2/T5
    model_key: mmgcn + dinov2/t5
    model_plain: MMGCN + DINOv2/T5
    value: 0.3042
    std: 0.0002
    paper_value: 0.3042
    paper_std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3042
    sort_std: 0.0002
    is_best: false
  - model: BUDDY + ViT/T5
    model_key: buddy + vit/t5
    model_plain: BUDDY + ViT/T5
    value: 0.3041
    std: 0.004
    paper_value: 0.3041
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3041
    sort_std: 0.004
    is_best: false
  - model: MGAT + ViT/T5
    model_key: mgat + vit/t5
    model_plain: MGAT + ViT/T5
    value: 0.3015
    std: 0.0034
    paper_value: 0.3015
    paper_std: 0.0034
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3015
    sort_std: 0.0034
    is_best: false
  - model: MGAT + ImageBind
    model_key: mgat + imagebind
    model_plain: MGAT + ImageBind
    value: 0.3015
    std: 0.0012
    paper_value: 0.3015
    paper_std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3015
    sort_std: 0.0012
    is_best: false
  - model: BUDDY + DINOv2/T5
    model_key: buddy + dinov2/t5
    model_plain: BUDDY + DINOv2/T5
    value: 0.3002
    std: 0.0034
    paper_value: 0.3002
    paper_std: 0.0034
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.3002
    sort_std: 0.0034
    is_best: false
  - model: MGAT + DINOv2/T5
    model_key: mgat + dinov2/t5
    model_plain: MGAT + DINOv2/T5
    value: 0.2891
    std: 0.0009
    paper_value: 0.2891
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2891
    sort_std: 0.0009
    is_best: false
  - model: MLP + CLIP
    model_key: mlp + clip
    model_plain: MLP + CLIP
    value: 0.2822
    std: 0.0009
    paper_value: 0.2822
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2822
    sort_std: 0.0009
    is_best: false
  - model: MGAT + CLIP
    model_key: mgat + clip
    model_plain: MGAT + CLIP
    value: 0.2756
    std: 0.003
    paper_value: 0.2756
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2756
    sort_std: 0.003
    is_best: false
  - model: MLP + ViT/T5
    model_key: mlp + vit/t5
    model_plain: MLP + ViT/T5
    value: 0.2481
    std: 0.0005
    paper_value: 0.2481
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2481
    sort_std: 0.0005
    is_best: false
  - model: MLP + DINOv2/T5
    model_key: mlp + dinov2/t5
    model_plain: MLP + DINOv2/T5
    value: 0.2481
    std: 0.0016
    paper_value: 0.2481
    paper_std: 0.0016
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: null
    sort_value: 0.2481
    sort_std: 0.0016
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
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
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
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
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
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
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SAGE (CLIP/CLIP)
    model_key: sage (clip/clip)
    model_plain: SAGE (CLIP/CLIP)
    metric_values:
    - 0.833
    - null
    metric_stds:
    - 0.0002
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.833
    sort_std: 0.0002
    true_value: 0.833
    true_std: 0.0002
    paper_value: 0.833
    paper_std: 0.0002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 18
  - model: SAGE + ViT/T5
    model_key: sage + vit/t5
    model_plain: SAGE + ViT/T5
    metric_values:
    - 0.8303
    - 0.4479
    metric_stds:
    - 0.0004
    - 0.0018
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8303
    sort_std: 0.0004
    true_value: 0.8303
    true_std: 0.0004
    paper_value: 0.8303
    paper_std: 0.0004
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 19
  - model: SAGE + DINOv2/T5
    model_key: sage + dinov2/t5
    model_plain: SAGE + DINOv2/T5
    metric_values:
    - 0.8299
    - 0.4561
    metric_stds:
    - 0.0008
    - 0.0022
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8299
    sort_std: 0.0008
    true_value: 0.8299
    true_std: 0.0008
    paper_value: 0.8299
    paper_std: 0.0008
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 20
  - model: MMGCN + DINOv2/T5
    model_key: mmgcn + dinov2/t5
    model_plain: MMGCN + DINOv2/T5
    metric_values:
    - 0.8171
    - 0.2821
    metric_stds:
    - 0.0003
    - 0.0112
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8171
    sort_std: 0.0003
    true_value: 0.8171
    true_std: 0.0003
    paper_value: 0.8171
    paper_std: 0.0003
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 24
  - model: MMGCN + ViT/T5
    model_key: mmgcn + vit/t5
    model_plain: MMGCN + ViT/T5
    metric_values:
    - 0.8167
    - 0.265
    metric_stds:
    - 0.0003
    - 0.001
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8167
    sort_std: 0.0003
    true_value: 0.8167
    true_std: 0.0003
    paper_value: 0.8167
    paper_std: 0.0003
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 25
  - model: MMGCN (CLIP/CLIP)
    model_key: mmgcn (clip/clip)
    model_plain: MMGCN (CLIP/CLIP)
    metric_values:
    - 0.8161
    - null
    metric_stds:
    - 0.0001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8161
    sort_std: 0.0001
    true_value: 0.8161
    true_std: 0.0001
    paper_value: 0.8161
    paper_std: 0.0001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 26
  - model: SAGE (ImageBind/ImageBind)
    model_key: sage (imagebind/imagebind)
    model_plain: SAGE (ImageBind/ImageBind)
    metric_values:
    - 0.8039
    - null
    metric_stds:
    - 0.0021
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8039
    sort_std: 0.0021
    true_value: 0.8039
    true_std: 0.0021
    paper_value: 0.8039
    paper_std: 0.0021
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 29
  - model: GCN (ImageBind/ImageBind)
    model_key: gcn (imagebind/imagebind)
    model_plain: GCN (ImageBind/ImageBind)
    metric_values:
    - 0.7891
    - null
    metric_stds:
    - 0.0004
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7891
    sort_std: 0.0004
    true_value: 0.7891
    true_std: 0.0004
    paper_value: 0.7891
    paper_std: 0.0004
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 30
  - model: MGAT (CLIP/CLIP)
    model_key: mgat (clip/clip)
    model_plain: MGAT (CLIP/CLIP)
    metric_values:
    - 0.7648
    - null
    metric_stds:
    - 0.0059
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7648
    sort_std: 0.0059
    true_value: 0.7648
    true_std: 0.0059
    paper_value: 0.7648
    paper_std: 0.0059
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 33
  - model: MGAT + ViT/T5
    model_key: mgat + vit/t5
    model_plain: MGAT + ViT/T5
    metric_values:
    - 0.7543
    - 0.7526
    metric_stds:
    - 0.0076
    - 0.0121
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7543
    sort_std: 0.0076
    true_value: 0.7543
    true_std: 0.0076
    paper_value: 0.7543
    paper_std: 0.0076
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 40
  - model: MGAT + DINOv2/T5
    model_key: mgat + dinov2/t5
    model_plain: MGAT + DINOv2/T5
    metric_values:
    - 0.7498
    - 0.7489
    metric_stds:
    - 0.0123
    - 0.0146
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7498
    sort_std: 0.0123
    true_value: 0.7498
    true_std: 0.0123
    paper_value: 0.7498
    paper_std: 0.0123
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 41
  - model: MGAT + ImageBind
    model_key: mgat + imagebind
    model_plain: MGAT + ImageBind
    metric_values:
    - null
    - 0.7477
    metric_stds:
    - null
    - 0.0049
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7477
    sort_std: 0.0049
    true_value: null
    true_std: null
    paper_value: 0.7477
    paper_std: 0.0049
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MGAT + CLIP
    model_key: mgat + clip
    model_plain: MGAT + CLIP
    metric_values:
    - null
    - 0.7475
    metric_stds:
    - null
    - 0.0123
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7475
    sort_std: 0.0123
    true_value: null
    true_std: null
    paper_value: 0.7475
    paper_std: 0.0123
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MLP (CLIP/CLIP)
    model_key: mlp (clip/clip)
    model_plain: MLP (CLIP/CLIP)
    metric_values:
    - 0.7229
    - null
    metric_stds:
    - 0.0002
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7229
    sort_std: 0.0002
    true_value: 0.7229
    true_std: 0.0002
    paper_value: 0.7229
    paper_std: 0.0002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 43
  - model: MLP + DINOv2/T5
    model_key: mlp + dinov2/t5
    model_plain: MLP + DINOv2/T5
    metric_values:
    - 0.6883
    - 0.1028
    metric_stds:
    - 0.0003
    - 0.0004
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6883
    sort_std: 0.0003
    true_value: 0.6883
    true_std: 0.0003
    paper_value: 0.6883
    paper_std: 0.0003
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 45
  - model: MLP + ViT/T5
    model_key: mlp + vit/t5
    model_plain: MLP + ViT/T5
    metric_values:
    - 0.6782
    - 0.111
    metric_stds:
    - 0.0007
    - 0.0017
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6782
    sort_std: 0.0007
    true_value: 0.6782
    true_std: 0.0007
    paper_value: 0.6782
    paper_std: 0.0007
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 46
  - model: MMGCN (ImageBind/ImageBind)
    model_key: mmgcn (imagebind/imagebind)
    model_plain: MMGCN (ImageBind/ImageBind)
    metric_values:
    - 0.5875
    - null
    metric_stds:
    - 0.0005
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.5875
    sort_std: 0.0005
    true_value: 0.5875
    true_std: 0.0005
    paper_value: 0.5875
    paper_std: 0.0005
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 65
  - model: SAGE + CLIP
    model_key: sage + clip
    model_plain: SAGE + CLIP
    metric_values:
    - null
    - 0.441
    metric_stds:
    - null
    - 0.0137
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.441
    sort_std: 0.0137
    true_value: null
    true_std: null
    paper_value: 0.441
    paper_std: 0.0137
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BUDDY + CLIP
    model_key: buddy + clip
    model_plain: BUDDY + CLIP
    metric_values:
    - null
    - 0.4325
    metric_stds:
    - null
    - 0.0023
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.4325
    sort_std: 0.0023
    true_value: null
    true_std: null
    paper_value: 0.4325
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BUDDY + DINOv2/T5
    model_key: buddy + dinov2/t5
    model_plain: BUDDY + DINOv2/T5
    metric_values:
    - null
    - 0.4325
    metric_stds:
    - null
    - 0.0013
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.4325
    sort_std: 0.0013
    true_value: null
    true_std: null
    paper_value: 0.4325
    paper_std: 0.0013
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BUDDY + ViT/T5
    model_key: buddy + vit/t5
    model_plain: BUDDY + ViT/T5
    metric_values:
    - null
    - 0.4318
    metric_stds:
    - null
    - 0.0053
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.4318
    sort_std: 0.0053
    true_value: null
    true_std: null
    paper_value: 0.4318
    paper_std: 0.0053
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BUDDY + ImageBind
    model_key: buddy + imagebind
    model_plain: BUDDY + ImageBind
    metric_values:
    - null
    - 0.4156
    metric_stds:
    - null
    - 0.0061
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.4156
    sort_std: 0.0061
    true_value: null
    true_std: null
    paper_value: 0.4156
    paper_std: 0.0061
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SAGE + ImageBind
    model_key: sage + imagebind
    model_plain: SAGE + ImageBind
    metric_values:
    - null
    - 0.3461
    metric_stds:
    - null
    - 0.0043
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.3461
    sort_std: 0.0043
    true_value: null
    true_std: null
    paper_value: 0.3461
    paper_std: 0.0043
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GCN + ImageBind
    model_key: gcn + imagebind
    model_plain: GCN + ImageBind
    metric_values:
    - null
    - 0.2756
    metric_stds:
    - null
    - 0.0126
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2756
    sort_std: 0.0126
    true_value: null
    true_std: null
    paper_value: 0.2756
    paper_std: 0.0126
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MMGCN + ImageBind
    model_key: mmgcn + imagebind
    model_plain: MMGCN + ImageBind
    metric_values:
    - null
    - 0.2632
    metric_stds:
    - null
    - 0.0023
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2632
    sort_std: 0.0023
    true_value: null
    true_std: null
    paper_value: 0.2632
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MMGCN + CLIP
    model_key: mmgcn + clip
    model_plain: MMGCN + CLIP
    metric_values:
    - null
    - 0.2534
    metric_stds:
    - null
    - 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2534
    sort_std: 0.0006
    true_value: null
    true_std: null
    paper_value: 0.2534
    paper_std: 0.0006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MLP + CLIP
    model_key: mlp + clip
    model_plain: MLP + CLIP
    metric_values:
    - null
    - 0.1103
    metric_stds:
    - null
    - 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.1103
    sort_std: 0.0006
    true_value: null
    true_std: null
    paper_value: 0.1103
    paper_std: 0.0006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: MLP + ImageBind
    model_key: mlp + imagebind
    model_plain: MLP + ImageBind
    metric_values:
    - null
    - 0.0773
    metric_stds:
    - null
    - 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.0773
    sort_std: 0.0006
    true_value: null
    true_std: null
    paper_value: 0.0773
    paper_std: 0.0006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - Accuracy
  - MRR
  primary_metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id003
main_figure: /figures/2406.16321/main_figure.png
---

