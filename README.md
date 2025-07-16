# lox.py

A Python implementation of the Lox programming language from [Crafting Interpreters](https://craftinginterpreters.com/).

## Description

This project is a Python rewrite of the Lox language interpreter, following the design and implementation described in Robert Nystrom's "Crafting Interpreters" book. Lox is a dynamically typed scripting language with C-style syntax.

## Features

Currently implemented:
- ✅ Lexical analysis (tokenization)
- ✅ Token definitions for all Lox language constructs
- ✅ Basic REPL (Read-Eval-Print Loop)
- ✅ File execution support

Planned features:
- 🔄 Parser (syntax analysis)
- 🔄 Abstract Syntax Tree (AST)
- 🔄 Interpreter (evaluation)
- 🔄 Variable declarations and scoping
- 🔄 Functions and closures
- 🔄 Classes and inheritance

## Installation

### Prerequisites
- Python 3.12 or higher
- pip or uv package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/MasaruFukazawa/lox.py.git
cd lox.py
```

2. Install the package in development mode:
```bash
pip install -e ".[dev]"
```

Or using uv:
```bash
uv pip install -e ".[dev]"
```

## Usage

### Running the REPL

```bash
python -m src.lox.main
```

Or using the installed script:
```bash
lox
```

### Running a Lox file

```bash
python -m src.lox.main script.lox
```

Or:
```bash
lox script.lox
```

### Example Lox Code

```lox
// Variables
var greeting = "Hello";
var name = "World";
print greeting + ", " + name + "!";

// Numbers and arithmetic
var a = 10;
var b = 20;
print a + b * 2;

// Booleans and logic
var isTrue = true;
var isFalse = false;
print isTrue and !isFalse;
```

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Code Formatting and Linting

```bash
ruff check src/ tests/
ruff format src/ tests/
```

### Project Structure

```
lox.py/
├── src/lox/           # Main package
│   ├── __init__.py    # Package initialization
│   ├── main.py        # Entry point and REPL
│   ├── token.py       # Token definitions
│   └── lexer.py       # Lexical analyzer
├── tests/             # Test files
├── main.py            # Alternative entry point
├── pyproject.toml     # Project configuration
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass and code is properly formatted
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Robert Nystrom for the excellent "Crafting Interpreters" book
- The original Lox language design and specification
