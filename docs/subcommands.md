# Subcommands

## venv activate/avenv

Activate a virtual environment

usage: venv activate [-h] [-n] venv

positional arguments:
virtual_environment

options:

-h/--help
show this help message and exit
-n/--no-cd
do not cd to the directory associated with this venv

## venv deactivate/dvenv

Deactivate the active virtual environment

usage: venv deactivate [-h]

options:

-h/--help
show this help message and exit

## venv list/lsvenv

List all the virtual environments

usage: venv list [-h]

options:

-h/--help
show this help message and exit

## venv make/mkvenv

Create a new virtual environment

usage: venv make [-h] [-e ENVIRONMENTS] [-P PROJECT] [-p PYTHON] [venv]

positional arguments:
virtual_environment
The name of the virtual environment (defaults to $(pwd))

options:

-h/--help
show this help message and exit
-e/--environments path/to/environment_variables
all environment variables set in path/to/environment_variables will be automatically sourced with `avenv`
-P/--project project path/to/project
cd automatically to path/to/project when using `avenv` (defaults to $(pwd))
-p/--python python_version
current (the default) uses the active one, a version gets passed to pyenv, empty string adds no python

## venv rm/rmvenv

Remove one or more virtual environments

usage: venv rm [-h] [virtual_environments ...]

positional arguments:
[virtual_environments]
the virtual environments to get removed

options:

-h/--help
show this help message and exit
