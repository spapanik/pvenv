from pathlib import Path
from unittest import mock

import pytest

from pvenv.subcommands.base import BaseCommand


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_dry_run_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    base = BaseCommand([Path.cwd()], dry_run=True, verbosity=1)
    base.execute(command)
    expected_calls = [mock.call(command)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_dry_run_non_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    base = BaseCommand([Path.cwd()], dry_run=True, verbosity=0)
    base.execute(command)
    expected_calls = [mock.call(command)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_live_run_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    base = BaseCommand([Path.cwd()], dry_run=False, verbosity=1)
    base.execute(command)
    expected_calls = [
        mock.call(command),
        mock.call(command, prefix=chr(2), force_prefix=True),
    ]
    assert mock_string.call_count == 2
    assert mock_string.call_args_list == expected_calls


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_live_run_non_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    base = BaseCommand([Path.cwd()], dry_run=False, verbosity=0)
    base.execute(command)
    expected_calls = [mock.call(command, prefix=chr(2), force_prefix=True)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls


def test_find_venv_in_primary_location(tmp_path: Path) -> None:
    venv_path = tmp_path / "test"
    venv_path.mkdir()
    base = BaseCommand([tmp_path], dry_run=True, verbosity=0)
    assert base.find_venv("test") == venv_path


def test_find_venv_in_legacy_location(tmp_path: Path) -> None:
    primary = tmp_path / "primary"
    primary.mkdir()
    legacy = tmp_path / "legacy"
    venv_path = legacy / "test"
    venv_path.mkdir(parents=True)
    base = BaseCommand([primary, legacy], dry_run=True, verbosity=0)
    with pytest.warns(FutureWarning, match="legacy location"):
        assert base.find_venv("test") == venv_path


def test_find_venv_missing(tmp_path: Path) -> None:
    base = BaseCommand([tmp_path], dry_run=True, verbosity=0)
    with pytest.raises(RuntimeError, match="doesn't exist"):
        base.find_venv("test")
