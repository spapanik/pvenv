from unittest import mock

import pytest

from pvenv.lib.cli import parse_args


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
