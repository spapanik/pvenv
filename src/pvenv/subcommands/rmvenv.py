from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from pathlib import Path


class Command(BaseCommand):
    __slots__ = ("venvs_to_remove",)

    def __init__(
        self,
        base_dirs: list[Path],
        *,
        dry_run: bool,
        verbosity: int,
        venvs_to_remove: list[str],
    ) -> None:
        super().__init__(base_dirs, dry_run=dry_run, verbosity=verbosity)
        self.venvs_to_remove: list[str] = venvs_to_remove

    def run(self) -> None:
        for venv in self.venvs_to_remove:
            try:
                venv_path = self.find_venv(venv)
            except RuntimeError:
                SGRString(f"{venv} does not exist, skipping...", is_error=True).print()
                continue
            try:
                shutil.rmtree(venv_path)
            except (PermissionError, NotADirectoryError):
                SGRString(f"Cannot delete {venv}, skipping...", is_error=True).print()
                continue

            SGRString(f"{venv} removed successfully!")
