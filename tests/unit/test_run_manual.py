from types import SimpleNamespace

from scripts.run_manual import _print_parse_summary


def test_print_parse_summary_reports_existing_updates(capsys):
    summary = SimpleNamespace(
        quarantined=False,
        new_results=0,
        updated_results=8,
        skipped_unknown_datasets=[],
        skipped_invalid_values=[],
        quarantine_model_names=[],
        quarantine_reasons=[],
    )

    _print_parse_summary(summary)

    captured = capsys.readouterr().out
    assert "0" in captured
    assert "existing result row(s) updated" in captured
    assert "Parsed 8 extracted row(s): 0 new, 8 updated." in captured
