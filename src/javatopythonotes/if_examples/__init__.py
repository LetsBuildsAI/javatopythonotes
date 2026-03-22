"""if / elif / else — Java: if (cond) { } else if { } else { }"""

from typing import Optional


def describe_sign(n: int) -> str:
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"


def max_of_two(a: int, b: int) -> int:
    if a >= b:
        return a
    return b


def greeting_for(name: Optional[str]) -> str:
    """None is falsy; empty string is falsy — similar to null / empty checks in Java."""
    if not name:
        return "Hello, stranger"
    return f"Hello, {name}"
