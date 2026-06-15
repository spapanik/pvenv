from __future__ import annotations

from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from pathlib import Path


class Command(BaseCommand):
    __slots__ = ()

    def __init__(self, base_dir: Path, *, dry_run: bool, verbosity: int) -> None:
        super().__init__(base_dir, dry_run=dry_run, verbosity=verbosity)

    def run(self) -> None:
        for directory in sorted(self.base_dir.glob("*")):
            if directory.is_dir():
                SGRString(directory.name).print()
