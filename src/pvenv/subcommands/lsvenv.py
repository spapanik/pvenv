from argparse import Namespace
from pathlib import Path


class Command:
    def __init__(self, base_dir: Path, _options: Namespace):
        self.base_dir = base_dir

    def run(self):
        for directory in sorted(self.base_dir.glob("*")):
            if directory.is_dir():
                print(directory.name)
