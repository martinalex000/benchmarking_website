---
title: PCQM4Mv2
slug: pcqm4mv2
benchmark: OGB
task_type: graph_regression
description: Quantum chemistry graph regression — predict HOMO-LUMO gap of 3.8M molecules.
primary_metric: MAE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.PCQM4Mv2.html
stats:
  num_graphs: 3746619
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 87
best_model:
  model: DeMol
  value: 0.0603
  metric: MAE
  arxiv_id: '2603.00568'
  paper_title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
    and Interactions
variants:
- slug: standard-split
  name: Standard split
  notes: 'Scaffold split. Metric: MAE on HOMO-LUMO gap (eV).'
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: DeMol
    model_plain: DeMol
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.0603
    metric_stds:
    - null
  - model: TGT-At
    model_plain: TGT-At
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0671
    metric_stds:
    - null
  - model: Unimol+
    model_plain: Unimol+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0693
    metric_stds:
    - null
  - model: OGB
    model_plain: OGB
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0722
    metric_stds:
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0755
    metric_stds:
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0772
    metric_stds:
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0778
    metric_stds:
    - null
  - model: Global-ViSNet
    model_plain: Global-ViSNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0784
    metric_stds:
    - null
  - model: GEM-2
    model_plain: GEM-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0793
    metric_stds:
    - null
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0831
    metric_stds:
    - null
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0838
    metric_stds:
    - null
  - model: GraphGPS-SPD
    model_plain: GraphGPS-SPD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - null
  - model: ILSVRC
    model_plain: ILSVRC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.001
  - model: GraphGPS_DEEP
    model_plain: GraphGPS_DEEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0852
    metric_stds:
    - null
  - model: GraphGPS-Neighbor
    model_plain: GraphGPS-Neighbor
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0856
    metric_stds:
    - null
  - model: GPS-medium
    model_plain: GPS-medium
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0858
    metric_stds:
    - null
  - model: GraphGPS_BASE
    model_plain: GraphGPS_BASE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0858
    metric_stds:
    - null
  - model: Graphormer-SPIS
    model_plain: Graphormer-SPIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0861
    metric_stds:
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0864
    metric_stds:
    - null
  - model: PostLN_Base
    model_plain: PostLN_Base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.04810'
    title: Benchmarking Graphormer on Large-Scale Molecular Modeling Datasets
    date: Mar 9, 2022
    date_iso: '2022-03-09'
    date_display: Mar 2022
    codebase_url: https://github.com/Microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0864
    metric_stds:
    - null
  - model: GRPE_LARGE
    model_plain: GRPE_LARGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0867
    metric_stds:
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0869
    metric_stds:
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0872
    metric_stds:
    - null
  - model: EGT_Large (24 layers)
    model_plain: EGT_Large (24 layers)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0872
    metric_stds:
    - null
  - model: Equiformer
    model_plain: Equiformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.088
    metric_stds:
    - 0.001
  - model: GRPE
    model_plain: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://github.com/graphcore/ogb-lsc-pcqm4mv2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.089
    metric_stds:
    - null
  - model: GRPE_BASE
    model_plain: GRPE_BASE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.089
    metric_stds:
    - null
  - model: GRPE
    model_plain: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0898
    metric_stds:
    - null
  - model: EGT_Small (6 layers)
    model_plain: EGT_Small (6 layers)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0899
    metric_stds:
    - null
  - model: TokenGT
    model_plain: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.091
    metric_stds:
    - null
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0911
    metric_stds:
    - null
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0918
    metric_stds:
    - null
  - model: SphereNet
    model_plain: SphereNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.092
    metric_stds:
    - 0.001
  - model: GPS + GPSE
    model_plain: GPS + GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0934
    metric_stds:
    - null
  - model: GPS-small
    model_plain: GPS-small
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0938
    metric_stds:
    - null
  - model: GraphGPS_SMALL
    model_plain: GraphGPS_SMALL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0938
    metric_stds:
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0942
    metric_stds:
    - null
  - model: PaiNN
    model_plain: PaiNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.095
    metric_stds:
    - 0.002
  - model: GCN SEM-IL
    model_plain: GCN SEM-IL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.098
    metric_stds:
    - 0.005
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.098
    metric_stds:
    - 0.001
  - model: DeeperGCN-VN
    model_plain: DeeperGCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1021
    metric_stds:
    - null
  - model: GCN SEM-only
    model_plain: GCN SEM-only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.106
    metric_stds:
    - 0.004
  - model: GCN Baseline
    model_plain: GCN Baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.108
    metric_stds:
    - 0.003
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1083
    metric_stds:
    - null
  - model: GCN-virtual
    model_plain: GCN-virtual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1084
    metric_stds:
    - null
  - model: MHNN
    model_plain: MHNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13136'
    title: Molecular Hypergraph Neural Networks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/schwallergroup/mhnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1125
    metric_stds:
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.115
    metric_stds:
    - 0.001
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13136'
    title: Molecular Hypergraph Neural Networks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/schwallergroup/mhnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1153
    metric_stds:
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.119
    metric_stds:
    - 0.001
  - model: GAT-VN
    model_plain: GAT-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13136'
    title: Molecular Hypergraph Neural Networks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/schwallergroup/mhnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1192
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13136'
    title: Molecular Hypergraph Neural Networks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/schwallergroup/mhnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1195
    metric_stds:
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.121
    metric_stds:
    - 0.001
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1218
    metric_stds:
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.122
    metric_stds:
    - 0.001
  - model: EGT_Medium (18 layers)
    model_plain: EGT_Medium (18 layers)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1224
    metric_stds:
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.123
    metric_stds:
    - 0.001
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1234
    metric_stds:
    - null
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.124
    metric_stds:
    - 0.001
  - model: PNA + RWSE
    model_plain: PNA + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.125
    metric_stds:
    - 0.001
  - model: Graphormer_Small
    model_plain: Graphormer_Small
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1264
    metric_stds:
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.128
    metric_stds:
    - 0.001
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.132
    metric_stds:
    - 0.002
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.132
    metric_stds:
    - 0.003
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.135
    metric_stds:
    - 0.002
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13136'
    title: Molecular Hypergraph Neural Networks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/schwallergroup/mhnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1379
    metric_stds:
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: Jul 2021
    date_iso: 2021-07
    date_display: Jul 2021
    codebase_url: https://github.com/deepmind/deepmind-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.138
    metric_stds:
    - 0.004
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1396
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1398
    metric_stds:
    - null
  - model: DeeperGCN-VN
    model_plain: DeeperGCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1398
    metric_stds:
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.14
    metric_stds:
    - null
  - model: GT-Wide
    model_plain: GT-Wide
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1408
    metric_stds:
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.151
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1536
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1684
    metric_stds:
    - null
  - model: MLP-Fingerprint
    model_plain: MLP-Fingerprint
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1735
    metric_stds:
    - null
  - model: TGT-At (+RDKit)
    model_plain: TGT-At (+RDKit)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 68.3
    metric_stds:
    - null
  - model: TGT-At
    model_plain: TGT-At
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 69.8
    metric_stds:
    - null
  - model: Uni-Mol+ (+RDKit)
    model_plain: Uni-Mol+ (+RDKit)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 70.5
    metric_stds:
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 72.0
    metric_stds:
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 78.2
    metric_stds:
    - null
  - model: GEM-2 (+RDKit)
    model_plain: GEM-2 (+RDKit)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 80.6
    metric_stds:
    - null
  - model: EGT
    model_plain: EGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 86.2
    metric_stds:
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 86.2
    metric_stds:
    - null
  - model: GRPE
    model_plain: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 87.6
    metric_stds:
    - null
  - model: TokenGT
    model_plain: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 91.9
    metric_stds:
    - null
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 108.4
    metric_stds:
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_iso: '2024-02-07'
    date_display: Feb 2024
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: false
    is_best: false
    metric_values:
    - 115.2
    metric_stds:
    - null
  milestones:
  - value: 0.1234
    std: null
    model: Graphormer
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: 2021-06
  - value: 0.085
    std: 0.001
    model: ILSVRC
    arxiv_id: '2107.09422'
    title: Large-scale graph representation learning with very deep GNNs and self-supervision
    date: 2021-07
  - value: 0.0722
    std: null
    model: OGB
    arxiv_id: '2212.02229'
    title: 'GPS++: An Optimised Hybrid MPNN/Transformer for Molecular Property Prediction'
    date: 2022-12
  - value: 0.0603
    std: null
    model: DeMol
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: 2026-03
---

