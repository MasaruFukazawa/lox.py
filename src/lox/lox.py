"""
Main entry point for the Lox interpreter.
"""

import sys


def main() -> None:
    """Main function for the Lox interpreter."""

    if len(sys.argv) > 2:
        print("Usage: lox/lox.py [script]")  # noqa: T201
        sys.exit()
    # elif len(sys.argv) == 2:
    #    runFile(sys.argv[1])
    # else:
    #    runPrompt()


if __name__ == "__main__":
    main()
