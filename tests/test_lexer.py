"""Tests for the Lox lexer."""

import pytest
from src.lox.lexer import Lexer
from src.lox.token import TokenType


def test_single_character_tokens():
    """Test scanning single character tokens."""
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
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type


def test_two_character_tokens():
    """Test scanning two character tokens."""
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
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type


def test_string_literals():
    """Test scanning string literals."""
    source = '"hello world"'
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    
    assert len(tokens) == 2  # STRING + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].literal == "hello world"


def test_number_literals():
    """Test scanning number literals."""
    source = "123 456.789"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    
    assert len(tokens) == 3  # NUMBER + NUMBER + EOF
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].literal == 123.0
    assert tokens[1].type == TokenType.NUMBER
    assert tokens[1].literal == 456.789


def test_keywords():
    """Test scanning keywords."""
    source = "and class else false for fun if nil or print return super this true var while"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    
    expected_types = [
        TokenType.AND,
        TokenType.CLASS,
        TokenType.ELSE,
        TokenType.FALSE,
        TokenType.FOR,
        TokenType.FUN,
        TokenType.IF,
        TokenType.NIL,
        TokenType.OR,
        TokenType.PRINT,
        TokenType.RETURN,
        TokenType.SUPER,
        TokenType.THIS,
        TokenType.TRUE,
        TokenType.VAR,
        TokenType.WHILE,
        TokenType.EOF,
    ]
    
    assert len(tokens) == len(expected_types)
    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type


def test_identifiers():
    """Test scanning identifiers."""
    source = "variable_name another_var"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    
    assert len(tokens) == 3  # IDENTIFIER + IDENTIFIER + EOF
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[0].lexeme == "variable_name"
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].lexeme == "another_var"
