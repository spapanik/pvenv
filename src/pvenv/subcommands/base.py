from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pyutilkit.term import SGROutput, SGRString

if TYPE_CHECKING:
    from argparse import Namespace
    from pathlib import Path

PREFIX = chr(2)


class BaseCommand:
    __slots__ = ("_prefix", "base_dir", "verbosity")

    def __init__(self, options: Namespace) -> None:
        self._prefix = "_PVENV_ENV"
        self.base_dir: Path = options.base_dir
        self.verbosity: int = options.verbosity

    def run(self) -> None:
        raise NotImplementedError

    @staticmethod
    def print(*args: str) -> None:
        if not os.getenv("PVENV_DEBUG"):
            args = tuple(f"{PREFIX}{arg}" for arg in args)
        print(*args)  # noqa: T201

    @staticmethod
    def output(*args: SGRString, is_error: bool = False) -> None:
        SGROutput(args, is_error=is_error).print(sep=os.linesep)
