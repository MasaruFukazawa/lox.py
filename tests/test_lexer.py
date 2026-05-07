"""Tests for the Lox lexer."""

from lox.lexer import Lexer


def test_lexer_basic() -> None:
    """Test basic lexer functionality."""
    source = "test"
    lexer = Lexer(source)
    assert lexer.source == "test"
