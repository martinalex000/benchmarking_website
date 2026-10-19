from backend.mapping.decisions import Candidate, Fact, Protocol, Verdict, propose
from backend.mapping.schema import Span


def candidate(table_id, row_line, eligibility):
    return Candidate(
        table_id=table_id,
        displayed_mean=82.88,
        displayed_std=0.41,
        divisor=100,
        method="wGNN1",
        dataset="Cora",
        metric="Accuracy",
        configuration="wGNN1, GCN base",
        eligibility=eligibility,
        main_experiment=False,
        row_evidence=Span(start_line=row_line, end_line=row_line),
        column_evidence=Span(start_line=row_line - 1, end_line=row_line - 1),
        cell_evidence=Span(start_line=row_line, end_line=row_line),
        protocol=Protocol(
            design="repeated_training",
            training_repetitions=10,
            cv_folds=None,
            cv_repetitions=None,
            dataset_splits=None,
            repetitions_per_split=None,
            reported_runs=10,
            variability_scope="training_runs",
            explanation="Ten runs",
            evidence=[Span(start_line=1, end_line=1)],
            scope_evidence=[Span(start_line=1, end_line=1)],
        ),
        cell_column_index=1,
        configuration_axes={"base_model": "GCN", "variant": "wGNN1"},
        identity_evidence=[Span(start_line=row_line - 1, end_line=row_line - 1)],
    )


def test_duplicate_benchmark_presentation_cannot_upgrade_selected_ablation():
    source = "\n".join(
        [
            "We report the average over 10 runs.",
            r"\begin{table}",
            r"Method & Cora \\",
            r"wGNN1 & 82.88 $\pm$ 0.41 \\",
            r"\end{table}",
            r"\begin{table}",
            r"Method & Cora \\",
            r"wGNN1 & 82.88 $\pm$ 0.41 \\",
            r"\end{table}",
        ]
    )
    ablation = candidate(1, 4, "ablation")
    duplicate = candidate(2, 8, "benchmark")
    fact = Fact(
        result_id=1,
        candidates=[ablation, duplicate],
        origin="self_evaluated",
        origin_evidence=[Span(start_line=1, end_line=1)],
        execution_evidence=[Span(start_line=1, end_line=1)],
        repair=None,
        explanation="The source cell was evaluated.",
    )
    verdict = Verdict(
        result_id=1,
        corrected_fact=fact,
        verified_candidate_indices=[0, 1],
        selected_candidate_index=0,
        origin_supported=True,
        execution_supported=True,
        protocol_supported=True,
        repair_supported=False,
        setting_status="supported",
        eligibility="ablation",
        explanation="The selected main presentation is an ablation.",
    )
    row = {
        "result_id": 1,
        "model": "wGNN1",
        "dataset": "Cora",
        "metric": "Accuracy",
        "variant": "wGNN1, GCN base",
        "value": 0.8288,
        "std": 0.0041,
    }

    proposal = propose(row, verdict, source, allow_experiments=True, allow_identity=True)

    assert proposal["action"] == "propose_quarantine"
    assert proposal["selected_candidate"]["table_id"] == 1
    assert proposal["selected_candidate"]["eligibility"] == "ablation"
