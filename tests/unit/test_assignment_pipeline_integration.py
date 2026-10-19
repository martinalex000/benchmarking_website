import json

from experiments.table_provenance_experiment import run_mapping_batch as batch
from tests.unit.test_assignment_protocol_refresh import reviewed_fixture
from tests.unit.test_mapping_protocol_binding import key


def test_generalized_chunk_runs_source_first_then_verifies_and_gates(tmp_path, monkeypatch):
    row, verdict, source, _ = reviewed_fixture()
    row.update(variant="", num_runs=None)
    verdict.presentations = [
        batch.PresentationReview(
            table_id=1,
            decision="same_experiment",
            evidence=[batch.Span(start_line=3, end_line=3)],
            explanation="This is the selected main benchmark cell",
        )
    ]
    source = source.replace("10-fold CV for tuning, repeated 10 times", "5 runs")
    folder = tmp_path / "papers" / "one" / "chunks" / "001"
    folder.mkdir(parents=True)
    paper = folder.parent.parent
    for name, data in (("protocol_keys.json", [key(repetitions=5)]), ("earlier_matches.json", [])):
        (paper / name).write_text(json.dumps(data))
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "generalized_assignment_checks": True,
                "targeted_fixes": True,
                "identity_guard_v4": True,
                "source_first_identity": True,
            }
        )
    )
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    for name in ("result_mapping_cv_v3.txt", "result_mapping_cv_v3_verifier.txt"):
        (prompts / name).write_text("Test prompt")
    calls = []

    def fake_call(client, prompt, content, schema, name, attempt):
        calls.append(name)
        if name == "mapping_facts":
            assert "OLD FIELDS FOR EXACT REPAIR" not in content
            return schema.model_validate({"facts": [verdict.corrected_fact.model_dump()]})
        assert "OLD FIELDS FOR EXACT REPAIR" in content
        assert "LITERAL SOURCE CELL LAYOUTS" in content
        return schema.model_validate({"verdicts": [verdict.model_dump()]})

    monkeypatch.setattr(batch, "client_for", lambda gate: object())
    monkeypatch.setattr(batch, "call", fake_call)
    proposals = batch.analyze_chunk(folder, "one", [row], source, prompts, object())
    assert calls == ["mapping_facts", "mapping_verifier"]
    assert proposals[0]["action"] == "propose_count"
    assert proposals[0]["proposed_num_runs"] == 5
    assert (folder / "verification_attempt_1/raw_verdicts.json").exists()
    assert (folder / "verification_attempt_1/adapted_verdicts.json").exists()
