dark mode

shadcn/ui

MLP baseline für fehlende Datensätze selbst berechnen

Used hardware for the experiments and potentially runtime (even though thats usually not the big tiebreaker)

show the number of stars on github when there is a github link?

add a lot more (hand-crafted) information about each of the benchmarks (more statistics, but also more content about what each of the datasets is about, how it came to be, potentially pictures). Also add a quick description of the metric used and in some cases its drawbacks.

make sure all the papers I used to have locally are also processed on the server

Der plot braucht viel zu lange zum laden, einfach weil viel zu viele punkte und deren std geplottet werden -> check if resolved

also mention when a paper improved a baseline, not only when it made things worse.

heterophily statistics and generally improved statistics for the datasets.

logos einbinden der jeweiligen benchmarks

there are a lot of papers where the title is not extracted correctly. 

check dass beim paper ranking wirklich nur die vorgeschlagene methode betrachtet wird plus eine bessere erklärung und erweiterte filtermöglichkeiten

for each paper: also try to figure out where it was published (if it was) and when. Then putting the conference in addition in the table would be nice.

also make sure that the authors are extracted. Optimally, link to google scholar for each author when there is a connection. orcid is also a good option and probably safer.

copy ogb results. Its important that everything from the ogb website will also appear on my leaderboard.

attribution of results: currently what we do is using the oldest paper with exactly this number and when there is e.g. a higher number for GCN, then all lower and older ones are silently swallowed. instead of doing this silently, it is important to do it in a transparent fashion. One should thus be able to open those aggregated results and see all the results published by different papers for this method. Of course this is especially important for very basic models such as GCN, GIN, etc because many people run them by themselves.

ranks at the time of submission and ranks today for the paper view.

zinc still does a lot of odd stuff - the leaderboard for the full zinc seems to include the other entries as well - at least at the first glance it looks like there are too many terrible appraoches for the full zinc one.

integrate into alpharxive and trending papers from various sites such as huggingface's paperswithcode

add year filter for papers

don't sort by amount of results but by amount of recent results

ways to interact with the website: how can I make sure my paper is re-parsed? Or flag problems with the paper?

http://localhost:1313/datasets/zinc/ hier gibt es verdammt grosse Zahlen gemixt unter die anderen - wo kommen die her und wie werde ich die los? Und schaffe ich es die y-achse so zu skalieren, dass man mehr sehen kann?

the page of shame papers should be extended by a comparison of what would have been the case at the time of publication - even though its just baselines, its nice to not complain about methods not copying baseline results from the future. The "future" value should of course still be provided.

How to deal with the exact dates of the conferences? -> rather stick with the arxiv dates of each paper.


Add clear benchmark-selection guidance. Right now the site helps browse results, but not decide which benchmarks are worth testing on. It should surface benchmark relevance, popularity/adoption, recency, task fit, dataset scale, and a “recommended benchmark suite” view.

Fix inconsistent headline numbers. The homepage and section pages use different counts, e.g. 224 papers on the homepage vs 159 papers on the papers page, and result totals also differ. That undermines trust immediately.

Tighten data-quality checks on dataset summaries. Some displayed stats look misleading; for example, ogbn-arxiv is described as having 40 subject areas but shows Classes / Targets = 1. Researchers will question the whole site if overview stats are wrong.

Complete core paper metadata. Paper pages are missing important scholarly context: author lists are empty on many/all pages, code links are absent, and dates are inconsistently formatted. That makes literature scanning much harder.

Make comparison fairness more explicit. Leaderboards should more clearly distinguish results that are not directly comparable: external data, different splits, fine-tuning vs from-scratch, and nonstandard evaluation setups.

Explain ranking logic in simpler terms. “Adjusted MRR with a three-dataset floor” is not self-evident. It needs a plainer explanation and likely an alternate ranking/sorting mode that matches common researcher questions. This should be explained in more detail.

The mobile view of the table is terrible. It is all squeezed together in a way that is not helpful instead of collapsing in a sensible way into a multiline-entry. 

Remove or downplay pipeline-internal terminology. Labels like “Extracted with qwen…” and footer text about automatic extraction/overrides feel internal. Researchers care more about provenance, confidence, and curation quality than the extraction pipeline details.

now the button to hide rows past row 50 is simply gone. Please bring it back.

the names of methods are terribly inconsistent and way too often wrong. Lets manually re-evaluate the most obvious cases (there have been significant improvements to the prompt). 


Improve homepage orientation. The homepage is too sparse: just a short blurb, counters, and two buttons. For researchers, it should surface starting points like benchmark families, task types, “recommended standard benchmarks,” recently updated benchmarks, and high-coverage / high-activity datasets.

Add benchmark-selection support, not just leaderboards. Right now the site is better at showing scores than helping decide what to test on. Dataset pages should expose signals like:
standard vs non-standard split
benchmark maturity / number of tracked papers
recent activity
code availability
dataset scale / cost
task scope
whether results are saturated or still moving

the abstracts shown on the paper often contain latex artifacts that reduce trust. Make sure they are properly cleaned. The most common indicator for latex artefacts are ~ symbols that would resolve to spaces - use them to find which papers are affected when checking whether re-extracting the abstract from the latex source worked successfully.

Improve metadata completeness on paper pages. Coverage is weak: 
224 paper pages have empty authors
216 have no code link
46 have no source URL
Missing authors, venue, DOI/BibTeX, and code links makes pages less useful for literature review.

## Script cleanup backlog

- consolidate `scripts/find_todo_papers.py` and `scripts/process_todo_list.py` if both remain in use; right now the first is a manual queue manager while the second is the priority-queue batch runner
- decide whether `scripts/test_model_ping.py` should stay as a committed diagnostic utility or move into docs-only troubleshooting notes once the endpoint/model situation stabilizes
- review whether `scripts/run_pipeline.sh` should absorb the off-peak-hours scheduling logic directly, or whether that belongs in external cron/systemd config instead of the repo

at some point in the future: add generation benchmarks/metrics etc. But this feels more like a paper than a normal benchmarking overview since everything is extremely scattered.

╭────────────────────────────────────┬────────────┬─────────┬─────────┬───────┬─────────────────────────────────────────────────────────────────────┬────────╮
│ Model                              │ Paper      │    Time │    TTFT │ tok/s │ Datasets found                                                      │ Status │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ openai-gpt-oss-120b                │ 2206.08164 │    6.8s │   4.64s │   315 │ PascalVOC-SP, COCO-SP, Peptides-func, Peptides-struct, PCQM-Contact │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ meta-llama-3.1-8b-instruct         │ 2206.08164 │    1.4s │   0.20s │   190 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-omni-30b-a3b-instruct        │ 2206.08164 │    1.8s │   0.25s │   174 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ internvl3.5-30b-a3b                │ 2206.08164 │    2.0s │   0.18s │   146 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-35b-a3b                    │ 2206.08164 │    7.9s │       — │   130 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-397b-a17b                  │ 2206.08164 │    9.0s │       — │   114 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-122b-a10b                  │ 2206.08164 │    9.0s │       — │   113 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.6-35b-a3b                    │ 2206.08164 │   12.2s │       — │    84 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ glm-4.7                            │ 2206.08164 │  246.9s │ 241.98s │    63 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-30b-a3b-instruct-2507        │ 2206.08164 │   16.3s │  11.10s │    58 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-coder-30b-a3b-instruct       │ 2206.08164 │    7.1s │   1.20s │    50 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-27b                        │ 2206.08164 │   21.5s │       — │    48 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ gemma-3-27b-it                     │ 2206.08164 │    7.8s │   0.72s │    39 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ medgemma-27b-it                    │ 2206.08164 │   16.2s │   1.10s │    24 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ devstral-2-123b-instruct-2512      │ 2206.08164 │  541.5s │ 155.90s │    16 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ mistral-large-3-675b-instruct-2512 │ 2206.08164 │   40.2s │   3.38s │     8 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ gemma-4-31b-it                     │ 2206.08164 │ 1095.1s │       — │     — │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ teuken-7b-instruct-research        │ 2206.08164 │   10.5s │       — │     — │ none                                                                │ ✓      │
╰────────────────────────────────────┴────────────┴─────────┴─────────┴───────┴─────────────────────────────────────────────────────────────────────┴────────╯

 Model Extraction Quality vs GLM 4.7 Baseline                                            
╭───────────────────────────────────┬────────┬──────────┬──────┬────────┬────────┬──────────┬────────┬───────────┬─────────┬───────╮
│                                   │        │ Baseline │      │    Val │        │ Halluci- │        │           │ Halluc. │   Avg │
│ Model                             │ Papers │  Entries │ Hits │ Errors │ Misses │  nations │ Recall │ Precision │    Rate │  Time │
├───────────────────────────────────┼────────┼──────────┼──────┼────────┼────────┼──────────┼────────┼───────────┼─────────┼───────┤
│ moonshotai/Kimi-K2.6              │      1 │      327 │  314 │      0 │     13 │       37 │    96% │       89% │     11% │ 2442s │
├───────────────────────────────────┼────────┼──────────┼──────┼────────┼────────┼──────────┼────────┼───────────┼─────────┼───────┤
│ Qwen/Qwen3-Coder-30B-A3B-Instruct │      1 │      327 │  151 │     14 │    162 │       47 │    46% │       71% │     22% │  307s │
╰───────────────────────────────────┴────────┴──────────┴──────┴────────┴────────┴──────────┴────────┴───────────┴─────────┴───────╯
│ google/gemma-4-31B-it             │      1 │      327 │  314 │      0 │     13 │       35 │    96% │       90% │     10% │ 4459s │
│ alias-huge-no-thinking            │      1 │      327 │  289 │      0 │     38 │      124 │    88% │       70% │     30% │ 2369s │
│ alias-huge-no-thinking            │      1 │      327 │   70 │      0 │    257 │       10 │    21% │       88% │     12% │ 7521s │ - wtf...

