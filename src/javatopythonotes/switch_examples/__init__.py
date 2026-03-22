"""Switch-style branching.

Java `switch` maps most directly to a chain of if/elif/else in Python.
Python 3.10+ also has `match` / `case` (structural pattern matching) — see stdlib docs.
"""


def http_status_category(code: int) -> str:
    if code == 200:
        return "ok"
    elif code == 404:
        return "not_found"
    elif code == 500:
        return "server_error"
    else:
        return "other"


def command_action(cmd: str) -> str:
    """Normalize with .lower() — Java often uses switch on enum or toLowerCase()."""
    key = cmd.strip().lower()
    if key == "start":
        return "starting"
    elif key == "stop":
        return "stopping"
    elif key == "pause":
        return "paused"
    else:
        return "unknown"


def weekday_type(day: str) -> str:
    d = day.strip().lower()
    if d in ("saturday", "sunday"):
        return "weekend"
    elif d in ("monday", "tuesday", "wednesday", "thursday", "friday"):
        return "weekday"
    else:
        return "invalid"
