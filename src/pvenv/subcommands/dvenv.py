from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from pathlib import Path


class Command(BaseCommand):
    __slots__ = ()

    def __init__(self, base_dir: Path, *, dry_run: bool, verbosity: int) -> None:
        super().__init__(base_dir, dry_run=dry_run, verbosity=verbosity)

    def run(self) -> None:
        self.execute(f"declare -f deactivate > {os.devnull} && deactivate")
        self.execute("outvenv")
