"""Defaults, *args / **kwargs, keyword-only parameters, closures."""


def greet(title: str, name: str, excited: bool = False) -> str:
    msg = f"{title} {name}"
    return msg.upper() if excited else msg


def sum_all(*values: int) -> int:
    """*args — like varargs in Java (int... values)."""
    return sum(values)


def build_profile(**fields: str) -> str:
    """**kwargs — like Map<String,String> of named options."""
    parts = [f"{k}={v}" for k, v in sorted(fields.items())]
    return ", ".join(parts)


def keyword_only_sink(prefix: str, *, must_be_named: str) -> str:
    """Everything after * must be passed by name (Python 3)."""
    return f"{prefix}:{must_be_named}"


def make_multiplier(factor: int):
    """Closure: inner function remembers factor from enclosing scope."""

    def scale(n: int) -> int:
        return n * factor

    return scale


def demo_summary() -> str:
    double = make_multiplier(2)
    return " | ".join(
        [
            greet("Ms.", "Lee"),
            greet("Mr.", "Bond", excited=True),
            str(sum_all(1, 2, 3)),
            build_profile(role="admin", city="NYC"),
            keyword_only_sink("id", must_be_named="42"),
            f"closure(5)={double(5)}",
        ]
    )
