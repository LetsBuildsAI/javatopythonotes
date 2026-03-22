from javatopythonotes.generators_examples import count_up_to, first_n_squares


def test_generators() -> None:
    assert list(count_up_to(3)) == [1, 2, 3]
    assert first_n_squares(3) == [1, 4, 9]
