import os
from argparse import Namespace
from pathlib import Path


class Command:
    def __init__(self, _base_dir: Path, _options: Namespace):
        self._prefix = "_pvenv_env"

    def run(self):
        if self._prefix not in os.environ:
            return

        print(f"unset {self._prefix}")
        prefix_size = len(self._prefix) + 1
        for key, value in os.environ.items():
            if key.startswith(f"{self._prefix}_"):
                print(f"export {key[prefix_size:]}={value}")
                print(f"unset {key}")
