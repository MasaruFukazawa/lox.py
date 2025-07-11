"""Lexical analyzer for the Lox language."""


class Lexer:
    """Lexical analyzer that converts source code into tokens."""
    
    def __init__(self, source: str) -> None:
        self.source = source
