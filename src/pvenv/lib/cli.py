from __future__ import annotations

import os
import sys
from argparse import SUPPRESS, ArgumentParser, BooleanOptionalAction, Namespace
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from pvenv.__version__ import __version__

if TYPE_CHECKING:
    from typing_extensions import Self  # upgrade: py3.10: import from typing

sys.tracebacklimit = 0


@dataclass(frozen=True, slots=True)
class OutCliArgs:
    @classmethod
    def from_args(cls, _args: Namespace, /) -> Self:
        return cls()


@dataclass(frozen=True, slots=True)
class ListCliArgs:
    @classmethod
    def from_args(cls, _args: Namespace, /) -> Self:
        return cls()


@dataclass(frozen=True, slots=True)
class InitCliArgs:
    @classmethod
    def from_args(cls, _args: Namespace, /) -> Self:
        return cls()


@dataclass(frozen=True, slots=True)
class DeactivateCliArgs:
    @classmethod
    def from_args(cls, _args: Namespace, /) -> Self:
        return cls()


@dataclass(frozen=True, slots=True)
class InCliArgs:
    env_vars: list[str]
    files: list[str]

    @classmethod
    def from_args(cls, args: Namespace, /) -> Self:
        return cls(
            env_vars=args.env_vars,
            files=args.files,
        )


@dataclass(frozen=True, slots=True)
class ActivateCliArgs:
    venv: str
    cd: bool

    @classmethod
    def from_args(cls, args: Namespace, /) -> Self:
        return cls(
            venv=args.venv,
            cd=args.cd,
        )


@dataclass(frozen=True, slots=True)
class MakeCliArgs:
    venv: str
    environments: list[str]
    project: str
    python: str
    legacy_seed: bool | None
    seed: bool | None

    @classmethod
    def from_args(cls, args: Namespace, /) -> Self:
        return cls(
            venv=args.venv,
            environments=args.environments,
            project=args.project,
            python=args.python,
            legacy_seed=args.legacy_seed,
            seed=args.seed,
        )


@dataclass(frozen=True, slots=True)
class RmCliArgs:
    venvs_to_remove: list[str]

    @classmethod
    def from_args(cls, args: Namespace, /) -> Self:
        return cls(
            venvs_to_remove=args.venvs_to_remove,
        )


@dataclass(frozen=True, slots=True)
class CliArgs:
    base_dirs: list[Path]
    dry_run: bool
    verbosity: int
    out_subcommand: OutCliArgs | None
    list_subcommand: ListCliArgs | None
    init_subcommand: InitCliArgs | None
    deactivate_subcommand: DeactivateCliArgs | None
    in_subcommand: InCliArgs | None
    activate_subcommand: ActivateCliArgs | None
    make_subcommand: MakeCliArgs | None
    rm_subcommand: RmCliArgs | None

    @classmethod
    def from_args(cls, args: Namespace, /) -> Self:
        in_subcommand = None
        init_subcommand = None
        out_subcommand = None
        activate_subcommand = None
        deactivate_subcommand = None
        list_subcommand = None
        make_subcommand = None
        rm_subcommand = None
        legacy_dir = get_legacy_base()
        base_dirs = [args.base_dir]
        if legacy_dir != args.base_dir and next(legacy_dir.iterdir(), None) is not None:
            base_dirs.append(legacy_dir)

        match args.subcommand:
            case "in":
                in_subcommand = InCliArgs.from_args(args)
            case "init":
                init_subcommand = InitCliArgs.from_args(args)
            case "out":
                out_subcommand = OutCliArgs.from_args(args)
            case "activate":
                activate_subcommand = ActivateCliArgs.from_args(args)
            case "deactivate":
                deactivate_subcommand = DeactivateCliArgs.from_args(args)
            case "list":
                list_subcommand = ListCliArgs.from_args(args)
            case "make":
                make_subcommand = MakeCliArgs.from_args(args)
            case "rm":
                rm_subcommand = RmCliArgs.from_args(args)

        return cls(
            base_dirs=base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            out_subcommand=out_subcommand,
            list_subcommand=list_subcommand,
            init_subcommand=init_subcommand,
            deactivate_subcommand=deactivate_subcommand,
            in_subcommand=in_subcommand,
            activate_subcommand=activate_subcommand,
            make_subcommand=make_subcommand,
            rm_subcommand=rm_subcommand,
        )


def get_default_base() -> Path:
    default = "~/.local/share/pvenv/virtualenvs"
    return Path(os.getenv("PVENV_BASE", default)).expanduser().absolute()


def get_legacy_base() -> Path:
    default = "~/.local/share/virtualenvs"
    return Path(os.getenv("PVENV_BASE", default)).expanduser().absolute()


def parse_args() -> CliArgs:
    parser = ArgumentParser(
        prog="pvenv",
        description="A utility to manage virtual environments",
        epilog="You can find the full documentation at: https://p-venv.readthedocs.io/en/stable/",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="print the version and exit",
    )

    default_base = get_default_base()
    parent_parser = ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--base_dir",
        action="store_const",
        const=default_base,
        default=default_base,
        help=SUPPRESS,
    )
    parent_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="only print the commands to be executed",
    )
    parent_parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbosity",
        help="increase the level of verbosity",
    )

    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    subparsers.add_parser("out", help="List venvs", parents=[parent_parser])
    subparsers.add_parser("list", help="List venvs", parents=[parent_parser])
    subparsers.add_parser(
        "init", help="Initialisation instructions for pvenv", parents=[parent_parser]
    )
    subparsers.add_parser(
        "deactivate", help="Deactivate a venv", parents=[parent_parser]
    )

    invenv_parser = subparsers.add_parser(
        "in", help="Export new variables for the venv", parents=[parent_parser]
    )
    invenv_parser.add_argument("env_vars", nargs="*")
    invenv_parser.add_argument("-f", "--files", action="append", default=[])

    avenv_parser = subparsers.add_parser(
        "activate", help="Activate a venv", parents=[parent_parser]
    )
    avenv_parser.add_argument("venv")
    avenv_parser.add_argument("-n", "--no-cd", dest="cd", action="store_false")

    mkvenv_parser = subparsers.add_parser(
        "make", help="Make a new venv", parents=[parent_parser]
    )
    mkvenv_parser.add_argument("venv", nargs="?", default=Path().absolute().name)
    mkvenv_parser.add_argument("-e", "--environments", action="append", default=[])
    mkvenv_parser.add_argument("-P", "--project", default=Path().absolute().as_posix())
    mkvenv_parser.add_argument("-p", "--python", default="system")
    mkvenv_parser.add_argument("--legacy-seed", action=BooleanOptionalAction)
    mkvenv_parser.add_argument("--seed", action=BooleanOptionalAction)

    rmvenv_parser = subparsers.add_parser(
        "rm", help="Remove virtualenvs", parents=[parent_parser]
    )
    rmvenv_parser.add_argument("venvs_to_remove", nargs="*")

    args = parser.parse_args()
    if args.verbosity > 0:
        sys.tracebacklimit = 1000

    return CliArgs.from_args(args)
