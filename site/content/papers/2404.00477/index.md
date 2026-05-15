---
title: 'DE-HNN: An effective neural model for Circuit Netlist representation'
arxiv_id: '2404.00477'
authors: []
published_date: '2024-03-30'
abstract: The run-time for optimization tools used in chip design has grown with the
  complexity of designs to the point where it can take several days to go through
  one design cycle which has become a bottleneck. Designers want fast tools that can
  quickly give feedback on a design. Using the input and output data of the tools
  from past designs, one can attempt to build a machine learning model that predicts
  the outcome of a design in significantly shorter time than running the tool. The
  accuracy of such models is affected by the representation of the design data, which
  is usually a netlist that describes the elements of the digital circuit and how
  they are connected. Graph representations for the netlist together with graph neural
  networks have been investigated for such models. However, the characteristics of
  netlists pose several challenges for existing graph learning frameworks, due to
  the large number of nodes and the importance of long-range interactions between
  nodes. To address these challenges, we represent the netlist as a directed hypergraph
  and propose a Directional Equivariant Hypergraph Neural Network (DE-HNN) for the
  effective learning of (directed) hypergraphs. Theoretically, we show that our DE-HNN
  can universally approximate any node or hyperedge based function that satisfies
  certain permutation equivariant and invariant properties natural for directed hypergraphs.
  We compare the proposed DE-HNN with several State-of-the-art (SOTA) machine learning
  models for (hyper)graphs and netlists, and show that the DE-HNN significantly outperforms
  them in predicting the outcome of optimized place-and-route tools directly from
  the input netlists. Our source code and the netlists data used are publicly available
  at https://github.com/YusuLab/chips.git
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2404.00477/main_figure.png
---

