---
title: AMAP
slug: amap
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: Amazon Photography co-purchase hypergraph node classification (8 categories).
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Amazon.html
stats: null
result_count: 45
best_model:
  model: DMON
  value: 0.67
  metric: F1
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  - AUROC
  - MRR
  rows:
  - model: DMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.14097'
    title: Non-Dissipative Graph Propagation for Non-Local Community Detection
    date: Aug 2025
    date_iso: 2025-08
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
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

