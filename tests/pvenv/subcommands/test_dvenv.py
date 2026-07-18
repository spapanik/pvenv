import os
from pathlib import Path
from unittest import mock

from pvenv.subcommands.dvenv import Command


@mock.patch.object(Command, "execute")
def test_run(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    command = Command([tmp_path], dry_run=True, verbosity=0)
    command.run()
    assert mock_execute.call_args_list == [
        mock.call(f"declare -f deactivate > {os.devnull} && deactivate"),
        mock.call("outvenv"),
    ]
