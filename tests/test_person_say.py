"""Pytest coverage for Person.say speech repetition behavior."""

import pytest

from theperson.person import Person


def test_say_prints_once_by_default(capsys: pytest.CaptureFixture[str]) -> None:
    Person.say("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"


def test_say_repeats_message(capsys: pytest.CaptureFixture[str]) -> None:
    Person.say("hello", repeat=3)
    captured = capsys.readouterr()
    assert captured.out == "hello\nhello\nhello\n"


def test_say_repeat_zero_prints_nothing(
    capsys: pytest.CaptureFixture[str],
) -> None:
    Person.say("hello", repeat=0, delay=1)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_say_delay_applies_between_repetitions(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[float] = []

    def fake_sleep(seconds: float) -> None:
        calls.append(seconds)

    monkeypatch.setattr("theperson.person.time.sleep", fake_sleep)

    Person.say("hello", repeat=4, delay=0.25)

    assert calls == [0.25, 0.25, 0.25]


# noinspection PyTypeChecker
def test_say_validation_errors() -> None:
    with pytest.raises(TypeError):
        Person.say("hello", repeat="3")
    with pytest.raises(TypeError):
        Person.say("hello", repeat=True)
    with pytest.raises(ValueError):
        Person.say("hello", repeat=-1)

    with pytest.raises(TypeError):
        Person.say("hello", delay="1")
    with pytest.raises(TypeError):
        Person.say("hello", delay=False)
    with pytest.raises(ValueError):
        Person.say("hello", delay=-0.1)
