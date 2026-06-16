from __future__ import annotations

from pyutilkit.term import SGRString

from pvenv.subcommands.base import BaseCommand


class Command(BaseCommand):
    __slots__ = ()

    def run(self) -> None:
        seen = set()
        for base_dir in self.base_dirs:
            for directory in sorted(base_dir.glob("*")):
                if directory.is_dir() and directory.name not in seen:
                    seen.add(directory.name)
                    SGRString(directory.name).print()
