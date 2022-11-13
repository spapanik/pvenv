from argparse import Namespace
from pathlib import Path


class Command:
    def __init__(self, base_dir: Path, _options: Namespace):
        self.base_dir = base_dir

    def run(self):
        """function lsvenv {
            local VENV_BASE=~/.local/share/virtualenvs
            for VENV_NAME in $(find ${VENV_BASE} -mindepth 1 -maxdepth 1 -type d | sort); do
                echo $(basename -- $VENV_NAME)
            done
        }"""
        for directory in sorted(self.base_dir.glob("*")):
            if directory.is_dir():
                print(directory.name)
