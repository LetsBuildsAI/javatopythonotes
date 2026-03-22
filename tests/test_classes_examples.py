from javatopythonotes.classes_examples import Counter, Point


def test_classes() -> None:
    assert Counter(1).inc(2) == 3
    assert Point(3, 4).distance_squared() == 25
