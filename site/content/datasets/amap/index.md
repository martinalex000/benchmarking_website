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
result_count: 77
best_model:
  model: CV
  value: 0.7527
  metric: F1
  arxiv_id: '2307.14613'
  paper_title: Self-Contrastive Graph Diffusion Network
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
  - ARI
  - HR@10
  - HR@20
  - HR@30
  - HR@40
  - HR@50
  - NDCG@20
  - NMI
  - Recall@10
  - Recall@20
  rows:
  - model: CV
    model_plain: CV
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7527
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CDC
    model_plain: CDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
  - model: DFCN
    model_plain: DFCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7125
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7103
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6999
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MCGC
    model_plain: MCGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6808
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0176
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MvAGC
    model_plain: MvAGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.64
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
  - model: AutoSSL
    model_plain: AutoSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5447
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.46
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
  - model: GDCL
    model_plain: GDCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3837
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3288
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3197
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: COMPLETER
    model_plain: COMPLETER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.307
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1859
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3735
    - null
    - null
    metric_stds:
    - null
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0005
    - null
    - null
  - model: DCN
    model_plain: DCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.208
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3876
    - null
    - null
    metric_stds:
    - null
    - 0.0047
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.003
    - null
    - null
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1924
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3783
    - null
    - null
    metric_stds:
    - null
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0008
    - null
    - null
  - model: AdaGAE
    model_plain: AdaGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.462
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5596
    - null
    - null
    metric_stds:
    - null
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0087
    - null
    - null
  - model: MGAE
    model_plain: MGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.4882
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6213
    - null
    - null
    metric_stds:
    - null
    - 0.0457
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0279
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5812
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6525
    - null
    - null
    metric_stds:
    - null
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0045
    - null
    - null
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.4418
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5836
    - null
    - null
    metric_stds:
    - null
    - 0.0441
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0276
    - null
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3121
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4485
    - null
    - null
    metric_stds:
    - null
    - 0.0123
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0083
    - null
    - null
  - model: AGE
    model_plain: AGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5589
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6538
    - null
    - null
    metric_stds:
    - null
    - 0.0134
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0061
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.1877
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3028
    - null
    - null
    metric_stds:
    - null
    - 0.0234
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0394
    - null
    - null
  - model: DFCN
    model_plain: DFCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5828
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6623
    - null
    - null
    metric_stds:
    - null
    - 0.0074
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0121
    - null
    - null
  - model: GDCL
    model_plain: GDCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.2157
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3732
    - null
    - null
    metric_stds:
    - null
    - 0.0051
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0028
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.2685
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4838
    - null
    - null
    metric_stds:
    - null
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0238
    - null
    - null
  - model: AutoSSL
    model_plain: AutoSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.2687
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4856
    - null
    - null
    metric_stds:
    - null
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0071
    - null
    - null
  - model: AGC-DRR
    model_plain: AGC-DRR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6015
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6654
    - null
    - null
    metric_stds:
    - null
    - 0.0156
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0124
    - null
    - null
  - model: AFGRL
    model_plain: AFGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5445
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6405
    - null
    - null
    metric_stds:
    - null
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0015
    - null
    - null
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3418
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3956
    - null
    - null
    metric_stds:
    - null
    - 0.0089
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0039
    - null
    - null
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.0536
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0637
    - null
    - null
    metric_stds:
    - null
    - 0.0214
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0189
    - null
    - null
  - model: RGC
    model_plain: RGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06827'
    title: Reinforcement Graph Clustering with Unknown Cluster Number
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/yueliu1999/RGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.5958
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6961
    - null
    - null
    metric_stds:
    - null
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0036
    - null
    - null
  - model: BPR-MF
    model_plain: BPR-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0607
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
    - null
    - null
  - model: NeuMF
    model_plain: NeuMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0507
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
    - null
    - null
  - model: FISM
    model_plain: FISM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0721
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
    - null
    - null
  - model: NGCF
    model_plain: NGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0617
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
    - null
    - null
  - model: MultiGCCF
    model_plain: MultiGCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0625
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
    - null
    - null
  - model: DGCF
    model_plain: DGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0737
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
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0797
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
    - null
    - null
  - model: SGL
    model_plain: SGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0898
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
    - null
    - null
  - model: NCL
    model_plain: NCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.06200'
    title: Improving Graph Collaborative Filtering with Neighborhood-enriched Contrastive
      Learning
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/RUCAIBox/NCL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0933
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
    - null
    - null
  - model: BPR
    model_plain: BPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.01851
    - 0.02853
    - 0.03821
    - 0.04737
    - 0.05556
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
    - null
    - null
  - model: GC-MC
    model_plain: GC-MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.02063
    - 0.03196
    - 0.04242
    - 0.05226
    - 0.06133
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
    - null
    - null
  - model: PinSage
    model_plain: PinSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.02043
    - 0.0321
    - 0.04298
    - 0.05239
    - 0.06165
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
    - null
    - null
  - model: NGCF
    model_plain: NGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.02071
    - 0.03244
    - 0.04343
    - 0.05329
    - 0.06263
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
    - null
    - null
  - model: L-GC-MC
    model_plain: L-GC-MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.02092
    - 0.03248
    - 0.04355
    - 0.05394
    - 0.06335
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
    - null
    - null
  - model: R-GC-MC
    model_plain: R-GC-MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.01962
    - 0.03084
    - 0.04153
    - 0.05139
    - 0.06032
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
    - null
    - null
  - model: L-GCCF
    model_plain: L-GCCF
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2001.10167'
    title: 'Revisiting Graph based Collaborative Filtering: A Linear Residual Graph
      Convolutional Network Approach'
    date: Jan 2020
    date_iso: 2020-01
    date_display: Jan 2020
    codebase_url: https://github.com/newlei/LR-GCCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.02209
    - 0.03407
    - 0.04532
    - 0.05532
    - 0.06498
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
    - null
    - null
  - model: BPR
    model_plain: BPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0764
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
    - null
    - null
  - model: NeuMF
    model_plain: NeuMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0575
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
    - null
    - null
  - model: NGCF
    model_plain: NGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.076
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
    - null
    - null
  - model: DGCF
    model_plain: DGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0867
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
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0953
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
    - null
    - null
  - model: GTN
    model_plain: GTN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.093
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
    - null
    - null
  - model: RGCF
    model_plain: RGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.109
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
    - null
    - null
  - model: DirectAU
    model_plain: DirectAU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.1053
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
    - null
    - null
  - model: JGCF
    model_plain: JGCF
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03624'
    title: 'On Manipulating Signals of User-Item Graph: A Jacobi Polynomial-based
      Graph Collaborative Filtering'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/SpaceLearner/JGCF
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.1191
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
    - null
    - null
  - model: VBPR
    model_plain: VBPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.10632'
    title: Multi-Modal Self-Supervised Learning for Recommendation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/HKUDS/MMSSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0166
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
    - null
    - null
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.10632'
    title: Multi-Modal Self-Supervised Learning for Recommendation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/HKUDS/MMSSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0219
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
    - null
    - null
  - model: LATTICE
    model_plain: LATTICE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.10632'
    title: Multi-Modal Self-Supervised Learning for Recommendation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/HKUDS/MMSSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0263
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
    - null
    - null
  - model: SLRec
    model_plain: SLRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.10632'
    title: Multi-Modal Self-Supervised Learning for Recommendation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/HKUDS/MMSSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0269
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
    - null
    - null
  - model: MMSSL
    model_plain: MMSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.10632'
    title: Multi-Modal Self-Supervised Learning for Recommendation
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/HKUDS/MMSSL
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.035
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
    - null
    - null
  - model: BPR-MF
    model_plain: BPR-MF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0589
    - null
    - null
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
    - null
    - null
  - model: GRU4REC
    model_plain: GRU4REC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0478
    - null
    - null
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
    - null
    - null
  - model: Caser
    model_plain: Caser
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0643
    - null
    - null
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
    - null
    - null
  - model: SASRec
    model_plain: SASRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0901
    - null
    - null
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
    - null
    - null
  - model: BERT4Rec
    model_plain: BERT4Rec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0984
    - null
    - null
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
    - null
    - null
  - model: DSSRec
    model_plain: DSSRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0914
    - null
    - null
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
    - null
    - null
  - model: S3-Rec
    model_plain: S3-Rec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0487
    - null
    - null
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
    - null
    - null
  - model: CL4SRec
    model_plain: CL4SRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0994
    - null
    - null
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
    - null
    - null
  - model: DCRec
    model_plain: DCRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0674
    - null
    - null
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
    - null
    - null
  - model: MAERec
    model_plain: MAERec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0854
    - null
    - null
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
    - null
    - null
  - model: IOCRec
    model_plain: IOCRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.0916
    - null
    - null
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
    - null
    - null
  - model: ICLRec
    model_plain: ICLRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.1072
    - null
    - null
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
    - null
    - null
  - model: ELCRec
    model_plain: ELCRec
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.05975'
    title: End-to-end Learnable Clustering for Intent Learning in Recommendation
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: https://github.com/yueliu1999/ELCRec
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.1079
    - null
    - null
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
    - null
    - null
  milestones:
  - value: 0.7527
    std: 0.0018
    model: CV
    arxiv_id: '2307.14613'
    title: Self-Contrastive Graph Diffusion Network
    date: 2023-07
---

