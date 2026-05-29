---
title: ogbl-wikikg2
slug: ogbl-wikikg2
benchmark: OGB
task_type: link_prediction
description: Knowledge graph link prediction on Wikidata (2.5M entities, 535 relations).
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats:
  num_graphs: 2500604
  avg_nodes: 17137181.0
  avg_edges: null
  num_classes: null
result_count: 45
best_model:
  model: DyGFormer
  value: 0.7983
  metric: MRR
  arxiv_id: '2406.02740'
  paper_title: Long Range Propagation on Continuous-Time Dynamic Graphs
variants:
- slug: standard-split
  name: Standard split
  notes: 'Metric: MRR.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MRR
  rows:
  - model: DyGFormer
    model_plain: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7983
    metric_stds:
    - 0.0042
  - model: TCL
    model_plain: TCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7811
    metric_stds:
    - 0.002
  - model: ML
    model_plain: ML
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.001
  - model: RotatE + GCN
    model_plain: RotatE + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.002
  - model: ComplEx + GCN
    model_plain: ComplEx + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.002
  - model: DistMult + GCN
    model_plain: DistMult + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.732
    metric_stds:
    - 0.002
  - model: CAWN
    model_plain: CAWN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.0
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7304
    metric_stds:
    - 0.006
  - model: RotatE
    model_plain: RotatE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    metric_stds:
    - 0.003
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    metric_stds:
    - 0.003
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    metric_stds:
    - 0.003
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6893
    metric_stds:
    - 0.0053
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.685
    metric_stds:
    - 0.004
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    metric_stds:
    - 0.004
  - model: CompGCN
    model_plain: CompGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    metric_stds:
    - 0.004
  - model: TuckER
    model_plain: TuckER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.672
    metric_stds:
    - 0.004
  - model: CTAN
    model_plain: CTAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6676
    metric_stds:
    - 0.0074
  - model: Holographic Embeddings
    model_plain: Holographic Embeddings
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.665
    metric_stds:
    - 0.005
  - model: HolE
    model_plain: HolE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.662
    metric_stds:
    - 0.005
  - model: EdgeBank_re
    model_plain: EdgeBank_re
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6588
    metric_stds:
    - null
  - model: ProjE
    model_plain: ProjE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.005
  - model: ConvE
    model_plain: ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.655
    metric_stds:
    - 0.005
  - model: EdgeBank_tw-ts
    model_plain: EdgeBank_tw-ts
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6325
    metric_stds:
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6305
    metric_stds:
    - 0.0169
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5994
    metric_stds:
    - 0.0163
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5975
    metric_stds:
    - 0.0039
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
    - 0.538
    metric_stds:
    - 0.002
  - model: EdgeBank_th
    model_plain: EdgeBank_th
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5281
    metric_stds:
    - null
  - model: EdgeBank_inf
    model_plain: EdgeBank_inf
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.525
    metric_stds:
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
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
    - 0.524
    metric_stds:
    - 0.0
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5191
    metric_stds:
    - 0.0195
  - model: HGT
    model_plain: HGT
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
    - 0.512
    metric_stds:
    - 0.0
  - model: CompGCN
    model_plain: CompGCN
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
    - 0.501
    metric_stds:
    - 0.0
  - model: R-GCN
    model_plain: R-GCN
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
    - 0.495
    metric_stds:
    - 0.0
  - model: RotatE
    model_plain: RotatE
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
    - 0.482
    metric_stds:
    - 0.0
  - model: ComplEx
    model_plain: ComplEx
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
    - 0.451
    metric_stds:
    - 0.0
  - model: DistMult
    model_plain: DistMult
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
    - 0.438
    metric_stds:
    - 0.0
  - model: RotatE (5x dim)
    model_plain: RotatE (5x dim)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4332
    metric_stds:
    - 0.0025
  - model: TransE (5x dim)
    model_plain: TransE (5x dim)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4256
    metric_stds:
    - 0.003
  - model: ComplEx (5x dim)
    model_plain: ComplEx (5x dim)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4027
    metric_stds:
    - 0.0027
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3804
    metric_stds:
    - 0.0022
  - model: DistMult (5x dim)
    model_plain: DistMult (5x dim)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3729
    metric_stds:
    - 0.0045
  - model: TransE
    model_plain: TransE
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
    - 0.365
    metric_stds:
    - 0.0
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3447
    metric_stds:
    - 0.0082
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2622
    metric_stds:
    - 0.0045
  - model: RotatE
    model_plain: RotatE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.253
    metric_stds:
    - 0.0034
  milestones:
  - value: 0.4332
    std: 0.0025
    model: RotatE (5x dim)
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
  - value: 0.746
    std: 0.001
    model: ML
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: 2021-03
  - value: 0.7983
    std: 0.0042
    model: DyGFormer
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
---

