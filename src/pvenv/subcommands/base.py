from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

from pyutilkit.term import SGRString

from pvenv.lib.constants import SHELL_PREFIX

if TYPE_CHECKING:
    from pathlib import Path


class BaseCommand:
    __slots__ = ("base_dirs", "dry_run", "verbosity")

    def __init__(
        self, base_dirs: list[Path], *, dry_run: bool, verbosity: int, **_kwargs: object
    ) -> None:
        self.base_dirs: list[Path] = base_dirs
        self.dry_run: bool = dry_run
        self.verbosity: int = verbosity

    def run(self) -> None:
        raise NotImplementedError

    def execute(self, command: str) -> None:
        if self.verbosity or self.dry_run:
            SGRString(command).print()

        if not self.dry_run:
            SGRString(command, prefix=SHELL_PREFIX, force_prefix=True).print()

    def find_venv(self, venv_name: str) -> Path:
        for i, base_dir in enumerate(self.base_dirs):
            venv_path = base_dir / venv_name
            if venv_path.exists():
                if i > 0:
                    warnings.warn(
                        f"Venv '{venv_name}' was found in a legacy location. "
                        "Support for legacy locations will be removed in pvenv 4.0.",
                        FutureWarning,
                        stacklevel=2,
                    )
                return venv_path
        msg = f"Venv {venv_name} doesn't exist, aborting..."
        raise RuntimeError(msg)
