"""Pytest coverage for the Person.smile method."""

from pathlib import Path
import sys
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from theperson.person import Person


VALID_SMILE_TYPES = ["small", "smile", "grin", "wide"]
VALID_SMILE_PRINT = ["🙂", "😊", "😁", "😄"]


def test_smile_without_type(
    capsys: pytest.CaptureFixture[str]
) -> None:
    dummy = Person()
    dummy.smile()
    captured = capsys.readouterr()
    assert captured.out.strip() in VALID_SMILE_PRINT


def test_smile_valid_type(
    capsys: pytest.CaptureFixture[str]
) -> None:
    dummy = Person()
    for smile_type, expected in zip(VALID_SMILE_TYPES, VALID_SMILE_PRINT):
        dummy.smile(smile_type)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected


def test_smile_unknown_type(
    capsys: pytest.CaptureFixture[str]
) -> None:
    dummy = Person()
    dummy.smile("foobar")
    captured = capsys.readouterr()
    assert captured.out.strip() in VALID_SMILE_PRINT


def test_smile_invalid_type() -> None:
    dummy = Person()
    with pytest.raises(TypeError):
        dummy.smile(123)
