import os
from pathlib import Path
from unittest import mock

import pytest

from pvenv.subcommands.mkvenv import Command


def test_environments_in_independent_venv(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="Cannot set environ in independent"):
        Command(
            [tmp_path],
            dry_run=True,
            verbosity=0,
            venv="test",
            environments=["a.env"],
            project=os.devnull,
            python="system",
            legacy_seed=None,
            seed=None,
        )


@mock.patch("pvenv.subcommands.mkvenv.DEV_NULL", Path("nul"))
def test_environments_in_independent_venv_on_windows(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="Cannot set environ in independent"):
        Command(
            [tmp_path],
            dry_run=True,
            verbosity=0,
            venv="test",
            environments=["a.env"],
            project="nul",
            python="system",
            legacy_seed=None,
            seed=None,
        )


def test_run_existing_venv(tmp_path: Path) -> None:
    tmp_path.joinpath("test").mkdir()
    command = Command(
        [tmp_path],
        dry_run=True,
        verbosity=0,
        venv="test",
        environments=[],
        project=str(tmp_path),
        python="system",
        legacy_seed=None,
        seed=None,
    )
    with pytest.raises(RuntimeError, match="already exists"):
        command.run()


@mock.patch("pvenv.subcommands.mkvenv.find_uv_bin", return_value="/uv")
@mock.patch.object(Command, "execute")
def test_run_without_python(
    mock_execute: mock.MagicMock, mock_uv: mock.MagicMock, tmp_path: Path
) -> None:
    command = Command(
        [tmp_path],
        dry_run=True,
        verbosity=0,
        venv="test",
        environments=[],
        project=str(tmp_path),
        python="",
        legacy_seed=None,
        seed=None,
    )
    command.run()
    venv_path = tmp_path / "test"
    assert mock_uv.call_count == 1
    assert mock_execute.call_args_list == [
        mock.call(f"mkdir -p {venv_path}"),
        mock.call(f"echo {tmp_path} > {venv_path / '.project'}"),
        mock.call("avenv test"),
    ]


@mock.patch("pvenv.subcommands.mkvenv.find_uv_bin", return_value="/uv")
@mock.patch.object(Command, "execute")
def test_run_independent_venv(
    mock_execute: mock.MagicMock, mock_uv: mock.MagicMock, tmp_path: Path
) -> None:
    command = Command(
        [tmp_path],
        dry_run=True,
        verbosity=0,
        venv="test",
        environments=[],
        project=os.devnull,
        python="system",
        legacy_seed=None,
        seed=None,
    )
    command.run()
    venv_path = tmp_path / "test"
    assert mock_uv.call_count == 1
    assert mock_execute.call_args_list == [
        mock.call(f"/uv venv --relocatable  {venv_path}"),
        mock.call(f"echo system > {venv_path / '.python'}"),
        mock.call("avenv test"),
    ]


@mock.patch("pvenv.subcommands.mkvenv.find_uv_bin", return_value="/uv")
@mock.patch.object(Command, "execute")
def test_run_with_all_options(
    mock_execute: mock.MagicMock, mock_uv: mock.MagicMock, tmp_path: Path
) -> None:
    project = tmp_path / "project"
    command = Command(
        [tmp_path],
        dry_run=True,
        verbosity=0,
        venv="test",
        environments=["a.env", "b.env"],
        project=str(project),
        python="3.12",
        legacy_seed=True,
        seed=True,
    )
    command.run()
    venv_path = tmp_path / "test"
    assert mock_uv.call_count == 1
    assert mock_execute.call_args_list == [
        mock.call(f"/uv venv --relocatable --python 3.12 --seed {venv_path}"),
        mock.call(f"echo 3.12 > {venv_path / '.python'}"),
        mock.call(f"echo {project} > {venv_path / '.project'}"),
        mock.call(f": > {venv_path / '.environment'}"),
        mock.call(f"echo {project / 'a.env'} >> {venv_path / '.environment'}"),
        mock.call(f"echo {project / 'b.env'} >> {venv_path / '.environment'}"),
        mock.call("avenv test"),
        mock.call("/uv pip install --upgrade uv"),
    ]
