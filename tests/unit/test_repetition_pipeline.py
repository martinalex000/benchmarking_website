from argparse import Namespace

from backend import pipeline, repetition_batch


def test_repetition_preflight_failure_propagates_to_pipeline(monkeypatch, tmp_path):
    monkeypatch.setattr(
        repetition_batch,
        "run_batch",
        lambda *_args, **_kwargs: {
            "state": "preflight_failed",
            "completed": 0,
            "total": 5,
            "categories": {},
            "preflight_error": "endpoint unavailable",
        },
    )

    assert pipeline.stage_repetitions(Namespace(output_dir=str(tmp_path))) is False
