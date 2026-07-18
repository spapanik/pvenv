from pathlib import Path
from unittest import mock

from pvenv.subcommands.outvenv import Command


@mock.patch.object(Command, "execute")
def test_run_outside_venv(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    command = Command([tmp_path], dry_run=True, verbosity=0)
    with mock.patch.dict("os.environ", {}, clear=True):
        command.run()
    assert mock_execute.call_count == 0


@mock.patch.object(Command, "execute")
def test_run_inside_venv(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    environ = {
        "_PVENV_ENV": "true",
        "_PVENV_ENV_A": "old",
        "_PVENV_ENV_UNSET_B": "",
        "OTHER": "x",
    }
    command = Command([tmp_path], dry_run=True, verbosity=0)
    with mock.patch.dict("os.environ", environ, clear=True):
        command.run()
    assert mock_execute.call_args_list == [
        mock.call("unset _PVENV_ENV"),
        mock.call("export A=old"),
        mock.call("unset _PVENV_ENV_A"),
        mock.call("unset B"),
        mock.call("unset _PVENV_ENV_UNSET_B"),
    ]
