from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Ok[T]:
    value: T

    def map[U](self, f: Callable[[T], U]) -> Ok[U]:
        return Ok(f(self.value))

    def flat_map[U, E](self, f: Callable[[T], Result[U, E]]) -> Result[U, E]:
        return f(self.value)

    def unwrap_or(self, default: T) -> T:
        return self.value


@dataclass(frozen=True)
class Err[E]:
    error: E

    def map[U](self, f: Callable[..., U]) -> Err[E]:
        return self

    def flat_map(self, f: Callable[..., Result[object, E]]) -> Err[E]:
        return self

    def unwrap_or[T](self, default: T) -> T:
        return default


type Result[T, E] = Ok[T] | Err[E]
