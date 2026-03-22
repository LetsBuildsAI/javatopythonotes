"""for loops — Java: for (int i = 0; i < n; i++), for (T x : list), etc."""

from typing import Dict, List


def sum_range_0_until(n: int) -> int:
    """0 + 1 + ... + (n - 1). Java: for (int i = 0; i < n; i++)."""
    total = 0
    for i in range(n):
        total += i
    return total


def squares(values: List[int]) -> List[int]:
    """Java enhanced for: for (int x : values)."""
    out: List[int] = []
    for x in values:
        out.append(x * x)
    return out


def indexed_words(words: List[str]) -> List[str]:
    """Java-style index + value: use enumerate."""
    lines: List[str] = []
    for index, word in enumerate(words):
        lines.append(f"{index}: {word}")
    return lines


def char_counts(word: str) -> Dict[str, int]:
    """Iterate a string character by character."""
    counts: Dict[str, int] = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    return counts
