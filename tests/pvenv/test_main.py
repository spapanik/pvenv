from unittest import mock

from pvenv import subcommands
from pvenv.__main__ import main

X = [
    "activate",
    "deactivate",
    "in",
    "init",
    "list",
    "make",
    "out",
    "rm",
]


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="activate")),
)
@mock.patch.object(subcommands.avenv.Command, "run")
def test_activate_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="deactivate")),
)
@mock.patch.object(subcommands.dvenv.Command, "run")
def test_deactivate_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="in")),
)
@mock.patch.object(subcommands.invenv.Command, "run")
def test_in_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="init")),
)
@mock.patch.object(subcommands.initvenv.Command, "run")
def test_init_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="list")),
)
@mock.patch.object(subcommands.lsvenv.Command, "run")
def test_list_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="make")),
)
@mock.patch.object(subcommands.mkvenv.Command, "run")
def test_make_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="out")),
)
@mock.patch.object(subcommands.outvenv.Command, "run")
def test_out_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls


@mock.patch(
    "pvenv.__main__.parse_args",
    new=mock.MagicMock(return_value=mock.MagicMock(subcommand="rm")),
)
@mock.patch.object(subcommands.rmvenv.Command, "run")
def test_rm_subcommand(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call()]
    assert mock_command.call_args_list == calls
