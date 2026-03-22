"""Run: python -m javatopythonotes.file_io_examples"""

import tempfile
from pathlib import Path

from javatopythonotes.file_io_examples import demo_summary


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        print(demo_summary(Path(tmp)))


if __name__ == "__main__":
    main()
