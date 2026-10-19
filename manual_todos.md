# My personal todo list for the benchmarks leaderboard webpage. 

## Small tasks for now
- not all benchmark groups (and benchmarks) have a date and a paper
- there is still some overlap for the conference badge and the date. 
- there should be LoG papers in the database


## Larger tasks to do later:
- [ ] Use verified repetition metadata for appropriate uncertainty/statistical comparisons (including repeated CV, split variability, copied baselines and missing counts). Metadata collection only for now; do not change statistics until this task is reviewed.
- [ ] Review table-dependent repetition assessments: match stored values to actual captioned tables, verify result origins and protocols, and approve any removal of ablation/non-comparable rows before applying it.
- copy ogb results. Its important that everything from the ogb website will also appear on my leaderboard.

## Check things
- make sure that the conferences are properly extracted. Currently its still missing for a large part of the papers. 
- are statistics properly imported?
- did the baseline merging part work well?
- do we only track results for settings where it makes sense? (i.e. make sure that the results are comparable)
- did we get all the author names for all the papers?
- did we successfully extract the conferences?


- exact chronology hints: papers may have had revisions under which the results may have been updated. This makes dating certain results harder/problematic.
- how to handle cross-validation and repeated cross-validation which all gives us results. 
- Graph U-Nets’ local LaTeX lacks experimental material present in its published PDF.

- resultate sollten abspeichern aus welchem Table sie extracted wurden.

## Backlog
- integrate into alpharxive and trending papers from various sites such as huggingface's paperswithcode
- add a lot more (hand-crafted) information about each of the benchmarks (more content about what each of the datasets is about, how it came to be, potentially pictures). 
    - logos einbinden der jeweiligen benchmarks
- MLP baseline für fehlende Datensätze selbst berechnen
- cleanup the number of scripts, they are too many.
- show the number of stars on github when there is a github link?
- Add clear benchmark-selection guidance. Right now the site helps browse results, but not decide which benchmarks are worth testing on. It should surface benchmark relevance, popularity/adoption, recency, task fit, dataset scale, and a “recommended benchmark suite” view.
- Tighten data-quality checks on dataset summaries. Some displayed stats look misleading; for example, ogbn-arxiv is described as having 40 subject areas but shows Classes / Targets = 1. Researchers will question the whole site if overview stats are wrong.
- Jan: Glaube da gibt es zum Teil ziemlich üble Fälle wo die Baselines einfach frei erfunden sind 😅 Ich denke eine Metrik die zeigt wie weit die berichteten baseline Ergebnisse von älteren bekannten Werten für die gleiche Methode abweichen ist der pragmatischste Filter der die gröbsten Probleme abfangen würde. Auf Enzymes gibt es Paper in denen sich der SOTA einfach plötzlich halbiert (https://arxiv.org/pdf/2502.14546 , Figure 4.)
- regression test jpg: einmal alle möglichen views rendern und in ein jpg vor jedem commit.


- multiple endpoints for LLMs (not only the local one, but in parallel having access to the big e.g. kimi or minimax model - both still have to be benchmarked)


attribution of results: currently what we do is using the oldest paper with exactly this number and when there is e.g. a higher number for GCN, then all lower and older ones are silently swallowed. instead of doing this silently, it is important to do it in a transparent fashion. One should thus be able to open those aggregated results and see all the results published by different papers for this method. Of course this is especially important for very basic models such as GCN, GIN, etc because many people run them by themselves.

the page of shame papers should be extended by a comparison of what would have been the case at the time of publication - even though its just baselines, its nice to not complain about methods not copying baseline results from the future. The "future" value should of course still be provided.


Complete core paper metadata. Paper pages are missing important scholarly context: author lists are empty on many/all pages, code links are absent, and dates are inconsistently formatted. That makes literature scanning much harder.

Make comparison fairness more explicit. Leaderboards should more clearly distinguish results that are not directly comparable: external data, different splits, fine-tuning vs from-scratch, and nonstandard evaluation setups.

Explain ranking logic in simpler terms. “Adjusted MRR with a three-dataset floor” is not self-evident. It needs a plainer explanation and likely an alternate ranking/sorting mode that matches common researcher questions. This should be explained in more detail.


Add benchmark-selection support, not just leaderboards. Right now the site is better at showing scores than helping decide what to test on. Dataset pages should expose signals like:
standard vs non-standard split
benchmark maturity / number of tracked papers
recent activity
code availability
dataset scale / cost
task scope
whether results are saturated or still moving

the abstracts shown on the paper often contain latex artifacts that reduce trust. Make sure they are properly cleaned. The most common indicator for latex artefacts are ~ symbols that would resolve to spaces - use them to find which papers are affected when checking whether re-extracting the abstract from the latex source worked successfully.



shadcn/ui

further tasks not yet included:
- few shot learning
- contrastive/embeddings
- adverserial attacks

MLP stärker in der Tabelle markieren

Wisonsin und co nochmal genauer angucken, da wurden ganz viele GCN methoden nicht erfolgreich gejoined - warum? Und Angucken was die unterschiede waren anekdotisch


