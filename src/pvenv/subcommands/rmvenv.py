import shutil
from argparse import Namespace
from pathlib import Path


class Command:
    def __init__(self, base_dir: Path, options: Namespace):
        self.base_dir = base_dir
        self.venv_to_remove = options.venvs_to_remove

    def run(self):
        for venv in self.venv_to_remove:
            venv_path = self.base_dir.joinpath(venv)
            if not venv_path.exists():
                print(f"{venv} does not exist, skipping...")
                continue
            try:
                shutil.rmtree(venv_path)
            except (PermissionError, NotADirectoryError):
                print(f"Cannot delete {venv}, skipping...")
                continue

            print(f"{venv} removed successfully!")
