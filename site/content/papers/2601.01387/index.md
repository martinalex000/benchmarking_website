---
title: Power Flow Benchmarks
arxiv_id: '2601.01387'
source_url: ''
authors: []
published_date: Jan 2026
published_date_iso: 2026-01
abstract: Developing deep learning models with strong adaptability to topological
  variations is of great practical significance for power flow analysis. To enhance
  model performance under variable system scales and improve robustness in branch
  power prediction, this paper proposes a Scale-adaptive Multi-task Power Flow Analysis
  (SaMPFA) framework. SaMPFA introduces a Local Topology Slicing (LTS) sampling technique
  that extracts subgraphs of different scales from the complete power network to strengthen
  the model's cross-scale learning capability. Furthermore, a Reference-free Multi-task
  Graph Learning (RMGL) model is designed for robust power flow prediction. Unlike
  existing approaches, RMGL predicts bus voltages and branch powers instead of phase
  angles. This design not only avoids the risk of error amplification in branch power
  calculation but also guides the model to learn the physical relationships of phase
  angle differences. In addition, the loss function incorporates extra terms that
  encourage the model to capture the physical patterns of angle differences and power
  transmission, further improving consistency between predictions and physical laws.
  Simulations on the IEEE 39-bus system and a real provincial grid in China demonstrate
  that the proposed model achieves superior adaptability and generalization under
  variable system scales, with accuracy improvements of 4.47\
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- RMGL
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Power Flow Benchmarks
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
  dataset: Case 1
  rows:
  - model: RMGL
    model_key: rmgl
    model_plain: RMGL
    value: 0.9987
    std: null
    paper_value: 0.9987
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 1
    true_value: 0.9987
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9987
    sort_std: null
    is_best: true
  - model: MGL
    model_key: mgl
    model_plain: MGL
    value: 0.9964
    std: null
    paper_value: 0.9964
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 2
    true_value: 0.9964
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9964
    sort_std: null
    is_best: false
  - model: GLR
    model_key: glr
    model_plain: GLR
    value: 0.9963
    std: null
    paper_value: 0.9963
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 3
    true_value: 0.9963
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9963
    sort_std: null
    is_best: false
  - model: GLP
    model_key: glp
    model_plain: GLP
    value: 0.9954000000000001
    std: null
    paper_value: 0.9954000000000001
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 4
    true_value: 0.9954000000000001
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9954000000000001
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Case 2
  rows:
  - model: RMGL
    model_key: rmgl
    model_plain: RMGL
    value: 0.9928
    std: null
    paper_value: 0.9928
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 1
    true_value: 0.9928
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9928
    sort_std: null
    is_best: true
  - model: MGL
    model_key: mgl
    model_plain: MGL
    value: 0.9606999999999999
    std: null
    paper_value: 0.9606999999999999
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 2
    true_value: 0.9606999999999999
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9606999999999999
    sort_std: null
    is_best: false
  - model: GLP
    model_key: glp
    model_plain: GLP
    value: 0.5072
    std: null
    paper_value: 0.5072
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 3
    true_value: 0.5072
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5072
    sort_std: null
    is_best: false
  - model: GLR
    model_key: glr
    model_plain: GLR
    value: 0.47090000000000004
    std: null
    paper_value: 0.47090000000000004
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 4
    true_value: 0.47090000000000004
    true_std: null
    value_gap_source_arxiv: '2601.01387'
    value_gap_source_title: Power Flow Benchmarks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47090000000000004
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Power Flow Benchmarks
  datasets:
  - *id001
  - *id002
single_proposed_model: RMGL
main_figure: /figures/2601.01387/main_figure.png
---

