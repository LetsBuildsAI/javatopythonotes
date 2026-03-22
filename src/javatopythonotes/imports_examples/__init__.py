"""Import styles — Java: import pkg.Type vs import static."""

import json as json_lib
from math import sqrt


def round_trip_number(n: int) -> int:
    """Uses ``import json as`` and ``from math import``."""
    text = json_lib.dumps({"n": n})
    data = json_lib.loads(text)
    root = int(sqrt(float(data["n"] ** 2)))
    return root


def demo_summary() -> str:
    return f"round_trip(5)={round_trip_number(5)}"
