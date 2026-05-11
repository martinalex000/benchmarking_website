- benchmarks for the heterogenous graphs, plus a comment on which of them are considered actually heterogenous (there is a v1 and v2 of such datasets)
- the prompt for the decision which papers to look at does not really work. it should be a two-stage thing which is first fed the abstract and title and checks whether it is on graph learning at all (there could also be some extremely simple pattern matching as a very first stage). And then in the second step it should actually read the paper and extract the information, the info which datasets are used is typically not included in the abstract and often not even in the introduction. 
- decide what to do with custom datasets, the information should be stored somewhere
- there should also be a table that effectively tracks which papers are NOT about graph learning such that there is no need to evaluate that every single time again...
- potentially we need a Vision-language-model in order to find out what the best figure is. so probably some pdf to jpg needed for that
- dataset statistics is still mostly missing
- the results table should be able to hold information on different metrics for several of the old datasets (future), all good datasets have clean metrics.
<!-- - extract available datasets from pyg -->
- make table extraction easier by finding the captions and then detecting the table around it.
- when performing extraction on long papers, make sure to check for the context window size. Also do the extraction per page or in the case of html per section/subsection
- something is off for the pcqm-contact leaderboard, it contains a large number of duplicates where it is unclear where stuff is from. Potentially its hits@50 @10 and @1 or something like that which are incorrectly accumulated.

GCN and GatedGCN are not the same model and for some reason it did not report the better number, but the weaker one (peptides func on where did the gap go). Also GCN is not a proposed model there (its honestly one of the oldest models overall). 

https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html has a list of datasets and corresponding papers. I want to be able to import all those papers.

make the extraction a 2-step process: first extract on which datasets there are experiments and then call the main extraction per dataset. This should increase the probability that a simpler model might be able to make it.
Perform an experiment on which of the available models are able to extract the correct results. Use GLM4.7 as the baseline of what should be in there and then tell me how many of the results are correctly extracted by which other model. Most importantly: mark when a model made up results, just missing one or two is not a big deal.

extraction of figures for existing papers should be automated and there should be a script that does it when working with the paper itself. If in doubt, go with the first figure.