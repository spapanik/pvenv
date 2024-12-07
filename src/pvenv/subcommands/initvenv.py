from argparse import Namespace
from pathlib import Path

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand


class Command(BaseCommand):
    def __init__(self, options: Namespace) -> None:
        super().__init__(options)

    def shell_script(self) -> Path:
        return Path(__file__).parent.joinpath("scripts/pvenv.sh").absolute()

    def run(self) -> None:
        self.output(
            SGRString("Add the following line to your shell rc:"),
            SGRString(f". {self.shell_script()}"),
        )
