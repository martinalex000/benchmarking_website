---
title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
arxiv_id: '2406.16321'
authors: []
published_date: Jun 2024
abstract: Graph machine learning has made significant strides in recent years, yet
  the integration of visual information with graph structure and its potential for
  improving performance in downstream tasks remains an underexplored area. To address
  this critical gap, we introduce the Multimodal Graph Benchmark ( ), a pioneering
  benchmark that incorporates both visual and textual information into graph learning
  tasks. extends beyond existing text-attributed graph benchmarks, offering a more
  comprehensive evaluation framework for multimodal graph learning. Our benchmark
  comprises seven diverse datasets of varying scales (ranging from thousands to millions
  of edges), designed to assess algorithms across different tasks in real-world scenarios.
  These datasets feature rich multimodal node attributes, including visual data, which
  enables a more holistic evaluation of various graph learning frameworks in complex,
  multimodal environments. To support advancements in this emerging field, we provide
  an extensive empirical study on various graph learning frameworks when presented
  with features from multiple modalities, particularly emphasizing the impact of visual
  information. This study offers valuable insights into the challenges and opportunities
  of integrating visual data into graph learning.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models: []
mrr: null
results:
- &id003
  dataset: AMAP
  rows:
  - model: DMON
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: SUBLIME
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: VGAER
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: SAGE + ImageBind
    value: 0.252
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + ImageBind
    value: 0.2472
    std: 0.0019
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + CLIP
    value: 0.2458
    std: 0.0018
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + ImageBind
    value: 0.2435
    std: 0.0024
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + CLIP
    value: 0.2344
    std: 0.0026
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + ViT/T5
    value: 0.2311
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + DINOv2/T5
    value: 0.2298
    std: 0.0001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + DINOv2/T5
    value: 0.2295
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + ViT/T5
    value: 0.2282
    std: 0.0019
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN + ImageBind
    value: 0.2281
    std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + CLIP
    value: 0.2228
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + ImageBind
    value: 0.2218
    std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + ImageBind
    value: 0.2213
    std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + ViT/T5
    value: 0.216
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + DINOv2/T5
    value: 0.2142
    std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + CLIP
    value: 0.2138
    std: 0.0023
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + DINOv2/T5
    value: 0.2119
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + CLIP
    value: 0.211
    std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + ViT/T5
    value: 0.2059
    std: 0.0041
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + ViT/T5
    value: 0.1765
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + DINOv2/T5
    value: 0.1753
    std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Amazon-Photo
  rows:
  - model: GENs
    value: 0.9712000000000001
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GraphSAGE
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GAT
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: SAGE + ImageBind
    value: 0.3432
    std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + CLIP
    value: 0.3383
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + ImageBind
    value: 0.3302
    std: 0.0044
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + DINOv2/T5
    value: 0.322
    std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: SAGE + ViT/T5
    value: 0.3201
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + ImageBind
    value: 0.3174
    std: 0.0021
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN + ImageBind
    value: 0.3167
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + CLIP
    value: 0.3155
    std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + CLIP
    value: 0.3138
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + ViT/T5
    value: 0.3083
    std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + ImageBind
    value: 0.3045
    std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MMGCN + DINOv2/T5
    value: 0.3042
    std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + ViT/T5
    value: 0.3041
    std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + ViT/T5
    value: 0.3015
    std: 0.0034
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + ImageBind
    value: 0.3015
    std: 0.0012
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BUDDY + DINOv2/T5
    value: 0.3002
    std: 0.0034
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + DINOv2/T5
    value: 0.2891
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + CLIP
    value: 0.2822
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MGAT + CLIP
    value: 0.2756
    std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + ViT/T5
    value: 0.2481
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP + DINOv2/T5
    value: 0.2481
    std: 0.0016
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
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
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: SAGE (CLIP/CLIP)
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
    is_best: false
    global_rank: 18
  - model: SAGE + ViT/T5
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
    is_best: false
    global_rank: 19
  - model: SAGE + DINOv2/T5
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
    is_best: false
    global_rank: 20
  - model: MMGCN + DINOv2/T5
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
    is_best: false
    global_rank: 24
  - model: MMGCN + ViT/T5
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
    is_best: false
    global_rank: 25
  - model: MMGCN (CLIP/CLIP)
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
    is_best: false
    global_rank: 26
  - model: SAGE (ImageBind/ImageBind)
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
    is_best: false
    global_rank: 29
  - model: GCN (ImageBind/ImageBind)
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
    is_best: false
    global_rank: 30
  - model: MGAT (CLIP/CLIP)
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
    is_best: false
    global_rank: 32
  - model: MGAT + ViT/T5
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
    is_best: false
    global_rank: 37
  - model: MGAT + DINOv2/T5
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
    is_best: false
    global_rank: 38
  - model: MLP (CLIP/CLIP)
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
    is_best: false
    global_rank: 39
  - model: MLP + DINOv2/T5
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
    is_best: false
    global_rank: 41
  - model: MLP + ViT/T5
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
    is_best: false
    global_rank: 42
  - model: MMGCN (ImageBind/ImageBind)
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
    is_best: false
    global_rank: 61
  - model: MMGCN + CLIP
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
    is_best: false
    global_rank: null
  - model: MMGCN + ImageBind
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
    is_best: false
    global_rank: null
  - model: MGAT + CLIP
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
    is_best: false
    global_rank: null
  - model: MGAT + ImageBind
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
    is_best: false
    global_rank: null
  - model: GCN + ImageBind
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
    is_best: false
    global_rank: null
  - model: SAGE + CLIP
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
    is_best: false
    global_rank: null
  - model: SAGE + ImageBind
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
    is_best: false
    global_rank: null
  - model: BUDDY + CLIP
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
    is_best: false
    global_rank: null
  - model: BUDDY + ViT/T5
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
    is_best: false
    global_rank: null
  - model: BUDDY + ImageBind
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
    is_best: false
    global_rank: null
  - model: BUDDY + DINOv2/T5
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
    is_best: false
    global_rank: null
  - model: MLP + CLIP
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
    is_best: false
    global_rank: null
  - model: MLP + ImageBind
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

