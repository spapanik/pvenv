import argparse
import os
import sys
from pathlib import Path

from pvenv import __version__, subcommands

sys.tracebacklimit = 0


def parse_args():
    parser = argparse.ArgumentParser(
        prog="pvenv", description="A utility to manage virtual environments"
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print the version and exit",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List venvs")
    return parser.parse_args()


def main() -> None:
    base_dir = Path(
        os.getenv("PVENV_BASE", f"{os.path.expanduser('~')}/.local/share/virtualenvs")
    ).absolute()
    args = parse_args()
    if args.command == "list":
        module = subcommands.lsvenv
    else:
        print("Add the following line to your shell rc:")
        print(f". {Path(__file__).parent.joinpath('scripts/pvenv.sh').absolute()}")
        return
    module.Command(base_dir, args).run()
