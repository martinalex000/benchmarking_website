---
title: Long-Range Graph Wavelet Networks
arxiv_id: '2509.06743'
source_url: ''
authors: []
published_date: Sep 2025
published_date_iso: 2025-09
abstract: Modeling long-range interactions, the propagation of information across
  distant parts of a graph, is a central challenge in graph machine learning. Graph
  wavelets, inspired by multi-resolution signal processing, provide a principled way
  to capture both local and global structures. However, existing wavelet-based graph
  neural networks rely on finite-order polynomial approximations, which limit their
  receptive fields and hinder long-range propagation. We propose Long-Range Graph
  Wavelet Networks, which decompose wavelet filters into complementary local and global
  components. Local aggregation is handled with efficient low-order polynomials, while
  long-range interactions are captured through a flexible spectral-domain parameterization.
  This hybrid design unifies short- and long-distance information flow within a principled
  wavelet framework. Experiments show that achieves state-of-the-art performance among
  wavelet-based methods on long-range benchmarks, while remaining competitive on short-range
  datasets.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- LR-GWN (TC)
- LR-GWN
mrr: 0.0169
adjusted_mrr: 0.0056
mrr_dataset_count: 1
benchmark_categories:
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
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
    date: Jan 29, 2025
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
    date: Jan 29, 2025
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: LR-GWN (TC)
    model_key: lr-gwn (tc)
    model_plain: LR-GWN (TC)
    value: 0.7216
    std: 0.0040999999999999995
    paper_value: 0.7216
    paper_std: 0.0040999999999999995
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 10
    true_value: 0.7216
    true_std: 0.0040999999999999995
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7216
    sort_std: 0.0040999999999999995
    is_best: false
  - model: WaveGC
    model_key: wavegc
    model_plain: WaveGC
    value: 0.6973
    std: 0.0043
    paper_value: 0.6973
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2024
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 59
    true_value: 0.6973
    true_std: 0.0043
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6973
    sort_std: 0.0043
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.6695
    std: 0.0063
    paper_value: 0.6695
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bastos et al. 2023
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 128
    true_value: 0.6695
    true_std: 0.0063
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6695
    sort_std: 0.0063
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.6547
    std: 0.0048
    paper_value: 0.6547
    paper_std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 167
    true_value: 0.6547
    true_std: 0.0048
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6547
    sort_std: 0.0048
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.6023
    std: 0.0027
    paper_value: 0.6023
    paper_std: 0.0027
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hammond et al. 2011
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 245
    true_value: 0.6023
    true_std: 0.0027
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 245
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6023
    sort_std: 0.0027
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: LR-GWN
    model_key: lr-gwn
    model_plain: LR-GWN
    value: 0.2463
    std: 0.0007
    paper_value: 0.2463
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 59
    true_value: 0.2463
    true_std: 0.0007
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2463
    sort_std: 0.0007
    is_best: false
  - model: WaveGC
    model_key: wavegc
    model_plain: WaveGC
    value: 0.2495
    std: 0.0007
    paper_value: 0.2495
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2024
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 129
    true_value: 0.2495
    true_std: 0.0007
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2495
    sort_std: 0.0007
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.2506
    std: 0.0013
    paper_value: 0.2506
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: Bastos et al. 2023
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 147
    true_value: 0.2506
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0013
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.2539
    std: 0.0021
    paper_value: 0.2539
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: Hammond et al. 2011
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 178
    true_value: 0.2539
    true_std: 0.0021
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2539
    sort_std: 0.0021
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.2734
    std: 0.0004
    paper_value: 0.2734
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: ''
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    global_rank: 249
    true_value: 0.2734
    true_std: 0.0004
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2734
    sort_std: 0.0004
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
main_figure: /figures/2509.06743/main_figure.png
---

