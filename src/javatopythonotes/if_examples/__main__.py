"""Run: python -m javatopythonotes.if_examples"""

from javatopythonotes.if_examples import describe_sign, greeting_for, max_of_two


def main() -> None:
    print(describe_sign(-3), describe_sign(0), describe_sign(7))
    print(max_of_two(10, 4))
    print(greeting_for(None), greeting_for(""), greeting_for("Ada"))


if __name__ == "__main__":
    main()
