"""Tests for the Lox lexer."""

from src.lox.lexer import Lexer
from src.lox.token import TokenType


def test_lexer_basic():
    """Test basic lexer functionality."""
    source = "test"
    lexer = Lexer(source)
    assert lexer.source == "test"


def test_lexer_single_character_tokens():
    """Test lexing of single character tokens."""
    source = "(){},.-+;*"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    expected_types = [
        TokenType.LEFT_PAREN,
        TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE,
        TokenType.RIGHT_BRACE,
        TokenType.COMMA,
        TokenType.DOT,
        TokenType.MINUS,
        TokenType.PLUS,
        TokenType.SEMICOLON,
        TokenType.STAR,
        TokenType.EOF,
    ]

    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types, strict=False):
        assert token.type == expected_type


def test_lexer_two_character_tokens():
    """Test lexing of two character tokens."""
    source = "!= == <= >="
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    expected_types = [
        TokenType.BANG_EQUAL,
        TokenType.EQUAL_EQUAL,
        TokenType.LESS_EQUAL,
        TokenType.GREATER_EQUAL,
        TokenType.EOF,
    ]

    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types, strict=False):
        assert token.type == expected_type


def test_lexer_string_literals():
    """Test lexing of string literals."""
    source = '"Hello, World!"'
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    assert len(tokens) == 2  # STRING + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].literal == "Hello, World!"
    assert tokens[0].lexeme == '"Hello, World!"'


def test_lexer_number_literals():
    """Test lexing of number literals."""
    source = "123 45.67"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    assert len(tokens) == 3  # NUMBER + NUMBER + EOF
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].literal == 123.0
    assert tokens[1].type == TokenType.NUMBER
    assert tokens[1].literal == 45.67


def test_lexer_identifiers_and_keywords():
    """Test lexing of identifiers and keywords."""
    source = "var myVariable = true;"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    expected_types = [
        TokenType.VAR,
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.TRUE,
        TokenType.SEMICOLON,
        TokenType.EOF,
    ]

    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types, strict=False):
        assert token.type == expected_type

    assert tokens[1].lexeme == "myVariable"


def test_lexer_comments():
    """Test that comments are ignored."""
    source = "var x = 5; // This is a comment\nvar y = 10;"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    expected_types = [
        TokenType.VAR,
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.NUMBER,
        TokenType.SEMICOLON,
        TokenType.VAR,
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.NUMBER,
        TokenType.SEMICOLON,
        TokenType.EOF,
    ]

    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types, strict=False):
        assert token.type == expected_type


def test_lexer_line_numbers():
    """Test that line numbers are tracked correctly."""
    source = "var x = 1;\nvar y = 2;"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    assert tokens[0].line == 1  # var
    assert tokens[1].line == 1  # x
    assert tokens[5].line == 2  # var (second line)
    assert tokens[6].line == 2  # y
