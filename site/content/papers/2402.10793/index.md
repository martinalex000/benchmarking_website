---
title: An end-to-end attention-based approach for learning on graphs
arxiv_id: '2402.10793'
authors: []
published_date: Feb 2024
abstract: There has been a recent surge in transformer-based architectures for learning
  on graphs, mainly motivated by attention as an effective learning mechanism and
  the desire to supersede the hand-crafted operators characteristic of message passing
  schemes. However, concerns over their empirical effectiveness, scalability, and
  complexity of the pre-processing steps have been raised, especially in relation
  to much simpler graph neural networks that typically perform on par with them across
  a wide range of benchmarks. To address these shortcomings, we consider graphs as
  sets of edges and propose a purely attention-based approach consisting of an encoder
  and an attention pooling mechanism. The encoder vertically interleaves masked and
  vanilla self-attention modules to learn an effective representation of edges while
  allowing for tackling possible misspecifications in input graphs. Despite its simplicity,
  the approach outperforms fine-tuned message passing baselines and recently proposed
  transformer-based methods on more than 70 node and graph-level tasks, including
  challenging long-range benchmarks. Moreover, we demonstrate state-of-the-art performance
  across different tasks, ranging from molecular to vision graphs, and heterophilous
  node classification. The approach also outperforms graph neural networks and transformers
  in transfer learning settings and scales much better than alternatives with a similar
  performance level or expressive power.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- ESA
mrr: 0.4775
results:
- &id004
  dataset: D&D
  rows:
  - model: MPNN
    value: 0.989
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
    value: 0.981
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
    value: 0.976
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: ESA
    value: 0.6968516041247438
    std: 0.0013794417525553372
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: PNA
    value: 0.6962037752713723
    std: 0.0017162537128048157
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GPS
    value: 0.675772
    std: 0.0019314683533518953
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DropGIN
    value: 0.6750444425282793
    std: 0.003010065997818225
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT
    value: 0.6659264497946298
    std: 0.0019193275851867547
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GATv2
    value: 0.65472612254266
    std: 0.004456977663883839
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: TokenGT
    value: 0.6407549500465393
    std: 0.008498306711241119
    metric: R^2
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
- &id005
  dataset: MalNet-Tiny
  rows:
  - model: ESA
    value: 0.948
    std: 0.00424
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GatedGCN
    value: 0.946
    std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GSM++ (BFS)
    value: 0.9417
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
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
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
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
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
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
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: ESA
    value: 0.7071
    std: 0.0015
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 38
    is_best: false
  - model: GCN
    value: 0.686
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 9
    is_best: false
  - model: GIN
    value: 0.6621
    std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 39
    is_best: false
  - model: GPS
    value: 0.6534
    std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 151
    is_best: false
  - model: TokenGT
    value: 0.6263
    std: 0.0117
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 221
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: ESA
    value: 0.245329301
    std: 0.000297453
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: GCN
    value: 0.246
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 2
    is_best: false
  - model: GIN
    value: 0.2473
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 7
    is_best: false
  - model: TokenGT
    value: 0.24888524548573923
    std: 0.0013272721664974406
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 110
    is_best: false
  - model: GPS
    value: 0.2509
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    global_rank: 120
    is_best: false
  metric: MAE
  higher_is_better: false
- &id006
  dataset: QM9
  is_multi_metric: true
  rows:
  - model: Mace
    metric_values:
    - 0.02
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: ''
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: DropGIN
    metric_values:
    - 0.02578744427174226
    - 0.16229444581483676
    metric_stds:
    - 0.000867405321348238
    - 0.0017203168654583633
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 2
  - model: ESA
    metric_values:
    - 0.02578744427174226
    - 0.15244936051398003
    metric_stds:
    - 0.000867405321348238
    - 0.0029945876029935353
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 3
  - model: SchNet
    metric_values:
    - 0.026
    - null
    metric_stds:
    - 0.002
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: ''
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: DimeNet++
    metric_values:
    - 0.027
    - null
    metric_stds:
    - 0.002
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.002
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_iso: ''
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: TokenGT
    metric_values:
    - 0.030389001220464663
    - 0.20003333687782282
    metric_stds:
    - 0.0005953300476479862
    - 0.00828174606274421
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 6
  - model: PNA
    metric_values:
    - 0.0317492975167588
    - 0.15115694898675025
    metric_stds:
    - 0.0028074830084290074
    - 0.0012178706316662376
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 7
  - model: GATv2
    metric_values:
    - 0.03219783138040288
    - 0.15725115601797318
    metric_stds:
    - 0.0008736508385477724
    - 0.0023134325943648688
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 8
  - model: GAT
    metric_values:
    - 0.03290000183733416
    - 0.1594100643906536
    metric_stds:
    - 0.0014504048065470119
    - 0.00274523474824748
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 9
  - model: GPS
    metric_values:
    - 0.033075999999999994
    - 0.178406
    metric_stds:
    - 0.005936661014408688
    - 0.0020226477696326695
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 11
  - model: Graphormer
    metric_values:
    - 0.05862095989286895
    - 0.17889551252591157
    metric_stds:
    - 0.03095901400991143
    - 0.008689612096286428
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 13
  - model: GCN
    metric_values:
    - null
    - 0.17144381081131788
    metric_stds:
    - null
    - 0.003676356368918919
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    is_best: false
    global_rank: null
  - model: GIN
    metric_values:
    - null
    - 0.16187201431047754
    metric_stds:
    - null
    - 0.0016597907171188395
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 17
  - model: GraphGPS
    metric_values:
    - null
    - 0.161956
    metric_stds:
    - null
    - 0.0015081326201631
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  - model: Grph.
    metric_values:
    - null
    - 0.19038245203081353
    metric_stds:
    - null
    - 0.005813449852960949
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: null
  metrics:
  - MAE
  - RMSE
  primary_metric: MAE
  higher_is_better: false
- &id001
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: arXiv:2402.08450
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: GPM
    value: 0.021
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: GPS
    value: 0.023842
    std: 0.0069779309254248125
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: Graphormer
    value: 0.036005993400000005
    std: 0.002019173876825075
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: TokenGT
    value: 0.0467565117234533
    std: 0.01010544569636761
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: PNA
    value: 0.05727021078890476
    std: 0.006639614126119909
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GIN
    value: 0.06763977903440473
    std: 0.00412784873186527
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GAT
    value: 0.0776354896230479
    std: 0.005512609666895327
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 124
    is_best: false
  - model: GATv2
    value: 0.0794978814609628
    std: 0.003649727726331984
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 128
    is_best: false
  - model: GCN
    value: 0.1517617683115362
    std: 0.02268571908117693
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 115
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: Other Graph Benchmarks
  datasets:
  - *id005
- benchmark: Quantum Chemistry
  datasets:
  - *id006
single_proposed_model: ESA
main_figure: /figures/2402.10793/main_figure.png
---

