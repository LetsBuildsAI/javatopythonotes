"""Context managers: class-based and contextlib (Java: AutoCloseable)."""

from contextlib import contextmanager
from typing import Iterator, List


class CollectingBuffer:
    """__enter__ / __exit__ — runs cleanup even if the block raises."""

    def __init__(self) -> None:
        self.lines: List[str] = []

    def __enter__(self) -> "CollectingBuffer":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.lines.append("closed")

    def add(self, text: str) -> None:
        self.lines.append(text)


@contextmanager
def append_marker(lines: List[str], marker: str) -> Iterator[None]:
    """Functional context manager: log enter/exit around a block."""
    lines.append(f"enter:{marker}")
    try:
        yield
    finally:
        lines.append(f"exit:{marker}")


def demo_summary() -> str:
    with CollectingBuffer() as buf:
        buf.add("a")
        buf.add("b")
    log: List[str] = []
    with append_marker(log, "job"):
        log.append("work")
    return f"buffer={buf.lines} log={log}"
