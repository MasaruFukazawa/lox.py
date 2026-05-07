"""
Tests for the Scanner class.
"""

import pytest
from pydantic import ValidationError

from lox.scanner.exceptions import ScannerError
from lox.scanner.scanner import Scanner
from lox.token.type import TokenType


class TestScanner:
    """
    Tests for the Scanner class.
    """

    def test_scanner_init_raises(self) -> None:
        """
        Scannerクラス初期例外
        """
        with pytest.raises(ValidationError):
            Scanner("")

    def test_is_at_end_init(self) -> None:
        """ """
        scanner = Scanner("()")
        assert scanner.is_at_end() is False

    def test_is_at_end_boundary_ok(self) -> None:
        """ """
        scanner = Scanner("()")
        scanner.current = 1
        assert scanner.is_at_end() is False

    def test_is_at_end_boundary_error(self) -> None:
        """ """
        scanner = Scanner("()")
        scanner.current = 2
        assert scanner.is_at_end() is True

    def test_is_at_end_past_boundary(self) -> None:
        """ """
        scanner = Scanner("()")
        scanner.current = 5
        assert scanner.is_at_end() is True

    def test_scan_tokens(self) -> None:
        """
        Test that the scanner can scan tokens from the source code.
        """
        scanner = Scanner("(){},.-+;*")
        scanner.scan_tokens()
        assert len(scanner.tokens) == 11
        assert scanner.tokens[0].token_type == TokenType.LEFT_PAREN
        assert scanner.tokens[1].token_type == TokenType.RIGHT_PAREN
        assert scanner.tokens[2].token_type == TokenType.LEFT_BRACE
        assert scanner.tokens[3].token_type == TokenType.RIGHT_BRACE
        assert scanner.tokens[4].token_type == TokenType.COMMA
        assert scanner.tokens[5].token_type == TokenType.DOT
        assert scanner.tokens[6].token_type == TokenType.MINUS
        assert scanner.tokens[7].token_type == TokenType.PLUS
        assert scanner.tokens[8].token_type == TokenType.SEMICOLON
        assert scanner.tokens[9].token_type == TokenType.STAR
        assert scanner.tokens[10].token_type == TokenType.EOF

    def test_scan_tokens_with_error_message(self) -> None:
        """
        Test that the scanner can handle errors.
        """
        scanner = Scanner("a(){},.-+;*")

        with pytest.raises(ScannerError) as excinfo:
            scanner.scan_tokens()

        assert "line 1: Unexpected character: a" in str(excinfo.value)
