"""
Scanner for the Lox language.
"""

from typing import Any

from pydantic import BaseModel, Field, validate_call

from lox.scanner.exceptions import ScannerError
from lox.token.token import Token
from lox.token.type import TokenType


class Scanner(BaseModel):
    """
    A scanner for the Lox language.
    """

    source: str = Field(default="")
    tokens: list[Token] = Field(default_factory=list)
    start: int = Field(default=0)
    current: int = Field(default=0)
    line: int = Field(default=1)

    @validate_call
    def __init__(self, source: str) -> None:
        """
        Initialize the scanner.
        """
        super().__init__(source=source)

    def is_at_end(self) -> bool:
        """
        Check if the scanner is at the end of the source code.
        """
        return self.current >= len(self.source)

    def advance(self) -> str:
        """
        Advance the scanner to the next character.
        """
        self.current += 1
        return self.source[self.current - 1]

    def error(self, message: str) -> None:
        """
        Print an error message.
        """
        raise ScannerError(message)

    def scan_token(self) -> None:
        """
        Scan a token from the source code.
        """
        c: str = self.advance()

        match c:
            case "(":
                self.add_token(TokenType.LEFT_PAREN, None)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN, None)
            case "{":
                self.add_token(TokenType.LEFT_BRACE, None)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE, None)
            case ",":
                self.add_token(TokenType.COMMA, None)
            case ".":
                self.add_token(TokenType.DOT, None)
            case "-":
                self.add_token(TokenType.MINUS, None)
            case "+":
                self.add_token(TokenType.PLUS, None)
            case ";":
                self.add_token(TokenType.SEMICOLON, None)
            case "*":
                self.add_token(TokenType.STAR, None)
            case " " | "\t" | "\r" | "\n":
                pass
            case _:
                self.error(f"line {self.line}: Unexpected character: {c}")

        return None

    def scan_tokens(self) -> list[Token]:
        """
        Scan the tokens from the source code.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.add_token(TokenType.EOF, None)

        return self.tokens

    @validate_call
    def add_token(self, token_type: TokenType, literal: Any) -> None:
        """
        Add a token to the list of tokens.
        """
        self.tokens.append(
            Token(
                token_type=token_type,
                lexeme=self.source[self.start : self.current],
                literal=literal,
                line=self.line,
            )
        )
