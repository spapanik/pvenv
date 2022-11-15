import argparse
import os
import sys
from pathlib import Path
from types import ModuleType

from pvenv import __version__, subcommands

sys.tracebacklimit = 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog="venv",
        description="A utility to manage virtual environments",
        epilog="You can find the full documentation at: https://p-venv.readthedocs.io/en/stable/",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print the version and exit",
    )
    subparsers = parser.add_subparsers(dest="command")

    invenv_parser = subparsers.add_parser(
        "in", help="Export new variables for the venv"
    )
    invenv_parser.add_argument("env_vars", nargs="*")
    invenv_parser.add_argument("-f", "--files", action="append", default=[])
    subparsers.add_parser("out", help="List venvs")

    subparsers.add_parser("list", help="List venvs")
    return parser.parse_args()


def main() -> None:
    base_dir = Path(
        os.getenv("PVENV_BASE", f"{os.path.expanduser('~')}/.local/share/virtualenvs")
    ).absolute()
    args = parse_args()
    module: ModuleType
    if args.command == "in":
        module = subcommands.invenv
    elif args.command == "out":
        module = subcommands.outvenv
    elif args.command == "list":
        module = subcommands.lsvenv
    else:
        print("Add the following line to your shell rc:")
        print(f". {Path(__file__).parent.joinpath('scripts/pvenv.sh').absolute()}")
        return
    module.Command(base_dir, args).run()
