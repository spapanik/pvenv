from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from argparse import Namespace
    from pathlib import Path


class Command(BaseCommand):
    def __init__(self, options: Namespace) -> None:
        super().__init__(options)
        self.base_dir: Path = options.base_dir
        self.venv_to_remove: list[str] = options.venvs_to_remove

    def run(self) -> None:
        for venv in self.venv_to_remove:
            venv_path = self.base_dir.joinpath(venv)
            if not venv_path.exists():
                self.output(
                    SGRString(f"{venv} does not exist, skipping..."), is_error=True
                )
                continue
            try:
                shutil.rmtree(venv_path)
            except (PermissionError, NotADirectoryError):
                self.output(
                    SGRString(f"Cannot delete {venv}, skipping..."), is_error=True
                )
                continue

            self.output(SGRString(f"{venv} removed successfully!"))
