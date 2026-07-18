from pathlib import Path
from unittest import mock

from pvenv.subcommands.rmvenv import Command


@mock.patch("pvenv.subcommands.rmvenv.SGRString")
def test_run_removes_venv(mock_string: mock.MagicMock, tmp_path: Path) -> None:
    venv_path = tmp_path / "test"
    venv_path.mkdir()
    command = Command([tmp_path], dry_run=False, verbosity=0, venvs_to_remove=["test"])
    command.run()
    assert not venv_path.exists()
    assert mock_string.call_args_list == [mock.call("test removed successfully!")]


@mock.patch("pvenv.subcommands.rmvenv.SGRString")
def test_run_missing_venv(mock_string: mock.MagicMock, tmp_path: Path) -> None:
    command = Command(
        [tmp_path], dry_run=False, verbosity=0, venvs_to_remove=["missing"]
    )
    command.run()
    assert mock_string.call_args_list == [
        mock.call("missing does not exist, skipping...", is_error=True)
    ]


@mock.patch("pvenv.subcommands.rmvenv.SGRString")
def test_run_venv_not_a_directory(mock_string: mock.MagicMock, tmp_path: Path) -> None:
    venv_path = tmp_path / "test"
    venv_path.touch()
    command = Command([tmp_path], dry_run=False, verbosity=0, venvs_to_remove=["test"])
    command.run()
    assert venv_path.exists()
    assert mock_string.call_args_list == [
        mock.call("Cannot delete test, skipping...", is_error=True)
    ]
