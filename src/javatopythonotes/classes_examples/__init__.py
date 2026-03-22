"""Classes, dunder methods, and @dataclass (Java: POJO / record-like DTOs)."""

from dataclasses import dataclass
from typing import Any


class Counter:
    """Minimal mutable object with behavior."""

    def __init__(self, start: int = 0) -> None:
        self.value = start

    def inc(self, step: int = 1) -> int:
        self.value += step
        return self.value

    def __repr__(self) -> str:
        return f"Counter({self.value})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Counter):
            return NotImplemented
        return self.value == other.value


@dataclass(frozen=True)
class Point:
    """Immutable data holder — similar spirit to Java record."""

    x: int
    y: int

    def distance_squared(self) -> int:
        return self.x * self.x + self.y * self.y


def demo_summary() -> str:
    c = Counter(2)
    c.inc(3)
    p = Point(3, 4)
    return f"{c!r} eq={Counter(5) == Counter(5)} point={p} d2={p.distance_squared()}"
