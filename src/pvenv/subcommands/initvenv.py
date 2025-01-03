from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from argparse import Namespace


class Command(BaseCommand):
    __slots__ = ()

    def __init__(self, options: Namespace) -> None:
        super().__init__(options)

    def shell_script(self) -> Path:
        return Path(__file__).parent.joinpath("scripts/pvenv.sh").absolute()

    def run(self) -> None:
        self.output(
            SGRString("Add the following line to your shell rc:"),
            SGRString(f". {self.shell_script()}"),
        )
