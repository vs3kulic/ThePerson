"""Pytest coverage for the Person.smile method."""

import pytest

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
