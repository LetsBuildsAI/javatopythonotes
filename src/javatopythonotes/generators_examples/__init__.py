"""Iterators and generators with yield (lazy sequences)."""

from typing import Iterator, List


def count_up_to(limit: int) -> Iterator[int]:
    n = 1
    while n <= limit:
        yield n
        n += 1


def first_n_squares(n: int) -> List[int]:
    gen = (k * k for k in range(1, n + 1))
    return list(gen)


def demo_summary() -> str:
    return f"yielded={list(count_up_to(3))} squares={first_n_squares(4)}"
