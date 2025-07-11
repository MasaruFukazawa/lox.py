"""Main entry point for the Lox interpreter."""

import sys
from pathlib import Path


def main() -> None:
    """Main function for the Lox interpreter."""
    if len(sys.argv) > 2:
        print("Usage: lox [script]", file=sys.stderr)
        sys.exit(64)
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


def run_file(path: str) -> None:
    """Run a Lox script from a file."""
    try:
        source = Path(path).read_text(encoding="utf-8")
        run(source)
    except FileNotFoundError:
        print(f"Error: Could not read file '{path}'", file=sys.stderr)
        sys.exit(66)


def run_prompt() -> None:
    """Run the Lox REPL."""
    print("Lox interpreter REPL")
    print("Type 'exit' to quit")
    
    while True:
        try:
            line = input("> ")
            if line.strip() == "exit":
                break
            run(line)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


def run(source: str) -> None:
    """Run Lox source code."""
    print(f"Running: {source}")


if __name__ == "__main__":
    main()
