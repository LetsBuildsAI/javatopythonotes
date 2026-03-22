"""File IO with pathlib and context managers (Java: try-with-resources, Path API)."""

from pathlib import Path
from typing import List


def write_and_read_lines(tmp_dir: Path, name: str, lines: List[str]) -> List[str]:
    path = tmp_dir / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(line + "\n")
    with path.open("r", encoding="utf-8") as handle:
        return [ln.rstrip("\n") for ln in handle.readlines()]


def demo_summary(base: Path) -> str:
    read_back = write_and_read_lines(base, "sample_file_io.txt", ["alpha", "beta"])
    return f"wrote sample -> {read_back}"
