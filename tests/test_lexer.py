"""Tests for the Lox lexer."""

from src.lox.lexer import Lexer


def test_lexer_basic():
    """Test basic lexer functionality."""
    source = "test"
    lexer = Lexer(source)
    assert lexer.source == "test"
