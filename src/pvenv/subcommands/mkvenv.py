from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING

from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from argparse import Namespace

DEV_NULL = Path(os.devnull)


class Command(BaseCommand):
    __slots__ = ("environments", "project", "python", "venv")

    def __init__(self, options: Namespace) -> None:
        super().__init__(options)
        self.venv: str = options.venv
        self.python: str = options.python
        self.project: Path = Path(options.project).absolute()
        self.environments: list[Path] = self._get_environments(options.environments)

    def _get_environments(self, environments: list[str]) -> list[Path]:
        if self.project == DEV_NULL and environments:
            msg = "Cannot set environ in independent"
            raise RuntimeError(msg)
        return [self.project.joinpath(environ) for environ in environments]

    def run(self) -> None:
        venv_path = self.base_dir.joinpath(self.venv)
        if venv_path.exists():
            msg = f"Venv {self.venv} already exists, aborting..."
            raise RuntimeError(msg)

        if self.python == "current":
            self.execute(f"python -m venv {venv_path}")
        elif self.python:
            self.execute(f"pyenv shell {self.python}")
            self.execute(f"python -m venv {venv_path}")
        else:
            self.execute(f"mkdir -p {venv_path}")

        if self.project != DEV_NULL:
            self.execute(f"echo {self.project} > {venv_path}/.project")

        for i, environment in enumerate(self.environments):
            if i == 0:
                self.execute(f": > {venv_path}/.environment")
            self.execute(f"echo {environment} >> {venv_path}/.environment")

        self.execute(f"avenv {self.venv}")

        if self.python:
            self.execute("pip install --upgrade pip")
