import dataclasses
from datetime import date, datetime, time

import pytest

from app.domain.models import Direction, Entry, Goal, GoalKind, Mode, Settings, Status


def make_goal(
    name: str = "Weight",
    start_value: float = 90.0,
    target_value: float = 80.0,
    deadline: date = date(2026, 12, 1),
) -> Goal:
    return Goal(
        id=1,
        name=name,
        kind=GoalKind.NUMBER,
        unit="kg",
        start_value=start_value,
        target_value=target_value,
        start_date=date(2026, 11, 1),
        deadline=deadline,
    )


@pytest.mark.parametrize(
    ("start", "target", "expected"),
    [
        (90.0, 80.0, Direction.DECREASING),
        (0.0, 20.0, Direction.INCREASING),
        (5.0, 5.0, Direction.INCREASING),
    ],
)
def test_direction_derived_from_start_and_target(
    start: float, target: float, expected: Direction
) -> None:
    assert make_goal(start_value=start, target_value=target).direction == expected


def test_goal_tap_step_defaults_to_one() -> None:
    assert make_goal().tap_step == 1.0


def test_goal_accepts_empty_name_and_inverted_dates() -> None:
    goal = make_goal(name="", deadline=date(2026, 10, 1))
    assert goal.name == ""


def test_goal_is_frozen() -> None:
    with pytest.raises(dataclasses.FrozenInstanceError):
        make_goal().name = "other"  # type: ignore[misc]


def test_entry_is_frozen() -> None:
    entry = Entry(goal_id=1, recorded_at=datetime(2026, 11, 2, 8, 0), value=1.0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        entry.value = 2.0  # type: ignore[misc]


def test_settings_is_frozen() -> None:
    settings = Settings(
        alarm_time=time(7, 0),
        bedtime=time(23, 0),
        morning_window_minutes=5,
        timezone="Europe/London",
        latitude=51.5,
        longitude=-0.1,
    )
    with pytest.raises(dataclasses.FrozenInstanceError):
        settings.morning_window_minutes = 10  # type: ignore[misc]


def test_enums_expose_expected_members() -> None:
    assert {k.name for k in GoalKind} == {"NUMBER", "COUNTER", "STREAK"}
    assert {s.name for s in Status} == {"GREEN", "AMBER", "RED"}
    assert {m.name for m in Mode} == {"DAY", "MORNING", "BEDTIME"}
