from __future__ import annotations

from typing import TYPE_CHECKING
from unittest import mock

from pvenv.subcommands.initvenv import Command

if TYPE_CHECKING:
    from pathlib import Path


def test_parse_env_var() -> None:
    assert Command.shell_script().exists()


@mock.patch("pvenv.subcommands.initvenv.SGRString")
def test_run(mock_string: mock.MagicMock, tmp_path: Path) -> None:
    command = Command([tmp_path], dry_run=False, verbosity=0)
    command.run()
    assert mock_string.call_args_list == [
        mock.call("Add the following line to your shell rc:"),
        mock.call(f". {Command.shell_script()}"),
    ]
