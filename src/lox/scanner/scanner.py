"""
Scanner for the Lox language.
"""

from typing import Annotated, Any, Final

from pydantic import Field, validate_call

from lox.scanner.exceptions import ScannerError
from lox.token.token import Token
from lox.token.type import TokenType


class Scanner:
    """
    A scanner for the Lox language.
    """

    @validate_call
    def __init__(self, source: Annotated[str, Field(min_length=1)]) -> None:
        """
        Initialize the scanner.
        """
        self.source: Final[str] = source
        self.tokens: Final[list[Token]] = []
        self.start: int = 0
        self.current: int = 0
        self.line: int = 1

    def scan_tokens(self) -> list[Token]:
        """
        Scan the tokens from the source code.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.add_token(TokenType.EOF, None)

        return self.tokens

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

    def is_at_end(self) -> bool:
        """
        Check if the scanner is at the end of the source code.
        """
        return self.current >= len(self.source)

    def advance(self) -> str:
        """
        Advance the scanner to the next character.
        """
        c: str = self.source[self.current]
        self.current += 1
        return c

    @validate_call
    def error(self, message: str) -> None:
        """
        Print an error message.
        """
        raise ScannerError(message)
