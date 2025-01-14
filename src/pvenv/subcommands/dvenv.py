from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pvenv.lib.constants import VENV_ENV_VAR
from pvenv.subcommands.base import BaseCommand

if TYPE_CHECKING:
    from argparse import Namespace


class Command(BaseCommand):
    __slots__ = ()

    def __init__(self, options: Namespace) -> None:
        super().__init__(options)

    def run(self) -> None:
        self.execute("outenv")
        self.execute(f"declare -f deactivate > {os.devnull} && deactivate")
        if os.getenv(VENV_ENV_VAR):
            self.execute(f"unset {VENV_ENV_VAR}")
