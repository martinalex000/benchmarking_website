---
title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
arxiv_id: '2406.16321'
source_url: ''
authors: []
published_date: Jun 24, 2024
published_date_iso: '2024-06-24'
published_venue: ''
abstract: Graph machine learning has made significant strides in recent years, yet
  the integration of visual information with graph structure and its potential for
  improving performance in downstream tasks remains an underexplored area. To address
  this critical gap, we introduce the Multimodal Graph Benchmark (MM-Graph), a pioneering
  benchmark that incorporates both visual and textual information into graph learning
  tasks. MM-Graph extends beyond existing text-attributed graph benchmarks, offering
  a more comprehensive evaluation framework for multimodal graph learning. Our benchmark
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
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Classic
- TU Dortmund
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id001
  dataset: Amazon-Photo
  rows:
  - model: Joint
    model_key: joint
    model_plain: Joint
    value: 0.973
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.14439'
    title: 'PUMA: Efficient Continual Graph Learning for Node Classification with
      Graph Condensation'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/superallen13/PUMA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.973
    sort_std: 0.001
    is_best: true
  - model: DAM-GT
    model_key: dam-gt
    model_plain: DAM-GT
    value: 0.9666
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9666
    sort_std: 0.0013
    is_best: false
  - model: novel graph MLP mixer
    model_key: novel graph mlp mixer
    model_plain: novel graph MLP mixer
    value: 0.9619
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9619
    sort_std: 0.0017
    is_best: false
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
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
    variant_inference_reason: 'dataset: fuzzy match to amazon-photo (score=80)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: null
    sort_value: 0.2481
    sort_std: 0.0016
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 25, 2025
    date_display: Nov 2025
    date_iso: '2025-11-25'
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: DC-GSAT
    model_key: dc-gsat
    model_plain: DC-GSAT
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DC-SMGNN
    model_key: dc-smgnn
    model_plain: DC-SMGNN
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: SAGE + CLIP/CLIP
    model_key: sage + clip/clip
    model_plain: SAGE + CLIP/CLIP
    value: 0.833
    std: 0.0002
    paper_value: 0.833
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 45
    true_value: 0.833
    true_std: 0.0002
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.833
    sort_std: 0.0002
    is_best: false
  - model: SAGE + ViT/T5
    model_key: sage + vit/t5
    model_plain: SAGE + ViT/T5
    value: 0.8303
    std: 0.0004
    paper_value: 0.8303
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 48
    true_value: 0.8303
    true_std: 0.0004
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8303
    sort_std: 0.0004
    is_best: false
  - model: SAGE + DINOv2/T5
    model_key: sage + dinov2/t5
    model_plain: SAGE + DINOv2/T5
    value: 0.8299
    std: 0.0008
    paper_value: 0.8299
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 50
    true_value: 0.8299
    true_std: 0.0008
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8299
    sort_std: 0.0008
    is_best: false
  - model: MMGCN + DINOv2/T5
    model_key: mmgcn + dinov2/t5
    model_plain: MMGCN + DINOv2/T5
    value: 0.8171
    std: 0.0003
    paper_value: 0.8171
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 61
    true_value: 0.8171
    true_std: 0.0003
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8171
    sort_std: 0.0003
    is_best: false
  - model: MMGCN + ViT/T5
    model_key: mmgcn + vit/t5
    model_plain: MMGCN + ViT/T5
    value: 0.8167
    std: 0.0003
    paper_value: 0.8167
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 62
    true_value: 0.8167
    true_std: 0.0003
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8167
    sort_std: 0.0003
    is_best: false
  - model: MMGCN + CLIP/CLIP
    model_key: mmgcn + clip/clip
    model_plain: MMGCN + CLIP/CLIP
    value: 0.8161
    std: 0.0001
    paper_value: 0.8161
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 63
    true_value: 0.8161
    true_std: 0.0001
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8161
    sort_std: 0.0001
    is_best: false
  - model: SAGE + ImageBind/ImageBind
    model_key: sage + imagebind/imagebind
    model_plain: SAGE + ImageBind/ImageBind
    value: 0.8039
    std: 0.0021
    paper_value: 0.8039
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 74
    true_value: 0.8039
    true_std: 0.0021
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.0021
    is_best: false
  - model: GCN + ImageBind/ImageBind
    model_key: gcn + imagebind/imagebind
    model_plain: GCN + ImageBind/ImageBind
    value: 0.7891
    std: 0.0004
    paper_value: 0.7891
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 99
    true_value: 0.7891
    true_std: 0.0004
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7891
    sort_std: 0.0004
    is_best: false
  - model: MGAT + CLIP/CLIP
    model_key: mgat + clip/clip
    model_plain: MGAT + CLIP/CLIP
    value: 0.7648
    std: 0.0059
    paper_value: 0.7648
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 163
    true_value: 0.7648
    true_std: 0.0059
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7648
    sort_std: 0.0059
    is_best: false
  - model: MGAT + ViT/T5
    model_key: mgat + vit/t5
    model_plain: MGAT + ViT/T5
    value: 0.7543
    std: 0.0076
    paper_value: 0.7543
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 183
    true_value: 0.7543
    true_std: 0.0076
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7543
    sort_std: 0.0076
    is_best: false
  - model: MGAT + DINOv2/T5
    model_key: mgat + dinov2/t5
    model_plain: MGAT + DINOv2/T5
    value: 0.7498
    std: 0.0123
    paper_value: 0.7498
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 189
    true_value: 0.7498
    true_std: 0.0123
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7498
    sort_std: 0.0123
    is_best: false
  - model: MLP + CLIP/CLIP
    model_key: mlp + clip/clip
    model_plain: MLP + CLIP/CLIP
    value: 0.7229
    std: 0.0002
    paper_value: 0.7229
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 228
    true_value: 0.7229
    true_std: 0.0002
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 228
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7229
    sort_std: 0.0002
    is_best: false
  - model: MLP + DINOv2/T5
    model_key: mlp + dinov2/t5
    model_plain: MLP + DINOv2/T5
    value: 0.6883
    std: 0.0003
    paper_value: 0.6883
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 255
    true_value: 0.6883
    true_std: 0.0003
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 255
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6883
    sort_std: 0.0003
    is_best: false
  - model: MLP + ViT/T5
    model_key: mlp + vit/t5
    model_plain: MLP + ViT/T5
    value: 0.6782
    std: 0.0007
    paper_value: 0.6782
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 259
    true_value: 0.6782
    true_std: 0.0007
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 259
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6782
    sort_std: 0.0007
    is_best: false
  - model: MMGCN + ImageBind/ImageBind
    model_key: mmgcn + imagebind/imagebind
    model_plain: MMGCN + ImageBind/ImageBind
    value: 0.5875
    std: 0.0005
    paper_value: 0.5875
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 24, 2024
    date_display: Jun 2024
    date_iso: '2024-06-24'
    published_venue: null
    global_rank: 308
    true_value: 0.5875
    true_std: 0.0005
    value_gap_source_arxiv: '2406.16321'
    value_gap_source_title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal
      Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5875
    sort_std: 0.0005
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
---

