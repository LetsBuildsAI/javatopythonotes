from javatopythonotes.imports_examples import round_trip_number


def test_imports_round_trip() -> None:
    assert round_trip_number(11) == 11
