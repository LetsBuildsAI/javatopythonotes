from javatopythonotes.data_structures_examples import comprehension_examples, unpacking_examples


def test_data_structures() -> None:
    sq, lens = comprehension_examples()
    assert sq == [0, 1, 4, 9, 16]
    assert lens == {"aa": 2, "bbb": 3}
    a, b, spread = unpacking_examples()
    assert (a, b, spread) == (1, 2, [10, 20, 30, 40])
