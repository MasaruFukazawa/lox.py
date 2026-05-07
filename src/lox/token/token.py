"""
Token definitions for the Lox language.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict

from .type import TokenType


class Token(BaseModel):
    """
    A token in the Lox language.

    Attributes:
        token_type: The type of the token.
        lexeme: The lexeme of the token.
        literal: The literal value of the token.
        line: The line number of the token.
    """

    model_config = ConfigDict(frozen=True)

    token_type: TokenType
    lexeme: str
    literal: Any
    line: int

    def __str__(self) -> str:
        return f"{self.token_type} {self.lexeme} {self.literal}"
