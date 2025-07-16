"""Main entry point for the Lox interpreter."""

import sys

from .lexer import Lexer


def main() -> None:
    """Main function for the Lox interpreter."""
    if len(sys.argv) > 2:
        print("Usage: lox [script]")
        sys.exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


def run_file(path: str) -> None:
    """Run a Lox script from a file."""
    try:
        with open(path, encoding="utf-8") as file:
            source = file.read()
        run(source)
    except FileNotFoundError:
        print(f"Error: Could not find file '{path}'")
        sys.exit(66)
    except Exception as e:
        print(f"Error reading file '{path}': {e}")
        sys.exit(66)


def run_prompt() -> None:
    """Run the Lox REPL."""
    print("Lox interpreter v0.1.0")
    print("Type 'exit' to quit.")

    while True:
        try:
            line = input("> ")
            if line.strip().lower() == "exit":
                break
            run(line)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


def run(source: str) -> None:
    """Run Lox source code."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
