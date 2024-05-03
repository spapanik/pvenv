# Installation

The easiest way is to use [pipx] to install `pvenv`.

```console
$ pipx install pvenv
```

This is the only officially supported way of installing it.

Alternatively, you can install it with [pip]:

```console
$ pip install --user pvenv
```

The biggest issue with this approach is that you won't have an isolated
environment for `pvenv`, therefore you might run into dependency
conflicts, and so this is neither recommended nor supported.

In both case, after it's installed, you need to source its path to your shell's rc.
You can get the path by executing it:

```console
$ pvenv
```

[pip]: https://pip.pypa.io/en/stable/
[pipx]: https://pypa.github.io/pipx/
[pyenv]: https://github.com/pyenv/pyenv
