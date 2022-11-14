import os
from argparse import Namespace
from pathlib import Path


class Command:
    def __init__(self, _base_dir: Path, options: Namespace):
        self._prefix = "_pvenv_env"
        self.env_vars = options.env_vars
        self.files = options.files

    @staticmethod
    def parse_env_var(line):
        return line.split("=", maxsplit=1)

    def run(self):
        new_vars = {}
        for file in self.files:
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        key, value = self.parse_env_var(line)
                        new_vars[key] = value
        for env_var in self.env_vars:
            key, value = self.parse_env_var(env_var)
            new_vars[key] = value

        if new_vars:
            if self._prefix in os.environ:
                raise RuntimeError("Already in a venv, aborting...")
            print(f"export {self._prefix}=true")
        for key, value in new_vars.items():
            if key in os.environ:
                print(f"export {self._prefix}_{key}={os.getenv(key)}")
            print(f"export {key}={value}")
