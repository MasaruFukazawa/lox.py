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
        """空文字列を渡すと min_length=1 制約で ValidationError が飛ぶこと。"""
        with pytest.raises(ValidationError):
            Scanner("")

    def test_scan_tokens(self) -> None:
        """単一文字トークンを順序通りにスキャンし、末尾に EOF を付与すること。"""
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
        """未知の文字に遭遇したとき、行番号付きの ScannerError を送出すること。"""
        scanner = Scanner("a(){},.-+;*")

        with pytest.raises(ScannerError) as excinfo:
            scanner.scan_tokens()

        assert "line 1: Unexpected character: a" in str(excinfo.value)

    def test_is_at_end_init(self) -> None:
        """初期状態 (current=0) では終端ではないこと。"""
        scanner = Scanner("()")
        assert scanner.is_at_end() is False

    def test_is_at_end_boundary_ok(self) -> None:
        """終端の1つ手前 (current < len) ではまだ終端ではないこと。"""
        scanner = Scanner("()")
        scanner.current = 1
        assert scanner.is_at_end() is False

    def test_is_at_end_boundary_error(self) -> None:
        """current が len(source) に達した時点で終端と判定されること。"""
        scanner = Scanner("()")
        scanner.current = 2
        assert scanner.is_at_end() is True

    def test_is_at_end_past_boundary(self) -> None:
        """current が len(source) を超えていても終端と判定されること。"""
        scanner = Scanner("()")
        scanner.current = 5
        assert scanner.is_at_end() is True

    def test_advance_ok(self) -> None:
        """current ポインタの位置の文字を返し、ポインタを一文字分進める。"""
        scanner = Scanner("()")

        assert scanner.advance() == "("
        assert scanner.current == 1

        assert scanner.advance() == ")"
        assert scanner.current == 2

    def test_advance_past_end_raises(self) -> None:
        """source の終端を超えて advance を呼ぶと IndexError を送出する。"""
        scanner = Scanner("(")
        scanner.advance()

        with pytest.raises(IndexError):
            scanner.advance()
