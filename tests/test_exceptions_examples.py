import pytest

from javatopythonotes.exceptions_examples import NotFoundError, lookup_user, parse_positive_int


def test_exceptions() -> None:
    assert parse_positive_int("5") == 5
    with pytest.raises(ValueError):
        parse_positive_int("nope")
    with pytest.raises(ValueError):
        parse_positive_int("0")
    with pytest.raises(NotFoundError):
        lookup_user({}, "missing")
