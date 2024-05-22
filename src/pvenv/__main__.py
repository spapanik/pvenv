from pathlib import Path
from types import ModuleType

from pvenv import subcommands
from pvenv.lib.parser import parse_args


def main() -> None:
    args = parse_args()
    module: ModuleType
    if args.subcommand == "in":
        module = subcommands.invenv
    elif args.subcommand == "out":
        module = subcommands.outvenv
    elif args.subcommand == "activate":
        module = subcommands.avenv
    elif args.subcommand == "deactivate":
        module = subcommands.dvenv
    elif args.subcommand == "list":
        module = subcommands.lsvenv
    elif args.subcommand == "make":
        module = subcommands.mkvenv
    elif args.subcommand == "rm":
        module = subcommands.rmvenv
    else:
        print("Add the following line to your shell rc:")
        print(f". {Path(__file__).parent.joinpath('scripts/pvenv.sh').absolute()}")
        return
    module.Command(args).run()
