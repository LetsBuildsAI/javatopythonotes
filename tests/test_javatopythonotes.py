"""Tests mirror JUnit-style folders: keep behavior checks next to the code you learn."""

from javatopythonotes import __version__


def test_version_is_set() -> None:
    assert __version__ == "0.1.0"
