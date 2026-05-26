---
title: AMAP
slug: amap
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: Amazon Photography co-purchase hypergraph node classification (8 categories).
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Amazon.html
stats:
  num_graphs: 1
  avg_nodes: null
  avg_edges: null
  num_classes: 8
result_count: 45
best_model:
  model: DMON
  value: 0.67
  metric: F1
  arxiv_id: '2508.14097'
  paper_title: Non-Dissipative Graph Propagation for Non-Local Community Detection
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - AUROC
  - MRR
  rows:
  - model: DMON
    model_plain: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.67
    - null
    - null
    metric_stds:
    - 0.1
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.65
    - null
    - null
    metric_stds:
    - 0.07
    - null
    - null
  - model: VGAER
    model_plain: VGAER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.61
    - null
    - null
    metric_stds:
    - 0.16
    - null
    - null
  - model: GRACE
    model_plain: GRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.51
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.48
    - null
    - null
    metric_stds:
    - 0.1
    - null
    - null
  - model: uAGNN
    model_plain: uAGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.48
    - null
    - null
    metric_stds:
    - 0.09
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34
    - null
    - null
    metric_stds:
    - 0.02
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.34
    - null
    - null
    metric_stds:
    - 0.06
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.25
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: AmPEP
    model_plain: AmPEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.6169
    - null
    metric_stds:
    - null
    - 0.0693
    - null
  - model: iAMP-2L
    model_plain: iAMP-2L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.626
    - null
    metric_stds:
    - null
    - 0.0951
    - null
  - model: SVM-LZ
    model_plain: SVM-LZ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.7971
    - null
    metric_stds:
    - null
    - 0.0243
    - null
  - model: CS-AMPPred
    model_plain: CS-AMPPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.8669
    - null
    metric_stds:
    - null
    - 0.0436
    - null
  - model: AMAP
    model_plain: AMAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.8987
    - null
    metric_stds:
    - null
    - 0.0418
    - null
  - model: Deep-AmPEP30
    model_plain: Deep-AmPEP30
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9098
    - null
    metric_stds:
    - null
    - 0.0561
    - null
  - model: AmPEPpy
    model_plain: AmPEPpy
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9535
    - null
    metric_stds:
    - null
    - 0.0299
    - null
  - model: AmpGram
    model_plain: AmpGram
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9556
    - null
    metric_stds:
    - null
    - 0.0254
    - null
  - model: MACREL
    model_plain: MACREL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9629
    - null
    metric_stds:
    - null
    - 0.0243
    - null
  - model: MLAMP
    model_plain: MLAMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9668
    - null
    metric_stds:
    - null
    - 0.0235
    - null
  - model: ampir
    model_plain: ampir
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9671
    - null
    metric_stds:
    - null
    - 0.0208
    - null
  - model: AMPScannerV2
    model_plain: AMPScannerV2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9679
    - null
    metric_stds:
    - null
    - 0.0208
    - null
  - model: TT
    model_plain: TT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9719
    - null
    metric_stds:
    - null
    - 0.0189
    - null
  - model: RDKit
    model_plain: RDKit
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9725
    - null
    metric_stds:
    - null
    - 0.0184
    - null
  - model: ECFP
    model_plain: ECFP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.9737
    - null
    metric_stds:
    - null
    - 0.0174
    - null
  - model: MMGCN + CLIP
    model_plain: MMGCN + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2228
    metric_stds:
    - null
    - null
    - 0.0005
  - model: MMGCN + ViT/T5
    model_plain: MMGCN + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.216
    metric_stds:
    - null
    - null
    - 0.0005
  - model: MMGCN + ImageBind
    model_plain: MMGCN + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2472
    metric_stds:
    - null
    - null
    - 0.0019
  - model: MMGCN + DINOv2/T5
    model_plain: MMGCN + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2119
    metric_stds:
    - null
    - null
    - 0.0008
  - model: MGAT + CLIP
    model_plain: MGAT + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2138
    metric_stds:
    - null
    - null
    - 0.0023
  - model: MGAT + ViT/T5
    model_plain: MGAT + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2059
    metric_stds:
    - null
    - null
    - 0.0041
  - model: MGAT + ImageBind
    model_plain: MGAT + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2213
    metric_stds:
    - null
    - null
    - 0.0027
  - model: MGAT + DINOv2/T5
    model_plain: MGAT + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2142
    metric_stds:
    - null
    - null
    - 0.0013
  - model: GCN + ImageBind
    model_plain: GCN + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2281
    metric_stds:
    - null
    - null
    - 0.0003
  - model: SAGE + CLIP
    model_plain: SAGE + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2458
    metric_stds:
    - null
    - null
    - 0.0018
  - model: SAGE + ViT/T5
    model_plain: SAGE + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2311
    metric_stds:
    - null
    - null
    - 0.0005
  - model: SAGE + ImageBind
    model_plain: SAGE + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.252
    metric_stds:
    - null
    - null
    - 0.0009
  - model: SAGE + DINOv2/T5
    model_plain: SAGE + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2298
    metric_stds:
    - null
    - null
    - 0.0001
  - model: BUDDY + CLIP
    model_plain: BUDDY + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2344
    metric_stds:
    - null
    - null
    - 0.0026
  - model: BUDDY + ViT/T5
    model_plain: BUDDY + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2282
    metric_stds:
    - null
    - null
    - 0.0019
  - model: BUDDY + ImageBind
    model_plain: BUDDY + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2435
    metric_stds:
    - null
    - null
    - 0.0024
  - model: BUDDY + DINOv2/T5
    model_plain: BUDDY + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2295
    metric_stds:
    - null
    - null
    - 0.0006
  - model: MLP + CLIP
    model_plain: MLP + CLIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.211
    metric_stds:
    - null
    - null
    - 0.0004
  - model: MLP + ViT/T5
    model_plain: MLP + ViT/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.1765
    metric_stds:
    - null
    - null
    - 0.0006
  - model: MLP + ImageBind
    model_plain: MLP + ImageBind
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.2218
    metric_stds:
    - null
    - null
    - 0.0002
  - model: MLP + DINOv2/T5
    model_plain: MLP + DINOv2/T5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - 0.1753
    metric_stds:
    - null
    - null
    - 0.0011
  milestones:
  - value: 0.67
    std: 0.1
    model: DMON
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: 2025-08
---

