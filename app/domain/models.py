from dataclasses import dataclass
from datetime import date, datetime, time
from enum import Enum, auto


class GoalKind(Enum):
    NUMBER = auto()
    COUNTER = auto()
    STREAK = auto()


class Direction(Enum):
    INCREASING = auto()
    DECREASING = auto()


class Status(Enum):
    GREEN = auto()
    AMBER = auto()
    RED = auto()


class Mode(Enum):
    DAY = auto()
    MORNING = auto()
    BEDTIME = auto()


@dataclass(frozen=True)
class Goal:
    id: int
    name: str
    kind: GoalKind
    unit: str
    start_value: float
    target_value: float
    start_date: date
    deadline: date
    tap_step: float = 1.0

    @property
    def direction(self) -> Direction:
        if self.target_value < self.start_value:
            return Direction.DECREASING
        return Direction.INCREASING


@dataclass(frozen=True)
class Entry:
    goal_id: int
    recorded_at: datetime
    value: float


@dataclass(frozen=True)
class Settings:
    alarm_time: time
    bedtime: time
    morning_window_minutes: int
    timezone: str
    latitude: float
    longitude: float
