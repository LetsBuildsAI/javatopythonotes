from javatopythonotes.context_manager_examples import CollectingBuffer, append_marker


def test_context_managers() -> None:
    with CollectingBuffer() as buf:
        buf.add("z")
    assert buf.lines == ["z", "closed"]
    log: list = []
    with append_marker(log, "m"):
        log.append("mid")
    assert log == ["enter:m", "mid", "exit:m"]
