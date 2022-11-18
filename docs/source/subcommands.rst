===========
Subcommands
===========

activate
--------

usage: venv activate [-h] [-n] venv

positional arguments:
  venv

options:
  -h, --help   show this help message and exit
  -n, --no-cd


deactivate
----------

usage: venv deactivate [-h]

options:
  -h, --help  show this help message and exit

list
----

usage: venv list [-h]

options:
  -h, --help  show this help message and exit

make
----

usage: venv make [-h] [-e ENVIRONMENTS] [-P PROJECT] [-p PYTHON] [venv]

positional arguments:
  venv

options:
  -h, --help            show this help message and exit
  -e ENVIRONMENTS, --environments ENVIRONMENTS
  -P PROJECT, --project PROJECT
  -p PYTHON, --python PYTHON

rm
--

usage: venv rm [-h] [venvs_to_remove ...]

positional arguments:
  venvs_to_remove

options:
  -h, --help       show this help message and exit
