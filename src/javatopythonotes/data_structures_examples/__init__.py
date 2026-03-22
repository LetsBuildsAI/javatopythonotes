"""Lists, tuples, dicts, sets, comprehensions, unpacking (Java: collections + streams-style habits)."""

from typing import Dict, List, Set, Tuple


def list_and_tuple_basics() -> Tuple[List[int], Tuple[int, ...]]:
    nums: List[int] = [1, 2, 3]
    nums.append(4)
    point: Tuple[int, int] = (10, 20)
    return nums, point


def dict_and_set_basics() -> Tuple[Dict[str, int], Set[int]]:
    counts: Dict[str, int] = {"a": 1, "b": 2}
    counts["c"] = counts.get("missing", 0) + 1
    unique: Set[int] = {1, 2, 2, 3}
    return counts, unique


def comprehension_examples() -> Tuple[List[int], Dict[str, int]]:
    squares: List[int] = [n * n for n in range(5)]
    lengths: Dict[str, int] = {word: len(word) for word in ("aa", "bbb")}
    return squares, lengths


def unpacking_examples() -> Tuple[int, int, List[int]]:
    first, second = (1, 2)
    head, *rest = [10, 20, 30, 40]
    return first, second, [head] + rest


def demo_summary() -> str:
    lst, tup = list_and_tuple_basics()
    d, s = dict_and_set_basics()
    sq, lens = comprehension_examples()
    a, b, spread = unpacking_examples()
    return (
        f"list={lst} tuple={tup} dict={d} set={sorted(s)} "
        f"squares={sq} lens={lens} unpack=({a},{b},{spread})"
    )
