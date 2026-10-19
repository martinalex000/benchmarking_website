from backend.results_parser import _validated_run_metadata


def entry(count, evidence):
    return {
        "num_runs": count,
        "trained_by_paper": True,
        "source_ref": "this paper",
        "num_runs_evidence": evidence,
    }


def test_cv_folds_alone_cannot_be_saved_as_runs():
    assert (
        _validated_run_metadata(entry(10, "We evaluate with 10-fold cross-validation."))[0] is None
    )


def test_repeated_cv_keeps_outer_trials_and_accepts_spelled_number():
    quote = "We repeat 10-fold cross-validation for five trials."
    assert _validated_run_metadata(entry(5, quote))[0] == 5
    assert _validated_run_metadata(entry(50, quote))[0] is None


def test_epoch_number_is_not_run_count():
    assert _validated_run_metadata(entry(100, "We train for 100 epochs."))[0] is None
