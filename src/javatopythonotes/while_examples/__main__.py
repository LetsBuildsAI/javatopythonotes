"""Run: python -m javatopythonotes.while_examples"""

from javatopythonotes.while_examples import (
    countdown_lines,
    first_index_of,
    skip_multiples_of_three,
    sum_until_limit,
)


def main() -> None:
    print("countdown_lines(3) ->", countdown_lines(3))
    print("first_index_of([1,2,3], 2) ->", first_index_of([1, 2, 3], 2))
    print("sum_until_limit(4, 20) ->", sum_until_limit(4, 20))
    print("skip_multiples_of_three(8) ->", skip_multiples_of_three(8))


if __name__ == "__main__":
    main()
