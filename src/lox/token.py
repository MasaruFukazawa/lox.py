"""Token definitions for the Lox language."""

from enum import Enum, auto
from typing import Any
from pydantic import BaseModel


class TokenType(Enum):
    """Token types for the Lox language."""
    pass


class Token(BaseModel):
    """A token in the Lox language."""
    pass
