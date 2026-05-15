---
title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for Graph
  Neural Networks'
arxiv_id: '2306.08385'
authors: []
published_date: ''
abstract: Graph neural networks have been extensively studied for learning with inter-connected
  data. Despite this, recent evidence has revealed GNNs' deficiencies related to over-squashing,
  heterophily, handling long-range dependencies, edge incompleteness and particularly,
  the absence of graphs altogether. While a plausible solution is to learn new adaptive
  topology for message passing, issues concerning quadratic complexity hinder simultaneous
  guarantees for scalability and precision in large networks. In this paper, we introduce
  a novel all-pair message passing scheme for efficiently propagating node signals
  between arbitrary nodes, as an important building block for a pioneering Transformer-style
  network for node classification on large graphs, dubbed as NodeFormer. Specifically,
  the efficient computation is enabled by a kernerlized Gumbel-Softmax operator that
  reduces the algorithmic complexity to linearity w.r.t. node numbers for learning
  latent graph structures from large, potentially fully-connected graphs in a differentiable
  manner. We also provide accompanying theory as justification for our design. Extensive
  experiments demonstrate the promising efficacy of the method in various tasks including
  node classification on graphs (with up to 2M nodes) and graph-enhanced applications
  (e.g., image classification) where input graphs are missing. The codes are available
  at https://github.com/qitianwu/NodeFormer.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2306.08385/main_figure.png
---

