from javatopythonotes.for_examples import char_counts, indexed_words, squares, sum_range_0_until
from javatopythonotes.if_examples import describe_sign, greeting_for, max_of_two
from javatopythonotes.switch_examples import command_action, http_status_category, weekday_type
from javatopythonotes.while_examples import (
    countdown_lines,
    first_index_of,
    skip_multiples_of_three,
    sum_until_limit,
)


def test_if_examples() -> None:
    assert describe_sign(-1) == "negative"
    assert describe_sign(0) == "zero"
    assert describe_sign(3) == "positive"
    assert max_of_two(3, 5) == 5
    assert greeting_for(None) == "Hello, stranger"
    assert greeting_for("Ada") == "Hello, Ada"


def test_for_examples() -> None:
    assert sum_range_0_until(5) == 10
    assert squares([2, 3]) == [4, 9]
    assert indexed_words(["x"]) == ["0: x"]
    assert char_counts("aba") == {"a": 2, "b": 1}


def test_while_examples() -> None:
    assert countdown_lines(2) == ["2", "1", "go"]
    assert first_index_of([9, 8, 7], 8) == 1
    assert first_index_of([], 1) == -1
    assert sum_until_limit(5, 12) == 5 + 10
    assert skip_multiples_of_three(5) == [1, 2, 4, 5]


def test_switch_style_examples() -> None:
    assert http_status_category(200) == "ok"
    assert http_status_category(999) == "other"
    assert command_action("STOP") == "stopping"
    assert weekday_type("sunday") == "weekend"
    assert weekday_type("Tuesday") == "weekday"
