from __future__ import annotations

from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from argparse import Namespace
    from pathlib import Path


class Command(BaseCommand):
    __slots__ = ("base_dir",)

    def __init__(self, options: Namespace) -> None:
        super().__init__(options)
        self.base_dir: Path = options.base_dir

    def run(self) -> None:
        for directory in sorted(self.base_dir.glob("*")):
            if directory.is_dir():
                self.output(SGRString(directory.name))
