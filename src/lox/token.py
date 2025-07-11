"""Token definitions for the Lox language."""

from enum import Enum, auto
from typing import Any
from pydantic import BaseModel


class TokenType(Enum):
    """Token types for the Lox language."""
    
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()
    
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()
    
    EOF = auto()


class Token(BaseModel):
    """A token in the Lox language."""
    
    type: TokenType
    lexeme: str
    literal: Any = None
    line: int
    
    def __str__(self) -> str:
        return f"{self.type.name} {self.lexeme} {self.literal}"
