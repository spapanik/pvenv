import os
from argparse import Namespace

from pyutilkit.term import SGROutput, SGRString

PREFIX = chr(2)


class BaseCommand:
    def __init__(self, _options: Namespace) -> None:
        self._prefix = "_pvenv_env"

    def run(self) -> None:
        msg = f"{self.__class__.__name__} must implement run"
        raise NotImplementedError(msg)

    @staticmethod
    def print(*args: str) -> None:
        if not os.getenv("PVENV_DEBUG"):
            args = tuple(f"{PREFIX}{arg}" for arg in args)
        print(*args)  # noqa: T201

    @staticmethod
    def output(*args: SGRString, is_error: bool = False) -> None:
        SGROutput(args, is_error=is_error).print(sep=os.linesep)
