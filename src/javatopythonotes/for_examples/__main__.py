"""Run: python -m javatopythonotes.for_examples"""

from javatopythonotes.for_examples import char_counts, indexed_words, squares, sum_range_0_until


def main() -> None:
    print("sum_range_0_until(5) ->", sum_range_0_until(5))
    print("squares([1,2,3]) ->", squares([1, 2, 3]))
    print("indexed_words ->", indexed_words(["a", "b"]))
    print("char_counts('aba') ->", char_counts("aba"))


if __name__ == "__main__":
    main()
