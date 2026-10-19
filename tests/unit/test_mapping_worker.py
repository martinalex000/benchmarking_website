import json

import pytest

from backend.mapping import worker
from backend.mapping.compact_verification import (
    CompactCandidateAddition,
    CompactRowDecision,
)
from backend.mapping.outputs import (
    MappingCandidate,
    MappingFact,
    MappingVerdict,
    PresentationReview,
)
from tests.unit.test_assignment_protocol_refresh import reviewed_fixture
from tests.unit.test_mapping_protocol_binding import key


def setup(tmp_path, prior=True):
    row, initial, source, _ = reviewed_fixture()
    source = source.replace("10-fold CV for tuning, repeated 10 times", "5 runs")
    row.update(variant="fixed")
    raw = initial.model_dump()
    raw.update(
        protocol_scope_review={
            "prior_reconciled": True,
            "scope_supported": True,
            "evidence": [{"start_line": 5, "end_line": 5}],
            "explanation": "Explicit own-method execution and five runs apply to this cell.",
        },
        presentations=[
            {
                "table_id": 1,
                "decision": "same_experiment",
                "evidence": [{"start_line": 3, "end_line": 3}],
                "explanation": "Only main benchmark table.",
            }
        ],
    )
    verdict = MappingVerdict.model_validate(raw)
    fact = MappingFact.model_validate(raw["corrected_fact"])
    paper = tmp_path / "papers" / "one"
    paper.mkdir(parents=True)
    (paper / "protocol_keys.json").write_text(json.dumps([key(repetitions=5)] if prior else []))
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    for name in ("result_mapping.txt", "result_mapping_verification.txt"):
        (prompts / name).write_text("Test prompt")
    (prompts / "result_mapping_delta_verification.txt").write_text(
        "Output contract\n\nReview rules"
    )
    return row, fact, verdict, source, paper / "chunks" / "001", prompts


@pytest.mark.parametrize("prior", [True, False])
def test_worker_extracts_source_first_then_independently_verifies(tmp_path, monkeypatch, prior):
    row, fact, verdict, source, folder, prompts = setup(tmp_path, prior)
    calls = []

    def fake(client, prompt, content, schema, name, target):
        calls.append(name)
        if name == "mapping_facts":
            assert "OLD FIELDS FOR EXACT REPAIR" not in content
            return schema(facts=[fact])
        assert "OLD FIELDS FOR EXACT REPAIR" in content
        assert "LITERAL CELL LAYOUTS" in content
        assert "COMPETING TABLE HINTS" in content
        return schema(verdicts=[verdict])

    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())
    monkeypatch.setattr(worker, "call", fake)
    proposals = worker.analyze_chunk(folder, "one", [row], source, prompts, object())
    assert calls == ["mapping_facts", "mapping_verifier"]
    assert proposals[0]["action"] == "propose_count"
    assert proposals[0]["proposed_num_runs"] == 5
    if not prior:
        assert (
            proposals[0]["protocol_binding"]["status"] == "independently_verified_new_method_scope"
        )
    assert (folder / "protocol_reviews.json").exists()


def test_missing_output_is_retried_and_preserved_not_invented_unknown(tmp_path, monkeypatch):
    row, fact, verdict, source, folder, prompts = setup(tmp_path)
    count = 0

    def fake(client, prompt, content, schema, name, target):
        nonlocal count
        if name == "mapping_facts":
            count += 1
            return schema(facts=[] if count == 1 else [fact])
        return schema(verdicts=[verdict])

    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())
    monkeypatch.setattr(worker, "call", fake)
    assert (
        worker.analyze_chunk(folder, "one", [row], source, prompts, object())[0][
            "proposed_num_runs"
        ]
        == 5
    )
    assert (folder / "mapping_facts_attempt_001" / "error.json").exists()
    assert (folder / "mapping_facts_attempt_002" / "output.json").exists()


def test_reuses_facts_only_when_saved_input_fingerprint_matches(tmp_path, monkeypatch):
    row, fact, verdict, source, folder, prompts = setup(tmp_path)
    paper = folder.parent.parent
    (paper / "rows.json").write_text(json.dumps([row]))
    content = worker.extraction_content(paper, source, "one", [row])
    prompt = (prompts / "result_mapping.txt").read_text()
    facts_attempt = folder / "mapping_facts_attempt_000"
    facts_attempt.mkdir(parents=True)
    (facts_attempt / "output.json").write_text(json.dumps({"facts": [fact.model_dump()]}))
    (folder / "facts.json").write_text(json.dumps({"facts": [fact.model_dump()]}))
    (folder / "facts_cache.json").write_text(
        json.dumps(
            {
                "cache_key": worker.facts_cache_key(prompt, content),
                "fact_attempt": facts_attempt.name,
            }
        )
    )
    calls = []

    def fake(client, prompt, content, schema, name, target):
        calls.append(name)
        assert name == "mapping_verifier"
        return schema(verdicts=[verdict])

    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())
    monkeypatch.setattr(worker, "call", fake)
    proposals = worker.analyze_chunk(folder, "one", [row], source, prompts, object())

    assert calls == ["mapping_verifier"]
    assert proposals[0]["action"] == "propose_count"
    assert json.loads((folder / "facts_cache_use.json").read_text())["reused"] is True


def test_compact_verifier_merges_delta_and_keeps_final_safety_gates(tmp_path, monkeypatch):
    row, fact, verdict, source, folder, prompts = setup(tmp_path)
    calls = []

    def fake(client, prompt, content, schema, name, target):
        calls.append(name)
        if name == "mapping_facts":
            return schema(facts=[fact])
        assert name == "mapping_delta_verifier"
        assert "UNTRUSTED SOURCE-FIRST FACTS" in content
        decision = CompactRowDecision(
            result_id=verdict.result_id,
            verified_candidate_indices=verdict.verified_candidate_indices,
            selected_candidate_index=verdict.selected_candidate_index,
            origin_supported=verdict.origin_supported,
            execution_supported=verdict.execution_supported,
            protocol_supported=verdict.protocol_supported,
            repair_supported=verdict.repair_supported,
            setting_status=verdict.setting_status,
            eligibility=verdict.eligibility,
            presentations=verdict.presentations,
            protocol_scope_review=verdict.protocol_scope_review,
            explanation=verdict.explanation,
        )
        return schema(
            reviewed_result_ids=[row["result_id"]],
            fact_patches=[],
            repair_patches=[],
            candidate_patches=[],
            candidate_additions=[],
            decisions=[decision],
        )

    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())
    monkeypatch.setattr(worker, "call", fake)
    proposals = worker.analyze_chunk(
        folder, "one", [row], source, prompts, object(), compact_verifier=True
    )

    assert calls == ["mapping_facts", "mapping_delta_verifier"]
    assert proposals[0]["action"] == "propose_count"
    assert proposals[0]["proposed_num_runs"] == 5
    assert (folder / "delta_verification.json").exists()
    assert (folder / "verification.json").exists()


def test_feedback_round_preserves_candidate_additions(tmp_path, monkeypatch):
    row, fact, verdict, source, folder, prompts = setup(tmp_path)
    source += (
        r"\begin{table}" + "\n"
        "Method & Cora \\\\\n"
        "Own & 80.0 $\\pm$ 0.2 \\\\\n"
        r"\end{table}" + "\n"
    )
    candidate = MappingCandidate.model_validate(
        fact.candidates[0].model_dump()
        | {
            "table_id": 2,
            "row_evidence": {"start_line": 8, "end_line": 8},
            "column_evidence": {"start_line": 7, "end_line": 7},
            "cell_evidence": {"start_line": 8, "end_line": 8},
            "identity_evidence": [{"start_line": 7, "end_line": 7}],
        }
    )
    second_presentation = PresentationReview(
        table_id=2,
        decision="same_experiment",
        evidence=[{"start_line": 8, "end_line": 8}],
        explanation="A duplicate same-experiment presentation.",
    )
    calls = []

    def decision(indices):
        presentations = [*verdict.presentations, second_presentation]
        return CompactRowDecision(
            result_id=verdict.result_id,
            verified_candidate_indices=indices,
            selected_candidate_index=0,
            origin_supported=verdict.origin_supported,
            execution_supported=verdict.execution_supported,
            protocol_supported=verdict.protocol_supported,
            repair_supported=verdict.repair_supported,
            setting_status=verdict.setting_status,
            eligibility=verdict.eligibility,
            presentations=presentations,
            protocol_scope_review=verdict.protocol_scope_review,
            explanation=verdict.explanation,
        )

    def fake(client, prompt, content, schema, name, target):
        if name == "mapping_facts":
            return schema(facts=[fact])
        calls.append(content)
        additions = [
            CompactCandidateAddition(
                result_id=row["result_id"],
                candidate=candidate,
                reason="The source has another same-experiment table presentation.",
            )
        ]
        if len(calls) == 1:
            return schema(
                reviewed_result_ids=[row["result_id"]],
                fact_patches=[],
                repair_patches=[],
                candidate_patches=[],
                candidate_additions=additions,
                decisions=[decision([0])],
            )
        assert "PREVIOUS COMPACT VERIFIER OUTPUT" in content
        assert '"candidate_additions"' in content
        return schema(
            reviewed_result_ids=[row["result_id"]],
            fact_patches=[],
            repair_patches=[],
            candidate_patches=[],
            candidate_additions=additions,
            decisions=[decision([0, 1])],
        )

    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())
    monkeypatch.setattr(worker, "call", fake)
    proposals = worker.analyze_chunk(
        folder, "one", [row], source, prompts, object(), compact_verifier=True
    )

    assert len(calls) == 2
    assert proposals[0]["action"] == "propose_count"
    assert proposals[0]["proposed_num_runs"] == 5


def test_terminal_failed_call_remains_failure(tmp_path, monkeypatch):
    row, _, _, source, folder, prompts = setup(tmp_path)
    monkeypatch.setattr(worker, "mapping_client", lambda gate, model=None: object())

    def fail(*args):
        raise TimeoutError("Timed out")

    monkeypatch.setattr(worker, "call", fail)
    with pytest.raises(ValueError, match="failed three"):
        worker.analyze_chunk(folder, "one", [row], source, prompts, object())
    assert len(list(folder.glob("mapping_facts_attempt_*/error.json"))) == 3
    assert not (folder / "proposals.json").exists()
