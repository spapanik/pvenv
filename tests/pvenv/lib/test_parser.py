from unittest import mock

import pytest

from pvenv.lib.parser import parse_args


@pytest.mark.parametrize(
    ("subcommand", "verbose", "expected_command", "expected_verbosity"),
    [
        ("deactivate", "-v", "deactivate", 1),
        ("init", "-vv", "init", 2),
        ("make", "-vvvvv", "make", 5),
    ],
)
def test_pvenv_verbose(
    subcommand: str, verbose: str, expected_command: str, expected_verbosity: int
) -> None:
    with mock.patch("sys.argv", ["pvenv", subcommand, verbose]):
        args = parse_args()

    assert args.subcommand == expected_command
    assert args.verbosity == expected_verbosity


@pytest.mark.parametrize(
    "subcommand",
    ["out", "list", "init", "deactivate", "in", "make", "rm"],
)
def test_pvenv_subcommands(subcommand: str) -> None:
    with mock.patch("sys.argv", ["pvenv", subcommand]):
        args = parse_args()
    assert args.subcommand == subcommand
    assert args.verbosity == 0


def test_pvenv_activate() -> None:
    with mock.patch("sys.argv", ["pvenv", "activate", "name"]):
        args = parse_args()
    assert args.subcommand == "activate"
    assert args.verbosity == 0


@mock.patch("sys.argv", ["pvenv", "new_subcommand"])
def test_pvenv_unknown_subcommand() -> None:
    with pytest.raises(SystemExit, match="2"):
        parse_args()
