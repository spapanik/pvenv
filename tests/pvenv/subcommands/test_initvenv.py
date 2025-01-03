from __future__ import annotations

from pvenv.subcommands.initvenv import Command


def test_parse_env_var() -> None:
    assert Command.shell_script().exists()
