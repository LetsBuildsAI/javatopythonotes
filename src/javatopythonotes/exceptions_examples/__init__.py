"""try / except / else / finally and custom exceptions."""

from typing import Dict


class NotFoundError(Exception):
    """Domain-specific error — like a small checked-style type in Java."""

    pass


def parse_positive_int(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(f"not an int: {raw!r}") from exc
    else:
        if value <= 0:
            raise ValueError("must be positive")
        return value


def lookup_user(users: Dict[str, str], user_id: str) -> str:
    try:
        return users[user_id]
    except KeyError:
        raise NotFoundError(user_id) from None


def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")


def demo_summary() -> str:
    parts = [str(parse_positive_int("7")), str(safe_divide(1.0, 0.0))]
    try:
        lookup_user({"1": "ada"}, "9")
    except NotFoundError as exc:
        parts.append(f"missing={exc.args[0]}")
    return " | ".join(parts)
