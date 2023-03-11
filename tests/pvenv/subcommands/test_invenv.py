import pytest

from pvenv.subcommands.invenv import Command


class TestInVenvCommand:
    @staticmethod
    @pytest.mark.parametrize(
        ("line", "expected"), [("x=1", ["x", "1"]), ("x=a=1", ["x", "a=1"])]
    )
    def test_parse_env_var(line, expected):
        assert Command.parse_env_var(line) == expected
