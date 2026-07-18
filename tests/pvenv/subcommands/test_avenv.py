from pathlib import Path
from unittest import mock

from pvenv.subcommands.avenv import SCRIPTS_DIR, Command


def _make_venv(base_dir: Path) -> Path:
    venv_path = base_dir / "test"
    venv_path.joinpath(SCRIPTS_DIR).mkdir(parents=True)
    return venv_path


@mock.patch.object(Command, "execute")
def test_run_without_project(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    venv_path = _make_venv(tmp_path)
    command = Command([tmp_path], dry_run=True, verbosity=0, venv="test", cd=True)
    with mock.patch.dict("os.environ", {}, clear=True):
        command.run()
    assert mock_execute.call_args_list == [
        mock.call(f". {venv_path / SCRIPTS_DIR / 'activate'}"),
        mock.call(f"invenv UV_PROJECT_ENVIRONMENT={venv_path}"),
    ]


@mock.patch.object(Command, "execute")
def test_run_deactivates_active_venv(
    mock_execute: mock.MagicMock, tmp_path: Path
) -> None:
    venv_path = _make_venv(tmp_path)
    command = Command([tmp_path], dry_run=True, verbosity=0, venv="test", cd=True)
    with mock.patch.dict("os.environ", {"VIRTUAL_ENV": "/old"}, clear=True):
        command.run()
    assert mock_execute.call_args_list == [
        mock.call("dvenv"),
        mock.call(f". {venv_path / SCRIPTS_DIR / 'activate'}"),
        mock.call(f"invenv UV_PROJECT_ENVIRONMENT={venv_path}"),
    ]


@mock.patch.object(Command, "execute")
@mock.patch("pvenv.subcommands.avenv.ConfigParser")
def test_run_with_project_and_environment(
    mock_parser: mock.MagicMock, mock_execute: mock.MagicMock, tmp_path: Path
) -> None:
    venv_path = _make_venv(tmp_path)
    venv_path.joinpath(".project").write_text("/home/user/project\n")
    venv_path.joinpath(".environment").write_text("production.env\n")
    mock_parser.return_value.data = {"KEY": "value"}
    command = Command([tmp_path], dry_run=True, verbosity=0, venv="test", cd=True)
    with mock.patch.dict("os.environ", {}, clear=True):
        command.run()
    assert mock_parser.call_args_list == [mock.call(["production.env"])]
    assert mock_execute.call_args_list == [
        mock.call("cd /home/user/project"),
        mock.call(f". {venv_path / SCRIPTS_DIR / 'activate'}"),
        mock.call(f"invenv UV_PROJECT_ENVIRONMENT={venv_path} KEY=value"),
    ]


@mock.patch.object(Command, "execute")
def test_run_with_project_no_cd(mock_execute: mock.MagicMock, tmp_path: Path) -> None:
    venv_path = _make_venv(tmp_path)
    venv_path.joinpath(".project").write_text("/home/user/project\n")
    command = Command([tmp_path], dry_run=True, verbosity=0, venv="test", cd=False)
    with mock.patch.dict("os.environ", {}, clear=True):
        command.run()
    assert mock_execute.call_args_list == [
        mock.call(f". {venv_path / SCRIPTS_DIR / 'activate'}"),
        mock.call(f"invenv UV_PROJECT_ENVIRONMENT={venv_path}"),
    ]
