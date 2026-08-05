import argparse

import pytest

from scripts.review_protocol_papers import _parse_paper_target


def test_parse_paper_target():
    assert _parse_paper_target("1910.11436=MNIST") == ("1910.11436", "MNIST")


@pytest.mark.parametrize("value", ["1910.11436", "=MNIST", "1910.11436="])
def test_parse_paper_target_rejects_incomplete_value(value):
    with pytest.raises(argparse.ArgumentTypeError):
        _parse_paper_target(value)
