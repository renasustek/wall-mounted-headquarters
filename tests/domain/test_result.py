from app.domain.result import Err, Ok, Result


def test_map_transforms_ok_value() -> None:
    result: Result[int, str] = Ok(2)
    assert result.map(lambda n: n * 10) == Ok(20)


def test_map_leaves_err_untouched() -> None:
    result: Result[int, str] = Err("boom")
    assert result.map(lambda n: n * 10) == Err("boom")


def test_flat_map_chains_ok_into_ok() -> None:
    result: Result[int, str] = Ok(2)
    assert result.flat_map(lambda n: Ok(n + 1)) == Ok(3)


def test_flat_map_chains_ok_into_err() -> None:
    result: Result[int, str] = Ok(2)
    assert result.flat_map(lambda _: Err("bad")) == Err("bad")


def test_flat_map_skips_function_on_err() -> None:
    result: Result[int, str] = Err("first")
    assert result.flat_map(lambda n: Ok(n + 1)) == Err("first")


def test_unwrap_or_returns_value_on_ok() -> None:
    result: Result[int, str] = Ok(5)
    assert result.unwrap_or(0) == 5


def test_unwrap_or_returns_default_on_err() -> None:
    result: Result[int, str] = Err("boom")
    assert result.unwrap_or(0) == 0
