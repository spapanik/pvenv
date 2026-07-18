from argparse import Namespace
from pathlib import Path
from unittest import mock

import pytest

from pvenv.lib.cli import CliArgs, get_default_base, parse_args


@pytest.mark.parametrize(
    ("subcommand", "verbose", "expected_command", "expected_verbosity"),
    [
        ("deactivate", "-v", "deactivate_subcommand", 1),
        ("init", "-vv", "init_subcommand", 2),
        ("make", "-vvvvv", "make_subcommand", 5),
    ],
)
def test_pvenv_verbose(
    subcommand: str, verbose: str, expected_command: str, expected_verbosity: int
) -> None:
    with mock.patch("sys.argv", ["pvenv", subcommand, verbose]):
        args = parse_args()

    assert getattr(args, expected_command) is not None
    assert args.verbosity == expected_verbosity


@pytest.mark.parametrize(
    "subcommand",
    ["out", "list", "init", "deactivate", "in", "make", "rm"],
)
def test_pvenv_subcommands(subcommand: str) -> None:
    with mock.patch("sys.argv", ["pvenv", subcommand]):
        args = parse_args()
    subcommand_attr = f"{subcommand}_subcommand"
    if subcommand == "rm":
        subcommand_attr = "rm_subcommand"
    assert getattr(args, subcommand_attr) is not None
    assert args.verbosity == 0


def test_pvenv_activate() -> None:
    with mock.patch("sys.argv", ["pvenv", "activate", "name"]):
        args = parse_args()
    assert args.activate_subcommand is not None
    assert args.verbosity == 0


@mock.patch("sys.argv", ["pvenv", "new_subcommand"])
def test_pvenv_unknown_subcommand() -> None:
    with pytest.raises(SystemExit, match="2"):
        parse_args()


def test_pvenv_legacy_base_dir(tmp_path: Path) -> None:
    legacy_dir = tmp_path / "legacy"
    legacy_dir.joinpath("venv").mkdir(parents=True)
    with (
        mock.patch("sys.argv", ["pvenv", "list"]),
        mock.patch("pvenv.lib.cli.get_legacy_base", return_value=legacy_dir),
    ):
        args = parse_args()
    assert args.base_dirs == [get_default_base(), legacy_dir]


def test_cli_args_without_matching_subcommand(tmp_path: Path) -> None:
    args = Namespace(
        subcommand="unknown", base_dir=tmp_path, dry_run=False, verbosity=0
    )
    with mock.patch("pvenv.lib.cli.get_legacy_base", return_value=tmp_path):
        cli_args = CliArgs.from_args(args)
    assert cli_args.base_dirs == [tmp_path]
    assert cli_args.rm_subcommand is None
