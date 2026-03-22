"""while loops — Java: while (cond) { } with break / continue."""

from typing import List


def countdown_lines(start: int) -> List[str]:
    lines: List[str] = []
    n = start
    while n > 0:
        lines.append(str(n))
        n -= 1
    lines.append("go")
    return lines


def first_index_of(haystack: List[int], needle: int) -> int:
    """Return index or -1 if missing — linear search with while."""
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return i
        i += 1
    return -1


def sum_until_limit(step: int, limit: int) -> int:
    """Demonstrate break when a condition inside the loop is met."""
    total = 0
    n = 0
    while True:
        n += step
        if n > limit:
            break
        total += n
    return total


def skip_multiples_of_three(up_to: int) -> List[int]:
    """Demonstrate continue — Java: continue;"""
    out: List[int] = []
    n = 0
    while n < up_to:
        n += 1
        if n % 3 == 0:
            continue
        out.append(n)
    return out
