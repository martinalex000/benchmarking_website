# Verified repetition metadata

## Whole-paper scheduler

`repetition_scheduler.py` runs the existing whole-paper repetition extractor. Each paper's
complete expanded LaTeX source is sent to the facts call and then the verification call; tables
are not split into independent jobs. Each successful paper is applied to the database as soon as
its assessment finishes. Run artifacts default to `papers/repetition_scheduler/`.
By default, papers with an `assessment.json` in the completed v5 experiment are skipped; an
existing database assessment alone does not mark a paper complete for this run.

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/repetition_scheduler.py worker \
  --endpoint primary --concurrency 10
```

Use `--endpoint second` for the separately configured second key and
`--include-nonconference` to include papers outside the published-conference cohort. Add
`--paper ARXIV_ID ...` to restrict a run. `status` reads the saved status file. Each completed
paper is applied immediately. `throughput.md`, `throughput.csv`, and `throughput.png` are updated
after each completed paper; run outputs and paper analyses are stored under the selected run
directory. Override the v5 exclusion source with `--exclude-root PATH`, or include those papers
with `--include-v5-completed`.

## Running and resuming

Use `UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.pipeline repetitions`.

The cohort contains papers with stored results and a non-empty **exported conference field**, using the site's existing venue normalizer. ArXiv-only/unresolved venue labels do not qualify. The initial October 6 cohort has 685 papers. Use `--paper ARXIV_ID ...` for a subset. Successful source-identical calls are reused on resume and revalidated before database application. A changed prompt requires a fresh output directory. A batch lock prevents duplicate supervisors in the same directory.

The main pipeline also runs this stage after successfully parsing eligible papers. New batches start at four concurrent requests and adapt upward to the number of eligible paper tasks; there is no fixed 20- or 100-stream cap. A 429 halves concurrency for the active time window and imposes a shared cooldown for the `retry-after` interval (seconds or HTTP date). Rate-limited calls keep retrying through shared cooldowns until one succeeds; other transient failures remain bounded by the configured retry count. Retries never switch models or keys, and successful calls gradually restore concurrency. Existing requests are allowed to finish at the daytime boundary, but no new requests beyond the active window's limit start.

## Stored data and safeguards

- `repetition_assessments` stores the source/prompt hashes, GLM model, classification, uniform count when supported, full extraction/verifier payload, exact-source evidence and artifact path.
- Every result from an assessed paper links to that assessment. `num_runs` is assigned only to matched, explicitly self-evaluated methods with a uniform verified protocol; copied/unsupported baseline counts remain unknown. A method must have accepted evidence across all applicable benchmark tables before paper-wide propagation. Existing conflicting counts are withheld for review, not silently overwritten with a different number.
- `repetition_status` distinguishes assigned counts, copied values, unknown origins/counts, table-pending cases and conflicts. A table-dependent paper receives no automatic per-table count assignment.
- Prior per-result run metadata is retained in the assessment's `row_update_audit`; human overrides are not altered. No scores, dataset assignments or result deletions are performed.
- No standard deviation does not imply zero or one run. Fold counts, split variability and nested protocols remain distinct from independent training repetitions.

Progress and raw call/source snapshots live in `papers/repetition_backfill/`. The Markdown progress report is `report.md`, with machine-readable state in `status.json`. The consistent pre-migration database backup is `data/backups/benchmarks_before_repetition_20261006.sqlite`; it includes existing WAL changes.

## Deferred work

The statistics task remains open in `manual_todos.md` and is not implemented. Table-dependent results need cell-level attribution and protocol review before any proposed removals. The read-only five-paper pilot is `experiments/table_provenance_experiment/run_2026-10-06_table_matching_pilot/report.md`; it measures candidate coverage, not matching accuracy, and records concrete existing dataset-column errors for review.

## Maintained cell-mapping change plans

The audited cell-mapping logic lives in `backend/mapping/`. The maintained
`mapping-plan` command validates saved outputs; it does **not** make model calls or apply
database updates:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.pipeline mapping-plan \
  --run-dir experiments/table_provenance_experiment/run_2026-10-09_mapping_production_recheck3 \
  --output-dir papers/mapping_change_plan
```

Use a fresh output directory. The command skips database initialization and opens SQLite
in read-only mode. It checks complete/error-free assessments, exact result-ID coverage,
unchanged stored rows, unchanged local LaTeX and manifest source hashes. Count proposals
must retain their verified physical cell identity, explicit execution and source-grounded
protocol. Source-bound human protocol reviews remain separate from model accuracy.

The plan retains full database-row snapshots and hashes for future stale-row checks and
rollback. Before opening a writable database connection, the apply CLI checks that the
plan covers every paper and result ID in the frozen manifest, row snapshots and
proposals. The apply function then revalidates included evidence and live row snapshots
inside one transaction. Human overrides are protected. Unresolved decisions never create
numeric repairs, exclusions or count assignments. Outputs include a concise `summary.md`, a
counts-only per-paper `override_counts.log`, and a machine-readable change plan for a
future application step; users do not need to edit that file.

For cell mapping, the agreed count unit is **models trained**: ten complete repetitions
of ten-fold CV give 100 models, while retaining both axes and the reported variability
scope in the evidence. This is not a claim that folds are statistically independent.
Split variability and non-standard uncertainty remain explicitly scoped special cases.

The saved-output check passed all 50 papers (2,072 rows) and produced 837 proposed row
changes. This is a compatibility/safety check, not a fresh end-to-end accuracy evaluation.
Application and rollback have also been exercised on a temporary backup: all 837
proposed rows applied, reapplication was idempotent, and rollback restored every
original data table. Exclusions use reversible flags, never result deletion. New
source-backed configuration variants are recorded and removed on rollback only if
they are unchanged and have not acquired unrelated results. A durable audit receipt
is committed in the same transaction as changes. Stale rows, changed source/evidence,
manual overrides and later edits prevent unsafe application or rollback.

That 837-row plan is a historical dry run, not the current plan to apply. A source-first
replay with the expanded identity guards now proposes 336 counts, 447 copied exclusions,
29 quarantines, and withholds 72 configuration/identity cases among the same 2,072
rows. This includes 24 GotenNet rows whose stored `Adam`/`Muon` labels are optimizer
columns, plus a competing-presentation case where a proposed repair would lose a
diffusion variant. These are saved-output replays, not fresh model confirmations; the
old frozen files remain unchanged. A current-code in-memory pass of the complete row
transformation and plan validator yielded zero validation errors, but direct plan
generation from the frozen files is correctly refused because they predate these guards.
Do not use the historical plan for application; a fresh GLM run and validated plan are
still required.

The writable storage functions are not invoked by `mapping-plan`. A separate opt-in CLI
can apply a reviewed plan; do not run it until the complete fresh plan has been checked
and database changes are explicitly authorized. It requires the
`--confirm-database-write` flag:

For now, apply only through this CLI. The lower-level `apply_plan()` function verifies the
included evidence and row snapshots but does not independently enforce full manifest/result
coverage; direct callers can therefore submit an incomplete plan. A library-level coverage
guard is still required before that function can safely be used directly.

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m scripts.apply_mapping_plan apply \
  --plan papers/mapping_change_plan/change_plan.json \
  --database data/benchmarks.db \
  --confirm-database-write
```

The command reports a plan ID, which is required for an explicitly authorized rollback:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m scripts.apply_mapping_plan rollback \
  --plan-id PLAN_ID \
  --database data/benchmarks.db \
  --confirm-database-write
```

The in-memory validation can safely be repeated on a disposable database with:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.mapping.validate_copy \
  --plan experiments/table_provenance_experiment/run_2026-10-09_production_change_plan_v4/change_plan.json
```

## Fresh maintained mapping execution

`map-results` is the maintained compact extraction/verifier entry point. New runs apply
each complete paper to the database by default, after revalidating every proposal against
the frozen source and row snapshot. Each paper is updated in one SQLite transaction; an
audit receipt makes resume idempotent and manual overrides remain protected. Use
`--database-mode collect-only` to preserve proposals without writing result rows. New runs
adapt from four streams up to
the number of eligible paper tasks, with no fixed concurrency cap. The shared request
gate halves the active window's concurrency after a 429 and honors `retry-after` before
any new request. Rate-limited calls retry through repeated cooldown windows; unrelated
transient failures retain the configured retry bound.
Before starting paper chunks, a run sends one minimal GLM inference preflight through
the same gate. A failed preflight is recorded in `preflight.json` and stops the batch
before any paper requests are launched; retrying later appends another preflight record.
Model/variant repairs must preserve distinguishing configuration axes already encoded
in the stored identity (for example, an optimizer or diffusion operator). Optimizer
column labels must not be mistaken for the architecture when the source identifies a
backbone such as GotenNet; the read-only plan refuses repairs that collapse distinct
configurations.
Only GLM-5.3-Flash with thinking is used, with a
one-million-token total budget, 64,000 completion tokens and an 1,800-second timeout.

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.pipeline map-results \
  --parent experiments/table_provenance_experiment/run_2026-10-09_mapping_production_recheck3 \
  --output-dir experiments/table_provenance_experiment/run_2026-10-09_mapping_50_maintained_v3
```

Compact verification is enabled by default (`--no-compact-verifier` opts out). To collect
the complete run first and apply it later:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.pipeline map-results \
  --database-mode collect-only \
  --output-dir experiments/table_provenance_experiment/run_mapping_collect

UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m scripts.apply_mapping_plan apply-run \
  --run-dir experiments/table_provenance_experiment/run_mapping_collect \
  --confirm-database-write
```

`apply-run` applies all successful papers from a terminal run. If papers failed or remain
incomplete, it asks before applying the completed subset; in non-interactive use,
`--include-finished-only` is the explicit confirmation. The run directory contains
`throughput.md`, `throughput.png` (output tokens/s by model), and
`completion_progress.png` (cumulative successful papers over time), plus their CSV data.

`--parent` reuses only the frozen cohort, source/row inputs and reviewed protocol records,
not model outputs. Without it, the cohort comprises stored-result papers with a non-empty
exported conference field, available LaTeX tables and no adversarial-example title.
`--paper`, `--count` and `--seed` allow scoped reproducible runs. The same command resumes
an existing run, reuses completed chunks, and retries failed papers while preserving
failed attempts. Changed inputs, source or implementation require a new run directory.

Complete per-row output is required; missing/truncated calls remain failures, while
valid abstentions retain their explanation. Extraction sees no old numbers; the
independent verifier receives them only for repair bookkeeping. Every competing-table
hint requires a source-backed disposition. The verifier can explicitly reconcile a
prior unknown/conflicting count or establish an unlisted baseline's scope, but only
with source-bound protocol evidence and explicit execution. No count propagates from
the proposed method solely because a baseline shares its table.

The fresh 50-paper maintained run still needs terminal call/error inspection and
comparison against the source-audited decisions before full readiness is established.
The v2 host run was stopped after exposing a shared-client read-timeout override;
its initial sandbox connection errors and host timeout attempts remain preserved as
infrastructure failures. V3 sets both the request and read timeouts explicitly;
a regression test checks the actual outgoing request timeout, not just SDK defaults.
The default command now applies each completed paper; use `--database-mode collect-only`
when database writes should be deferred to the explicit apply command above.

### Recovery after the full-disk interruption (October 10)

The original V3 supervisor no longer existed when disk space became available again
(208 GB free). Before resuming, the frozen implementation and all fifty source/input
hashes were checked, and every selected database row matched its saved snapshot.
All 488 saved JSON files parsed successfully; thirteen complete assessments had empty
error lists. The same read-only command above resumed the remaining work, reusing
successful papers/chunks and preserving prior attempts. The new host supervisor was
confirmed live as PID 57687. These are recovery checks, not a terminal accuracy audit.

The temporary V4 working copy was lost, but its forty frozen implementation files
survived in the six-paper run's `implementation/` snapshot. They were restored to the
original isolated path and checked against the manifest, including frozen prompts.
All six source/input/row snapshots remain unchanged; the task/source-scope regression
tests passed (22 tests). The previous V4 queue supervisor is dead: its saved waiting
status must not be interpreted as a running queue. V4 calls have not restarted yet.

The follow-up queue was subsequently restored with the durable launcher
`experiments/table_provenance_experiment/resume_scoped_validation.py` (host PID 60681).
Its current state is in V4's `recovery_queue_status.json`, not the original queue file.
It checks frozen code, prompts and inputs, waits for the exact live V3 predecessor
to terminate with unchanged-row proof, and then runs V4 read-only. Neither timer was
reactivated. Provider rate limits in V3 are being handled by the existing shared cooldown.

A broader restored-revision test pass initially found six failures in old V3 fixtures:
they lacked the now-required independent task and uncertainty reviews. Only the isolated
test copy was updated, using explicit task/standard-deviation fixture evidence and bound
reviews; production code and frozen outputs were not relaxed. The resulting 77 tests
passed, covering worker retries, source/task scopes, protocol/CV binding, plan rejection,
and disposable-database apply/undo. Four updated fixture/test files are preserved under
V4's `recovered_tests/` for recovery. This does not replace the pending live V4 audit.

Additional uncertainty round-trip regressions now exercise the actual restored V4
worker, read-only plan builder, and temporary-database storage/undo for STD, SEM,
variance and 95% confidence intervals. Each retains the explicit five-model count,
stores the independently reviewed uncertainty kind in count evidence, leaves the old
STD field untouched, verifies idempotent application and exact row restoration, and
rejects tampered uncertainty metadata. These four tests passed; the broader maintained
mapping/CV/plan/storage/client/consistency suite passed 204 tests against the isolated
revision. No external model calls or real database writes were made by these tests.
The new round-trip test is also preserved in `recovered_tests/`. Live V4 validation,
source-backed outcome review and promotion into the main pipeline remain pending.

Seven additional mocked post-parse integration tests passed against the frozen V4
pipeline: only successful parses are mapped; ineligible papers cause no model calls;
each automatic run gets a fresh destination; preparation retains the one-daytime-stream
defaults; mapping failures and missing unchanged-row proof fail the parse stage. Real
parsers and API calls were not invoked. The restored isolated `backend/prompts/` files
were also synchronized byte-for-byte from V4's frozen prompts, so later automatic
preparation cannot accidentally copy V3 prompts left over from recovery.

An integration blocker remains outside the new mapping worker: the existing
`aggregate` dispatcher returns `(stage_parse(...), stage_export(...))`, and `main`
treats that tuple as success even when parsing/mapping returns False. A strict expected-
failure regression in `recovered_tests/test_mapping_post_parse.py` reproduces this.
Fix the dispatcher to propagate failures during promotion; do not edit either live
run's frozen `pipeline.py`. Seven tests passed plus one expected failure; this known
failure must not be counted as a passing production-readiness check.

The failure-propagation fix is now implemented and tested in a separate promotion
candidate (`/tmp/glm-mapping-promotion-x364sJ`), not in either frozen run. `aggregate`
returns the parse/mapping failure without exporting; `run-all` skips export/build after
parse/mapping failure and also propagates export/build failures. Fourteen integration
tests passed, including the formerly expected-failing case; the broader candidate suite
passed 218 tests with no expected failures. The changed pipeline and integration test
are preserved in `experiments/table_provenance_experiment/promotion_candidate_20261010/`.
Main-checkout promotion still awaits live validation review. No real database writes,
site export, builds, statistics changes or extra model calls occurred in these tests.

The promotion candidate also passed six extract/parse/export integration tests using
temporary SQLite databases and site directories. One eligible local-LaTeX case runs
the real automatic preparation/batch/logging path with mocked model outputs, retaining
one daytime stream and twenty maximum requests; it checks terminal unchanged-row proof,
saved proposals and override logs, and confirms that mapping itself assigns no counts
to the database. The companion no-LaTeX case makes no mapping calls. Count extraction
is mocked separately; these tests do not establish model accuracy. The updated integration
test is preserved alongside the promotion candidate.

V3 reached fifteen successful saved assessments with empty error lists. New source
checks: GDE `1911.07532` table 1 caption at line 302 and setup at 308 support 100
training runs; line 310 explicitly distinguishes copied vanilla GCN from rerun GCN*.
The twelve stored GCN*/GCDE assignments use 100, consistent with the user's eligibility
decision, not the separate ten-run dynamical task or twenty test-undersampling repeats.

Adaptive Sampling `1809.05343` exposes a further setting-label issue to resolve before
promotion: row 248848 (full Adapt/Cora) matches the main table cell at line 446 and the
explicit twenty random-seed trials at 423, but is proposed for quarantine because its
stored label says 10-fold CV and no variant repair was supplied. CiteSeer rows from the
same table instead receive a source-backed variant repair and twenty-model count.
The pipeline must distinguish an incorrect stored label from a genuinely ineligible
source experiment. Do not automatically preserve that quarantine merely because its
source cell is correct. Rows 248849/248850 use the separate component-comparison table
and need independent eligibility review; actual no-variance-reduction ablation 248864
remains excluded. Prose-only official-code FastGCN rerun 248865 remains a legitimate
configuration abstention, not a reason to substitute the copied main-table result.
Original V3 decisions remain frozen; targeted feedback/rerun work is pending.

## Next-revision guard checks (not active in frozen V3)

`backend.mapping.source_scopes` has independently tested helpers for two observed
guard errors: a selected cell matching the old literal units is not a competing
configuration, and uncertainty wording from a preceding table must not leak into
the current table. These helpers are deliberately not wired into the frozen live
run. A percentage caption with multiple fractional mean/std cells in the selected
column now also produces a review hint, not an automatic change of units. Integration
must pair the configuration fix with unit-conflict handling so it cannot turn an
incorrect rescaling into an actionable correction.

Concrete unit review: GIB (`2010.05563`), source line 779 says accuracy in percent,
but lines 784–797 print fractional mean/std pairs. The caption and cells disagree;
score magnitude alone must not settle the units. Current decisions withhold repairs
as a configuration conflict, which is the wrong explanation for this ambiguity.

Concrete task-scope review: GEM (`2104.06643`), rows 162197, 162198, 241540 and 241779
are stored as graph-classification Accuracy. Source line 260 explicitly evaluates
predictions on explainer-produced subgraphs using a pretrained GNN; lines 287–309
report explanation accuracy at different K values. The live mapping selected the
correct cells but labelled them benchmark-eligible and withheld counts as unknown.
Cell identity is therefore not sufficient: the next revision must explicitly verify
the evaluation target/metric before accepting ordinary classification eligibility.
This must remain separate from ablation wording; a normal method-comparison table
can still measure an incompatible target. Preserve these frozen decisions as a
regression case rather than rewriting their outputs.

### Partial live source review, 2026-10-09 (not final accuracy evaluation)

Reviewed all 30 row decisions in three newly completed papers against local source,
including the 29 accepted counts and one configuration abstention. This is a
convenience sample of completed outputs, not an unbiased accuracy denominator.

- CoGSL `2201.05540`, rows 252896–252905: ten models for each of ten Citeseer
  entries. Header line 376 identifies method columns, line 399 supplies F1-macro
  values, lines 462–464 explicitly describe authors' baseline implementations and
  ten runs for all methods, and line 468 links the protocol to the result table.
  The accepted count and Accuracy-to-F1-macro repairs are source-supported.
- ProtGNN `2112.00911`, rows 174624–174627 and 269236–269239: three models over
  random data splits, not the stored scaffold split or ten-fold CV. Lines 295–301
  distinguish backbone and method columns; lines 315 and 319 establish the split
  and three runs. Seven accepted counts and split-label repairs are supported.
  Row 269237's old 91.7±2.9 is in the GIN/ProtGNN+ column, not the selected
  GCN/ProtGNN 76.7±6.4 cell (line 297). Withholding this default-backbone repair
  is correct while its intended configuration remains unresolved. A regression
  test ensures the unit-repair fix still catches this genuine column conflict.
- LADIES `1911.07323`, rows 274383–274394: ten models for all twelve selected
  method/dataset cells. Lines 398–434 identify the five-layer benchmark table;
  lines 445 and 449 establish authors' execution and ten trainings for every
  method/dataset; line 451 explicitly defines micro F1. Counts and metric-label
  repairs are supported. The source says "mean and variance", not standard
  deviation (line 449): no variance-to-std conversion is justified from the ±
  notation alone. Split labels also remain unverified. These uncertainties do
  not invalidate the explicit trained-model count or authorize statistical use.

Additional live source check: LR-GWN `2509.06743`, rows 203436–203445. Line 718
reports **between five and ten** independent runs and **standard error of the mean**;
it does not establish an exact count or standard deviation. Eight baseline origins
remain unknown; citation markers alone do not prove copying. The two proposed-method
rows correctly abstain on an exact count, but their uncertainty is not yet explicitly
labelled SEM in the proposal. The new uncertainty-review hint helper catches SEM,
confidence intervals and explicit "mean and variance" wording using local context
plus this cell's protocol evidence. This preserves global setup statements across
subsections without borrowing unrelated tables' uncertainty or converting SEM/variance
into std. These remain hints requiring independently verified scope in the next revision.

Task-scope quarantine proposals use the canonical `propose_quarantine` action and
the distinct `incompatible_evaluation_target` reason. The current frozen plan validator
does **not** accept this new reason: verifier schema, worker, plan validation and
application proof validation must be integrated together before it is actionable.

An isolated development copy at `/tmp/glm-mapping-revision4-5Bra4p` now connects
the task review schema, verifier instructions, worker gate and plan proof validation.
It also connects the unit-conflict and physical-cell/configuration safeguards.
Targeted integration tests cover a supported count passing worker and plan validation,
incompatible targets producing quarantine proposals, unclear targets withholding
actions, and plan validation rejecting a task review bound to a different cell.
These 33 targeted tests pass; lint passes. This is not a live GLM quality evaluation
or a full revision-four regression run. Existing tests/legacy fixtures and automatic
post-parse integration still need migration and checking before promotion. The active
V3 implementation and prompt hashes remain unchanged; no database writes occurred.

The isolated revision now also invokes read-only mapping after successful parsing
and repetition extraction. It uses a fresh run directory, default one daytime stream
and the existing adaptive nighttime limiter; it saves proposals, never applies them.
Automatic invocation skips newly parsed papers that lack eligible conference results
or local source, while explicit `map-results --paper` retains strict eligibility
checking. Failed mappings propagate failure rather than being counted as successes.
Regression fixtures were updated to include the newly required source-bound task
review, without weakening the guard. The broader relevant suite passed 216 tests;
an additional parser-orchestration test passed and confirms only successfully parsed
paper IDs enter the two new analysis stages. Promotion and fresh-model validation
of this isolated revision are still pending; these results do not certify production
accuracy.

The isolated revision now separates reported uncertainty from trained-model counts
through verifier schema, source-scoped hints, worker metadata, plan revalidation and
stored count provenance. Standard errors, variance, intervals and unclear quantities
cannot authorize std-field repairs. They do not erase an independently established
model count. Source inspection of `2310.07235` found an explicit five-run protocol
(lines 506 and 533), while V3 suppressed six counts because their table reports CI.
The isolated interval guard preserves explicit counts but still rejects competing
configuration repairs; an integration test confirms SEM also preserves the count
and that tampering with its uncertainty assessment is rejected by the plan validator.
The presentation-safety tests now import the maintained implementation, rather than
the legacy experiment helper, so they actually test the code being integrated.
No frozen V3 outputs were rewritten and no uncertainty-to-std conversion was performed.

An end-to-end disposable-database test now exercises worker output, change-plan
validation, application, idempotent reapplication and exact rollback together. It
confirms that an explicit five-model count and SEM provenance survive application
without converting or replacing the existing std field, then undo restores the
complete original result row. Only a temporary fixture database is written.

The six-paper GLM validation inputs are prepared in
`experiments/table_provenance_experiment/run_2026-10-10_mapping_scoped_v4`, with code
and prompts frozen from the isolated revision. The cohort is GEM, GIB, LR-GWN,
ProtGNN, GAT initialization and LADIES, covering task mismatch, caption/cell unit
conflict, SEM, random splits/competing backbones, CI and variance. No model calls
have been started in that run. Do not edit its frozen implementation in place;
further implementation changes require a new validation directory.

The scoped V4 validation is now queued behind V3, not running concurrently with it.
Queue supervisor PID 1773484 executes `/tmp/queue_glm_scoped_validation.py` using
the isolated revision. Progress is in the V4 directory's `queue_status.json`.
It waits for V3's terminal phase, verified unchanged selected rows, and termination
of the exact recorded supervisor before issuing any model calls. An exited but
non-terminal predecessor, PID reuse, changed frozen implementation/prompts or absent
endpoint fails the queue rather than restarting jobs. It reuses the authorized key
without copying credentials into artifacts and allows only GLM-5.3-Flash. No new
notification timer was created or reactivated.

Additional origin/scope source checks:

- MPSN/SIN `2103.03212`: rows 229115, 229124 and 229127 have an explicit single
  ten-fold evaluation protocol at line 1310, giving ten trained models under the
  agreed convention, not 100. No outer repetitions are stated for these TU cells;
  the five-seed trajectory experiment and untrained ten-initialization experiment
  elsewhere in the paper must not supply their count. Three copied dispositions
  (229106, 229111, 229120) have strong earlier exact-result support beyond citation
  markers: PK/PROTEINS 73.7±0.7 appears in `2009.06211` lines 462–488; GIN/PROTEINS
  76.2±2.8 and GIN/NCI1 82.7±1.7 appear in `1905.11136` lines 834 and 863. These
  earlier local tables were inspected, including dataset headers. This supports
  the copying interpretation but does not create a hard chronology rule or imply
  that a citation alone proves copying. The other eighteen baseline origins remain
  unresolved; this source check does not certify their individual cell assignments.
- HEI `2408.09490`: nine baseline rows 272965–272973 have a ten-trial caption
  (line 392), but their execution evidence points only to the baseline citation
  list (line 532), not a clear statement of authors' execution. The proposed-method
  row 272974 is independently self-evaluated (line 536), but the initial and verified
  selections disagree about backbone/column scope. The table explicitly distinguishes
  LINKX/GloGNN++ and Full/High-Hom/Low-Hom tests (lines 397–399 onward); the settings
  paragraph defines these distinct test groups at line 527. These are origin and
  configuration abstentions, not timeout failures or evidence that ten trials is
  missing. No count is forced from the table caption or fallible stored numbers.

### Candidate setting-conflict safeguard (10 October)

The isolated promotion candidate now distinguishes an erroneous stored setting label
from an actually incompatible source experiment. For a uniquely identified, executed
benchmark, a wrong CV/split label requires an independently supported old-to-new
variant repair; it does not alone justify quarantine. Missing or unclear evidence
withholds both the repair and count. Source-proven incompatible experiments and real
ablations remain excluded. Reviews are bound to the source, selected cell and saved
verifier output; cell-scope evidence must cover the complete cell span.

The candidate passes 225 regression checks, including worker-to-plan-to-disposable-
database application of a corrected split label with its count, idempotent reapplication
and exact result-row rollback. This is implementation evidence, not live model accuracy.
The code and new test are preserved under `promotion_candidate_20261010/`; they are
not promoted into the frozen V3/V4 runs. A fresh targeted GLM validation remains
required before promotion. Production database rows have not been changed.

The targeted live validation is now frozen in `run_2026-10-10_mapping_setting_v5`
(Adaptive Sampling: 23 stored rows; GDE eligibility control: 12). Its supervisor
`run_setting_validation.py` waits for the scoped V4 supervisor to exit and for
terminal unchanged-row verification before making any GLM calls. It rechecks frozen
implementation, prompts, source inputs and selected rows at startup. Failures or
PID reuse stop the queue; they do not automatically relaunch a predecessor. There
is no additional timer. Four additional adversarial grounding tests check wrong old
labels, out-of-range evidence, partial cell spans and missing verifier references.

### Numeric-subscript guard correction (10 October)

GraphTOP `2510.22451` revealed a deterministic grounding failure: the literal-number
regex rejected means followed by an underscore, such as `55.69_{\pm 5.74}`. The
source table and all 48 saved candidates over twelve rows were inspected; with the
isolated fix, all 48 pass literal and physical-column grounding. This does not
establish correct dataset selection, configuration or final count assignment.
Six regression tests cover ordinary, bold and underlined subscript notation, retain
identifier-boundary rejection and reject a wrong physical column. The combined
candidate suite passes 235 tests.

`run_2026-10-10_mapping_numeric_v6` freezes a fresh 35-row validation on GraphTOP
and `2310.01794` (the latter also has mistaken CV labels and table-scoped ten-run
counts). `run_numeric_validation.py` waits for terminal V5 completion and supervisor
exit. The numeric candidate is separately saved in `promotion_candidate_numeric_20261010`,
so neither the already frozen V5 implementation nor any original decisions change.
Actual GLM outcomes and a source-backed comparison remain required before promotion.

### Explicit upstream-protocol reconciliation feedback

Local source review of GCN-squared `2007.08349` found the proposed TU evaluation
explicitly uses ten-fold CV (lines 849 and 940), with standard deviation across the
ten folds. Two mapped own-method rows were nevertheless withheld because the verifier
supported their counts but did not complete the required upstream protocol-scope
review; an alternate method alias also lacked an exact prior key. No count is forced
from the alias or from another method's protocol.

The isolated candidate now detects that inconsistency before the final binding gate
and asks the verifier to explicitly reconcile the unknown/conflicting/aliased input
against the selected source cell. A grounded independent scope review is still
required; persistent missing reviews remain abstentions after the existing bounded
retry. Unsupported counts and legitimate protocol abstentions do not trigger this
feedback. This change is preserved separately in `promotion_candidate_protocol_20261010`
and does not change the frozen V3–V6 implementations or their decisions.

The final targeted protocol validation is frozen in
`run_2026-10-10_mapping_protocol_v7` (GCN-squared: 42 rows) and queued through
`run_protocol_validation.py` after V6 exits. This preserves the existing shared-key
execution chain rather than starting independent overlapping batches. Candidate
regressions now pass 239 tests, including worker-level successful reconciliation and
bounded persistent abstention. The six isolated pipeline integration tests also pass:
they exercise extraction, parsing, automatic read-only mapping preparation, saved
override logs and export against disposable paths and databases. The fourteen
post-parse tests confirm that mapping failure propagates and prevents downstream
export/build. Neither test set makes external model calls or modifies production rows.

Additional source audit of the resumed V3 run: SPAGAN `2101.03464`, nine actionable
rows inspected (three counts, six copied dispositions). Own-method rows 264231,
264238 and 264247 map to Cora/Citeseer/Pubmed cells at lines 495–496; the table row
wraps across two source lines, so the physical indices are respectively 1, 1 and 2.
The ten fixed-split executions are explicit at lines 440–441, with own-method
implementation at lines 428–439. These ten-run assignments are supported; the stated
fixed split is not split variability or CV.

Copied Pubmed rows 264239, 264240, 264241, 264243, 264244 and 264245 were checked
against the primary local GAT source `1710.10903`, not just database coincidences.
Its table header and rows at lines 298–314 show exactly the same dataset, methods,
means and available standard deviations (MLP 71.4, DeepWalk 65.3, Chebyshev 74.4,
GCN 79.0, MoNet 78.8±0.3 and GAT 79.0±0.3). The complete cross-dataset row pattern
also matches. This supports copying under the agreed strong-indicator rule, without
turning an earlier coincidence or a citation into a hard-coded copying criterion.
The matching GAT Pubmed secondary presentation at SPAGAN line 620 is a duplicate
reference inside a sensitivity table; the main benchmark cell at line 492 is preferred.
This nine-row source audit does not certify the remaining fifteen rows or estimate
corpus-wide accuracy. Paper links: https://arxiv.org/pdf/2101.03464 and
https://arxiv.org/pdf/1710.10903. No production rows were changed.

### Non-numeric source cells: explicit OOM

HSAN `2212.08665` row 177666 (DCRN/AMAP/F1) has no numeric source result: the
AMAP block's DCRN cell is explicitly OOM, including its F1 row at line 448. Its
stored 0.7086±0.0018 instead matches the CITE accuracy cell. The frozen V3 mapper
correctly refuses to borrow that score but leaves this invalid row unresolved.

The isolated candidate adds an independent `non_numeric_review` for this case.
Quarantine requires exact target method/dataset/metric evidence inside the same
table, a single physical cell containing OOM, no competing numeric candidates and
an explicit verifier statement that no matching numeric presentation exists. Blank
or dash cells remain unresolved. Planning re-derives this proof from the verifier
payload and actual source; forged reviews, wrong columns, changed datasets/sources,
missing call references and competing numeric candidates are rejected. Reversible
fixture-database application preserves the old score for audit, clears any old
count, records source evidence, supports idempotence and restores the original row
on rollback. Seven targeted tests pass. The candidate is preserved separately in
`promotion_candidate_oom_20261010`; a fresh GLM check is still required.

Source review also confirms HSAN line 523 explicitly reproduces all baselines and
conducts ten runs. Sampled F1 repairs retain the intended dataset and metric:
177657 (MGAE/AMAP), 177671 (MGAE/EAT), 177680 (DCRN/EAT) and 177684 (HSAN/EAT)
point to the F1 rows at 448/456, not the old accuracy or adjacent-dataset cells.
SUGAR `2101.08170` explicitly states single ten-fold CV at line 585 and copied
baseline origins at line 587; its four proposed-method assignments must therefore
remain ten models, not 100. Its table additionally separates parenthesized ranks
from standard deviations. These source checks are not a corpus accuracy estimate.

The OOM guard additionally strips unescaped LaTeX comments without changing line
numbers or original table ordinals. Commented-out OOM cells/tables and numeric cells
with an inline OOM comment cannot justify quarantine. Ten OOM tests and 249 combined
candidate regressions pass. Fresh GLM validation is frozen as
`run_2026-10-10_mapping_oom_v8` (HSAN: 28 rows), queued by
`run_oom_validation.py` strictly after V7 terminal validation and supervisor exit.
The expected source-backed outcome is quarantine of row 177666 without borrowing
another dataset's score, while retaining verified numeric F1 repairs/counts for the
other rows. That expectation remains unproven until the live outputs are inspected.

### Visible numbers versus formatting arguments

A synthetic source-grounding test exposed that `\color[HTML]{000000}` could be
misread as a printed zero score, even in an OOM cell. The isolated literal guard
now removes colour arguments and the structural arguments of multirow, multicolumn,
font-size and rule commands before matching scores. Visible numeric content inside
formatting wrappers is retained, including real zero scores and subscript uncertainty.
Twelve focused tests pass, including rejection of a fabricated zero anchored only to
a colour code. Replaying the tighter guard against 233 actionable numeric selections
from the completed frozen V3 assessments rejected none. This is a deterministic
grounding regression check, not new evidence for their origin/protocol accuracy.
The change is preserved in `promotion_candidate_literal_20261010`; frozen live
validation implementations and decisions remain unchanged.

### Final validation contract

The first 23 completed V3 papers cannot be treated as final-candidate assessments:
their verifier outputs lack the required independent task and uncertainty reviews.
The source-first extraction prompt has the same hash, but its input is not identical:
the later candidate supplies each target's `evaluation_task` as an additional fallible
identity hint. An exact saved-call/content/output check therefore found zero reusable
chunks among the 36 completed extraction chunks inspected. Do not silently inject
the missing review fields, relax the final schema or claim these old outputs validate
the final pipeline.

After reviewing the targeted validations and consolidating the fixes, the final
50-paper validation must use fresh final-contract extraction and verification calls.
Preserve the original runs for before/after comparison. Production promotion requires
terminal error checks, unchanged selected rows, source-backed review of the changed
and high-risk decisions, and a valid final change plan. The existing disposable-
database application/rollback tests must pass against that final plan. Actual
production application remains separately subject to explicit user authorization;
statistics remain deferred. The copied-result visibility policy is still awaiting
the user's answer and must not be silently changed during promotion.

Threaded request-gate tests now exercise actual admission: twenty requests may
enter at the nighttime cap while four additional threads wait; at 08:00 Berlin,
existing concurrent requests finish but new requests wait until the single daytime
slot is available. A provider `retry-after: 30` blocks every new stream until the
shared window resets. These three tests pass without external calls; the combined
candidate suite passes 258 tests. This verifies gate behavior, not provider throughput
or the accuracy of any model output.

Release checks: the candidate mapping package and pipeline pass Ruff. The configured
Bandit gate (`-ll -ii`) passes for the mapping package after constant audit-table
queries were made literal and dynamic result-update identifiers were explicitly
restricted to schema-known ASCII SQL identifiers. All values remain parameterized;
SQLite metadata names in copy validation retain escaped double quotes. A malicious
schema-column test confirms rejection without changing any fixture result. There are
still two low-confidence dynamic-SQL scanner notices below the configured confidence
threshold, documented here rather than hidden with suppressions. This is not a claim
that the unrelated repository code has passed a full security audit.

The repository pre-commit hook always executes a WAL checkpoint on the real database,
even for code-only commits. No commit hook has been invoked during this read-only
mapping task; a final code commit must avoid unauthorized database writes without
bypassing the configured hooks. All currently running implementations remain frozen.

The candidate backend and full regression fixtures are now consolidated under
`promotion_candidate_literal_20261010`, not only in `/tmp`. Reproduce the isolated
checks from the repository with:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python \
  experiments/table_provenance_experiment/promotion_candidate_literal_20261010/validate_candidate.py \
  --integration
```

The runner verifies the imported implementation path and uses saved tests with
disposable databases/workspaces and mocked model calls. It does not promote code or
apply production proposals. The unit-only invocation passes 259 tests from this
persistent snapshot.
The same persistent runner with `--integration` passes all 265 tests, including six
end-to-end pipeline cases. Only pytest plugin-rewrite and SQLite datetime-adapter
deprecation warnings remain; they are not external-call or database-application errors.

Source audit: HC-GAE `2405.14742` own-method rows 270803, 270810, 270817, 270825
and 270844 map to the correct Cora/CiteSeer/PubMed/PROTEINS/MUTAG benchmark cells
at lines 365/385. Node setup at line 405 explicitly uses single ten-fold CV, and
graph classification at line 417 explicitly reports mean/std over ten-fold CV;
ten fold fits, not 100 or ten independent neural-network seed repetitions, are
the agreed count. The source describes SVM evaluation of learned representations,
so the fold count must not be described as evidence of ten independently retrained
encoders. The specific old PubMed Planetoid label is contradicted and repaired to
ten-fold CV. Node-baseline results are copied from previous papers "if available"
(line 403); this conditional statement does not automatically establish copying or
current execution for every individual cell. No production rows were changed.

Additional source review: QM9 optimizer results in `2605.27662` explicitly report
mean MAE and standard deviation over four seeds (expanded source lines 132–154).
Grid-search fits are not additional evaluation repetitions. The selected Adam/Muon
columns belong to `tab:qm9`; an explanation identifying that table does not mean
the old database `table_ref` has itself been repaired. MLG `1603.06186` retains the
user-reviewed ten evaluation repetitions, with inner slack-parameter tuning folds
excluded. This is a source-bound human interpretation, not an independently resolved
model prediction, and must not be included as fresh model-accuracy evidence.

A candidate-only safety regression reproduced an OOM annotation beside a printed
numeric score being treated as an unambiguously failed result. The OOM guard now
requires the selected physical cell to contain no visible numeric values, using
the formatting-aware literal parser. Both score-plus-OOM cases must abstain; pure
OOM still permits a source-grounded quarantine proposal. Frozen V8 and other live
implementations are unchanged; the consolidated candidate requires fresh validation.
The consolidated candidate now passes 267 regression/integration tests after this
fix, and the changed guard and tests pass Ruff. These tests use disposable databases
and mocked model calls; they do not establish live extraction accuracy. The maintained
run has 26 completed assessments with empty error fields; full pipeline completion
and terminal selected-row invariance remain pending.

Candidate plan/application safety review reproduced an injected numeric correction
being accepted even though the saved independent verifier supplied no repair. The
plan gate now reconstructs the correction from the verifier's repair, the selected
literal cell and original row fields. It then reapplies deterministic percentage/std
normalization, setting-label withholding and the uncertainty-kind policy, rather than
accepting an arbitrary correction payload. New tests reject changed values, methods,
old fields, evidence and missing verifier approval, while retaining legitimate
partial normalization and withheld label refinements. The disposable variant/undo
fixture now supplies an actual independently supported metadata-error review, not a
hand-added unverified correction. No live implementation or database row was changed.

Raw reconstruction against 93 saved V3 repairs identified twelve differences caused
by V3's subsequent setting-label safety transformation; these are not twelve model
errors. The planner now uses that same deterministic transformation. V3 has no new
independent uncertainty review, so it remains incompatible with the final schema;
this replay does not make the older outputs eligible for final application.
The reconstruction also reapplies the separate setting-scope guard: an unknown or
copied baseline may retain a numeric repair without inheriting the authors' split.
Nine dedicated repair-binding tests now cover this boundary and pass. The full
suite passed 276 tests before the final setting-scope addition; its final rerun is
in progress. All four prepared V5–V8 follow-up manifests, input/source snapshots and
selected database rows passed their read-only preflight checks without model calls.

The final consolidated regression/integration run passes 277 tests. A fresh final
cohort is now prepared at `run_2026-10-10_mapping_50_final_v9`: fifty papers and
2,072 stored rows, GLM Flash with reasoning, five explicitly authorized daytime
streams and an adaptive nighttime cap of twenty. Preflight checked every frozen
implementation/prompt/input hash and every live selected row against its snapshot.
There are no model calls, chunks or proposals in this prepared run. Only prior
table-level protocol inputs and scoped human reviews were retained; row-mapping
extraction and independent verification must be freshly generated. The candidate
implementation is now frozen by this manifest and must not be edited in place.
Launch remains conditional on source-reviewing the targeted V4–V8 outcomes; it is
not automatically queued and does not authorize any production database update.

Additional source-backed identity audit: `2502.09263` rows 211910–211912 (ZINC)
and 211929–211931 (Peptides-struct) contain scores from GCN+/GIN+/GatedGCN+
but are stored under the plain backbone names. Each row has exactly one matching
original extraction entry when dataset, metric, mean/std and table reference are
checked; those saved entries explicitly retain the `+` model label. Primary source
lines 395/398/401 and 472/475/478 are the enhanced cells. Captions at lines 362
and 440–441 distinguish enhanced methods from copied plain-baseline results.
The live database's model aliases map all three enhanced names to the plain models,
confirming an identity-loss mechanism rather than a repetition-count ambiguity.
The frozen V3 guard correctly withholds replacing these with a different vanilla
configuration, but does not yet recover the original enhanced identity. A specific
user question asks whether to restore the source-confirmed `+` identity in the
dry-run. This remains a pending policy decision; no raw extraction, alias, real row,
frozen candidate or prepared-run input has been changed. Original extraction labels
would be fallible provenance hints, not independent proof of counts or execution.

### 2026-10-12: method-modifier safety and fresh targeted validation

Host checks found the recorded V3 and V4–V8 supervisors absent. V3 saved 28
assessments with empty error fields but no terminal invariant check; its stale
running status does not establish completion. The old outputs remain unchanged.

The isolated modifier candidate reproduced source-label aliases transferring
counts between GCN and GCN+, even after punctuation-preserving method matching.
The binding guard now withholds counts when the selected method and physical
source row disagree on a +/* marker. The verifier receives bounded-retry feedback
to repair that identity. Multirow/multicolumn formatting arguments are removed
before interpreting the row label, so alignment stars are not model qualifiers.
All 289 regression/integration tests pass; Ruff passes. Tests use disposable
databases/mocked calls and do not establish external-model accuracy.

A fresh frozen five-paper validation is prepared in
`run_2026-10-12_mapping_modifiers_v10`, using GLM Flash with reasoning and five
daytime streams (adaptive night cap twenty). It covers 2502.09263, 1911.07532,
2007.08349, 2212.08665 and 2510.22451, reusing prior table-level protocol inputs
but not row-mapping model outputs. It must finish and receive primary-source
review before a final fifty-paper validation. No real database corrections,
quarantines or statistics are authorized by this validation.

Source inspection during V10 found three valid GDE rerun cells on source line 298:
that line contains both GCN and GCN*. The first-label heuristic falsely withholds
rows 157187, 267132 and 267139. A separate unfrozen candidate,
`promotion_candidate_rows_20261012`, now resolves the physical row from the
selected cell-column ordinal, strips rule/colour/alignment decorations and ignores
commented content. It preserves nested formatted variant labels and declines
ambiguous multi-row aliases rather than inventing the first method. Replay against
all three actual GDE cells returns GCN*. Source lines 308 and 310 support 100
training runs and current-paper execution of GCN*, respectively. The change-plan
gate also rechecks physical method identity before any actionable application.
All 299 regression/integration tests and Ruff pass. No V10 code, inputs or outputs
were changed; these improvements still require fresh live validation.

V10 also exposed a systematic coverage blocker in the independent task guard:
every stored row in 2502.09263 has a null evaluation_task, so all 37 are withheld
despite source-backed metric/task and copied-origin reviews. Frozen cohort
snapshots show this missing field on 607 of 2,072 rows across thirteen papers.
This is a storage-completeness issue, not 607 demonstrated model mistakes. A user
question asks whether the dry-run may infer missing task labels from independently
verified paper/dataset/metric evidence, without overriding conflicting labels.
The guard remains unchanged pending that decision.

GraphTOP's six stored Amazon2M rows are also unresolved: its actual Amazon dataset
has 24,492 nodes, 300 features and five classes (source line 1001), not an assumed
Amazon2M benchmark. The source's reference to Platonov et al. is at line 431.
Do not count these abstentions as call failures or silently treat the datasets as
aliases. Separately, numeric repairs between pretraining strategies in that main
table need configuration-scope review before application; disposition totals do
not establish correctness. No final fifty-paper model run has been launched.

V10 completed all five papers with no assessment errors. All 23 saved extraction/
verification calls have finish_reason=stop; status records pipeline_terminal=true,
phase=complete and selected_rows_unchanged=true. Its 131 row dispositions are
18 count proposals, 26 copied exclusions, one OOM quarantine, 64 missing-task
abstentions, nine targeted-validation abstentions and thirteen unknown origins.
These are coverage/disposition totals, not accuracy. The OOM proposal is row
177666, DCRN/AMAP/F1: primary source line 448 column 11 contains OOM, consistent
with the earlier source audit. GCN-squared now proposes counts on three own-method
rows rather than one; their individual source scope still needs review. The final
full-cohort gate remains closed pending missing-task handling, physical-row fixes,
enhanced-method identity recovery and pretraining-configuration repair review.

Primary-source review confirms the three GCN-squared count proposals: rows 249431
(MUTAG), 249442 (PROTEINS) and 249454 (NCI1) bind to the own-method row at line
884. Line 849 explicitly describes current-paper execution and ten-fold averaging;
line 940 distinguishes second-fold hyperparameter optimization from reporting the
mean/std across the ten evaluation folds. Under the agreed total-model convention,
each receives ten, not one hundred. This is a three-row source check, not an audit
of all 42 rows or all proposed corrections.

Configuration-repair follow-up reproduced a missed competing-cell hint when the
method appears after a leading strategy column. GraphTOP rows 149227 and 149228
were proposed for numeric changes, but their old mean/std pairs occur in source
lines 493 and 487, respectively. Line 493 is GraphPrompt+ (the original saved
extraction also retains the + label), while line 487 is ProNoG under LP-GPPT.
Replacing those scores with the first GraphCL strategy is not justified merely
by a missing strategy label. The competing-cell guard now inspects both leading
label columns and withholds such repairs. Physical method binding also recognises
a method after an empty or populated strategy column, preserving +/* markers.

The candidate's priority feedback and prompts now clarify that source order only
breaks ties between equivalent presentations, not distinct configurations in a
main table. Extraction lists those alternatives with separate configuration axes;
verification must establish the chosen identity or abstain rather than silently
switch strategies. The source-priority unit tests now import the maintained
candidate helper directly instead of the older experimental helper. All 303
regression/integration tests and Ruff pass. A fresh two-paper V11 validation
(GDE and GraphTOP) tests these changes, with no reuse of row-mapping outputs and
no changes to the frozen V10 run or live database.

V11 finished both papers with empty terminal assessment error fields and unchanged
selected rows. GDE's twelve stored results now all receive 100 runs, including
the three GCN* cells incorrectly withheld in V10. No numerical repairs are
proposed. GraphTOP's five resolved Minesweeper rows retain their source-supported
values with five runs; row 149228 stays at 0.6611 ± 0.042 under LP-GPPT, as
reported on line 487. Lines 445–452 explicitly specify the shared architecture,
training of each method and five random-seed runs. The sixth Minesweeper row,
149227, remains unresolved because its stored GraphPrompt label conflicts with
the GraphPrompt+ source cell at line 493. All six Amazon2M rows remain unresolved.
GraphTOP required three schema-failed verifier attempts before valid outputs;
the failures are retained, not mistaken for completed assessments or truncation.

The separate audit candidate fixes override logs counting field repairs on
abstentions/quarantines even though the application planner ignores those repairs.
Six direct maintained-code tests reproduce and cover this boundary; proposed
dispositions remain counted separately from applicable field changes.

A second next-candidate fix permits a verified different-dataset source cell to
serve as exclusion evidence, not as a replacement benchmark. It requires a
source-bound incompatible_experiment review, exact old-variant echo, verified
candidate selection and supported current-paper execution/origin. Without those
conditions, dataset mismatch still abstains. The proposer returns quarantine with
no count/correction before any numeric assignment path; plan validation rechecks
the independent setting review. Six tests cover this path and missing/unclear/
unbound review failures. All 315 regression/integration tests and Ruff pass.
These are fixture checks, not a live accuracy claim for the new exclusion path.

V12 finished GraphTOP with no terminal assessment errors and unchanged rows.
It recovered all six Minesweeper counts (five each) and correctly proposes restoring
GraphPrompt+ on row 149227 without changing its score/std. The six Amazon2M rows
remain withheld: GLM identifies a mistaken stored dataset label, not an ineligible
Amazon experiment. This is the correct distinction; do not force the verifier to
call a metadata error an incompatible protocol merely to permit quarantine.

The user explicitly approved proposing Amazon-ratings for those six rows
(149218–149223). The next candidate adds per-row human-reviewed dataset identities:
old row and source hashes, exact old/corrected/source names, target registered ID,
source evidence and authorization are frozen inputs. Matching uses the approved
physical source label while retaining original row snapshots. Planning/application
reject a missing/tampered authorization or changed target registration; global
dataset aliases are not changed. Only applicable independently verified proposals
can include dataset moves. Applying/undoing a move and reapplication were tested
only on disposable fixtures. Dataset override counts are included in the per-paper
log. All 326 regression/integration tests pass. The approved fresh one-paper run is
`run_2026-10-12_mapping_dataset_approved_v13`; real database rows remain untouched.
