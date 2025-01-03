from __future__ import annotations

import pytest

from pvenv.subcommands.invenv import Command


@pytest.mark.parametrize(
    ("line", "expected"), [("x=1", ["x", "1"]), ("x=a=1", ["x", "a=1"])]
)
def test_parse_env_var(line: str, expected: list[str]) -> None:
    assert Command.parse_env_var(line) == expected
