from argparse import Namespace
from pathlib import Path
from unittest import mock

from pvenv.subcommands.base import BaseCommand


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_dry_run_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    options = Namespace(base_dir=Path.cwd(), dry_run=True, verbosity=1)
    base = BaseCommand(options)
    base.execute(command)
    expected_calls = [mock.call(command)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_dry_run_non_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    options = Namespace(base_dir=Path.cwd(), dry_run=True, verbosity=0)
    base = BaseCommand(options)
    base.execute(command)
    expected_calls = [mock.call(command)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls


@mock.patch("pvenv.subcommands.base.SGRString")
def test_execute_live_run_verbose(mock_string: mock.MagicMock) -> None:
    command = "echo 'Hello, World!'"
    options = Namespace(base_dir=Path.cwd(), dry_run=False, verbosity=1)
    base = BaseCommand(options)
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
    options = Namespace(base_dir=Path.cwd(), dry_run=False, verbosity=0)
    base = BaseCommand(options)
    base.execute(command)
    expected_calls = [mock.call(command, prefix=chr(2), force_prefix=True)]
    assert mock_string.call_count == 1
    assert mock_string.call_args_list == expected_calls
