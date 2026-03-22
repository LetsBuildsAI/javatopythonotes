from javatopythonotes.file_io_examples import write_and_read_lines


def test_io(tmp_path) -> None:
    assert write_and_read_lines(tmp_path, "t.txt", ["x", "y"]) == ["x", "y"]
