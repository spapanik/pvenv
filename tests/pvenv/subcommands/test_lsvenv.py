from pathlib import Path
from unittest import mock

from pvenv.subcommands.lsvenv import Command


@mock.patch("pvenv.subcommands.lsvenv.SGRString")
def test_run(mock_string: mock.MagicMock, tmp_path: Path) -> None:
    primary = tmp_path / "primary"
    legacy = tmp_path / "legacy"
    primary.joinpath("b").mkdir(parents=True)
    primary.joinpath("a").mkdir()
    primary.joinpath("z.txt").touch()
    legacy.joinpath("a").mkdir(parents=True)
    legacy.joinpath("c").mkdir()
    command = Command([primary, legacy], dry_run=False, verbosity=0)
    command.run()
    assert mock_string.call_args_list == [
        mock.call("a"),
        mock.call("b"),
        mock.call("c"),
    ]
