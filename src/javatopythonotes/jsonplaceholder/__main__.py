"""Run with: python -m javatopythonotes.jsonplaceholder (requires network)."""

import json

from javatopythonotes.jsonplaceholder import fetch_post


def main() -> None:
    data = fetch_post(1)
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
