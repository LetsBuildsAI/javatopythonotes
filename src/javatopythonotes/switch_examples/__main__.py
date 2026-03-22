"""Run: python -m javatopythonotes.switch_examples"""

from javatopythonotes.switch_examples import command_action, http_status_category, weekday_type


def main() -> None:
    print(http_status_category(200), http_status_category(404), http_status_category(418))
    print(command_action("START"), command_action("  pause "), command_action("nope"))
    print(weekday_type("Monday"), weekday_type("SATURDAY"))


if __name__ == "__main__":
    main()
