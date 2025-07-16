"""Tests for the Lox token module."""

from src.lox.token import Token, TokenType


def test_token_creation():
    """Test creating a token."""
    token = Token(
        type=TokenType.IDENTIFIER,
        lexeme="variable",
        literal=None,
        line=1
    )

    assert token.type == TokenType.IDENTIFIER
    assert token.lexeme == "variable"
    assert token.literal is None
    assert token.line == 1


def test_token_with_literal():
    """Test creating a token with a literal value."""
    token = Token(
        type=TokenType.STRING,
        lexeme='"hello"',
        literal="hello",
        line=1
    )

    assert token.type == TokenType.STRING
    assert token.lexeme == '"hello"'
    assert token.literal == "hello"
    assert token.line == 1


def test_token_string_representation():
    """Test the string representation of a token."""
    token = Token(
        type=TokenType.NUMBER,
        lexeme="42",
        literal=42.0,
        line=1
    )

    expected = "NUMBER 42 42.0"
    assert str(token) == expected


def test_token_type_enum():
    """Test that TokenType enum has all expected values."""
    expected_tokens = [
        "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE",
        "COMMA", "DOT", "MINUS", "PLUS", "SEMICOLON", "SLASH", "STAR",
        "BANG", "BANG_EQUAL", "EQUAL", "EQUAL_EQUAL",
        "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL",
        "IDENTIFIER", "STRING", "NUMBER",
        "AND", "CLASS", "ELSE", "FALSE", "FUN", "FOR", "IF", "NIL",
        "OR", "PRINT", "RETURN", "SUPER", "THIS", "TRUE", "VAR", "WHILE",
        "EOF"
    ]

    for token_name in expected_tokens:
        assert hasattr(TokenType, token_name)
        assert getattr(TokenType, token_name).value == token_name
