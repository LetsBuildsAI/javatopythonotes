from javatopythonotes.functions_advanced_examples import greet, keyword_only_sink, make_multiplier


def test_functions_advanced() -> None:
    assert greet("Ms.", "Lee") == "Ms. Lee"
    assert make_multiplier(3)(4) == 12
    assert keyword_only_sink("x", must_be_named="y") == "x:y"
