from pathlib import Path
from unittest import mock

from pvenv import subcommands
from pvenv.__main__ import main
from pvenv.lib.cli import (
    ActivateCliArgs,
    CliArgs,
    DeactivateCliArgs,
    InCliArgs,
    InitCliArgs,
    ListCliArgs,
    MakeCliArgs,
    OutCliArgs,
    RmCliArgs,
)


def _mock_args(
    out_subcommand: OutCliArgs | None = None,
    list_subcommand: ListCliArgs | None = None,
    init_subcommand: InitCliArgs | None = None,
    deactivate_subcommand: DeactivateCliArgs | None = None,
    in_subcommand: InCliArgs | None = None,
    activate_subcommand: ActivateCliArgs | None = None,
    make_subcommand: MakeCliArgs | None = None,
    rm_subcommand: RmCliArgs | None = None,
) -> CliArgs:
    return CliArgs(
        base_dirs=[Path.cwd()],
        dry_run=False,
        verbosity=0,
        out_subcommand=out_subcommand,
        list_subcommand=list_subcommand,
        init_subcommand=init_subcommand,
        deactivate_subcommand=deactivate_subcommand,
        in_subcommand=in_subcommand,
        activate_subcommand=activate_subcommand,
        make_subcommand=make_subcommand,
        rm_subcommand=rm_subcommand,
    )


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.avenv.Command, "run")
def test_activate_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(
        activate_subcommand=ActivateCliArgs(venv="test", cd=True)
    )
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.dvenv.Command, "run")
def test_deactivate_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(deactivate_subcommand=DeactivateCliArgs())
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.invenv.Command, "run")
def test_in_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(in_subcommand=InCliArgs(env_vars=[], files=[]))
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.initvenv.Command, "run")
def test_init_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(init_subcommand=InitCliArgs())
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.lsvenv.Command, "run")
def test_list_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(list_subcommand=ListCliArgs())
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.mkvenv.Command, "run")
def test_make_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(
        make_subcommand=MakeCliArgs(
            venv="test",
            environments=[],
            project="/dev/null",
            python="system",
            legacy_seed=None,
            seed=None,
        )
    )
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.outvenv.Command, "run")
def test_out_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(out_subcommand=OutCliArgs())
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]


@mock.patch("pvenv.__main__.parse_args")
@mock.patch.object(subcommands.rmvenv.Command, "run")
def test_rm_subcommand(
    mock_command: mock.MagicMock, mock_parse: mock.MagicMock
) -> None:
    mock_parse.return_value = _mock_args(
        rm_subcommand=RmCliArgs(venvs_to_remove=["test"])
    )
    main()
    assert mock_command.call_count == 1
    assert mock_command.call_args_list == [mock.call()]
