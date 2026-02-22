"""Tests for lib_mov_top_list."""

from typer.testing import CliRunner

from lib_mov_top_list import __version__


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
