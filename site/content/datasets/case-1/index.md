---
title: Case 1
slug: case-1
benchmark: Power Flow Benchmarks
task_type: graph_regression
description: Power flow analysis on IEEE test case 1 (small power grid, node-level
  regression).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1000000
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 50
best_model:
  model: MGMT
  value: 0.6547
  metric: Accuracy
  arxiv_id: '2601.22593'
  paper_title: arXiv:2601.22593
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - Glob
  - Global
  - P@20
  - Pearson correlation
  - Pearson correlation (Glob)
  - Pearson correlation (Per)
  - Per
  - Per-target
  rows:
  - model: MGMT
    model_plain: MGMT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0239
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MT
    model_plain: MT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6231
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGLAM
    model_plain: MGLAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6196
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DNN
    model_plain: DNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6187
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0227
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FlexCare
    model_plain: FlexCare
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.611
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0139
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MultiMoDN
    model_plain: MultiMoDN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.604
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0167
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MedFuse
    model_plain: MedFuse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.597
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0152
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MMGL
    model_plain: MMGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.592
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AMIGO
    model_plain: AMIGO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5868
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0212
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MaxCorrMGNN
    model_plain: MaxCorrMGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5623
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN
    model_plain: GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5564
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0236
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5378
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GVP-GNN
    model_plain: GVP-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.79
    - 0.82
    - null
    - 0.888
    - 0.84
    - 0.66
    - 0.73
    - 0.62
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 3DCNN
    model_plain: 3DCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.49
    - null
    - null
    - null
    - 0.59
    - 0.52
    - 0.44
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Ornate
    model_plain: Ornate
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.55
    - null
    - null
    - null
    - 0.64
    - 0.47
    - 0.57
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphQA
    model_plain: GraphQA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.72
    - 0.81
    - null
    - null
    - 0.83
    - 0.63
    - 0.68
    - 0.61
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VoroMQA
    model_plain: VoroMQA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.46
    - null
    - null
    - 0.726
    - 0.69
    - 0.62
    - 0.61
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SBROD
    model_plain: SBROD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.37
    - null
    - null
    - null
    - 0.58
    - 0.65
    - 0.64
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ3D
    model_plain: ProQ3D
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.67
    - null
    - null
    - 0.822
    - 0.8
    - 0.69
    - 0.71
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.62
    - null
    - null
    - 0.61
    - 0.3
    - null
    - 0.47
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SASHAN
    model_plain: SASHAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.84
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MESHI-corr-server
    model_plain: MESHI-corr-server
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.838
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MESHI
    model_plain: MESHI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.813
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MESHI-enrich-server
    model_plain: MESHI-enrich-server
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.813
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FaeNNz
    model_plain: FaeNNz
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.81
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ3D-CAD
    model_plain: ProQ3D-CAD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.803
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ3D-lDDT
    model_plain: ProQ3D-lDDT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.803
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ2
    model_plain: ProQ2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.802
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ3D-TM
    model_plain: ProQ3D-TM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.791
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MASS1
    model_plain: MASS1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.776
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MASS2
    model_plain: MASS2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.689
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MULTICOM-NOVEL
    model_plain: MULTICOM-NOVEL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.652
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProQ4
    model_plain: ProQ4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.604
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PLU-AngularQA
    model_plain: PLU-AngularQA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.577
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bhattacharya-Server
    model_plain: Bhattacharya-Server
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.577
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Bhattacharya-SingQ
    model_plain: Bhattacharya-SingQ
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.498
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Kiharalab
    model_plain: Kiharalab
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.375
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PLU-TopQA
    model_plain: PLU-TopQA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.239
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Jagodzinski-Cao-QA
    model_plain: Jagodzinski-Cao-QA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.01411'
    title: Learning from Protein Structure with Geometric Vector Perceptrons
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/drorlab/gvp
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.18
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: POP
    model_plain: POP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 1.33
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-POP
    model_plain: S-POP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 27.08
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Item-KNN
    model_plain: Item-KNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 52.31
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BPR-MF
    model_plain: BPR-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 3.4
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FPMC
    model_plain: FPMC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.4562
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRU4REC
    model_plain: GRU4REC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 59.53
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NARM
    model_plain: NARM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 69.73
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: STAMP
    model_plain: STAMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 70.44
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SR-GNN
    model_plain: SR-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 71.36
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SR-GNN-L
    model_plain: SR-GNN-L
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7011
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SR-GNN-ATT
    model_plain: SR-GNN-ATT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1811.00855'
    title: Session-based Recommendation with Graph Neural Networks
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: https://github.com/CRIPAC-DIG/SR-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.7031
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.6547
    std: 0.0239
    model: MGMT
    arxiv_id: '2601.22593'
    title: arXiv:2601.22593
    date: 2026-01
---

