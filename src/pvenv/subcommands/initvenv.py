from __future__ import annotations

from pathlib import Path

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand


class Command(BaseCommand):
    __slots__ = ()

    def __init__(self, base_dirs: list[Path], *, dry_run: bool, verbosity: int) -> None:
        super().__init__(base_dirs, dry_run=dry_run, verbosity=verbosity)

    @staticmethod
    def shell_script() -> Path:
        return Path(__file__).parents[1].joinpath("scripts/pvenv.sh").resolve()

    def run(self) -> None:
        SGRString("Add the following line to your shell rc:").print()
        SGRString(f". {self.shell_script()}").print()
