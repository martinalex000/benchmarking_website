---
title: 'gLSTM: Mitigating Over-Squashing by Increasing Storage Capacity'
arxiv_id: '2510.08450'
source_url: ''
authors: []
published_date: ''
published_date_iso: ''
abstract: Graph Neural Networks (GNNs) leverage the graph structure to transmit information
  between nodes, typically through the message-passing mechanism. While these models
  have found a wide variety of applications, they are known to suffer from, where
  information from a large receptive field of node representations is collapsed into
  a single fixed sized vector, resulting in an information bottleneck. In this paper,
  we re-examine the phenomenon through the lens of model storage and retrieval capacity,
  which we define as the amount of information that can be stored in a node's representation
  for later use. We study some of the limitations of existing tasks used to measure
  and introduce a new synthetic task to demonstrate that an information bottleneck
  can saturate this capacity. Furthermore, we adapt ideas from the sequence modeling
  literature on associative memories, fast weight programmers, and the xLSTM model
  to develop a novel GNN architecture with improved capacity. We demonstrate strong
  performance of this architecture both on our capacity synthetic task, as well as
  a range of real-world graph benchmarks.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories: []
task_categories: []
experiment_scopes: []
results: []
results_grouped: []
main_figure: /figures/2510.08450/main_figure.png
---

