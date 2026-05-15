---
title: Short-Range Oversquashing
arxiv_id: '2511.20406'
authors: []
published_date: ''
abstract: 'Message Passing Neural Networks (MPNNs) are widely used for learning on
  graphs, but their ability to process long-range information is limited by the phenomenon
  of oversquashing. This limitation has led some researchers to advocate Graph Transformers
  as a better alternative, whereas others suggest that it can be mitigated within
  the MPNN framework, using virtual nodes or other rewiring techniques. In this work,
  we demonstrate that oversquashing is not limited to long-range tasks, but can also
  arise in short-range problems. This observation allows us to disentangle two distinct
  mechanisms underlying oversquashing: (1) the bottleneck phenomenon, which can arise
  even in low-range settings, and (2) the vanishing gradient phenomenon, which is
  closely associated with long-range tasks. We further show that the short-range bottleneck
  effect is not captured by existing explanations for oversquashing, and that adding
  virtual nodes does not resolve it. In contrast, transformers do succeed in such
  tasks, positioning them as the more compelling solution to oversquashing, compared
  to specialized MPNNs. Code available at https://github.com/YakovM93/Short-Range-Oversquashing.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2511.20406/main_figure.png
---

