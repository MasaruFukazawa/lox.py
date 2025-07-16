"""Lexical analyzer for the Lox language."""

from typing import Any

from .token import Token, TokenType


class Lexer:
    """Lexical analyzer that converts source code into tokens."""

    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens: list[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1

        self.keywords = {
            "and": TokenType.AND,
            "class": TokenType.CLASS,
            "else": TokenType.ELSE,
            "false": TokenType.FALSE,
            "for": TokenType.FOR,
            "fun": TokenType.FUN,
            "if": TokenType.IF,
            "nil": TokenType.NIL,
            "or": TokenType.OR,
            "print": TokenType.PRINT,
            "return": TokenType.RETURN,
            "super": TokenType.SUPER,
            "this": TokenType.THIS,
            "true": TokenType.TRUE,
            "var": TokenType.VAR,
            "while": TokenType.WHILE,
        }

    def scan_tokens(self) -> list[Token]:
        """Scan the source code and return a list of tokens."""
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(
            type=TokenType.EOF,
            lexeme="",
            literal=None,
            line=self.line
        ))
        return self.tokens

    def is_at_end(self) -> bool:
        """Check if we've reached the end of the source code."""
        return self.current >= len(self.source)

    def scan_token(self) -> None:
        """Scan a single token."""
        c = self.advance()

        match c:
            case "(":
                self.add_token(TokenType.LEFT_PAREN)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.add_token(TokenType.LEFT_BRACE)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "-":
                self.add_token(TokenType.MINUS)
            case "+":
                self.add_token(TokenType.PLUS)
            case ";":
                self.add_token(TokenType.SEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case "!":
                self.add_token(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
            case "=":
                self.add_token(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
            case "<":
                self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
            case ">":
                self.add_token(TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER)
            case "/":
                if self.match("/"):
                    while self.peek() != "\n" and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case " " | "\r" | "\t":
                pass
            case "\n":
                self.line += 1
            case '"':
                self.string()
            case _:
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()

    def advance(self) -> str:
        """Consume and return the current character."""
        self.current += 1
        return self.source[self.current - 1]

    def match(self, expected: str) -> bool:
        """Check if the current character matches the expected character."""
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self) -> str:
        """Return the current character without consuming it."""
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self) -> str:
        """Return the next character without consuming it."""
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def string(self) -> None:
        """Parse a string literal."""
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_at_end():
            return

        self.advance()

        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def number(self) -> None:
        """Parse a number literal."""
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def identifier(self) -> None:
        """Parse an identifier or keyword."""
        while self.is_alphanumeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        token_type = self.keywords.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    def is_digit(self, c: str) -> bool:
        """Check if a character is a digit."""
        return c >= "0" and c <= "9"

    def is_alpha(self, c: str) -> bool:
        """Check if a character is alphabetic."""
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or c == "_"

    def is_alphanumeric(self, c: str) -> bool:
        """Check if a character is alphanumeric."""
        return self.is_alpha(c) or self.is_digit(c)

    def add_token(self, token_type: TokenType, literal: Any = None) -> None:
        """Add a token to the tokens list."""
        text = self.source[self.start:self.current]
        self.tokens.append(Token(
            type=token_type,
            lexeme=text,
            literal=literal,
            line=self.line
        ))
