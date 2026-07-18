from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

import pytest

from pvenv.subcommands.invenv import Command

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize(
    ("line", "expected"), [("x=1", ["x", "1"]), ("x=a=1", ["x", "a=1"])]
)
def test_parse_env_var(line: str, expected: list[str]) -> None:
    assert Command.parse_env_var(line) == expected


def test_run_already_in_venv(tmp_path: Path) -> None:
    command = Command([tmp_path], dry_run=True, verbosity=0, env_vars=[], files=[])
    with (
        mock.patch.dict("os.environ", {"_PVENV_ENV": "true"}, clear=True),
        pytest.raises(RuntimeError, match="Already in a venv"),
    ):
        command.run()


@mock.patch.object(Command, "execute")
def test_run_with_files_and_env_vars(
    mock_execute: mock.MagicMock, tmp_path: Path
) -> None:
    env_file = tmp_path / "vars.env"
    env_file.write_text("# comment\n\nA=1\n")
    command = Command(
        [tmp_path],
        dry_run=True,
        verbosity=0,
        env_vars=["B=2"],
        files=[str(env_file)],
    )
    with mock.patch.dict("os.environ", {"A": "old"}, clear=True):
        command.run()
    assert mock_execute.call_args_list == [
        mock.call("export _PVENV_ENV=true"),
        mock.call("export _PVENV_ENV_A=old"),
        mock.call("export A=1"),
        mock.call("export _PVENV_ENV_UNSET_B="),
        mock.call("export B=2"),
    ]


@mock.patch.object(Command, "execute")
def test_run_without_new_vars(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    command = Command([tmp_path], dry_run=True, verbosity=0, env_vars=[], files=[])
    with mock.patch.dict("os.environ", {}, clear=True):
        command.run()
    assert mock_execute.call_count == 0
